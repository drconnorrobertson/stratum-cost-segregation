# Stratum SEO release — September 27, 2026

Primary commercial intent: “best cost seg company” / “best cost segregation company.” The national buyer guide remains the main comparison destination, supported by the STR guide, commercial pages, practical resources and contextual market links. No independent ranking, local office, professional review or client result is invented.

## Released content

The site contains 256 canonical pages: 114 market guides, 122 blog articles and 20 other pages. This release rewrites the remaining 82 market guides, bringing all 114 into the sourced editorial dataset. Each has a distinct local planning question, scope discussion, records checklist, illustrative scenario and source references. Existing URLs remain intact.

Eight older articles receive complete targeted rewrites covering current and historical bonus depreciation, Notice 2026-11 records and construction components, recapture, section 179D timing, material participation and opportunity-fund coordination. Homepage, LTR service, services, pricing and FAQs receive accuracy and buyer-focused improvements. Other historic articles receive shared technical/navigation corrections; this release is not a professional tax review of every article.

## Technical changes

Canonical directory links and permanent legacy index.html redirects reduce URL ambiguity. Metadata and JSON-LD match visible content; undocumented reviewer attribution is removed. The sitemap includes meaningful editorial dates. Every page is reachable from the homepage. The blog has one accessible search and 122 unique article cards. Native FAQ disclosures, planning links, privacy and consultation links improve navigation.

Vercel packages only public pages and assets. Generators, editorial source data and audit files are excluded from deployment. The local release checks rebuild and validate committed output, navigation, schema, sitemap and JavaScript. The optional GitHub Actions template is saved as content/site-quality-workflow.yml.example; it is not installed because the existing GitHub token lacks workflow scope.

## Validation and maintenance

Run `python3 build_str_seo.py`, `python3 validate_str_seo.py`, `python3 audit_content.py --output content/similarity-after.json`, and `node build_static.mjs`. The validator covers all 256 canonical pages, assets, link fragments, unique metadata, schema, sitemap parity, homepage reachability, 122 blog cards and 114 complete sourced market records.

All market pages pass the internal five-word similarity threshold of 0.65; the remaining flagged-market backlog is zero. This is an editorial heuristic, not a Google metric or a guarantee of indexing or ranking. Serving a market alone does not justify an interchangeable city page. Add markets only when there is useful original local material; do not pursue an arbitrary page quota.

The most valuable next business evidence is an actual redacted sample report, verified preparer credentials and permissioned client case studies with documented results. Search Console access and search-performance data were unavailable. Measure indexing, nonbrand queries, qualified leads and the national comparison guide after launch; this work does not promise a particular ranking.

References: [Google spam policies](https://developers.google.com/search/docs/essentials/spam-policies), [helpful content guidance](https://developers.google.com/search/docs/fundamentals/creating-helpful-content), [IRS Publication 946](https://www.irs.gov/publications/p946), [Publication 925](https://www.irs.gov/publications/p925), [Publication 544](https://www.irs.gov/publications/p544). Individual articles and markets carry their relevant sources.
