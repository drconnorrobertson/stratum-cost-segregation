#!/usr/bin/env python3
"""Refresh trust, editorial, analytics, and durable location content site-wide."""

from __future__ import annotations

import html
import json
import re
from pathlib import Path

from stratum_render import AE_BOOKING, ANALYTICS, BASE_URL, SCRIPTS, footer, nav

ROOT = Path(__file__).parent
UPDATED = "September 22, 2026"

STATE_NAMES = {
    "al":"Alabama","az":"Arizona","ca":"California","co":"Colorado","fl":"Florida",
    "ga":"Georgia","id":"Idaho","il":"Illinois","in":"Indiana","ky":"Kentucky",
    "la":"Louisiana","ma":"Massachusetts","md":"Maryland","mi":"Michigan","mn":"Minnesota",
    "mo":"Missouri","nc":"North Carolina","ne":"Nebraska","nj":"New Jersey","nm":"New Mexico",
    "nv":"Nevada","ny":"New York","oh":"Ohio","ok":"Oklahoma","or":"Oregon",
    "pa":"Pennsylvania","sc":"South Carolina","tn":"Tennessee","tx":"Texas","ut":"Utah",
    "va":"Virginia","wa":"Washington","wi":"Wisconsin",
}

TRUST = """<div class="footer-trust">
    <div class="footer-trust-item"><span class="trust-icon">&#128736;</span> Engineering-Based Methodology</div>
    <div class="footer-trust-item"><span class="trust-icon">&#128196;</span> Component-Level Reporting</div>
    <div class="footer-trust-item"><span class="trust-icon">&#127968;</span> Nationwide Service</div>
    <div class="footer-trust-item"><span class="trust-icon">&#129309;</span> AE Tax Strategy Coordination</div>
  </div>"""

TRACKER = """<script>
  document.addEventListener('click',function(event){
    var link=event.target.closest('a[href*="aetaxadvisors.com/discovery"]');
    if(!link||!window.va)return;
    var placement=link.classList.contains('nav-cta')?'navigation':link.closest('.cta-banner')?'content-cta':link.closest('footer')?'footer':'inline';
    window.va('event',{name:'AE Discovery Click',data:{path:location.pathname,placement:placement}});
  });
</script>"""


def shell(title: str, desc: str, path: str, body: str, depth: int = 1, schema_type: str = "WebPage") -> str:
    url = f"{BASE_URL}/{path.strip('/')}/"
    ld = json.dumps({
        "@context":"https://schema.org", "@type":schema_type, "url":url,
        "name":title, "description":desc,
        "publisher":{"@type":"Organization","name":"Stratum Cost Segregation","url":BASE_URL},
        "dateModified":"2026-09-22",
    }, separators=(",", ":"))
    rel = "../" * depth
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{html.escape(title)}</title>
  <meta name="description" content="{html.escape(desc, quote=True)}">
  <meta property="og:title" content="{html.escape(title, quote=True)}">
  <meta property="og:description" content="{html.escape(desc, quote=True)}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{url}">
  <link rel="canonical" href="{url}">
  <link rel="stylesheet" href="{rel}style.css">
  <script type="application/ld+json">{ld}</script>
{ANALYTICS}
</head>
<body>
{nav(depth)}
{body}
{footer(depth)}
{SCRIPTS}
</body>
</html>
"""


def extract_location(old: str, path: Path):
    heading = re.search(r"<h1>Cost Segregation in <span>(.*?), ([A-Z]{2})</span></h1>", old)
    if not heading:
        return None
    city, state_code = heading.group(1), heading.group(2)
    state = STATE_NAMES.get(state_code.lower(), state_code)
    types = "rental homes, multifamily buildings, and furnished short-term rentals"
    m = re.search(r"market features (.*?), each with", old, re.I)
    if m:
        types = re.sub(r"<[^>]+>", "", m.group(1)).strip()
    else:
        m = re.search(r"for ([^,.]+(?:cabins|chalets|properties|homes|condos|cottages|rentals)[^,.]*)", old, re.I)
        if m and len(m.group(1)) < 120:
            types = m.group(1).strip()
    areas = "neighborhoods and submarkets across the local area"
    m = re.search(r"including properties in (.*?)\.", old, re.I)
    if not m:
        m = re.search(r"Properties in (.*?) are particularly", old, re.I)
    if m and len(m.group(1)) < 220:
        areas = re.sub(r"<[^>]+>", "", m.group(1)).strip()
    return city, state_code, state, types, areas


def location_body(city: str, code: str, state: str, types: str, areas: str) -> str:
    return f"""<section class="hero" style="padding-bottom:60px;">
  <div class="container"><h1>Cost Segregation in <span>{city}, {code}</span></h1>
    <p>Engineering-based cost segregation studies for rental and investment properties in {city}, {state}, coordinated with AE Tax Advisors.</p></div>
</section>
<main class="section"><div class="container article" style="max-width:820px;">
  <div class="article-review">Published by Dr. Connor Robertson, real estate entrepreneur and investor &middot; Tax review by <a href="https://www.aetaxadvisors.com/">AE Tax Advisors Tax Team</a> &middot; Reviewed {UPDATED} &middot; <a href="../editorial-policy/index.html">Editorial policy</a></div>
  <h2>Cost Segregation for {city} Investment Properties</h2>
  <p>Cost segregation is a property-level depreciation analysis. Instead of treating every part of a building as one long-life asset, the study documents components that may fall into shorter federal recovery periods. A {city} owner can use the analysis when evaluating a recently acquired property, a renovation, or an older asset that has continued under straight-line depreciation.</p>
  <p>Properties around {city} include {html.escape(types)}. Each asset has its own construction, renovation history, placed-in-service date, land allocation, and furnishing package. Those facts matter more to the study than a market-wide estimate. Stratum therefore begins with the owner’s records and the actual building rather than publishing a promised percentage or deduction.</p>

  <h2>Local Property Context</h2>
  <p>Owners often ask about studies for properties in {html.escape(areas)}. Neighborhood names help describe the service area, but they do not determine tax treatment. The useful inputs are the property’s depreciable basis and the costs tied to finishes, specialty electrical and plumbing, cabinetry, appliances, site work, landscaping, paving, furniture, and other components.</p>
  <p>For furnished short-term rentals, the inventory may also include beds, electronics, window treatments, décor, outdoor furniture, hot tubs, fire pits, and guest amenities. For long-term rentals and multifamily properties, turnover improvements, common areas, security systems, parking, and exterior work may require separate review. Classification depends on the facts and applicable federal authority.</p>

  <h2>What a Stratum Study Analyzes</h2>
  <p>The process starts by reconciling the building basis to closing documents and improvement records while separating nondepreciable land. The study team reviews available plans, photographs, appraisals, contractor detail, and owner records. Components are then identified, costed, and assigned to the relevant recovery categories with a stated methodology and supporting documentation.</p>
  <p>The final report is designed to give the owner and tax preparer a component-level schedule, the basis reconciliation, assumptions, photographs or source records, depreciation detail, and the authority used for classification. A report supports the tax position; it does not guarantee an examination result or a specific tax benefit.</p>

  <h2>Federal and {state} Tax Coordination</h2>
  <p>Cost segregation begins with federal depreciation rules, but the return impact depends on the owner’s tax profile. Bonus depreciation, passive activity limitations, at-risk rules, short-term rental participation, entity structure, state conformity, and future recapture can all change the timing or value of a deduction. {state} treatment may differ from the federal return and can change as law and guidance change.</p>
  <p>That is why calls from this site are scheduled with AE Tax Advisors. Stratum focuses on the property study. AE Tax Advisors considers how the study may fit the owner’s broader strategy and coordinates implementation questions with the return preparer. Property owners should obtain advice for their facts before relying on an estimate.</p>

  <h2>Records to Gather Before the Call</h2>
  <ul>
    <li>Closing statement, purchase agreement, and any appraisal or land allocation support</li>
    <li>Placed-in-service date and current depreciation schedule</li>
    <li>Renovation invoices, contractor draws, or fixed-asset detail</li>
    <li>Plans, inspection reports, listing photographs, and an amenities inventory</li>
    <li>Ownership entity, rental use, and the tax years under consideration</li>
  </ul>
  <p>Complete records improve the quality of the feasibility discussion. If documents are missing, the team can explain which alternatives may support the analysis and which assumptions would need to be disclosed.</p>

  <h2>When to Consider a Study</h2>
  <p>A study may be evaluated in the year a property is placed in service, after a substantial improvement, or later through a potential accounting-method change. Timing affects the available procedure and return filing. A feasibility review should compare likely timing benefits, study cost, holding period, passive-loss position, and the chance of future recapture. The site’s <a href="../cost-segregation-calculator/index.html">educational calculator</a> can organize a preliminary scenario, and the <a href="../property-types/index.html">property-type guides</a> explain common component groups.</p>

  <div class="cta-banner"><h2>Discuss Your {city} Property</h2>
    <p>Book a discovery call with AE Tax Advisors to review your facts and whether a Stratum cost segregation study may fit.</p>
    <a href="{AE_BOOKING}" class="btn btn-gold">Book a Free AE Tax Advisors Call &rarr;</a></div>
</div></main>"""


def refresh_locations() -> int:
    count = 0
    for path in sorted(ROOT.glob("cost-segregation-*/index.html")):
        if path.parent.name == "cost-segregation-calculator":
            continue
        old = path.read_text()
        data = extract_location(old, path)
        if not data:
            continue
        city, code, state, types, areas = data
        title = f"Cost Segregation in {city}, {code} | Stratum"
        desc = f"Cost segregation studies for {city}, {state} investment properties. Learn what the analysis covers and book a discovery call with AE Tax Advisors."
        path.write_text(shell(title, desc, path.parent.name, location_body(city, code, state, types, areas)))
        count += 1
    return count


def write_core_pages():
    about_body = f"""<section class="hero" style="padding-bottom:60px;"><div class="container"><h1>About <span>Stratum</span> Cost Segregation</h1><p>Property-level cost segregation analysis with tax strategy coordination through AE Tax Advisors.</p></div></section>
<main class="section"><div class="container article" style="max-width:820px;">
<h2>What Stratum Does</h2><p>Stratum Cost Segregation focuses on engineering-based analysis of rental and investment properties. The work connects a building’s actual components and costs to federal depreciation classifications so the property owner and tax preparer receive a documented schedule rather than a general percentage estimate.</p>
<p>A typical engagement begins with basis and land allocation records, plans or property photographs, improvement detail, and the placed-in-service history. The report describes its methodology, lists components and classifications, reconciles the analyzed basis, and records material assumptions.</p>
<h2>How Stratum and AE Tax Advisors Work Together</h2><p>Stratum produces the property study. AE Tax Advisors hosts the discovery calls linked throughout this website and considers how a study may fit the owner’s wider tax strategy. The owner’s return preparer remains responsible for filing positions and should confirm federal and state treatment for the relevant year.</p>
<h2>Our Publishing Standard</h2><p>Educational content is published by Dr. Connor Robertson, a real estate entrepreneur and investor. Tax content is reviewed by the <a href="https://www.aetaxadvisors.com/">AE Tax Advisors Tax Team</a>. We use primary tax authorities where practical, identify examples as illustrations, and avoid presenting estimated outcomes as guarantees. Read the <a href="../editorial-policy/index.html">full editorial policy</a>.</p>
<h2>What Owners Should Expect</h2><ul><li>A scope based on the actual property and available records</li><li>Transparent assumptions and basis reconciliation</li><li>Component-level schedules and cited classification methodology</li><li>Coordination with AE Tax Advisors and the owner’s tax preparer</li><li>Clear disclosure that tax results depend on individual facts</li></ul>
<div class="cta-banner"><h2>Start With Your Property Facts</h2><p>Book a discovery call with AE Tax Advisors to discuss whether a Stratum study may fit.</p><a href="{AE_BOOKING}" class="btn btn-gold">Book a Free AE Tax Advisors Call &rarr;</a></div>
</div></main>"""
    (ROOT/"about/index.html").write_text(shell("About Stratum Cost Segregation | Stratum + AE", "Learn how Stratum prepares property-level cost segregation studies and how AE Tax Advisors coordinates the tax strategy conversation.", "about", about_body))

    standards_body = f"""<section class="hero" style="padding-bottom:60px;"><div class="container"><h1>Cost Segregation <span>Study Standards</span></h1><p>What to expect from a well-documented property study and how to evaluate the deliverable.</p></div></section>
<main class="section"><div class="container article" style="max-width:820px;">
<h2>Evaluate the Method, Not a Promised Result</h2><p>Every property and taxpayer is different. A credible feasibility review starts with basis, land allocation, asset type, placed-in-service date, improvement records, use, holding period, and the owner’s tax position. Published percentages and testimonials cannot establish the result for another property.</p>
<h2>Core Deliverables</h2><ul><li>Reconciliation of the analyzed depreciable basis to owner records</li><li>Component-level asset listing with cost, recovery period, and method</li><li>Explanation of the costing and classification methodology</li><li>Source records, photographs, plans, or disclosed estimates supporting the analysis</li><li>Depreciation schedules and a clear list of assumptions</li><li>Technical authority for material classifications</li></ul>
<h2>Questions to Ask Any Provider</h2><ul><li>Who performs and reviews the analysis?</li><li>How is land separated from depreciable basis?</li><li>Which records are required and how are missing costs estimated?</li><li>Does the report reconcile to the depreciation schedule?</li><li>How are renovations, dispositions, and prior depreciation handled?</li><li>What support is available to the owner’s CPA?</li></ul>
<h2>Stratum and AE Tax Advisors</h2><p>Stratum focuses on the property report. AE Tax Advisors leads the discovery and strategy discussion so the owner can consider passive activity rules, bonus depreciation, state conformity, recapture, and other facts that affect implementation. A study documents classifications; it does not promise a particular deduction, refund, or examination outcome.</p>
<h2>Editorial Transparency</h2><p>Stratum does not publish anonymous or unverified testimonials as evidence of likely results. Educational content follows our <a href="../editorial-policy/index.html">editorial policy</a>, is dated, and separates illustrative examples from property-specific analysis.</p>
<div class="cta-banner"><h2>Request a Property Review</h2><p>Book a discovery call with AE Tax Advisors to discuss your records, timeline, and next steps.</p><a href="{AE_BOOKING}" class="btn btn-gold">Book a Free AE Tax Advisors Call &rarr;</a></div>
</div></main>"""
    (ROOT/"reviews/index.html").write_text(shell("Cost Segregation Study Standards | Stratum", "Review Stratum's cost segregation study standards, core deliverables, provider questions, and AE Tax Advisors coordination process.", "reviews", standards_body))

    editorial_body = """<section class="hero" style="padding-bottom:60px;"><div class="container"><h1>Editorial <span>Policy</span></h1><p>How Stratum creates, reviews, updates, and corrects educational tax content.</p></div></section>
<main class="section"><div class="container article" style="max-width:820px;">
<h2>Publisher and Review</h2><p>Stratum’s educational content is published by Dr. Connor Robertson, a real estate entrepreneur and investor. Tax content is reviewed by the <a href="https://www.aetaxadvisors.com/">AE Tax Advisors Tax Team</a>. Review identifies technical issues and areas where property owners should seek advice for their specific facts.</p>
<h2>Source Standard</h2><p>Writers prioritize primary authorities such as the Internal Revenue Code, Treasury Regulations, IRS publications and forms, the IRS Cost Segregation Audit Technique Guide, revenue procedures, and court decisions. Secondary explanations may be used for context but do not replace the underlying authority.</p>
<h2>Examples and Estimates</h2><p>Examples are educational illustrations. They do not promise a deduction, savings amount, study result, or examination outcome. Actual results depend on basis, land allocation, property components, dates, tax law, taxpayer participation, passive-loss limitations, state rules, and other facts.</p>
<h2>Updates and Corrections</h2><p>Pages show a review or modification date when practical. Material tax-law changes and identified factual errors are corrected in the published page. Readers can report a concern to <a href="mailto:info@stratumcostseg.com">info@stratumcostseg.com</a>.</p>
<h2>Roles and Disclosure</h2><p>Stratum focuses on cost segregation studies. AE Tax Advisors hosts discovery calls and broader tax strategy discussions for visitors referred from this site. This website provides general education and does not create a tax-advisor relationship. Owners should consult their tax professional before filing.</p>
<p style="margin-top:32px;color:var(--text-muted);">Last reviewed September 22, 2026.</p></div></main>"""
    (ROOT/"editorial-policy").mkdir(exist_ok=True)
    (ROOT/"editorial-policy/index.html").write_text(shell("Editorial Policy | Stratum Cost Segregation", "How Stratum Cost Segregation publishes, reviews, sources, updates, and corrects educational tax content.", "editorial-policy", editorial_body))


def update_json_ld(text: str) -> str:
    pattern = re.compile(r'<script type="application/ld\+json">(.*?)</script>', re.S)
    def repl(match):
        try:
            data = json.loads(match.group(1))
        except Exception:
            return match.group(0)
        nodes = data.get("@graph", [data]) if isinstance(data, dict) else []
        for node in nodes:
            if isinstance(node, dict) and node.get("@type") in ("BlogPosting", "Article"):
                node["author"] = {"@type":"Person","name":"Dr. Connor Robertson","url":"https://www.drconnorrobertson.com/"}
                node["reviewedBy"] = {"@type":"Organization","name":"AE Tax Advisors Tax Team","url":"https://www.aetaxadvisors.com/"}
                node["dateModified"] = "2026-09-22"
            if isinstance(node, dict):
                node.pop("aggregateRating", None)
                node.pop("review", None)
        return '<script type="application/ld+json">' + json.dumps(data, separators=(",", ":")) + '</script>'
    return pattern.sub(repl, text)


def postprocess_html() -> int:
    changed = 0
    for path in ROOT.rglob("*.html"):
        text = path.read_text()
        old = text
        text = re.sub(r'<div class="footer-trust">.*?</div>\s*<div class="footer-bottom">', TRUST + '\n  <div class="footer-bottom">', text, flags=re.S)
        text = text.replace('>Study Standards</a>', '>Study Standards</a>')
        text = re.sub(r'\s*<div class="footer-social">.*?</div>\s*</div>', '\n    </div>', text, flags=re.S)
        if "editorial-policy/index.html" not in text and "<h4>Resources</h4>" in text:
            text = text.replace("</ul>\n    </div>\n    <div>\n      <h4>Contact</h4>", '<li><a href="/editorial-policy/">Editorial Policy</a></li>\n      </ul>\n    </div>\n    <div>\n      <h4>Contact</h4>')
        text = text.replace('href="../../editorial-policy/index.html"', 'href="/editorial-policy/"')
        text = text.replace('href="../editorial-policy/index.html"', 'href="/editorial-policy/"')
        text = text.replace('href="editorial-policy/index.html"', 'href="/editorial-policy/"')
        if "/_vercel/insights/script.js" not in text and "</head>" in text:
            text = text.replace("</head>", ANALYTICS + "\n</head>")
        if "AE Discovery Click" not in text and "</body>" in text:
            text = text.replace("</body>", TRACKER + "\n</body>")
        if path.parent.parent.name == "blog" and 'class="article"' in text and "Published by" not in text:
            text = re.sub(r'<div class="meta">(.*?)</div>', r'<div class="meta">\1 &middot; Published by Dr. Connor Robertson &middot; Tax review by <a href="https://www.aetaxadvisors.com/">AE Tax Advisors Tax Team</a> &middot; <a href="../../editorial-policy/index.html">Editorial policy</a></div>', text, count=1, flags=re.S)
        if path.parent.parent.name == "blog" and 'class="article"' in text and "content-disclosure" not in text:
            disclosure = '<div class="content-disclosure"><strong>Educational illustration:</strong> Examples use stated assumptions and do not predict a property-specific deduction or tax outcome. Tax rules, eligibility, and return treatment depend on the facts and filing year.</div>'
            text = re.sub(r'(<div class="meta">.*?</div>)', r'\1\n  ' + disclosure, text, count=1, flags=re.S)
        text = update_json_ld(text)
        replacements = {
            "engineering-based":"engineering-based", "well-documented":"well-documented", "Documented Methodology":"Documented Methodology",
            "withstands IRS examination":"is designed to support review by the owner’s tax professional",
            "built to withstand IRS scrutiny":"documented for review by the owner’s tax professional",
            "Maximize depreciation deductions and accelerate tax savings":"Identify and document property components for depreciation analysis",
            "maximize depreciation deductions and accelerate tax savings":"identify and document property components for depreciation analysis",
        }
        for a, b in replacements.items():
            text = text.replace(a, b)
        if text != old:
            path.write_text(text)
            changed += 1
    return changed


def update_privacy():
    path = ROOT/"privacy/index.html"
    text = path.read_text()
    text = re.sub(r'<h2>Website technology</h2><p>.*?</p>', '<h2>Website analytics and technology</h2><p>This site uses Vercel Web Analytics to understand aggregate page use and measure clicks that send visitors to the AE Tax Advisors discovery page. Vercel Web Analytics is designed without cookies and reports anonymized usage data. The click event includes only the Stratum page path and CTA placement; it does not include tax, property, form, or contact information. This site also loads fonts from Google Fonts, and the hosting provider processes standard request data to deliver and protect the site.</p>', text, flags=re.S)
    path.write_text(text)


def update_home():
    path = ROOT/"index.html"
    text = path.read_text()
    text = re.sub(r'<div class="social-proof-bar">.*?</div>\s*<section class="section">', '<div class="social-proof-bar"><p>Engineering-based property studies &nbsp;&bull;&nbsp; Transparent assumptions &nbsp;&bull;&nbsp; Tax strategy coordination with AE Tax Advisors</p></div>\n<section class="section">', text, count=1, flags=re.S)
    text = re.sub(r'<div class="stats">.*?</div>\s*</div>\s*</section>', '''<div class="stats">
      <div class="stat-item fade-in-up"><div class="stat-num">5, 7 &amp; 15</div><div class="stat-label">Year Property Classes Analyzed</div></div>
      <div class="stat-item fade-in-up"><div class="stat-num">50</div><div class="stat-label">States Served</div></div>
      <div class="stat-item fade-in-up"><div class="stat-num">1</div><div class="stat-label">Component-Level Report</div></div>
    </div></div></section>''', text, count=1, flags=re.S)
    text = text.replace("<h3>IRS Audit Protection</h3>", "<h3>Documented Methodology</h3>")
    path.write_text(text)


def harden_claims():
    """Remove absolute outcome statements from high-intent core pages."""
    targets = [ROOT/"faq/index.html", ROOT/"short-term-rental-cost-segregation/index.html", ROOT/"long-term-rental-cost-segregation/index.html"]
    replacements = {
        "Any owner of residential rental property can benefit from a cost segregation study.": "Owners of residential rental property may benefit from a cost segregation study when the expected timing benefit supports the study cost and fits their tax position.",
        "The fee is tax-deductible as a business expense, and the tax savings from the study typically exceed the cost by 5x to 20x.": "Ask your tax advisor how the study fee should be treated and compare the fee with a property-specific feasibility estimate.",
        "No. A cost segregation study does not increase your audit risk.": "A study by itself does not establish whether a return will be examined, and no provider can predict audit selection.",
        "This approach is accepted by the IRS and allows us to serve property investors in all 50 states without requiring an on-site visit.": "The appropriate scope depends on the building, available records, materiality, and the evidence needed to support the analysis.",
        "We have completed studies in every major market and vacation rental destination in the country.": "Service availability and the required study scope are confirmed during intake.",
        "Yes. The fee for a cost segregation study is fully tax-deductible as a business expense (investment expense) in the year it is paid. This further increases the return on investment of the study.": "Treatment of the study fee depends on the taxpayer's facts and accounting method. Ask the return preparer whether and when the fee may be deducted or capitalized.",
        "Savings vary based on property value, type, and your tax bracket. As a general rule, a cost segregation study can accelerate 20-40% of your property's depreciable basis into 5, 7, and 15-year categories. For a $400,000 property, this could mean $60,000 to $120,000 in first-year deductions, translating to $15,000 to $45,000 in tax savings depending on your marginal tax rate.": "Results depend on the building components, depreciable basis, land allocation, placed-in-service date, current law, passive-loss position, and state rules. A property-specific feasibility review is required; Stratum does not promise a reclassification percentage or tax-savings amount.",
        "Without a cost segregation study, your $500,000 vacation rental is depreciated straight-line over 27.5 years, yielding roughly $18,000 per year in depreciation. With a cost segregation study, 25-40% of that cost basis can be reclassified into 5, 7, and 15-year property, generating $75,000 to $150,000 or more in first-year deductions when combined with bonus depreciation.": "A short-term rental study separates land, long-life building costs, shorter-life components, and land improvements based on the property's records. The first-year effect depends on the actual component costs, placed-in-service date, applicable bonus-depreciation rules, and whether the owner can currently use the resulting deductions.",
    }
    for path in targets:
        if not path.exists():
            continue
        text = path.read_text()
        for old, new in replacements.items():
            text = text.replace(old, new)
        path.write_text(text)

    case = ROOT/"blog/cost-segregation-case-study-vacation-rental/index.html"
    if case.exists():
        text = case.read_text()
        text = text.replace("A hypothetical Gatlinburg vacation-rental example showing how basis assumptions and component classifications can affect depreciation timing.", "A hypothetical Gatlinburg vacation-rental example showing how basis assumptions and component classifications can affect depreciation timing.")
        text = text.replace("The investor's estimated first-year tax savings exceeded $45,000, representing a return of more than 12x the cost of the study. Over the first five years of ownership, the cumulative tax benefit was projected at approximately $65,000 in present-value terms.", "Under the stated hypothetical assumptions, the model changes the timing of depreciation. It is not a client result or a prediction. An owner would still need a property-specific study and tax analysis covering loss limitations, state conformity, recapture, and the law for the filing year.")
        text = text.replace("Cost Segregation Case Study:", "Hypothetical Cost Segregation Example:")
        case.write_text(text)
    index = ROOT/"blog/index.html"
    if index.exists():
        text = index.read_text().replace("A hypothetical Gatlinburg vacation-rental example showing how basis assumptions and component classifications can affect depreciation timing.", "A hypothetical Gatlinburg vacation-rental example showing how basis and component assumptions affect depreciation timing.")
        text = text.replace("Cost Segregation Case Study:", "Hypothetical Cost Segregation Example:")
        index.write_text(text)


if __name__ == "__main__":
    cities = refresh_locations()
    write_core_pages()
    update_privacy()
    update_home()
    harden_claims()
    pages = postprocess_html()
    print(f"Refreshed {cities} location pages and postprocessed {pages} HTML files.")
