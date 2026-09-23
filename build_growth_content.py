#!/usr/bin/env python3
"""Build Stratum's calculator, property-type hub, and commercial search pages."""

from pathlib import Path
import html
import json

from build_new_content import rebuild_sitemap, update_blog_index
from stratum_render import AE_BOOKING, ANALYTICS, BASE_URL, SCRIPTS, footer, nav, write_post

ROOT = Path(__file__).resolve().parent


PROPERTY_PAGES = [
    {
        "slug": "cost-segregation-banks-credit-unions",
        "name": "Banks and Credit Unions",
        "description": "Learn how cost segregation applies to bank branches and credit union facilities, including teller systems, vault support, drive-through improvements, and site work.",
        "why": "Bank branches combine standard office construction with secure transaction areas, customer service zones, specialized electrical systems, and substantial exterior improvements. A study should distinguish building systems from removable equipment and should document how each asset supports the financial-services operation.",
        "components": ["teller counters and transaction partitions", "security and access-control wiring", "dedicated equipment power", "decorative millwork and customer-area finishes", "drive-through canopies and pneumatic-tube supports", "parking, curbs, signage, and landscaping"],
        "records": "branch plans, fixed-asset ledgers, vault and security scopes, signage invoices, drive-through contracts, and site-development costs",
        "question": "Were security, teller, and drive-through packages separately bid, or are they buried inside a general contractor schedule of values?",
    },
    {
        "slug": "cost-segregation-grocery-stores-supermarkets",
        "name": "Grocery Stores and Supermarkets",
        "description": "A practical guide to cost segregation for grocery stores and supermarkets, from refrigeration support and specialty electrical work to parking and customer fixtures.",
        "why": "Grocery properties often contain dense electrical distribution, refrigeration support, food-preparation areas, customer fixtures, and large parking fields. The analysis must separate the building shell from assets installed to support retail food operations and must coordinate owner-provided equipment with landlord improvements.",
        "components": ["display and checkout fixtures", "specialty power for refrigeration and food equipment", "flooring serving sales areas", "decorative lighting and department finishes", "loading-area improvements", "parking, sidewalks, curbs, and exterior signage"],
        "records": "department plans, equipment schedules, refrigeration scopes, electrical one-lines, fixture invoices, landlord work letters, and site-cost details",
        "question": "Which costs belong to the building owner, and which were paid by the grocery operator or equipment vendor?",
    },
    {
        "slug": "cost-segregation-shopping-centers-strip-malls",
        "name": "Shopping Centers and Strip Malls",
        "description": "Explore cost segregation for shopping centers and strip malls, including tenant buildouts, common-area improvements, parking lots, signage, and acquisition records.",
        "why": "Retail centers combine a long-lived shell with repeated tenant buildouts, common-area assets, pylon signage, and extensive land improvements. Good records matter because landlord allowances, tenant-owned property, and later remodels may overlap in the fixed-asset ledger.",
        "components": ["tenant-specific partitions and finishes", "storefront systems tied to a tenant layout", "decorative lighting", "pylon and monument signs", "parking lots, sidewalks, and drainage", "landscaping and site lighting"],
        "records": "tenant work letters, allowance schedules, lease exhibits, as-built plans, signage packages, paving contracts, and acquisition closing records",
        "question": "Does the owner retain tax ownership of tenant improvements when a lease ends, and are abandoned buildout costs still on the books?",
    },
    {
        "slug": "cost-segregation-mixed-use-buildings",
        "name": "Mixed-Use Buildings",
        "description": "Understand cost segregation for mixed-use buildings with residential, retail, office, hospitality, or parking components under one ownership structure.",
        "why": "Mixed-use projects can include more than one recovery period before individual components are analyzed. Residential rental space, nonresidential space, parking, and shared building systems may need separate cost pools. The study should document the allocation method before classifying shorter-life assets.",
        "components": ["residential appliances and unit finishes", "retail and office tenant improvements", "shared amenity furnishings", "parking-control equipment", "rooftop and courtyard improvements", "site paving, lighting, and landscaping"],
        "records": "unit and use-area schedules, lease plans, condominium declarations if applicable, construction draws, tenant allowances, and shared-cost allocation workpapers",
        "question": "How were common costs allocated among residential, commercial, parking, and owner-occupied portions of the project?",
    },
    {
        "slug": "cost-segregation-wineries-breweries-distilleries",
        "name": "Wineries, Breweries, and Distilleries",
        "description": "Learn how cost segregation studies address production facilities, tasting rooms, utility infrastructure, storage areas, and site improvements for beverage businesses.",
        "why": "Beverage facilities mix hospitality space with production, storage, and process infrastructure. Dedicated drainage, power, piping, and equipment support may serve a business process rather than the building generally, but the conclusion depends on design, function, and tax ownership.",
        "components": ["tasting-room millwork and decorative finishes", "process-equipment electrical distribution", "production-area drainage and equipment pads", "removable storage and racking", "patios and outdoor guest areas", "vineyard-adjacent roads, fencing, and site improvements"],
        "records": "process plans, equipment lists, utility diagrams, tasting-room buildout costs, equipment-installation invoices, and civil drawings",
        "question": "Which utility runs serve specific production equipment, and which serve the building as a whole?",
    },
    {
        "slug": "cost-segregation-golf-courses-country-clubs",
        "name": "Golf Courses and Country Clubs",
        "description": "Review cost segregation opportunities for golf courses and country clubs, including clubhouse assets, irrigation, cart paths, landscaping, and recreational amenities.",
        "why": "Golf properties are unusually site-intensive. Clubhouse costs are only one part of the analysis; irrigation, paths, drainage, outdoor lighting, practice areas, and recreational amenities can represent substantial separate cost pools. Land itself remains nondepreciable.",
        "components": ["clubhouse furnishings and decorative finishes", "kitchen and bar support systems", "irrigation controls and distribution", "cart paths and pedestrian paving", "outdoor lighting and recreational amenities", "drainage, fencing, and landscaping improvements"],
        "records": "course-development budgets, irrigation plans, civil drawings, clubhouse schedules, kitchen equipment scopes, renovation history, and land allocations",
        "question": "Can original course-development costs be separated from later irrigation, drainage, bunker, or clubhouse renovations?",
    },
    {
        "slug": "cost-segregation-marinas-boat-storage",
        "name": "Marinas and Boat Storage",
        "description": "A guide to cost segregation for marinas, dry-stack boat storage, docks, utility pedestals, fuel systems, paving, and waterfront support facilities.",
        "why": "Marinas often have multiple asset classes across land and water: docks, utility distribution, dry-stack systems, service buildings, fuel infrastructure, and customer amenities. Ownership and permanence are central facts, especially where improvements occupy leased waterfront or submerged land.",
        "components": ["floating dock systems and gangways", "shore-power and utility pedestals", "dry-stack racking and handling support", "fuel-dispensing infrastructure", "customer-area furnishings and decorative finishes", "paving, fencing, lighting, and site drainage"],
        "records": "dock contracts, marina permits, equipment schedules, utility plans, waterfront leases, fuel-system scopes, and civil drawings",
        "question": "Are dock, utility, and fuel-system costs owned by the operator, the landlord, or a public authority?",
    },
    {
        "slug": "cost-segregation-data-centers",
        "name": "Data Centers",
        "description": "Understand cost segregation for data centers, including redundant electrical capacity, cooling infrastructure, security, raised floors, and tenant-owned equipment.",
        "why": "Data centers contain building systems with capacity and redundancy designed around computing operations. Classification depends on whether an asset serves the building generally or directly supports specific equipment and business functions. A conclusory percentage estimate is especially risky for these facilities.",
        "components": ["equipment-specific power distribution", "specialized cooling serving computing loads", "raised access floors", "security and monitoring systems", "equipment pads and support frames", "generators, switchgear, and redundant infrastructure analyzed by function"],
        "records": "electrical one-lines, mechanical sequences, load studies, rack layouts, owner-furnished equipment lists, commissioning reports, and tenant responsibility schedules",
        "question": "Which power and cooling assets would be unnecessary at the same capacity if the computing equipment were removed?",
    },
    {
        "slug": "cost-segregation-research-laboratory-facilities",
        "name": "Research and Laboratory Facilities",
        "description": "Explore cost segregation for research laboratories, including casework, process utilities, equipment power, specialty ventilation, controls, and flexible lab buildouts.",
        "why": "Laboratories combine general building systems with casework, process utilities, specialized controls, and equipment support. The study must analyze use and adaptability rather than assume that every specialized-looking system receives a shorter life.",
        "components": ["removable laboratory casework", "equipment-specific electrical connections", "process gases and specialty piping", "equipment pads and support frames", "dedicated controls and monitoring", "site improvements and secure exterior storage"],
        "records": "lab equipment matrices, process-utility diagrams, casework submittals, mechanical schedules, electrical one-lines, and change-order logs",
        "question": "Does each specialty utility serve identified research equipment, or is it part of the permanent building distribution system?",
    },
    {
        "slug": "cost-segregation-airplane-hangars-aviation-facilities",
        "name": "Airplane Hangars and Aviation Facilities",
        "description": "Learn how cost segregation applies to airplane hangars, fixed-base operators, maintenance facilities, aprons, fueling systems, and aviation support areas.",
        "why": "Aviation facilities can include open-span hangars, maintenance shops, passenger lounges, fueling assets, and extensive exterior paving. The study should trace who owns apron and utility improvements because airports, landlords, and operators may each fund different portions.",
        "components": ["hangar-door equipment and controls", "aircraft-maintenance power and compressed air", "shop equipment supports", "passenger-lounge furnishings and finishes", "fueling support assets", "aprons, fencing, lighting, and site paving"],
        "records": "airport leases, hangar specifications, equipment schedules, fueling contracts, apron scopes, tenant-improvement records, and grant documentation",
        "question": "Which aviation improvements revert to the airport or landlord at lease expiration, and who has tax ownership during the lease?",
    },
    {
        "slug": "cost-segregation-movie-theaters-entertainment-venues",
        "name": "Movie Theaters and Entertainment Venues",
        "description": "Review cost segregation for movie theaters and entertainment venues, including seating, projection support, acoustic finishes, concessions, signage, and parking.",
        "why": "Entertainment venues use purpose-built interiors, customer flow features, equipment support, and branded finishes. A study should distinguish removable operational assets from permanent walls and general building systems, especially after auditorium or concept renovations.",
        "components": ["seating and mounting systems", "projection and audio equipment support", "decorative and acoustic finishes analyzed by function", "concession fixtures and specialty power", "digital signage and queue systems", "parking, exterior lighting, and monument signs"],
        "records": "auditorium plans, seating and audio-visual contracts, concession equipment lists, finish schedules, signage invoices, and remodel histories",
        "question": "Which assets were replaced during recent auditorium conversions, and were the retired assets removed from the tax books?",
    },
    {
        "slug": "cost-segregation-laundromats",
        "name": "Laundromats",
        "description": "A cost segregation guide for laundromats covering machine connections, utility distribution, payment systems, customer fixtures, leasehold improvements, and site work.",
        "why": "Laundromats may have modest building shells but unusually concentrated equipment support. Water, drainage, gas, venting, and power costs must be traced to specific machines or to general building service. Lease terms also affect who owns improvements.",
        "components": ["washer and dryer utility connections", "equipment-specific venting and exhaust", "payment and card systems", "customer tables and seating", "decorative finishes and signage", "parking, exterior lighting, and site improvements"],
        "records": "machine schedules, plumbing and gas plans, equipment-installation contracts, lease work letters, electrical scopes, and remodel invoices",
        "question": "Were utility upgrades sized and routed for identified laundry equipment, and are those costs separate from the building's general service?",
    },
    {
        "slug": "cost-segregation-funeral-homes",
        "name": "Funeral Homes",
        "description": "Learn how cost segregation can apply to funeral homes, viewing rooms, preparation areas, specialized equipment support, decorative interiors, and parking improvements.",
        "why": "Funeral homes combine assembly, office, hospitality, and specialized preparation functions. Interior finishes and equipment support should be analyzed by use and permanence, while large parking and landscaped areas may create separate land-improvement cost pools.",
        "components": ["removable furnishings and display fixtures", "decorative viewing-room finishes", "preparation-equipment connections", "specialty ventilation analyzed by function", "canopies and exterior signage", "parking, sidewalks, lighting, and landscaping"],
        "records": "floor plans, equipment schedules, finish packages, mechanical scopes, renovation invoices, and site-development records",
        "question": "Which preparation-area systems serve specific equipment, and which are required for the building's general occupancy?",
    },
    {
        "slug": "cost-segregation-cold-storage-facilities",
        "name": "Cold Storage Facilities",
        "description": "Understand cost segregation for refrigerated warehouses and cold storage facilities, including insulated enclosures, refrigeration support, racking, docks, and paving.",
        "why": "Cold storage buildings may include temperature-controlled enclosures and utility capacity designed around a specific operation. Classification turns on detailed function, integration, and permanence. Separate ownership of refrigeration equipment can materially change the study scope.",
        "components": ["equipment-specific power distribution", "refrigeration equipment supports", "removable storage and racking", "dock equipment and traffic-control assets", "specialized monitoring and controls", "truck paving, fencing, lighting, and drainage"],
        "records": "refrigeration diagrams, panel schedules, enclosure specifications, equipment ownership lists, racking contracts, and civil plans",
        "question": "Are insulated rooms and refrigeration assets integral to the building itself, or installed as a separate operational system under the facts of the project?",
    },
    {
        "slug": "cost-segregation-leasehold-improvements",
        "name": "Leasehold Improvements",
        "description": "A practical guide to cost segregation for leasehold and tenant improvements, including tax ownership, qualified improvement property, abandoned assets, and documentation.",
        "why": "Leasehold improvement studies start with tax ownership. A landlord allowance, tenant reimbursement, or lease provision can affect who depreciates an asset. Qualified improvement property rules may also matter, but they do not replace a component-level review.",
        "components": ["tenant-specific partitions and finishes", "decorative lighting and millwork", "equipment-specific electrical or plumbing work", "removable fixtures and casework", "signage and branded elements", "assets removed or abandoned during a later remodel"],
        "records": "executed leases, work letters, allowance reconciliations, construction invoices, fixed-asset ledgers, reimbursement records, and surrender provisions",
        "question": "Who bore the economic cost of each improvement, who owns it for tax purposes, and what happens to it when the lease ends?",
    },
]


def make_posts():
    posts = []
    for item in PROPERTY_PAGES:
        lis = "".join(f"<li>{html.escape(x.capitalize())}</li>" for x in item["components"])
        sections = [
            (f"Why {item['name']} Require a Property-Specific Review", f"    <p>{item['why']}</p>\n    <p>Cost segregation is an accounting and engineering analysis. It does not create new basis. It identifies portions of an existing depreciable basis that may qualify for recovery periods shorter than the building's general recovery period. Land is excluded, and the final treatment depends on the property's facts, placed-in-service date, and current tax law.</p>"),
            ("Components the Study Team Will Review", f"    <p>A study for this property type commonly evaluates the following cost groups:</p>\n    <ul>{lis}</ul>\n    <p>This list is a starting point, not a classification result. Similar-looking assets can receive different treatment when their function, permanence, or relationship to the building differs.</p>"),
            ("The Records That Improve the Analysis", f"    <p>The most useful records include {item['records']}. When original cost detail is incomplete, the study team may use accepted estimating methods, but actual invoices and drawings generally make the allocation easier to support.</p>\n    <p>One early scoping question is: <strong>{item['question']}</strong> Answering it helps separate the owner's depreciable basis from tenant, vendor, or public-authority property.</p>"),
            ("Acquisitions, New Construction, and Renovations", "    <p>For a recent acquisition, the analysis starts with the purchase-price allocation and removes nondepreciable land. For new construction, detailed job costs can be traced to individual systems. For an older property, a look-back study may allow the owner and tax advisor to evaluate an accounting-method change using Form 3115 rather than amending multiple returns.</p>\n    <p>Renovations deserve a separate review. The owner may need to identify disposed components, new qualified improvement property, and costs that were repaired rather than capitalized. A cost segregation report should coordinate with the fixed-asset ledger so the tax return does not continue depreciating assets that no longer exist.</p>"),
            ("How to Decide Whether a Study Is Worthwhile", "    <p>Start with depreciable basis, remaining holding period, current and expected taxable income, passive-activity limitations, state conformity, and the expected study fee. Accelerated depreciation changes timing; it does not make the underlying tax basis larger. A future sale can also create depreciation-recapture consequences.</p>\n    <p>A useful estimate should therefore show assumptions instead of promising a deduction. Use Stratum's <a href=\"/cost-segregation-calculator/\">cost segregation calculator</a> for an initial range, then have a tax advisor test the result against the owner's complete return.</p>"),
            ("What an Engineering-Based Study Delivers", "    <p>A complete report should describe the property, establish the depreciable basis analyzed, explain the methodology, classify assets, reconcile the results to source costs, and provide depreciation schedules that a tax preparer can use. The IRS Cost Segregation Audit Technique Guide and <a href=\"https://www.irs.gov/pub/irs-pdf/p946.pdf\">IRS Publication 946</a> are useful reference points for methodology and depreciation rules.</p>\n    <p>Stratum prepares the study. AE Tax Advisors handles the discovery call and can discuss how the study fits within a broader real estate tax plan. Your return preparer remains responsible for the final filing positions.</p>"),
            (f"Discuss a {item['name']} Study", f"    <p>Bring the purchase date, placed-in-service date, estimated land value, current depreciable basis, renovation history, and available plans to the first conversation. <a href=\"{AE_BOOKING}\">Book a discovery call with AE Tax Advisors</a> to scope a Stratum cost segregation study.</p>"),
        ]
        posts.append({
            "slug": item["slug"], "title": f"Cost Segregation for {item['name']}",
            "description": item["description"], "date": "September 22, 2026",
            "iso_date": "2026-09-22", "sections": sections,
            "related": [("what-is-cost-segregation", "What Is Cost Segregation?"), ("cost-segregation-study-cost-pricing", "Cost Segregation Study Cost and Pricing"), ("how-to-choose-cost-segregation-company", "How to Choose a Cost Segregation Company")],
        })
    return posts


def page_shell(title, description, slug, body, extra_schema=None, extra_head="", extra_scripts=""):
    url = f"{BASE_URL}/{slug}/"
    graph = [
        {"@type": "WebPage", "@id": f"{url}#webpage", "url": url, "name": title, "description": description},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{BASE_URL}/"},
            {"@type": "ListItem", "position": 2, "name": title, "item": url},
        ]},
    ]
    if extra_schema:
        graph.append(extra_schema)
    schema = html.escape(json.dumps({"@context": "https://schema.org", "@graph": graph}), quote=False)
    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{html.escape(title)} | Stratum Cost Segregation</title>
<meta name="description" content="{html.escape(description, quote=True)}"><link rel="canonical" href="{url}">
<meta property="og:title" content="{html.escape(title, quote=True)}"><meta property="og:description" content="{html.escape(description, quote=True)}"><meta property="og:type" content="website"><meta property="og:url" content="{url}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet"><link rel="stylesheet" href="../style.css">{extra_head}
<script type="application/ld+json">{schema}</script>{ANALYTICS}</head><body>
{nav(1)}{body}{footer(1)}{SCRIPTS}{extra_scripts}</body></html>"""


def write_property_hub(posts):
    existing = [
        ("Apartments", "/blog/cost-segregation-apartment-buildings/"), ("Hotels", "/blog/cost-segregation-hotels/"),
        ("Restaurants", "/blog/cost-segregation-restaurants/"), ("Self Storage", "/blog/cost-segregation-self-storage-facilities/"),
        ("Medical Offices", "/blog/cost-segregation-medical-office-buildings/"), ("Warehouses", "/blog/cost-segregation-industrial-warehouse/"),
        ("Retail", "/blog/cost-segregation-retail-properties/"), ("Manufacturing", "/blog/cost-segregation-manufacturing-facilities/"),
        ("Car Washes", "/blog/cost-segregation-car-washes/"), ("Gas Stations", "/blog/cost-segregation-gas-stations-convenience-stores/"),
        ("RV Parks", "/blog/cost-segregation-rv-parks-campgrounds/"), ("Mobile Home Parks", "/blog/cost-segregation-mobile-home-parks/"),
    ]
    links = existing + [(p["title"].replace("Cost Segregation for ", ""), f'/blog/{p["slug"]}/') for p in posts]
    cards = "".join(f'<a class="card" href="{u}" style="text-decoration:none;"><h3>{html.escape(n)}</h3><p>See the assets, records, and tax questions that shape a study for this property type.</p></a>' for n, u in links)
    body = f"""<section class="hero" style="padding-bottom:60px;"><div class="container"><h1>Cost Segregation by <span>Property Type</span></h1><p>Every building has a different mix of structural systems, business assets, and land improvements. Find the guide for your property before requesting a study.</p><div class="hero-buttons"><a href="../cost-segregation-calculator/index.html" class="btn btn-gold">Estimate Potential Savings &rarr;</a></div></div></section>
<section class="section"><div class="container"><h2 class="section-title">Choose Your Property Type</h2><p class="section-subtitle">These guides explain what a study team reviews, which documents help, and which ownership or use questions to resolve.</p><div class="card-grid">{cards}</div></div></section>
<section class="section section-alt"><div class="container" style="max-width:900px;"><h2 class="section-title">A Guide Is the Starting Point</h2><p>Property type suggests where short-life components may exist, but it does not decide classification. The report must connect each asset to its function, source cost, tax ownership, and placed-in-service date. Stratum performs that analysis; AE Tax Advisors handles discovery calls and broader tax planning conversations.</p><div class="cta-banner"><h2>Talk Through Your Property</h2><p>Bring your basis, placed-in-service date, land allocation, and renovation history.</p><a class="btn btn-gold" href="{AE_BOOKING}">Book a Free AE Tax Advisors Call &rarr;</a></div></div></section>"""
    out = ROOT / "property-types"; out.mkdir(exist_ok=True)
    (out / "index.html").write_text(page_shell("Cost Segregation by Property Type", "Browse detailed cost segregation guides for rental, commercial, hospitality, industrial, medical, retail, and specialty real estate.", "property-types", body), encoding="utf-8")


def write_calculator():
    description = "Estimate a range of first-year accelerated depreciation and potential tax deferral from a cost segregation study using transparent assumptions."
    body = f"""<section class="hero" style="padding-bottom:60px;"><div class="container"><h1>Cost Segregation <span>Calculator</span></h1><p>Estimate a planning range for accelerated depreciation. See every assumption, then discuss the result with your tax advisor.</p></div></section>
<section class="section"><div class="container calc-layout"><form class="calc-panel" id="costseg-calculator"><h2>Property Inputs</h2>
<div class="form-group"><label for="basis">Depreciable building basis, excluding land</label><input id="basis" type="number" min="0" step="1000" value="800000" inputmode="decimal"></div>
<div class="form-row"><div class="form-group"><label for="property-type">Property type</label><select id="property-type"><option value="15,30">Single-family or vacation rental</option><option value="20,35">Multifamily</option><option value="15,30">Office</option><option value="20,35">Retail or shopping center</option><option value="25,40">Restaurant</option><option value="15,30">Warehouse or industrial</option><option value="25,40">Hotel or hospitality</option><option value="20,35">Self storage</option><option value="20,35">Medical or dental</option><option value="15,30">Other commercial property</option></select></div>
<div class="form-group"><label for="recovery">Building recovery period</label><select id="recovery"><option value="27.5">27.5-year residential rental</option><option value="39">39-year nonresidential</option></select></div></div>
<div class="form-row"><div class="form-group"><label for="tax-rate">Combined marginal tax rate</label><div class="input-suffix"><input id="tax-rate" type="number" min="0" max="60" step="1" value="32"><span>%</span></div></div>
<div class="form-group"><label for="bonus-rate">Bonus depreciation assumption</label><div class="input-suffix"><input id="bonus-rate" type="number" min="0" max="100" step="1" value="100"><span>%</span></div></div></div>
<button class="btn btn-gold" type="submit">Update Estimate</button><p class="calc-note">Use the bonus percentage your tax advisor confirms for the property's placed-in-service date and facts.</p></form>
<div class="calc-results" aria-live="polite"><p class="eyebrow">Planning estimate</p><h2>Potential first-year impact</h2><div class="result-grid"><div><span>Basis reclassified</span><strong id="reclass-result">$0 to $0</strong></div><div><span>Additional first-year depreciation</span><strong id="deduction-result">$0 to $0</strong></div><div><span>Potential federal and state tax deferral</span><strong id="savings-result">$0 to $0</strong></div></div><div class="assumptions" id="assumptions"></div><a href="{AE_BOOKING}" class="btn btn-outline">Review This Estimate with AE Tax Advisors &rarr;</a></div></div></section>
<section class="section section-alt"><div class="container" style="max-width:900px;"><h2 class="section-title">How the Estimate Works</h2><p>The calculator applies a low and high reclassification assumption to the depreciable building basis. It estimates first-year depreciation on that short-life basis using the bonus percentage you enter plus a 15% blended first-year MACRS assumption on the remaining short-life basis. It compares that amount with straight-line building depreciation.</p><p>The result is a range, not a quote or tax opinion. It does not model passive-activity loss limits, real estate professional status, the short-term rental material-participation rules, state depreciation adjustments, interest limits, at-risk limits, recapture, or time value of money. A study determines classification; a tax advisor determines how the deduction fits your return.</p><h2>What to Do Next</h2><p>Gather the closing statement, land allocation, depreciation schedule, placed-in-service date, renovation costs, and any construction drawings. Browse the <a href="../property-types/index.html">property type guides</a>, then use the estimate to frame a discovery call.</p></div></section>"""
    scripts = r"""<script>(function(){
const f=document.getElementById('costseg-calculator'),money=new Intl.NumberFormat('en-US',{style:'currency',currency:'USD',maximumFractionDigits:0});
function calculate(e){if(e)e.preventDefault();const basis=Math.max(0,Number(document.getElementById('basis').value)||0),parts=document.getElementById('property-type').value.split(',').map(Number),life=Number(document.getElementById('recovery').value),tax=Math.max(0,Number(document.getElementById('tax-rate').value)||0)/100,bonus=Math.min(1,Math.max(0,Number(document.getElementById('bonus-rate').value)||0)/100),baseRate=1/life,shortRate=bonus+(1-bonus)*.15;
const lowBasis=basis*parts[0]/100,highBasis=basis*parts[1]/100,lowExtra=Math.max(0,lowBasis*(shortRate-baseRate)),highExtra=Math.max(0,highBasis*(shortRate-baseRate));
document.getElementById('reclass-result').textContent=money.format(lowBasis)+' to '+money.format(highBasis);document.getElementById('deduction-result').textContent=money.format(lowExtra)+' to '+money.format(highExtra);document.getElementById('savings-result').textContent=money.format(lowExtra*tax)+' to '+money.format(highExtra*tax);document.getElementById('assumptions').innerHTML='<strong>Assumptions used:</strong> '+parts[0]+'% to '+parts[1]+'% reclassified, '+Math.round(bonus*100)+'% bonus depreciation, '+life+'-year building life, and '+Math.round(tax*100)+'% combined marginal rate.';}
f.addEventListener('submit',calculate);f.addEventListener('input',calculate);calculate();})();</script>"""
    schema = {"@type": "WebApplication", "name": "Cost Segregation Calculator", "url": f"{BASE_URL}/cost-segregation-calculator/", "applicationCategory": "FinanceApplication", "operatingSystem": "Any", "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}}
    out = ROOT / "cost-segregation-calculator"; out.mkdir(exist_ok=True)
    (out / "index.html").write_text(page_shell("Cost Segregation Calculator", description, "cost-segregation-calculator", body, schema, extra_scripts=scripts), encoding="utf-8")


def add_home_links():
    path = ROOT / "index.html"; content = path.read_text(encoding="utf-8")
    cards = ('      <div class="card"><h3><a href="cost-segregation-calculator/index.html">Cost segregation calculator</a></h3><p>Estimate a transparent range for accelerated depreciation and potential tax deferral.</p></div>\n'
             '      <div class="card"><h3><a href="property-types/index.html">Property type guides</a></h3><p>Explore the assets and records that shape studies across residential and commercial real estate.</p></div>\n')
    # Remove an earlier generated pair so the operation remains idempotent if the
    # surrounding homepage sections are rearranged.
    content = content.replace(cards, "").replace(cards + "      \n", "")
    topic_heading = '<h2 class="section-title" id="topics-heading">'
    start = content.find(topic_heading)
    if start >= 0:
        grid = content.find('<div class="card-grid">', start)
        if grid >= 0:
            insert_at = grid + len('<div class="card-grid">')
            content = content[:insert_at] + "\n" + cards + content[insert_at:]
    path.write_text(content, encoding="utf-8")


def main():
    posts = make_posts()
    for post in posts: write_post(post, str(ROOT))
    update_blog_index(posts)
    write_property_hub(posts)
    write_calculator()
    add_home_links()
    total = rebuild_sitemap(posts)
    print(f"Built {len(posts)} property pages, calculator, and property hub")
    print(f"Sitemap: {total} URLs")


if __name__ == "__main__": main()
