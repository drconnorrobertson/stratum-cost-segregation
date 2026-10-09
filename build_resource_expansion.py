#!/usr/bin/env python3
"""Build 500 task-specific reference guides, navigation, and evidence worksheets.

Editorial inputs are tracked alongside this generator. No client outcomes,
professional review, credentials, or universal recovery periods are invented.
"""
from pathlib import Path
from html import escape as E
import json, re, xml.etree.ElementTree as ET
from urllib.parse import urljoin, urlparse
from stratum_render import nav, footer, SCRIPTS, ANALYTICS, BASE_URL, AE_BOOKING

ROOT=Path(__file__).resolve().parent
DATE='2026-10-09'
DATE_LABEL='October 9, 2026'
manifest=[]
def slug(t): return re.sub(r'[^a-z0-9]+','-',t.lower()).strip('-')
def p(t): return '<p>'+E(t)+'</p>'
def section(h,*texts): return '<section><h2>'+E(h)+'</h2>'+''.join(p(t) for t in texts)+'</section>'
def ul(items): return '<ul>'+''.join('<li>'+E(t)+'</li>' for t in items)+'</ul>'
def table(rows):
    return '<div class="table-scroll"><table><thead><tr><th scope="col">Field</th><th scope="col">What to record</th></tr></thead><tbody>'+''.join('<tr><th scope="row">'+E(a)+'</th><td>'+E(b)+'</td></tr>' for a,b in rows)+'</tbody></table></div>'
def records(name,n):
    rows=[x.split('|') for x in (ROOT/'content'/name).read_text().splitlines() if x.strip()]
    assert len(rows)==n,(name,len(rows),n)
    return rows

SOURCES={
 'study':('https://www.irs.gov/pub/irs-pdf/p5653.pdf','IRS Cost Segregation Audit Technique Guide, Publication 5653'),
 'depreciation':('https://www.irs.gov/publications/p946','IRS Publication 946: depreciation, ownership, methods, and timing'),
 'basis':('https://www.irs.gov/publications/p551','IRS Publication 551: acquisition, transferred, and adjusted basis'),
 'rental':('https://www.irs.gov/publications/p527','IRS Publication 527: rental use, conversion, and expense considerations'),
 'loss':('https://www.irs.gov/publications/p925','IRS Publication 925: passive activity and at-risk considerations'),
 'method':('https://www.irs.gov/instructions/i3115','IRS Instructions for Form 3115: accounting-method change procedures'),
}
def refs(keys):
    return '<section class="source-panel"><h2>References and scope</h2><ul>'+''.join(f'<li><a href="{SOURCES[k][0]}">{E(SOURCES[k][1])}</a></li>' for k in keys)+'</ul>'+p('These references explain the underlying tax framework. The checklists and scenarios on this page are editorial tools for gathering evidence, not quotations or asset-specific rulings from the IRS. The audit guide is examination guidance, not an official pronouncement of law or certification of a provider. A return preparer must apply current authority to the particular property, taxpayer, and filing year.')+'</section>'
def clean_links(s):
    def f(m):
        link=m[1]
        if link.endswith('index.html'):
            link=urljoin('/',link).removesuffix('index.html')
        return 'href="'+link+'"'
    # Shared renderer uses depth-relative links; resolve with the known page separately.
    return s
def render(path,title,desc,body,category='Guides',siblings=(),source_keys=('study','depreciation'),is_guide=True):
    url=BASE_URL+'/'+path.strip('/')+'/'
    depth=len(path.split('/'))
    graph=[{'@type':'Organization','@id':BASE_URL+'/#organization','name':'Stratum Cost Segregation','url':BASE_URL+'/'},
      {'@type':'WebPage','@id':url+'#webpage','url':url,'name':title+' | Stratum','description':desc,'dateModified':DATE,'publisher':{'@id':BASE_URL+'/#organization'}},
      {'@type':'BreadcrumbList','itemListElement':[{'@type':'ListItem','position':1,'name':'Home','item':BASE_URL+'/'},{'@type':'ListItem','position':2,'name':'Resource center','item':BASE_URL+'/resources/'},{'@type':'ListItem','position':3,'name':title,'item':url}]}]
    if is_guide:
        graph.append({'@type':'Article','headline':title,'description':desc,'datePublished':DATE,'dateModified':DATE,'author':{'@id':BASE_URL+'/#organization'},'publisher':{'@id':BASE_URL+'/#organization'},'mainEntityOfPage':url+'#webpage'})
    contents=''
    heads=re.findall(r'<h2>(.*?)</h2>',body)
    if heads:
        for i,h in enumerate(heads): body=body.replace('<h2>'+h+'</h2>',f'<h2 id="section-{i}">'+h+'</h2>',1)
        contents='<nav class="guide-toc" aria-label="On this page"><strong>On this page</strong><ul>'+''.join(f'<li><a href="#section-{i}">{h}</a></li>' for i,h in enumerate(heads))+'</ul></nav>'
    related='<section class="guide-related"><h2>Related work</h2><ul>'+''.join(f'<li><a href="/{a}/">{E(b)}</a></li>' for a,b in siblings)+'</ul></section>' if siblings else ''
    meta='<p class="meta">'+E(category)+' · Published '+DATE_LABEL+' · Stratum editorial team</p>' if is_guide else ''
    disclosure='<div class="content-disclosure">Practical evidence guide. Classification, basis, and usable deductions require property-specific analysis. Scenarios are hypothetical.</div>' if is_guide else ''
    text=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(title)} | Stratum</title><meta name="description" content="{E(desc,quote=True)}"><link rel="canonical" href="{url}">
<meta property="og:title" content="{E(title,quote=True)} | Stratum"><meta property="og:description" content="{E(desc,quote=True)}"><meta property="og:url" content="{url}"><meta property="og:type" content="{'article' if is_guide else 'website'}"><meta name="twitter:card" content="summary"><link rel="stylesheet" href="/style.css">
<script type="application/ld+json">{json.dumps({'@context':'https://schema.org','@graph':graph},ensure_ascii=False)}</script>{ANALYTICS}</head><body>{nav(depth)}
<main class="article resource-article"><div class="breadcrumbs"><a href="/">Home</a> &raquo; <a href="/resources/">Resource center</a> &raquo; {E(category)}</div><h1>{E(title)}</h1><p class="guide-summary">{E(desc)}</p>{meta}{disclosure}{contents}{body}{refs(source_keys) if is_guide else ''}{related}
<div class="cta-banner"><h2>Bring the evidence into a property review</h2><p>Stratum documents the property. AE Tax Advisors can discuss how a study may fit your broader tax position. Confirm the engagement scope and filing responsibilities before work begins.</p><a class="btn btn-gold" href="{AE_BOOKING}">Discuss your property with AE Tax Advisors &rarr;</a></div></main>{footer(depth)}{SCRIPTS}</body></html>'''
    # Normalize existing shared navigation to clean canonical URLs.
    def normalize(m):
        link=m[1]; resolved=urljoin(url,link)
        if link.startswith(('https://','http://')):return m[0]
        if urlparse(resolved).netloc==urlparse(BASE_URL).netloc:
            u=urlparse(resolved); link=u.path.removesuffix('index.html')+('?' +u.query if u.query else '')+('#'+u.fragment if u.fragment else '')
        return 'href="'+link+'"'
    text=re.sub(r'href="([^"]+)"',normalize,text)
    out=ROOT/path/'index.html';out.parent.mkdir(parents=True,exist_ok=True);out.write_text(text)
    if is_guide: manifest.append({'path':path,'title':title,'description':desc,'category':category,'sources':[SOURCES[k][0] for k in source_keys]})

ASSET_TASKS=[
('classification','Classification evidence','Describe the physical facts that distinguish the equipment, site work, and building construction.',
 '''A recovery period is a conclusion supported by an asset's use, construction, ownership, and applicable authority. It is not a feature supplied by a product's marketing name. Start by dividing the work into physical components, then ask whether each component serves the general building or a particular function. Permanence and attachment can matter, but one photograph showing a screw or a movable part is not a complete classification analysis.''',
 '''Ask the provider for a description of the component and the technical reasoning behind material classifications. The reviewer should be able to connect the reasoning to the property's facts. If a system contains separately identified equipment and structural work, the explanation should show how those costs were separated. A generic percentage or a favorable asset label does not establish that separation.'''),
('acquisition-allocation','Acquisition allocation','Reconcile what transferred at closing before assigning cost to individual components.',
 '''An acquisition study allocates an existing supported cost pool; it does not create additional basis merely by identifying more items. Begin with the purchase documents and the preparer's land and cost determinations. Identify furnishings sold separately, items retained by the seller, and components owned by someone else. A photograph taken before closing can show an item that was never transferred to the buyer.''',
 '''Trace each separately valued item through the purchase allocation and the owner's asset schedule. An item included in a bill of sale may already be outside the building pool. For costs estimated from physical quantities, ask how the estimate is converted into an allocation of the acquisition basis. Do not add a current replacement price on top of the original purchase price as if it were a new expenditure.'''),
('renovation-costs','Renovation cost breakdown','Separate equipment, installation, retained construction, and project credits in a new improvement.',
 '''A renovation study starts with what was actually bought, constructed, removed, and retained. Gather the original scope, approved changes, final invoices, and owner-direct purchases. The provider needs enough detail to distinguish work packages and allocate shared labor or indirect costs. A contractor can supply factual detail without deciding the recovery periods that the tax professional will evaluate.''',
 '''Reconcile allowances and credits before combining contractor and owner records. An owner-direct purchase can replace an item in the builder's allowance rather than add another item to the project. Keep payments, deposits, refunds, and unfinished work separately visible. Ask the preparer to evaluate repair versus capitalization treatment and relevant service dates before a new component is entered into the tax schedule.'''),
('photo-checklist','Photo and measurement checklist','Show the location, attachment, function, dimensions, and relevant system connections.',
 '''Useful photographs answer a physical question. Take an overview that shows location, a closer view showing installation, and a label or specification photograph where appropriate. Include measurements with their units and explain whether they were measured directly or estimated. Attractive listing photography often omits the attachments, utilities, and hidden layers that distinguish one component from another.''',
 '''Name files by property, component, date, and viewpoint. Link photographs to an invoice or inventory row where possible. An image establishes visible condition, not cost basis, ownership, or the correct filing treatment. Explain concealed work with plans, specifications, or contractor descriptions. Do not dismantle equipment or enter unsafe areas to gather evidence; ask the provider what alternative records will answer the question.'''),
('report-review','Report review questions','Trace the described component through its cost support, assumptions, and proposed treatment.',
 '''Review the asset description before examining its recovery period. A classification can look precise while describing the wrong physical item. Compare report quantities and locations with the owner inventory and supporting photographs. For material entries, ask whether the cost comes from actual records, a quantity estimate, or an allocation, and how the approach reconciles to the total analyzed basis.''',
 '''Use a written issue log for missing records, inconsistent quantities, unexplained assumptions, and disagreements. Ask the provider to identify the affected rows and issue a dated correction when appropriate. Preserve both the original and final versions. The return preparer should receive the final report and any explanation that changes implemented depreciation, rather than relying on an earlier spreadsheet forwarded during drafting.'''),
('replacement-disposition','Replacement and disposition records','Identify the removed component and preserve its historical record separately from the new addition.',
 '''A replacement can involve removal of one component while much of a system remains. Preserve photographs and records before demolition when practical. Identify the old component's description, location, acquisition history, and prior schedule entry. A new replacement invoice establishes facts about the new work; it does not automatically prove the removed asset's original basis or a deductible disposition amount.''',
 '''Ask the preparer whether disposition rules or elections apply, what basis support is acceptable, and how any sale or salvage proceeds are treated. The provider can help identify physical components within its agreed scope. Keep demolition, removal, new construction, and retained construction separate. Update the asset inventory after implementation so an old item is not still treated as present while its replacement is also recorded.'''),
]

def build_assets():
    data=records('expansion_components.txt',50)
    notes=dict(records('expansion_component_notes.txt',50))
    for i,(name,parts,docs,distinction,scenario,disposal) in enumerate(data):
        ss=slug(name)
        sibling=[('resources/components/'+ss+'-'+t[0],name+': '+t[1]) for t in ASSET_TASKS]
        for j,(task,label,goal,method,review) in enumerate(ASSET_TASKS):
            title=name+' Cost Segregation: '+label
            desc=f'{goal} A practical {name.lower()} guide for rental owners preparing a cost segregation study.'
            body=section('Start with the actual '+name.lower(),distinction,'For this review, identify '+parts+'. The objective is to describe the property accurately enough that the analyst can distinguish separate assets and shared work. Record any difference between acquisition condition and the current installation.')
            body+=section(label+' workflow',method,review)
            body+=section('Details that matter for '+name.lower(),notes[name])
            body+='<section><h2>'+E('Evidence to collect for '+name.lower())+'</h2>'+p('Start with '+docs+'. Keep the original records and mark which portions of the component or project each document supports. An unexplained total should remain an open question rather than be divided into invented amounts.')+table([
                ('Component boundary',parts.capitalize()),('Primary records',docs.capitalize()),
                ('Location and ownership','Property address, room or site location, owner entity, and any shared or third-party use.'),
                ('Cost trail','Invoice or acquisition-allocation reference; include credits, separately recorded items, and the estimation method if costs are reconstructed.'),
                ('Timeline','Acquisition, installation, availability for intended use, and later changes; retain the record supporting each relevant date.')])+'</section>'
            prompts=[
              'Which physical feature in this installation supports separating the item from the surrounding building or site work?',
              'Is any value for this item already included in a separate furnishings purchase or an existing asset schedule?',
              'Does the final contractor total include the same item as an owner-direct purchase, allowance, or later credit?',
              'Do the submitted views show the function and attachment, or only an attractive finished surface?',
              'Can the report reviewer trace the component quantity and supported cost back to this installation?',
              'Which part was actually removed, and what reliable record supports its historical identity and basis?'
            ]
            body+=section('A hypothetical '+name.lower()+' evidence problem',scenario,'The unresolved question is: '+prompts[j]+' Give the reviewer the underlying records and identify the uncertainty explicitly. This example illustrates an evidence issue; it does not assign a tax life, estimate a deduction, or describe a completed Stratum client engagement.')
            next_steps=[
              'Prepare an asset description that distinguishes the physical elements and request technical support for any material classification.',
              'Build a purchase-allocation bridge that shows the item once, with its ownership and separately recorded costs visible.',
              'Ask the contractor for a factual breakdown and reconcile the final net cost to the owner-direct purchases.',
              'Submit a labeled photo set with a short explanation of concealed construction and the related document references.',
              'List each unresolved report row and obtain a final dated version before the preparer implements it.',
              'Before discarding records, '+disposal+'. Give the preparer the old schedule and replacement scope together.'
            ]
            body+=section('Finish this review before implementation',next_steps[j],'The study supplies property evidence and proposed classifications. The return analysis determines applicable depreciation methods, any bonus eligibility, loss limitations, state adjustments, and disposition consequences. Agree who resolves each outstanding issue and keep the accepted records with the final report.')
            rel=[v for k,v in enumerate(sibling) if k!=j][:3]+[('resources/buyers/sample-cost-segregation-report-walkthrough','Sample report walkthrough'),('resources/components','Component evidence library')]
            render('resources/components/'+ss+'-'+task,title,desc,body,'Component evidence',rel,('study','basis','depreciation'))

SCENARIO_TASKS=[
 ('study-scope','Study scope','Define what the property engagement includes before work begins.',
  'A scope should identify the property interest, relevant buildings and components, acquisition and improvement periods, available records, and excluded work. It should describe the report and schedules being delivered, who performs the technical work, and how missing information will be handled. A broad promise to maximize deductions does not resolve these operational questions.',
  'Request written confirmation of the scope, fee, deliverables, evidence requirements, and change process. Separate property analysis from return preparation and advisory services. If the facts change during intake, ask whether the engagement needs a revised cost pool or additional work instead of quietly expanding the original scope.'),
 ('basis-review','Basis review','Establish the supported cost pool before evaluating component classifications.',
  'Basis is a tax starting point, not necessarily current value, borrowed funds, insurance coverage, or the number shown in a listing. The acquisition or transfer history can determine which records are relevant. Give the preparer enough information to establish and adjust the cost pool, then give the provider a reconciliation that can be followed back to those records.',
  'Document the difference between the opening amount and the final study basis. Show land, separately recorded assets, credits, additions, exclusions, and relevant prior treatment. Keep estimates identified. A component analysis cannot repair an unsupported basis simply by allocating the total among many short-lived rows.'),
 ('document-checklist','Document checklist','Gather the records that resolve the scenario rather than uploading an unstructured folder.',
  'Organize original records by property, event, and date. Give the reviewer a short narrative of what happened and an index connecting each material cost to its supporting document. Identify missing information and the person most likely to provide it. A complete-looking folder can still omit the one record that establishes ownership, allocation, or timing.',
  'Keep purchase and transfer documents, improvement evidence, prior tax schedules, and operating records separately labeled. Use a secure sharing process and exclude unnecessary private information. A bookkeeper, manager, contractor, or prior preparer can each hold part of the evidence. Ask for source records rather than relying only on their summary labels.'),
 ('report-reconciliation','Report reconciliation','Check that the delivered study follows the actual property history.',
  'Start with the scope and basis reconciliation, then inspect material asset descriptions, quantities, methods, and assumptions. Compare what the report says was acquired or constructed with what the owner records establish. Ask for an explanation of differences before implementing the schedule. A larger proposed deduction does not resolve an inconsistency in physical facts or costs.',
  'Create a written issue log and preserve dated versions of the report. Identify whether an issue concerns missing evidence, an allocation, a classification, or return treatment. Direct physical and costing questions to the study provider and filing questions to the preparer. Record the final decision and which asset rows it affects.'),
 ('tax-preparer-handoff','Tax preparer handoff','Connect the property evidence to the return decisions without assuming filing work is included.',
  'Send the final study, reconciled basis, prior asset schedules, relevant dates, and unresolved issues together. Ask the preparer to confirm the implementation approach and any required election or accounting-method analysis. Explain the ownership and use history rather than expecting an asset spreadsheet alone to convey it.',
  'The preparer evaluates current authority, applicable methods, bonus eligibility, loss limitations, state treatment, and any later sale effects. Assign filing tasks explicitly and distinguish study delivery from completion of the return. Retain final filed statements and schedules so a future preparer can determine what was actually implemented.'),
]

def build_scenarios():
    for name,issue,docs,principle,example,risk in records('expansion_scenarios.txt',30):
        ss=slug(name)
        siblings=[('resources/scenarios/'+ss+'-'+t[0],name+': '+t[1]) for t in SCENARIO_TASKS]
        for j,(task,label,goal,method,action) in enumerate(SCENARIO_TASKS):
            title=name+' Cost Segregation: '+label
            desc=goal+' Resolve '+issue+' using property-specific records.'
            body=section('The issue this scenario creates',principle,'The main objective is to '+issue+'. A useful analysis makes the ownership and timeline understandable before anyone applies a reclassification estimate. Do not replace missing history with an assumed new purchase or a generic depreciation percentage.')
            body+=section(label+' approach',method,action)
            body+='<section><h2>Scenario-specific evidence</h2>'+p('Start with '+docs+'. Connect each record to the event it establishes. Explain conflicts and missing years rather than presenting a single unexplained number.')+table([
              ('Main question',issue.capitalize()),('Source documents',docs.capitalize()),
              ('Known uncertainty',risk.capitalize()),('Event timeline','Original acquisition or transfer; changes in rental use; additions, removals, and prior filing events.'),
              ('Reconciliation','Supported opening amount, relevant adjustments, land and separate assets, prior treatment, and the cost pool used in the report.')])+'</section>'
            body+=section('Hypothetical example',example,'The review should guard against '+risk+'. Resolve that concern using the specific records above. The example illustrates a process question, not an available deduction or an actual completed client study.')
            questions=[
              'Does the written engagement describe the ownership and events above, and does it exclude any work the owner expects?',
              'Can the provider and preparer explain each adjustment from the supported starting basis to the analyzed amount?',
              'Which source record is still missing, who holds it, and what decision depends on obtaining it?',
              'Do the final report descriptions and quantities match the supported ownership, use, and improvement history?',
              'Has the preparer confirmed the filing approach and received the final records rather than an earlier draft?'
            ]
            body+=section('Question to resolve before closing this task',questions[j],'Write down the response and retain the supporting record. Assign an owner to any remaining issue and confirm whether it changes the study scope, projected benefit, delivery timeline, or implementation cost. A property report and a usable deduction are separate steps in the workflow.')
            body+='<section><h2>Practical completion checklist</h2>'+ul(['Identify the actual property owner and reporting taxpayer.','Preserve original records and explain missing information.','Keep existing assets separate from later additions and replacements.','Confirm the provider and return preparer have accepted the same basis reconciliation.','Retain the final report and the schedules actually implemented.'])+'</section>'
            keys=('basis','rental','depreciation','method') if task=='tax-preparer-handoff' else ('basis','rental','depreciation')
            related=[v for k,v in enumerate(siblings) if k!=j][:3]+[('resources/scenarios','Ownership and project scenario library'),('resources/buyers/cpa-implementation-responsibility-checklist','CPA implementation responsibility checklist')]
            render('resources/scenarios/'+ss+'-'+task,title,desc,body,'Ownership and project scenarios',related,keys)

def build_buyers():
    notes=dict(records('expansion_buyer_notes.txt',50))
    for title,issue,request,workflow,example in records('expansion_buyers.txt',50):
        ss=slug(title); desc=issue+' Practical cost segregation buyer guidance from Stratum.'
        body=section('The decision this guide addresses',issue,request)
        body+=section('Make this review concrete',notes[title])
        body+=section('A practical review sequence',workflow,'Begin with the actual property and engagement being considered. Keep a written distinction between confirmed facts, estimates, services being purchased, and decisions reserved for the return preparer. If a seller or provider presents only a headline benefit, ask for the underlying evidence and assumptions before making a comparison.')
        body+='<section><h2>Working review sheet</h2>'+table([
          ('Question to resolve',issue),('Evidence or explanation to request',request),('Review action',workflow),
          ('Responsible party','Name the owner, study provider, technical reviewer, or return preparer who can answer this particular question.'),
          ('Acceptance record','Document the answer, its supporting reference, unresolved items, and the version of the report or engagement to which it applies.')])+'</section>'
        body+=section('A hypothetical problem to recognize',example,'Treat the missing explanation as an open item. Ask for a written response, connect it to the affected records, and determine whether it changes the proposed scope or feasibility. This scenario is an editorial illustration, not a testimonial or evidence that a particular provider has performed deficient work.')
        body+=section('Questions for the next conversation','What evidence supports the proposed conclusion for this property? Which facts or records could change the answer? Who is responsible for resolving them, and is that work included in the quoted engagement? These questions are more useful when they identify a specific document, asset row, or service than when they request a general assurance of quality.',
          'Ask what the final deliverable will contain and how the preparer will receive it. Where the question affects costs or implementation, request a revised written scope rather than relying on a sales-call recollection. Where it affects tax treatment, the preparer should apply the current rules to the taxpayer rather than extrapolate from another property.')
        body+=section('Complete the decision record','Retain the relevant proposal, response, source documents, final report version, and implementation notes in the property file. Record what remains unresolved and whether it must be addressed before engagement, before report delivery, or before filing. A documented decision is easier to review later than an unexplained schedule or an isolated benefit estimate.',
          'Stratum focuses on component evidence and reporting. Broader tax planning, method changes, state calculations, and return preparation need defined responsibilities and an agreed scope. Confirm those roles so the property work produces a useful handoff rather than an assumption that one purchased service includes every related task.')
        keys=('study','basis','depreciation')
        if any(w in title.lower() for w in ['3115','cpa','prior depreciation']): keys=('study','depreciation','method')
        elif any(w in title.lower() for w in ['loss','feasibility','break-even','incremental','holding-period','small rental']):keys=('depreciation','loss','rental')
        related=[('resources/buyers','Buyer and CPA guide library'),('reviews','Study standards'),('pricing','Published Stratum pricing'),('resources/cost-seg-preparer-handoff','Cost segregation preparer handoff')]
        render('resources/buyers/'+ss,title,desc,body,'Buyer and CPA guides',related,keys)

def hub(path,title,desc,items,extra=()):
    body='<section><h2>Choose the question you need to resolve</h2><div class="guide-search"><label for="guide-search">Search these guides</label><input id="guide-search" type="search" placeholder="Try hot tubs, inherited property, or report review"><p id="guide-result-count" role="status" aria-live="polite">'+str(len(items))+' guides</p></div><div class="guide-grid">'
    for m in items:
        body+=f'<article class="guide-card" data-search="{E((m["title"]+" "+m["description"]).lower(),quote=True)}"><span class="eyebrow">{E(m["category"])}</span><h3><a href="/{m["path"]}/">{E(m["title"])}</a></h3><p>{E(m["description"])}</p></article>'
    body+='</div><p id="guide-empty" hidden>No guides match that search. Try a component name or a shorter phrase.</p></section>'
    body+=r'''<script>(function(){var field=document.getElementById('guide-search'),cards=Array.from(document.querySelectorAll('[data-search]')),count=document.getElementById('guide-result-count'),empty=document.getElementById('guide-empty');field.addEventListener('input',function(){var words=field.value.toLowerCase().trim().split(/\s+/).filter(Boolean),n=0;cards.forEach(function(c){var show=words.every(function(w){return c.dataset.search.includes(w)});c.hidden=!show;if(show)n++});count.textContent=n+' guides';empty.hidden=n!==0})})();</script>'''
    render(path,title,desc,body,'Resource library',extra,is_guide=False)

def expand_navigation():
    categories=[('resources/components','Component evidence'),('resources/scenarios','Ownership and project scenarios'),('resources/buyers','Buyer and CPA guides')]
    descriptions={
      'resources/components':'Explore 300 component-specific cost segregation guides covering classification evidence, acquisition costs, renovations, photographs, report review, and replacement records.',
      'resources/scenarios':'Explore 150 cost segregation workflow guides for transfers, mixed use, furnished acquisitions, portfolios, renovations, missing records, and preparer coordination.',
      'resources/buyers':'Explore 50 practical cost segregation buyer and CPA guides covering report deliverables, engagement scope, pricing comparisons, feasibility, and implementation.'}
    for path,title in categories:
        items=[m for m in manifest if m['path'].startswith(path+'/')]
        hub(path,title+' Library',descriptions[path],items,[('resources','All resource categories')]+[x for x in categories if x[0]!=path])
    body=section('Start with the decision in front of you','Use the component library to understand what physical and cost evidence a study needs. Use the scenario library when ownership, transfers, personal use, or project history complicate the starting point. Use the buyer and CPA guides to evaluate deliverables, fees, and implementation responsibilities.')
    body+='<div class="guide-grid">'+''.join(f'<article class="guide-card"><h2><a href="/{a}/">{b}</a></h2><p>{sum(m["path"].startswith(a+"/") for m in manifest)} practical guides</p></article>' for a,b in categories)+'</div>'
    body+=section('What this resource center provides','The library contains 500 new evidence and workflow guides. It does not publish invented client results or claim an undocumented professional review. A component name is not a guaranteed depreciation classification, and a hypothetical scenario is not a property-specific tax conclusion.')
    existing=[('resources/cost-segregation-input-quality','Input quality and the records behind a study'),('resources/cost-seg-preparer-handoff','The preparer handoff'),('str-study-planner','STR study planner'),('cost-segregation-calculator','Cost segregation calculator'),('blog','Tax and property articles'),('locations','Location guides')]
    render('resources','Cost Segregation Resource Center','Explore 500 component evidence, ownership scenario, study buyer, and CPA handoff guides from Stratum Cost Segregation.',body,'Resource center',categories+existing,is_guide=False)
    # Add discoverable navigation to all retained pages, not just newly generated ones.
    for file in pages():
        s=file.read_text()
        if '/resources/">Resource center</a>' not in s:
            marker='<a href="/blog/">Blog</a>'
            if marker in s:s=s.replace(marker,marker+'<a href="/resources/">Resource center</a>',1)
        if 'resource-library-links' not in s and not file.relative_to(ROOT).as_posix().startswith('resources/'):
            links='<aside class="research-links resource-library-links" aria-label="Property evidence resources"><h2>Property evidence and study decisions</h2><ul>'+''.join(f'<li><a href="/{a}/">{E(b)}</a></li>' for a,b in categories)+'</ul></aside>'
            s=s.replace('<footer class="footer">',links+'<footer class="footer">',1)
        file.write_text(s)

def pages():return sorted(p for p in ROOT.rglob('index.html') if not set(p.relative_to(ROOT).parts)&{'public','.git','node_modules'})
def sitemap():
    ET.register_namespace('','http://www.sitemaps.org/schemas/sitemap/0.9');ns='{http://www.sitemaps.org/schemas/sitemap/0.9}'
    doc=ET.Element(ns+'urlset')
    for file in pages():
        canonical=re.search(r'<link rel="canonical" href="([^"]+)"',file.read_text())
        assert canonical,file
        node=ET.SubElement(doc,ns+'url');ET.SubElement(node,ns+'loc').text=canonical[1]
        ET.SubElement(node,ns+'lastmod').text=DATE
    ET.indent(doc);ET.ElementTree(doc).write(ROOT/'sitemap.xml',encoding='utf-8',xml_declaration=True)

def main():
    build_assets();build_scenarios();build_buyers()
    assert len(manifest)==500,len(manifest)
    assert len({m['path'] for m in manifest})==500
    (ROOT/'content/resource-expansion-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    expand_navigation();sitemap()
    print(json.dumps({'new_guides':len(manifest),'component_guides':300,'scenario_guides':150,'buyer_guides':50,'total_site_pages':len(pages())},indent=2))
if __name__=='__main__':main()
