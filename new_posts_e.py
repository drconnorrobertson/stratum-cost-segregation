#!/usr/bin/env python3
"""Batch E: 15 long-tail cost segregation posts (part 2 of 2)."""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from stratum_render import write_post  # noqa: E402

ROOT = os.path.dirname(os.path.abspath(__file__))
DATE = "August 10, 2026"
ISO = "2026-08-10"

AE = "https://aetaxadvisors.com"


def ae(path, text):
    return f'<a href="{AE}/{path}/" target="_blank" rel="noopener">{text}</a>'


POSTS = [
    {
        "slug": "de-minimis-safe-harbor-vs-cost-segregation",
        "title": "De Minimis Safe Harbor vs Cost Segregation: Two Different Tools for Two Different Problems",
        "description": "The de minimis safe harbor expenses small purchases. Cost segregation reclassifies acquisition basis. They are complementary, not alternatives, and using only one leaves deductions behind.",
        "date": DATE,
        "iso_date": ISO,
        "sections": [
            ("Two Tools That Get Confused for Each Other", """<p>Owners regularly ask whether they should elect the de minimis safe harbor or run a cost segregation study, as though the two were competing options. They address entirely different parts of the depreciation problem.</p>
<p>The de minimis safe harbor deals with what you buy after you own the property: appliances, furniture, tools, small improvements. Cost segregation deals with the lump sum you paid to acquire the property in the first place.</p>
<p>A well-run rental uses both. Electing the safe harbor does nothing to unlock the 5-year and 15-year property buried in your purchase price, and a cost segregation study does nothing to simplify the treatment of the dishwasher you bought last month.</p>"""),
            ("What the Safe Harbor Does", """<p>Regulation 1.263(a)-1(f) allows a taxpayer to elect to expense amounts paid for tangible property that would otherwise be capitalized, up to a per-item or per-invoice threshold. The threshold is $5,000 for taxpayers with an applicable financial statement, meaning an audited financial statement, and $2,500 for everyone else.</p>
<p>Most individual real estate investors fall in the $2,500 category. That covers the large majority of furniture, appliance, and equipment purchases on a residential rental.</p>
<p>The election is made annually on a timely filed return, including extensions. It requires accounting procedures in place at the beginning of the tax year treating such amounts as expenses for book purposes. That written policy requirement is real, and it is the piece most owners skip.</p>"""),
            ("What Cost Segregation Does", """<p>A cost segregation study takes the depreciable basis of an acquired or constructed building, ordinarily recovered over 27.5 or 39 years, and identifies the components that properly belong in shorter recovery classes under MACRS.</p>
<p>Carpeting, cabinetry, decorative lighting, dedicated electrical, and specialty plumbing become 5-year or 7-year personal property. Paving, fencing, landscaping, and site utilities become 15-year land improvements. On a typical residential rental, 20 to 30 percent of depreciable basis moves.</p>
<p>The safe harbor cannot reach any of this, because the building was acquired as a single asset for a single price. There is no invoice for the cabinetry to apply a $2,500 threshold to.</p>"""),
            ("The Other Tangible Property Elections Worth Knowing", """<p>The regulations contain two more provisions that sit alongside the safe harbor. The routine maintenance safe harbor in Regulation 1.263(a)-3(i) permits deduction of recurring activities expected to be performed more than once during a ten-year period for buildings, keeping ordinary upkeep out of capitalization.</p>
<p>The safe harbor for small taxpayers in Regulation 1.263(a)-3(h) permits taxpayers with average annual gross receipts of $10 million or less to expense improvements to a building with an unadjusted basis of $1 million or less, capped at the lesser of $10,000 or 2 percent of unadjusted basis.</p>
<p>That last one is genuinely useful for small residential portfolios and almost entirely unknown outside professional practice. AE Tax Advisors walks through the full set in their """ + ae("real-estate-depreciation", "real estate depreciation") + """ guidance.</p>"""),
            ("Where the Two Interact", """<p>The interaction point is a renovation. Suppose you acquire a property for $700,000 and immediately spend $90,000 on improvements before placing it in service.</p>
<p>The $700,000 is acquisition basis, and cost segregation applies. The $90,000 of improvement work is a separate matter. Individual invoices under $2,500 can be expensed under the safe harbor if elected. Larger invoices are capitalized, and those capitalized improvements can themselves be cost segregated, because a new roof, new flooring, and new site work carry different recovery periods.</p>
<p>Owners who expense everything under the safe harbor without regard to invoice size take an aggressive position that will not survive review. Owners who capitalize everything into 27.5-year property give away deductions they were entitled to.</p>"""),
            ("Why Bonus Depreciation Blurs the Distinction Right Now", """<p>With 100 percent bonus depreciation available for qualifying property, the practical outcome of the safe harbor and of reclassifying an asset to 5-year property is often the same: full deduction in year one.</p>
<p>The difference is administrative. Safe harbor items never enter the depreciation schedule, so there is nothing to track, nothing to dispose of, and no recapture on sale as Section 1245 property. Bonus-depreciated 5-year assets do sit on the schedule and are subject to recapture at ordinary rates on disposition.</p>
<p>For high-turnover items in a short-term rental, that recapture difference is a genuine reason to prefer the safe harbor where both are available.</p>"""),
            ("What to Put in Place", """<p>Adopt a written capitalization policy before the tax year begins, setting the threshold at $2,500 per item or invoice. Keep it with your records. It costs nothing and it is a prerequisite for the election.</p>
<p>Ask your preparer to make the annual election on the return. It is a statement attached to the return, and it is easy to omit when the return is prepared under deadline pressure.</p>
<p>Then run the cost segregation analysis separately on the acquisition basis and on any capitalized improvement projects. The two workstreams do not overlap, and treating them as alternatives is how owners end up with less deduction than they were entitled to on both fronts.</p>"""),
        ],
        "related": [
            ("str-furniture-ffe-depreciation", "Furniture and Equipment in a Short-Term Rental"),
            ("qualified-improvement-property-cost-segregation", "Qualified Improvement Property"),
            ("cost-segregation-new-construction", "Cost Segregation on New Construction"),
        ],
    },
    {
        "slug": "cost-segregation-selling-property-early",
        "title": "What Happens if You Sell Two Years After a Cost Segregation Study?",
        "description": "Selling shortly after accelerating depreciation triggers recapture at ordinary rates on 1245 property. Here is how to model whether a short-hold study still comes out ahead.",
        "date": DATE,
        "iso_date": ISO,
        "sections": [
            ("The Question Every Short-Hold Investor Should Ask First", """<p>Cost segregation is usually described as a timing strategy: you accelerate deductions into early years and give some of it back later. Over a long hold, the time value of money makes that trade clearly favorable.</p>
<p>Over a two-year hold, it is not obvious. You take a large deduction in year one, sell in year three, and a meaningful portion of what you deducted comes back as ordinary income. Whether you come out ahead depends on rate differentials, your discount rate, and the composition of the reclassified property.</p>
<p>The answer is frequently still yes, but it is close enough that it deserves a calculation rather than an assumption.</p>"""),
            ("What Comes Back and at What Rate", """<p>Two recapture regimes apply, and they behave differently.</p>
<p>Section 1245 recapture applies to the 5-year and 7-year personal property identified in your study. On sale, depreciation taken on that property is recaptured as ordinary income to the extent of gain. There is no preferential rate. For a taxpayer in the 37 percent bracket, this is recaptured at 37 percent.</p>
<p>Unrecaptured Section 1250 gain applies to the 27.5-year or 39-year structural component. It is taxed at a maximum of 25 percent. Land improvements at 15 years are Section 1250 property, so they also fall under the 25 percent treatment rather than ordinary recapture.</p>
<p>The composition of your study therefore matters a great deal to the short-hold analysis. A study heavy in 15-year land improvements recaptures more gently than one heavy in 5-year personal property.</p>"""),
            ("Running the Actual Comparison", """<p>Consider a $1.2 million residential rental, $960,000 depreciable after land, sold at the end of year three. Without a study, three years of straight-line 27.5-year depreciation is roughly $105,000, all unrecaptured 1250 gain at 25 percent.</p>
<p>With a study reclassifying $240,000 to 5-year and 15-year property, and 100 percent bonus on the eligible portion, first-year depreciation might be $260,000 instead of $35,000. Total depreciation over three years climbs to roughly $310,000.</p>
<p>On sale, the incremental $205,000 of depreciation is recaptured. Say $150,000 of it is 1245 property at 37 percent and $55,000 is additional 1250 at 25 percent. The recapture cost is roughly $69,250. The year-one benefit on the additional $225,000 of deduction at 37 percent was roughly $83,250, received two years earlier.</p>"""),
            ("Where the Advantage Comes From", """<p>In that example the strategy still wins, and it wins for two reasons that are worth separating.</p>
<p>The first is pure time value. You held roughly $83,000 for two to three years. At an 8 percent cost of capital, that is meaningful, and for an investor redeploying into another property it can be considerably more.</p>
<p>The second is rate arbitrage, and it is the one people forget. The deduction offsets income at your marginal ordinary rate. The recapture on 1250 property comes back at a capped 25 percent. That spread is a permanent benefit, not a timing one, and it is why studies remain attractive even on shorter holds for high-bracket taxpayers.</p>
<p>The 1245 portion has no such spread, which is why a study weighted heavily toward personal property is the least favorable composition for a quick sale.</p>"""),
            ("When It Does Not Work", """<p>Three fact patterns turn the answer negative.</p>
<p>A taxpayer whose deduction suspends under the passive activity rules gets no year-one benefit, then sells and triggers recapture. The suspended loss does release on a fully taxable disposition, which largely offsets the problem, but the timing benefit is gone entirely.</p>
<p>A taxpayer whose marginal rate is lower in the deduction year than in the sale year loses the rate arbitrage and may invert it. Someone in the 24 percent bracket taking the deduction and the 37 percent bracket at sale has made the trade backwards.</p>
<p>A taxpayer planning a 1031 exchange has a different calculus entirely, because recapture is deferred in a properly structured exchange, though 1245 property requires like-kind personal property to fully defer, which is no longer available after the 2017 changes limited 1031 to real property.</p>"""),
            ("The 1031 Wrinkle Worth Understanding", """<p>Since Section 1031 is limited to real property, personal property identified in a cost segregation study does not qualify for exchange treatment. Gain attributable to that 1245 property is generally recognized even in an otherwise fully deferred exchange.</p>
<p>This creates a real tension for investors who accelerate aggressively and then exchange. The larger the 1245 allocation, the larger the taxable boot-like exposure on exchange.</p>
<p>It is a solvable problem with planning, and it argues for coordinating the study composition with the exit strategy at the outset. AE Tax Advisors covers the interaction in their """ + ae("1031-exchange-guide", "1031 exchange guide") + """.</p>"""),
            ("How to Decide", """<p>If your hold period is genuinely uncertain, which describes most investors, the study is usually still worth running. The rate arbitrage on the 1250 portion and the time value on the rest carry the analysis in most scenarios.</p>
<p>If you know you are selling within twenty-four months, model it explicitly. Ask your provider for the split between 1245 and 1250 property, apply your actual marginal rate to each, and discount the timing benefit at your real cost of capital.</p>
<p>The one thing not to do is run the study, take the deduction, and be surprised at closing. Recapture is entirely predictable, and the time to understand it is before you file, not when the settlement statement arrives.</p>"""),
        ],
        "related": [
            ("depreciation-recapture-cost-segregation", "Depreciation Recapture After Cost Segregation"),
            ("cost-segregation-1031-exchanges", "Cost Segregation and 1031 Exchanges"),
            ("when-not-to-do-cost-segregation", "When Not to Do a Cost Segregation Study"),
        ],
    },
    {
        "slug": "how-long-does-cost-segregation-study-take",
        "title": "How Long Does a Cost Segregation Study Take? A Realistic Timeline",
        "description": "A quality engineering-based study takes three to six weeks from engagement to final report. Here is what happens in each phase and what causes delays.",
        "date": DATE,
        "iso_date": ISO,
        "sections": [
            ("The Short Answer and the Honest Answer", """<p>A properly executed engineering-based cost segregation study takes three to six weeks from engagement to delivered report. Rush timelines of two weeks are achievable when documentation is complete and the property is straightforward.</p>
<p>The honest answer is that most of the elapsed time is not the engineer working. It is waiting for documents. Studies that finish in three weeks are studies where the owner had the closing statement, appraisal, and property records ready on day one.</p>
<p>If a provider promises a completed study in forty-eight hours without a site visit or document review, they are not performing an engineering analysis. They are applying a percentage model, and the IRS Audit Technique Guide is explicit that rule of thumb approaches are not considered reliable.</p>"""),
            ("Phase One: Feasibility and Engagement, Two to Five Days", """<p>Before anyone commits, a preliminary analysis establishes whether the study makes economic sense. This uses the purchase price, property type, placed-in-service date, and a discussion of your tax position.</p>
<p>The output is an estimated reclassification range and an estimated first-year deduction, weighed against the study fee. For most properties this is a same-day or next-day answer, and it should be free.</p>
<p>The critical piece of this phase is not the engineering estimate. It is confirming that you can actually use the deduction. A study on a passive investor with no passive income and no path to material participation produces a suspended loss, and that conversation belongs at the start.</p>"""),
            ("Phase Two: Document Collection, One to Three Weeks", """<p>This is the phase that determines your overall timeline. The core document set includes the closing or settlement statement, the purchase agreement, any appraisal, the property tax assessment, depreciation schedules from prior returns, and construction documents or renovation invoices if available.</p>
<p>For new construction, the engineer wants the general contractor's schedule of values, change orders, and the architectural and mechanical drawings. Where those exist, the detailed engineering approach from actual cost records is available, which is the most reliable methodology and produces the strongest report.</p>
<p>Owners consistently underestimate how long it takes to retrieve documents from a lender, a former property manager, or a closing attorney. Starting document collection at engagement rather than after the site visit is the single largest time saver available.</p>"""),
            ("Phase Three: Site Inspection, One Day", """<p>A physical inspection documents the property's actual components: finishes, fixtures, mechanical systems, electrical distribution, site improvements, and anything unusual that a plan set would not reveal.</p>
<p>The engineer photographs and measures, building the record that supports the takeoff. For a single-family or small multifamily property this is a half day. For a larger commercial property it can be a full day or more.</p>
<p>Some providers offer virtual inspections using owner-supplied photography and video. This is a reasonable accommodation for remote properties and it is materially weaker than a physical visit. If a virtual inspection is used, the report should say so and explain why.</p>"""),
            ("Phase Four: Engineering Analysis and Report, Two to Three Weeks", """<p>This is the actual work. The engineer performs quantity takeoffs, applies unit costs from recognized construction cost databases, allocates indirect and soft costs across components, classifies each asset under MACRS, and reconciles the total back to depreciable basis.</p>
<p>The report is then assembled: methodology, legal analysis citing the controlling authorities, asset-level detail schedules, photographs, the reconciliation, and the depreciation schedules your preparer will use.</p>
<p>Quality review adds a few days. A second reviewer checking classifications and reconciliation is standard practice at competent firms and is one of the more common places a rushed study cuts corners.</p>"""),
            ("Phase Five: Implementation With Your Preparer", """<p>The report is not the end. For a current-year acquisition, your preparer applies the schedules directly to the return. For a prior-year property, the study supports a Form 3115 with a Section 481(a) adjustment, which must be filed with the return and a copy submitted to the IRS.</p>
<p>Build in time for your preparer to review the report before the filing deadline. Handing a study to a CPA on April 10 for an April 15 deadline is how errors get made and extensions get filed.</p>
<p>If you are working with a tax advisor on the broader planning, loop them in during phase one rather than at delivery. AE Tax Advisors coordinates study timing with the rest of the plan through their """ + ae("tax-planning-for-real-estate-investors", "real estate investor tax planning") + """ work.</p>"""),
            ("Planning Backward From Your Deadline", """<p>For a calendar-year taxpayer filing by April 15, engaging by early February leaves comfortable room. Engaging in late March means an extension, which is fine and routine but should be a decision rather than a surprise.</p>
<p>For a property acquired late in the year, there is no rush to complete the study before December 31. The deduction attaches to the tax year the property was placed in service, not to when the study was performed. A study completed in March for a November acquisition applies to the prior year return.</p>
<p>The only genuine deadline pressure comes from extended return due dates and from Form 3115 filings, which must accompany a timely filed return. Working backward from those two dates gives you your engagement date.</p>"""),
        ],
        "related": [
            ("how-cost-segregation-works-real-estate-investors", "How Cost Segregation Works"),
            ("cost-segregation-study-cost-pricing", "What a Cost Segregation Study Costs"),
            ("how-to-choose-cost-segregation-company", "How to Choose a Cost Segregation Company"),
        ],
    },
    {
        "slug": "cost-segregation-condos-townhomes",
        "title": "Cost Segregation on a Condo or Townhome: What You Own and What You Can Depreciate",
        "description": "Condo owners can run a cost segregation study, but the analysis has to account for what the unit deed actually conveys and how common elements are treated. Here is how it works.",
        "date": DATE,
        "iso_date": ISO,
        "sections": [
            ("A Property Type That Gets Written Off Too Quickly", """<p>Investors often assume cost segregation does not apply to condominiums because they do not own the roof, the parking lot, or the exterior. That assumption costs them real deductions.</p>
<p>A condo unit contains exactly the components a study targets: flooring, cabinetry, countertops, appliances, plumbing fixtures, dedicated electrical, decorative lighting, and interior finishes. On a finished residential unit, these frequently represent 20 to 30 percent of the improvement basis.</p>
<p>What changes is not whether a study applies. It is what the study examines and how the ownership interest in common elements is handled.</p>"""),
            ("What the Deed Actually Conveys", """<p>A condominium interest under most state acts consists of two things: exclusive ownership of the unit as defined by the declaration, and an undivided percentage interest in the common elements.</p>
<p>The declaration is the controlling document, and it varies. Some define the unit boundary at the unfinished surface of perimeter walls, floors, and ceilings, meaning the owner holds the finishes and everything inboard. Others define it more broadly to include portions of building systems serving the unit exclusively.</p>
<p>The engineer needs the declaration, not just the deed. A study that assumes a standard boundary without reading the document is guessing at the scope of what is being depreciated.</p>"""),
            ("The Common Element Interest Is Depreciable Too", """<p>Here is the part owners miss. Your undivided percentage interest in the common elements is part of what you purchased, and to the extent it represents depreciable improvements rather than land, it is depreciable.</p>
<p>Common elements typically include the building shell, roof, corridors, elevators, mechanical rooms, parking areas, pools, landscaping, and site utilities. Your share of the paving, fencing, site lighting, and landscaping is 15-year land improvement property. Your share of amenity finishes and equipment may be shorter-lived still.</p>
<p>Capturing this requires allocating total purchase price between the unit and the common element interest, then applying the study methodology to both. Providers who examine only the unit interior leave the 15-year bucket almost entirely unclaimed.</p>"""),
            ("Land Allocation in a Vertical Building", """<p>Land is not depreciable, and every condo purchase includes an implicit share of it. In a high-rise, that share is small relative to the improvement value, which works in the owner's favor.</p>
<p>A twenty-story building on a half-acre urban parcel might carry a land allocation of 8 to 12 percent of value, compared to 20 to 30 percent for a detached single-family home in the same market. Townhomes sit in between, since they consume more land per unit.</p>
<p>This is a genuine and underappreciated advantage of attached product. More of the purchase price is depreciable, before any reclassification occurs. It is worth documenting the allocation properly rather than defaulting to the assessor ratio, which in condo markets is often set by formula.</p>"""),
            ("Special Assessments and Capital Improvements", """<p>Condo owners pay special assessments for roof replacements, elevator modernization, facade work, and parking lot resurfacing. These are capital expenditures allocable to your ownership interest, not deductible operating expenses.</p>
<p>They are also depreciable, and they carry their own class lives. A parking lot resurfacing assessment is 15-year land improvement property. An elevator modernization is generally a building system at 27.5 or 39 years. A common area furniture replacement may be 5-year or 7-year property.</p>
<p>Owners routinely expense these in error or capitalize them all at 27.5 years. Tracking them properly, and cost segregating the larger ones, is a recurring source of deduction over a long hold. AE Tax Advisors addresses the capitalization question in their """ + ae("tax-deductions-rental-property-owners-complete-checklist", "rental property deduction checklist") + """.</p>"""),
            ("Short-Term Rental Condos", """<p>Condo units operated as short-term rentals are among the better candidates for a study. They are furnished, which adds personal property. They are often renovated at acquisition, which adds recently placed-in-service components with clear cost records. And the owner is frequently able to materially participate.</p>
<p>The complication is HOA restrictions. Many associations limit or prohibit short-term rentals, and rules change. A depreciation strategy premised on seven-day average stays becomes fragile if the association adopts a thirty-day minimum, because the activity reverts to a rental under Section 469 and losses become passive.</p>
<p>Check the declaration and the rental policy before building a tax plan on top of a use the association can revoke.</p>"""),
            ("Whether the Economics Work", """<p>The threshold question is depreciable basis. A $250,000 condo with a 10 percent land allocation has $225,000 of depreciable basis. A study reclassifying 25 percent produces roughly $56,000 of accelerated basis, which at a 35 percent marginal rate is around $19,600 of first-year tax benefit.</p>
<p>Against a study fee in the low thousands, that works. Below roughly $150,000 of depreciable basis, the math gets thin and a simplified approach may be more appropriate.</p>
<p>Investors holding several units in the same building have the strongest case of all, since much of the engineering work is shared across units and providers will price a portfolio accordingly.</p>"""),
        ],
        "related": [
            ("cost-segregation-single-family-rentals", "Cost Segregation for Single-Family Rentals"),
            ("cost-segregation-under-500k", "Cost Segregation on Properties Under $500,000"),
            ("land-value-allocation-cost-segregation", "Land Value Allocation in a Cost Segregation Study"),
        ],
    },
    {
        "slug": "cost-segregation-farms-agricultural-property",
        "title": "Cost Segregation for Farms and Agricultural Property: An Overlooked Category",
        "description": "Agricultural property contains an unusually high share of short-life assets: single purpose structures, drainage tile, fencing, grain handling, and irrigation. Here is how a study treats them.",
        "date": DATE,
        "iso_date": ISO,
        "sections": [
            ("Why Farms Reclassify Better Than Almost Anything", """<p>Cost segregation is usually discussed in the context of rentals and commercial buildings. Agricultural property is rarely mentioned, which is odd, because it routinely produces higher reclassification percentages than either.</p>
<p>The reason is structural. A farm is not one building on a lot. It is a collection of purpose-built improvements, most of which Congress and the regulations already assign short recovery periods: single purpose agricultural structures at 10 years, land improvements at 15 years, and equipment at 5 or 7 years.</p>
<p>On a diversified operation, the share of purchase price landing outside the 20-year and 39-year buckets can exceed 40 percent. That is well above what a typical apartment building produces.</p>"""),
            ("Single Purpose Agricultural and Horticultural Structures", """<p>Section 168(i)(13) defines a single purpose agricultural structure as one specifically designed, constructed, and used for housing, raising, and feeding a particular type of livestock, including the equipment necessary for those functions and for waste handling.</p>
<p>These carry a 10-year recovery period, not 20 or 39. Poultry houses, hog barns, dairy parlors, and greenhouses meeting the horticultural definition all qualify when they meet the specific-design test.</p>
<p>The test is genuinely restrictive. A general purpose barn used for equipment storage and occasional livestock does not qualify. The structure must be so specialized that it is not economically usable for another purpose, and the supporting analysis needs to establish that.</p>"""),
            ("Land Improvements, Which Are Everywhere on a Farm", """<p>Fifteen-year land improvement property on agricultural land includes fencing, drainage tile, wells, irrigation systems, farm roads, culverts, retention structures, grain bin foundations, and livestock watering systems.</p>
<p>Drainage tile alone can represent a substantial figure on productive cropland. Systematic tiling runs $1,000 to $1,500 per acre in many markets, and on a purchased farm that cost is embedded in the price with no invoice attached to it. An engineering study is the only practical way to extract it.</p>
<p>Fencing follows the same pattern. A cattle operation with perimeter and cross fencing across several hundred acres carries real value that defaults into non-depreciable land in the absence of an analysis.</p>"""),
            ("The Land Question Is the Hard Part", """<p>Agricultural purchases carry a high land allocation, and land is not depreciable. On a $2 million farm purchase, bare land value might be $1.4 million, leaving $600,000 of depreciable improvements.</p>
<p>This makes the land allocation analysis more consequential here than in any other property type. The difference between a defensible allocation supported by comparable bare land sales and a rough assessor-based split can move depreciable basis by hundreds of thousands of dollars.</p>
<p>The good news is that agricultural markets generally have abundant comparable sales of unimproved land, which makes the extraction method genuinely reliable. Farm appraisers routinely separate bare land, tile, fencing, and structures, and where such an appraisal exists it is strong support.</p>"""),
            ("Special Rules That Apply to Farming Activities", """<p>Farming has its own overlay. Section 168(b)(2)(B) generally requires the 150 percent declining balance method rather than 200 percent for property used in a farming business, which slows recovery somewhat relative to other trades.</p>
<p>Taxpayers who elect out of the uniform capitalization rules under Section 263A(d)(3) for preproductive period costs are required to use the alternative depreciation system for all farming assets placed in service in that year, which is a long recovery period and a significant consequence.</p>
<p>That election interaction is the single most important thing to check before commissioning a study on a farm. A taxpayer under ADS by election will not see the results a study projects, and the projection needs to be built on the correct method from the start.</p>"""),
            ("Who Can Actually Use the Deduction", """<p>Farming is a trade or business, and an owner-operator who materially participates generates non-passive losses. That is a considerably better starting position than a passive rental investor faces.</p>
<p>Cash-rent landlords are in a different position. Rental of farmland for cash is generally a passive rental activity, and losses suspend under Section 469 in the ordinary way. Crop share arrangements can be structured to reach material participation, but the arrangement has to be real.</p>
<p>Excess business loss limits under Section 461(l) also apply and cap the amount of business loss that can offset nonbusiness income in a year, with the excess becoming a net operating loss carryforward. AE Tax Advisors works through these limits in their """ + ae("passive-activity-loss-rules-real-estate", "passive activity loss") + """ material.</p>"""),
            ("When to Look at This", """<p>The strongest candidates are recently purchased operations, farms that have completed significant improvement projects, and operations that have never had the embedded tile, fencing, and structures separately valued.</p>
<p>Farms purchased in prior years are eligible for a Form 3115 look-back, which captures the missed depreciation as a current-year Section 481(a) adjustment without amending returns. Given how rarely agricultural buyers commission studies at acquisition, look-back opportunities in this sector are unusually common.</p>
<p>If you bought a farm in the last decade and the depreciation schedule shows a single line for buildings and improvements, there is almost certainly something there.</p>"""),
        ],
        "related": [
            ("land-improvements-15-year-property-cost-segregation", "Land Improvements and 15-Year Property"),
            ("form-3115-look-back-cost-segregation", "Form 3115 Look-Back Studies"),
            ("land-value-allocation-cost-segregation", "Land Value Allocation in a Cost Segregation Study"),
        ],
    },
    {
        "slug": "converting-str-to-ltr-depreciation",
        "title": "Converting a Short-Term Rental to a Long-Term Rental: What Happens to Your Depreciation",
        "description": "Switching from nightly to annual leases changes the recovery period, the passive activity treatment, and what happens to losses you already claimed. Here is the full picture.",
        "date": DATE,
        "iso_date": ISO,
        "sections": [
            ("A Common Move With Uncommon Tax Consequences", """<p>Owners convert short-term rentals to long-term rentals constantly. A city tightens its ordinance, occupancy softens, the operational burden wears thin, or a good tenant appears. The operational decision is usually straightforward.</p>
<p>The tax consequences are not. A conversion changes the property's recovery period, changes how losses are characterized under the passive activity rules, and may trigger recapture of losses you already took.</p>
<p>None of this makes conversion a bad idea. It does mean the switch should be timed deliberately rather than discovered on the return.</p>"""),
            ("The Recovery Period Actually Changes", """<p>Residential rental property under Section 168(e)(2)(A) is defined as a building where 80 percent or more of gross rental income is from dwelling units, and it recovers over 27.5 years. A unit used on a transient basis, where the average stay is short enough that it functions like lodging, is generally treated as nonresidential real property at 39 years.</p>
<p>So a short-term rental typically depreciates the structure over 39 years, and the same property under annual leases depreciates over 27.5 years.</p>
<p>The 80 percent test is applied annually. In the year of conversion, the classification depends on the actual income mix for that year, which means a mid-year conversion produces a fact question rather than a clean answer. Converting effective January 1 avoids it entirely.</p>"""),
            ("How the Change Is Implemented", """<p>A change in the use of property is addressed in Regulation 1.168(i)-4. Where the change results in a different recovery period or method, depreciation is computed going forward using the adjusted basis at the beginning of the year of change and the new applicable recovery period.</p>
<p>It is not a change in accounting method requiring Form 3115, and it does not require recomputing prior years. You do not amend anything. Depreciation simply continues on the remaining basis under the new schedule.</p>
<p>Your 5-year, 7-year, and 15-year property from the cost segregation study is unaffected. Those classifications were made based on the nature of the assets, not the rental term, and they continue on their existing schedules.</p>"""),
            ("The Passive Activity Consequence Is the Big One", """<p>This is where conversion actually costs money. A short-term rental with an average stay of seven days or less is outside the definition of a rental activity, so a materially participating owner has non-passive losses.</p>
<p>A long-term rental is a rental activity by definition, and it is passive per se under Section 469(c)(2) regardless of hours worked, unless the owner qualifies as a real estate professional.</p>
<p>So an owner who was offsetting W-2 income with rental losses stops being able to do so on conversion. Future losses suspend. If the cost segregation deduction has already been fully absorbed, this may not matter. If a portion remains, the timing of conversion matters a great deal.</p>"""),
            ("What Happens to Losses You Already Claimed", """<p>Losses properly claimed as non-passive in prior years are not recaptured or reversed by a later conversion. The characterization is determined year by year on that year's facts.</p>
<p>There is an exception worth knowing. Section 469(f) contains former passive activity rules, and Regulation 1.469-2(f) contains recharacterization provisions that can convert income from a formerly passive activity. These are more likely to affect the treatment of future income than to claw back prior deductions, but they are why the analysis should not be done casually.</p>
<p>Suspended passive losses from the long-term rental period remain suspended, carrying forward until you have passive income or dispose of the entire interest in a fully taxable transaction. AE Tax Advisors covers the treatment in their comparison of """ + ae("str-vs-ltr-tax-treatment", "STR and LTR tax treatment") + """.</p>"""),
            ("Timing the Conversion", """<p>If a large cost segregation deduction remains unabsorbed, finishing the absorption in a short-term rental year is generally worth more than converting early. That may mean holding the nightly model one additional year.</p>
<p>If the deduction is exhausted and the property is now generating positive taxable income, conversion is less costly and the operational benefits dominate.</p>
<p>Converting effective the first day of a tax year avoids the mixed-use classification question entirely and gives a clean record. Converting mid-year is workable but requires documenting the income mix to support the 80 percent test.</p>"""),
            ("If You Never Ran a Study During the Short-Term Period", """<p>An owner who operated a short-term rental for several years without a cost segregation study, and now plans to convert, is in a specific and time-sensitive position.</p>
<p>A Form 3115 look-back can capture all the missed depreciation as a Section 481(a) adjustment in the current year. Filed in a year where the property is still short-term and the owner still materially participates, that catch-up is non-passive and can offset ordinary income.</p>
<p>Filed a year later, after conversion, the same adjustment is a passive loss that suspends. The economics of that one-year difference can run into six figures, and it is one of the clearest examples of why sequencing matters more than optimization.</p>"""),
        ],
        "related": [
            ("cost-segregation-str-tax-loophole", "The Short-Term Rental Tax Strategy Explained"),
            ("cost-segregation-long-term-rentals", "Cost Segregation for Long-Term Rentals"),
            ("form-3115-look-back-cost-segregation", "Form 3115 Look-Back Studies"),
        ],
    },
    {
        "slug": "cost-segregation-after-refinance",
        "title": "Does Refinancing Affect Cost Segregation? What a Cash-Out Actually Changes",
        "description": "Refinancing does not change your depreciable basis, but it changes at-risk amounts, interest deductibility, and the tracing of loan proceeds. Here is what a cash-out does and does not do.",
        "date": DATE,
        "iso_date": ISO,
        "sections": [
            ("A Frequent Misconception Worth Clearing Up", """<p>Investors regularly ask whether a refinance resets basis, creates a new placed-in-service date, or opens the door to a fresh cost segregation study. The answer to all three is no.</p>
<p>Depreciable basis is determined by cost, adjusted for improvements and depreciation taken. It has nothing to do with debt. You could own a property free and clear or leverage it to 90 percent, and your depreciation schedule would be identical.</p>
<p>A cash-out refinance puts money in your pocket without creating taxable income, which is genuinely valuable, but it does not touch the depreciation side of the ledger.</p>"""),
            ("What Refinancing Does Not Change", """<p>It does not change basis. It does not create a new placed-in-service date. It does not restart any recovery period. It does not make a property newly eligible for bonus depreciation, since bonus eligibility attaches to the original acquisition or improvement.</p>
<p>It does not affect the classification of components identified in an existing cost segregation study, and it does not create a reason to redo one.</p>
<p>It is also not a taxable event. Loan proceeds are not income because they carry an obligation to repay, which is why a cash-out refinance is one of the more efficient ways to access appreciation without triggering gain.</p>"""),
            ("What It Does Change: At-Risk Amounts", """<p>Section 465 limits deductions to the amount a taxpayer has at risk in the activity. For real estate, qualified nonrecourse financing secured by real property and borrowed from a qualified person is generally treated as at-risk under Section 465(b)(6).</p>
<p>A refinance can change this. If you replace qualified nonrecourse financing from a commercial lender with a loan from a related party, or with financing that fails the qualified person test, the amount at risk can decrease, potentially limiting deductions that were previously allowable.</p>
<p>Seller financing and loans from related entities are the common trouble spots. This rarely comes up in a straightforward bank refinance and comes up regularly in creative structures.</p>"""),
            ("Interest Tracing on the Cash-Out Portion", """<p>This is the piece that most affects the tax outcome. Interest deductibility is determined by how the borrowed funds are used, not by what secures the loan. The tracing rules of Regulation 1.163-8T govern.</p>
<p>Interest on the portion of the new loan that refinances the original acquisition debt remains allocable to the rental activity and deductible against rental income. Interest on cash-out proceeds is allocated based on what you do with the money.</p>
<p>Use the cash to buy another rental, and that interest is allocable to the new rental. Use it to pay down a personal residence mortgage or buy a boat, and it becomes personal interest, which is not deductible. Use it for a business, and it is business interest.</p>
<p>Tracing requires documentation. Depositing cash-out proceeds into an account that already holds personal funds and then spending from it creates an allocation problem that is tedious to unwind. A separate account for the proceeds solves it. AE Tax Advisors covers tracing and related recordkeeping in their """ + ae("real-estate-bookkeeping", "real estate bookkeeping") + """ guidance.</p>"""),
            ("Where a Refinance Does Interact With Depreciation", """<p>There is an indirect interaction worth understanding. A cost segregation deduction is limited at the partner or member level by basis and at-risk amounts. In a partnership, a share of nonrecourse debt increases outside basis under Section 752.</p>
<p>So a refinance that increases partnership debt increases partners' outside basis, which can free up a cost segregation deduction that was previously basis-limited. That is a genuine planning lever in partnerships where a large study deduction exceeds available basis.</p>
<p>The corollary is that a paydown or payoff reduces debt share and can reduce basis, potentially triggering gain if a partner's share of liabilities falls below their basis. Refinancing decisions in leveraged partnerships have basis consequences that deserve modeling before closing.</p>"""),
            ("Loan Costs Are Their Own Category", """<p>Points, origination fees, appraisal costs, and title charges on a refinance are not deductible when paid. They are amortized over the life of the new loan under Section 461(g).</p>
<p>When you refinance again, any unamortized costs from the prior loan are generally deductible in full in the year the old loan is retired, since the asset being amortized no longer exists.</p>
<p>Investors who refinance repeatedly accumulate these balances and frequently miss the writeoff on payoff. It is a small item individually and a real one across a portfolio over a decade.</p>"""),
            ("If You Have Never Run a Study", """<p>The useful connection between refinancing and cost segregation is behavioral rather than technical. A refinance is when owners gather documents, revisit the numbers, and think about the property as a financial asset.</p>
<p>That is a natural moment to check whether a study was ever performed. If the property has been held for years on a single-line depreciation schedule, a Form 3115 look-back can capture the missed depreciation in the current year without amending prior returns.</p>
<p>The cash from the refinance and the deduction from the look-back are unrelated mechanically, but they land in the same year and the combination is often what makes the next acquisition possible.</p>"""),
        ],
        "related": [
            ("form-3115-look-back-cost-segregation", "Form 3115 Look-Back Studies"),
            ("cost-segregation-existing-property", "Cost Segregation on a Property You Already Own"),
            ("cost-segregation-partnership-special-allocations", "Cost Segregation Inside a Partnership"),
        ],
    },
]


if __name__ == "__main__":
    for p in POSTS:
        print("wrote", write_post(p, ROOT))
