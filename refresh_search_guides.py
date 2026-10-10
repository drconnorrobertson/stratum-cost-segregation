#!/usr/bin/env python3
"""Refresh retained commercial guides in source HTML and after every public build."""
from pathlib import Path
import csv, html, json, re, sys

ROOT = Path(__file__).resolve().parent
DATE = '2026-10-09'
SOURCES = {
    'atg': ('IRS cost segregation audit technique guide', 'https://www.irs.gov/pub/irs-pdf/p5653.pdf'),
    'rental': ('IRS Publication 527: residential rental property', 'https://www.irs.gov/publications/p527'),
    'passive': ('IRS Publication 925: passive activity and at-risk rules', 'https://www.irs.gov/publications/p925'),
    'depreciation': ('IRS Publication 946: depreciation and qualified improvement property', 'https://www.irs.gov/publications/p946'),
    'bonus': ('IRS guidance on Notice 2026-11', 'https://www.irs.gov/newsroom/treasury-irs-issue-guidance-on-the-additional-first-year-depreciation-deduction-amended-as-part-of-the-one-big-beautiful-bill'),
    'method': ('IRS Form 3115 instructions', 'https://www.irs.gov/instructions/i3115'),
}

def refresh(target):
    guides = json.loads((ROOT / 'content/search-guide-refresh.json').read_text())
    changed, overrides = [], []
    download = target / 'assets/downloads/commercial-study-cost-bridge.csv'
    download.parent.mkdir(parents=True, exist_ok=True)
    with download.open('w', newline='') as f:
        csv.writer(f).writerow(['Property reference', 'Project or acquisition', 'Legal owner', 'Component and location', 'Function', 'Invoice or closing reference', 'Source cost', 'Credit or reimbursement', 'Amount requiring reconciliation', 'Acquisition date reference', 'Available for use date reference', 'Retained or removed', 'Ownership unresolved', 'Preparer question'])
    for g in guides:
        rel = 'blog/' + g['slug'] + '/'
        file = target / rel / 'index.html'
        text = file.read_text()
        title, desc = g['title'] + ' | Stratum', g['description']
        esc = html.escape
        sections = ''.join('<h2>' + esc(h) + '</h2><p>' + esc(p) + '</p>' for h, p in g['sections'])
        related = [s for s in g['related'] if (target / 'blog' / s / 'index.html').exists()]
        body = '<article class="article" data-search-guide-refresh="20261009">'
        body += '<div class="breadcrumbs"><a href="/">Home</a> / <a href="/blog/">Blog</a></div><h1>' + esc(g['title']) + '</h1>'
        body += '<p class="meta">Updated October 9, 2026 · Stratum Cost Segregation · <a href="/editorial-policy/">Editorial policy</a></p>'
        body += '<p>' + esc(desc) + '</p>' + sections
        body += '<h2>Download the cost and ownership worksheet</h2><p><a href="/assets/downloads/commercial-study-cost-bridge.csv" download>Commercial property cost bridge (CSV)</a>. Use document references rather than account numbers. Complete this blank worksheet privately and share it through your adviser’s secure process. It organizes evidence and does not assign recovery periods.</p>'
        body += '<h2>Primary references</h2><ul>' + ''.join('<li><a href="' + esc(SOURCES[s][1], quote=True) + '">' + esc(SOURCES[s][0]) + '</a></li>' for s in g['sources']) + '</ul><p>References checked October 9, 2026. The examples are illustrative, and the article is educational. Confirm the applicable year and facts with your qualified tax professional.</p>'
        body += '<h2>Continue your property review</h2><ul>' + ''.join('<li><a href="/blog/' + s + '/">' + esc(s.replace('-', ' ').capitalize()) + '</a></li>' for s in related) + '<li><a href="/resources/">Browse property evidence resources</a></li></ul>'
        body += '<div class="cta-banner"><h2>Discuss your property and study scope</h2><p>Bring your cost records, ownership questions, and current depreciation schedule to a cost segregation discovery call.</p><a class="btn btn-gold" href="https://www.aetaxadvisors.com/cost-seg-discovery/?utm_source=stratumcostsegregation.com&amp;utm_medium=referral&amp;utm_campaign=commercial_guides">Book a cost segregation discovery call</a></div></article>'
        text, count = re.subn(r'<article class="article"[^>]*>[\s\S]*?</article>', lambda _: body, text, count=1)
        if count != 1:
            raise ValueError('Missing expected article shell: ' + rel)
        text = re.sub(r'<title>[\s\S]*?</title>', lambda _: '<title>' + esc(title) + '</title>', text, count=1)
        for key, value in [('description', desc), ('og:title', title), ('og:description', desc), ('twitter:title', title), ('twitter:description', desc)]:
            text = re.sub(r'(<meta (?:name|property)="' + re.escape(key) + r'" content=")[^"]*(")', lambda m: m[1] + esc(value, quote=True) + m[2], text)
        def schema(m):
            data = json.loads(m[1])
            for node in data.get('@graph', []):
                if node.get('@type') in ['WebPage', 'BlogPosting', 'Article']:
                    node['description'] = desc
                    node['dateModified'] = DATE
                    if 'headline' in node: node['headline'] = g['title']
                    if 'name' in node: node['name'] = title
                if node.get('@type') == 'BreadcrumbList':
                    node['itemListElement'][-1]['name'] = g['title']
            return '<script type="application/ld+json">' + json.dumps(data, separators=(',', ':')) + '</script>'
        text = re.sub(r'<script type="application/ld\+json">([\s\S]*?)</script>', schema, text)
        file.write_text(text)
        overrides.append({'path': rel + 'index.html', 'article': body,
                          'titleTag': re.search(r'<title>.*?</title>', text).group(0),
                          'meta': [{'key': key, 'tag': re.search(r'<meta (?:name|property)="' + re.escape(key) + r'" content="[^"]*">', text).group(0)} for key in ['description','og:title','og:description','twitter:title','twitter:description']],
                          'schema': re.search(r'<script type="application/ld\+json">[\s\S]*?</script>', text).group(0)})
        changed.append('https://www.stratumcostsegregation.com/' + rel)
    sitemap = target / 'sitemap.xml'
    xml = sitemap.read_text()
    for url in changed:
        pattern = r'(<url>\s*<loc>' + re.escape(url) + r'</loc>)([\s\S]*?)(</url>)'
        def lastmod(m):
            tail = re.sub(r'<lastmod>.*?</lastmod>', '', m[2]).strip()
            return m[1] + '<lastmod>' + DATE + '</lastmod>' + tail + m[3]
        xml, count = re.subn(pattern, lastmod, xml)
        if count != 1: raise ValueError('Expected one sitemap entry: ' + url)
    sitemap.write_text(xml)
    if target == ROOT:
        (ROOT / 'content/search-guide-overrides.json').write_text(json.dumps(overrides, indent=2) + '\n')
    print(json.dumps({'refreshed': changed, 'worksheet': str(download)}))

if __name__ == '__main__':
    refresh(ROOT / 'public' if '--public' in sys.argv else ROOT)
