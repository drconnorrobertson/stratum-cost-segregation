#!/usr/bin/env python3
"""Final editorial, navigation and deployment integrity pass."""
from pathlib import Path
from urllib.parse import urljoin,urlparse,unquote
from html import escape as E
import json,re,xml.etree.ElementTree as ET
from stratum_render import BASE_URL
ROOT=Path(__file__).resolve().parent
DATE='2026-09-27'

def site_pages():
    return sorted(p for p in ROOT.rglob('index.html') if not set(p.relative_to(ROOT).parts)&{'public','.git','node_modules'})

def rewrite_articles(page,links):
    posts=json.loads((ROOT/'content/editorial-refresh.json').read_text())
    titles={p['slug']:p['title'] for p in posts}
    index=ROOT/'blog/index.html';cards=index.read_text()
    for post in posts:
        slug=post['slug'];path=ROOT/'blog'/slug/'index.html'
        previous=path.read_text();published=re.search(r'"datePublished"\s*:\s*"([0-9-]+)"',previous)
        published=published[1] if published else None
        content='<p class="meta">Updated September 27, 2026 · Stratum Cost Segregation</p>'
        content+=''.join('<h2>'+E(h)+'</h2><p>'+E(t)+'</p>' for h,t in post['sections'])
        content+='<h2>Primary references</h2><ul>'+''.join(f'<li><a href="{E(u,quote=True)}">{E(label)}</a></li>' for u,label in post['sources'])+'</ul>'
        content+='<p>Educational information. The return preparer should verify current guidance and apply it to the taxpayer’s facts.</p><h2>Continue your review</h2>'
        related=[]
        for s in post['related']:
            target=ROOT/'blog'/s/'index.html'
            h=re.search('<h1[^>]*>(.*?)</h1>',target.read_text(),re.S)
            label=titles.get(s,re.sub('<[^>]+>','',h[1]) if h else s.replace('-',' ').title())
            related.append(('blog/'+s,label))
        content+=links(related)
        page('blog/'+slug,post['title']+' | Stratum',post['description'],post['title'],content,article=True)
        if published:
            s=path.read_text();s=re.sub(r'"datePublished"\s*:\s*"[0-9-]+"',f'"datePublished": "{published}"',s);path.write_text(s)
        # Both legacy relative and normalized absolute card URLs are supported.
        pattern=r'(<a href="(?:/blog/)?'+re.escape(slug)+r'/(?:index.html)?" class="blog-card"[^>]*>)(.*?)(</a>)'
        def update(m):
            inner=re.sub('<h3>.*?</h3>','<h3>'+E(post['title'])+'</h3>',m[2],flags=re.S)
            inner=re.sub('<p>.*?</p>','<p>'+E(post['description'])+'</p>',inner,flags=re.S)
            return m[1]+inner+m[3]
        cards=re.sub(pattern,update,cards,flags=re.S)
    index.write_text(cards)
    return posts

def refresh_commercial(page,links,metadata):
    p=ROOT/'index.html';s=p.read_text()
    s=metadata(s,'Cost Segregation Company for Rental Property | Stratum','Compare Stratum’s cost segregation process, pricing, and study standards for STR and long-term rental property. Prepare your records and book a discovery call.')
    s=s.replace('STR Cost Segregation Built Around','Cost Segregation Built Around')
    s=s.replace('Stratum provides cost segregation studies for short-term rentals, Airbnb properties, and vacation homes. AE Tax Advisors connects the property analysis to your wider tax strategy.','Stratum provides cost segregation studies for short-term and long-term rental properties. Compare our process, pricing, and study standards, with tax strategy coordination through AE Tax Advisors.')
    p.write_text(s)
    p=ROOT/'services/index.html';s=p.read_text()
    replacements={
      'Maximize depreciation on your Airbnb, VRBO, or vacation rental property. STR investors can often qualify for bonus depreciation to offset active income when they meet material participation requirements. Our studies identify every component eligible for accelerated recovery.':'Analyze the components of an Airbnb, vacation home, or other STR using property-specific records. Your return preparer evaluates bonus eligibility, participation, and other limitations before estimating a usable deduction.',
      'Accelerate deductions on your traditional rental properties with a study tailored to buy-and-hold investors. Even with passive activity limitations, LTR cost segregation creates significant tax-deferred cash flow advantages and portfolio-level depreciation strategies.':'Evaluate a component study for your long-term rental or portfolio. Compare the fee and expected timing benefit with your passive-income position, prior depreciation, state treatment, and expected holding period.',
      'Already own your property and missed years of accelerated depreciation? File IRS Form 3115 to claim prior-year deductions in a single tax year without amending old returns. This is one of the most powerful tools in a real estate investor\'s tax toolkit.':'Already own the property? Provide the existing depreciation schedule. Your preparer determines whether an accounting-method change, amended return, or another approach is appropriate and what a look-back study must document.',
      'Renovating your rental? A partial asset disposition study identifies components being replaced, allowing you to write off their remaining book value in the year of renovation. This pairs perfectly with a cost segregation study on the newly installed improvements.':'Renovating your rental? Document removed components and new work separately. Ask your preparer whether a partial-disposition election applies and what basis evidence is required before assuming a deduction.',
      'Our reports integrate seamlessly with major tax preparation software for efficient implementation.':'Confirm the report format and implementation responsibilities with your preparer before engagement.'}
    for a,b in replacements.items():s=s.replace(a,b)
    p.write_text(s)
    ltr='''<p>A long-term rental study should start with the owner’s cost records and the expected value of changing depreciation timing. The building’s components, prior treatment, and the owner’s ability to use deductions matter more than a generic savings percentage.</p>
<h2>Define the property and eligible cost pool</h2><p>Bring the acquisition documents, land allocation, existing asset schedule, and improvement invoices. Identify each building and unit, shared equipment, tenant-owned improvements, and personal-use areas. The provider should reconcile its analysis to supported costs and explain assumptions or missing records.</p>
<h2>Evaluate the owner’s tax position</h2><p>Ask your return preparer to model the proposed treatment alongside the depreciation available without a study. Include passive-activity and other loss limitations, state adjustments, study and filing fees, expected holding period, and sale consequences. Real estate professional status alone does not settle every participation or loss-limit question. A deduction may be suspended rather than produce current cash savings.</p>
<h2>Keep a portfolio separated by property</h2><p>Similar apartments can have different purchase dates, renovation histories, and ownership. Maintain a schedule by address and a separate reconciliation of shared costs. One invoice or manager account should not cause a component to be counted in multiple buildings. Agree on the report structure and evidence plan before work starts.</p>
<h2>Coordinate an existing-property study</h2><p>Preserve prior returns, elections, and depreciation schedules. Ask the preparer which filing approach fits the facts and which schedules the report needs to supply. A new study does not automatically change the original acquisition date or make current-year bonus rules apply to older assets.</p>
<h2>Choose the provider and confirm the scope</h2><p>Request a written scope, fee, evidence requirements, delivery assumptions, and explanation of CPA follow-up. A preliminary reclassification estimate is not a promise of a usable deduction. Confirm the commercial terms for your property or portfolio during intake.</p>'''
    ltr+=links([('blog/how-to-choose-cost-segregation-company','Compare cost segregation companies'),('pricing','Review pricing'),('blog/passive-activity-loss-rules-cost-segregation','Understand passive-loss limitations'),('blog/str-cost-segregation-multiple-properties','Organize a property portfolio')])
    ltr+='<p>Technical references: <a href="https://www.irs.gov/publications/p925">IRS Publication 925</a> and <a href="https://www.irs.gov/publications/p946">Publication 946</a>.</p>'
    page('long-term-rental-cost-segregation','Long-Term Rental Cost Segregation Studies | Stratum','Evaluate a cost segregation study for a long-term rental or portfolio. Review records, passive-loss considerations, study scope, and CPA coordination.','Long-Term Rental Cost Segregation',ltr)
    p=ROOT/'pricing/index.html';s=p.read_text()
    s=s.replace('The fee for a cost segregation study is tax-deductible as a business expense in the year it is incurred. For most rental property investors, the tax savings from a single cost segregation study exceed the cost of the study by 5x to 20x or more.','Ask your return preparer whether and when the study fee is deductible or capitalized. Compare the written fee and any filing costs with a property-specific projection of the benefit you can actually use.')
    s=s.replace('A $3,500 study on a $400,000 property might identify $80,000 or more in accelerated deductions, resulting in $20,000 to $30,000 in tax savings, depending on your marginal rate. The return on investment is significant and immediate.','Purchase price alone does not establish a worthwhile study. The component evidence, land allocation, prior depreciation, loss limitations, state rules, and expected sale date can change the result. Confirm scope, exclusions, and delivery assumptions in the engagement.')
    p.write_text(s)
    faqs=[
      ('What does a cost segregation study do?','It analyzes supported property costs and components to identify the appropriate depreciation classifications. The owner’s return preparer evaluates implementation and the usable tax benefit; the report does not guarantee savings.'),
      ('How do I choose the best cost segregation company?','Compare qualifications, property evidence, basis reconciliation, report detail, fee and exclusions, CPA handoff, and written examination-support terms. Request a redacted sample and a scope suited to your property.'),
      ('Does every rental benefit from a study?','No. Evaluate the fee, expected timing benefit, loss limitations, state treatment, and likely holding period. A large projected deduction may provide little immediate benefit for a particular owner.'),
      ('What records should I prepare?','Start with closing documents, land-allocation support, existing depreciation, dated photographs, furnishing records, and final improvement invoices. Explain missing evidence and personal-use periods. Listing photographs alone may not support the required scope.'),
      ('What are the current bonus-depreciation rules?','The IRS has issued guidance on restored 100% additional first-year depreciation for eligible property acquired after January 19, 2025. The preparer must verify eligibility, dates, elections, and owner-level limitations; it is not an automatic deduction for an entire building.'),
      ('Can an older property receive a study?','A look-back analysis may be useful. Supply prior schedules and returns so the preparer can determine the appropriate implementation method. Do not assume every case uses Form 3115 or that the study resets acquisition dates.'),
      ('Is more than 100 hours enough for an STR owner?','Not by itself. The comparative test also requires at least as much participation as any other individual, and the preparer must first evaluate the activity rules. Other participation tests and loss limitations may apply.'),
      ('Does the provider need to inspect the property?','Agree on the evidence and inspection approach in the engagement. Photographs, plans, construction records, and public information may be relevant; the property’s complexity and missing evidence determine what additional work is needed.'),
      ('How are fees and delivery dates confirmed?','Use the pricing page as an introduction, then obtain the property-specific written engagement. Confirm required records, exclusions, revision terms, implementation responsibilities, and the effect of incomplete information on delivery.'),
      ('Can you guarantee IRS acceptance?','No. Compare the methodology and supporting evidence, and ask who responds to examination questions and what the contract includes. Marketing labels cannot guarantee an examination outcome.'),
      ('Do location pages represent local offices?','No. They describe nationwide service coverage and local property-planning context. Confirm availability and the required engagement scope during intake.'),
      ('What happens after the report is delivered?','The return preparer reconciles the report to the owner’s records, evaluates elections and applicable limits, and determines the filing approach. Keep the final schedules, supporting records, and filed documents together.')]
    body='<p>Answers to common questions about choosing a provider, preparing records, and coordinating a study with your tax preparer.</p>'
    body+=''.join('<details class="seo-faq"><summary>'+E(q)+'</summary><p>'+E(a)+'</p></details>' for q,a in faqs)
    body+='<h2>Plan your next step</h2>'+links([('blog/how-to-choose-cost-segregation-company','Use the company comparison guide'),('str-study-planner','Build a preparation checklist'),('pricing','Review study pricing'),('locations','Find a local market guide')])
    body+='<p>References: <a href="https://www.irs.gov/pub/irs-drop/n-26-11.pdf">Notice 2026-11</a> and <a href="https://www.irs.gov/publications/p925">Publication 925</a>.</p>'
    page('faq','Cost Segregation Questions & Provider Checklist | Stratum','Answers about cost segregation company selection, study records, fees, bonus depreciation, material participation, and CPA implementation.','Cost Segregation Questions',body)
    for slug in ['faq','long-term-rental-cost-segregation']:
        p=ROOT/slug/'index.html';s=p.read_text();s=re.sub('<div class="breadcrumbs">.*?</div>','<div class="breadcrumbs"><a href="/">Home</a></div>',s,count=1,flags=re.S);p.write_text(s)


def normalize_and_clean(posts):
    # Targeted removal of unsupported certainty; source authorship is not a tax-review certification.
    corrections={
      'IRS-approved tax strategy':'property analysis method',
      'audit-proof':'documented', 'Audit-Proof':'Documented',
      'For properties in the $200,000 to $400,000 range, cost segregation is almost always worth the analysis.':'Evaluate the study fee against a property-specific estimate of the benefit the owner can actually use.',
      'If your property has a depreciable basis above $150,000, the math almost always works in your favor.':'Depreciable basis alone does not establish value; compare the fee with the incremental usable benefit and expected holding period.',
      'Owners in this position frequently clear the 100-hour threshold without effort.':'Owners should document actual participation and have their preparer evaluate the applicable test rather than assume qualification.',
      'subject to the current phase-down schedule':'subject to applicable acquisition-date, service-date, eligibility, and election rules',
      'more than any other individual':'at least as much as any other individual',
      'more time than anyone else':'at least as much time as any other individual',
      'more-than-anyone-else test':'comparative participation test',
      'For an investor weighing whether a charger installation still pencils out without the credit, the answer is almost always yes, and the depreciation benefit alone is typically worth several times what the credit would have provided.':'Evaluate the charger project using its actual installed cost, operating economics, applicable tax treatment, and the owner’s usable benefit. Depreciation does not automatically replace an unavailable credit.',
      'The key threshold is whether the tax savings in year one meaningfully exceed the study cost, which is almost always the case for self-storage purchased at $500,000 or more in total value.':'Compare the study cost with a property-specific projection of incremental usable benefit. Purchase price alone does not establish a favorable result.'}
    for p in site_pages()+[ROOT/'404.html']:
        s=p.read_text()
        for a,b in corrections.items():s=s.replace(a,b)
        s=re.sub(r'Tax review by <a href="https://www.aetaxadvisors.com/">AE Tax Advisors Tax Team</a>(?: &middot; Reviewed [^<]*?)?(?= &middot;|</div>)','Educational content; consult your tax preparer',s)
        s=re.sub(r'Tax content is reviewed by the <a href="https://www.aetaxadvisors.com/">AE Tax Advisors Tax Team</a>\.(?: Review identifies technical issues and areas where property owners should seek advice for their specific facts\.)?','Tax conclusions require review by the owner’s return preparer. A professional-review attribution is added only when an actual review is documented.',s)
        def clean_schema(m):
            obj=json.loads(m[1])
            def walk(v):
                if isinstance(v,dict):
                    v.pop('reviewedBy',None)
                    for x in v.values():walk(x)
                elif isinstance(v,list):
                    for x in v:walk(x)
            walk(obj)
            return '<script type="application/ld+json">'+json.dumps(obj,ensure_ascii=False,separators=(',',':'))+'</script>'
        s=re.sub(r'<script type="application/ld\+json">(.*?)</script>',clean_schema,s,flags=re.S)
        # Resolve local links against their source page and point directly at canonical directory URLs.
        base=BASE_URL+'/'+p.relative_to(ROOT).as_posix()
        def href(m):
            raw=m[1];url=urlparse(urljoin(base,raw))
            if url.netloc not in ('www.stratumcostsegregation.com','stratumcostsegregation.com'):return m[0]
            target=ROOT/unquote(url.path).lstrip('/')
            if url.path.endswith('/index.html') and target.is_file():
                path=url.path.removesuffix('index.html')
                if url.query:path+='?'+url.query
                if url.fragment:path+='#'+url.fragment
                return 'href="'+E(path,quote=True)+'"'
            return m[0]
        s=re.sub(r'href="([^"]+)"',href,s)
        # Shared discovery links remain short, descriptive and useful to readers.
        s=re.sub(r'<div id="str-footer-links".*?</div>\n?','',s,flags=re.S)
        footerlinks='<div id="str-footer-links" class="container"><h4>Planning resources</h4><ul><li><a href="/blog/how-to-choose-cost-segregation-company/">Compare providers</a></li><li><a href="/locations/">Market guides</a></li><li><a href="/str-study-planner/">Study preparation checklist</a></li><li><a href="/str-cost-segregation-resources/">Rental property resources</a></li><li><a href="/booking/">Consultation preparation</a></li><li><a href="/privacy/">Privacy notice</a></li></ul></div>'
        s=s.replace('<div class="footer-bottom">',footerlinks+'\n<div class="footer-bottom">',1)
        s=re.sub(r'(style\.css)(?:\?v=[^" ]*)?(?=")',r'\1?v=20260927-2',s)
        if p==ROOT/'privacy/index.html' and 'application/ld+json' not in s:
            s=s.replace('</head>','<script type="application/ld+json">'+json.dumps({'@context':'https://schema.org','@type':'WebPage','name':'Privacy Notice','url':BASE_URL+'/privacy/'},separators=(',',':'))+'</script></head>')
        if p.name=='404.html':
            s=re.sub(r'<link rel="canonical"[^>]+>','',s)
            if 'name="robots"' not in s:s=s.replace('</head>','<meta name="robots" content="noindex,follow">\n</head>')
        p.write_text('\n'.join(line.rstrip() for line in s.splitlines())+'\n')


def apply_integrity(page,links,metadata):
    posts=rewrite_articles(page,links)
    refresh_commercial(page,links,metadata)
    improve_blog_index(metadata)
    normalize_and_clean(posts)
    print(f'Editorial integrity: {len(posts)} refreshed articles, commercial/FAQ corrections, canonical navigation, transparent review attribution.')


def finalize_sitemap():
    # Dates are editorial records, not build timestamps. Unknown dates are omitted.
    revised={f'cost-segregation-{m["slug"]}/' for m in json.loads((ROOT/'content/markets-researched.json').read_text())}
    revised|={f'blog/{p["slug"]}/' for p in json.loads((ROOT/'content/editorial-refresh.json').read_text())}
    revised|={'','services/','pricing/','faq/','long-term-rental-cost-segregation/','locations/'}
    ET.register_namespace('','http://www.sitemaps.org/schemas/sitemap/0.9')
    root=ET.Element('{http://www.sitemaps.org/schemas/sitemap/0.9}urlset')
    for p in site_pages():
        path=p.relative_to(ROOT).as_posix().removesuffix('index.html')
        node=ET.SubElement(root,'url');ET.SubElement(node,'loc').text=BASE_URL+'/'+path
        if path in revised:ET.SubElement(node,'lastmod').text=DATE
    ET.indent(root,space='  ')
    ET.ElementTree(root).write(ROOT/'sitemap.xml',encoding='utf-8',xml_declaration=True)


def improve_blog_index(metadata):
    p=ROOT/'blog/index.html';s=p.read_text()
    s=metadata(s,'Cost Segregation Guides & Company Comparisons | Stratum','Explore cost segregation company comparisons, property-study records, local market guides, and tax topics for short-term and long-term rental owners.')
    # Replace the legacy search control and its handler with one accessible search.
    s=re.sub(r'<label for="guide-search".*?</label>\s*<input id="guide-search"[^>]*>\s*<p id="guide-count".*?</p>', '', s, flags=re.S)
    s=re.sub(r"<script>\s*\(function\(\)\{\s*var input=document.getElementById\('guide-search'\);.*?</script>", '', s, flags=re.S)
    # Remove duplicate cards left by older relative-link generators and update every card from its destination.
    seen=set()
    def card(m):
        url=urlparse(urljoin(BASE_URL+'/blog/',m[1])).path
        slug=url.removesuffix('index.html').strip('/').split('/')[-1]
        if slug in seen:return ''
        seen.add(slug)
        target=ROOT/'blog'/slug/'index.html'
        if not target.exists():return m[0]
        doc=target.read_text();heading=re.search('<h1[^>]*>(.*?)</h1>',doc,re.S)
        desc=re.search('<meta name="description" content="([^"]*)"',doc)
        inner=m[2]
        if heading:inner=re.sub('<h3>.*?</h3>','<h3>'+heading[1]+'</h3>',inner,flags=re.S)
        if desc:inner=re.sub('<p>.*?</p>','<p>'+desc[1]+'</p>',inner,flags=re.S)
        return '<a href="/blog/'+slug+'/" class="blog-card" style="text-decoration:none;">'+inner+'</a>'
    s=re.sub(r'<a href="([^"]+)" class="blog-card"[^>]*>(.*?)</a>',card,s,flags=re.S)
    s=re.sub(r'<section id="blog-find".*?</section>\n?','',s,flags=re.S)
    block='<section id="blog-find" class="section"><div class="container"><h2>Find a guide for your next decision</h2><p>Start with <a href="/blog/how-to-choose-cost-segregation-company/">comparing providers</a>, <a href="/str-study-planner/">preparing records</a>, or <a href="/locations/">your property market</a>.</p><label for="blog-search">Search articles<input id="blog-search" type="search" placeholder="Try bonus, condo, or pricing"></label><p id="blog-count" role="status" aria-live="polite"></p><noscript><p>All articles are listed below. Search requires JavaScript.</p></noscript></div></section>'
    s=re.sub(r'(<div class="blog-grid"[^>]*>)',block+r'\n\1',s,count=1)
    if '/assets/blog-search.js' not in s:s=s.replace('</body>','<script defer src="/assets/blog-search.js"></script>\n</body>')
    p.write_text(s)
