# SEO content rollout — September 27, 2026

Primary commercial query: best cost segregation company. Use the existing /blog/how-to-choose-cost-segregation-company/ as the comparison destination, with contextual links from commercial pages and researched markets. Keep the STR-specific company guide as a supporting intent. Do not manufacture independent rankings, ratings, office locations, or client results.

This release rewrites 30 existing market pages and adds Palm Springs and Sevierville, adds six practical articles, a checklist planner, four blank CSV worksheets, and a searchable directory. There are 256 canonical pages, including 114 markets and 122 blog articles. Local sources support jurisdiction-specific planning context; IRS sources support technical references. Outbound links serve readers and substantiate information, not guaranteed ranking gains.

## Quality and remaining work

The five-word main-body similarity audit flags 77 older market pages after this release, down from 100. All 32 researched pages pass the internal editorial threshold. This is not a Google metric or a guarantee of indexing or compliance. See similarity-before.json and similarity-after.json for the exact backlog. A service footprint alone does not justify interchangeable city pages.

Before adding another batch, research a distinct property/ownership question, check the relevant official local source, record its date, write a meaningful example and records checklist, and link to appropriate service and topic pages. Populate markets-researched.json and run the build and validators. Consider consolidating overlapping markets only after reviewing search performance and user intent. Do not grow toward an arbitrary 250-location quota.

Next business evidence with highest value: a real redacted sample report, named and verified preparer/reviewer credentials, permissioned client case studies with methodology and limitations, and independently verifiable client feedback. These require actual business evidence; this release invents none.

Measure the national guide and market cohorts in Search Console: indexing, non-brand impressions, query mix, clicks, and qualified booking conversions. Search Console data was not available for this release. Prioritize remaining rewrites using that evidence. Google rankings are not guaranteed.

## Validation

Run python3 build_str_seo.py, python3 validate_str_seo.py, and python3 audit_content.py --output content/similarity-after.json. All 256 pages pass the HTML/navigation/sitemap validator. Repeat generation is stable. Both new scripts pass node --check. Browser checks cover planner selection/reset, market filtering and empty results, buyer-guide layout, and mobile overflow.

Google reference: https://developers.google.com/search/docs/essentials/spam-policies
