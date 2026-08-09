#!/usr/bin/env python3
"""Batch C: technical and mechanism long-tail posts."""

POSTS_C = [
    {
        "slug": "cost-segregation-bonus-depreciation-obbba-2026",
        "title": "Cost Segregation and Bonus Depreciation Under OBBBA: What Changed for 2026",
        "description": "The One Big Beautiful Bill Act restored 100 percent bonus depreciation permanently. Learn what that means for cost segregation, the acquisition date test, and how to plan around it in 2026.",
        "date": "August 2026",
        "iso_date": "2026-08-09",
        "sections": [
            ("The Phase-Down Reversed",
             """<p>For several years, cost segregation planning was dominated by a countdown. The Tax Cuts and Jobs Act had set bonus depreciation at 100 percent and then scheduled it to step down: 80 percent in 2023, 60 percent in 2024, 40 percent in 2025, 20 percent in 2026, and zero thereafter. Every conversation about a study included some version of act now, because the rate was falling.</p>
<p>The One Big Beautiful Bill Act changed that. It restored 100 percent bonus depreciation and made it permanent rather than scheduling another expiration. For property acquired after January 19, 2025 and placed in service thereafter, qualifying assets are fully deductible in the first year rather than at a reduced percentage.</p>
<p>That removes the artificial deadline that drove a lot of prior-year decision making, and it changes the shape of the planning conversation from when to whether.</p>"""),
            ("Why This Makes Cost Segregation More Valuable, Not Less",
             """<p>It is tempting to read a permanent benefit as a reason to delay. That reasoning does not hold up, for a simple reason: bonus depreciation does nothing for real property on its own.</p>
<p>Bonus depreciation applies to property with a recovery period of 20 years or less. A residential rental building is 27.5-year property. A commercial building is 39-year property. Neither qualifies. Without a cost segregation study, there is no short-lived property on your depreciation schedule for bonus depreciation to apply to, and the rate being 100 percent instead of 40 percent makes no difference at all.</p>
<p>The study is what creates the 5-year, 7-year, and 15-year classifications that bonus depreciation attaches to. At a 40 percent rate, a study that reclassified $1,000,000 produced $400,000 of first-year bonus. At 100 percent, the same study produces $1,000,000. The permanent restoration makes every study meaningfully more valuable than it was under the phase-down, which is the opposite of a reason to wait.</p>"""),
            ("The Acquisition Date Test Matters",
             """<p>The relevant date is generally when the property was acquired, not simply when it was placed in service. Property acquired after January 19, 2025 falls under the restored 100 percent rate. Property acquired before that date remains subject to the phase-down percentage that applied under prior law, even if it was placed in service later.</p>
<p>For most buyers this is straightforward. For anyone who had a binding written contract in place before that date, or who was mid-construction across the transition, the analysis requires care. A study should document the acquisition date and the rate applied rather than assuming 100 percent across the board.</p>
<p>This also matters for look-back studies. If you are running a study on a property placed in service in 2023, the bonus rate that applied in 2023 governs the catch-up computation. A look-back does not upgrade an old property to today's rate. It recovers what you were entitled to under the law that applied then, which is still substantial.</p>"""),
            ("What Else Changed That Affects Real Estate Owners",
             """<p>OBBBA also raised the Section 179 expensing limit substantially, to $2.5 million with a phaseout threshold beginning at $4 million. Section 179 and bonus depreciation are different tools with different rules. Section 179 is limited to taxable income and cannot create a loss, while bonus depreciation can. Section 179 also applies to certain nonresidential improvements, including roofs, HVAC, fire protection, and security systems, that bonus depreciation does not reach. Our post on <a href="/blog/section-179-vs-cost-segregation/">Section 179 versus cost segregation</a> covers when each applies.</p>
<p>The legislation also created a new category of qualified production property, allowing full expensing of certain nonresidential real property used in domestic manufacturing, subject to specific construction start and placed-in-service windows. For manufacturers building new capacity, that is a significant and separate opportunity worth evaluating alongside a conventional study.</p>
<p>State conformity remains a separate question entirely. Many states decouple from federal bonus depreciation and require an addback, which means your federal and state depreciation schedules diverge. Our post on <a href="/blog/state-bonus-depreciation-conformity/">state bonus depreciation conformity</a> covers which states follow federal treatment.</p>"""),
            ("What Actually Drives Timing Now",
             """<p>With the rate stable, the timing argument shifts to the time value of money and to your own tax position. A deduction taken in 2026 is worth more than the same deduction taken in 2029, because you have the cash in the interim. That argument is durable and does not depend on a legislative deadline.</p>
<p>The more important timing question is whether you have income to absorb the deduction. A large passive loss with no passive income to offset simply suspends and carries forward. In that case the study still has value, but the benefit is deferred until you have income or dispose of the property. Owners who expect a large income year, a property sale, or a change in participation status should sequence the study accordingly rather than defaulting to the earliest possible year.</p>
<p>AE Tax Advisors works through this sequencing with real estate owners in their <a href="{AE}/bonus-depreciation-rental-property/" target="_blank" rel="noopener">bonus depreciation</a> and <a href="{AE}/real-estate-investor-tax-planning/" target="_blank" rel="noopener">real estate investor tax planning</a> resources.</p>"""),
            ("Getting a Study Scoped for 2026",
             """<p>Stratum performs engineering-based cost segregation studies that document the acquisition date, the applicable bonus rate, and the classification support for every reclassified component. That documentation is what makes the position defensible if it is ever examined.</p>
<p>Request a free estimate or book a call to discuss your property and the year that makes the most sense to place the deduction.</p>"""),
        ],
        "related": [
            ("bonus-depreciation-2026-rental-property", "Bonus Depreciation for Rental Property in 2026"),
            ("section-179-vs-cost-segregation", "Section 179 vs. Cost Segregation"),
            ("state-bonus-depreciation-conformity", "State Bonus Depreciation Conformity"),
        ],
    },
    {
        "slug": "irc-168-macrs-property-classification-guide",
        "title": "IRC Section 168 and MACRS Property Classification: A Guide for Real Estate Owners",
        "description": "A practical guide to how IRC Section 168 and MACRS assign recovery periods, why buildings land at 27.5 or 39 years, and how cost segregation reclassifies components under the same statute.",
        "date": "August 2026",
        "iso_date": "2026-08-09",
        "sections": [
            ("Where Depreciation Rules Actually Come From",
             """<p>Every depreciation deduction a real estate owner claims traces back to IRC Section 168, the Modified Accelerated Cost Recovery System. MACRS is not a policy or a convention. It is a statute that assigns each depreciable asset a class life, a recovery period, a depreciation method, and an averaging convention.</p>
<p>Understanding the structure matters because cost segregation is frequently described as if it were an aggressive strategy layered on top of the rules. It is not. A cost segregation study is an exercise in applying Section 168 correctly to a property that was originally recorded as a single asset. The statute already provides shorter recovery periods for the components in question. The study identifies them.</p>
<p>The IRS itself acknowledges this. The Cost Segregation Audit Techniques Guide, which examiners use, describes the methodology and sets expectations for what a quality study contains. The dispute in practice is almost never about whether reclassification is permissible. It is about whether a particular component was correctly classified and adequately documented.</p>"""),
            ("How MACRS Assigns Recovery Periods",
             """<p>Section 168 sorts property into classes with defined recovery periods. The classes relevant to real estate owners are 5-year property, 7-year property, 15-year property, 27.5-year residential rental property, and 39-year nonresidential real property. There are others, including 3-year, 10-year, and 20-year classes, that appear less often in building studies.</p>
<p>Class assignment generally flows from the asset class tables in Revenue Procedure 87-56, which map asset types to class lives. Some classifications are set directly in the statute instead. Residential rental property is defined in Section 168(e)(2)(A) as a building where 80 percent or more of gross rental income comes from dwelling units, and it carries a 27.5-year period. Nonresidential real property is everything else that is real property, at 39 years.</p>
<p>Method and convention follow from class. Property in the 5-year, 7-year, and 15-year classes uses declining balance methods switching to straight line, while real property uses straight line. Personal property generally uses the half-year convention, or the mid-quarter convention if too much is placed in service late in the year. Real property uses the mid-month convention. These details affect the arithmetic more than most owners realize.</p>"""),
            ("The Structural Component Rule",
             """<p>The heart of a cost segregation analysis is the distinction between a structural component of a building and tangible personal property. Regulation 1.48-1(e), written for the old investment tax credit, remains the framework courts and the IRS use for the question.</p>
<p>A structural component includes walls, floors, ceilings, permanent coverings, windows and doors, and the central systems for heating, cooling, plumbing, electrical, and fire protection that serve the building. Those follow the building's recovery period.</p>
<p>Property that is not a structural component is Section 1245 personal property with its own, shorter recovery period. The tests that emerged from Whiteco Industries are the standard analysis: how permanently is the item attached, was it designed to be moved, how difficult is removal, and how is it treated in practice. Applied to a building, this is why a dedicated circuit serving a specific piece of equipment is personal property while the panel serving the whole building is structural.</p>
<p>Land improvements occupy a separate 15-year class under Section 168(e)(3)(E). Paving, sidewalks, site lighting, fencing, and landscaping are neither building nor personal property. They are improvements to land, and the statute gives them a 15-year life directly.</p>"""),
            ("Special Classifications Worth Knowing",
             """<p>Several provisions assign 15-year treatment to things that would otherwise be 39-year property. Qualified improvement property, defined in Section 168(e)(6), covers interior nonstructural improvements made to a nonresidential building after it was first placed in service, excluding enlargements, elevators and escalators, and internal structural framework. Retail motor fuels outlets meeting the test in Section 168(e)(3)(E)(iii) get 15-year treatment for the entire building.</p>
<p>Why 15 years matters so much: bonus depreciation under Section 168(k) applies to property with a recovery period of 20 years or less. Anything that lands in the 15-year class or shorter becomes eligible for immediate expensing. Anything that stays at 27.5 or 39 years does not. That single threshold is what makes reclassification worth doing.</p>"""),
            ("What This Means in Practice",
             """<p>When your closing statement records a single purchase price and your accountant records a single building asset, the property has not been classified under Section 168. It has been approximated. Every component inside that building still has a statutory recovery period, and lumping them together simply assigns them all the longest one.</p>
<p>A cost segregation study performs the classification the statute contemplates: identifying each component, determining its correct class under the asset class tables and the structural component rules, allocating basis to it using engineering-based cost data, and documenting the support. Our post on <a href="/blog/5-year-7-year-15-year-property-examples/">5-year, 7-year, and 15-year property examples</a> works through what lands in each class.</p>
<p>AE Tax Advisors covers the broader depreciation framework for real estate owners in their <a href="{AE}/real-estate-depreciation/" target="_blank" rel="noopener">real estate depreciation</a> and <a href="{AE}/depreciation-tax-strategy/" target="_blank" rel="noopener">depreciation strategy</a> resources.</p>"""),
            ("Applying It to Your Property",
             """<p>Stratum performs engineering-based studies that document the statutory and regulatory basis for every classification, following the methodology described in the IRS Cost Segregation Audit Techniques Guide.</p>
<p>Request a free estimate or book a call to discuss how Section 168 applies to your property.</p>"""),
        ],
        "related": [
            ("5-year-7-year-15-year-property-examples", "5-Year, 7-Year, and 15-Year Property Examples"),
            ("components-reclassified-cost-segregation", "What Components Get Reclassified in a Cost Segregation Study"),
            ("qualified-improvement-property-cost-segregation", "Qualified Improvement Property and Cost Segregation"),
        ],
    },
    {
        "slug": "5-year-7-year-15-year-property-examples",
        "title": "5-Year, 7-Year, and 15-Year Property: Examples From Real Cost Segregation Studies",
        "description": "A component-by-component look at what lands in the 5-year, 7-year, and 15-year MACRS classes in a cost segregation study, and the reasoning behind each classification.",
        "date": "August 2026",
        "iso_date": "2026-08-09",
        "sections": [
            ("The Three Buckets That Matter",
             """<p>A cost segregation study moves basis out of a 27.5-year or 39-year building classification and into shorter MACRS classes. In practice, almost everything reclassified lands in one of three buckets: 5-year property, 7-year property, or 15-year property.</p>
<p>All three qualify for bonus depreciation, because the threshold under Section 168(k) is a recovery period of 20 years or less. That means the practical difference between the buckets matters less for the first-year deduction than it does for what happens afterward, and for how recapture is computed on sale.</p>
<p>What follows is a working list of what actually lands in each class, drawn from the kinds of components engineering-based studies identify, along with the reasoning that puts them there.</p>"""),
            ("5-Year Property",
             """<p>The 5-year class captures most tangible personal property found inside a building. In residential rental property this includes appliances, carpeting and resilient flooring, window treatments, cabinetry and countertops that are not structural components, decorative and accent lighting, and furniture in a furnished rental.</p>
<p>In commercial property the list broadens: data and telecommunications cabling, security and access control systems, audiovisual systems, movable partitions and systems furniture, kitchen and break room equipment, walk-in refrigeration, signage that is not structurally integrated, and process or task lighting.</p>
<p>The category that owners most often miss is specialty utility infrastructure. Electrical, plumbing, gas, and air distribution that serves specific equipment rather than the building generally is personal property classified with the equipment it serves. A dedicated 220-volt circuit to a piece of machinery, the water and drain serving a specific process sink, and the compressed air drop at a workstation all belong here. The panel and the main distribution serving the whole building do not.</p>
<p>The test comes from Regulation 1.48-1(e) and the Whiteco factors: how permanently the item is attached, whether it was designed to be moved, how much damage removal causes, and how the item functions in practice.</p>"""),
            ("7-Year Property",
             """<p>The 7-year class appears less often in building studies but shows up meaningfully in certain asset types. Office furniture, fixtures, and equipment fall here, as do many categories of machinery not assigned elsewhere in the asset class tables.</p>
<p>In hotels and furnished properties, some of the furniture and case goods land at 7 years rather than 5, depending on how the asset class tables map the specific item and the activity. In manufacturing, a substantial amount of production equipment carries a 7-year life under the activity-based asset classes in Revenue Procedure 87-56.</p>
<p>For first-year deduction purposes, the distinction between 5-year and 7-year is immaterial when bonus depreciation applies at 100 percent, since both are fully expensed. It matters if bonus is not claimed, if the property is subject to a state that decouples from bonus, or when computing depreciation in later years on assets that were not fully expensed.</p>"""),
            ("15-Year Property",
             """<p>The 15-year class contains two very different things. The first is land improvements under Section 168(e)(3)(E): asphalt and concrete paving, parking lots, striping, curbs and gutters, sidewalks, site lighting and its underground conduit, fencing and gates, retaining walls, signage foundations, landscaping and irrigation, site utilities running from the property line, stormwater drainage and detention, pools and pool decking, playgrounds, and sport courts.</p>
<p>These are not part of a building and they are not personal property. The statute gives them their own class. On properties with large sites -- retail centers, dealerships, RV parks, garden apartments -- land improvements are frequently the largest reclassification category by dollar amount.</p>
<p>The second thing in the 15-year class is qualified improvement property: interior nonstructural improvements to a nonresidential building made after the building was first placed in service. QIP excludes building enlargements, elevators and escalators, and internal structural framework. For landlords who build out tenant space, correctly identifying <a href="/blog/qualified-improvement-property-cost-segregation/">QIP</a> instead of capitalizing to the 39-year building is one of the most valuable classification decisions available.</p>
<p>Retail motor fuels outlets meeting the statutory test are also 15-year property, including the building itself.</p>"""),
            ("Why the Classification Affects More Than Year One",
             """<p>With 100 percent bonus depreciation, all three classes produce the same first-year result: full expensing. The classification still matters for two reasons.</p>
<p>First, recapture. Section 1245 personal property, which includes the 5-year and 7-year assets, is recaptured as ordinary income on sale to the extent of depreciation claimed. Land improvements and QIP are Section 1250 property, which generally receives the more favorable unrecaptured gain treatment capped at 25 percent. A study that reclassifies heavily into 1245 property creates a different exit profile than one weighted toward land improvements. Our post on <a href="/blog/depreciation-recapture-cost-segregation/">depreciation recapture</a> covers the mechanics.</p>
<p>Second, states. Many states decouple from federal bonus depreciation and require an addback, in which case the actual recovery period governs the state deduction and the difference between 5, 7, and 15 years becomes real.</p>"""),
            ("Seeing It Applied to Your Property",
             """<p>Every property has a different mix. A car wash is weighted toward 5-year equipment. An RV park is almost entirely 15-year land improvements. A medical office splits between specialty 5-year systems and site work. Stratum studies document each component, the class assigned, the basis allocated, and the authority supporting the classification.</p>
<p>Request a free estimate or book a call and we will walk through the likely mix for your property type.</p>"""),
        ],
        "related": [
            ("irc-168-macrs-property-classification-guide", "IRC Section 168 and MACRS Property Classification"),
            ("land-improvements-15-year-property-cost-segregation", "15-Year Land Improvements in a Cost Segregation Study"),
            ("depreciation-recapture-cost-segregation", "Depreciation Recapture and Cost Segregation"),
        ],
    },
    {
        "slug": "section-481a-adjustment-catch-up-depreciation",
        "title": "The Section 481(a) Adjustment: How Catch-Up Depreciation Works on a Look-Back Study",
        "description": "A look-back cost segregation study recovers missed depreciation through a Section 481(a) adjustment on Form 3115. Learn how the catch-up is computed, why no amended returns are needed, and the timing rules.",
        "date": "August 2026",
        "iso_date": "2026-08-09",
        "sections": [
            ("The Mechanism That Makes Look-Back Studies Work",
             """<p>The most common question about cost segregation on a property you already own is some version of: have I missed my chance? The answer is no, and the reason is a provision most owners have never heard of.</p>
<p>Section 481(a) governs what happens when a taxpayer changes an accounting method. Rather than requiring you to go back and redo every affected prior year, it requires a single cumulative adjustment in the year of change, computed as the difference between what you actually deducted and what you would have deducted had the new method always been in place.</p>
<p>Applied to depreciation, that means an owner who has been depreciating a building straight-line for six years can adopt the correct component-level classifications, compute the entire six years of missed acceleration, and deduct all of it in the current year. Not spread over six years. All of it, in one year.</p>"""),
            ("Why This Is a Method Change Rather Than an Error Correction",
             """<p>The distinction matters. Correcting an error generally requires amending the return for the year the error occurred, and amended returns are subject to the statute of limitations, typically three years.</p>
<p>Depreciation is different. Under the regulations, using an impermissible method of depreciation for two or more consecutive years establishes a method of accounting. Changing from that method to a permissible one is a change in accounting method, which goes on Form 3115 rather than an amended return.</p>
<p>That has two consequences owners care about. First, no amended returns. You do not reopen prior years, you do not disturb prior filings, and you do not need your prior preparer's cooperation. Second, no lookback limit. Because you are not amending anything, the three-year statute is not the constraint. A study on a property placed in service in 2011 can capture every year of missed depreciation since 2011.</p>
<p>There is a wrinkle for property held less than two tax years. If you have used the original method for only one year, you have not yet established a method of accounting, and an amended return may be the correct route instead. That timing question should be settled before filing.</p>"""),
            ("How the Catch-Up Is Actually Computed",
             """<p>Consider a commercial property placed in service in January 2021 with a $3,000,000 depreciable basis. Under the 39-year straight-line schedule the owner has been deducting roughly $76,923 per year. Through the end of 2025, five years of deductions total approximately $384,615.</p>
<p>A study performed in 2026 determines that $900,000 should have been classified as 5-year and 15-year property. Had that classification been in place from the start, the owner would have claimed the applicable bonus depreciation on that $900,000 in 2021 plus depreciation on the remaining $2,100,000 shell over 39 years. The cumulative correct depreciation through 2025 is substantially larger than $384,615.</p>
<p>The difference between the two cumulative figures is the Section 481(a) adjustment. Because it is a favorable adjustment, meaning it decreases taxable income, it is taken entirely in the year of change. Unfavorable adjustments that increase income are generally spread over four years, but that is not the situation in a cost segregation look-back.</p>
<p>One important constraint: the bonus depreciation rate used in the computation is the rate that applied in the year the property was placed in service, not today's rate. A 2021 property uses the 2021 rate. A look-back recovers what you were entitled to under the law then.</p>"""),
            ("Filing Mechanics",
             """<p>The change is made on Form 3115, Application for Change in Accounting Method, filed under the automatic consent procedures. Because it is automatic, no advance IRS approval and no user fee are required. A copy of the form is attached to the timely filed return for the year of change, including extensions, and a duplicate is filed separately with the IRS.</p>
<p>The form requires a description of the present and proposed methods, the computation of the Section 481(a) adjustment, and the designated change number for the depreciation change being made. The cost segregation study is the supporting documentation behind the numbers on the form, and it should be retained rather than attached.</p>
<p>The deadline is the return due date including extensions for the year of change. This is a real constraint. A study started in late March for a calendar-year taxpayer may not be complete in time to file by the original deadline, which is one reason extensions are common in the year an owner adopts a study. Our post on <a href="/blog/form-3115-look-back-cost-segregation/">Form 3115 look-back cost segregation</a> covers the filing sequence in more detail, and AE Tax Advisors addresses the preparer side in their <a href="{AE}/form-3115-cost-segregation/" target="_blank" rel="noopener">Form 3115 guide</a>.</p>"""),
            ("The Question That Determines Whether It Is Worth It",
             """<p>A large catch-up deduction is only useful if you can absorb it. If the property is a passive rental and you have no passive income, the entire 481(a) adjustment becomes a suspended passive loss carrying forward. The study still has value, because the loss frees up when you have passive income or dispose of the property, but the cash benefit is deferred.</p>
<p>This is why timing a look-back deliberately often beats doing it as early as possible. An owner who expects to sell another property, take a large K-1 distribution, or qualify for real estate professional status in a particular year may be better served placing the catch-up in that year. Our post on <a href="/blog/passive-activity-loss-rules-cost-segregation/">passive activity loss rules and cost segregation</a> works through the analysis.</p>"""),
            ("Running the Numbers on Your Property",
             """<p>Stratum performs look-back studies on properties placed in service in any prior year, including the cumulative computation your CPA needs to complete Form 3115. If you have owned a property for more than a year and never had a study, the catch-up is usually the single largest deduction available to you.</p>
<p>Request a free estimate or book a call with your placed-in-service date and current depreciation schedule.</p>"""),
        ],
        "related": [
            ("form-3115-look-back-cost-segregation", "Form 3115 Look-Back Cost Segregation"),
            ("cost-segregation-existing-property", "Cost Segregation on a Property You Already Own"),
            ("passive-activity-loss-rules-cost-segregation", "Passive Activity Loss Rules and Cost Segregation"),
        ],
    },
    {
        "slug": "passive-activity-loss-rules-cost-segregation",
        "title": "Passive Activity Loss Rules and Cost Segregation: Why Your Deduction May Not Reduce Your Taxes",
        "description": "A large cost segregation deduction is worthless if IRC Section 469 suspends it. Learn how the passive activity rules work, the four exceptions, and how to plan a study around them.",
        "date": "August 2026",
        "iso_date": "2026-08-09",
        "sections": [
            ("The Question That Should Come Before the Study",
             """<p>Cost segregation marketing tends to lead with the deduction: six figures of first-year depreciation, unlocked from a property you already own. The deduction is real. Whether it reduces your tax bill this year is a separate question, and it is governed by IRC Section 469.</p>
<p>Section 469 divides income and loss into passive and non-passive. Passive losses can only offset passive income. If you generate a $200,000 passive loss and have no passive income, the loss does not reduce your W-2 wages, your business profit, or your portfolio income. It suspends and carries forward indefinitely.</p>
<p>This is the single most common disappointment in cost segregation. An owner runs a study, generates a large deduction, and discovers at filing that it is sitting on Form 8582 as a suspended loss doing nothing for the current year. The deduction is not lost, and it will eventually be used. But the cash benefit the owner was counting on does not arrive.</p>"""),
            ("Why Rentals Are Passive by Default",
             """<p>Section 469(c)(2) states the rule bluntly: a rental activity is passive regardless of whether the taxpayer materially participates. This is different from every other kind of business, where material participation determines the answer.</p>
<p>That means an owner who personally screens tenants, handles maintenance calls, and manages the books for a rental property is still generating passive losses. Effort does not change the classification for a rental activity. Only one of the specific exceptions does.</p>
<p>Understanding this is what separates realistic planning from wishful planning. Before commissioning a study, the honest question is not how large the deduction will be. It is which exception, if any, applies to you.</p>"""),
            ("The Four Ways Out",
             """<p><strong>The short-term rental exception.</strong> Regulation 1.469-1T(e)(3)(ii)(A) provides that an activity is not a rental activity if the average period of customer use is seven days or fewer. Because it is not a rental activity, the automatic passive rule does not apply, and ordinary material participation testing governs. An owner who materially participates in a qualifying short-term rental generates non-passive losses usable against W-2 income. This is the mechanism behind the <a href="/blog/cost-segregation-str-tax-loophole/">short-term rental strategy</a>, and it applies to hotels, RV parks, and campgrounds as well.</p>
<p><strong>Real estate professional status.</strong> Section 469(c)(7) allows a taxpayer who spends more than 750 hours in real property trades or businesses, and more than half of total working time in those activities, to treat rental activities in which they materially participate as non-passive. Only one spouse needs to qualify on a joint return, though the material participation test applies per activity unless a grouping election is made. Our post on <a href="/blog/real-estate-professional-status-cost-segregation/">REPS and cost segregation</a> covers the requirements.</p>
<p><strong>Passive income from elsewhere.</strong> If you own other profitable rentals or hold interests in passive businesses, the loss from a new study offsets that income immediately. Investors with a portfolio rarely have an absorption problem. Investors with one property and a salary usually do.</p>
<p><strong>The $25,000 special allowance.</strong> Section 469(i) allows up to $25,000 of rental losses against non-passive income for taxpayers who actively participate, a lower standard than material participation. It phases out between $100,000 and $150,000 of modified AGI, which means it is unavailable to most taxpayers large enough to be considering a cost segregation study.</p>"""),
            ("What Happens to a Suspended Loss",
             """<p>Suspended losses are not forfeited. They carry forward and become available in three circumstances.</p>
<p>First, when the activity generates passive income in a later year. Second, when you have passive income from any other source, since suspended losses from one activity can offset passive income generally. Third, and most importantly, when you dispose of your entire interest in the activity in a fully taxable transaction to an unrelated party. At that point all suspended losses attributable to the activity are freed and become fully deductible against any income.</p>
<p>That third rule is worth planning around. An owner who runs a study, suspends the loss for six years, then sells the property releases the entire accumulated suspension in the year of sale, where it offsets the gain on the sale itself. Note that a 1031 exchange is not a fully taxable disposition, so it does not trigger the release. Exchanging defers the gain and keeps the suspended loss suspended.</p>"""),
            ("Planning the Study Around the Answer",
             """<p>The practical takeaway is that the study should be timed to the year you can use it, not simply the earliest year available. Because a <a href="/blog/section-481a-adjustment-catch-up-depreciation/">Section 481(a) catch-up</a> lets you claim all prior missed depreciation in whatever year you file Form 3115, you have real control over which year receives the deduction.</p>
<p>An owner who expects to qualify for real estate professional status next year, or to sell an appreciated property, or to convert a long-term rental to short-term use, may generate substantially more value by placing the catch-up in that year. This is a conversation to have with a tax advisor before commissioning the study rather than after receiving it. AE Tax Advisors works through this analysis with investors in their <a href="{AE}/passive-activity-loss-rules-real-estate/" target="_blank" rel="noopener">passive activity loss rules</a> and <a href="{AE}/real-estate-professional-status-reps/" target="_blank" rel="noopener">real estate professional status</a> resources.</p>"""),
            ("Getting an Honest Assessment",
             """<p>Stratum will tell you before you engage whether the deduction is likely to be usable in your situation. If the answer is that it suspends with no clear path to absorption, we will say so rather than sell you a study.</p>
<p>Request a free estimate or book a call to talk through your property and your income picture.</p>"""),
        ],
        "related": [
            ("real-estate-professional-status-cost-segregation", "REPS and Cost Segregation"),
            ("offset-w2-income-rental-property", "How to Offset W-2 Income with Rental Property Depreciation"),
            ("section-481a-adjustment-catch-up-depreciation", "The Section 481(a) Catch-Up Adjustment"),
        ],
    },
    {
        "slug": "cost-segregation-long-term-rentals",
        "title": "Cost Segregation for Long-Term Rentals: What Buy-and-Hold Investors Should Expect",
        "description": "Long-term residential rentals reclassify 20 to 30 percent of basis through cost segregation on a 27.5-year schedule. Learn what qualifies, the passive loss constraint, and when a study makes sense.",
        "date": "August 2026",
        "iso_date": "2026-08-09",
        "sections": [
            ("The 27.5-Year Baseline",
             """<p>Long-term residential rentals depreciate over 27.5 years under IRC Section 168(e)(2)(A), which is already the shortest recovery period the tax code assigns to a building. That shorter baseline means the gap between default treatment and a cost segregation study is narrower for long-term rentals than for commercial property on a 39-year schedule.</p>
<p>Narrower is not small. A $400,000 depreciable basis produces $14,545 per year under straight-line. A study that reclassifies 25 percent of that basis and applies 100 percent bonus depreciation produces roughly $100,000 in year one instead. That is a seven-fold difference in first-year deduction on a modest single-family rental.</p>
<p>Long-term rentals typically reclassify 20 to 30 percent of depreciable basis. Newer construction with updated finishes and properties with meaningful site work land at the higher end. Older properties with minimal exterior improvements land lower.</p>"""),
            ("What Reclassifies in a Long-Term Rental",
             """<p>The 5-year bucket in a residential rental covers appliances including the refrigerator, range, dishwasher, microwave, washer, and dryer, carpeting and vinyl or luxury vinyl plank flooring, window blinds and treatments, cabinetry and countertops that are not structural components, decorative and accent lighting, ceiling fans, and the dedicated electrical serving specific appliances.</p>
<p>The 15-year land improvement bucket covers driveways and parking pads, walkways and patios, decks that are not structurally integrated, fencing, retaining walls, exterior site lighting, landscaping and irrigation, sheds and detached structures, and site drainage. On a single-family rental with a large lot, land improvements are frequently the larger of the two categories.</p>
<p>What stays on the 27.5-year schedule is the shell: foundation, framing, roof, siding, windows and doors, drywall, and the central HVAC, plumbing, and electrical systems that serve the house as a whole.</p>
<p>Small multifamily follows the same pattern with more of everything, since each unit repeats the appliance and finish package. Our post on <a href="/blog/cost-segregation-duplexes-multifamily/">cost segregation for duplexes and small multifamily</a> covers that variation.</p>"""),
            ("The Constraint Long-Term Rental Owners Have to Face",
             """<p>Here is where long-term rentals differ sharply from short-term rentals, and it is the most important thing a buy-and-hold investor should understand before commissioning a study.</p>
<p>A long-term rental is a rental activity under IRC Section 469, and rental activities are passive regardless of how much work the owner does. The short-term rental exception, which requires an average stay of seven days or fewer, is unavailable by definition when your tenants sign twelve-month leases.</p>
<p>That means the accelerated depreciation is a passive loss. It offsets passive income. It does not offset W-2 wages or active business income unless you qualify for <a href="/blog/real-estate-professional-status-cost-segregation/">real estate professional status</a>, which requires more than 750 hours in real property trades or businesses and more than half of your total working time.</p>
<p>For a full-time investor or a spouse who manages the portfolio, REPS is achievable. For a physician, engineer, or executive with a day job and three rentals, it generally is not. That investor's study still produces value, but as a suspended loss that frees up when there is passive income or when the property is sold in a fully taxable disposition.</p>"""),
            ("When a Long-Term Rental Study Clearly Makes Sense",
             """<p>Several fact patterns make the answer straightforward.</p>
<p>You own multiple rentals and some are profitable. The loss from a study on the new acquisition offsets the passive income from the others immediately.</p>
<p>You or your spouse qualifies for real estate professional status. The loss becomes non-passive and reduces household income directly.</p>
<p>You are planning to sell another property. Suspended losses free up on a fully taxable disposition, and a study performed in advance builds a loss position that offsets the eventual gain.</p>
<p>You have a large accumulated suspended loss already and expect passive income going forward. Adding to the pile is still useful if the pile will eventually be used.</p>
<p>Conversely, if you own one rental, work a W-2 job, have no other passive income, and plan to hold indefinitely through 1031 exchanges, a study will produce a deduction that sits unused for a very long time. That is the case where we tell owners to wait. Our post on <a href="/blog/when-not-to-do-cost-segregation/">when not to do a cost segregation study</a> covers the other disqualifying patterns.</p>"""),
            ("Look-Backs and Portfolio Timing",
             """<p>Because a <a href="/blog/section-481a-adjustment-catch-up-depreciation/">Section 481(a) adjustment</a> lets you claim all prior missed depreciation in the year you file Form 3115, buy-and-hold investors have unusual flexibility over timing. You are not required to run the study in the year you buy. You can hold the option and exercise it in the year the deduction is most useful.</p>
<p>Investors with a portfolio often stage studies deliberately: one property per year, timed to offset the passive income the portfolio throws off, rather than running everything at once and creating a suspended loss that takes a decade to absorb. AE Tax Advisors works with buy-and-hold investors on this sequencing in their <a href="{AE}/long-term-rental-tax-planning/" target="_blank" rel="noopener">long-term rental tax planning</a> and <a href="{AE}/rental-property-tax-planning/" target="_blank" rel="noopener">rental property tax planning</a> services.</p>"""),
            ("Getting a Realistic Estimate",
             """<p>Stratum performs engineering-based studies on long-term residential rentals nationwide, and we will tell you honestly whether the deduction is likely to be usable in your situation before you engage.</p>
<p>Request a free estimate or book a call with your purchase price, placed-in-service date, and a summary of your other income.</p>"""),
        ],
        "related": [
            ("cost-segregation-single-family-rentals", "Cost Segregation for Single-Family Rentals"),
            ("passive-activity-loss-rules-cost-segregation", "Passive Activity Loss Rules and Cost Segregation"),
            ("when-not-to-do-cost-segregation", "When Not to Do a Cost Segregation Study"),
        ],
    },
    {
        "slug": "how-cost-segregation-works-real-estate-investors",
        "title": "How Cost Segregation Works: A Step-by-Step Walkthrough for Real Estate Investors",
        "description": "A practical walkthrough of how a cost segregation study actually works, from basis determination through engineering analysis, classification, reporting, and filing.",
        "date": "August 2026",
        "iso_date": "2026-08-09",
        "sections": [
            ("What a Study Actually Does",
             """<p>Most explanations of cost segregation stop at the concept: it reclassifies building components into shorter depreciation categories. True, but it does not tell an investor what happens between signing an engagement and claiming a deduction.</p>
<p>Here is the actual sequence. A study determines your depreciable basis, breaks the property into its component assets, assigns each component a MACRS class under IRC Section 168, allocates a defensible dollar amount to each, and documents all of it in a report your CPA uses to rebuild your depreciation schedule.</p>
<p>The output is not tax advice and it is not a filing. It is an engineering and cost analysis that produces the numbers a tax return needs. Understanding that division of labor helps set expectations about what the study provider does and what your CPA does.</p>"""),
            ("Step One: Establishing Depreciable Basis",
             """<p>Everything starts with basis, and basis is not the same as purchase price.</p>
<p>Start with the total acquisition cost, then add capitalized closing costs such as title fees, recording fees, and transfer taxes. Certain items are excluded, including prepaid insurance, prepaid taxes, and loan-related costs, which are amortized separately rather than added to basis.</p>
<p>Then subtract land. Land is never depreciable, and the allocation between land and improvements is one of the two most consequential numbers in the entire study. An unsupported allocation that assigns too little to land inflates every downstream figure and creates real exposure. Defensible approaches include the county assessor's ratio, an appraisal that separately values land, or comparable land sales in the market. The study should document which method was used and why.</p>
<p>What remains after land is your depreciable basis, and it is the number the entire study allocates.</p>"""),
            ("Step Two: The Engineering Analysis",
             """<p>This is what distinguishes an engineering-based study from a rule-of-thumb estimate. The IRS Cost Segregation Audit Techniques Guide describes several methodologies, and the detailed engineering approach is the one it treats as most reliable.</p>
<p>For a new construction or a recent renovation, the analysis works from actual cost data: the contractor's schedule of values, pay applications, change orders, and subcontractor invoices. Every dollar has a known destination, which produces the most precise result available.</p>
<p>For an acquisition, actual construction costs generally do not exist, so the analysis works from a site inspection and takeoffs. An engineer documents the property through photographs, measures and counts components, reviews available plans, and then applies published construction cost data such as RSMeans to estimate the replacement cost of each component. Those component costs are then reconciled proportionally back to actual purchase basis, so the pieces sum to what you actually paid rather than to a theoretical construction cost.</p>
<p>Utility systems get particular attention, because that is where much of the value sits and where the structural component analysis is least obvious. Tracing electrical, plumbing, and mechanical from source to endpoint is what determines whether a given run serves the building or serves specific equipment.</p>"""),
            ("Step Three: Classification and Documentation",
             """<p>Each identified component is assigned a MACRS class. Personal property lands at 5 or 7 years, land improvements at 15 years, qualified improvement property at 15 years, and the remaining shell at 27.5 or 39 years depending on whether the property is residential rental or nonresidential real property.</p>
<p>The classification rests on the asset class tables in Revenue Procedure 87-56, the structural component definition in Regulation 1.48-1(e), and the permanence analysis derived from the Whiteco factors. A quality report states the authority for each classification rather than presenting a bare list of numbers. Our post on <a href="/blog/irc-168-macrs-property-classification-guide/">IRC Section 168 and MACRS classification</a> explains the framework in more detail.</p>
<p>The deliverable typically includes the basis computation and land allocation support, a component-level asset listing with cost and class for each item, photographic documentation, a description of the methodology, the depreciation schedules by class and year, and the technical authority relied upon. If you ever face examination, this report is the defense.</p>"""),
            ("Step Four: Getting It Onto the Return",
             """<p>What happens next depends on when the property was placed in service.</p>
<p>If the study covers the current tax year, your CPA simply uses the new schedules when preparing the return. No special election or form is required. The property is depreciated correctly from the start.</p>
<p>If the property was placed in service in a prior year and has been depreciated straight-line for two or more years, the change is a change in accounting method. Your CPA files <a href="/blog/form-3115-look-back-cost-segregation/">Form 3115</a> under the automatic consent procedures and claims the cumulative catch-up as a <a href="/blog/section-481a-adjustment-catch-up-depreciation/">Section 481(a) adjustment</a> in the current year. No amended returns are required and there is no limit on how far back the study reaches.</p>
<p>Timeline in practice: two to four weeks from engagement to delivered report for most residential and small commercial properties, longer for large or complex assets. Owners filing by an original deadline should start well before it, and extensions are common in the first year a study is adopted.</p>"""),
            ("The Question to Answer Before Any of This",
             """<p>None of the mechanics matter if the deduction cannot be used. Before commissioning a study, determine whether the resulting loss will be passive and, if so, whether you have passive income to absorb it or qualify for an exception. That analysis is covered in our post on <a href="/blog/passive-activity-loss-rules-cost-segregation/">passive activity loss rules and cost segregation</a>.</p>
<p>Coordinating the study with your overall tax picture is worth doing with an advisor rather than in isolation. AE Tax Advisors covers the planning side for investors in their <a href="{AE}/cost-segregation-studies-for-real-estate-investors/" target="_blank" rel="noopener">cost segregation for real estate investors</a> and <a href="{AE}/tax-planning-for-real-estate-investors/" target="_blank" rel="noopener">real estate tax planning</a> resources.</p>
<p>Stratum performs engineering-based studies nationwide. Request a free estimate or book a call to walk through your property.</p>"""),
        ],
        "related": [
            ("what-is-cost-segregation", "What Is Cost Segregation?"),
            ("irc-168-macrs-property-classification-guide", "IRC Section 168 and MACRS Property Classification"),
            ("how-to-read-cost-segregation-report", "How to Read a Cost Segregation Report"),
        ],
    },
    {
        "slug": "qualified-improvement-property-cost-segregation",
        "title": "Qualified Improvement Property and Cost Segregation: The 15-Year Classification Landlords Miss",
        "description": "QIP is interior nonstructural improvement to nonresidential buildings, recovered over 15 years and bonus eligible. Learn the definition, the exclusions, and why landlords routinely misclassify it.",
        "date": "August 2026",
        "iso_date": "2026-08-09",
        "sections": [
            ("A Classification Worth 24 Years",
             """<p>When a landlord builds out a tenant suite, remodels a lobby, or replaces interior finishes in a commercial building, the default bookkeeping treatment is to capitalize the cost to the building. That puts it on a 39-year schedule.</p>
<p>In many cases that is wrong. Interior nonstructural improvements made to a nonresidential building after the building was first placed in service are qualified improvement property, defined in IRC Section 168(e)(6), and QIP carries a 15-year recovery period rather than 39.</p>
<p>Because 15-year property has a recovery period of 20 years or less, it is eligible for bonus depreciation under Section 168(k). With bonus at 100 percent, correctly identifying QIP can mean the difference between deducting a $500,000 buildout over 39 years and deducting all of it in year one.</p>"""),
            ("The Definition and Its Exclusions",
             """<p>QIP is any improvement made by the taxpayer to an interior portion of a building which is nonresidential real property, if the improvement is placed in service after the date the building was first placed in service.</p>
<p>Three things are expressly excluded. Improvements attributable to the enlargement of the building. Elevators and escalators. And any improvement attributable to the internal structural framework of the building.</p>
<p>Several implications follow. QIP applies only to nonresidential property, so an apartment building renovation does not qualify. The improvement must be interior, so roof work, exterior facade, windows, and site work are outside the definition. And the building must already have been placed in service, so improvements made as part of original construction are not QIP -- they are simply part of the building.</p>
<p>Note also that the improvement must be made by the taxpayer. If you buy a building that a previous owner improved, you have acquired a building, not QIP. The classification attaches to improvements you make.</p>"""),
            ("The Retail Glitch and Why History Matters",
             """<p>QIP has a complicated recent history that still causes confusion. The Tax Cuts and Jobs Act intended to assign QIP a 15-year life, but a drafting error left it at 39 years and therefore ineligible for bonus depreciation. This was widely known as the retail glitch, and it meant that from 2018 through early 2020, taxpayers were required to recover QIP over 39 years.</p>
<p>The CARES Act corrected the error retroactively to property placed in service after 2017. Taxpayers who had capitalized QIP at 39 years during that window were permitted to change their method and recover the difference.</p>
<p>This history matters because it is still producing look-back opportunities. Buildings improved during that period may still be sitting on 39-year schedules if nobody revisited the classification after the fix. A <a href="/blog/section-481a-adjustment-catch-up-depreciation/">Section 481(a) catch-up</a> on Form 3115 recovers it.</p>"""),
            ("QIP Versus 5-Year Property Inside the Same Buildout",
             """<p>A common misunderstanding is that QIP and cost segregation are alternatives. They are not. A tenant buildout contains both.</p>
<p>Within a $500,000 office buildout, a study might identify $150,000 of 5-year personal property -- data cabling, decorative lighting, movable partitions, appliances, security systems, and the dedicated electrical serving specific equipment. Another $300,000 might be QIP: new interior walls, ceilings, general lighting, interior doors, flooring, and the HVAC distribution serving the improved space. The remaining $50,000 might be structural work or exterior scope that stays on the 39-year building.</p>
<p>All of the 5-year property and all of the QIP is bonus eligible, so with 100 percent bonus the first-year outcome is similar. Where the distinction becomes real is on sale. The 5-year personal property is Section 1245 property subject to full ordinary income recapture. QIP is Section 1250 property, generally receiving the more favorable unrecaptured gain treatment capped at 25 percent. Our post on <a href="/blog/depreciation-recapture-cost-segregation/">depreciation recapture</a> covers the difference.</p>"""),
            ("Section 179 Reaches Things QIP Does Not",
             """<p>There is a fourth category worth knowing. Section 179 expensing applies to certain improvements to nonresidential real property that fall outside both QIP and personal property: roofs, HVAC units, fire protection and alarm systems, and security systems.</p>
<p>Those items are structural components on a 39-year life, and they are not bonus eligible. But they can be expensed under Section 179 subject to the annual limit and the taxable income limitation. For a landlord replacing a roof and an HVAC system in the same year, Section 179 is the only accelerated option available. Our post on <a href="/blog/section-179-vs-cost-segregation/">Section 179 versus cost segregation</a> covers how the two interact.</p>
<p>Because Section 179 cannot create a loss and bonus depreciation can, the ordering of these elections matters and should be modeled rather than defaulted. AE Tax Advisors addresses the interaction for commercial owners in their guide to <a href="{AE}/the-business-owners-guide-to-qualified-improvement-property-qip-and-tenant-renovations/" target="_blank" rel="noopener">QIP and tenant renovations</a>.</p>"""),
            ("Getting Buildouts Classified Correctly",
             """<p>If you own commercial property and have capitalized tenant buildouts, remodels, or interior renovations to the building over the past several years, there is a reasonable chance some of it should be sitting at 15 years instead of 39.</p>
<p>Stratum performs engineering-based studies that separate QIP, personal property, land improvements, and structural components within a single renovation, and provides the documentation your CPA needs for a current-year filing or a Form 3115 catch-up.</p>
<p>Request a free estimate or book a call with your renovation history.</p>"""),
        ],
        "related": [
            ("section-179-vs-cost-segregation", "Section 179 vs. Cost Segregation"),
            ("partial-asset-disposition-cost-segregation", "Partial Asset Disposition and Cost Segregation"),
            ("cost-segregation-retail-properties", "Cost Segregation for Retail Properties"),
        ],
    },
    {
        "slug": "land-improvements-15-year-property-cost-segregation",
        "title": "15-Year Land Improvements: The Cost Segregation Category Owners Overlook",
        "description": "Land improvements are 15-year property under IRC Section 168(e)(3)(E) and fully bonus eligible. Learn what qualifies, how they differ from non-depreciable land, and why they often exceed 5-year property.",
        "date": "August 2026",
        "iso_date": "2026-08-09",
        "sections": [
            ("Neither Land Nor Building",
             """<p>Cost segregation conversations usually focus on personal property: appliances, cabinets, cabling, specialty electrical. That is where the intuition goes, because those items are visibly separate from the building.</p>
<p>On many properties, the larger reclassification category is something else entirely. Land improvements are a distinct class under IRC Section 168(e)(3)(E), carrying a 15-year recovery period, and on properties with significant site work they routinely exceed the 5-year personal property total.</p>
<p>The reason they get overlooked is that they are invisible in the accounting. When a property is recorded as land plus building, everything outside the four walls gets swept into one bucket or the other. The paving becomes part of the building. The parking lot lighting becomes part of the building. Neither is correct.</p>"""),
            ("What Counts as a Land Improvement",
             """<p>Land improvements are depreciable additions made to land that are not part of a building and are not personal property. The category includes asphalt and concrete paving for parking, drives, and aprons, striping, wheel stops, curbs and gutters, sidewalks and walkways, patios and hardscape, retaining walls, exterior site lighting including poles, bases, and underground conduit, signage foundations and pylon structures, fencing and gates, landscaping, trees and shrubs, and irrigation systems, site utilities running from the property line to the building including water, sewer, gas, and electrical service, storm drainage, catch basins, and detention and retention basins, swimming pools and pool decking, playgrounds and sport courts, and outdoor amenity structures such as pavilions and shade structures.</p>
<p>All of it depreciates over 15 years using the 150 percent declining balance method under MACRS, and all of it qualifies for bonus depreciation because 15 years is within the 20-year threshold under Section 168(k).</p>"""),
            ("The Line Against Non-Depreciable Land",
             """<p>The critical distinction in this category is not between land improvements and the building. It is between land improvements and land itself, because land is never depreciable.</p>
<p>Raw land, and the cost of permanently preparing it, stays in the non-depreciable bucket. General grading and clearing that permanently changes the contour of the site is treated as part of the land. So is the cost of the land itself, obviously.</p>
<p>But grading, excavation, and fill that is directly associated with and necessary for a specific improvement is generally depreciable with that improvement. The excavation for a parking lot subgrade, the trenching for site utilities, and the base preparation beneath a concrete pad are part of the improvement rather than part of the land.</p>
<p>This distinction has real dollars behind it on properties with substantial sitework, and it is the kind of determination that requires engineering judgment applied to actual construction records or takeoffs. It is also a common examination focus, which is why a defensible study documents the reasoning rather than simply asserting a number.</p>"""),
            ("Why the Category Dominates Certain Property Types",
             """<p>Land improvements scale with site area rather than with building area, which means their share of total cost varies enormously by property type.</p>
<p>An <a href="/blog/cost-segregation-rv-parks-campgrounds/">RV park</a> is nearly all land improvement, with pads, roads, and utility distribution across the entire site and only a small bathhouse and office as building. Reclassification in the 50 to 70 percent range is typical. An <a href="/blog/cost-segregation-auto-dealerships/">auto dealership</a> paves its display lot heavily and lights it for night visibility, pushing land improvements to 20 to 25 percent of basis on its own. <a href="/blog/cost-segregation-retail-properties/">Retail centers</a>, garden apartments, and suburban office parks all carry large surface lots.</p>
<p>At the other end, a downtown office tower with structured parking integrated into the building and a small streetscape footprint may have almost no land improvements at all. That is a large part of why urban assets reclassify at lower percentages than suburban ones.</p>"""),
            ("A Better Recapture Profile Than Personal Property",
             """<p>Land improvements have an advantage that owners planning an exit should understand. They are Section 1250 property, not Section 1245 property.</p>
<p>Section 1245 personal property is subject to full ordinary income recapture on sale, to the extent of depreciation claimed. Section 1250 property generally receives unrecaptured Section 1250 gain treatment, taxed at a maximum federal rate of 25 percent rather than at ordinary rates.</p>
<p>That means a study weighted toward land improvements produces a materially better exit profile than one weighted toward 5-year equipment, even though both deliver the same first-year deduction under 100 percent bonus depreciation. For an owner in the top bracket, the spread between ordinary rates and the 25 percent cap is meaningful. Our post on <a href="/blog/depreciation-recapture-cost-segregation/">depreciation recapture and cost segregation</a> works through the computation.</p>
<p>AE Tax Advisors covers how this interacts with a planned sale or exchange in their <a href="{AE}/1031-exchange-guide/" target="_blank" rel="noopener">1031 exchange guide</a> and <a href="{AE}/real-estate-depreciation/" target="_blank" rel="noopener">real estate depreciation</a> resources.</p>"""),
            ("Capturing What You Already Own",
             """<p>If you own a property with a parking lot, a fenced yard, site lighting, or landscaped grounds, and your depreciation schedule shows one line for land and one for building, there is 15-year property sitting inside your 27.5-year or 39-year asset right now.</p>
<p>A look-back study with Form 3115 recovers all of the missed acceleration in the current tax year. Stratum performs engineering-based studies that separate and document land improvements with the support required to withstand examination.</p>
<p>Request a free estimate or book a call to discuss your site.</p>"""),
        ],
        "related": [
            ("5-year-7-year-15-year-property-examples", "5-Year, 7-Year, and 15-Year Property Examples"),
            ("cost-segregation-rv-parks-campgrounds", "Cost Segregation for RV Parks and Campgrounds"),
            ("depreciation-recapture-cost-segregation", "Depreciation Recapture and Cost Segregation"),
        ],
    },
    {
        "slug": "cost-segregation-real-estate-syndications-passive-investors",
        "title": "Cost Segregation in Real Estate Syndications: What Limited Partners Should Expect on a K-1",
        "description": "Syndications routinely run cost segregation studies, producing large first-year losses on LP K-1s. Learn how those losses are allocated, why they are usually passive, and what actually happens at exit.",
        "date": "August 2026",
        "iso_date": "2026-08-09",
        "sections": [
            ("Why Nearly Every Syndication Runs a Study",
             """<p>If you have invested as a limited partner in an apartment, self-storage, or industrial syndication, you have almost certainly received a K-1 in year one showing a large loss despite the property performing well and distributing cash.</p>
<p>That loss is cost segregation. Sponsors run a study on the property in the first year, apply bonus depreciation to the reclassified components, and allocate the resulting depreciation among the partners according to the operating agreement. A deal that reclassifies 30 percent of a $20,000,000 basis generates roughly $6,000,000 of first-year bonus depreciation, and most of that flows to the limited partners.</p>
<p>For the sponsor, this is a genuine feature to market. For the investor, the value depends entirely on a question the offering memorandum usually does not address in detail: whether you can actually use the loss.</p>"""),
            ("The Loss Is Almost Always Passive",
             """<p>A limited partner in a real estate syndication holds a passive interest by nearly every measure. The activity is a rental activity under IRC Section 469, which is passive regardless of participation. And limited partners are generally presumed not to materially participate, with narrow exceptions.</p>
<p>That means the loss on your K-1 is a passive loss. It offsets passive income and nothing else. It does not reduce your W-2 wages, your consulting income, your business profit, or your dividends and interest.</p>
<p>If you hold other passive investments generating income -- other syndications distributing taxable income, profitable rentals, or non-managed business interests -- the loss shelters that income immediately, which is a real and valuable outcome. If this is your only passive investment and the rest of your income is earned, the loss suspends on Form 8582 and carries forward.</p>
<p>Real estate professional status does not usually rescue an LP either, because REPS still requires material participation in the activity, and a passive LP interest generally fails that test. Our post on <a href="/blog/passive-activity-loss-rules-cost-segregation/">passive activity loss rules and cost segregation</a> covers the framework in full.</p>"""),
            ("Cash Distributions Versus Taxable Loss",
             """<p>A source of confusion for new LPs is receiving a distribution check and a loss on the same K-1. Both are correct and they measure different things.</p>
<p>Distributions are cash. Taxable income or loss is an accounting result after depreciation. A property can generate positive cash flow and a substantial taxable loss simultaneously, precisely because depreciation is a non-cash deduction. That is the core appeal of real estate as an asset class.</p>
<p>What the distribution does affect is your basis. Distributions reduce your outside basis in the partnership interest, and your ability to deduct losses is limited by that basis under IRC Section 704(d), by the at-risk rules under Section 465, and only then by the passive loss rules under Section 469. Those three limitations apply in sequence. An LP whose basis has been reduced by distributions and prior losses may find losses limited before the passive rules are even reached.</p>"""),
            ("What Happens at Exit",
             """<p>Suspended passive losses are released when you dispose of your entire interest in the activity in a fully taxable transaction to an unrelated party. When the syndication sells the property and winds up, that is generally the triggering event.</p>
<p>At that point the accumulated suspended losses become fully deductible against any income, and they offset the gain recognized on the sale. The gain itself includes depreciation recapture: Section 1245 recapture on the personal property taxed at ordinary rates, and unrecaptured Section 1250 gain on the real property and land improvements taxed at up to 25 percent.</p>
<p>The net effect for a typical LP is that the year-one loss is a deferral rather than a permanent benefit, and the deferral is settled at exit. That is still valuable. Deferring tax for five to seven years is worth real money. But it is different from the permanent savings the pitch sometimes implies.</p>
<p>One important caveat: if the sponsor executes a 1031 exchange into a replacement property rather than selling outright, that is not a fully taxable disposition. Your suspended losses stay suspended and the gain stays deferred. Our post on <a href="/blog/cost-segregation-1031-exchanges/">cost segregation and 1031 exchanges</a> explains the interaction.</p>"""),
            ("Questions Worth Asking Before You Invest",
             """<p>A few questions materially affect how the tax benefit lands for you. Does the operating agreement allocate depreciation pro rata, or does the sponsor take a disproportionate share? Is there a special allocation that shifts losses toward certain partners? Does the deal use leverage in a way that affects your at-risk amount, particularly whether the debt is qualified nonrecourse financing?</p>
<p>And most importantly for your own planning: do you have passive income to absorb the loss, or will it suspend? An investor with a portfolio of income-producing passive investments gets immediate value. An investor with a salary and one syndication gets a deferred benefit.</p>
<p>These are worth reviewing with a tax advisor before committing capital rather than discovering the answer at filing. AE Tax Advisors works with syndication investors on K-1 analysis and passive loss planning through their <a href="{AE}/tax-planning-for-high-net-worth-individuals-with-complex-partnership-and-k1-income/" target="_blank" rel="noopener">partnership and K-1 income planning</a> and <a href="{AE}/passive-activity-loss-rules-real-estate/" target="_blank" rel="noopener">passive activity loss</a> resources.</p>"""),
            ("For Sponsors Commissioning a Study",
             """<p>Stratum performs engineering-based cost segregation studies for syndication sponsors and fund managers, delivering the component detail and documentation needed for K-1 reporting and for investor communications.</p>
<p>Request a free estimate or book a call to discuss your acquisition.</p>"""),
        ],
        "related": [
            ("passive-activity-loss-rules-cost-segregation", "Passive Activity Loss Rules and Cost Segregation"),
            ("cost-segregation-student-housing", "Cost Segregation for Student Housing"),
            ("depreciation-recapture-cost-segregation", "Depreciation Recapture and Cost Segregation"),
        ],
    },
]
