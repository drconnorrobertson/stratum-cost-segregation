#!/usr/bin/env python3
"""Additional sections inserted before the closing section of specific posts.

Each entry is slug -> (heading, html). Used to bring posts to full depth.
"""

EXTRA_SECTIONS = {
    "cost-segregation-office-buildings": (
        "What Depresses an Office Reclassification Percentage",
        """<p>Not every office building performs well, and it is worth knowing the factors that pull the number down before you commission a study.</p>
<p>A high land allocation is the biggest one. If the appraisal or assessor's ratio assigns 35 percent of the purchase price to land, your depreciable basis shrinks before the analysis even begins. Urban infill assets are frequently in this position, and there is nothing a study can do about it.</p>
<p>Structured parking is the second. When parking is a concrete deck integrated into the building rather than an asphalt lot, it is generally a structural component on the building's recovery period rather than a 15-year land improvement. That single distinction can move an office property from 26 percent reclassification to 15 percent.</p>
<p>Older buildings acquired with no recent buildout are the third. If the suites were last renovated in 1998, there is not much cabling, decorative lighting, or specialty electrical left to identify. A shell purchase with a plan to renovate is a better candidate than a fully leased building nobody has touched in twenty years, because the renovation spend itself becomes the study.</p>""",
    ),
    "cost-segregation-medical-office-buildings": (
        "Watch the Line Between Building Systems and Equipment",
        """<p>Medical office studies attract more scrutiny than most, because the classifications are more aggressive and the dollar amounts per square foot are higher. The distinction that matters most is between a system that serves the building and one that serves specific equipment.</p>
<p>The main electrical service, the general HVAC serving the suite, the base plumbing, and the fire protection system are structural components on the building's recovery period, however clinical the building is. What reclassifies is the branch that runs to a particular machine: the dedicated feeder to the MRI, the medical gas line to a specific outlet, the supplemental condenser installed for the imaging room.</p>
<p>Studies that sweep entire mechanical and electrical systems into the 5-year bucket because the building is a medical facility are exactly the fact pattern the IRS Cost Segregation Audit Techniques Guide warns examiners about. A defensible report traces each run, states what it serves, and cites the authority for the classification.</p>
<p>This is also why photographs and mechanical drawings matter in the deliverable. When a study is examined years later, the documentation is the argument.</p>""",
    ),
    "cost-segregation-restaurants": (
        "Buying an Existing Restaurant Versus Building One",
        """<p>The two paths into a restaurant produce different studies, and it is worth knowing which one you are on.</p>
<p>If you are building out a space, the contractor's schedule of values already itemizes the work by trade. Kitchen equipment arrives on invoices. The mechanical and electrical subcontractor bids break out the specialty gas, dedicated circuits, and hood systems separately. A study performed against actual cost data is more precise and less expensive than one reconstructed later, and the detailed engineering method it supports is the approach the IRS treats as most reliable.</p>
<p>If you are buying an existing restaurant as a going concern, the analysis starts with the purchase price allocation. Part of what you paid may be goodwill, a liquor license, or a covenant not to compete, all of which are Section 197 intangibles amortized over 15 years and not eligible for bonus depreciation. Part may be equipment. Only the remainder is real property subject to a cost segregation analysis.</p>
<p>Getting that allocation right at closing, ideally documented in the purchase agreement, prevents a fight later and determines how much basis the study has to work with.</p>""",
    ),
    "cost-segregation-hotels": (
        "Where the Land Allocation Decides the Outcome",
        """<p>Hotel studies live or die on two inputs, and neither is the component analysis.</p>
<p>The first is the land allocation. Resort and urban hotels frequently sit on extremely valuable land, and land is never depreciable. A property purchased for $12,000,000 where the land is genuinely worth $4,000,000 has a much smaller depreciable basis than the headline price suggests. That allocation should be supported by an appraisal that separately values land or by comparable land sales, not by a convenient percentage.</p>
<p>The second is the allocation to intangibles and going-concern value. When you buy an operating hotel you are buying a business as well as a building: the franchise agreement, the assembled workforce, the reservation system, and the goodwill. Those are Section 197 intangibles amortized over 15 years, not depreciable real property, and they are not eligible for bonus depreciation.</p>
<p>Studies that ignore both questions and simply apply a reclassification percentage to the full purchase price produce numbers that do not survive examination. A defensible hotel study starts by establishing what portion of the price is actually depreciable real property, then segregates within it.</p>""",
    ),
    "cost-segregation-assisted-living-facilities": (
        "Going Concern Value in a Facility Acquisition",
        """<p>Senior housing is rarely bought as an empty building. You are typically acquiring a licensed, occupied, staffed operation, and the purchase price reflects that.</p>
<p>That means a meaningful portion of what you paid may be allocable to intangibles rather than to depreciable real property: the operating licenses and certificates of need, the resident contracts and in-place census, the assembled workforce, and goodwill. Those are Section 197 intangibles amortized over 15 years and not eligible for bonus depreciation.</p>
<p>Allocating too little to intangibles inflates the depreciable basis and every downstream figure in the study. Allocating too much needlessly reduces the deduction. Neither is a judgment a cost segregation engineer should make alone, and it is worth resolving with a valuation professional and your tax advisor, ideally with the allocation documented in the purchase agreement under Section 1060.</p>
<p>A quality study states clearly what basis it is working from and how that figure was derived. If a provider quotes you a first-year deduction based on the full purchase price of an operating senior housing facility without asking about intangibles, that is a signal to slow down.</p>""",
    ),
    "cost-segregation-dental-practices": (
        "Tenants Should Confirm Who Owns the Improvements",
        """<p>Most dental practices lease their space, and lease terms determine who gets the depreciation. This is worth confirming before you assume a study is available to you.</p>
<p>If you paid for the buildout, the improvements are your asset and you depreciate them, even though they are physically attached to someone else's building. If the landlord paid and provided the space finished, the landlord owns and depreciates them, and you have nothing to segregate.</p>
<p>Tenant improvement allowances sit in between and are the most commonly misunderstood arrangement. When a landlord provides a TI allowance, the general rule is that the party who bears the economic cost and holds the benefits and burdens of ownership depreciates the improvements. An allowance that simply reimburses you for work you contracted and paid for is often treated as landlord property, while an allowance structured as a rent concession may leave the improvements with you. The lease language controls.</p>
<p>Get this answered before commissioning a study. It is a five-minute question for your attorney or CPA and it determines whether the entire exercise is worth running.</p>""",
    ),
    "cost-segregation-veterinary-clinics": (
        "Cost Segregation Does Not Cover Practice Goodwill",
        """<p>Veterinary practices trade frequently, and much of that activity is corporate consolidators acquiring independent hospitals. If you bought a practice rather than building one, understanding what a study can and cannot reach saves disappointment.</p>
<p>A practice acquisition allocates the purchase price across several categories under Section 1060: equipment, leasehold improvements or real property, and intangibles including goodwill, the client list, and any non-compete. Goodwill and the other Section 197 intangibles amortize over 15 years and are not eligible for bonus depreciation. A cost segregation study cannot change that.</p>
<p>What a study reaches is the real property and improvement component. If you acquired the building along with the practice, that basis is fully in scope. If you acquired only the practice and lease the building, the study covers the leasehold improvements you own.</p>
<p>The practical implication is that the allocation negotiated at closing determines how much a study has to work with. Buyers generally prefer more basis in short-lived assets and less in goodwill. That is a negotiation to have with the seller and your advisors before signing, not after.</p>""",
    ),
    "cost-segregation-fitness-centers-gyms": (
        "Confirm the Lease Before You Commission the Study",
        """<p>Because most fitness operators are tenants, the threshold question is who actually owns the improvements. The answer is in the lease, and it determines whether a study is worth running at all.</p>
<p>If you funded the buildout directly, the improvements are your depreciable asset. If the landlord delivered a finished space, they are the landlord's. Where a tenant improvement allowance is involved, the treatment depends on which party bears the economic burden and holds the benefits and burdens of ownership, which turns on how the allowance is structured in the lease.</p>
<p>Lease term matters for a second reason. If your improvements have a shorter useful life than the recovery period assigned to them, you do not get to depreciate them over the lease term instead. The MACRS recovery period governs regardless of how long you plan to stay. What does happen is that if you abandon the improvements at lease end, the remaining undepreciated basis is generally deductible as a loss in that year.</p>
<p>Both points are worth confirming with your CPA before engaging a study provider.</p>""",
    ),
    "cost-segregation-rv-parks-campgrounds": (
        "Cabins, Park Models, and How They Are Titled",
        """<p>Many parks add cabins, yurts, or park model units to capture higher nightly rates, and how those units are classified is one of the more consequential judgments in a campground study.</p>
<p>A permanently affixed cabin on a foundation, connected to utilities and not designed to be moved, is generally a building. Whether it is residential rental property at 27.5 years or nonresidential at 39 years depends on the average period of guest use, which in a transient park is usually short enough to land it in the nonresidential category.</p>
<p>A park model or RV that retains its wheels and title, sits on a pad, and can be relocated is a different asset entirely. Units that remain titled as vehicles and are not permanently affixed are frequently treated as tangible personal property with a much shorter recovery period, which is a substantially better outcome.</p>
<p>The distinction turns on the same permanence analysis that governs everywhere else in cost segregation: how it is attached, whether it was designed to be moved, and how difficult removal actually is. Because the classification swings the recovery period from 39 years to 5 or 7, it deserves specific documentation in the report rather than a blanket assumption.</p>""",
    ),
    "cost-segregation-student-housing": (
        "Watch the Residential Classification Test",
        """<p>Student housing is normally residential rental property at 27.5 years, but the classification is not automatic and it is worth confirming rather than assuming.</p>
<p>Under IRC Section 168(e)(2)(A), a building is residential rental property if 80 percent or more of its gross rental income comes from dwelling units. Most purpose-built student properties clear that easily. Where it gets interesting is on mixed-use assets with ground-floor retail, structured parking leased separately, or substantial commercial space. If commercial income pushes the dwelling unit share below 80 percent, the entire building is nonresidential real property at 39 years.</p>
<p>The test is applied annually, which means a property near the threshold can shift classification as the retail component leases up or empties out. That is an unusual and unwelcome dynamic, and it is worth modeling on any student asset with a meaningful commercial component.</p>
<p>Separately, parking that is leased to non-residents for a separate fee can raise questions about whether it is part of the residential activity at all. On mixed-use student properties these determinations should be documented in the study rather than assumed from the property type.</p>""",
    ),
    "cost-segregation-auto-dealerships": (
        "Sequencing a Study Around LIFO and Floorplan Interest",
        """<p>Dealership returns have moving parts that most real estate owners do not deal with, and they affect how much of a large depreciation deduction actually lands.</p>
<p>Dealers using LIFO inventory accounting carry a reserve that can swing taxable income substantially year to year depending on inventory levels and vehicle costs. A year with a large LIFO recapture is a year with a lot of income to absorb accelerated depreciation. A year with a LIFO benefit may already have low taxable income, in which case a large deduction produces a net operating loss rather than a current-year tax reduction.</p>
<p>Floorplan interest adds a second consideration. Floorplan financing interest is generally exempt from the business interest limitation under Section 163(j), but electing that treatment has a consequence: a dealer whose floorplan interest is excepted from the limitation is not permitted to claim bonus depreciation. That is a direct trade-off between two significant benefits and it has to be modeled, not assumed.</p>
<p>This is the single most important reason dealers should coordinate a cost segregation study with their tax advisor before the year closes rather than discovering the interaction at filing.</p>""",
    ),
    "cost-segregation-manufacturing-facilities": (
        "The New Qualified Production Property Opportunity",
        """<p>Manufacturers building new domestic capacity have an additional provision worth evaluating alongside a conventional study.</p>
<p>The One Big Beautiful Bill Act created a category of qualified production property that permits full expensing of certain nonresidential real property used in domestic manufacturing or production. Unlike bonus depreciation, which reaches only property with a recovery period of 20 years or less, this provision reaches the building itself, which would otherwise sit on a 39-year schedule.</p>
<p>The provision comes with specific conditions on when construction begins and when the property is placed in service, and it applies to the portion of the property used in a qualified production activity rather than to office or unrelated space. Those boundaries matter, and a facility with mixed use requires an allocation.</p>
<p>For a manufacturer weighing a new plant, this can change the analysis considerably, because it addresses the one category a conventional cost segregation study cannot accelerate. It does not replace a study, since the study is still what identifies process equipment and land improvements. The two work together, and both should be scoped before construction rather than after.</p>""",
    ),
    "cost-segregation-daycare-centers": (
        "Franchise Buildouts and Multi-Site Operators",
        """<p>A large share of the childcare market is franchised, and franchise operators have both an advantage and a complication when it comes to cost segregation.</p>
<p>The advantage is repeatability. Franchise prototypes are standardized, which means the component mix at one center closely resembles the next. An operator who runs a detailed study on the first location can apply the same methodology across subsequent builds at substantially lower cost per site, since the engineering analysis does not start from zero each time.</p>
<p>The complication is the purchase price allocation on a franchise acquisition. Franchise fees, the franchise agreement itself, and any goodwill acquired when buying an existing center are Section 197 intangibles amortized over 15 years without bonus eligibility. Only the real property and improvement component is in scope for a study.</p>
<p>Operators opening several centers over a few years should also model the excess business loss limitation under Section 461(l), which caps how much business loss an individual can apply against non-business income annually. Front-loading three buildouts into one tax year can generate more deduction than the limitation permits you to use, with the excess carried forward as a net operating loss.</p>""",
    ),
}
