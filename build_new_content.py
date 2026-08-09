#!/usr/bin/env python3
"""Build the new Stratum blog posts, refresh the blog index, and rebuild the sitemap.

Idempotent: re-running regenerates the same output.
"""

import os
import re
import sys

from stratum_render import BASE_URL, write_post
from new_posts_a import POSTS_A
from new_posts_b import POSTS_B
from new_posts_c import POSTS_C
from extra_sections import EXTRA_SECTIONS

ROOT = os.path.dirname(os.path.abspath(__file__))
AE = "https://aetaxadvisors.com"

POSTS = POSTS_A + POSTS_B + POSTS_C


def expand(posts):
    """Insert extra sections, then substitute the {AE} token with the AE Tax base URL."""
    for p in posts:
        extra = EXTRA_SECTIONS.get(p["slug"])
        if extra and extra[0] not in [h for h, _ in p["sections"]]:
            # Insert just before the closing call-to-action section.
            p["sections"].insert(len(p["sections"]) - 1, extra)
        p["sections"] = [(h, b.replace("{AE}", AE)) for h, b in p["sections"]]
    return posts


def existing_blog_slugs():
    blog_dir = os.path.join(ROOT, "blog")
    return {
        d for d in os.listdir(blog_dir)
        if os.path.isdir(os.path.join(blog_dir, d))
    }


def validate(posts):
    """Fail loudly if any internal /blog/<slug>/ link points nowhere."""
    known = existing_blog_slugs() | {p["slug"] for p in posts}
    problems = []
    seen = set()
    for p in posts:
        if p["slug"] in seen:
            problems.append(f"duplicate slug: {p['slug']}")
        seen.add(p["slug"])
        body = " ".join(b for _, b in p["sections"])
        for slug in re.findall(r'href="/blog/([a-z0-9\-]+)/"', body):
            if slug not in known:
                problems.append(f"{p['slug']}: broken internal link -> /blog/{slug}/")
        for slug, _ in p.get("related", []):
            if slug not in known:
                problems.append(f"{p['slug']}: broken related link -> /blog/{slug}/")
        if "{AE}" in body:
            problems.append(f"{p['slug']}: unexpanded AE token")
        if "—" in body or "—" in p["title"] or "—" in p["description"]:
            problems.append(f"{p['slug']}: contains em dash")
    return problems


def word_counts(posts):
    out = []
    for p in posts:
        text = " ".join(b for _, b in p["sections"])
        text = re.sub(r"<[^>]+>", " ", text)
        out.append((p["slug"], len(text.split())))
    return out


def update_blog_index(posts):
    path = os.path.join(ROOT, "blog", "index.html")
    with open(path, encoding="utf-8") as f:
        html = f.read()

    anchor = '<div class="blog-grid">'
    if anchor not in html:
        raise SystemExit("blog index: could not find .blog-grid anchor")

    cards = []
    for p in posts:
        if f'href="{p["slug"]}/index.html"' in html:
            continue  # already listed
        cards.append(
            f'      <a href="{p["slug"]}/index.html" class="blog-card" style="text-decoration:none;">\n'
            f'        <div class="blog-card-body">\n'
            f'          <div class="meta">{p["date"]}</div>\n'
            f'          <h3>{p["title"]}</h3>\n'
            f'          <p>{p["description"]}</p>\n'
            f'        </div>\n'
            f'      </a>'
        )

    if not cards:
        return 0

    html = html.replace(anchor, anchor + "\n" + "\n".join(cards), 1)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    return len(cards)


def rebuild_sitemap(posts):
    """Rewrite sitemap.xml from the filesystem so nothing is missed."""
    urls = []

    # Root-level directory pages
    skip = {".git", "assets", "images", "scripts", "__pycache__", "blog"}
    for name in sorted(os.listdir(ROOT)):
        full = os.path.join(ROOT, name)
        if not os.path.isdir(full) or name in skip or name.startswith("."):
            continue
        if os.path.exists(os.path.join(full, "index.html")):
            urls.append((f"{BASE_URL}/{name}/", "weekly", "0.8"))

    # Blog index + posts
    urls.append((f"{BASE_URL}/blog/", "weekly", "0.8"))
    blog_dir = os.path.join(ROOT, "blog")
    for name in sorted(os.listdir(blog_dir)):
        full = os.path.join(blog_dir, name)
        if os.path.isdir(full) and os.path.exists(os.path.join(full, "index.html")):
            urls.append((f"{BASE_URL}/blog/{name}/", "monthly", "0.7"))

    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
             f'  <url><loc>{BASE_URL}/</loc><changefreq>weekly</changefreq><priority>1.0</priority></url>']
    for loc, freq, pri in urls:
        lines.append(f'  <url><loc>{loc}</loc><changefreq>{freq}</changefreq><priority>{pri}</priority></url>')
    lines.append('</urlset>')

    path = os.path.join(ROOT, "sitemap.xml")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    return len(urls) + 1


def main():
    posts = expand(POSTS)

    problems = validate(posts)
    if problems:
        print("VALIDATION FAILED:")
        for p in problems:
            print("  -", p)
        sys.exit(1)

    for p in posts:
        write_post(p, ROOT)
    print(f"Wrote {len(posts)} blog posts")

    counts = word_counts(posts)
    low = [(s, n) for s, n in counts if n < 800]
    high = [(s, n) for s, n in counts if n > 1400]
    print(f"Word counts: min={min(n for _, n in counts)} max={max(n for _, n in counts)} "
          f"avg={sum(n for _, n in counts)//len(counts)}")
    for s, n in low:
        print(f"  SHORT: {s} ({n})")
    for s, n in high:
        print(f"  LONG:  {s} ({n})")

    added = update_blog_index(posts)
    print(f"Blog index: added {added} cards")

    total = rebuild_sitemap(posts)
    print(f"Sitemap: {total} URLs")


if __name__ == "__main__":
    main()
