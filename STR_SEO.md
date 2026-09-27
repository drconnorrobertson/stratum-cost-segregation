# STR search content expansion

Run `python3 build_str_seo.py` after the legacy site generators. It preserves existing URLs and regenerates the expansion, applies shared resource links, and rebuilds the sitemap. Run `python3 validate_str_seo.py` before deployment.

This release adds 12 service-area guides, 3 original buyer/preparation articles, a directory of all 112 market guides, and an STR resource center. It refreshes the homepage, blog metadata, STR service content and existing location search presentation. Other articles retain their specific subject and receive shared navigation to the STR resources; this is not a claim that every historic article received a technical tax review.

The STR service page replaces outdated bonus phase-down language and removes blanket recovery-period and deduction claims. New articles use an organizational byline without asserting an unperformed professional review. New market pages identify national service coverage rather than fictitious local offices; scenarios are illustrative rather than fabricated client results.

## Verification

The validator covers all 247 index pages: internal link destinations, one H1, descriptions, unique titles, self-canonicals, parseable JSON-LD and complete unique sitemap URLs. Re-running the builder produces identical HTML.

## Search follow-through

After production deployment, verify representative new URLs return 200 and inspect rendered pages on desktop/mobile. Submit the updated sitemap in the verified Search Console property. Establish a baseline for nonbrand impressions, qualified discovery calls, and market-page engagement. Search Console and keyword-volume data were not available during this change; no measured traffic, keyword difficulty, or ranking claims are made.

Use Search Console query data to prioritize the next location-specific improvements. The 112-market directory is a defined service-area footprint, not an exhaustive ranking of every U.S. STR market. Existing location bodies still share a common structure; add documented regional case studies and address-specific operating resources as they become available. Obtain actual client consent and supporting evidence before publishing results, testimonials, or savings examples.

Primary references consulted September 27, 2026:
- https://www.irs.gov/publications/p946
- https://www.irs.gov/publications/p925
- https://www.irs.gov/publications/p527
- https://developers.google.com/search/docs/essentials/spam-policies
