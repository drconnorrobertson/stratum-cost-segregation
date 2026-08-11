#!/usr/bin/env python3
"""Batch D: 15 long-tail cost segregation posts (part 1 of 2)."""

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
        "slug": "str-100-hour-material-participation-test",
        "title": "The 100-Hour Test: How Short-Term Rental Owners Actually Qualify for Material Participation",
        "description": "The most common route to material participation on a short-term rental is the 100-hour test, not the 500-hour test. Here is how it works, what counts, and how to document it.",
        "date": DATE,
        "iso_date": ISO,
        "sections": [
            ("Why This Test Matters More Than the Study Itself", """<p>A cost segregation study on a short-term rental can produce a first-year deduction of $80,000 to $200,000 on a typical property. Whether that deduction reduces your tax bill this year, or sits suspended on Form 8582 waiting for passive income that may never arrive, comes down to a single question: did you materially participate?</p>
<p>Most owners assume material participation requires 500 hours. That number gets quoted constantly, and it is one of the seven tests, but for short-term rental owners it is usually the wrong one to aim at. The realistic path for someone with a day job and one or two properties is the 100-hour test.</p>
<p>Getting this right is worth more than optimizing the study. A perfectly engineered reclassification that produces a suspended loss delivers zero cash benefit in year one.</p>"""),
            ("What the 100-Hour Test Actually Says", """<p>Treasury Regulation 1.469-5T(a)(3) provides that you materially participate in an activity if you participate for more than 100 hours during the tax year, and no other individual participates more than you do.</p>
<p>Read that second clause carefully, because it is where most owners fail. It is not enough to log 101 hours. You must log more hours than any other single person involved in the property. That includes your cleaner, your handyman, your co-host, and critically, your property manager.</p>
<p>The comparison is made person by person, not in aggregate. If your cleaner works 60 hours across the year and your handyman works 40, you are compared against 60, not 100. But if you use a full-service management company and a single account manager touches your property for 150 hours, you cannot clear the bar without matching them.</p>"""),
            ("Why Short-Term Rentals Get to Use This Test at All", """<p>Rental activities are ordinarily passive by definition under IRC Section 469(c)(2), regardless of how many hours you work. The short-term rental exception sits in Treasury Regulation 1.469-1T(e)(3)(ii)(A), which removes an activity from the definition of rental when the average period of customer use is seven days or less.</p>
<p>Once the property falls outside the rental definition, it becomes a trade or business, and the ordinary material participation tests apply. That is the whole mechanism behind what people call the short-term rental loophole. It is not a loophole so much as a definitional consequence, and it has been in the regulations since 1988.</p>
<p>The seven-day average is computed across the year, using total rental days divided by number of bookings. One thirty-day booking in an otherwise three-night-average calendar can push you over the line, so it is worth tracking monthly rather than discovering the problem in March. AE Tax Advisors covers the mechanics in detail in their guide to """ + ae("str-material-participation", "short-term rental material participation") + """.</p>"""),
            ("What Counts as Participation, and What Does Not", """<p>Qualifying hours are work done in connection with the activity in which you own an interest. For a short-term rental, that ordinarily includes guest communication, pricing and calendar management, listing optimization, ordering and restocking supplies, coordinating vendors, handling maintenance issues, bookkeeping specific to the property, and physical work you perform yourself.</p>
<p>Three categories are excluded or heavily scrutinized. Investor-type activities, meaning reviewing financial statements or studying operations in a non-managerial capacity, do not count under Regulation 1.469-5T(f)(2)(ii). Travel time to and from the property is routinely challenged and should not be relied on. Work of a type an owner would not customarily do, performed mainly to generate hours, can be disregarded entirely.</p>
<p>Time spent researching a future purchase does not count toward the current property. Neither does time on your broader portfolio unless you have made a valid grouping election.</p>"""),
            ("The Documentation Standard That Survives an Exam", """<p>The regulation says participation may be established by any reasonable means, and that contemporaneous daily time reports are not required. Owners read that sentence and conclude they can reconstruct hours later. In practice, the Tax Court has rejected reconstructed logs in case after case, particularly where the totals land suspiciously close to a threshold.</p>
<p>What holds up is a contemporaneous record with enough specificity to be tested. Each entry should carry a date, a duration, and a description concrete enough that an examiner can cross-reference it against something else: a booking record, an email timestamp, a vendor invoice, a receipt.</p>
<p>Log honestly and log everything. Owners who track properly are frequently surprised to find they cleared 100 hours by June. Owners who guess tend to either overstate and lose the deduction on exam, or understate and give up a deduction they had earned.</p>"""),
            ("The Comparison Problem With Property Managers", """<p>If you use a management company, the second prong of the 100-hour test becomes the binding constraint. You will need to know how many hours that company devoted to your specific property, and you will need to exceed it.</p>
<p>Some owners solve this by unbundling: keeping guest communication and pricing in-house while outsourcing only cleaning and turnovers, which are lower-hour functions per property. Others move to a co-hosting arrangement with defined, limited scope. Either approach is legitimate, but it is a structural decision that has to be made before the year begins, not reconstructed at filing.</p>
<p>Ask your manager for an hours estimate in writing at the start of the engagement. If they cannot or will not provide one, you are relying on a number you cannot defend.</p>"""),
            ("Sequencing the Study With the Participation Year", """<p>The order of operations matters. Confirm the seven-day average is achievable for the year, build the participation log from January, and commission the """ + ae("cost-segregation-studies-for-real-estate-investors", "cost segregation study") + """ once you have line of sight on both. A study delivered in a year where participation fails is not wasted, but the benefit is deferred, sometimes for years.</p>
<p>If you acquired the property in a prior year and did not run a study then, you are not out of options. A Form 3115 look-back captures the missed depreciation as a Section 481(a) adjustment in the current year, which lets you land the catch-up in a year you know you will pass the participation test.</p>
<p>That sequencing decision, choosing which year absorbs the deduction, is often worth more than any adjustment to the study itself.</p>"""),
        ],
        "related": [
            ("cost-segregation-str-tax-loophole", "The Short-Term Rental Tax Strategy Explained"),
            ("passive-activity-loss-rules-cost-segregation", "Passive Activity Loss Rules and Cost Segregation"),
            ("form-3115-look-back-cost-segregation", "Form 3115 Look-Back Studies"),
        ],
    },
    {
        "slug": "land-value-allocation-cost-segregation",
        "title": "Land Value Allocation in a Cost Segregation Study: The Number That Quietly Determines Your Deduction",
        "description": "Land is not depreciable, so every dollar allocated to it is a dollar you cannot deduct. Here is how land value is determined, why the assessor ratio is a weak method, and what defensible allocation looks like.",
        "date": DATE,
        "iso_date": ISO,
        "sections": [
            ("The Allocation Nobody Argues About Until It Is Too Late", """<p>Before a cost segregation engineer reclassifies a single dollar into 5-year or 15-year property, a more consequential split has already happened: the division of your purchase price between land and improvements.</p>
<p>Land is not depreciable. It has no recovery period because it does not wear out. Every dollar allocated to land is permanently outside the depreciation system, and it reduces not just your reclassified components but your 27.5-year or 39-year structural basis as well.</p>
<p>On a $900,000 property, the difference between a 20 percent land allocation and a 30 percent land allocation is $90,000 of basis. Run through a study that reclassifies 25 percent to short-life property, that swing is roughly $22,500 of first-year deduction, before you even consider the structural component.</p>"""),
            ("What the Rules Actually Require", """<p>Section 1.167(a)-5 of the regulations requires that basis be allocated between depreciable and non-depreciable property in proportion to their respective fair market values at the time of acquisition. The operative phrase is fair market value, not assessed value, not insured value, and not whatever the closing statement happened to say.</p>
<p>This matters because fair market value is a factual determination supported by evidence. The IRS does not prescribe a single method. It requires that whatever method you use be reasonable and supportable, which means the burden is on you to document the reasoning.</p>
<p>There is no safe harbor percentage. Practitioners who apply a blanket 20 percent to every property are applying a habit, not a method.</p>"""),
            ("Why the Assessor Ratio Is the Weakest Common Method", """<p>The most widely used approach is to take the county assessor's land and improvement values and apply that ratio to the purchase price. It is fast, it is cheap, and it is generally accepted. It is also frequently wrong.</p>
<p>Assessment ratios are built for property tax administration, not for federal income tax basis. Many jurisdictions reassess on multi-year cycles, so the underlying values can be years stale. Some states apply statutory land-to-improvement conventions that have no relationship to market reality. Others assess land at a fixed percentage of total value across an entire class of property.</p>
<p>The method's real weakness shows up in appreciating markets. Land appreciates; a thirty-year-old building depreciates in real terms. In a market that has run hard, an assessor ratio anchored to an older reassessment can materially understate land, which sounds good until an examiner substitutes a current appraisal.</p>"""),
            ("Methods That Hold Up Better", """<p>The strongest approach is a qualified appraisal that separately values land and improvements as of the acquisition date. If you obtained an appraisal for financing, it may already contain a land value in the cost approach section. Many owners have this document sitting in a closing folder and never look at it.</p>
<p>The second-strongest is the extraction or abstraction method, where the engineer establishes land value from comparable vacant land sales in the immediate market and treats the residual as improvements. This works well in markets with genuine vacant land transactions and poorly in dense urban submarkets where none exist.</p>
<p>The replacement cost approach runs the other direction: establish the depreciated replacement cost of the improvements and treat the residual as land. This is the method most cost segregation engineers are best equipped to execute, because estimating construction cost is precisely what they do.</p>"""),
            ("Where Owners Get Into Trouble", """<p>The most common error is inconsistency. An owner uses a 15 percent land allocation to maximize depreciation, then years later, on sale, argues for a high land basis to reduce gain. Both positions are on file. That is a bad set of facts.</p>
<p>The second is applying a portfolio-wide percentage. An urban infill duplex on a small lot and a rural lakefront cabin on five acres do not share a land ratio, and using one number across both signals that no analysis occurred.</p>
<p>The third is ignoring land improvements. Driveways, walkways, fencing, retaining walls, site lighting, and landscaping are 15-year property under MACRS, not land. They sit on the land, but they depreciate. Studies that fold site work into the non-depreciable land bucket give away real deductions, and this happens more often than it should.</p>"""),
            ("The Interaction With Your Overall Depreciation Position", """<p>Land allocation compounds through every downstream calculation. It sets the ceiling on total depreciable basis, which sets the ceiling on reclassification, which drives bonus depreciation, which drives the loss available to offset income.</p>
<p>It also affects your position on disposition. A higher land basis reduces gain on sale but produces less depreciation along the way. A lower land basis accelerates deductions but increases eventual gain, some of which comes back as unrecaptured Section 1250 gain at 25 percent and Section 1245 recapture at ordinary rates.</p>
<p>Owners planning a hold of five years or less should think about that trade explicitly rather than defaulting to maximum acceleration. AE Tax Advisors works through the interaction between allocation choices and long-run outcomes in their """ + ae("real-estate-depreciation", "real estate depreciation") + """ and """ + ae("capital-gains-tax-planning-minimize-investment-profits", "capital gains planning") + """ resources.</p>"""),
            ("What to Ask Your Provider", """<p>Ask which method was used, what evidence supports it, and whether site improvements were carved out of land. A provider who answers "we used the tax assessor" without further comment has done the cheapest thing available, and you should understand that is the position you are taking.</p>
<p>Ask to see the land value stated as a dollar figure and as a percentage of purchase price, and ask how that percentage compares to others in the same submarket. An outlier is not automatically wrong, but it should have a reason attached to it.</p>
<p>Every Stratum study documents the allocation method and the supporting evidence in the report itself, because that page is the first one an examiner turns to.</p>"""),
        ],
        "related": [
            ("components-reclassified-cost-segregation", "What Gets Reclassified in a Cost Segregation Study"),
            ("land-improvements-15-year-property-cost-segregation", "Land Improvements and 15-Year Property"),
            ("how-to-read-cost-segregation-report", "How to Read a Cost Segregation Report"),
        ],
    },
    {
        "slug": "cost-segregation-house-hacking",
        "title": "Cost Segregation for House Hacking: How to Handle a Property You Live In and Rent",
        "description": "House hackers can run a cost segregation study, but only on the rental portion. Here is how allocation works, what the personal-use rules do to your deduction, and when the study is worth it.",
        "date": DATE,
        "iso_date": ISO,
        "sections": [
            ("A Real Strategy With a Real Constraint", """<p>House hacking, living in one unit of a small multifamily or renting rooms in a single-family home, is one of the most efficient ways into real estate. It is also one of the most misunderstood from a depreciation standpoint.</p>
<p>The constraint is straightforward: you cannot depreciate the portion of a property you use personally. Section 280A and the general rule that depreciation is allowed only on property used in a trade or business or held for the production of income both point the same direction.</p>
<p>What that means in practice is not that cost segregation is unavailable. It means the study runs against a reduced basis, and the allocation between personal and rental use becomes a documented position you have to defend.</p>"""),
            ("Establishing the Rental Percentage", """<p>For a duplex, triplex, or fourplex where you occupy one unit, the cleanest allocation is by square footage. If you live in a 1,100 square foot unit in a 4,000 square foot fourplex, roughly 72 percent of the building is rental. Unit count is a permissible alternative when units are comparable in size, but square footage is more defensible when they are not.</p>
<p>For room rentals in a single-family home, allocation is messier. The standard approach assigns exclusively rented bedrooms and bathrooms fully to rental use, exclusively personal space fully to personal use, and shared common areas proportionally, typically by the ratio of exclusive rental space to exclusive personal space, or by occupant count.</p>
<p>Whatever method you choose, document it with a floor plan and measurements at the time you place the property in service. Reconstructing square footage three years later during an exam is not a comfortable position.</p>"""),
            ("How the Study Applies to the Rental Share", """<p>A cost segregation study on a house hack examines the entire property, then applies the rental percentage. Components serving only rental units, dedicated appliances, unit-specific flooring, separate HVAC systems, are allocated fully to rental. Shared components, roof, foundation, site work, common area finishes, are allocated at the rental percentage.</p>
<p>This is where a competent engineer earns the fee. A generic percentage applied across the whole property understates the deduction, because owner-occupied units in small multifamily are frequently the least improved unit in the building, while rental units carry the newer appliances and finishes.</p>
<p>Land improvements deserve particular attention. Driveways, parking pads, fencing, and landscaping serve the whole property and get the blended rate, but a dedicated tenant parking area does not.</p>"""),
            ("The Personal Use Rules You Need to Clear", """<p>Section 280A limits deductions when you use a dwelling unit as a residence. For a duplex where you occupy a separate unit, the units are generally treated as separate dwelling units, and the rental unit is not subject to the 280A limitation simply because you live next door.</p>
<p>Room rentals inside your own home are harder. The unit is your residence, so 280A applies, and deductions attributable to the rental use are generally capped at rental income. Excess deductions carry forward rather than offsetting other income. A large cost segregation deduction in that setting may produce a carryforward rather than a current benefit.</p>
<p>This distinction, separate unit versus shared dwelling, is the single most important fact pattern question for a house hacker considering a study, and it should be settled before you commission one.</p>"""),
            ("The Short-Term Rental Angle", """<p>House hackers who rent units or rooms on a nightly basis face an additional layer. If the average period of customer use is seven days or less, the activity falls outside the definition of a rental under Regulation 1.469-1T(e)(3)(ii)(A), which opens the door to treating losses as non-passive if you materially participate.</p>
<p>Living on site makes material participation considerably easier to achieve and to document, since you are handling turnovers, guest issues, and maintenance directly. Owners in this position frequently clear the 100-hour threshold without effort.</p>
<p>The 280A analysis still applies to the space you occupy, but the combination of on-site participation and short-term treatment is one of the more favorable structures available to a small investor. AE Tax Advisors covers the interaction in their """ + ae("short-term-rental-tax-strategy", "short-term rental tax strategy") + """ material.</p>"""),
            ("When You Move Out", """<p>House hacks usually end. When you vacate and convert your unit to rental use, the previously personal portion is placed in service as rental property, and its basis becomes the lesser of adjusted basis or fair market value at the conversion date.</p>
<p>At that point a second study, or an amendment to the original, captures the newly converted portion. This is a routine and worthwhile step that many owners miss entirely, leaving years of accelerated depreciation on the table.</p>
<p>If you never ran a study on the rental portion in the first place, a Form 3115 look-back can capture both the original rental share and the converted share as a Section 481(a) adjustment without amending prior returns.</p>"""),
            ("Is It Worth It on a Small Property", """<p>The economics turn on the depreciable rental basis. On a $500,000 fourplex with 75 percent rental use and a 20 percent land allocation, the rental depreciable basis is roughly $300,000. A study reclassifying 25 to 30 percent to short-life property produces something in the range of $75,000 to $90,000 of accelerated basis.</p>
<p>Against a study fee of a few thousand dollars, that is a strong return if you can use the deduction currently. If the loss is going to suspend under the passive activity rules or the 280A limitation, the return is deferred and the calculus changes.</p>
<p>The honest answer is that house hacks sit near the line more often than larger properties do. It is worth running the numbers before committing, which is exactly what a free estimate is for.</p>"""),
        ],
        "related": [
            ("cost-segregation-duplexes-multifamily", "Cost Segregation for Duplexes and Small Multifamily"),
            ("cost-segregation-under-500k", "Cost Segregation on Properties Under $500,000"),
            ("cost-segregation-first-time-rental-owners", "Cost Segregation for First-Time Rental Owners"),
        ],
    },
    {
        "slug": "mid-quarter-convention-cost-segregation",
        "title": "The Mid-Quarter Convention: The Timing Trap That Can Cut Your First-Year Deduction",
        "description": "Buy too much personal property in the fourth quarter and MACRS switches from the half-year convention to mid-quarter, changing your first-year deduction. Here is how the 40 percent test works.",
        "date": DATE,
        "iso_date": ISO,
        "sections": [
            ("A Rule That Surprises People in December", """<p>MACRS depreciation for personal property normally uses the half-year convention: regardless of when during the year you placed an asset in service, you are treated as having placed it in service at the midpoint of the year, and you take half a year of depreciation.</p>
<p>There is an override. Under Section 168(d)(3), if more than 40 percent of the aggregate basis of personal property placed in service during the year is placed in service in the fourth quarter, the mid-quarter convention applies to all personal property placed in service that year.</p>
<p>The word "all" is what stings. It is not a fourth-quarter penalty. Failing the test reaches back and changes the convention for assets you placed in service in January.</p>"""),
            ("How the Test Is Computed", """<p>The calculation looks at the aggregate basis of MACRS property with a recovery period of less than 27.5 years, placed in service during the tax year. Divide the fourth-quarter portion by the total. If the result exceeds 40 percent, mid-quarter applies.</p>
<p>Real property, meaning your 27.5-year residential or 39-year nonresidential structural basis, is excluded from both the numerator and the denominator. So is property placed in service and disposed of in the same year.</p>
<p>Critically, 15-year land improvements are included. Many owners assume the test is about furniture and equipment, then discover that a fourth-quarter closing brought a large land improvement allocation into the fourth-quarter bucket.</p>"""),
            ("Why Cost Segregation Makes This Live", """<p>Without a cost segregation study, a rental property purchase generates almost no personal property. The whole basis lands in the 27.5-year or 39-year bucket, which is excluded from the test. The mid-quarter convention never comes up.</p>
<p>A study changes that. It carves 20 to 35 percent of depreciable basis into 5-year, 7-year, and 15-year classes, all of which count. On a $1.2 million property closing in November, a study might produce $280,000 of short-life property, and every dollar of it lands in the fourth quarter.</p>
<p>If that is your only acquisition for the year, you are at 100 percent fourth-quarter, and mid-quarter applies automatically.</p>"""),
            ("What Mid-Quarter Actually Does to the Number", """<p>Under mid-quarter, each asset is treated as placed in service at the midpoint of the quarter in which it was actually placed in service. First-quarter assets get 10.5 months of depreciation, second-quarter 7.5 months, third-quarter 4.5 months, and fourth-quarter 1.5 months.</p>
<p>For a fourth-quarter acquisition, that is 12.5 percent of a full year instead of the 50 percent the half-year convention would have given. On 5-year property using 200 percent declining balance, the first-year rate drops from 20 percent to 5 percent.</p>
<p>For a first-quarter acquisition caught by a fourth-quarter purchase elsewhere in the portfolio, the effect runs the other way and is favorable: 35 percent instead of 20 percent on 5-year property. Mid-quarter is not uniformly bad. It is uniformly different.</p>"""),
            ("Bonus Depreciation Changes the Picture Substantially", """<p>Here is the part that resolves most of the anxiety. Bonus depreciation under Section 168(k) is applied before the convention. Property eligible for 100 percent bonus is fully expensed in the placed-in-service year regardless of which convention governs.</p>
<p>With 100 percent bonus depreciation restored and made permanent for qualifying property, most short-life property from a cost segregation study is expensed immediately, and the convention question becomes largely academic for those assets.</p>
<p>It still matters in three situations: property that is not bonus-eligible, taxpayers who elect out of bonus under Section 168(k)(7), and states that decouple from federal bonus depreciation. That last category is the big one, because state conformity varies widely and the state calculation runs on the federal convention. AE Tax Advisors maintains guidance on """ + ae("bonus-depreciation-rental-property", "bonus depreciation for rental property") + """ including the state conformity wrinkles.</p>"""),
            ("Planning Around It", """<p>If you control closing timing and expect a large short-life allocation, moving a closing from early October to late September changes the quarter and can flip the test. That is a genuine planning lever, though it should never override a business reason to close.</p>
<p>If you are acquiring multiple properties in a year, sequencing matters. Two acquisitions of similar size, one in the second quarter and one in the fourth, keep you comfortably under 40 percent. Both in the fourth quarter, and you fail.</p>
<p>Electing out of bonus depreciation is sometimes advantageous, particularly where a taxpayer wants to spread deductions across years to stay out of a higher bracket or to preserve the ability to use other credits. Just recognize that electing out is what makes the convention question matter again.</p>"""),
            ("What to Confirm in Your Study", """<p>Ask your provider to state the placed-in-service date used and to confirm whether the mid-quarter test was evaluated across all of your acquisitions for the year, not just the property being studied. The test is taxpayer-level, not property-level, and a provider studying one property in isolation may not have the full picture.</p>
<p>If you have multiple studies from different providers in the same year, someone needs to aggregate them. That is usually your tax preparer, and it is worth flagging proactively rather than assuming it will be caught.</p>
<p>The convention is a detail, but it is the kind of detail that shows up as an unexplained difference between the deduction you expected and the deduction on the return.</p>"""),
        ],
        "related": [
            ("bonus-depreciation-2026-rental-property", "Bonus Depreciation for Rental Property in 2026"),
            ("state-bonus-depreciation-conformity", "State Bonus Depreciation Conformity"),
            ("irc-168-macrs-property-classification-guide", "IRC 168 and MACRS Property Classification"),
        ],
    },
    {
        "slug": "irs-audit-technique-guide-cost-segregation",
        "title": "The IRS Cost Segregation Audit Technique Guide: What Examiners Are Actually Told to Look For",
        "description": "The IRS publishes the guide its examiners use to review cost segregation studies, including the 13 principal elements of a quality study. Here is what it says and how to use it.",
        "date": DATE,
        "iso_date": ISO,
        "sections": [
            ("The Rare Case Where the IRS Shows Its Work", """<p>Cost segregation occupies an unusual position in tax practice. There is no statute that authorizes it by name, no regulation that prescribes a methodology, and no form to file. What exists instead is a body of case law running back to Hospital Corporation of America, and an Audit Technique Guide the IRS publishes for its own examiners.</p>
<p>The ATG is publicly available. It tells you, in the government's own words, how a study will be evaluated if it is examined. Reading it is the closest thing available to seeing the grading rubric before the test.</p>
<p>It is also the reason quality varies so much across providers. Firms that build to the ATG produce reports that look a certain way. Firms that do not produce reports that are shorter, cheaper, and considerably harder to defend.</p>"""),
            ("The Thirteen Principal Elements", """<p>The guide identifies thirteen elements it associates with a quality study. Paraphrased, they are: preparation by an individual with expertise and experience; a detailed methodology description; use of appropriate documentation; interviews with people who have knowledge of the property; a common nomenclature; a standard numbering system; an explanation of the legal analysis; a determination of unit costs and engineering takeoffs; an organized and detailed asset listing; reconciliation of total costs; an explanation of the treatment of indirect costs; identification and listing of Section 1245 property; and consideration of related aspects such as Section 263A and change in accounting method requirements.</p>
<p>None of these are optional in practice. A study missing several is not a study the IRS considers reliable, and the examiner is instructed to say so.</p>
<p>The element most commonly missing from low-cost studies is the engineering takeoff. That is the actual measurement and unit-cost work. Without it, the reclassification is an estimate dressed as an analysis.</p>"""),
            ("The Methodologies the Guide Recognizes", """<p>The ATG describes six approaches and ranks them implicitly by reliability. The detailed engineering approach from actual cost records is the gold standard, available where original construction invoices exist. The detailed engineering cost estimate approach is the standard for acquired property where records do not exist, and it is what most quality studies on purchased buildings use.</p>
<p>Below those sit the survey or letter approach, the residual estimation approach, the sampling or modeling approach, and the rule of thumb approach. The guide is direct about the last one: rule of thumb studies have little or no supporting documentation and are not considered reliable.</p>
<p>If a provider quotes you a price that seems impossibly low and turns the study around in three days without a site visit or a document request, you are almost certainly buying a rule of thumb study. It will produce a number. It will not produce support.</p>"""),
            ("What Examiners Are Told to Challenge", """<p>The guide directs examiners toward specific pressure points. Classification of electrical and plumbing systems is one: the distinction between building systems serving the structure generally, which are structural, and components serving specific equipment or process needs, which may be 1245 property, is fact-intensive and frequently overreached.</p>
<p>Site improvements are another. The line between land, which is non-depreciable, land improvements at 15 years, and building components is often drawn aggressively.</p>
<p>Cost allocation and reconciliation get sustained attention. The examiner is looking for whether the sum of the reclassified components plus the remaining structural basis equals the total depreciable basis. Reports that do not reconcile invite the conclusion that the numbers were assembled rather than derived.</p>"""),
            ("The Change in Accounting Method Overlay", """<p>The guide devotes real attention to the mechanics of applying a study to a property placed in service in a prior year. That is a change in method of accounting requiring Form 3115, filed under the automatic consent procedures, with a Section 481(a) adjustment.</p>
<p>Examiners check whether the Form 3115 was filed, whether the 481(a) computation is supported, and whether the taxpayer improperly amended prior returns instead of using the method change. Amending is generally not permitted for depreciation method changes after the second year, and doing it anyway is a straightforward adjustment for an examiner to make.</p>
<p>This is one of the more common procedural failures in self-prepared or low-cost studies. The engineering may be fine and the filing mechanics wrong, which produces the same outcome as bad engineering. AE Tax Advisors handles the procedural side in their """ + ae("form-3115-cost-segregation", "Form 3115 cost segregation") + """ guidance.</p>"""),
            ("How to Read Your Own Report Against the Guide", """<p>Open your report and look for four things. Is there a stated methodology naming which of the recognized approaches was used? Is there an asset-level listing with quantities, unit costs, and extended totals rather than category percentages? Is there a reconciliation tying components back to total basis? Is there a legal analysis section citing the authorities relied on?</p>
<p>If all four are present, your report is built the way the guide expects. If your report is twelve pages of summary tables with a percentage allocation and no takeoff detail, it will not hold under examination, and the price you paid was not a bargain.</p>
<p>Ask who performed the work. The guide expects expertise in both construction and tax. A study signed by someone with neither is a document, not an opinion.</p>"""),
            ("What This Means for Choosing a Provider", """<p>The practical takeaway is that the standard is knowable and testable. You do not have to take a provider's word about quality. You can ask which of the six methodologies they use, whether they perform a site visit, whether they produce engineering takeoffs, and whether they provide audit support if the study is examined.</p>
<p>Providers building to the ATG answer those questions easily because the answers are their selling points. Providers who do not tend to redirect toward price and turnaround time.</p>
<p>Every Stratum study is built to the thirteen elements, includes the reconciliation and legal analysis sections, and comes with audit support at no additional cost. That is not a differentiator so much as a baseline, but it is a baseline a surprising share of the market does not meet.</p>"""),
        ],
        "related": [
            ("how-to-choose-cost-segregation-company", "How to Choose a Cost Segregation Company"),
            ("diy-vs-professional-cost-segregation", "DIY vs Professional Cost Segregation"),
            ("how-to-read-cost-segregation-report", "How to Read a Cost Segregation Report"),
        ],
    },
    {
        "slug": "str-furniture-ffe-depreciation",
        "title": "Furniture, Fixtures, and Equipment in a Short-Term Rental: What Depreciates Fast and What Does Not",
        "description": "Furnishing a short-term rental creates 5-year and 7-year property that is fully deductible in year one. Here is what qualifies, how it interacts with a cost segregation study, and what owners miss.",
        "date": DATE,
        "iso_date": ISO,
        "sections": [
            ("The Deduction Owners Already Have and Do Not Claim", """<p>A short-term rental is furnished. A long-term rental usually is not. That single operational difference creates a category of deduction that many STR owners either capitalize into the building by mistake or expense inconsistently across years.</p>
<p>Furniture, fixtures, and equipment, commonly abbreviated FF&E, is tangible personal property under Section 1245. It carries a 5-year or 7-year MACRS recovery period, and it is bonus depreciation eligible, which means it is generally fully deductible in the year placed in service.</p>
<p>On a typical three-bedroom short-term rental, a full furnishing package runs $25,000 to $60,000. That is a first-year deduction sitting in an owner's credit card statements, and it is entirely separate from anything a cost segregation study produces on the building.</p>"""),
            ("What Falls Into the 5-Year and 7-Year Buckets", """<p>Under the MACRS asset class system, furniture and fixtures used in a rental activity generally land in the 7-year class, while appliances, carpeting, and certain equipment used in residential rental activity land in the 5-year class.</p>
<p>Practically, the 5-year bucket picks up refrigerators, ranges, dishwashers, washers and dryers, microwaves, window air conditioning units, carpeting and area rugs, televisions, and computer and networking equipment including smart locks, routers, and security cameras.</p>
<p>The 7-year bucket picks up beds, mattresses, sofas, dining sets, desks, dressers, patio furniture, and decorative fixtures that are not permanently attached. Outdoor equipment such as grills, fire pits, and hot tubs that are not permanently installed generally follows here as well.</p>"""),
            ("The Line Between FF&E and the Building", """<p>The classification question is whether an item is a component of the building or personal property that happens to be inside it. Permanence, method of attachment, and whether removal would damage the structure all matter.</p>
<p>A freestanding refrigerator is personal property. Built-in cabinetry is generally a building component. A wall-mounted television is personal property; the recessed niche and blocking installed to hold it may not be. A hot tub set on a pad is personal property; one integrated into a deck with dedicated plumbing and electrical runs closer to a land improvement or building component.</p>
<p>This is precisely the analysis a cost segregation engineer performs on the building itself, and it is why studies on short-term rentals reclassify more than studies on comparable long-term rentals. The property is simply built out with more removable content.</p>"""),
            ("Items Purchased Before Placing the Property in Service", """<p>A common sequencing issue: you buy the property in March, furnish it through April and May, and take the first booking in June. The furniture purchased in April was not placed in service when purchased. It was placed in service when the property became available for rent.</p>
<p>That timing matters for the placed-in-service date, for the mid-quarter convention test, and for which tax year the deduction lands in. Purchases made in a prior tax year but placed in service in the current year are deducted in the current year.</p>
<p>It also matters for what gets capitalized. Costs incurred to make the property ready for its intended use are generally capitalized into basis rather than expensed, though FF&E retains its own class life rather than folding into the 27.5-year or 39-year structure.</p>"""),
            ("The De Minimis Safe Harbor as an Alternative Path", """<p>The tangible property regulations provide a de minimis safe harbor election under Regulation 1.263(a)-1(f) that lets taxpayers expense items under a per-item or per-invoice threshold, $2,500 for taxpayers without an applicable financial statement, $5,000 for those with one.</p>
<p>For a short-term rental, most individual furniture and appliance purchases fall under $2,500. Electing the safe harbor lets you expense them directly rather than tracking them on a depreciation schedule for seven years.</p>
<p>The election is annual, made on a timely filed return, and requires a written accounting policy in place at the start of the year. It does not replace a cost segregation study, which addresses the building, but it dramatically simplifies the FF&E side and produces the same current-year result while bonus depreciation is at 100 percent.</p>"""),
            ("Replacement Cycles and Partial Dispositions", """<p>Short-term rental FF&E wears out fast. Mattresses, sofas, and linens on a well-booked property have a real life closer to three years than seven, and owners replace them regularly.</p>
<p>When you replace an item that has not been fully depreciated, you dispose of the old asset and recognize the remaining basis as a loss, then place the new asset in service. This is straightforward for tracked assets and impossible for untracked ones, which is an argument for maintaining a real fixed asset schedule rather than a shoebox.</p>
<p>The same concept applies at the building level through partial asset disposition elections, which let you write off the remaining basis of a replaced roof or HVAC system rather than depreciating a component that no longer exists.</p>"""),
            ("Coordinating FF&E With the Building Study", """<p>The cleanest approach is to treat them as two workstreams. The cost segregation study handles the acquisition basis of the building and site. A separate fixed asset schedule handles the furnishing package and subsequent capital purchases.</p>
<p>Owners run into trouble when the furnishing package gets folded into the building basis at closing, typically because the seller included furnishings in the sale. In that case, the purchase price allocation needs to separate the personal property, and the study should identify it explicitly rather than burying it in the structural component.</p>
<p>Whether the resulting loss is currently usable still depends on material participation and the passive activity rules. AE Tax Advisors covers that interaction in their """ + ae("str-tax-loophole", "short-term rental tax") + """ and """ + ae("rental-property-tax-planning", "rental property tax planning") + """ resources.</p>"""),
        ],
        "related": [
            ("cost-segregation-airbnb-properties", "Cost Segregation for Airbnb Properties"),
            ("5-year-7-year-15-year-property-examples", "5-Year, 7-Year, and 15-Year Property Examples"),
            ("partial-asset-disposition-cost-segregation", "Partial Asset Disposition Elections"),
        ],
    },
    {
        "slug": "cost-segregation-partnership-special-allocations",
        "title": "Cost Segregation Inside a Partnership: How Depreciation Gets Allocated Among Members",
        "description": "A cost segregation study in an LLC or partnership creates a large deduction that has to be allocated among partners. Here is how substantial economic effect, capital accounts, and basis limits govern who gets it.",
        "date": DATE,
        "iso_date": ISO,
        "sections": [
            ("The Deduction Is Only Half the Question", """<p>When a single owner runs a cost segregation study, the deduction goes to that owner and the analysis moves on to whether the passive activity rules allow its use. When a partnership or multi-member LLC runs one, an additional question appears first: who gets the deduction?</p>
<p>The answer is not automatically "everyone in proportion to ownership." Partnership tax allows allocations that differ from ownership percentages, and real estate partnerships use that flexibility constantly. It is also where the most expensive mistakes get made.</p>
<p>A $400,000 first-year deduction allocated to a partner who cannot use it is worth far less than the same deduction allocated to one who can. Getting the allocation right is a planning exercise, not a compliance afterthought.</p>"""),
            ("The Substantial Economic Effect Framework", """<p>Section 704(b) governs. An allocation stated in the operating agreement is respected if it has substantial economic effect, or if it is otherwise in accordance with the partners' interests in the partnership.</p>
<p>The economic effect prong is mechanical and has three requirements: capital accounts must be maintained in accordance with the regulations, liquidating distributions must be made in accordance with positive capital account balances, and there must be either an unconditional deficit restoration obligation or a qualified income offset provision.</p>
<p>The substantiality prong is the judgment-heavy part. An allocation lacks substantiality if its after-tax effect on one partner is enhanced and no partner is substantially diminished, considered on a present-value basis. Allocating depreciation to the partner in the highest bracket, with an offsetting allocation of gain later, is the classic pattern that gets tested here.</p>"""),
            ("Why Depreciation Allocations Get Special Attention", """<p>Depreciation deductions attributable to nonrecourse debt cannot have economic effect, because the partner bearing them has no economic risk. The regulations handle this through the nonrecourse deduction rules and minimum gain chargeback provisions in Regulation 1.704-2.</p>
<p>Most real estate partnerships are financed with nonrecourse debt, which means a substantial share of the depreciation from a cost segregation study will be nonrecourse deductions. Those must be allocated in a manner reasonably consistent with some other significant partnership item, and the agreement must contain a minimum gain chargeback.</p>
<p>Operating agreements drafted from generic templates frequently lack these provisions, or contain them in boilerplate that conflicts with the economic deal the partners actually struck. A large accelerated deduction is what surfaces the conflict. AE Tax Advisors addresses the capital account mechanics in their guide to """ + ae("the-business-owners-guide-to-section-704b-capital-accounts-and-partner-allocations", "Section 704(b) capital accounts and partner allocations") + """.</p>"""),
            ("Basis and At-Risk Limits Cap What a Partner Can Use", """<p>Even a valid allocation does not guarantee a usable deduction. Three limitations apply in sequence at the partner level.</p>
<p>First, Section 704(d) limits deductions to the partner's adjusted basis in the partnership interest. Basis includes the partner's share of partnership liabilities, and for real estate partnerships the share of nonrecourse debt under Section 752 is often what makes a large depreciation allocation usable at all.</p>
<p>Second, the at-risk rules of Section 465 limit deductions to amounts the partner is economically at risk for. Qualified nonrecourse financing secured by real property is generally treated as at-risk, which is why real estate is treated more favorably here than most activities.</p>
<p>Third, the passive activity rules of Section 469 apply. A limited partner or a passive member faces the full passive loss regime, and a cost segregation deduction that clears basis and at-risk can still suspend at this stage.</p>"""),
            ("Syndications and the Passive Investor Problem", """<p>In a syndication, most investors are passive by design. They contribute capital, take a limited role, and cannot claim real estate professional status or material participation on the deal.</p>
<p>Their share of the cost segregation deduction is a passive loss. It offsets passive income from that or other passive activities and otherwise suspends, carrying forward until they have passive income or dispose of the entire interest in a fully taxable transaction.</p>
<p>This is not a defect. Suspended losses released on disposition can shelter a substantial portion of the exit gain, which is frequently the point. But sponsors who market first-year deductions to passive investors without explaining the suspension mechanics create expectations that the K-1 will not meet.</p>"""),
            ("The Section 754 Election and Incoming Partners", """<p>When a partnership interest changes hands, the new partner's outside basis reflects what they paid, but the partnership's inside basis in its assets does not adjust unless a Section 754 election is in effect.</p>
<p>Without the election, an incoming partner who paid a premium for an appreciated property inherits a share of depreciation computed on the partnership's old, lower basis. With the election, a Section 743(b) adjustment steps up that partner's share of inside basis, generating additional depreciation allocated solely to them.</p>
<p>Cost segregation and a 754 election interact well. The step-up can itself be allocated across asset classes, meaning a portion lands in 5-year and 15-year property rather than all of it in the 39-year structure. That is an underused planning combination in partnerships with turnover.</p>"""),
            ("What to Do Before Commissioning the Study", """<p>Read the operating agreement first. Confirm that capital accounts are maintained under the 704(b) rules, that a qualified income offset or deficit restoration obligation is present, and that a minimum gain chargeback exists. If any is missing, amend before the deduction arrives, not after.</p>
<p>Model the allocation partner by partner against basis, at-risk, and passive limitations. The output you want is not "the study produces $400,000" but "partner A can currently use $180,000, partner B suspends $90,000, partner C is basis-limited at $40,000."</p>
<p>That model is what tells you whether the study should be run this year, next year, or paired with a capital contribution or debt restructuring that creates the basis to absorb it.</p>"""),
        ],
        "related": [
            ("cost-segregation-real-estate-syndications-passive-investors", "Cost Segregation in Syndications"),
            ("passive-activity-loss-rules-cost-segregation", "Passive Activity Loss Rules and Cost Segregation"),
            ("cost-segregation-apartment-buildings", "Cost Segregation for Apartment Buildings"),
        ],
    },
    {
        "slug": "cost-segregation-niit-net-investment-income-tax",
        "title": "Does Cost Segregation Reduce the 3.8% Net Investment Income Tax?",
        "description": "Rental income is generally subject to the 3.8 percent NIIT. A cost segregation deduction can reduce it, but only if the income is included in net investment income in the first place. Here is how the interaction works.",
        "date": DATE,
        "iso_date": ISO,
        "sections": [
            ("The Surtax That Sits on Top of Everything Else", """<p>Section 1411 imposes a 3.8 percent tax on the lesser of net investment income or the excess of modified adjusted gross income over a threshold: $200,000 for single filers, $250,000 for joint filers. Those thresholds are not indexed for inflation, so the tax reaches steadily further each year.</p>
<p>For real estate investors, the relevant point is that rental income is generally net investment income. So is gain on the sale of rental property. A high earner with a rental portfolio is typically paying 3.8 percent on top of their marginal rate on that income.</p>
<p>The question owners ask is whether a cost segregation deduction reduces it. The answer is usually yes, but the mechanism matters and there is a significant exception that cuts the other way.</p>"""),
            ("How Deductions Flow Into the NIIT Calculation", """<p>Net investment income is computed net of deductions properly allocable to that income. Depreciation on a rental property is properly allocable to the rental income it offsets.</p>
<p>So a cost segregation study that converts $500,000 of structural basis into currently deductible short-life property reduces rental net income, which reduces net investment income, which reduces the base on which the 3.8 percent is imposed.</p>
<p>If the study turns rental net income of $60,000 into a rental loss, the $60,000 that would have been subject to NIIT is eliminated. At 3.8 percent that is $2,280, on top of the ordinary rate savings. It is a secondary benefit, not the headline, but it is real.</p>"""),
            ("Where Passive Loss Suspension Interferes", """<p>The NIIT computation follows the Section 469 characterization. A passive loss suspended under the passive activity rules is not deductible for regular tax, and it is likewise not available to reduce net investment income in the year it suspends.</p>
<p>This means the same limitation that blocks your regular-tax benefit blocks your NIIT benefit. An investor whose cost segregation deduction suspends gets neither.</p>
<p>When the suspended loss is later released, either against passive income or on a fully taxable disposition of the activity, it reduces net investment income at that point. The benefit is deferred rather than lost, which is the same pattern as the regular tax treatment.</p>"""),
            ("The Real Estate Professional Exception That Cuts Both Ways", """<p>Here is the interaction that surprises people. Regulation 1.1411-4(g)(7) provides that rental income derived in the ordinary course of a trade or business, where the taxpayer is a real estate professional under Section 469(c)(7) and participates in the rental activity for more than 500 hours, is excluded from net investment income.</p>
<p>For a profitable portfolio, that exclusion is valuable. It removes the rental income from the NIIT base entirely.</p>
<p>For a portfolio generating losses from a cost segregation study, it works against you. If the income is excluded from net investment income, the corresponding loss is also excluded, so it cannot offset other investment income such as dividends, interest, or capital gains. A real estate professional with a $300,000 cost segregation loss and $300,000 of portfolio income does not get to net them for NIIT purposes.</p>"""),
            ("Short-Term Rentals Sit in a Different Position", """<p>A short-term rental where the average stay is seven days or less falls outside the Section 469 definition of a rental activity. If the owner materially participates, the losses are non-passive.</p>
<p>For NIIT purposes, the analysis turns on whether the activity is a trade or business in which the taxpayer materially participates. If it is, income and loss from it are excluded from net investment income under Section 1411(c)(2)(A).</p>
<p>The practical result mirrors the real estate professional case: material participation in a short-term rental generally takes the activity out of the NIIT base in both directions. Owners should not count on a short-term rental cost segregation loss to shelter portfolio income from the surtax. AE Tax Advisors covers the surtax mechanics in their guide to the """ + ae("net-investment-income-tax-reduce-3-8-percent-surtax", "net investment income tax") + """.</p>"""),
            ("The Disposition Year Is Where It Gets Large", """<p>Gain on sale of rental property is net investment income, and it is often the largest single item an investor will ever report. Depreciation recapture flows into that gain: unrecaptured Section 1250 gain taxed at up to 25 percent and Section 1245 recapture taxed at ordinary rates, both included in net investment income.</p>
<p>A cost segregation study accelerates depreciation, which lowers basis, which increases gain on sale. So the study can increase the NIIT exposure in the disposition year even as it reduced it in the holding years.</p>
<p>That is the standard time-value trade in cost segregation, and it applies to the surtax the same way it applies to the ordinary rate. It argues for planning the exit alongside the study rather than treating them as separate events, particularly for owners contemplating a hold shorter than seven years.</p>"""),
            ("Practical Takeaways", """<p>If you are a passive investor with rental income and no real estate professional status, a cost segregation study reduces NIIT to the extent it reduces rental net income, and to the extent the loss is not suspended.</p>
<p>If you are a real estate professional or a materially participating short-term rental owner, your rental income is likely already outside the NIIT base, so the study's NIIT benefit is limited. Its value comes from the ordinary rate reduction instead.</p>
<p>Either way, the 3.8 percent should be modeled, not assumed. It is small enough to ignore in a conversation and large enough to matter in a calculation, and its treatment depends entirely on facts that vary from one investor to the next.</p>"""),
        ],
        "related": [
            ("real-estate-professional-status-cost-segregation", "REPS and Cost Segregation"),
            ("depreciation-recapture-cost-segregation", "Depreciation Recapture After Cost Segregation"),
            ("cost-segregation-qbi-deduction-section-199a", "Cost Segregation and the QBI Deduction"),
        ],
    },
]


if __name__ == "__main__":
    for p in POSTS:
        print("wrote", write_post(p, ROOT))
