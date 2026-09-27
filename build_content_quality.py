#!/usr/bin/env python3
"""Curated market/guide layer. Called last by build_str_seo.py."""
from pathlib import Path
from collections import defaultdict
import csv, html, json, re
from stratum_render import BASE_URL
from build_new_content import update_blog_index
ROOT=Path(__file__).resolve().parent
E=html.escape
DATE='2026-09-27'
STATE_NAMES={'AL':'Alabama','AZ':'Arizona','CA':'California','CO':'Colorado','DC':'District of Columbia','FL':'Florida','GA':'Georgia','HI':'Hawaii','ID':'Idaho','IL':'Illinois','IN':'Indiana','KY':'Kentucky','LA':'Louisiana','MA':'Massachusetts','MD':'Maryland','MI':'Michigan','MN':'Minnesota','MO':'Missouri','MT':'Montana','NC':'North Carolina','NE':'Nebraska','NJ':'New Jersey','NM':'New Mexico','NV':'Nevada','NY':'New York','OH':'Ohio','OK':'Oklahoma','OR':'Oregon','PA':'Pennsylvania','RI':'Rhode Island','SC':'South Carolina','TN':'Tennessee','TX':'Texas','UT':'Utah','VA':'Virginia','WA':'Washington','WI':'Wisconsin','WY':'Wyoming'}

def load(name):return json.loads((ROOT/'content'/name).read_text())
def bullets(items):return '<ul>'+''.join('<li>'+E(t)+'</li>' for t in items)+'</ul>'
def css_link(path):
    p=ROOT/path/'index.html';s=p.read_text().replace('</head>','<link rel="stylesheet" href="/assets/str-resources.css">\n</head>');p.write_text(s)

def downloads():
    root=ROOT/'assets/downloads';root.mkdir(parents=True,exist_ok=True)
    specs={
      'furnished-str-inventory.csv':['Property ID','Room or area','Item description','Quantity','Acquired from seller or later purchase','Document reference','Supported cost if known','Value unresolved','Retained replaced or excluded','Replacement document','Available for intended use date','Question for preparer'],
      'str-improvement-reconciliation.csv':['Property ID','Project ID','Work area','Component or scope','Vendor','Contract reference','Original contract amount','Approved changes','Credits','Final project cost','Payments reconciled','Work completion date','Available for intended use date','Replaced asset reference','Unresolved question'],
      'str-portfolio-records.csv':['Property ID','Ownership entity','Address reference','Closing file reference','Basis schedule status','Inventory status','Improvement file status','Prior depreciation schedule status','Rental use timeline status','Manager records status','Outstanding records','Responsible person','Target follow-up date']
    }
    for name,headers in specs.items():
        with (root/name).open('w',newline='') as f:csv.writer(f).writerow(headers)

def render_planner(page):
    body='''<p>Build a document checklist for your property. The choices below organize a study discussion; they do not determine tax eligibility or estimate a deduction. No address, income, or account information is requested.</p>
<form id="study-planner" class="study-planner">
<fieldset><legend>Which property facts apply?</legend>
<label><input type="checkbox" name="facts" value="furnished"> The purchase included furniture</label>
<label><input type="checkbox" name="facts" value="condo"> It is a condominium or has shared amenities</label>
<label><input type="checkbox" name="facts" value="renovation"> There are renovations or later improvements</label>
<label><input type="checkbox" name="facts" value="personal"> There is personal use or owner-occupied space</label>
<label><input type="checkbox" name="facts" value="manager"> A property manager holds records</label>
<label><input type="checkbox" name="facts" value="portfolio"> I am preparing more than one property</label>
<label><input type="checkbox" name="facts" value="existing"> The property already has a depreciation schedule</label>
</fieldset>
<div class="planner-actions"><button type="button" class="btn btn-gold" id="download-checklist">Download my checklist</button><button type="button" class="btn btn-outline" id="print-checklist">Print</button><button type="reset" class="btn btn-outline">Reset</button></div></form>
<p id="planner-status" role="status" aria-live="polite">6 starting records to gather.</p>
<section id="planner-results" aria-label="Your document checklist"><h2>Your study preparation checklist</h2><ul id="checklist-items"><li>Closing statement and executed purchase agreement</li><li>Supported land and building basis information for preparer review</li><li>Property identity and actual ownership interest</li><li>Timeline of acquisition and availability for rental use</li><li>Current photographs or available plans</li><li>Questions about study scope, fee, deliverables, and CPA coordination</li></ul></section>
<noscript><p>JavaScript is off. Use the full printable checklist below; the downloadable spreadsheet templates also work without JavaScript.</p></noscript>
<details><summary>View all scenario-specific records</summary><div id="all-records"></div></details>
<h2>Download blank working templates</h2><ul><li><a href="/assets/downloads/furnished-str-inventory.csv" download>Furnished-property inventory (CSV)</a></li><li><a href="/assets/downloads/str-improvement-reconciliation.csv" download>Improvement and date reconciliation (CSV)</a></li><li><a href="/assets/downloads/str-portfolio-records.csv" download>Portfolio record index (CSV)</a></li></ul><p>These are organizing worksheets, not completed valuations or tax schedules. Fill them privately and use your adviser’s secure document-transfer process.</p>
<h2>Read the preparation guides</h2><p><a href="/str-cost-segregation-resources/">Choose a guide for your property situation</a> or <a href="/locations/">find local service-area resources</a>.</p>'''
    groups={
     'furnished':('Furnished purchase',['Executed seller inventory and bill of sale','Closing credits and excluded items','Post-closing furniture receipts and replacement log']),
     'condo':('Condo or shared property',['Deed and condominium declaration','Association assessment notices and project descriptions','Owner-versus-association asset inventory']),
     'renovation':('Renovations',['Final contractor scope and approved change orders','Payment reconciliation including deposits and credits','Improvement completion dates and replaced-asset records']),
     'personal':('Personal or mixed use',['Floor plan of guest-only, owner-only, and shared space','Rental and personal-use calendar','Conversion history and basis questions for the preparer']),
     'manager':('Manager records',['Vendor invoices underlying capital charges','Management agreement and asset-ownership explanation','Manager inventory and rental-availability timeline']),
     'portfolio':('Multiple properties',['Entity-to-property identifier map','Separate basis and acquisition file for each property','Bulk purchase allocations and furniture-transfer register']),
     'existing':('Previously depreciated property',['Latest depreciation and fixed-asset schedules','Prior study, if any, and implementation records','List of assets retained, removed, replaced, or transferred'])
    }
    all_records=''.join('<h3>'+E(label)+'</h3>'+bullets(records) for label,records in groups.values())
    body=body.replace('<div id="all-records"></div>','<div id="all-records">'+all_records+'</div>')
    page('str-study-planner','STR Study Preparation Planner & Checklists | Stratum','Build a tailored cost segregation document checklist for furnished rentals, condos, renovations, personal use, managers, and property portfolios.','Prepare Your STR Cost Segregation Study',body)
    p=ROOT/'str-study-planner/index.html';s=p.read_text().replace('</body>','<script defer src="/assets/str-study-planner.js"></script>\n</body>');p.write_text(s);css_link('str-study-planner')
    (ROOT/'assets/str-study-planner.js').write_text('''"use strict";
(function(){
 const form=document.getElementById('study-planner');if(!form)return;
 const list=document.getElementById('checklist-items');
 const base=Array.from(list.children).map(item=>item.textContent);
 const groups='''+json.dumps(groups)+''';
 function items(){
  return base.concat(Array.from(form.querySelectorAll('input:checked')).flatMap(input=>groups[input.value][1]));
 }
 function render(){
  const records=items();list.replaceChildren();
  for(const record of records){const li=document.createElement('li');li.textContent=record;list.appendChild(li);}
  document.getElementById('planner-status').textContent=records.length+' records or questions on your checklist. This is document planning, not an eligibility result.';
 }
 form.addEventListener('change',render);
 form.addEventListener('submit',event=>event.preventDefault());
 form.addEventListener('reset',()=>setTimeout(render,0));
 document.getElementById('print-checklist').addEventListener('click',()=>window.print());
 document.getElementById('download-checklist').addEventListener('click',()=>{
  const content='STR study preparation checklist\\n\\n'+items().map(item=>'[ ] '+item).join('\\n')+'\\n\\nOrganizing aid only; confirm the scope and tax treatment with your advisers.\\n';
  const url=URL.createObjectURL(new Blob([content],{type:'text/plain;charset=utf-8'}));
  const a=document.createElement('a');a.href=url;a.download='str-study-checklist.txt';document.body.appendChild(a);a.click();a.remove();setTimeout(()=>URL.revokeObjectURL(url),1000);
 });
})();
''')

def render_directory(page,links,markets):
    enhanced={m['slug']:m for m in markets};groups=defaultdict(list)
    for p in ROOT.glob('cost-segregation-*/index.html'):
        s=p.read_text();m=re.search(r'<h1>(.*?)</h1>',s,re.S)
        if not m:continue
        h=html.unescape(re.sub('<[^>]+>','',m[1]));m=re.search(r'(?:STR )?Cost Segregation in (.*), ([A-Z]{2})',h)
        if m:groups[m[2]].append((p.parent.name,m[1]))
    body='''<p>Choose the state where the property is located. A guide describes nationwide service coverage, not a local branch office. Each guide includes a checked local resource and a distinct property-study question.</p><label class="market-search" for="market-search">Find a city, region, or state<input type="search" id="market-search" placeholder="Try Gatlinburg, Florida, or condo"></label><p id="market-count" role="status" aria-live="polite"></p><noscript><p>Search requires JavaScript; all market links remain available below by state.</p></noscript>'''
    for code,entries in sorted(groups.items(),key=lambda x:STATE_NAMES.get(x[0],x[0])):
        body+=f'<section class="market-state"><h2>{E(STATE_NAMES.get(code,code))}</h2><ul class="market-list">'
        for slug,city in sorted(entries,key=lambda x:x[1]):
            data=enhanced.get(slug.removeprefix('cost-segregation-'))
            desc=data['angle'] if data else 'Cost segregation service overview'
            search=f'{city} {code} {STATE_NAMES.get(code,code)} {desc}'.lower()
            body+=f'<li class="market-entry" data-search="{E(search,quote=True)}"><a href="/{slug}/">{E(city)}, {code}</a><span>{E(desc)}</span></li>'
        body+='</ul></section>'
    body+='<h2>Start with your property records</h2>'+links([('str-study-planner','Build a study checklist'),('str-cost-segregation-resources','Browse practical STR guides')])
    page('locations','STR Cost Segregation Locations & Markets | Stratum','Find vacation-rental cost segregation service areas by city or state, with local planning sources and property-specific study questions.','STR Cost Segregation Locations',body)
    p=ROOT/'locations/index.html';s=p.read_text().replace('</body>','<script defer src="/assets/market-search.js"></script>\n</body>');p.write_text(s);css_link('locations')
    (ROOT/'assets/market-search.js').write_text('''"use strict";
(function(){
 const input=document.getElementById('market-search');if(!input)return;
 const entries=Array.from(document.querySelectorAll('.market-entry'));
 function filter(){
  const terms=input.value.toLowerCase().trim().split(/\\s+/).filter(Boolean);let count=0;
  for(const entry of entries){entry.hidden=!terms.every(term=>entry.dataset.search.includes(term));if(!entry.hidden)count++;}
  for(const group of document.querySelectorAll('.market-state'))group.hidden=!Array.from(group.querySelectorAll('.market-entry')).some(entry=>!entry.hidden);
  document.getElementById('market-count').textContent=count?count+(count===1?' service area shown.':' service areas shown.'):'No matching service areas. Try a state or another city.';
 }
 input.addEventListener('input',filter);filter();
})();
''')

def apply_quality(page,links):
    markets=load('markets-researched.json');guides=load('str-practical-guides.json');titles={g['slug']:g['title'] for g in guides}
    for m in markets:
        for field in ['local','scope','scenario','question','answer','source_label','source_checked']:
            if not m.get(field):raise ValueError(f'Missing {field}: {m["slug"]}')
        if not m['source_url'].startswith('https://') or len(m['records'])<3:
            raise ValueError(f'Incomplete researched market: {m["slug"]}')
        desc=f'{m["city"]} STR cost segregation: {m["angle"].lower()}. Review local resources, study records, and a property-specific planning example.'
        body='<p class="meta">Stratum Cost Segregation · Updated September 27, 2026</p>'
        body+=f'<h2>{E(m["angle"])}</h2><p>{E(m["local"])} <a href="{E(m["source_url"],quote=True)}">{E(m["source_label"])}</a>.</p>'
        body+=f'<h2>Define the property study</h2><p>{E(m["scope"])}</p><h2>Records that resolve the main questions</h2>'+bullets(m['records'])
        body+=f'<h2>A scoping example</h2><p>{E(m["scenario"])}</p><p class="meta">Illustrative documentation scenario; not a completed client study or a savings estimate.</p>'
        body+=f'<h2>{E(m["question"])}</h2><p>{E(m["answer"])}</p>'
        body+='<h2>Prepare for a Stratum study</h2><p>Stratum provides nationwide property-study services, with discovery calls through AE Tax Advisors. Confirm the engagement scope, fee, evidence requirements, and CPA handoff. A service-area page does not represent a local office. Local operating approval and federal depreciation are separate questions.</p>'
        body+=links([('str-study-planner','Build your document checklist'),('blog/'+m['topic'],titles[m['topic']]),('short-term-rental-cost-segregation','Understand the STR study service'),('blog/best-str-cost-segregation-company','Compare study providers')])
        if m['related']:
            body+='<h2>Related service areas</h2>'+links([('cost-segregation-'+s,s.rsplit('-',1)[0].replace('-',' ').title()) for s in m['related']])
        else:
            body+='<h2>Explore service coverage</h2><p><a href="/locations/">Browse market guides by state</a></p>'
        body+='<p class="meta">Local source checked September 27, 2026. Confirm current address-specific requirements with the relevant authority. This page provides planning information, not a determination of rental eligibility or tax treatment.</p>'
        page('cost-segregation-'+m['slug'],f'STR Cost Segregation in {m["city"]}, {m["state"]} | Stratum',desc,f'STR Cost Segregation in {m["city"]}, {m["state"]}',body,area=f'{m["city"]}, {m["state"]}')
    downloads()
    cards=[]
    for g in guides:
        body='<p class="meta">Published September 27, 2026 by Stratum Cost Segregation</p>'+''.join('<h2>'+E(h)+'</h2><p>'+E(p)+'</p>' for h,p in g['sections'])
        body+=f'<p><a href="/assets/downloads/{g["download"]}" download>{E(g["download_label"])}</a>. Blank organizing worksheet; no login required.</p><p>Technical reference: <a href="{g["source"]}">{E(g["source_label"])}</a>. Templates and examples are organizational aids, not tax conclusions.</p>'
        body+='<h2>Apply the checklist to your property</h2>'+links([('str-study-planner','Build a tailored preparation checklist')]+[('cost-segregation-'+s,s.rsplit('-',1)[0].replace('-',' ').title()+' study questions') for s in g['markets']])
        page('blog/'+g['slug'],g['title']+' | Stratum',g['description'],g['title'],body,article=True)
        cards.append({**g,'date':'September 27, 2026'})
    update_blog_index(cards)
    render_planner(page);render_directory(page,links,markets)
    resource_body='<p>Start with the situation that matches your property. Each practical guide explains the records to gather and provides a blank worksheet where useful.</p>'+links([('str-study-planner','Build a tailored study checklist'),('blog/best-str-cost-segregation-company','Choose a cost segregation provider'),('blog/str-cost-segregation-proposal-comparison','Compare proposals')])
    for g in guides:resource_body+='<h2><a href="/blog/'+g['slug']+'/">'+E(g['title'])+'</a></h2><p>'+E(g['description'])+'</p>'
    resource_body+='<h2>Tax concepts to discuss with your preparer</h2>'+links([('blog/str-100-hour-material-participation-test','Material participation'),('blog/bonus-depreciation-2026-rental-property','Bonus depreciation'),('blog/depreciation-recapture-cost-segregation','Recapture on sale'),('blog/when-not-to-do-cost-segregation','When a study may not fit'),('locations','Find your local market guide')])
    page('str-cost-segregation-resources','STR Cost Segregation Guides & Resources | Stratum','Practical STR study guides, blank inventory worksheets, renovation records, and a preparation planner for vacation-rental property owners.','STR Cost Segregation Resource Center',resource_body)
    # Add prominent discovery links without replacing existing business flows.
    feature='<section id="str-practical-resources" class="section"><div class="container"><h2>Prepare your STR property for a study</h2><p>Organize a furnished purchase, condo, renovation, or portfolio before comparing study proposals.</p>'+links([('str-study-planner','Build your study checklist'),('str-cost-segregation-resources','Read the practical guides'),('locations','Find a market by city or state')])+'</div></section>'
    for p in [ROOT/'index.html',ROOT/'blog/index.html',ROOT/'short-term-rental-cost-segregation/index.html']:
        s=p.read_text();s=re.sub(r'<section id="str-practical-resources".*?</section>\n?','',s,flags=re.S)
        if p==ROOT/'index.html':s=s.replace('<section class="trust-strip',feature+'\n<section class="trust-strip',1) if '<section class="trust-strip' in s else s.replace('<footer class="footer">',feature+'\n<footer class="footer">',1)
        elif p==ROOT/'blog/index.html':
            s=re.sub(r'(<div class="blog-grid"[^>]*>)',feature+r'\n\1',s,count=1)
        else:s=s.replace('<footer class="footer">',feature+'\n<footer class="footer">',1)
        p.write_text(s)
    # The shared helper uses locations as its default parent. Resource and service pages are root-level.
    for slug in ['locations','str-cost-segregation-resources','str-study-planner','short-term-rental-cost-segregation']:
        p=ROOT/slug/'index.html';s=p.read_text();s=re.sub(r'<div class="breadcrumbs">.*?</div>',f'<div class="breadcrumbs"><a href="/">Home</a> &raquo; <span>{E(slug.replace("-"," ").title())}</span></div>',s,count=1,flags=re.S);p.write_text(s)
    print(f'Curated layer: {len(markets)} market guides, {len(guides)} practical articles, planner and 3 preparation downloads.')

def apply_buyer_focus(page,links):
    slug='blog/how-to-choose-cost-segregation-company'
    title='How to Choose the Best Cost Segregation Company'
    desc='Compare cost segregation companies by study evidence, fees, qualifications, and CPA support. Use Stratum’s buyer checklist and provider comparison worksheet.'
    page(slug,'Best Cost Segregation Company: Compare Providers | Stratum',desc,title,(ROOT/'content/company-buyer-guide.html').read_text(),article=True)
    css_link(slug)
    # This is a revision of an existing January article, not a newly published article.
    p=ROOT/slug/'index.html';s=p.read_text().replace('"datePublished": "2026-09-27"','"datePublished": "2026-01-01"');p.write_text(s)
    with (ROOT/'assets/downloads/cost-seg-company-comparison.csv').open('w',newline='') as f:
        writer=csv.writer(f);writer.writerow(['Provider','Offering quoted','Preparer and reviewer','Inspection and evidence','Basis reconciliation','Report sample received','Fee and exclusions','CPA coordination','Audit support terms','Timing assumptions','Unanswered questions','Proposal reference'])
    # Update the existing blog card instead of creating a second URL for the same intent.
    p=ROOT/'blog/index.html';s=p.read_text()
    pattern=r'(<a href="how-to-choose-cost-segregation-company/index.html" class="blog-card"[^>]*>)(.*?)(</a>)'
    def card(m):
        inner=re.sub(r'<h3>.*?</h3>','<h3>'+E(title)+'</h3>',m[2],flags=re.S)
        inner=re.sub(r'<p>.*?</p>','<p>'+E(desc)+'</p>',inner,flags=re.S)
        return m[1]+inner+m[3]
    s=re.sub(pattern,card,s,flags=re.S);p.write_text(s)
    panel='<section id="company-selection-guide" class="section"><div class="container"><h2>What makes a cost segregation company the best fit?</h2><p>Compare the study evidence, written scope, fee, and CPA support before choosing a provider.</p>'+links([(slug,'How to choose the best cost segregation company'),('reviews','Review Stratum study standards'),('pricing','Understand study pricing')])+'</div></section>'
    selected=['index.html','services/index.html','pricing/index.html','reviews/index.html','how-it-works/index.html','short-term-rental-cost-segregation/index.html','long-term-rental-cost-segregation/index.html','str-cost-segregation-resources/index.html','blog/best-str-cost-segregation-company/index.html','blog/str-cost-segregation-proposal-comparison/index.html','blog/cost-segregation-study-cost-pricing/index.html','blog/diy-vs-professional-cost-segregation/index.html','blog/irs-audit-technique-guide-cost-segregation/index.html']
    for name in selected:
        p=ROOT/name;s=p.read_text();s=re.sub(r'<section id="company-selection-guide".*?</section>\n?','',s,flags=re.S)
        if name=='index.html':
            marker='<section id="str-practical-resources"'
            s=s.replace(marker,panel+'\n'+marker,1)
        else:s=s.replace('<footer class="footer">',panel+'\n<footer class="footer">',1)
        p.write_text(s)
    # Include the broader comparison in the new market guides, keeping STR-specific reading as a separate intent.
    for m in load('markets-researched.json'):
        p=ROOT/('cost-segregation-'+m['slug'])/'index.html';s=p.read_text();s=s.replace('<a href="/blog/best-str-cost-segregation-company/">Compare study providers</a>','<a href="/'+slug+'/">Compare cost segregation companies</a>');p.write_text(s)

    # Version the revised shared stylesheet so returning readers receive responsive fixes.
    for p in ROOT.rglob('index.html'):
        if 'public' in p.relative_to(ROOT).parts:continue
        s=p.read_text();s=re.sub(r'href="([^"?]*style\.css)(?:\?v=[^" ]*)?"',r'href="\1?v=20260927"',s);p.write_text(s)
