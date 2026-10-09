#!/usr/bin/env python3
"""Apply targeted editorial repairs after the resource expansion build."""
import re,json
from pathlib import Path
from html import escape as E
from build_resource_expansion import render,section,p,ul,table,pages,sitemap,DATE,BASE_URL
ROOT=Path(__file__).resolve().parent

def main():
    changes=[]
    # Remove contradictory exclusivity language without claiming a new service.
    home=ROOT/'index.html';s=home.read_text()
    s=s.replace('We specialize exclusively in residential cost segregation for STR and LTR investors, delivering precise, well-documented studies.','Our core focus is residential cost segregation for STR and LTR investors. Commercial articles are educational resources; confirm property eligibility and engagement scope before ordering a study.')
    s=s.replace('We focus exclusively on residential rental properties, from Airbnb vacation rentals to traditional long-term rental portfolios. We understand the nuances of each strategy.','Our residential focus includes Airbnb vacation rentals and traditional long-term rental portfolios. The study documents property facts; your preparer evaluates the tax treatment for your operating strategy.')
    s=s.replace('Explore the assets and records that shape studies across residential and commercial real estate.','Explore residential property study questions and commercial educational guides. Confirm service scope for your property.')
    if 'new-guide-library' not in s:
        block='<section class="section" id="new-guide-library"><div class="container"><h2>Resolve the details behind your property study</h2>'+p('Explore 500 new practical guides covering component evidence, ownership and renovation scenarios, and buyer and CPA review questions. Start with the issue in your records rather than a generic savings percentage.')+'<div class="card-grid"><div class="card"><h3><a href="/resources/components/">Component evidence</a></h3><p>Equipment, outdoor improvements, installation records, and report review.</p></div><div class="card"><h3><a href="/resources/scenarios/">Ownership and project scenarios</a></h3><p>Transfers, mixed use, portfolios, missing records, and prior studies.</p></div><div class="card"><h3><a href="/resources/buyers/">Buyer and CPA guides</a></h3><p>Scope, fees, report quality, feasibility, and implementation responsibilities.</p></div></div></div></section>'
        s=s.replace('<footer class="footer">',block+'<footer class="footer">',1)
    home.write_text(s);changes.append('Homepage residential scope and resource navigation')

    body=section('Published residential study pricing','The published single-property fee is $3,500. The published portfolio fee is $2,900 per property for three to five properties. Six or more properties use a custom quote. Confirm the final written fee and property scope during intake; published prices do not resolve every unusual property or records issue.')
    body+=table([('Single residential property','$3,500 published fee'),('Portfolio of 3 to 5 properties','$2,900 per property published fee'),('6 or more properties','Custom scope and quote')])
    body+=section('Define the deliverables in writing','The engagement should identify the property and cost periods covered, component analysis, basis reconciliation, schedules, technical explanations, assumptions, and the support available to the return preparer. Ask what form the schedules take and whether the report covers acquired furnishings, later improvements, or partial dispositions.',
      'Confirm who performs and reviews the work, how physical evidence is gathered, how unavailable cost detail is estimated, and whether changes in records affect the fee. The report and the tax return are different deliverables. A quoted study should not be assumed to include every associated tax-planning or filing task.')
    body+=section('Confirm what is charged separately','Ask specifically about land valuation work, site visits, historical schedule reconstruction, Form 3115 preparation and filing, amended returns, state depreciation adjustments, and representation in an examination. Guidance or coordination is not the same as preparing and filing a form. Obtain the complete scope before relying on an estimate of total cost.')
    body+=section('Delivery targets and complete intake','Published delivery targets have been 14 days for a single property, 10 days for a three-to-five-property portfolio, and 7 days for an expedited enterprise engagement. Confirm availability, when the delivery clock starts, and how missing records or revisions affect the schedule. A complete report requires adequate evidence; a target is not a substitute for resolving a material basis question.')
    body+=section('Evaluate the benefit you can use','Ask your preparer to compare proposed depreciation with the deductions available without the study. Include passive activity and other applicable loss limitations, federal and state differences, implementation costs, expected holding period, and sale consequences. A reclassified amount is not an automatic refund or permanent tax saving.',
      'The preparer should also determine whether and when the fee is deductible or capitalized. The economic decision depends on your facts. A purchase-price threshold alone does not establish that a study is worthwhile, and a higher or lower provider price does not prove its report quality.')
    body+=section('Before signing','Confirm the property list, complete price, delivery assumptions, evidence requirements, exclusions, revision process, and CPA handoff. Ask who will resolve a disputed classification and what audit-support language actually covers. Keep the accepted proposal with the final report.')
    rel=[('resources/buyers/cost-segregation-engagement-exclusions','Study exclusions checklist'),('resources/buyers/comparing-two-study-proposals','Compare two study proposals'),('resources/buyers/study-fee-break-even-analysis','Study-fee break-even analysis')]
    render('pricing','Cost Segregation Pricing and Engagement Scope','Review published Stratum residential fees, delivery targets, scope questions, exclusions, and the costs to confirm before commissioning a study.',body,'Pricing',rel,is_guide=False)
    title='How Much Does a Cost Segregation Study Cost? Pricing Guide'
    render('blog/cost-segregation-study-cost-pricing',title,'Compare study fees with scope, evidence quality, implementation costs, and usable incremental depreciation benefits.',body,'Study buyer guidance',rel,('study','depreciation','loss'))
    changes.append('Pricing page and pricing article: scope, fee, delivery, and feasibility repairs')

    case=section('An explicitly hypothetical property','This educational model uses a $520,000 vacation-rental purchase and an assumed $78,000 land allocation, leaving $442,000 for the example cost pool. These figures are assumptions, not a documented Stratum client outcome. An actual land allocation, furnishings allocation, and component schedule require supporting evidence.')
    case+=section('The arithmetic before the classifications','Assume, only to illustrate a reconciliation, that a supported study proposes $150,280 in shorter-life components and leaves $291,720 in building property. The amounts total $442,000. The proposed shorter-life share is 34 percent. That percentage is an input to this example, not a typical result or a target for another property.')
    case+=table([('Assumed purchase amount','$520,000'),('Assumed land allocation','$78,000'),('Illustrative cost pool','$442,000'),('Illustrative shorter-life amount','$150,280'),('Remaining building amount','$291,720')])
    case+=section('What the physical analysis would still need','A furnished mountain cabin may include acquired furniture, appliances, spa equipment, exterior paving, and building systems. Each material component needs an ownership description, cost support or disclosed allocation method, and a supported classification. Specialty cabinetry, installed lighting, and security equipment should not receive a tax life merely because their names sound like personal property.',
      'The furnished purchase inventory must reconcile to the analyzed cost pool. If items were already assigned separate basis, the study should not count them again within the building. Later improvements need their own actual costs and relevant dates. A provider should explain the asset boundary and classification rather than force the report to reach the assumed 34 percent.')
    case+=section('Why this example does not calculate a refund','Dividing $442,000 by 27.5 gives roughly $16,073 as a simple full-year straight-line arithmetic reference. It is not a valid first-year return calculation by itself. The proper building recovery period, depreciation convention, placed-in-service date, methods, and other facts need confirmation.',
      'Likewise, the $150,280 component amount is not automatically an additional current deduction. A preparer must evaluate each component, applicable bonus rules and elections, depreciation otherwise available, and the owner\'s ability to use resulting losses. State treatment and disposition consequences can change the usable timing benefit.')
    case+=section('Short stays do not establish wage offsets','The booking arrangement, average customer use, services, participation, and other applicable rules require review. Calling a property an STR does not automatically make its losses usable against wages. The model does not claim that this hypothetical owner qualifies for an exception or recovers the study fee in the first year.')
    case+=section('Use the illustration as an evidence checklist','Bring the actual closing, land evidence, furnishing inventory, installation invoices, rental-use history, and previous schedules. Request a feasibility comparison before commissioning the study. Document both the proposed depreciation and what would otherwise be available, together with fees and an expected holding period.')
    render('blog/cost-segregation-case-study-vacation-rental','Hypothetical Cost Segregation Example: $520K Vacation Rental in Gatlinburg','Review an explicitly hypothetical $520,000 vacation-rental cost pool, component reconciliation, and the facts needed before estimating usable tax benefits.',case,'Hypothetical illustration',[('resources/buyers/sample-cost-segregation-report-walkthrough','Report walkthrough'),('resources/buyers/incremental-depreciation-comparison','Incremental depreciation comparison'),('resources/scenarios/furnished-rental-acquisition-basis-review','Furnished acquisition basis review')],('basis','depreciation','loss','rental'))
    changes.append('Vacation-rental example: hypothetical labels, reconciliation, and conditional tax treatment')

    about=ROOT/'about/index.html';s=about.read_text()
    if 'technical-role-clarity' not in s:
        more='<section id="technical-role-clarity"><h2>Ask who performs the technical work</h2>'+p('During intake, request the names and qualifications of the assigned analyst and technical reviewer, the person responsible for the final report, and the process for resolving your preparer\'s questions. The educational publisher is not presented as the engineer signing a property study. Professional review attribution is used only when the actual review is documented.')+'<h2>Evidence you can evaluate before engaging</h2><ul><li><a href="/resources/buyers/sample-cost-segregation-report-walkthrough/">What to examine in a sample report</a></li><li><a href="/resources/buyers/verifying-the-study-preparer-s-credentials/">Verify the assigned preparer\'s credentials</a></li><li><a href="/resources/buyers/what-a-documented-client-case-study-should-show/">What documented case work should show</a></li></ul></section>'
        s=s.replace('<div class="cta-banner">',more+'<div class="cta-banner">',1)
    about.write_text(s);changes.append('About: technical roles and verification questions')

    # Repair high-confidence unconditional phrases without manufacturing filing conclusions.
    repairs=0
    replacements={
      'that accelerated amount is deductible in full in the year of acquisition':'a current deduction for that amount still depends on each asset\'s eligibility, relevant dates, elections, and the owner\'s applicable limitations',
      'There is no statute of limitations on the look-back while you continue to own the property.':'The applicable accounting-method procedure, eligibility, prior methods, and filing requirements need preparer review; continued ownership alone does not establish an unrestricted right to a catch-up deduction.',
      'There is no time limit on the look-back period.':'The preparer must evaluate the applicable method-change procedure and the property\'s actual prior treatment before calculating any adjustment.',
      'the full cost of qualifying 15-year assets is deducted in Year 1':'first-year treatment requires review of qualifying costs, acquisition and service dates, elections, and loss limitations',
      'they are deducted entirely in Year 1':'any first-year deduction depends on the particular assets, timing, elections, and applicable limitations',
    }
    for file in pages():
        if file.relative_to(ROOT).parts[0]=='resources':continue
        s=file.read_text();before=s
        for a,b in replacements.items():s=s.replace(a,b)
        # Keep legacy dashes out of newly revised user-facing prose.
        s=s.replace('\u2014','; ').replace('&mdash;','; ').replace('&#8212;','; ')
        if s!=before:repairs+=1;file.write_text(s)
    changes.append(f'Applied targeted claim and prose repairs to {repairs} retained pages')
    # Repair a known root-relative asset error in older standalone resources.
    for file in (ROOT/'resources').glob('*/index.html'):
        s=file.read_text();s=s.replace('href="style.css?v=20260927-2"','href="/style.css?v=20260927-2"');file.write_text(s)
    # Synchronize metadata on the two updated blog cards, preserving one card per article.
    blog=ROOT/'blog/index.html';s=blog.read_text()
    for key,desc in [('cost-segregation-study-cost-pricing','Compare study fees with scope, evidence quality, implementation costs, and usable incremental depreciation benefits.'),('cost-segregation-case-study-vacation-rental','An explicitly hypothetical model of property basis and the facts needed before estimating usable depreciation benefits.')]:
        pattern=r'(<a href="/blog/'+key+r'/" class="blog-card"[^>]*>)(.*?)(</a>)'
        s=re.sub(pattern,lambda m:m[1]+re.sub(r'<p>.*?</p>','<p>'+desc+'</p>',m[2],flags=re.S)+m[3],s,flags=re.S)
    blog.write_text(s)
    sitemap()
    (ROOT/'content/existing-content-improvements.json').write_text(json.dumps({'date':DATE,'changes':changes,'verification_limit':'Targeted editorial repairs; no undocumented technical reviewer or client evidence is asserted.'},indent=2)+'\n')
    print(json.dumps(changes,indent=2))
if __name__=='__main__':main()
