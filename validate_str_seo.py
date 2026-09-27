#!/usr/bin/env python3
"""Validate the deployable HTML, schema, internal navigation and sitemap."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse, unquote
import json, xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parent
class Page(HTMLParser):
    def __init__(self):
        super().__init__();self.h1=0;self.canon=[];self.links=[];self.schema=False;self.data='';self.errors=[];self.title=False;self.titles=[];self.desc=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='h1':self.h1+=1
        if tag=='title':self.title=True
        if tag=='meta' and a.get('name')=='description':self.desc.append(a.get('content'))
        if tag=='link' and a.get('rel')=='canonical':self.canon.append(a.get('href'))
        if tag=='a' and 'href' in a:self.links.append(a['href'])
        if tag=='script' and a.get('type')=='application/ld+json':self.schema=True;self.data=''
    def handle_data(self,s):
        if self.schema:self.data+=s
        if self.title:self.titles.append(s)
    def handle_endtag(self,t):
        if t=='title':self.title=False
        if t=='script' and self.schema:
            try:json.loads(self.data)
            except ValueError:self.errors.append('Invalid JSON-LD')
            self.schema=False

def main():
    errors=[];pages={};titles={}
    for p in ROOT.rglob('index.html'):
        doc=Page();doc.feed(p.read_text());pages[p]=doc
        rel=p.relative_to(ROOT).as_posix();expected='https://www.stratumcostsegregation.com/'+rel.removesuffix('index.html')
        if doc.h1!=1:errors.append(f'{rel}: {doc.h1} H1s')
        if doc.canon!=[expected]:errors.append(f'{rel}: canonical mismatch {doc.canon}')
        if len(doc.desc)!=1 or not doc.desc[0]:errors.append(f'{rel}: missing/duplicate description')
        title=''.join(doc.titles)
        if not title:errors.append(f'{rel}: missing title')
        if title in titles:errors.append(f'{rel}: duplicate title with {titles[title]}')
        titles[title]=rel
        errors.extend(f'{rel}: {e}' for e in doc.errors)
        for link in doc.links:
            u=urlparse(link)
            if u.scheme and u.scheme not in ('http','https'):continue
            if u.netloc and u.netloc not in ('www.stratumcostsegregation.com','stratumcostsegregation.com'):continue
            if not u.path:continue
            target=(ROOT/unquote(u.path).lstrip('/')) if u.path.startswith('/') else (p.parent/unquote(u.path))
            if target.is_dir():target=target/'index.html'
            if not target.exists():errors.append(f'{rel}: broken link {link}')
    tree=ET.parse(ROOT/'sitemap.xml');urls=[n.text for n in tree.findall('.//{*}loc')]
    canon={d.canon[0] for d in pages.values() if d.canon}
    if set(urls)!=canon:errors.append(f'Sitemap mismatch missing={canon-set(urls)} extra={set(urls)-canon}')
    if len(urls)!=len(set(urls)):errors.append('Duplicate sitemap URLs')
    if errors:
        print('\n'.join(errors));raise SystemExit(1)
    print(f'PASS: {len(pages)} pages; internal links, unique titles, H1s, descriptions, canonicals, JSON-LD and {len(urls)} sitemap URLs')
if __name__=='__main__':main()
