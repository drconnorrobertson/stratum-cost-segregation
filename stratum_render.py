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
AE_BOOKING = (
    "https://www.aetaxadvisors.com/discovery/"
    "?utm_source=stratumcostsegregation.com"
    "&amp;utm_medium=referral&amp;utm_campaign=cost_segregation"
)


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
      <a href="{r}reviews/index.html">Study Standards</a>
      <a href="{r}contact/index.html">Contact</a>
      <a href="{AE_BOOKING}" class="nav-cta">Book with AE Tax Advisors &rarr;</a>
    </div>
    <button class="mobile-toggle" type="button" aria-label="Open navigation" aria-controls="nav-menu" aria-expanded="false"><span aria-hidden="true">&#9776;</span></button>
  </div>
</nav>"""


def footer(depth):
    r = _rel(depth)
    return f"""  <footer class="footer">
  <div class="footer-partner">
    <div class="footer-partner-copy">
      <span class="eyebrow">One coordinated process</span>
      <strong>Stratum studies. AE Tax strategy.</strong>
      <p>Stratum documents the property. AE Tax Advisors leads the discovery call and broader strategy discussion.</p>
    </div>
    <a href="{AE_BOOKING}" class="btn btn-outline">Book a Discovery Call &rarr;</a>
  </div>

  <div class="footer-grid">
    <div>
      <div class="footer-brand"><span>Stratum</span> Cost Segregation</div>
      <p class="footer-desc">Engineering-based cost segregation studies for short-term and long-term rental property investors, with tax strategy coordination through AE Tax Advisors.</p>
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
        <li><a href="{r}reviews/index.html">Study Standards</a></li>
        <li><a href="{r}editorial-policy/index.html">Editorial Policy</a></li>
        <li><a href="{r}about/index.html">About Us</a></li>
      </ul>
    </div>
    <div>
      <h4>Contact</h4>
      <ul class="footer-links">
        <li><a href="tel:{PHONE_HREF}">{PHONE}</a></li>
        <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
        <li><a href="{AE_BOOKING}">Book with AE Tax Advisors</a></li>
        <li><a href="{r}contact/index.html">Contact Us</a></li>
      </ul>
    </div>
  </div>
  <div class="footer-trust">
    <div class="footer-trust-item"><span class="trust-icon">&#128736;</span> Engineering-Based Methodology</div>
    <div class="footer-trust-item"><span class="trust-icon">&#128196;</span> Component-Level Reporting</div>
    <div class="footer-trust-item"><span class="trust-icon">&#127968;</span> Nationwide Service</div>
    <div class="footer-trust-item"><span class="trust-icon">&#129309;</span> AE Tax Strategy Coordination</div>
  </div>
  <div class="footer-bottom">
    &copy; 2026 Stratum Cost Segregation. All rights reserved. &nbsp;|&nbsp; Engineering-based tax solutions for rental property investors.
  </div>
</footer>"""


ANALYTICS = """  <script>
    window.va = window.va || function () { (window.vaq = window.vaq || []).push(arguments); };
  </script>
  <script defer src="/_vercel/insights/script.js"></script>"""

SCRIPTS = """  <script>
  // Navigation behavior
  (function(){
    var nav=document.getElementById('main-nav');
    if(!nav)return;
    function onScroll(){nav.classList.toggle('scrolled',window.scrollY>40);}
    window.addEventListener('scroll',onScroll,{passive:true});
    onScroll();
    var toggle=nav.querySelector('.mobile-toggle');
    var menu=document.getElementById('nav-menu');
    if(!toggle||!menu)return;
    toggle.addEventListener('click',function(){
      var open=toggle.getAttribute('aria-expanded')==='true';
      toggle.setAttribute('aria-expanded',String(!open));
      toggle.setAttribute('aria-label',open?'Open navigation':'Close navigation');
      toggle.querySelector('span').textContent=open?'\u2630':'\u00d7';
      menu.classList.toggle('is-open',!open);
      document.body.classList.toggle('menu-open',!open);
    });
    menu.addEventListener('click',function(event){
      if(event.target.tagName!=='A')return;
      toggle.setAttribute('aria-expanded','false');
      toggle.setAttribute('aria-label','Open navigation');
      toggle.querySelector('span').textContent='\u2630';
      menu.classList.remove('is-open');
      document.body.classList.remove('menu-open');
    });
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
  // Measure outbound discovery-call clicks without collecting form or tax data.
  document.addEventListener('click',function(event){
    var link=event.target.closest('a[href*="aetaxadvisors.com/discovery"]');
    if(!link||!window.va)return;
    var placement=link.classList.contains('nav-cta')?'navigation':
      link.closest('.cta-banner')?'content-cta':link.closest('footer')?'footer':'inline';
    window.va('event',{name:'AE Discovery Click',data:{path:location.pathname,placement:placement}});
  });
  </script>"""


def _org_nodes():
    return [
        {
            "@type": "Organization",
            "@id": f"{BASE_URL}/#organization",
            "name": "Stratum Cost Segregation",
            "url": BASE_URL,
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
            "author": {"@type": "Person", "name": "Dr. Connor Robertson", "url": "https://www.drconnorrobertson.com/"},
            "reviewedBy": {"@type": "Organization", "name": "AE Tax Advisors Tax Team", "url": "https://www.aetaxadvisors.com/"},
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
{ANALYTICS}
</head>
<body>
{nav(2)}

<article class="article">
  <div class="breadcrumbs" style="padding:0; margin-bottom:24px;">
    <a href="../../index.html">Home</a> &raquo; <a href="../index.html">Blog</a> &raquo; <span>{title}</span>
  </div>
  <h1>{title}</h1>
  <div class="meta">{post['date']} &middot; Published by Dr. Connor Robertson &middot; Tax review by <a href="https://www.aetaxadvisors.com/">AE Tax Advisors Tax Team</a> &middot; <a href="../../editorial-policy/index.html">Editorial policy</a></div>

{body_html}
{related}  <div class="cta-banner">
  <h2>Ready to Unlock Hidden Tax Savings?</h2>
  <p>Discuss your property with AE Tax Advisors and learn whether a Stratum study may fit your tax plan.</p>
  <a href="{AE_BOOKING}" class="btn btn-gold">Book a Free AE Tax Advisors Call &rarr;</a>
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
