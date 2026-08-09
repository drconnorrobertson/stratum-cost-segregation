#!/usr/bin/env python3
"""Shared page renderer for Stratum Cost Segregation.

Produces pages that match the existing site template exactly: nav, JSON-LD
@graph, article body, CTA banner, footer and scripts.
"""

import json
import os

BASE_URL = "https://www.stratumcostsegregation.com"
PHONE = "(412) 255-8888"
PHONE_HREF = "+14122558888"
EMAIL = "info@stratumcostseg.com"


def _rel(depth):
    """Relative prefix for a page nested `depth` directories below the root."""
    return "../" * depth


def nav(depth):
    r = _rel(depth)
    return f"""  <nav class="nav" id="main-nav">
  <div class="nav-inner">
    <a href="{r}index.html" class="nav-logo"><span>Stratum</span> Cost Segregation</a>
    <div class="nav-links" id="nav-menu">
      <a href="{r}services/index.html">Services</a>
      <a href="{r}how-it-works/index.html">How It Works</a>
      <a href="{r}pricing/index.html">Pricing</a>
      <a href="{r}blog/index.html">Blog</a>
      <a href="{r}reviews/index.html">Reviews</a>
      <a href="{r}contact/index.html">Contact</a>
      <a href="{r}booking/index.html">Book a Call</a>
      <a href="{r}free-estimate/index.html" class="nav-cta">Free Estimate &rarr;</a>
    </div>
    <button class="mobile-toggle" onclick="var m=document.getElementById('nav-menu');m.style.display=m.style.display==='flex'?'none':'flex'" aria-label="Menu">&#9776;</button>
  </div>
</nav>"""


def footer(depth):
    r = _rel(depth)
    return f"""  <footer class="footer">
  <div class="footer-grid">
    <div>
      <div class="footer-brand"><span>Stratum</span> Cost Segregation</div>
      <p class="footer-desc">Engineering-based cost segregation studies for short-term and long-term rental property investors. Maximize depreciation deductions and accelerate tax savings across all 50 states.</p>
      <div class="footer-social">
        <a href="#" aria-label="LinkedIn" title="LinkedIn">in</a>
        <a href="#" aria-label="Twitter" title="Twitter">X</a>
        <a href="#" aria-label="Facebook" title="Facebook">f</a>
      </div>
    </div>
    <div>
      <h4>Services</h4>
      <ul class="footer-links">
        <li><a href="{r}short-term-rental-cost-segregation/index.html">STR Cost Segregation</a></li>
        <li><a href="{r}long-term-rental-cost-segregation/index.html">LTR Cost Segregation</a></li>
        <li><a href="{r}how-it-works/index.html">How It Works</a></li>
        <li><a href="{r}pricing/index.html">Pricing</a></li>
      </ul>
    </div>
    <div>
      <h4>Resources</h4>
      <ul class="footer-links">
        <li><a href="{r}blog/index.html">Blog</a></li>
        <li><a href="{r}faq/index.html">FAQ</a></li>
        <li><a href="{r}reviews/index.html">Reviews</a></li>
        <li><a href="{r}about/index.html">About Us</a></li>
      </ul>
    </div>
    <div>
      <h4>Contact</h4>
      <ul class="footer-links">
        <li><a href="tel:{PHONE_HREF}">{PHONE}</a></li>
        <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
        <li><a href="{r}booking/index.html">Book a Call</a></li>
        <li><a href="{r}free-estimate/index.html">Free Estimate</a></li>
        <li><a href="{r}contact/index.html">Contact Us</a></li>
      </ul>
    </div>
  </div>
  <div class="footer-trust">
    <div class="footer-trust-item"><span class="trust-icon">&#9733;</span> 4.9/5.0 Client Rating</div>
    <div class="footer-trust-item"><span class="trust-icon">&#128737;</span> IRS Audit-Ready</div>
    <div class="footer-trust-item"><span class="trust-icon">&#127968;</span> All 50 States</div>
    <div class="footer-trust-item"><span class="trust-icon">&#9989;</span> 5,000+ Studies Completed</div>
  </div>
  <div class="footer-bottom">
    &copy; 2026 Stratum Cost Segregation. All rights reserved. &nbsp;|&nbsp; Engineering-based tax solutions for rental property investors.
  </div>
</footer>"""


SCRIPTS = """  <script>
  // Nav scroll effect
  (function(){
    var nav=document.getElementById('main-nav');
    if(!nav)return;
    function onScroll(){nav.classList.toggle('scrolled',window.scrollY>40);}
    window.addEventListener('scroll',onScroll,{passive:true});
    onScroll();
  })();
  // Scroll-triggered fade-in animations
  (function(){
    var els=document.querySelectorAll('.fade-in-up');
    if(!els.length)return;
    var observer=new IntersectionObserver(function(entries){
      entries.forEach(function(e){
        if(e.isIntersecting){e.target.classList.add('visible');observer.unobserve(e.target);}
      });
    },{threshold:0.1,rootMargin:'0px 0px -40px 0px'});
    els.forEach(function(el){observer.observe(el);});
  })();
  </script>"""


def _org_nodes():
    return [
        {
            "@type": "Organization",
            "@id": f"{BASE_URL}/#organization",
            "name": "Stratum Cost Segregation",
            "url": BASE_URL,
            "logo": {"@type": "ImageObject", "url": f"{BASE_URL}/logo.png", "width": 300, "height": 60},
            "image": f"{BASE_URL}/og-image.png",
            "description": "Professional engineering-based cost segregation studies for short-term and long-term rental property investors across all 50 states.",
            "telephone": "+1-412-255-8888",
            "email": EMAIL,
            "address": {"@type": "PostalAddress", "addressLocality": "Pittsburgh", "addressRegion": "PA", "addressCountry": "US"},
            "areaServed": {"@type": "Country", "name": "United States"},
            "sameAs": [],
        },
        {
            "@type": "WebSite",
            "@id": f"{BASE_URL}/#website",
            "name": "Stratum Cost Segregation",
            "url": BASE_URL,
            "publisher": {"@id": f"{BASE_URL}/#organization"},
        },
        {
            "@type": "ProfessionalService",
            "@id": f"{BASE_URL}/#business",
            "name": "Stratum Cost Segregation",
            "url": BASE_URL,
            "logo": {"@type": "ImageObject", "url": f"{BASE_URL}/logo.png", "width": 300, "height": 60},
            "image": f"{BASE_URL}/og-image.png",
            "description": "Professional engineering-based cost segregation studies for short-term and long-term rental property investors. Maximize depreciation deductions and accelerate tax savings.",
            "telephone": "+1-412-255-8888",
            "email": EMAIL,
            "priceRange": "$$$",
            "address": {"@type": "PostalAddress", "addressLocality": "Pittsburgh", "addressRegion": "PA", "addressCountry": "US"},
            "areaServed": {"@type": "Country", "name": "United States"},
            "serviceType": [
                "Cost Segregation Studies",
                "Accelerated Depreciation Analysis",
                "IRS Form 3115 Look-Back Studies",
                "Partial Asset Disposition Studies",
                "Tax Depreciation Consulting",
            ],
            "knowsAbout": [
                "Cost Segregation",
                "MACRS Depreciation",
                "Bonus Depreciation",
                "IRS Form 3115",
                "Real Estate Tax Planning",
                "Short-Term Rental Tax Strategy",
            ],
            "parentOrganization": {"@id": f"{BASE_URL}/#organization"},
        },
    ]


def render_post(post):
    """Render a blog post page (blog/<slug>/index.html)."""
    slug = post["slug"]
    title = post["title"]
    desc = post["description"]
    url = f"{BASE_URL}/blog/{slug}/"
    full_title = f"{title} | Stratum Cost Segregation"
    iso = post.get("iso_date", "2026-08-09")

    graph = _org_nodes() + [
        {
            "@type": "BreadcrumbList",
            "@id": f"{url}#breadcrumb",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{BASE_URL}/"},
                {"@type": "ListItem", "position": 2, "name": "Blog", "item": f"{BASE_URL}/blog/"},
                {"@type": "ListItem", "position": 3, "name": title, "item": url},
            ],
        },
        {
            "@type": "WebPage",
            "@id": f"{url}#webpage",
            "url": url,
            "name": full_title,
            "description": desc,
            "isPartOf": {"@id": f"{BASE_URL}/#website"},
            "about": {"@id": f"{BASE_URL}/#business"},
            "breadcrumb": {"@id": f"{url}#breadcrumb"},
        },
        {
            "@type": "BlogPosting",
            "@id": f"{url}#article",
            "headline": title,
            "description": desc,
            "datePublished": iso,
            "dateModified": iso,
            "author": {"@type": "Organization", "name": "Stratum Cost Segregation", "@id": f"{BASE_URL}/#organization"},
            "publisher": {"@id": f"{BASE_URL}/#organization"},
            "mainEntityOfPage": {"@type": "WebPage", "@id": url},
            "url": url,
            "isPartOf": {"@id": f"{BASE_URL}/#website"},
        },
    ]
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph})

    body = []
    for heading, html in post["sections"]:
        body.append(f"    <h2>{heading}</h2>\n{html}\n")
    body_html = "\n".join(body)

    related = ""
    if post.get("related"):
        items = "\n".join(
            f'      <li><a href="/blog/{s}/">{t}</a></li>' for s, t in post["related"]
        )
        related = f"""    <h2>Related Reading</h2>
    <ul>
{items}
    </ul>

"""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{full_title}</title>
  <meta name="description" content="{desc}">
  <meta property="og:title" content="{full_title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:type" content="article">
  <meta property="og:url" content="{url}">
  <meta property="og:site_name" content="Stratum Cost Segregation">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{full_title}">
  <meta name="twitter:description" content="{desc}">
  <link rel="canonical" href="{url}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../../style.css">

<script type="application/ld+json">{ld}</script>
</head>
<body>
{nav(2)}

<article class="article">
  <div class="breadcrumbs" style="padding:0; margin-bottom:24px;">
    <a href="../../index.html">Home</a> &raquo; <a href="../index.html">Blog</a> &raquo; <span>{title}</span>
  </div>
  <h1>{title}</h1>
  <div class="meta">{post['date']} &middot; Stratum Cost Segregation</div>

{body_html}
{related}  <div class="cta-banner">
  <h2>Ready to Unlock Hidden Tax Savings?</h2>
  <p>Get a free, no-obligation estimate for your property, or book a call with a Stratum specialist.</p>
  <a href="../../free-estimate/index.html" class="btn btn-gold">Get Your Free Estimate &rarr;</a>
  <a href="../../booking/index.html" class="btn btn-outline">Book a Call</a>
</div>
</article>

{footer(2)}

{SCRIPTS}
</body>
</html>"""


def write_post(post, root):
    out_dir = os.path.join(root, "blog", post["slug"])
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(render_post(post))
    return f"blog/{post['slug']}/"
