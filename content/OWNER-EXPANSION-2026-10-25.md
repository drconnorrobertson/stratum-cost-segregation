# Rental owner content expansion

Explicit human request on October 24: implement the proposed expansion, with direct-to-consumer rental-home owners as the primary audience. This release is the specific requested expansion; it does not change any portfolio-wide recurring publishing schedule or authorize subsequent automatic volume expansion.

## Delivered scope

- 25 new canonical destinations under `/rental-owner-guide/`: one hub, eight owner decision guides, six fictional worked examples, six CPA resources, and four interactive tools.
- Six downloadable blank CSV templates.
- Substantive improvements on 25 retained destinations: 11 discovery/resource/property pages, six commercial guides, four provider comparisons and four market guides.
- Owner-guide links in shared footers; source manifest reports exact coverage.
- Sitemap entries for new pages and modified dates for the 25 substantively revised pages. Existing generator baselines remain unchanged; expansion runs as the final content pass.
- Vercel Analytics custom events for completed tool interactions, exports and the new discovery CTA. Events contain resource path and tool name, never entered financial values or property labels. Existing analytics availability/account settings determine whether events appear in the dashboard. No signed-study or revenue attribution is claimed.

## Editorial boundaries

No verified client report or outcome data was available in this task workspace. The six examples explicitly identify all inputs as fictional and distinguish additional depreciation from usable tax reduction. They include zero-usability and negative-economics discussion. Actual client case studies and actual redacted reports require verified source files and appropriate permission before replacing these illustrations.

The fee-benefit worksheet is an undiscounted early-period calculation using user/adviser inputs. It does not assign component percentages or determine bonus eligibility, passive-loss treatment, state results, future deductions or sale-year consequences. Portfolio groups indicate record/preparer readiness, not eligibility or tax-benefit ranking. The readiness checklist does not collect documents or transmit entries. Browser refresh clears inputs; CSV export preserves a user-selected local copy.

The four provider additions use their official service pages, checked October 25, 2026. R.E. product starting fees are distinguished from property-specific quotes. No superiority, rating or review count is invented. Market sections link official county/state resources and distinguish assessment data from federal tax basis. California guidance is identified as 2025 instructions, requiring applicable-year and entity review.

## Source references

- https://www.irs.gov/publications/p527
- https://www.irs.gov/publications/p925
- https://www.irs.gov/publications/p551
- https://www.irs.gov/publications/p946
- https://www.irs.gov/publications/p544
- https://www.irs.gov/forms-pubs/about-form-3115
- https://www.irs.gov/pub/irs-pdf/p5653.pdf (examination guidance, not law)
- https://www.senecacostseg.com/help/
- https://www.recostseg.com/services
- https://www.kbkg.com/costsegregation
- https://www.mavencostseg.com/our-services/detailed-engineering-cost-segregation-studies/
- https://www.ftb.ca.gov/forms/2025/2025-3885a-instructions.html
- https://realestate.alleghenycounty.us/search
- https://assessment.cot.tn.gov/
- https://www.sdarcc.gov/

## Rebuild and verification

`python3 content/build_owner_growth.py` regenerates the curated JSON source. `node topical-depth-build.cjs` builds the full public tree and validates the expansion and retained site rules. `node scripts/brand-check.mjs public` is the Vercel build's final brand guard.

`scripts/validate-owner-growth.cjs` verifies arithmetic against all six examples, the per-property minimum, zero rate/usability, invalid inputs, workflow classification, tailored checklist behavior, canonical uniqueness, page IDs, structured data, links/fragments/assets, example disclosures and template CSVs.

Browser verification: all 25 new pages at 390px and 1280px, plus all 25 substantively revised pages at 390px. No horizontal overflow. Interactive calculator, zero-usability branch, portfolio totals/groups, tailored checklist, report accordion and three generated CSV downloads exercised. Evidence is saved under `outputs/`.

## Measurement

Compare settled Search Console periods for the new owner-page cohort separately from the competitor cohort. Use qualified discovery calls and signed engagements from actual booking/CRM records to evaluate business impact. Do not equate custom-event totals with booked calls or signed studies. Existing indexing and ranking monitoring remains separate; this release does not reset its accepted-request ledger or bypass quota.
