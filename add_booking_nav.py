#!/usr/bin/env python3
"""Add the Book a Call nav link and footer link to every existing page.

Idempotent: pages that already have the links are skipped.
"""

import os
import re

ROOT = os.path.dirname(os.path.abspath(__file__))

# <a href="../contact/index.html">Contact</a>  ->  same + Book a Call
NAV_RE = re.compile(r'(<a href="((?:\.\./)*)contact/index\.html">Contact</a>)')
# footer contact list item -> insert Book a Call above it.
# Older posts use "Contact" here rather than "Contact Us".
FOOTER_RE = re.compile(r'(<li><a href="((?:\.\./)*)contact/index\.html">Contact(?: Us)?</a></li>)')


def main():
    nav_changed = footer_changed = skipped = 0

    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in (".git", "__pycache__")]
        if "index.html" not in filenames:
            continue
        path = os.path.join(dirpath, "index.html")
        with open(path, encoding="utf-8") as f:
            html = f.read()

        original = html

        if 'booking/index.html">Book a Call</a>' not in html:
            def nav_sub(m):
                return f'{m.group(1)}\n      <a href="{m.group(2)}booking/index.html">Book a Call</a>'
            html, n = NAV_RE.subn(nav_sub, html, count=1)
            if n:
                nav_changed += 1

        if 'booking/index.html">Book a Call</a></li>' not in html:
            def footer_sub(m):
                return (f'<li><a href="{m.group(2)}booking/index.html">Book a Call</a></li>\n'
                        f'        {m.group(1)}')
            html, n = FOOTER_RE.subn(footer_sub, html, count=1)
            if n:
                footer_changed += 1

        if html != original:
            with open(path, "w", encoding="utf-8") as f:
                f.write(html)
        else:
            skipped += 1

    print(f"nav links added:    {nav_changed}")
    print(f"footer links added: {footer_changed}")
    print(f"unchanged:          {skipped}")


if __name__ == "__main__":
    main()
