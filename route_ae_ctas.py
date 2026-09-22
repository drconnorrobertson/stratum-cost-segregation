#!/usr/bin/env python3
"""Route Stratum's consultation CTAs to AE's verified discovery page.

Run after any of the site's content generators. The transformation is
idempotent so regenerated static pages can be prepared for deployment.
"""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
AE_BOOKING = (
    "https://www.aetaxadvisors.com/discovery/"
    "?utm_source=stratumcostsegregation.com"
    "&amp;utm_medium=referral&amp;utm_campaign=cost_segregation"
)


def update_anchor(match: re.Match[str]) -> str:
    opening, label, closing = match.groups()
    href = re.search(r'href="([^"]+)"', opening)
    if not href or not re.search(r'(?:^|/)(?:booking|free-estimate)/index\.html$', href.group(1)):
        return match.group(0)

    opening = opening.replace(href.group(0), f'href="{AE_BOOKING}"')
    if re.search(r'Free Estimate|free written estimate|Get Started', label, re.I):
        label = "Book a Free AE Tax Advisors Call &rarr;" if 'class="btn' in opening or 'nav-cta' in opening else "Book with AE Tax Advisors"
    elif re.search(r'Book a Call|Schedule', label, re.I):
        label = "Book with AE Tax Advisors" if 'class="btn' not in opening else "Book a Call with AE Tax Advisors &rarr;"
    return opening + label + closing


def main() -> None:
    changed = 0
    for path in ROOT.rglob("*.html"):
        if ".git" in path.parts:
            continue
        html = path.read_text(encoding="utf-8")
        updated = re.sub(r'(<a\b[^>]*>)(.*?)(</a>)', update_anchor, html, flags=re.S | re.I)
        if updated != html:
            path.write_text(updated, encoding="utf-8")
            changed += 1
    print(f"Routed consultation CTAs on {changed} pages")


if __name__ == "__main__":
    main()
