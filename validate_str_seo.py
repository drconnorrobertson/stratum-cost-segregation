#!/usr/bin/env python3
"""Validate deployable pages, navigation, source coverage and editorial safeguards."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse, unquote, urljoin
from collections import Counter, deque
import json,re,datetime,xml.etree.ElementTree as ET
from build_seo_integrity import site_pages,BASE_URL,ROOT
from audit_content import audit
class Page(HTMLParser):
    def __init__(self):
        super().__init__();self.h1=0;self.canon=[];self.links=[];self.schema=False;self.data='';self.errors=[];self.title=False;self.titles=[];self.desc=[];self.ids=[];self.assets=[];self.blogcards=[];self.robots=[];self.json=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if a.get('id'):self.ids.append(a['id'])
        if tag=='h1':self.h1+=1
        if tag=='title':self.title=True
        if tag=='meta' and a.get('name')=='description':self.desc.append(a.get('content'))
        if tag=='meta' and a.get('name')=='robots':self.robots.append(a.get('content',''))
        if tag=='link' and a.get('rel')=='canonical':self.canon.append(a.get('href'))
        if tag=='a' and 'href' in a:
            self.links.append(a['href'])
            if 'blog-card' in a.get('class','').split():self.blogcards.append(a['href'])
        if tag in ('script','img') and a.get('src'):self.assets.append(a['src'])
        if tag=='link' and a.get('rel')=='stylesheet':self.assets.append(a.get('href',''))
        if tag=='img' and 'alt' not in a:self.errors.append('Image lacks alt attribute')
        if tag=='script' and a.get('type')=='application/ld+json':self.schema=True;self.data=''
    def handle_data(self,s):
        if self.schema:self.data+=s
        if self.title:self.titles.append(s)
    def handle_endtag(self,t):
        if t=='title':self.title=False
        if t=='script' and self.schema:
            try:self.json.append(json.loads(self.data))
            except ValueError:self.errors.append('Invalid JSON-LD')
            self.schema=False

def resolve(p,link):
    u=urlparse(urljoin(BASE_URL+'/'+p.relative_to(ROOT).as_posix(),link))
    if u.scheme not in ('http','https') or u.netloc not in ('www.stratumcostsegregation.com','stratumcostsegregation.com'):return None,u
    target=(ROOT/unquote(u.path).lstrip('/')).resolve()
    if target.is_dir():target=target/'index.html'
    return target,u

def main():
    errors=[];pages={};titles={};descriptions={};edges={}
    for p in site_pages():
        doc=Page();doc.feed(p.read_text());pages[p]=doc
    for p,doc in pages.items():
        rel=p.relative_to(ROOT).as_posix();expected=BASE_URL+'/'+rel.removesuffix('index.html')
        if doc.h1!=1:errors.append(f'{rel}: {doc.h1} H1s')
        if doc.canon!=[expected]:errors.append(f'{rel}: canonical mismatch {doc.canon}')
        if len(doc.desc)!=1 or not doc.desc[0]:errors.append(f'{rel}: missing/duplicate description')
        elif doc.desc[0] in descriptions:errors.append(f'{rel}: duplicate description with {descriptions[doc.desc[0]]}')
        else:descriptions[doc.desc[0]]=rel
        title=''.join(doc.titles)
        if not title:errors.append(f'{rel}: missing title')
        if title in titles:errors.append(f'{rel}: duplicate title with {titles[title]}')
        titles[title]=rel
        if any('noindex' in x for x in doc.robots):errors.append(f'{rel}: canonical page is noindex')
        if len(doc.ids)!=len(set(doc.ids)):errors.append(f'{rel}: duplicate HTML ids')
        if not doc.json:errors.append(f'{rel}: no structured data')
        if any('"reviewedBy"' in json.dumps(j) for j in doc.json):errors.append(f'{rel}: undocumented review attribution')
        errors.extend(f'{rel}: {e}' for e in doc.errors)
        edges[p]=set()
        for link in doc.links+doc.assets:
            target,u=resolve(p,link)
            if target is None or u.path=='/_vercel/insights/script.js':continue
            if not target.exists():errors.append(f'{rel}: broken link/asset {link}');continue
            if target in pages:
                if link in doc.links:edges[p].add(target)
                if u.fragment and unquote(u.fragment) not in pages[target].ids:errors.append(f'{rel}: missing fragment {link}')
            if link in doc.links and u.path.endswith('index.html'):errors.append(f'{rel}: noncanonical internal navigation {link}')
    tree=ET.parse(ROOT/'sitemap.xml');urls=[n.text for n in tree.findall('.//{*}loc')]
    canon={d.canon[0] for d in pages.values() if d.canon}
    if set(urls)!=canon:errors.append(f'Sitemap mismatch missing={canon-set(urls)} extra={set(urls)-canon}')
    if len(urls)!=len(set(urls)):errors.append('Duplicate sitemap URLs')
    visited=set();queue=deque([ROOT/'index.html'])
    while queue:
        p=queue.popleft()
        if p in visited:continue
        visited.add(p);queue.extend(edges.get(p,set())-visited)
    for p in set(pages)-visited:errors.append(f'Orphan/unreachable page: {p.relative_to(ROOT)}')
    cards=pages[ROOT/'blog/index.html'].blogcards
    expected_cards={BASE_URL+'/blog/'+p.parent.name+'/' for p in pages if p.parent.parent==ROOT/'blog'}
    card_urls=[urljoin(BASE_URL+'/blog/',u) for u in cards]
    if set(card_urls)!=expected_cards or len(cards)!=len(expected_cards):errors.append('Blog index must list every article exactly once')
    markets=json.loads((ROOT/'content/markets-researched.json').read_text())
    expected_markets={p.parent.name.removeprefix('cost-segregation-') for p in ROOT.glob('cost-segregation-*/index.html') if p.parent.name not in {'cost-segregation-calculator','cost-segregation-resources'}}
    if {m['slug'] for m in markets}!=expected_markets or len(markets)!=len(expected_markets):errors.append('Every market requires one researched record')
    fields=['angle','local','scope','scenario','question','answer','source_url','source_label','source_checked']
    for m in markets:
        for field in fields:
            if not m.get(field):errors.append(f'{m["slug"]}: missing {field}')
        if not m['source_url'].startswith('https://'):errors.append(f'{m["slug"]}: source must use HTTPS')
        try:datetime.date.fromisoformat(m['source_checked'])
        except ValueError:errors.append(f'{m["slug"]}: invalid source date')
        if len(m['records'])<3:errors.append(f'{m["slug"]}: incomplete records checklist')
        if any(s not in expected_markets or s==m['slug'] for s in m['related']):errors.append(f'{m["slug"]}: invalid related market')
    for field in ['local','scope','scenario']:
        values=[m[field].strip().lower() for m in markets]
        if len(values)!=len(set(values)):errors.append(f'Duplicated market {field}')
    similarity=audit()
    if similarity['flagged_count']:errors.append(f'{similarity["flagged_count"]} market pages need similarity review')
    if errors:
        print('\n'.join(errors));raise SystemExit(1)
    print(f'PASS: {len(pages)} pages; {len(cards)} unique blog cards; {len(markets)} sourced markets; metadata, assets, fragments, canonicals, schema, sitemap, reachability and similarity checks.')
if __name__=='__main__':main()
