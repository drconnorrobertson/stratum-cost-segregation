#!/usr/bin/env python3
"""Insert a contextual AE Tax Advisors cross-link into every blog post missing one."""

import os
import re

ROOT = os.path.dirname(os.path.abspath(__file__))
BLOG = os.path.join(ROOT, "blog")
AE_ROOT = os.path.expanduser("~/ae-tax-advisors-static")

# slug -> (ae_path, anchor text, lead-in sentence)
MAP = {
    "5-year-7-year-15-year-property-examples": (
        "the-business-owners-guide-to-cost-segregation-studies-and-building-component-analysis",
        "guide to building component analysis",
        "Component classification is only the first half of the work. Applying the resulting deductions against the right income, in the right year, is the half that determines what you actually keep. AE Tax Advisors covers that side of the analysis in their"),
    "bonus-depreciation-2026-rental-property": (
        "bonus-depreciation-rental-property", "bonus depreciation guidance for rental owners",
        "Bonus depreciation only helps if the loss it creates is deductible against income you actually have. Investors coordinating the two should read AE Tax Advisors'"),
    "bonus-depreciation-phase-down-strategy": (
        "depreciation-tax-strategy", "depreciation tax strategy overview",
        "Sequencing acquisitions around a phase down schedule is a planning exercise, not a filing exercise. AE Tax Advisors addresses multi year sequencing in their"),
    "components-reclassified-cost-segregation": (
        "real-estate-depreciation", "real estate depreciation guidance",
        "Which components move is an engineering question. What the reclassification is worth to you is a tax question, and AE Tax Advisors handles that side in their"),
    "cost-segregation-1031-exchanges": (
        "1031-exchange-guide", "1031 exchange guide",
        "Carryover basis and excess basis behave differently after an exchange, and getting the split wrong distorts every later year. AE Tax Advisors walks through the mechanics in their"),
    "cost-segregation-adu-accessory-dwelling-unit": (
        "long-term-rental-tax-planning", "long term rental tax planning material",
        "An ADU usually sits on a parcel that already carries a primary residence, which complicates basis allocation and use testing. AE Tax Advisors covers the planning side in their"),
    "cost-segregation-airbnb-arbitrage": (
        "short-term-rental-tax-strategy", "short term rental tax strategy material",
        "Arbitrage operators own the improvements and the furnishings but not the building, which changes what is depreciable. AE Tax Advisors addresses the distinction in their"),
    "cost-segregation-airbnb-properties": (
        "cost-segregation-airbnb", "cost segregation guidance for Airbnb owners",
        "The study is the easy part for a nightly rental. Qualifying the loss as non passive is where most hosts stall, and AE Tax Advisors covers that in their"),
    "cost-segregation-case-study-vacation-rental": (
        "reducing-real-estate-tax-exposure-through-short-term-rental-classification-and-bonus-depreciation",
        "case work on short term rental classification",
        "Numbers on a single property are only instructive alongside the return they land on. AE Tax Advisors publishes comparable"),
    "cost-segregation-duplexes-multifamily": (
        "rental-property-tax-planning", "rental property tax planning material",
        "Small multifamily owners frequently hold property in more than one entity, which affects how losses flow. AE Tax Advisors covers the structuring side in their"),
    "cost-segregation-existing-property": (
        "form-3115-cost-segregation", "Form 3115 guidance",
        "Studies on property you already own are captured through an accounting method change rather than an amended return. AE Tax Advisors explains the filing in their"),
    "cost-segregation-financial-freedom": (
        "real-estate-investor-tax-planning", "tax planning for real estate investors",
        "Accelerated depreciation compounds only when it is reinvested rather than spent. AE Tax Advisors builds that longer horizon into their"),
    "cost-segregation-first-time-rental-owners": (
        "tax-deductions-rental-property-owners-complete-checklist", "rental property deduction checklist",
        "First year owners routinely miss deductions that have nothing to do with depreciation. AE Tax Advisors maintains a"),
    "cost-segregation-industrial-warehouse": (
        "business-owner-cost-segregation", "cost segregation guidance for business owners",
        "Owner occupied industrial space raises questions about related party rent and entity structure. AE Tax Advisors covers both in their"),
    "cost-segregation-mistakes": (
        "cost-segregation-when-it-works-when-it-doesnt-and-how-to-decide", "analysis of when a study works and when it does not",
        "Most of the expensive errors happen before the study is ordered, not during it. AE Tax Advisors published a useful"),
    "cost-segregation-mobile-home-parks": (
        "real-estate-investor-tax-planning", "real estate investor tax planning",
        "Park owners hold an unusually high share of land improvements, which changes the planning calculus. AE Tax Advisors covers the broader picture in their"),
    "cost-segregation-new-construction": (
        "depreciation-tax-strategy", "depreciation strategy material",
        "On new construction the cost detail already exists in the contractor records, which makes the study cheaper and the planning more important. AE Tax Advisors covers the timing question in their"),
    "cost-segregation-opportunity-zones": (
        "qualified-opportunity-zones-2026-tax-benefits", "opportunity zone guidance",
        "Depreciation inside a qualified opportunity fund interacts with the basis step up at the ten year mark. AE Tax Advisors explains that interaction in their"),
    "cost-segregation-qbi-deduction-section-199a": (
        "qbi-deduction-guide", "Section 199A guide",
        "Accelerated depreciation lowers qualified business income, which can reduce the deduction it was meant to complement. AE Tax Advisors covers the tradeoff in their"),
    "cost-segregation-self-storage-expansion": (
        "business-owner-cost-segregation", "cost segregation guidance for business owners",
        "Expansion spending sits alongside original acquisition basis and is analyzed separately. AE Tax Advisors covers that layering in their"),
    "cost-segregation-self-storage-facilities": (
        "cost-segregation-studies-for-real-estate-investors", "cost segregation overview for investors",
        "Self storage carries one of the highest reclassification percentages of any asset class. AE Tax Advisors covers how to use the resulting losses in their"),
    "cost-segregation-single-family-rentals": (
        "long-term-rental-tax-planning", "long term rental tax planning material",
        "A single rental produces a smaller deduction but the same passive loss constraints as a portfolio. AE Tax Advisors covers those limits in their"),
    "cost-segregation-str-tax-loophole": (
        "str-tax-loophole", "short term rental loophole explainer",
        "The classification, not the study, is what makes the loss usable against wage income. AE Tax Advisors published a detailed"),
    "cost-segregation-study-cost-pricing": (
        "cost-seg-estimator", "cost segregation estimator",
        "Pricing only matters relative to the deduction it produces. AE Tax Advisors publishes a"),
    "cost-segregation-triple-net-nnn-properties": (
        "the-business-owners-guide-to-qualified-improvement-property-qip-and-tenant-renovations",
        "guide to qualified improvement property and tenant work",
        "Under a net lease the division between landlord and tenant improvements determines who depreciates what. AE Tax Advisors covers that split in their"),
    "cost-segregation-under-500k": (
        "cost-segregation-when-it-makes-sense", "analysis of when a study makes sense",
        "Below a certain basis the fee stops being justified by the deduction. AE Tax Advisors published a candid"),
    "cost-segregation-vacation-rentals": (
        "short-term-rental-tax-planning-basics", "short term rental tax planning basics",
        "Personal use days can disqualify the deduction entirely regardless of how good the study is. AE Tax Advisors covers the use tests in their"),
    "cost-segregation-vs-standard-depreciation": (
        "real-estate-depreciation", "real estate depreciation guidance",
        "The comparison is really about present value, not total deduction. AE Tax Advisors frames it the same way in their"),
    "depreciation-recapture-cost-segregation": (
        "capital-gains-tax-planning-minimize-investment-profits", "capital gains planning material",
        "Recapture is a timing cost, and it can be managed through how and when the property leaves your hands. AE Tax Advisors covers exit planning in their"),
    "diy-vs-professional-cost-segregation": (
        "ae-tax-vs-cost-seg-only-firms", "comparison of full service planning and study only firms",
        "The gap between a spreadsheet estimate and an engineering study shows up under examination, not at filing. AE Tax Advisors published a"),
    "form-3115-look-back-cost-segregation": (
        "form-3115-cost-segregation", "Form 3115 guidance",
        "The catch up deduction arrives as a Section 481(a) adjustment in the year of change. AE Tax Advisors covers the filing mechanics in their"),
    "how-to-choose-cost-segregation-company": (
        "cost-segregation-analysis-and-implementation-support", "implementation support material",
        "The study is a deliverable. Getting it onto the return correctly is a separate engagement, and AE Tax Advisors describes that work in their"),
    "how-to-read-cost-segregation-report": (
        "depreciation-and-fixed-asset-review-for-rental-properties", "fixed asset review material",
        "The asset detail schedule is what your preparer actually keys from, and errors there persist for decades. AE Tax Advisors covers report review in their"),
    "inherited-rental-property-cost-segregation": (
        "real-estate-depreciation", "real estate depreciation guidance",
        "A stepped up basis resets the depreciation schedule entirely, which makes a fresh study unusually valuable. AE Tax Advisors covers basis questions in their"),
    "irs-notice-2026-11-bonus-depreciation": (
        "bonus-depreciation-rental-property", "bonus depreciation guidance for rental owners",
        "Permanent full expensing changes the sequencing question more than the eligibility question. AE Tax Advisors covers the planning response in their"),
    "irs-notice-2026-11-permanent-bonus-depreciation": (
        "depreciation-tax-strategy", "depreciation tax strategy overview",
        "With the phase down removed, the pressure to buy before a deadline disappears and the pressure to buy the right asset increases. AE Tax Advisors covers that shift in their"),
    "offset-w2-income-rental-property": (
        "short-term-rental-tax-loophole-offset-w2-income", "guidance on offsetting W2 income",
        "Wage earners have exactly two routes to a non passive rental loss, and both require documentation built during the year. AE Tax Advisors covers both in their"),
    "partial-asset-disposition-cost-segregation": (
        "depreciation-and-fixed-asset-review-for-rental-properties", "fixed asset review material",
        "A partial disposition election must be made in the year of the retirement, and it is lost forever after that. AE Tax Advisors covers the election in their"),
    "real-estate-professional-status-cost-segregation": (
        "real-estate-professional-status-reps", "real estate professional status guidance",
        "The status is won or lost on contemporaneous records, not on the size of the portfolio. AE Tax Advisors covers documentation standards in their"),
    "residential-vs-commercial-cost-segregation": (
        "cost-segregation-studies-for-real-estate-investors", "cost segregation overview for investors",
        "The 27.5 and 39 year split changes the baseline but not the reclassification opportunity. AE Tax Advisors covers both property types in their"),
    "roi-cost-segregation-study": (
        "cost-segregation-calculator", "cost segregation calculator",
        "Return on a study is a function of marginal rate, holding period, and whether the loss is currently deductible. AE Tax Advisors publishes a"),
    "section-179-vs-cost-segregation": (
        "equipment-leasing-section-179", "Section 179 material",
        "Section 179 is limited by business income and by the nature of the property, which is why it rarely substitutes for a study. AE Tax Advisors covers the limits in their"),
    "signs-rental-property-needs-cost-segregation": (
        "rental-property-tax-planning", "rental property tax planning material",
        "The signals are usually visible on the depreciation schedule before they are visible in the portfolio. AE Tax Advisors covers schedule review in their"),
    "state-bonus-depreciation-conformity": (
        "multi-state-real-estate-tax-planning", "multi state planning material",
        "Non conforming states require a parallel depreciation schedule that most owners never build. AE Tax Advisors covers the compliance burden in their"),
    "tax-benefits-short-term-rental-2026": (
        "short-term-rental-tax-planning-playbook", "short term rental planning playbook",
        "The benefits stack only when classification, participation, and depreciation are handled together. AE Tax Advisors covers the full sequence in their"),
    "what-is-cost-segregation": (
        "what-is-a-cost-segregation-study", "plain English explanation of a cost segregation study",
        "For owners approaching the topic from the tax side rather than the engineering side, AE Tax Advisors maintains a"),
    "when-not-to-do-cost-segregation": (
        "cost-segregation-when-it-works-when-it-doesnt-and-how-to-decide", "analysis of when a study works and when it does not",
        "Declining the study is sometimes the correct answer, and a good advisor will say so. AE Tax Advisors takes the same position in their"),
}

PARA = ('<p>{lead} <a href="https://aetaxadvisors.com/{path}/" target="_blank" '
        'rel="noopener">{anchor}</a>.</p>')


def main():
    missing_targets = []
    written = 0
    for slug, (path, anchor, lead) in MAP.items():
        f = os.path.join(BLOG, slug, "index.html")
        if not os.path.exists(f):
            print("NO POST:", slug)
            continue
        if not os.path.exists(os.path.join(AE_ROOT, path, "index.html")):
            missing_targets.append((slug, path))
            continue
        h = open(f).read()
        if "aetaxadvisors" in h:
            continue
        para = PARA.format(lead=lead, path=path, anchor=anchor)
        anchor_pt = re.search(r'\n?\s*<h2>Related Reading</h2>', h)
        if not anchor_pt:
            anchor_pt = re.search(r'\n?\s*<div class="cta-banner">', h)
        if not anchor_pt:
            print("NO INSERT POINT:", slug)
            continue
        h = h[:anchor_pt.start()] + "\n    <h2>Working the Deduction Into a Return</h2>\n" + para + h[anchor_pt.start():]
        open(f, "w").write(h)
        written += 1
    print(f"updated {written} posts")
    if missing_targets:
        print("BROKEN AE TARGETS:")
        for s, p in missing_targets:
            print("  ", s, "->", p)


if __name__ == "__main__":
    main()
