#!/usr/bin/env python3
"""Batch A: commercial property-type long-tail posts."""

AE = "https://aetaxadvisors.com"

POSTS_A = [
    {
        "slug": "cost-segregation-apartment-buildings",
        "title": "Cost Segregation for Apartment Buildings: What Multifamily Owners Recover in Year One",
        "description": "Apartment buildings typically reclassify 20 to 30 percent of depreciable basis through cost segregation. Learn which multifamily components qualify and what a 48-unit property yields in year one.",
        "date": "August 2026",
        "iso_date": "2026-08-09",
        "sections": [
            ("Why Apartment Buildings Are Strong Cost Segregation Candidates",
             """<p>Apartment buildings sit in an unusual sweet spot for cost segregation. They are classified as residential rental property, which means the building shell depreciates over 27.5 years rather than the 39 years applied to commercial real estate. That shorter baseline is already favorable. What makes multifamily compelling is the sheer density of qualifying assets packed into the property.</p>
<p>Every unit contains its own appliance package, cabinetry, countertops, flooring, window treatments, and plumbing fixtures. Multiply that by 24, 48, or 200 units and the personal property component grows fast. Add the site work that surrounds nearly every apartment complex -- parking lots, sidewalks, site lighting, landscaping, fencing, signage, and often a pool or clubhouse -- and you have two large categories of short-lived assets that the default depreciation schedule buries inside a single 27.5-year line item.</p>
<p>In practice, engineering-based studies on apartment properties reclassify 20 to 30 percent of depreciable basis into 5-year, 7-year, and 15-year categories. Garden-style complexes with extensive surface parking and amenity areas land at the higher end. Mid-rise and high-rise buildings with structured parking and less site work tend to land closer to 15 to 22 percent.</p>"""),
            ("What Gets Reclassified in a Multifamily Property",
             """<p>The 5-year bucket under IRC Section 1245 captures assets that are personal property rather than structural components. In an apartment building that means refrigerators, ranges, dishwashers, microwaves, and in-unit washers and dryers. It also captures carpet and vinyl plank flooring, decorative lighting, window blinds, cabinetry and countertops that are not permanently affixed as part of the building structure, appliances and equipment in the common laundry room, and fitness equipment in the amenity center.</p>
<p>Specialty electrical and plumbing that serves specific equipment rather than the building as a whole also moves to 5-year treatment. Dedicated circuits for kitchen appliances, the rough-in serving a common-area kitchen, and wiring for security and access control systems are common examples.</p>
<p>The 15-year land improvement bucket is often where the largest single dollar figure appears on a garden-style property. Asphalt and concrete paving, striping, curbs, sidewalks, retaining walls, site utilities running from the property line to the building, exterior site lighting and its underground conduit, fencing and gates, dumpster enclosures, playgrounds, pools and pool decking, and irrigation and landscaping all belong here. On a suburban complex, land improvements alone frequently represent 10 to 15 percent of total basis.</p>"""),
            ("A 48-Unit Example",
             """<p>Consider a 48-unit garden-style apartment complex purchased for $6,200,000. After allocating $900,000 to land, the depreciable basis is $5,300,000. Under the default schedule the owner deducts $192,727 per year for 27.5 years.</p>
<p>A cost segregation study on this property identifies $742,000 of 5-year personal property (roughly 14 percent) and $689,000 of 15-year land improvements (roughly 13 percent), for total reclassification of $1,431,000, or 27 percent of basis. The remaining $3,869,000 stays on the 27.5-year schedule.</p>
<p>With 100 percent bonus depreciation available on the reclassified 5-year and 15-year property, the first-year deduction becomes $1,431,000 of bonus depreciation plus roughly $140,700 of depreciation on the remaining shell, for a total near $1,571,700. That is more than eight times the $192,727 the owner would otherwise have claimed. For a taxpayer facing a combined 40 percent marginal rate, the additional $1,378,000 of first-year deduction represents roughly $551,000 of deferred tax, assuming the owner has income the loss can offset.</p>"""),
            ("The Passive Loss Question Multifamily Owners Have to Answer",
             """<p>Generating a large deduction and being able to use it are two different problems. Apartment buildings almost never qualify for the short-term rental exception, because average tenant stay is measured in months or years rather than the seven days or fewer that exception requires. That means the activity is a rental activity under IRC Section 469 and the losses are passive by default.</p>
<p>Passive losses offset passive income. If you own other profitable rentals, a syndication throwing off K-1 income, or another passive business interest, the accelerated depreciation from your apartment building can shelter that income immediately. If your income is primarily W-2 wages or active business profit, the loss suspends and carries forward until you have passive income or you dispose of the property in a fully taxable sale.</p>
<p>The exception is <a href="/blog/real-estate-professional-status-cost-segregation/">real estate professional status</a>. An owner who spends more than 750 hours in real property trades or businesses, spends more than half of total working time in those activities, and materially participates in the rental can treat the losses as non-passive. For a full-time multifamily operator this is often achievable. For a physician or executive buying an apartment building as a side investment, it usually is not. AE Tax Advisors covers the mechanics in depth in their guide to <a href="{AE}/passive-activity-loss-rules-real-estate/" target="_blank" rel="noopener">passive activity loss rules for real estate</a>.</p>"""),
            ("Timing, Look-Backs, and Value-Add Renovations",
             """<p>The ideal time to order a study is the year the property is placed in service. If you bought the building two or five years ago and have been depreciating it straight-line the entire time, you have not lost the benefit. A look-back study paired with <a href="/blog/form-3115-look-back-cost-segregation/">IRS Form 3115</a> lets you claim the entire cumulative missed depreciation as a Section 481(a) adjustment in the current year. No amended returns are required, and there is no limit on how far back the study can reach.</p>
<p>Value-add multifamily operators have a second opportunity that is frequently missed. When you gut a unit and replace flooring, cabinets, appliances, and fixtures, the components you removed still sit on your depreciation schedule. A <a href="/blog/partial-asset-disposition-cost-segregation/">partial asset disposition election</a> lets you write off the remaining basis of what you tore out, rather than continuing to depreciate assets that are in a dumpster. Combined with a study on the renovation spend, this materially improves the after-tax return on a repositioning.</p>"""),
            ("Getting a Number for Your Property",
             """<p>Stratum performs engineering-based cost segregation studies on multifamily properties nationwide, following the methodology set out in the IRS Cost Segregation Audit Techniques Guide. Every study includes a component-level asset listing, photographic documentation, the cost basis allocation supporting each classification, and the depreciation schedules your CPA needs to file.</p>
<p>If you own or are under contract on an apartment building, request a free estimate or book a call. We will tell you the likely reclassification percentage for your property type and market, and we will tell you plainly if the numbers do not justify a study.</p>"""),
        ],
        "related": [
            ("cost-segregation-duplexes-multifamily", "Cost Segregation for Duplexes and Small Multifamily"),
            ("real-estate-professional-status-cost-segregation", "Real Estate Professional Status and Cost Segregation"),
            ("partial-asset-disposition-cost-segregation", "Partial Asset Disposition and Cost Segregation"),
        ],
    },
    {
        "slug": "cost-segregation-retail-properties",
        "title": "Cost Segregation for Retail Properties: Strip Centers, Shopping Centers, and Standalone Stores",
        "description": "Retail properties reclassify 20 to 35 percent of basis through cost segregation, driven by parking, site work, and tenant improvements. See what qualifies and how a $3.5M strip center performs.",
        "date": "August 2026",
        "iso_date": "2026-08-09",
        "sections": [
            ("Retail Real Estate and the 39-Year Default",
             """<p>Retail buildings are nonresidential real property, which puts the shell on a 39-year straight-line schedule. On a $3,000,000 depreciable basis that produces $76,923 of annual depreciation. Spread across four decades, it is one of the slowest cost recovery periods in the tax code.</p>
<p>What the default schedule ignores is that a retail property is not one asset. It is a building shell surrounded by an unusually large amount of site work and filled with tenant-specific improvements that have nothing like a 39-year economic life. A cost segregation study separates those components and assigns each the recovery period the tax code actually provides for it.</p>
<p>Retail is one of the better performing asset classes in cost segregation precisely because of the parking. A strip center or shopping center devotes far more of its site to paved surface, lighting, and landscaping than an office tower or a warehouse does. Those are 15-year land improvements, and on a suburban retail property they routinely account for 12 to 20 percent of total depreciable basis on their own.</p>"""),
            ("Components That Reclassify in a Retail Property",
             """<p>The 15-year land improvement category typically dominates. It includes asphalt and concrete paving, parking lot striping and wheel stops, curbs and gutters, sidewalks, pylon and monument sign foundations, parking lot light poles and their underground conduit, landscaping and irrigation, retaining walls, fencing, and site drainage and detention infrastructure.</p>
<p>The 5-year bucket captures decorative and tenant-specific items: display lighting and track lighting, decorative millwork and storefront finishes, carpeting and vinyl flooring, signage that is not structurally integrated, security and surveillance systems, sound systems, and the specialty electrical and plumbing that serves specific tenant equipment rather than the building generally. A dedicated 220-volt circuit for a tenant's equipment is 5-year property. The panel serving the entire building is not.</p>
<p>Then there is qualified improvement property. Interior nonstructural improvements made to a nonresidential building after it was first placed in service are QIP, which carries a 15-year recovery period and is bonus eligible. For a landlord who regularly builds out tenant spaces, <a href="/blog/qualified-improvement-property-cost-segregation/">QIP treatment</a> is one of the most valuable and most frequently missed classifications in retail. It excludes building enlargements, elevators and escalators, and internal structural framework.</p>"""),
            ("A $3.5 Million Strip Center",
             """<p>Take a 22,000 square foot neighborhood strip center acquired for $3,500,000, with $600,000 allocated to land. Depreciable basis is $2,900,000, producing $74,359 per year under the standard 39-year schedule.</p>
<p>An engineering-based study on this property identifies $261,000 of 5-year personal property (9 percent) and $551,000 of 15-year land improvements (19 percent). Total reclassification is $812,000, or 28 percent of basis. The remaining $2,088,000 continues over 39 years.</p>
<p>With 100 percent bonus depreciation on the reclassified property, the first-year deduction is $812,000 plus roughly $53,500 on the remaining shell, for a total of about $865,500. Against the $74,359 the owner would otherwise deduct, that is an additional $791,000 of first-year deduction. At a 37 percent federal marginal rate, that is roughly $293,000 of tax deferred into future years.</p>"""),
            ("Triple-Net Leases and the Investor Who Never Visits",
             """<p>A large share of retail is held under triple-net leases, where the tenant pays taxes, insurance, and maintenance. Owners sometimes assume that because they have no operational involvement, cost segregation is not relevant to them. The opposite is true. The landlord still owns the building and still claims the depreciation, and the study is a paper exercise that requires nothing operationally.</p>
<p>The real constraint for NNN investors is the same one that affects most commercial owners: the passive activity rules. NNN retail income is passive, and the accelerated loss from a study is a passive loss. That works perfectly if you hold a portfolio of income-producing properties, because the loss from the new acquisition shelters income from the others. It works less well if this is your only real estate and your other income is a salary. We cover the interaction in detail in our post on <a href="/blog/cost-segregation-triple-net-nnn-properties/">cost segregation for triple-net lease properties</a>.</p>
<p>Investors weighing whether a study fits their broader tax picture should coordinate with a planning-focused advisor. AE Tax Advisors works with commercial owners on exactly this question in their <a href="{AE}/real-estate-investor-tax-planning/" target="_blank" rel="noopener">real estate investor tax planning</a> practice.</p>"""),
            ("Tenant Turnover Creates a Second Opportunity",
             """<p>Retail turns over. When a tenant vacates and you demolish the old build-out to deliver a white box for the next one, the improvements you removed are still being depreciated on your books. A partial asset disposition election lets you deduct the remaining basis of the demolished components in the year of removal, and it also lets you deduct the removal costs rather than capitalizing them.</p>
<p>Without a cost segregation study you generally cannot make this election, because you have no basis figures for the individual components. The study is what makes the disposition deduction possible. For a landlord who re-tenants space every few years, this compounds into a meaningful recurring benefit that most retail owners never claim.</p>"""),
            ("Next Steps for Retail Owners",
             """<p>If you own a strip center, shopping center, standalone retail building, or a portfolio of net-leased stores, a cost segregation study is likely to produce a first-year deduction several times larger than your current schedule. Stratum delivers audit-ready, engineering-based studies with full component detail and the documentation your CPA needs to implement the results.</p>
<p>Request a free estimate with your purchase price and placed-in-service date, or book a call and we will size the opportunity on the phone.</p>"""),
        ],
        "related": [
            ("cost-segregation-triple-net-nnn-properties", "Cost Segregation for Triple-Net (NNN) Lease Properties"),
            ("qualified-improvement-property-cost-segregation", "Qualified Improvement Property and Cost Segregation"),
            ("partial-asset-disposition-cost-segregation", "Partial Asset Disposition and Cost Segregation"),
        ],
    },
    {
        "slug": "cost-segregation-office-buildings",
        "title": "Cost Segregation for Office Buildings: Reclassifying Cabling, Buildouts, and Site Work",
        "description": "Office buildings reclassify 15 to 28 percent of depreciable basis through cost segregation. Learn which components qualify, how QIP applies to tenant buildouts, and what a $5M office asset yields.",
        "date": "August 2026",
        "iso_date": "2026-08-09",
        "sections": [
            ("The Case for Cost Segregation in Office",
             """<p>Office buildings depreciate over 39 years as nonresidential real property. On the surface an office building looks like a poor cost segregation candidate compared with a restaurant or a car wash, because so much of the value sits in the structure itself: the frame, the envelope, the core, the elevators, and the base building systems.</p>
<p>That intuition is only half right. Office properties do carry a lower reclassification percentage than equipment-heavy asset classes, typically landing between 15 and 28 percent. But office deals are large. Fifteen percent of a $12,000,000 basis is $1,800,000 of accelerated deduction, which dwarfs the absolute dollars available on a small property with a flashier percentage. The percentage matters less than the dollars.</p>
<p>Suburban office properties with surface parking outperform urban assets substantially, because parking lots, site lighting, and landscaping are 15-year land improvements. A single-story suburban office park can reach 25 to 30 percent reclassification. A downtown tower with structured parking integrated into the building typically lands in the mid-teens.</p>"""),
            ("What Qualifies Inside an Office Building",
             """<p>Structured cabling is the classic office example. The low-voltage data and telecommunications cabling running through the building serves the tenants' equipment rather than the operation of the building, and it is treated as 5-year personal property. In a modern office building this can be a substantial number on its own.</p>
<p>Other 5-year items include decorative lighting and accent fixtures, carpeting and modular flooring, demountable partitions and systems furniture, window treatments, kitchen and break room appliances and cabinetry, audiovisual and conference room systems, access control and security systems, and the dedicated electrical serving server rooms, supplemental cooling units, and tenant-specific equipment.</p>
<p>The 15-year land improvement category picks up paving, parking striping, curbs, sidewalks, exterior site lighting and conduit, monument signage foundations, landscaping and irrigation, fencing, and stormwater detention. On a suburban campus these frequently exceed the 5-year total.</p>
<p>Tenant improvements deserve separate attention. Interior nonstructural work performed after the building was placed in service is qualified improvement property, recovered over 15 years and eligible for bonus depreciation. Landlords who build out suites regularly and simply capitalize the cost to the building are leaving a 15-year classification on the table in favor of a 39-year one.</p>"""),
            ("A $5 Million Suburban Office Example",
             """<p>Consider a 40,000 square foot two-story suburban office building purchased for $5,000,000. Land is allocated at $750,000, leaving a depreciable basis of $4,250,000. The default 39-year schedule yields $108,974 per year.</p>
<p>A study identifies $382,500 of 5-year property (9 percent, driven largely by cabling, finishes, and dedicated electrical) and $722,500 of 15-year land improvements (17 percent, driven by the surface lot and site work). Total reclassification is $1,105,000, or 26 percent.</p>
<p>Applying 100 percent bonus depreciation to the reclassified property produces a first-year deduction of $1,105,000 plus roughly $80,600 on the remaining $3,145,000 shell, for a total near $1,185,600. That is $1,076,600 more than the standard schedule allows, worth approximately $398,000 in deferred federal tax at a 37 percent rate.</p>"""),
            ("Owner-Occupants Have a Different and Often Better Position",
             """<p>Many office buildings are owned by the business that occupies them, frequently through a separate LLC that leases the space back to the operating company. This structure changes the analysis in the owner's favor.</p>
<p>When a self-rental arrangement produces income, that income is generally recharacterized as non-passive under the self-rental rule. More importantly, an owner who materially participates in the operating business and has structured the arrangement appropriately may be able to use the depreciation against active business income rather than having it suspend as a passive loss. The grouping election under Regulation 1.469-4 is often the mechanism, and it needs to be made deliberately and documented.</p>
<p>This is genuinely technical ground and it is worth planning before you close rather than after. AE Tax Advisors addresses the entity and grouping questions for owner-occupants in their <a href="{AE}/business-owner-cost-segregation/" target="_blank" rel="noopener">business owner cost segregation</a> and <a href="{AE}/real-estate-entity-structuring-for-rental-portfolios/" target="_blank" rel="noopener">real estate entity structuring</a> resources.</p>"""),
            ("Renovation Cycles and Disposition Deductions",
             """<p>Office buildings renovate constantly. Every time a tenant leaves and you demolish the old build-out, you are throwing away assets that remain on your depreciation schedule. A partial asset disposition election lets you write off the undepreciated basis of the removed components and deduct the demolition cost, rather than carrying phantom assets for another three decades.</p>
<p>The election requires component-level basis, which is exactly what a cost segregation study produces. Owners who run a study once and then maintain the asset detail through subsequent renovations capture value on every turnover, not just at acquisition.</p>"""),
            ("Sizing the Opportunity",
             """<p>Office assets vary widely, and the honest answer for any specific building depends on its parking, its age, its buildout history, and how much of the purchase price the appraisal assigns to land. Stratum performs engineering-based studies on office properties nationwide and will give you a realistic range before you commit.</p>
<p>Send us the purchase price, square footage, and placed-in-service date through our free estimate form, or book a call to talk through it directly.</p>"""),
        ],
        "related": [
            ("qualified-improvement-property-cost-segregation", "Qualified Improvement Property and Cost Segregation"),
            ("residential-vs-commercial-cost-segregation", "Residential vs. Commercial Cost Segregation"),
            ("partial-asset-disposition-cost-segregation", "Partial Asset Disposition and Cost Segregation"),
        ],
    },
    {
        "slug": "cost-segregation-medical-office-buildings",
        "title": "Cost Segregation for Medical Office Buildings: Specialty Systems That Qualify as 5-Year Property",
        "description": "Medical office buildings reclassify 25 to 35 percent of basis thanks to medical gas, lead shielding, and dedicated electrical. See what qualifies and what a $4M MOB yields in year one.",
        "date": "August 2026",
        "iso_date": "2026-08-09",
        "sections": [
            ("Why Medical Office Outperforms Standard Office",
             """<p>A medical office building looks like an office building from the parking lot. Inside, it is a substantially different asset for depreciation purposes. Clinical space is dense with specialty systems installed to serve specific equipment, and under the tax code, building systems that serve particular equipment rather than the building as a whole are Section 1245 personal property rather than structural components.</p>
<p>That distinction is worth real money. Standard office properties typically reclassify 15 to 28 percent of depreciable basis. Medical office buildings routinely reach 25 to 35 percent, and imaging-heavy or surgical facilities can exceed that. The difference is entirely in the specialty infrastructure.</p>
<p>Medical office remains nonresidential real property on a 39-year schedule by default, so the gap between what the standard schedule delivers and what a study delivers is unusually wide in this asset class.</p>"""),
            ("The Specialty Components That Drive the Number",
             """<p>Medical gas systems are the signature MOB component. Oxygen, nitrous oxide, medical air, and vacuum lines, along with the manifolds, alarms, and outlets they feed, serve clinical equipment rather than the building, and qualify as 5-year property.</p>
<p>Lead shielding in radiology and imaging suites is another. Lead-lined walls, doors, and viewing windows exist solely to support the imaging equipment and are classified with it. The dedicated high-amperage electrical service running to an MRI, CT, or X-ray suite follows the same logic, as does the supplemental cooling installed specifically to keep imaging equipment within its operating temperature range.</p>
<p>Beyond the marquee items, MOBs carry heavy amounts of ordinary 5-year property: casework and cabinetry in exam rooms, sinks and plumbing serving specific clinical fixtures, nurse call systems, sterilization and autoclave utility connections, exam lighting, vinyl and specialty flooring, millwork at reception, data cabling, and security and access control.</p>
<p>Site work contributes the 15-year layer: patient parking, ambulance and drop-off aprons, sidewalks, site lighting, signage foundations, and landscaping. Medical office generally parks at a higher ratio than general office, which helps.</p>"""),
            ("A $4 Million Medical Office Example",
             """<p>Take a 16,000 square foot multi-tenant medical office building purchased for $4,000,000, with $500,000 allocated to land. Depreciable basis is $3,500,000, producing $89,744 per year on the standard 39-year schedule.</p>
<p>An engineering-based study identifies $665,000 of 5-year property (19 percent, reflecting the clinical infrastructure across several suites) and $437,500 of 15-year land improvements (12.5 percent). Total reclassification is $1,102,500, or 31.5 percent of basis.</p>
<p>With 100 percent bonus depreciation, the first-year deduction is $1,102,500 plus approximately $61,500 on the remaining $2,397,500 shell, totaling roughly $1,164,000. Compared to the $89,744 standard deduction, the owner picks up an additional $1,074,000 in year one. At a combined 40 percent marginal rate that is roughly $430,000 of tax deferred.</p>"""),
            ("Practice Owners Who Own Their Building",
             """<p>A large portion of medical office is owned by the physicians or physician groups who practice there, typically through a real estate LLC that leases to the practice entity. For these owners the analysis is more favorable than for a passive MOB investor.</p>
<p>Rental income from a self-rental to a business in which you materially participate is recharacterized as non-passive under Regulation 1.469-2(f)(6). With a properly considered grouping election, the accelerated depreciation may be usable against practice income rather than suspending as a passive loss. That turns a paper deduction into a current-year tax reduction for the physician owner.</p>
<p>The structure needs to be set up correctly and the election documented contemporaneously, which is a planning exercise rather than a filing exercise. AE Tax Advisors works with practice owners on this specific fact pattern through their <a href="{AE}/physician-cost-segregation/" target="_blank" rel="noopener">physician cost segregation</a> and <a href="{AE}/tax-planning-for-doctors/" target="_blank" rel="noopener">physician tax planning</a> services.</p>"""),
            ("Buildouts, Look-Backs, and Suite Turnover",
             """<p>Medical suites are expensive to build and are rebuilt when a tenant changes specialty. Interior nonstructural buildout performed after the building was placed in service is qualified improvement property, recovered over 15 years and bonus eligible, rather than being buried in the 39-year shell. Landlords who capitalize buildouts to the building without segregating QIP are systematically over-lengthening their recovery period.</p>
<p>If you already own the building and have been depreciating it straight-line, a <a href="/blog/form-3115-look-back-cost-segregation/">look-back study filed with Form 3115</a> recovers every dollar of missed acceleration in the current tax year through a Section 481(a) adjustment. There is no amended return and no lookback limit. Practices that bought their building in 2019 or 2015 and never ran a study are usually the largest single opportunities we see in this asset class.</p>"""),
            ("Getting a Study Scoped",
             """<p>Stratum performs engineering-based cost segregation studies on medical office buildings, ambulatory surgery centers, imaging centers, and clinical space nationwide. Our reports document each specialty system, the basis assigned to it, and the authority supporting its classification, so the position holds up under examination.</p>
<p>Request a free estimate or book a call with your building details and we will give you a realistic reclassification range for your property.</p>"""),
        ],
        "related": [
            ("cost-segregation-dental-practices", "Cost Segregation for Dental Practices"),
            ("cost-segregation-office-buildings", "Cost Segregation for Office Buildings"),
            ("qualified-improvement-property-cost-segregation", "Qualified Improvement Property and Cost Segregation"),
        ],
    },
    {
        "slug": "cost-segregation-restaurants",
        "title": "Cost Segregation for Restaurants: Why Food Service Properties Reclassify 30 to 40 Percent",
        "description": "Restaurants are among the strongest cost segregation candidates, with 30 to 40 percent of basis reclassifying into 5-year and 15-year property. See what qualifies and what a $2.2M build yields.",
        "date": "August 2026",
        "iso_date": "2026-08-09",
        "sections": [
            ("Restaurants Are Built Almost Entirely Out of Short-Lived Assets",
             """<p>Few property types reclassify as heavily as restaurants. The reason is structural: a restaurant is a modest building shell wrapped around an enormous amount of equipment, specialty utility infrastructure, and decorative finish work, all of which has a real economic life far shorter than 39 years.</p>
<p>Think about what actually sits inside the four walls. Commercial kitchen equipment, walk-in coolers and freezers, exhaust hoods and their make-up air systems, grease interceptors, dedicated gas and water lines running to specific appliances, high-amperage circuits serving individual equipment, decorative lighting, booth seating and millwork, bar equipment, and point-of-sale infrastructure. Almost none of that is a structural component of the building.</p>
<p>Engineering-based studies on restaurant properties commonly reclassify 30 to 40 percent of depreciable basis into 5-year, 7-year, and 15-year categories. Quick-service restaurants with drive-throughs, extensive paving, and menu board infrastructure can push past 40 percent.</p>"""),
            ("What Reclassifies in a Restaurant",
             """<p>The 5-year bucket is unusually large. It captures kitchen equipment and appliances, walk-in refrigeration boxes and their compressors, exhaust hood systems and fire suppression serving cooking equipment, the dedicated gas piping and electrical running to specific appliances, specialty plumbing serving prep sinks and dish stations, decorative and accent lighting, booth and banquette seating, bar millwork and back-bar equipment, sound and audiovisual systems, decorative wall and ceiling treatments, signage, and point-of-sale wiring.</p>
<p>A key principle governs most of these calls. A gas line serving the building is a structural component on a 39-year life. A gas line branching off to serve a specific range or fryer is 5-year property because it serves the equipment, not the building. The same reasoning applies to electrical, water, and ventilation. This is why an engineering-based study, which traces utilities to their endpoints, produces dramatically better results than a rule-of-thumb allocation.</p>
<p>The 15-year layer picks up parking and drive-through paving, striping, curbs, sidewalks and patio hardscape, site lighting, menu board and pylon sign foundations, landscaping and irrigation, fencing, and outdoor dining infrastructure.</p>"""),
            ("A $2.2 Million Restaurant Example",
             """<p>Consider a freestanding 4,800 square foot casual dining restaurant, purchased with the land and equipment in place for $2,200,000. Land is allocated at $400,000, leaving a depreciable basis of $1,800,000. On the standard 39-year schedule that produces $46,154 per year.</p>
<p>A study identifies $468,000 of 5-year property (26 percent) and $270,000 of 15-year land improvements (15 percent). Total reclassification is $738,000, or 41 percent of basis. The remaining $1,062,000 stays on the 39-year schedule.</p>
<p>With 100 percent bonus depreciation applied to the reclassified property, the first-year deduction is $738,000 plus roughly $27,200 on the shell, totaling about $765,200. That is $719,000 more than the standard schedule delivers. For an owner at a 37 percent federal rate, roughly $266,000 of federal tax is deferred out of year one.</p>"""),
            ("Restaurant Operators Who Own Their Real Estate",
             """<p>Restaurant owners frequently hold the real estate in a separate entity and lease it to the operating company. This is good practice for liability and estate reasons, and it also matters for depreciation.</p>
<p>Because the operator materially participates in the restaurant business, a properly structured and documented arrangement can allow the accelerated depreciation to reduce active business income rather than suspending as a passive loss. The self-rental rules and the grouping election under Regulation 1.469-4 are the relevant machinery. Getting this right requires deliberate planning with a tax advisor before the structure is locked in.</p>
<p>There is also a distinction worth flagging: if you purchased an existing restaurant as a going concern, part of the purchase price may be allocable to goodwill or an assembled workforce, which is a 15-year Section 197 intangible rather than depreciable real property. A proper purchase price allocation is a prerequisite to a defensible study. AE Tax Advisors covers the broader planning picture for operating businesses in their <a href="{AE}/business-owner-cost-segregation/" target="_blank" rel="noopener">business owner cost segregation</a> resource.</p>"""),
            ("Remodels, Refreshes, and Disposition Elections",
             """<p>Restaurants remodel on a cycle. Brand refreshes, concept conversions, and equipment replacement happen every five to seven years in most operations. Each of those events is a depreciation opportunity that most owners miss twice over.</p>
<p>First, interior nonstructural remodel work in a nonresidential building placed in service earlier is qualified improvement property, recovered over 15 years and bonus eligible, not 39-year building. Second, the fixtures and finishes you tear out are still on your depreciation schedule. A partial asset disposition election writes off their remaining basis and lets you deduct the removal cost rather than capitalizing it.</p>
<p>Both require component-level basis detail. A cost segregation study at acquisition or at build-out is what makes the later elections available.</p>"""),
            ("Getting an Estimate",
             """<p>Whether you own a single freestanding location, a portfolio of franchised units, or the real estate under a tenant-operated concept, restaurant properties are among the highest-yield cost segregation candidates in commercial real estate. Stratum delivers engineering-based studies with full component detail and IRS-compliant documentation.</p>
<p>Request a free estimate or book a call and we will size the first-year deduction for your property.</p>"""),
        ],
        "related": [
            ("cost-segregation-hotels", "Cost Segregation for Hotels"),
            ("qualified-improvement-property-cost-segregation", "Qualified Improvement Property and Cost Segregation"),
            ("components-reclassified-cost-segregation", "What Components Get Reclassified in a Cost Segregation Study"),
        ],
    },
    {
        "slug": "cost-segregation-hotels",
        "title": "Cost Segregation for Hotels: FF&E, Guest Rooms, and Amenity Space",
        "description": "Hotels reclassify 25 to 40 percent of depreciable basis through cost segregation, driven by FF&E and guest room finishes. Learn what qualifies and what a $12M select-service hotel yields.",
        "date": "August 2026",
        "iso_date": "2026-08-09",
        "sections": [
            ("Hotels Carry More Personal Property Than Almost Any Real Estate Asset",
             """<p>A hotel is a real estate asset wrapped around an operating business, and the operating business requires an enormous quantity of furniture, fixtures, and equipment. Every guest room contains beds, case goods, seating, lamps, televisions, artwork, window treatments, carpet, and a bathroom package. Multiply by 120 rooms and the personal property component alone becomes a very large number.</p>
<p>Add the public spaces and the number grows further. Lobby furnishings, front desk millwork, restaurant and bar equipment, fitness center equipment, pool and spa systems, meeting room audiovisual and partitions, laundry equipment, and back-of-house kitchen infrastructure are all short-lived assets sitting inside a building that the default schedule depreciates over 39 years.</p>
<p>Engineering-based studies on hotels commonly reclassify 25 to 40 percent of depreciable basis. Full-service and resort properties with extensive amenity space, surface parking, and site work land at the high end. Limited-service properties on small urban sites land lower but still comfortably in the mid-twenties.</p>"""),
            ("What Reclassifies in a Hotel",
             """<p>The 5-year and 7-year buckets capture guest room furniture and case goods, mattresses and bedding, televisions and in-room technology, decorative and task lighting, carpet and resilient flooring, window treatments, bathroom accessories and vanities that are not structural, lobby and public area furnishings, restaurant and bar equipment, kitchen equipment and walk-in refrigeration, fitness equipment, laundry equipment, property management and point-of-sale systems, data and telecommunications cabling, and security and access control including electronic door lock systems.</p>
<p>Specialty utility infrastructure follows the same rule that governs other property types. Electrical and plumbing that serves specific equipment -- the dedicated service to the laundry, the pool equipment room, the kitchen line -- is personal property. The service that runs the building is structural.</p>
<p>The 15-year land improvement layer includes parking and drive lanes, porte-cochere paving, sidewalks and pool decking, site lighting, signage foundations, landscaping and irrigation, fencing, and outdoor amenity hardscape. Suburban and resort hotels with large surface lots see meaningful value here.</p>"""),
            ("A $12 Million Select-Service Hotel",
             """<p>Consider a 118-room select-service hotel purchased for $12,000,000. Land is allocated at $1,200,000, leaving $10,800,000 of depreciable basis. The default 39-year schedule produces $276,923 per year.</p>
<p>An engineering-based study identifies $2,376,000 of 5-year and 7-year property (22 percent, driven by the guest room FF&E packages and public space furnishings) and $972,000 of 15-year land improvements (9 percent). Total reclassification is $3,348,000, or 31 percent of basis.</p>
<p>With 100 percent bonus depreciation on the reclassified property, the first-year deduction is $3,348,000 plus roughly $191,000 on the remaining $7,452,000 shell, totaling about $3,539,000. Against the $276,923 the standard schedule delivers, the owner picks up $3,262,000 in additional first-year deduction. At a 37 percent marginal rate that is approximately $1,207,000 of federal tax deferred.</p>"""),
            ("The Material Participation Question for Hotel Owners",
             """<p>Hotels occupy interesting ground under the passive activity rules. Because the average guest stay is measured in days, a hotel is not a rental activity under Regulation 1.469-1T(e)(3)(ii)(A). It is a trade or business. That removes the automatic passive classification that applies to apartment buildings and long-term rentals.</p>
<p>What remains is the material participation test. If the owner materially participates in the hotel operation -- meeting one of the seven tests in Regulation 1.469-5T, most commonly the 500-hour test or the 100-hour-and-more-than-anyone-else test -- the losses are non-passive and can offset active income including W-2 wages and business profit.</p>
<p>The practical complication is that most hotels are run by third-party management companies, and an owner who has delegated operations may struggle to meet any participation test. Owner-operators are in a materially better position than passive equity holders. This is the same analytical framework that governs the <a href="/blog/cost-segregation-str-tax-loophole/">short-term rental strategy</a>, applied at institutional scale. AE Tax Advisors discusses documenting participation in their guide to <a href="{AE}/material-participation-real-estate-documentation/" target="_blank" rel="noopener">material participation documentation</a>.</p>"""),
            ("PIP Cycles and Ongoing Deductions",
             """<p>Franchised hotels operate under property improvement plans that mandate periodic renovation of guest rooms, public space, and building systems. A PIP is a large capital event, and how it is classified determines whether the spend recovers over 5 years or 39.</p>
<p>Replacement FF&E is 5-year or 7-year property and bonus eligible. Interior nonstructural improvements to the building are qualified improvement property at 15 years, also bonus eligible. And the FF&E and finishes being replaced are still on the depreciation schedule, which makes a partial asset disposition election available to write off their remaining basis.</p>
<p>Hotels that run a cost segregation study at acquisition and maintain component detail through each PIP cycle capture value repeatedly. Those that capitalize each renovation to the building as a lump sum do not.</p>"""),
            ("Scoping a Hotel Study",
             """<p>Stratum performs engineering-based cost segregation studies on hotels, resorts, and extended-stay properties nationwide, following IRS Cost Segregation Audit Techniques Guide methodology. Reports include a component-level asset listing, photographic support, and the depreciation schedules your CPA and asset manager need.</p>
<p>Request a free estimate or book a call to discuss your property.</p>"""),
        ],
        "related": [
            ("cost-segregation-restaurants", "Cost Segregation for Restaurants"),
            ("cost-segregation-str-tax-loophole", "The Short-Term Rental Tax Loophole"),
            ("cost-segregation-vacation-rentals", "Cost Segregation for Vacation Rentals"),
        ],
    },
    {
        "slug": "cost-segregation-car-washes",
        "title": "Cost Segregation for Car Washes: One of the Highest Reclassification Rates in Real Estate",
        "description": "Car washes reclassify 40 to 60 percent of depreciable basis through cost segregation, driven by wash equipment, water reclamation, and site work. See what qualifies and what a $4M express tunnel yields.",
        "date": "August 2026",
        "iso_date": "2026-08-09",
        "sections": [
            ("Why Car Washes Reclassify So Heavily",
             """<p>Car washes produce some of the highest reclassification percentages in cost segregation, frequently landing between 40 and 60 percent of depreciable basis. The reason is simple: a car wash is a piece of industrial equipment with a building around it, and most of the capital cost is in the equipment and the site rather than in the structure.</p>
<p>An express tunnel wash contains conveyor systems, wraps and brushes, dryers, chemical dosing and delivery systems, water reclamation and filtration, high-pressure pumps, vacuum stations, pay stations and gate arms, tunnel controllers, and licence plate recognition systems. None of that is a structural component of a building. All of it is Section 1245 personal property on a 5-year or 7-year recovery period.</p>
<p>Then there is the site. Car washes sit on heavily improved lots: stacking lanes, vacuum bays, paving, striping, canopies, site lighting, signage, and substantial underground utility and drainage work. Those are 15-year land improvements. Between equipment and site work, the 39-year building shell often accounts for less than half the total cost.</p>"""),
            ("What Qualifies as Short-Lived Property",
             """<p>The 5-year and 7-year categories capture the entire wash package: conveyor and correlator, brushes, wraps, and mitters, the arch and applicator systems, blowers and dryers, high-pressure pump stations, chemical storage, mixing, and delivery equipment, water softening, reclamation, and filtration systems, vacuum systems including the producer units and hose drops, pay stations, kiosks, and gate arms, tunnel control systems and sensors, point-of-sale and membership management systems, and security cameras and license plate recognition.</p>
<p>Critically, the utility infrastructure serving that equipment follows the equipment. The dedicated electrical feeding the pump room, the water lines serving the wash arches, the compressed air distribution, and the trench drains and process piping tied to reclamation all serve the equipment rather than the building. An engineering-based study traces these to their endpoints, which is where a great deal of the value is found.</p>
<p>The 15-year layer includes concrete and asphalt paving in the stacking lanes and vacuum area, curbing and islands, vacuum canopies and their foundations, site lighting and conduit, pylon and directional signage foundations, landscaping and irrigation, fencing, and stormwater detention and site drainage.</p>"""),
            ("A $4 Million Express Tunnel Example",
             """<p>Consider a newly constructed express tunnel car wash with a total project cost of $4,000,000, including $700,000 for the land. Depreciable basis is $3,300,000. On the default 39-year nonresidential schedule that produces $84,615 per year.</p>
<p>An engineering-based study identifies $1,254,000 of 5-year and 7-year equipment (38 percent) and $693,000 of 15-year land improvements (21 percent). Total reclassification is $1,947,000, or 59 percent of basis. Only $1,353,000 remains on the 39-year schedule.</p>
<p>With 100 percent bonus depreciation on the reclassified property, the first-year deduction is $1,947,000 plus roughly $34,700 on the shell, totaling about $1,981,700. That is $1,897,000 more than the standard schedule. At a 37 percent federal marginal rate the owner defers roughly $702,000 of federal tax out of year one.</p>"""),
            ("Recapture Deserves Real Attention in This Asset Class",
             """<p>When reclassification is this aggressive, the recapture conversation matters more than it does elsewhere. Section 1245 property is subject to full ordinary income recapture on sale, to the extent of depreciation claimed. Section 1250 real property gets the more favorable unrecaptured gain treatment capped at 25 percent.</p>
<p>On a car wash where 38 percent of basis went into 1245 property and was fully expensed in year one, a sale five years later can produce a substantial ordinary income recapture event. That does not make the strategy wrong. Deferring tax for five years at a 37 percent rate and paying it back at ordinary rates later is still valuable because of the time value of money, and many owners will be in a different bracket or will structure an exit differently by then.</p>
<p>But it should be modeled, not assumed away. Our post on <a href="/blog/depreciation-recapture-cost-segregation/">depreciation recapture and cost segregation</a> walks through the mechanics, and a <a href="/blog/cost-segregation-1031-exchanges/">1031 exchange</a> can defer the entire event if the exit is planned in advance. AE Tax Advisors covers the exchange rules in their <a href="{AE}/1031-exchange-guide/" target="_blank" rel="noopener">1031 exchange guide</a>.</p>"""),
            ("Owner-Operators and Multi-Site Developers",
             """<p>Car washes are usually owner-operated, which is helpful. An owner who materially participates in the business is not subject to the passive activity limitation on the resulting loss, so the deduction can offset active business income directly rather than suspending.</p>
<p>Developers building multiple sites have an additional consideration. Because construction costs are known at the component level from the outset, a study performed contemporaneously with construction is cheaper and more precise than one reconstructed years later. Operators building a pipeline of sites often engage a study provider once and roll the methodology across each location, which reduces per-site cost substantially.</p>"""),
            ("Getting Started",
             """<p>If you own, are building, or are acquiring a car wash, this is one of the few asset classes where cost segregation is close to a default decision rather than a judgment call. Stratum performs engineering-based studies on express tunnels, in-bay automatics, self-serve sites, and multi-site portfolios.</p>
<p>Request a free estimate or book a call and we will size the reclassification for your specific build.</p>"""),
        ],
        "related": [
            ("cost-segregation-gas-stations-convenience-stores", "Cost Segregation for Gas Stations and Convenience Stores"),
            ("depreciation-recapture-cost-segregation", "Depreciation Recapture and Cost Segregation"),
            ("cost-segregation-new-construction", "Cost Segregation for New Construction"),
        ],
    },
    {
        "slug": "cost-segregation-gas-stations-convenience-stores",
        "title": "Cost Segregation for Gas Stations and Convenience Stores: The 15-Year Retail Motor Fuels Rule",
        "description": "Gas stations can depreciate the entire building over 15 years under the retail motor fuels outlet rule. Learn the three-part test, what else reclassifies, and what a $3M site yields in year one.",
        "date": "August 2026",
        "iso_date": "2026-08-09",
        "sections": [
            ("A Special Rule That Changes the Entire Calculation",
             """<p>Most commercial buildings depreciate over 39 years. Gas stations and convenience stores may not have to. Under IRC Section 168(e)(3)(E)(iii), a qualifying retail motor fuels outlet is 15-year property, and that applies to the building itself, not just to the site improvements.</p>
<p>This is one of the most valuable and least understood provisions available to a specific property type. Instead of recovering the store building over 39 years, a qualifying owner recovers it over 15 years. And because 15-year property is bonus depreciation eligible, a qualifying building can be substantially expensed in the first year rather than depreciated over four decades.</p>
<p>The rule does not apply automatically. The property has to meet one of three alternative tests, and documenting which test is met is part of what a defensible study delivers.</p>"""),
            ("The Three-Part Test for Retail Motor Fuels Outlet Treatment",
             """<p>A building qualifies as a retail motor fuels outlet if it meets any one of the following. First, 50 percent or more of the gross revenue generated at the property comes from petroleum sales. Second, 50 percent or more of the floor space at the property is devoted to petroleum marketing sales. Third, the building is 1,400 square feet or less.</p>
<p>The third test is the cleanest and is why small kiosk-style stations qualify without analysis. The first test is the one that most modern convenience stores turn on, and it is where the analysis gets interesting. A high-volume fuel site with a modest food offering typically clears the 50 percent revenue threshold easily. A large travel center where the store, quick-service restaurant, and merchandise sales dominate revenue may not.</p>
<p>Because the revenue mix can shift over time and the classification is determined when the property is placed in service, contemporaneous documentation matters. A study that asserts 15-year treatment without supporting the test it relies on is exactly the kind of position that does not survive examination.</p>"""),
            ("What Reclassifies Beyond the Building",
             """<p>Whether or not the building qualifies for 15-year treatment, a great deal of a fuel site reclassifies. The 5-year and 7-year categories capture dispensers and pumps, underground and above-ground storage tanks and their piping, leak detection and monitoring systems, vapor recovery equipment, canopy lighting and the dispenser electrical, point-of-sale and fuel management systems, walk-in coolers and freezers, food service equipment, shelving and display fixtures, coffee and beverage equipment, security and surveillance systems, and car wash equipment where a wash is present on site.</p>
<p>The 15-year land improvement layer includes the fuel canopy and its supporting columns and foundations, concrete islands and paving, the tank field excavation and backfill, striping and bollards, site lighting, pylon and price signage foundations, landscaping, and site drainage.</p>
<p>Between the tank and dispenser systems, the canopy, and the site work, fuel sites routinely reclassify 45 to 70 percent of depreciable basis. When the building itself also qualifies for 15-year treatment, the effective recovery period for the entire property becomes remarkably short.</p>"""),
            ("A $3 Million Fuel and Convenience Site",
             """<p>Consider a fuel and convenience site with total acquisition cost of $3,000,000, of which $600,000 is land. Depreciable basis is $2,400,000. On a standard 39-year assumption the owner would deduct $61,538 per year.</p>
<p>An engineering-based study identifies $840,000 of 5-year and 7-year equipment (35 percent, driven by tanks, dispensers, and store equipment), $624,000 of 15-year land improvements (26 percent, driven by the canopy, islands, and paving), and determines that the 2,800 square foot store qualifies as a retail motor fuels outlet under the gross revenue test, moving the remaining $936,000 of building to a 15-year life.</p>
<p>With 100 percent bonus depreciation available on all 5-year, 7-year, and 15-year property, essentially the entire $2,400,000 depreciable basis is deductible in year one. Against $61,538 under the standard assumption, that is roughly $2,338,000 of additional first-year deduction, worth approximately $865,000 in deferred federal tax at a 37 percent rate.</p>"""),
            ("Environmental Costs, Tank Replacement, and Dispositions",
             """<p>Fuel sites carry capital events that other retail does not. Tank replacement, dispenser upgrades to meet EMV requirements, and canopy re-imaging all represent significant spend, and each is a classification decision.</p>
<p>Replaced tanks and dispensers are still sitting on the depreciation schedule when the new ones go in. A partial asset disposition election writes off the remaining basis of the removed assets and allows the removal costs to be deducted rather than capitalized. On a tank replacement running several hundred thousand dollars, this is not a rounding error.</p>
<p>Remediation costs are their own analysis. Costs to remediate contamination that existed when you acquired the property are generally capitalized, while costs to remediate contamination caused by your own operations may be currently deductible. This is fact-specific and worth reviewing with a tax advisor. AE Tax Advisors works with fuel and convenience operators through their <a href="{AE}/business-owner-cost-segregation/" target="_blank" rel="noopener">business owner cost segregation</a> practice.</p>"""),
            ("Getting a Study Scoped for Your Site",
             """<p>Gas stations and convenience stores are among the strongest cost segregation candidates available, and the retail motor fuels outlet rule makes them stronger still when the test is met and properly documented. Stratum performs engineering-based studies on single sites and multi-site portfolios, including the revenue and floor space analysis needed to support 15-year building treatment.</p>
<p>Request a free estimate or book a call with your site details.</p>"""),
        ],
        "related": [
            ("cost-segregation-car-washes", "Cost Segregation for Car Washes"),
            ("cost-segregation-retail-properties", "Cost Segregation for Retail Properties"),
            ("land-improvements-15-year-property-cost-segregation", "15-Year Land Improvements in a Cost Segregation Study"),
        ],
    },
    {
        "slug": "cost-segregation-self-storage-expansion",
        "title": "Cost Segregation for Self-Storage Expansions and Climate-Controlled Conversions",
        "description": "Self-storage expansions and climate-controlled conversions carry different cost segregation profiles than a stabilized acquisition. Learn how to treat new phases, conversions, and demolished components.",
        "date": "August 2026",
        "iso_date": "2026-08-09",
        "sections": [
            ("Expansion Is a Different Analysis Than Acquisition",
             """<p>Cost segregation on a stabilized self-storage acquisition is well understood, and we cover it in our post on <a href="/blog/cost-segregation-self-storage-facilities/">cost segregation for self-storage facilities</a>. What gets far less attention is what happens when you expand an existing facility, add a climate-controlled building, or convert a big-box retail shell into storage.</p>
<p>These are common value-add plays in the sector, and each one presents a depreciation profile different from a straightforward purchase. The distinction matters because expansion and conversion spend is new basis with a known component breakdown, which makes it both easier to segregate and easier to over-capitalize if nobody is paying attention.</p>
<p>Self-storage is nonresidential real property on a 39-year schedule by default. Stabilized acquisitions typically reclassify 20 to 35 percent. Expansions and conversions frequently do better, because the spend is concentrated in exactly the categories that reclassify.</p>"""),
            ("New Phase Construction",
             """<p>When you add buildings to an existing site, the construction budget is already broken out by trade, which is the ideal starting point for a study. Site work on a self-storage expansion is disproportionately large relative to the vertical construction: drive aisles, paving, perimeter fencing and gates, site lighting, security infrastructure, and drainage often account for 25 percent or more of the phase cost.</p>
<p>Those are 15-year land improvements almost in their entirety. The gate and access control system, the camera network, the individual door alarms, and the office and kiosk equipment are 5-year property. What remains on the 39-year schedule is the building shell itself: foundation, framing, roof, and envelope.</p>
<p>On a new phase where the vertical construction is a pre-engineered metal building and the site work is extensive, it is not unusual to see 35 to 45 percent of phase cost land outside the 39-year bucket. Running the study contemporaneously with construction, while the contractor pay applications and schedules of values are still current, produces a more precise and less expensive result than reconstructing it three years later.</p>"""),
            ("Climate-Controlled Conversions",
             """<p>Converting non-climate space to climate-controlled, or converting a vacant retail or industrial shell to storage, is where the classifications get more interesting.</p>
<p>The HVAC question is the central one. A system serving the building as a whole is a structural component on the building's recovery period. But supplemental units installed to serve specific climate-controlled areas, and the dedicated electrical running to them, are frequently classified as personal property when the engineering supports that they serve the storage function rather than the building. The distinction turns on facts, and it needs to be documented rather than asserted.</p>
<p>Beyond HVAC, a conversion generates substantial 5-year property: interior partition systems and roll-up doors where they are not structural, unit door alarms and individual unit access controls, lighting retrofits, the security and camera system, and office buildout finishes. Interior nonstructural work performed on a nonresidential building already placed in service is qualified improvement property at 15 years and bonus eligible, which is a materially better answer than capitalizing it to a 39-year building.</p>"""),
            ("The Demolition Deduction Owners Forget",
             """<p>Conversions destroy things. When you convert a retail shell, you demolish the storefront, the interior finishes, the old HVAC distribution, and the existing lighting. When you upgrade a climate-controlled building, you remove the old system.</p>
<p>Everything you removed is still on your depreciation schedule if you acquired the building as a single 39-year asset. A partial asset disposition election lets you deduct the remaining undepreciated basis of the removed components in the year of removal, and lets you deduct the removal cost rather than capitalizing it into the new work.</p>
<p>This election requires component-level basis, which is precisely what a cost segregation study at acquisition provides. Owners who buy a conversion candidate, run a study at acquisition, then run a second study on the conversion spend capture value at both ends. Owners who capitalize everything into one 39-year line item capture neither. Our post on <a href="/blog/partial-asset-disposition-cost-segregation/">partial asset disposition</a> explains the election mechanics.</p>"""),
            ("Sizing an Expansion Study",
             """<p>Consider a facility owner adding a 42,000 square foot climate-controlled phase at a total cost of $4,200,000, all of it depreciable improvements on land already owned. The standard 39-year assumption yields $107,692 per year.</p>
<p>A study identifies $504,000 of 5-year property (12 percent, driven by access control, alarms, security, and office equipment) and $1,092,000 of 15-year land improvements (26 percent, driven by paving, fencing, lighting, and drainage). Total reclassification is $1,596,000, or 38 percent.</p>
<p>With 100 percent bonus depreciation, the first-year deduction becomes $1,596,000 plus roughly $66,800 on the remaining shell, or about $1,662,800, against $107,692 under the default treatment. That is $1,555,000 of additional first-year deduction, roughly $575,000 of deferred federal tax at a 37 percent rate.</p>"""),
            ("Talk Through Your Phase Plan",
             """<p>If you are expanding, converting, or repositioning a self-storage asset, the best time to scope a study is before the work is complete, while cost detail is still readily available. Stratum performs engineering-based studies on self-storage acquisitions, expansions, and conversions nationwide.</p>
<p>Request a free estimate or book a call to walk through your phase plan and cost budget.</p>"""),
        ],
        "related": [
            ("cost-segregation-self-storage-facilities", "Cost Segregation for Self-Storage Facilities"),
            ("partial-asset-disposition-cost-segregation", "Partial Asset Disposition and Cost Segregation"),
            ("cost-segregation-new-construction", "Cost Segregation for New Construction"),
        ],
    },
]
