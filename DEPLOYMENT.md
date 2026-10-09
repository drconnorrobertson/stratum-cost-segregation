# Stratum production deployment and DNS

Verified October 9, 2026.

## One production source

- Repository: `drconnorrobertson/stratum-cost-segregation`
- Production branch: `main`
- Vercel project: `stratum-cost-segregation`
- Project ID: `prj_YCMGCpQ4rl4Xz7BvkmKSSsIy7ZdG`
- Team: `drconnorrobertsons-projects`
- Canonical website: https://www.stratumcostsegregation.com/

Use Vercel's existing Git integration. Push reviewed changes to main; Vercel builds and assigns the production domains. Do not create replacement projects, deploy from an unrelated checkout, or change DNS for routine releases. Preview branches must not receive production domains.

Build configuration is versioned in vercel.json: run `node topical-depth-build.cjs`, publish `public`, and retain trailing slashes. Generated public output is ignored by Git and rebuilt from source. To reproduce locally, use Node 24 and run the same command from the repository root.

## GoDaddy DNS

Domains are in BryceRobertson's GoDaddy account, accessible through Connor's existing delegated access.

| Zone | Type | Name | Value | TTL |
| --- | --- | --- | --- | --- |
| stratumcostsegregation.com | A | @ | 216.150.1.1 | 3600 |
| stratumcostsegregation.com | CNAME | www | 5e293b507ba4b433.vercel-dns-017.com | 3600 |
| stratumcostseg.com | A | @ | 216.150.1.1 | 600 |
| stratumcostseg.com | CNAME | www | 5e293b507ba4b433.vercel-dns-017.com | 3600 |

The apex values were updated to the recommendation shown in the authenticated Vercel domain dashboard on October 9, 2026. Both www records already matched the project and were retained. All four domain entries then showed Valid Configuration.

Keep GoDaddy nameservers: ns29/ns30.domaincontrol.com for stratumcostsegregation.com and ns35/ns36.domaincontrol.com for stratumcostseg.com. Preserve email, verification, payment and other unrelated records.

Do not point DNS at a single deployment URL. These DNS records route to Vercel's platform; the project chooses which production deployment is served. DNS and Git do not need a separate synchronization job.

In Vercel, www.stratumcostsegregation.com serves production. The other three custom domain names redirect with HTTP 308 to www.stratumcostsegregation.com. Handle web redirects in Vercel, not GoDaddy forwarding.

## Verify a release or investigate an outage

1. Compare GitHub main's SHA with the latest Vercel production deployment's source SHA.
2. Confirm deployment status is Ready, read build logs, and check for alias errors.
3. Confirm all four custom domains show Valid Configuration in the authenticated Vercel dashboard. Read the project-specific recommendation before modifying DNS.
4. Compare public DNS through independent DNS-over-HTTPS services and the affected computer's DNS path. Check A, CNAME and AAAA records.
5. Check HTTPS on the canonical site, apex redirect, companion-domain redirects, stylesheet, sitemap and booking page.
6. If the public Vercel site works but only one network resolves a different address, investigate that network's DNS override/filter/cache. Redeploying or changing correct public records will not repair that network issue.

On October 9, 2026, public Google and Cloudflare DNS-over-HTTPS returned Vercel addresses while the affected computer's normal DNS path returned 18.204.152.241 and refused HTTPS connections. The local DNS gateway was 192.168.40.1. The responsible network service was not identified or modified. Do not interpret a successful public DNS update as proof that this separate local issue is resolved.

If Vercel changes its recommended addresses in the future, confirm them in this same project's dashboard, update only the relevant website records, verify propagation, and revise this document. No DNS setting can guarantee immunity to future provider or network outages.
