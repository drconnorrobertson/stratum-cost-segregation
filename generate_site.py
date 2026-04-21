#!/usr/bin/env python3
"""
Stratum Cost Segregation - Full Site Generator
Generates 120+ HTML pages with shared CSS, SEO, schema markup, and internal linking.
"""
import os
import json
from datetime import datetime

SITE_URL = "https://drconnorrobertson.github.io/stratum-cost-segregation"
SITE_NAME = "Stratum Cost Segregation"
PHONE = "(412) 255-8888"
EMAIL = "info@stratumcostseg.com"
YEAR = datetime.now().year

# ============================================================
# COLOR SCHEME & SHARED CSS (loaded from style.css)
# ============================================================
# CSS is maintained in style.css and loaded via link tag.
# The SHARED_CSS variable is kept empty since we use external CSS.
SHARED_CSS = ""  # CSS is in style.css

# ============================================================
# NAVIGATION & FOOTER HTML
# ============================================================
def get_nav(depth=0):
    prefix = "../" * depth
    return f"""<nav class="nav" id="main-nav">
  <div class="nav-inner">
    <a href="{prefix}index.html" class="nav-logo"><span>Stratum</span> Cost Segregation</a>
    <div class="nav-links" id="nav-menu">
      <a href="{prefix}services/index.html">Services</a>
      <a href="{prefix}how-it-works/index.html">How It Works</a>
      <a href="{prefix}pricing/index.html">Pricing</a>
      <a href="{prefix}blog/index.html">Blog</a>
      <a href="{prefix}reviews/index.html">Reviews</a>
      <a href="{prefix}contact/index.html">Contact</a>
      <a href="{prefix}free-estimate/index.html" class="nav-cta">Free Estimate &rarr;</a>
    </div>
    <button class="mobile-toggle" onclick="var m=document.getElementById('nav-menu');m.style.display=m.style.display==='flex'?'none':'flex'" aria-label="Menu">&#9776;</button>
  </div>
</nav>"""


def get_footer(depth=0):
    prefix = "../" * depth
    return f"""<footer class="footer">
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
        <li><a href="{prefix}short-term-rental-cost-segregation/index.html">STR Cost Segregation</a></li>
        <li><a href="{prefix}long-term-rental-cost-segregation/index.html">LTR Cost Segregation</a></li>
        <li><a href="{prefix}how-it-works/index.html">How It Works</a></li>
        <li><a href="{prefix}pricing/index.html">Pricing</a></li>
      </ul>
    </div>
    <div>
      <h4>Resources</h4>
      <ul class="footer-links">
        <li><a href="{prefix}blog/index.html">Blog</a></li>
        <li><a href="{prefix}faq/index.html">FAQ</a></li>
        <li><a href="{prefix}reviews/index.html">Reviews</a></li>
        <li><a href="{prefix}about/index.html">About Us</a></li>
      </ul>
    </div>
    <div>
      <h4>Contact</h4>
      <ul class="footer-links">
        <li><a href="tel:+14122558888">{PHONE}</a></li>
        <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
        <li><a href="{prefix}free-estimate/index.html">Free Estimate</a></li>
        <li><a href="{prefix}contact/index.html">Contact Us</a></li>
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
    &copy; {YEAR} Stratum Cost Segregation. All rights reserved. &nbsp;|&nbsp; Engineering-based tax solutions for rental property investors.
  </div>
</footer>"""


def get_cta_banner(depth=0):
    prefix = "../" * depth
    return f"""<div class="cta-banner">
  <h2>Ready to Unlock Hidden Tax Savings?</h2>
  <p>Get a free, no-obligation estimate for your rental property cost segregation study.</p>
  <a href="{prefix}free-estimate/index.html" class="btn btn-gold">Get Your Free Estimate &rarr;</a>
</div>"""


def wrap_page(title, description, body, depth=0, schema="", canonical_path=""):
    prefix = "../" * depth
    css_path = f"{prefix}style.css"
    canonical = f"{SITE_URL}/{canonical_path}" if canonical_path else SITE_URL
    og_title = title.replace('"', '&quot;')
    og_desc = description.replace('"', '&quot;')
    faq_js = """
<script>
document.querySelectorAll('.faq-q').forEach(q => {
  q.addEventListener('click', () => {
    q.parentElement.classList.toggle('open');
  });
});
</script>""" if 'faq-q' in body else ""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{og_desc}">
  <meta property="og:title" content="{og_title}">
  <meta property="og:description" content="{og_desc}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{canonical}">
  <meta property="og:site_name" content="{SITE_NAME}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{og_title}">
  <meta name="twitter:description" content="{og_desc}">
  <link rel="canonical" href="{canonical}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{css_path}">
  {schema}
</head>
<body>
  {get_nav(depth)}
  {body}
  {get_footer(depth)}
  {faq_js}
  <script>
  // Nav scroll effect
  (function(){{
    var nav=document.getElementById('main-nav');
    if(!nav)return;
    function onScroll(){{nav.classList.toggle('scrolled',window.scrollY>40);}}
    window.addEventListener('scroll',onScroll,{{passive:true}});
    onScroll();
  }})();
  // Scroll-triggered fade-in animations
  (function(){{
    var els=document.querySelectorAll('.fade-in-up');
    if(!els.length)return;
    var observer=new IntersectionObserver(function(entries){{
      entries.forEach(function(e){{
        if(e.isIntersecting){{e.target.classList.add('visible');observer.unobserve(e.target);}}
      }});
    }},{{threshold:0.1,rootMargin:'0px 0px -40px 0px'}});
    els.forEach(function(el){{observer.observe(el);}});
  }})();
  </script>
</body>
</html>"""


def write_file(path, content):
    full = os.path.join(".", path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  Created: {path}")


# ============================================================
# CORE PAGES
# ============================================================
def generate_homepage():
    body = """
<section class="hero">
  <div class="container">
    <h1>Maximize Your Rental Property <span>Tax Savings</span></h1>
    <p>Stratum Cost Segregation delivers professional, IRS-compliant cost segregation studies for short-term and long-term rental property investors across all 50 states.</p>
    <div class="hero-buttons">
      <a href="free-estimate/index.html" class="btn btn-gold">Get a Free Estimate &rarr;</a>
      <a href="how-it-works/index.html" class="btn btn-outline">How It Works</a>
    </div>
  </div>
</section>

<div class="social-proof-bar">
  <p>Trusted by <span>5,000+</span> rental property investors &nbsp;&bull;&nbsp; <span>$2.1B+</span> in tax savings identified &nbsp;&bull;&nbsp; All <span>50</span> states</p>
</div>

<section class="section">
  <div class="container">
    <div class="stats">
      <div class="stat-item fade-in-up"><div class="stat-num">$2.1B+</div><div class="stat-label">Tax Savings Identified</div></div>
      <div class="stat-item fade-in-up"><div class="stat-num">5,000+</div><div class="stat-label">Studies Completed</div></div>
      <div class="stat-item fade-in-up"><div class="stat-num">50</div><div class="stat-label">States Served</div></div>
      <div class="stat-item fade-in-up"><div class="stat-num">14 Days</div><div class="stat-label">Average Turnaround</div></div>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <h2 class="section-title">Why Property Investors Choose Stratum</h2>
    <p class="section-subtitle">We specialize exclusively in residential cost segregation for STR and LTR investors, delivering precise, audit-ready studies.</p>
    <div class="card-grid">
      <div class="card fade-in-up">
        <div class="card-icon">&#9881;</div>
        <h3>Engineering-Based Studies</h3>
        <p>Our studies are prepared by licensed professionals using component-level analysis that meets IRS standards for audit defense. Every asset is individually identified and classified.</p>
      </div>
      <div class="card fade-in-up">
        <div class="card-icon">&#128176;</div>
        <h3>Maximize Depreciation</h3>
        <p>Reclassify 20-40% of your property cost basis into 5, 7, and 15-year recovery periods instead of 27.5 or 39 years. Accelerate deductions and improve cash flow from day one.</p>
      </div>
      <div class="card fade-in-up">
        <div class="card-icon">&#128640;</div>
        <h3>Fast 14-Day Delivery</h3>
        <p>Receive your completed, audit-ready cost segregation report within 14 business days. We know time matters during tax season and for year-end planning.</p>
      </div>
      <div class="card fade-in-up">
        <div class="card-icon">&#128737;</div>
        <h3>IRS Audit Protection</h3>
        <p>Every Stratum study includes comprehensive documentation, component photographs, and engineering methodology that withstands IRS examination.</p>
      </div>
      <div class="card fade-in-up">
        <div class="card-icon">&#127968;</div>
        <h3>STR &amp; LTR Specialists</h3>
        <p>We focus exclusively on residential rental properties, from Airbnb vacation rentals to traditional long-term rental portfolios. We understand the nuances of each strategy.</p>
      </div>
      <div class="card fade-in-up">
        <div class="card-icon">&#128200;</div>
        <h3>Look-Back Studies Available</h3>
        <p>Already own your property? File Form 3115 to claim missed depreciation from prior years without amending previous returns. Recover years of unclaimed deductions.</p>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <h2 class="section-title">How Cost Segregation Works</h2>
    <p class="section-subtitle">A straightforward process that accelerates your depreciation deductions and puts money back in your pocket.</p>
    <div class="card-grid">
      <div class="card fade-in-up">
        <h3>1. Property Analysis</h3>
        <p>Share your property details, closing statement, and photos. We evaluate whether a cost segregation study makes financial sense for your specific property and investment strategy.</p>
      </div>
      <div class="card fade-in-up">
        <h3>2. Engineering Study</h3>
        <p>Our team conducts a detailed component-level analysis, identifying and reclassifying building components into shorter MACRS recovery periods (5, 7, and 15-year property classes).</p>
      </div>
      <div class="card fade-in-up">
        <h3>3. Deliver Your Report</h3>
        <p>You receive a comprehensive, audit-ready report with all asset classifications, depreciation schedules, and supporting documentation. Your CPA files the study with your tax return.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
""" + get_cta_banner(0) + """
  </div>
</section>
"""
    return wrap_page(
        "Stratum Cost Segregation | Residential Cost Seg Studies for STR & LTR",
        "Professional cost segregation studies for short-term and long-term rental properties. Maximize depreciation deductions and accelerate tax savings. Free estimates available.",
        body, depth=0, canonical_path=""
    )


def generate_about():
    body = """
<section class="hero" style="padding-bottom:60px;">
  <div class="container">
    <h1>About <span>Stratum</span> Cost Segregation</h1>
    <p>We are a team of tax professionals and engineers dedicated to helping residential rental property investors maximize their depreciation deductions through IRS-compliant cost segregation studies.</p>
  </div>
</section>
<section class="section">
  <div class="container" style="max-width:800px;">
    <h2 class="section-title" style="text-align:left; font-size:1.8rem;">Our Mission</h2>
    <p style="color:var(--text-muted); margin-bottom:24px;">Stratum Cost Segregation was founded with a singular focus: to deliver precise, affordable, and defensible cost segregation studies to residential rental property investors. Whether you own one Airbnb or a portfolio of long-term rentals, our engineering-based approach ensures that every eligible dollar is reclassified into accelerated depreciation categories.</p>
    <p style="color:var(--text-muted); margin-bottom:24px;">Too many property investors leave money on the table because they either do not know about cost segregation or believe it is only for large commercial buildings. That is not the case. A single-family rental purchased for $350,000 can yield $25,000 to $50,000 in first-year depreciation deductions through a properly conducted cost segregation study.</p>
    <h2 class="section-title" style="text-align:left; font-size:1.8rem; margin-top:48px;">Why Stratum?</h2>
    <p style="color:var(--text-muted); margin-bottom:24px;">The name Stratum comes from the geological concept of layers. Just as the earth is composed of distinct strata, every building is composed of distinct components with different useful lives. Our job is to identify each layer and classify it correctly under the IRS tax code, unlocking deductions that straight-line depreciation would spread over decades.</p>
    <p style="color:var(--text-muted); margin-bottom:24px;">We serve property investors in all 50 states and have completed over 5,000 studies. Our reports are prepared by licensed engineers and reviewed by tax professionals, ensuring they meet the highest standards for IRS compliance and audit defense.</p>
    <h2 class="section-title" style="text-align:left; font-size:1.8rem; margin-top:48px;">Our Values</h2>
    <p style="color:var(--text-muted); margin-bottom:12px;"><strong style="color:var(--gold);">Precision.</strong> Every component is individually identified and classified. No shortcuts, no estimates.</p>
    <p style="color:var(--text-muted); margin-bottom:12px;"><strong style="color:var(--gold);">Transparency.</strong> Clear pricing, clear timelines, and clear reports. No hidden fees or upsells.</p>
    <p style="color:var(--text-muted); margin-bottom:12px;"><strong style="color:var(--gold);">Speed.</strong> 14-day average turnaround. We respect your timeline and your tax deadlines.</p>
    <p style="color:var(--text-muted); margin-bottom:12px;"><strong style="color:var(--gold);">Defense.</strong> Every study is built to withstand IRS scrutiny, with full engineering documentation and methodology.</p>
  </div>
</section>
<section class="section section-alt">
  <div class="container">
""" + get_cta_banner(1) + """
  </div>
</section>
"""
    return wrap_page("About Stratum Cost Segregation | Our Mission & Team",
        "Learn about Stratum Cost Segregation, our mission, and our team of tax professionals and engineers dedicated to maximizing depreciation for rental property investors.",
        body, depth=1, canonical_path="about/")


def generate_services():
    body = """
<section class="hero" style="padding-bottom:60px;">
  <div class="container">
    <h1>Cost Segregation <span>Services</span></h1>
    <p>Professional, IRS-compliant cost segregation studies designed specifically for residential rental property investors.</p>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="card-grid">
      <div class="card fade-in-up">
        <div class="card-icon">&#127965;</div>
        <h3>Short-Term Rental Cost Segregation</h3>
        <p>Maximize depreciation on your Airbnb, VRBO, or vacation rental property. STR investors can often qualify for bonus depreciation to offset active income when they meet material participation requirements. Our studies identify every component eligible for accelerated recovery.</p>
        <p style="margin-top:16px;"><a href="../short-term-rental-cost-segregation/index.html" class="btn btn-outline" style="padding:10px 20px; font-size:0.9rem;">Learn More</a></p>
      </div>
      <div class="card fade-in-up">
        <div class="card-icon">&#127970;</div>
        <h3>Long-Term Rental Cost Segregation</h3>
        <p>Accelerate deductions on your traditional rental properties with a study tailored to buy-and-hold investors. Even with passive activity limitations, LTR cost segregation creates significant tax-deferred cash flow advantages and portfolio-level depreciation strategies.</p>
        <p style="margin-top:16px;"><a href="../long-term-rental-cost-segregation/index.html" class="btn btn-outline" style="padding:10px 20px; font-size:0.9rem;">Learn More</a></p>
      </div>
      <div class="card fade-in-up">
        <div class="card-icon">&#128203;</div>
        <h3>Look-Back / Catch-Up Studies</h3>
        <p>Already own your property and missed years of accelerated depreciation? File IRS Form 3115 to claim prior-year deductions in a single tax year without amending old returns. This is one of the most powerful tools in a real estate investor's tax toolkit.</p>
        <p style="margin-top:16px;"><a href="../blog/form-3115-look-back-cost-segregation/index.html" class="btn btn-outline" style="padding:10px 20px; font-size:0.9rem;">Learn More</a></p>
      </div>
      <div class="card fade-in-up">
        <div class="card-icon">&#128269;</div>
        <h3>Partial Asset Disposition</h3>
        <p>Renovating your rental? A partial asset disposition study identifies components being replaced, allowing you to write off their remaining book value in the year of renovation. This pairs perfectly with a cost segregation study on the newly installed improvements.</p>
      </div>
      <div class="card fade-in-up">
        <div class="card-icon">&#128202;</div>
        <h3>Portfolio Studies</h3>
        <p>Own multiple rental properties? We offer portfolio pricing and batch processing to maximize efficiency across your entire real estate portfolio. One engagement, one point of contact, all properties analyzed.</p>
      </div>
      <div class="card fade-in-up">
        <div class="card-icon">&#128101;</div>
        <h3>CPA Partnership Program</h3>
        <p>We work directly with your CPA or tax advisor, providing all documentation and schedules needed to file the study. Our reports integrate seamlessly with major tax preparation software for efficient implementation.</p>
      </div>
    </div>
  </div>
</section>
<section class="section section-alt">
  <div class="container">
""" + get_cta_banner(1) + """
  </div>
</section>
"""
    return wrap_page("Cost Segregation Services | STR, LTR, Look-Back Studies",
        "Explore our cost segregation services including STR studies, LTR studies, look-back analysis, partial asset dispositions, and portfolio studies for rental property investors.",
        body, depth=1, canonical_path="services/")


def generate_str():
    body = """
<section class="hero" style="padding-bottom:60px;">
  <div class="container">
    <h1>Short-Term Rental <span>Cost Segregation</span></h1>
    <p>Unlock massive first-year depreciation deductions on your Airbnb, VRBO, or vacation rental property with an engineering-based cost segregation study.</p>
  </div>
</section>
<section class="section">
  <div class="container" style="max-width:800px;">
    <h2 style="color:var(--white); font-size:1.8rem; margin-bottom:16px;">Why STR Investors Need Cost Segregation</h2>
    <p style="color:var(--text-muted); margin-bottom:20px;">Short-term rental properties present a unique and powerful tax opportunity. When the average guest stay is seven days or less and the owner materially participates in the rental activity, the IRS treats the income as non-passive. This distinction is critical because it allows STR investors to use accelerated depreciation deductions from a cost segregation study to offset W-2 wages, business income, and other active income sources.</p>
    <p style="color:var(--text-muted); margin-bottom:20px;">Without a cost segregation study, your $500,000 vacation rental is depreciated straight-line over 27.5 years, yielding roughly $18,000 per year in depreciation. With a cost segregation study, 25-40% of that cost basis can be reclassified into 5, 7, and 15-year property, generating $75,000 to $150,000 or more in first-year deductions when combined with bonus depreciation.</p>

    <h2 style="color:var(--white); font-size:1.8rem; margin:40px 0 16px;">What We Reclassify</h2>
    <p style="color:var(--text-muted); margin-bottom:16px;">Our engineering team identifies and segregates building components into the following MACRS recovery periods:</p>
    <div class="table-wrap" style="margin-bottom:32px;">
      <table>
        <tr><th>Recovery Period</th><th>Example Components</th><th>Typical % of Basis</th></tr>
        <tr><td>5-Year Property</td><td>Appliances, carpeting, window treatments, specialty lighting, decorative fixtures</td><td>15-25%</td></tr>
        <tr><td>7-Year Property</td><td>Furniture, outdoor equipment, security systems, specialty cabinetry</td><td>3-8%</td></tr>
        <tr><td>15-Year Property</td><td>Landscaping, driveways, patios, fencing, outdoor lighting, sidewalks</td><td>5-12%</td></tr>
        <tr><td>27.5-Year Property</td><td>Structural components (walls, roof, foundation) remain at standard recovery</td><td>55-75%</td></tr>
      </table>
    </div>

    <h2 style="color:var(--white); font-size:1.8rem; margin:40px 0 16px;">The STR Tax Strategy</h2>
    <p style="color:var(--text-muted); margin-bottom:20px;">The short-term rental tax strategy has become one of the most discussed strategies in real estate investing. Here is how it works in practice: an investor purchases a vacation rental property, conducts a cost segregation study, and uses the resulting accelerated depreciation to generate a large paper loss. If the investor qualifies as a real estate professional or the property meets the short-term rental exception, this loss can offset ordinary income.</p>
    <p style="color:var(--text-muted); margin-bottom:20px;">For a high-income earner with a $600,000 STR purchase, a cost segregation study might identify $180,000 in components eligible for accelerated depreciation. In the first year, this could create a tax deduction that saves $50,000 to $70,000 in federal taxes alone, depending on the investor's marginal tax bracket.</p>

    <h2 style="color:var(--white); font-size:1.8rem; margin:40px 0 16px;">Bonus Depreciation and STR</h2>
    <p style="color:var(--text-muted); margin-bottom:20px;">As of 2026, bonus depreciation allows investors to deduct a significant percentage of the cost of 5, 7, and 15-year property in the year the asset is placed in service. This is a time-sensitive benefit, as bonus depreciation rates have been phasing down. The sooner you conduct your study, the more you can capture.</p>
    <p style="color:var(--text-muted); margin-bottom:20px;">Stratum Cost Segregation delivers your study within 14 business days so you can take full advantage of current bonus depreciation rates before they decrease further.</p>
  </div>
</section>
<section class="section section-alt">
  <div class="container">
""" + get_cta_banner(1) + """
  </div>
</section>
"""
    return wrap_page("Short-Term Rental Cost Segregation | Airbnb & Vacation Rental Tax Savings",
        "Maximize depreciation on your short-term rental property with a professional cost segregation study. Accelerate deductions on your Airbnb or VRBO investment.",
        body, depth=1, canonical_path="short-term-rental-cost-segregation/")


def generate_ltr():
    body = """
<section class="hero" style="padding-bottom:60px;">
  <div class="container">
    <h1>Long-Term Rental <span>Cost Segregation</span></h1>
    <p>Accelerate depreciation deductions on your traditional rental properties and improve your portfolio cash flow with a professional cost segregation study.</p>
  </div>
</section>
<section class="section">
  <div class="container" style="max-width:800px;">
    <h2 style="color:var(--white); font-size:1.8rem; margin-bottom:16px;">Cost Segregation for Buy-and-Hold Investors</h2>
    <p style="color:var(--text-muted); margin-bottom:20px;">Long-term rental investors often assume cost segregation is only for short-term rentals or large commercial properties. That is a costly misconception. A residential rental property held as a traditional long-term rental is fully eligible for a cost segregation study, and the tax benefits can be substantial.</p>
    <p style="color:var(--text-muted); margin-bottom:20px;">Under standard depreciation, your rental property is depreciated over 27.5 years using the straight-line method. A cost segregation study identifies building components that qualify for 5, 7, and 15-year MACRS recovery periods, front-loading your depreciation deductions and increasing your after-tax cash flow in the early years of ownership.</p>

    <h2 style="color:var(--white); font-size:1.8rem; margin:40px 0 16px;">Tax Benefits for LTR Investors</h2>
    <p style="color:var(--text-muted); margin-bottom:20px;">For a $400,000 long-term rental property (after land allocation), a cost segregation study typically reclassifies $80,000 to $140,000 into accelerated depreciation categories. Combined with applicable bonus depreciation, this can generate first-year deductions of $60,000 to $100,000 or more, compared to roughly $14,500 under straight-line depreciation.</p>
    <p style="color:var(--text-muted); margin-bottom:20px;">While long-term rental income is generally classified as passive, investors who qualify as Real Estate Professionals under IRC Section 469 can use these deductions to offset active income. Even passive investors benefit from accelerated depreciation by sheltering rental income and reducing current-year tax liability.</p>

    <h2 style="color:var(--white); font-size:1.8rem; margin:40px 0 16px;">Portfolio-Level Strategy</h2>
    <p style="color:var(--text-muted); margin-bottom:20px;">If you own multiple long-term rental properties, a portfolio-level cost segregation strategy can compound the benefits. By strategically timing studies across your portfolio, you can create consistent tax-deferred cash flow advantages year after year. We offer portfolio pricing for investors with three or more properties.</p>
    <p style="color:var(--text-muted); margin-bottom:20px;">Stratum specializes in residential cost segregation and understands the unique aspects of long-term rental properties, including tenant improvements, common area allocations, and multi-unit residential structures.</p>
  </div>
</section>
<section class="section section-alt">
  <div class="container">
""" + get_cta_banner(1) + """
  </div>
</section>
"""
    return wrap_page("Long-Term Rental Cost Segregation | Traditional Rental Property Tax Savings",
        "Accelerate depreciation on your long-term rental properties with a professional cost segregation study. Improve cash flow and reduce taxes on buy-and-hold investments.",
        body, depth=1, canonical_path="long-term-rental-cost-segregation/")


def generate_how_it_works():
    body = """
<section class="hero" style="padding-bottom:60px;">
  <div class="container">
    <h1>How Cost Segregation <span>Works</span></h1>
    <p>A clear, three-step process from property analysis to completed report. We handle the engineering so you can focus on investing.</p>
  </div>
</section>
<section class="section">
  <div class="container" style="max-width:800px;">
    <h2 style="color:var(--white); font-size:1.8rem; margin-bottom:24px;">Step 1: Free Property Evaluation</h2>
    <p style="color:var(--text-muted); margin-bottom:20px;">Submit your property details through our free estimate form. We review the purchase price, property type, and basic details to determine whether a cost segregation study makes financial sense for your investment. Most residential properties above $150,000 in purchase price are strong candidates. We provide a preliminary estimate of potential tax savings before you commit.</p>

    <h2 style="color:var(--white); font-size:1.8rem; margin:40px 0 16px;">Step 2: Engineering Analysis</h2>
    <p style="color:var(--text-muted); margin-bottom:20px;">Once you engage Stratum, we begin our component-level engineering analysis. You provide your closing statement (HUD-1 or CD), property appraisal or listing photos, and any relevant renovation documentation. Our engineering team identifies and classifies every building component according to IRS guidelines, including MACRS class life assignments per Revenue Procedure 87-56 and the IRS Cost Segregation Audit Techniques Guide.</p>
    <p style="color:var(--text-muted); margin-bottom:20px;">Each component is individually categorized into the appropriate recovery period: 5-year personal property, 7-year personal property, 15-year land improvements, or 27.5-year real property. We document the methodology, component descriptions, and cost allocations for full IRS compliance.</p>

    <h2 style="color:var(--white); font-size:1.8rem; margin:40px 0 16px;">Step 3: Report Delivery</h2>
    <p style="color:var(--text-muted); margin-bottom:20px;">Within 14 business days, you receive your completed cost segregation report. The report includes a detailed asset listing, depreciation schedules by recovery period, supporting photographs, engineering methodology, and all documentation required for IRS audit defense. We deliver the report directly to you and your CPA in a format that integrates with standard tax preparation software.</p>
    <p style="color:var(--text-muted); margin-bottom:20px;">Your CPA or tax preparer uses the study to file the appropriate depreciation schedules with your tax return. For properties placed in service in prior years, we include Form 3115 guidance so your CPA can file a change in accounting method and claim all prior-year missed depreciation in a single tax year.</p>
  </div>
</section>
<section class="section section-alt">
  <div class="container">
    <h2 class="section-title">What You Need to Get Started</h2>
    <div class="card-grid" style="max-width:800px; margin:32px auto 0;">
      <div class="card fade-in-up">
        <h3>Closing Statement</h3>
        <p>Your HUD-1 settlement statement or closing disclosure showing the purchase price breakdown and transaction details.</p>
      </div>
      <div class="card fade-in-up">
        <h3>Property Photos</h3>
        <p>Interior and exterior photographs of the property. Listing photos from the purchase are typically sufficient for most studies.</p>
      </div>
      <div class="card fade-in-up">
        <h3>Renovation Documentation</h3>
        <p>If applicable, invoices and details for any renovations or improvements made to the property since purchase.</p>
      </div>
      <div class="card fade-in-up">
        <h3>Property Details</h3>
        <p>Basic information including property address, date placed in service, property type (STR or LTR), and your CPA contact.</p>
      </div>
    </div>
  </div>
</section>
<section class="section">
  <div class="container">
""" + get_cta_banner(1) + """
  </div>
</section>
"""
    return wrap_page("How Cost Segregation Works | Step-by-Step Process",
        "Learn how the cost segregation process works from free estimate to completed report. Engineering-based studies delivered in 14 business days.",
        body, depth=1, canonical_path="how-it-works/")


def generate_pricing():
    body = """
<section class="hero" style="padding-bottom:60px;">
  <div class="container">
    <h1>Transparent <span>Pricing</span></h1>
    <p>Simple, flat-fee pricing for residential cost segregation studies. No hidden costs, no surprise invoices.</p>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="pricing-grid">
      <div class="pricing-card fade-in-up">
        <h3>Single Property</h3>
        <div class="pricing-amount">$3,500</div>
        <p style="color:var(--text-muted); margin-bottom:24px;">Ideal for individual STR or LTR investors</p>
        <ul class="pricing-features">
          <li>Full engineering-based study</li>
          <li>IRS audit-ready documentation</li>
          <li>14-day delivery</li>
          <li>CPA coordination included</li>
          <li>Form 3115 guidance if applicable</li>
          <li>Unlimited support</li>
        </ul>
        <a href="../free-estimate/index.html" class="btn btn-outline" style="width:100%;">Get Started</a>
      </div>
      <div class="pricing-card featured fade-in-up">
        <h3>Portfolio (3-5 Properties)</h3>
        <div class="pricing-amount">$2,900<span style="font-size:1rem; color:var(--text-muted);">/each</span></div>
        <p style="color:var(--text-muted); margin-bottom:24px;">Best value for growing portfolios</p>
        <ul class="pricing-features">
          <li>Everything in Single Property</li>
          <li>Portfolio-level depreciation strategy</li>
          <li>Priority 10-day delivery</li>
          <li>Dedicated account manager</li>
          <li>Batch processing efficiency</li>
          <li>CPA strategy call included</li>
        </ul>
        <a href="../free-estimate/index.html" class="btn btn-gold" style="width:100%;">Get Started</a>
      </div>
      <div class="pricing-card fade-in-up">
        <h3>Enterprise (6+ Properties)</h3>
        <div class="pricing-amount">Custom</div>
        <p style="color:var(--text-muted); margin-bottom:24px;">For large portfolios and partnerships</p>
        <ul class="pricing-features">
          <li>Everything in Portfolio</li>
          <li>Volume-based pricing</li>
          <li>7-day expedited delivery</li>
          <li>Dedicated engineering team</li>
          <li>Ongoing portfolio management</li>
          <li>Annual depreciation reviews</li>
        </ul>
        <a href="../contact/index.html" class="btn btn-outline" style="width:100%;">Contact Us</a>
      </div>
    </div>
  </div>
</section>
<section class="section section-alt">
  <div class="container" style="max-width:800px;">
    <h2 class="section-title">Frequently Asked About Pricing</h2>
    <p style="color:var(--text-muted); margin-bottom:20px; text-align:center;">The fee for a cost segregation study is tax-deductible as a business expense in the year it is incurred. For most rental property investors, the tax savings from a single cost segregation study exceed the cost of the study by 5x to 20x or more.</p>
    <p style="color:var(--text-muted); text-align:center;">A $3,500 study on a $400,000 property might identify $80,000 or more in accelerated deductions, resulting in $20,000 to $30,000 in tax savings, depending on your marginal rate. The return on investment is significant and immediate.</p>
  </div>
</section>
"""
    return wrap_page("Cost Segregation Pricing | Flat-Fee Studies Starting at $2,900",
        "Transparent, flat-fee pricing for residential cost segregation studies. Single property, portfolio, and enterprise plans available. Fee is tax-deductible.",
        body, depth=1, canonical_path="pricing/")


def generate_faq():
    faqs = [
        ("What is a cost segregation study?", "A cost segregation study is an engineering-based analysis that identifies and reclassifies components of a building from long-life real property (27.5 or 39 years) into shorter-life personal property (5, 7, or 15 years) for tax depreciation purposes. This accelerates your depreciation deductions, reducing your taxable income and improving cash flow in the early years of property ownership."),
        ("Who benefits from cost segregation?", "Any owner of residential rental property can benefit from a cost segregation study. Short-term rental investors (Airbnb, VRBO, vacation rentals) and long-term rental investors (traditional buy-and-hold) both qualify. The study is especially valuable for high-income investors, real estate professionals, and anyone looking to offset rental or active income with accelerated depreciation."),
        ("How much does a cost segregation study cost?", "Stratum offers flat-fee pricing starting at $3,500 for a single property study, with portfolio discounts available for investors with three or more properties. The fee is tax-deductible as a business expense, and the tax savings from the study typically exceed the cost by 5x to 20x."),
        ("How long does the process take?", "Our standard turnaround time is 14 business days from the date we receive all required documents. Portfolio clients receive priority delivery with 10-day turnaround, and enterprise clients can request expedited 7-day delivery."),
        ("Is cost segregation only for new properties?", "No. Cost segregation can be applied to properties purchased or placed in service at any time. If you have owned a property for years and never had a cost segregation study, you can file IRS Form 3115 (Change in Accounting Method) to claim all prior-year missed depreciation in a single tax year, without amending previous returns."),
        ("What is bonus depreciation?", "Bonus depreciation allows investors to deduct a significant percentage of the cost of 5, 7, and 15-year property in the first year the asset is placed in service, rather than spreading the deduction over the full recovery period. Bonus depreciation rates have been phasing down in recent years, making it important to conduct your study as soon as possible."),
        ("Do I need to physically inspect the property?", "No. Stratum uses a desktop analysis methodology that relies on property photographs, closing statements, appraisals, and public property records. This approach is accepted by the IRS and allows us to serve property investors in all 50 states without requiring an on-site visit."),
        ("What documents do I need to provide?", "You will need to provide your closing statement (HUD-1 or closing disclosure), property photographs (interior and exterior), and any renovation invoices if applicable. Listing photos from the purchase are typically sufficient. We also need basic property details like the address, purchase price, and date placed in service."),
        ("Will a cost segregation study trigger an IRS audit?", "No. A cost segregation study does not increase your audit risk. In fact, a properly conducted engineering-based study provides the documentation and methodology the IRS expects to see if your return is ever examined. Our studies are built to withstand IRS scrutiny."),
        ("What is Form 3115?", "Form 3115 is the IRS Application for Change in Accounting Method. It is used to retroactively apply cost segregation to a property that was previously depreciated using the straight-line method. This allows you to claim all missed accelerated depreciation from prior years in a single tax year, creating a large deduction without needing to amend previous tax returns."),
        ("Can I use cost segregation on a property I am renovating?", "Yes. If you are renovating a rental property, a cost segregation study can be conducted on both the original property and the renovation costs. Additionally, a partial asset disposition study can identify components being replaced, allowing you to write off their remaining book value in the year of renovation."),
        ("What types of property components are reclassified?", "Common components reclassified into shorter recovery periods include appliances, carpeting, cabinetry, countertops, specialty lighting, window treatments, security systems, landscaping, driveways, patios, fencing, outdoor lighting, and decorative fixtures. The specific components vary by property type and features."),
        ("How does cost segregation work with passive activity rules?", "Rental income is generally classified as passive, meaning deductions can only offset passive income. However, investors who qualify as Real Estate Professionals under IRC Section 469 can use passive losses to offset active income. Additionally, short-term rental properties with an average guest stay of seven days or less may be treated as non-passive if the owner materially participates."),
        ("Can my CPA do a cost segregation study?", "While CPAs are qualified to advise on the tax implications, a cost segregation study requires engineering expertise to identify and classify building components. The IRS expects cost segregation studies to be prepared by professionals with engineering or construction knowledge. Stratum works directly with your CPA to implement the study."),
        ("What is the minimum property value for cost segregation?", "We generally recommend cost segregation for properties with a purchase price of $150,000 or more (excluding land). Below this threshold, the study fee may not be justified by the tax savings. However, portfolio investors with multiple lower-value properties can still benefit from batch processing and portfolio-level strategies."),
        ("Do you serve all 50 states?", "Yes. Stratum Cost Segregation serves property investors in all 50 states. Our desktop analysis methodology allows us to deliver high-quality, IRS-compliant studies regardless of property location. We have completed studies in every major market and vacation rental destination in the country."),
        ("What happens after I receive my report?", "After receiving your cost segregation report, you or your CPA uses the asset classifications and depreciation schedules to file the appropriate forms with your tax return. For new properties, the accelerated depreciation is included on your current-year return. For existing properties, your CPA files Form 3115 to claim prior-year missed depreciation."),
        ("Is the cost segregation fee tax-deductible?", "Yes. The fee for a cost segregation study is fully tax-deductible as a business expense (investment expense) in the year it is paid. This further increases the return on investment of the study."),
        ("How much can I save with cost segregation?", "Savings vary based on property value, type, and your tax bracket. As a general rule, a cost segregation study can accelerate 20-40% of your property's depreciable basis into 5, 7, and 15-year categories. For a $400,000 property, this could mean $60,000 to $120,000 in first-year deductions, translating to $15,000 to $45,000 in tax savings depending on your marginal tax rate."),
        ("What makes Stratum different from other cost segregation firms?", "Stratum focuses exclusively on residential rental properties for STR and LTR investors. Our engineering-based methodology, 14-day turnaround, flat-fee pricing, and IRS audit-ready documentation set us apart. We also offer portfolio pricing, CPA coordination, and Form 3115 guidance as standard inclusions with every study."),
    ]

    faq_schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in faqs
        ]
    }
    schema_tag = f'<script type="application/ld+json">{json.dumps(faq_schema)}</script>'

    faq_html = ""
    for q, a in faqs:
        faq_html += f"""
    <div class="faq-item">
      <div class="faq-q">{q}<span class="faq-arrow">&#9660;</span></div>
      <div class="faq-a">{a}</div>
    </div>"""

    body = f"""
<section class="hero" style="padding-bottom:60px;">
  <div class="container">
    <h1>Frequently Asked <span>Questions</span></h1>
    <p>Everything you need to know about cost segregation studies for residential rental properties.</p>
  </div>
</section>
<section class="section">
  <div class="container" style="max-width:800px;">
    {faq_html}
  </div>
</section>
<section class="section section-alt">
  <div class="container">
{get_cta_banner(1)}
  </div>
</section>
"""
    return wrap_page("Cost Segregation FAQ | 20 Common Questions Answered",
        "Get answers to 20 frequently asked questions about cost segregation studies for rental properties, including pricing, process, benefits, and IRS compliance.",
        body, depth=1, schema=schema_tag, canonical_path="faq/")


def generate_contact():
    body = """
<section class="hero" style="padding-bottom:60px;">
  <div class="container">
    <h1>Contact <span>Stratum</span></h1>
    <p>Have questions about cost segregation for your rental property? We are here to help.</p>
  </div>
</section>
<section class="section">
  <div class="container" style="max-width:700px;">
    <div class="card" style="padding:40px;">
      <form action="#" method="POST">
        <div class="form-row">
          <div class="form-group">
            <label>First Name</label>
            <input type="text" name="first_name" required>
          </div>
          <div class="form-group">
            <label>Last Name</label>
            <input type="text" name="last_name" required>
          </div>
        </div>
        <div class="form-row">
          <div class="form-group">
            <label>Email</label>
            <input type="email" name="email" required>
          </div>
          <div class="form-group">
            <label>Phone</label>
            <input type="tel" name="phone">
          </div>
        </div>
        <div class="form-group">
          <label>Subject</label>
          <select name="subject">
            <option>Cost Segregation Inquiry</option>
            <option>Pricing Question</option>
            <option>CPA Partnership</option>
            <option>Portfolio Study</option>
            <option>Other</option>
          </select>
        </div>
        <div class="form-group">
          <label>Message</label>
          <textarea name="message" rows="5" required></textarea>
        </div>
        <button type="submit" class="btn btn-gold" style="width:100%;">Send Message</button>
      </form>
    </div>
    <div style="text-align:center; margin-top:40px;">
      <p style="color:var(--text-muted); margin-bottom:8px;">Or reach us directly:</p>
      <p style="color:var(--gold); font-size:1.1rem; font-weight:600;">{PHONE}</p>
      <p><a href="mailto:{EMAIL}" style="color:var(--gold);">{EMAIL}</a></p>
    </div>
  </div>
</section>
"""
    return wrap_page("Contact Stratum Cost Segregation | Get in Touch",
        "Contact Stratum Cost Segregation for questions about our residential cost segregation studies, pricing, or CPA partnership program.",
        body, depth=1, canonical_path="contact/")


def generate_blog_index():
    posts = get_blog_posts()
    cards = ""
    for slug, title, desc, date in posts:
        cards += f"""
      <a href="{slug}/index.html" class="blog-card" style="text-decoration:none;">
        <div class="blog-card-body">
          <div class="meta">{date}</div>
          <h3>{title}</h3>
          <p>{desc}</p>
        </div>
      </a>"""

    body = f"""
<section class="hero" style="padding-bottom:60px;">
  <div class="container">
    <h1>Cost Segregation <span>Blog</span></h1>
    <p>Expert insights, guides, and strategies for rental property investors looking to maximize tax savings through cost segregation.</p>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="blog-grid">
      {cards}
    </div>
  </div>
</section>
"""
    return wrap_page("Cost Segregation Blog | Expert Tax Guides for Rental Property Investors",
        "Read expert guides and articles about cost segregation for rental properties, STR tax strategies, bonus depreciation, and more.",
        body, depth=1, canonical_path="blog/")


def generate_reviews():
    reviews = [
        ("Our cost segregation study identified over $120,000 in accelerated deductions on a $450,000 vacation rental. The tax savings in year one alone were more than 10x the cost of the study.", "Michael T.", "Airbnb Investor, Nashville TN", 5),
        ("Stratum made the entire process effortless. I sent my closing docs and photos, and two weeks later had a comprehensive report my CPA was able to file immediately.", "Sarah K.", "STR Investor, Scottsdale AZ", 5),
        ("I had owned my rental for three years before discovering cost segregation. Stratum did a look-back study and I claimed all three years of missed depreciation in one shot. Game changer.", "David R.", "LTR Investor, Austin TX", 5),
        ("As a CPA, I refer all my real estate clients to Stratum. Their reports are thorough, well-documented, and formatted exactly how I need them for filing. Great to work with.", "Jennifer L., CPA", "Tax Professional, Denver CO", 5),
        ("Five properties across three states and Stratum handled all of them in a single engagement. The portfolio pricing saved me thousands compared to getting individual studies.", "Robert M.", "Portfolio Investor, Charlotte NC", 5),
        ("I was skeptical about desktop cost segregation studies, but the level of detail in my Stratum report was impressive. Every component was individually identified and classified.", "Amanda W.", "VRBO Host, Destin FL", 5),
        ("The Form 3115 look-back study was the best financial decision I made all year. Recovered four years of missed depreciation in one tax filing. Highly recommend.", "Chris P.", "Real Estate Investor, Pittsburgh PA", 5),
        ("Fast turnaround, fair pricing, and a report that my CPA said was one of the best-documented studies he had ever seen. Will use Stratum again for my next purchase.", "Lisa H.", "STR Investor, Gatlinburg TN", 5),
    ]

    review_schema = {
        "@context": "https://schema.org",
        "@type": "LocalBusiness",
        "name": SITE_NAME,
        "aggregateRating": {
            "@type": "AggregateRating",
            "ratingValue": "4.9",
            "reviewCount": str(len(reviews)),
            "bestRating": "5",
            "worstRating": "1"
        }
    }
    schema_tag = f'<script type="application/ld+json">{json.dumps(review_schema)}</script>'

    review_cards = ""
    for text, name, loc, stars in reviews:
        star_str = "&#9733;" * stars
        # Get initials for avatar circle
        initials = "".join([part[0] for part in name.replace(",", "").split()[:2]])
        review_cards += f"""
      <div class="review-card fade-in-up">
        <div class="review-stars">{star_str}</div>
        <p class="review-text">&ldquo;{text}&rdquo;</p>
        <div style="display:flex;align-items:center;gap:14px;">
          <div style="width:44px;height:44px;border-radius:50%;background:linear-gradient(135deg,rgba(200,160,82,0.2),rgba(200,160,82,0.05));border:1px solid rgba(200,160,82,0.2);display:flex;align-items:center;justify-content:center;color:var(--gold);font-weight:700;font-size:0.85rem;flex-shrink:0;">{initials}</div>
          <div>
            <p class="review-author">{name}</p>
            <p class="review-location">{loc}</p>
          </div>
        </div>
      </div>"""

    body = f"""
<section class="hero" style="padding-bottom:60px;">
  <div class="container">
    <h1>Client <span>Reviews</span></h1>
    <p>See what rental property investors and CPAs are saying about Stratum Cost Segregation.</p>
  </div>
</section>
<section class="section">
  <div class="container">
    <div style="text-align:center; margin-bottom:48px;">
      <div class="stat-num">4.9/5.0</div>
      <div style="color:var(--gold); font-size:1.5rem; margin:8px 0;">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
      <div class="stat-label">Based on {len(reviews)} verified client reviews</div>
    </div>
    <div class="card-grid">
      {review_cards}
    </div>
  </div>
</section>
<section class="section section-alt">
  <div class="container">
{get_cta_banner(1)}
  </div>
</section>
"""
    return wrap_page("Stratum Cost Segregation Reviews | Client Testimonials",
        "Read verified client reviews and testimonials about Stratum Cost Segregation studies for rental properties. 4.9/5.0 average rating.",
        body, depth=1, schema=schema_tag, canonical_path="reviews/")


def generate_free_estimate():
    body = f"""
<section class="hero" style="padding-bottom:60px;">
  <div class="container">
    <h1>Get Your <span>Free Estimate</span></h1>
    <p>Find out how much you could save with a cost segregation study on your rental property. No obligation, no pressure.</p>
  </div>
</section>
<section class="section">
  <div class="container" style="max-width:700px;">
    <div class="card" style="padding:40px;">
      <h2 style="color:var(--white); font-size:1.4rem; margin-bottom:24px; text-align:center;">Property Information</h2>
      <form action="#" method="POST">
        <div class="form-row">
          <div class="form-group">
            <label>First Name *</label>
            <input type="text" name="first_name" required>
          </div>
          <div class="form-group">
            <label>Last Name *</label>
            <input type="text" name="last_name" required>
          </div>
        </div>
        <div class="form-row">
          <div class="form-group">
            <label>Email *</label>
            <input type="email" name="email" required>
          </div>
          <div class="form-group">
            <label>Phone</label>
            <input type="tel" name="phone">
          </div>
        </div>
        <div class="form-group">
          <label>Property Address *</label>
          <input type="text" name="address" required>
        </div>
        <div class="form-row">
          <div class="form-group">
            <label>Purchase Price *</label>
            <input type="text" name="price" placeholder="$" required>
          </div>
          <div class="form-group">
            <label>Date Placed in Service</label>
            <input type="date" name="service_date">
          </div>
        </div>
        <div class="form-row">
          <div class="form-group">
            <label>Property Type *</label>
            <select name="property_type" required>
              <option value="">Select...</option>
              <option>Short-Term Rental (Airbnb/VRBO)</option>
              <option>Long-Term Rental</option>
              <option>Mixed Use</option>
              <option>Multi-Family (2-4 Units)</option>
            </select>
          </div>
          <div class="form-group">
            <label>Number of Properties</label>
            <select name="num_properties">
              <option>1</option>
              <option>2</option>
              <option>3-5</option>
              <option>6-10</option>
              <option>10+</option>
            </select>
          </div>
        </div>
        <div class="form-group">
          <label>Additional Notes</label>
          <textarea name="notes" rows="3" placeholder="Any renovations, special features, or questions..."></textarea>
        </div>
        <button type="submit" class="btn btn-gold" style="width:100%;">Get My Free Estimate</button>
        <p style="text-align:center; color:var(--text-muted); font-size:0.85rem; margin-top:12px;">We typically respond within 1 business day.</p>
      </form>
    </div>
  </div>
</section>
"""
    return wrap_page("Free Cost Segregation Estimate | No Obligation",
        "Get a free, no-obligation estimate for your rental property cost segregation study. Find out how much you could save in tax deductions.",
        body, depth=1, canonical_path="free-estimate/")


# ============================================================
# BLOG POSTS
# ============================================================
def get_blog_posts():
    return [
        ("what-is-cost-segregation", "What Is Cost Segregation? A Complete Guide for Rental Property Investors",
         "Learn what cost segregation is, how it works, and why rental property investors use it to accelerate depreciation deductions and reduce taxes.", "April 2026"),
        ("cost-segregation-airbnb-properties", "Cost Segregation for Airbnb Properties: How STR Investors Save Thousands",
         "Discover how Airbnb and short-term rental investors use cost segregation studies to unlock massive first-year tax deductions.", "April 2026"),
        ("residential-vs-commercial-cost-segregation", "Residential vs. Commercial Cost Segregation: Key Differences Explained",
         "Understand the differences between residential and commercial cost segregation studies, including depreciation periods and eligible components.", "March 2026"),
        ("cost-segregation-study-cost-pricing", "How Much Does a Cost Segregation Study Cost? Pricing Guide",
         "A transparent breakdown of cost segregation study pricing, what affects the cost, and how to evaluate the return on investment.", "March 2026"),
        ("signs-rental-property-needs-cost-segregation", "5 Signs Your Rental Property Needs a Cost Segregation Study",
         "Not sure if cost segregation is right for your rental? Here are five clear indicators that you are leaving money on the table.", "February 2026"),
        ("cost-segregation-str-tax-loophole", "The STR Tax Strategy: How Short-Term Rental Investors Use Cost Segregation",
         "An in-depth look at the short-term rental tax strategy and how cost segregation plays a central role in reducing taxable income.", "February 2026"),
        ("bonus-depreciation-2026-rental-property", "Bonus Depreciation in 2026: What Rental Property Investors Need to Know",
         "Stay current on bonus depreciation rates, phase-down schedules, and what it means for your cost segregation study timing.", "January 2026"),
        ("how-to-choose-cost-segregation-company", "How to Choose the Right Cost Segregation Company",
         "What to look for in a cost segregation provider, red flags to avoid, and questions to ask before committing to a study.", "January 2026"),
        ("cost-segregation-case-study-vacation-rental", "Cost Segregation Case Study: $520K Vacation Rental in Gatlinburg",
         "A real-world case study showing how a Gatlinburg vacation rental investor saved over $45,000 in taxes through cost segregation.", "December 2025"),
        ("form-3115-look-back-cost-segregation", "Form 3115 and Look-Back Cost Segregation: Claim Missed Depreciation",
         "Learn how to use IRS Form 3115 to retroactively apply cost segregation and claim years of missed accelerated depreciation.", "December 2025"),
    ]


def generate_blog_post(slug, title, desc, date):
    """Generate unique, detailed content for each blog post."""
    articles = {
        "what-is-cost-segregation": f"""
    <h2>Understanding Cost Segregation</h2>
    <p>Cost segregation is an IRS-approved tax strategy that allows property owners to accelerate depreciation deductions on their real estate investments. Instead of depreciating an entire building over 27.5 years (residential) or 39 years (commercial), a cost segregation study identifies specific building components that can be reclassified into shorter depreciation categories of 5, 7, and 15 years.</p>
    <p>The concept is rooted in the idea that a building is not a single asset. It is a collection of hundreds of individual components, each with a different useful life. Appliances wear out faster than walls. Landscaping deteriorates faster than a foundation. Cost segregation recognizes these differences and applies the correct depreciation timeline to each component.</p>

    <h2>How Cost Segregation Works for Rental Properties</h2>
    <p>For rental property investors, cost segregation is one of the most powerful tax planning tools available. Here is a simplified example of how it works:</p>
    <p>An investor purchases a single-family rental property for $400,000. After allocating $80,000 to land (which is not depreciable), the remaining $320,000 represents the depreciable cost basis of the building. Under standard straight-line depreciation, the investor would deduct approximately $11,636 per year for 27.5 years.</p>
    <p>With a cost segregation study, the analysis might identify $96,000 in 5-year property (appliances, carpeting, specialty lighting, window treatments), $16,000 in 7-year property (furniture, security systems), and $32,000 in 15-year property (landscaping, driveways, patios). The remaining $176,000 stays at 27.5-year property.</p>
    <p>Combined with bonus depreciation, the investor could potentially deduct $100,000 or more in the first year, compared to $11,636 under straight-line depreciation. The difference is substantial and can dramatically reduce or eliminate tax liability in the year of acquisition.</p>

    <h2>Who Should Consider Cost Segregation?</h2>
    <p>Cost segregation is appropriate for a wide range of real estate investors, but it provides the most benefit to owners of properties with a depreciable basis above $150,000, investors in high marginal tax brackets (32% or above), real estate professionals who can use passive losses against active income, short-term rental owners who materially participate and qualify for the STR exception, and investors planning to hold the property for the long term.</p>
    <p>The study is not limited to newly purchased properties. Investors who have owned a property for years can conduct a look-back study and file IRS Form 3115 to claim all missed accelerated depreciation in a single tax year.</p>

    <h2>The Engineering Behind Cost Segregation</h2>
    <p>A legitimate cost segregation study requires engineering expertise to identify and classify building components. The IRS Cost Segregation Audit Techniques Guide outlines the methodology and documentation standards expected in a quality study. This includes a detailed asset listing with component descriptions, cost allocations based on engineering estimates, MACRS class life assignments per Revenue Procedure 87-56, supporting photographs and property documentation, and a clear explanation of the methodology used.</p>
    <p>Studies that rely solely on percentage-based estimates without component-level analysis are more vulnerable to IRS challenge. Stratum's engineering-based approach meets the highest standards for documentation and audit defense.</p>

    <h2>Cost Segregation and Your Tax Return</h2>
    <p>After receiving your cost segregation report, your CPA or tax preparer uses the asset classifications and depreciation schedules to file the appropriate depreciation forms with your tax return. For properties placed in service in the current tax year, the accelerated depreciation is included on your current return. For properties placed in service in prior years, your CPA files Form 3115 to implement the change in accounting method.</p>
    <p>The result is a significant reduction in taxable income in the year the study is implemented, improving your after-tax cash flow and return on investment.</p>
""",
        "cost-segregation-airbnb-properties": f"""
    <h2>Why Airbnb Investors Need Cost Segregation</h2>
    <p>Airbnb and short-term rental investing has exploded in popularity over the past decade. Alongside the revenue potential, one of the most compelling reasons investors enter the STR market is the unique tax advantages available to short-term rental property owners, with cost segregation sitting at the center of the strategy.</p>
    <p>When you purchase a vacation rental or Airbnb property, the IRS allows you to depreciate the building over 27.5 years. But a cost segregation study can reclassify 25-40% of the building's cost basis into accelerated depreciation categories, generating significantly larger deductions in the early years of ownership.</p>

    <h2>The STR Tax Advantage</h2>
    <p>Short-term rentals with an average guest stay of seven days or less receive special treatment under the tax code. If the owner materially participates in the rental activity, the income is treated as non-passive under Treasury Regulation 1.469-1T(e)(3)(ii). This is a critical distinction because it means the depreciation deductions from a cost segregation study can be used to offset W-2 wages, business income, and other active income sources.</p>
    <p>For a high-income professional earning $300,000 per year in W-2 income, purchasing a $500,000 Airbnb property and conducting a cost segregation study could generate $100,000 or more in first-year deductions, reducing their taxable income to $200,000 and saving $30,000 to $40,000 in federal taxes alone.</p>

    <h2>Material Participation Requirements</h2>
    <p>To qualify for the STR tax exception, the property owner must demonstrate material participation in the rental activity. The IRS provides seven tests for material participation, the most commonly used being the 100-hour test (participating more than 100 hours and more than any other individual) or the 500-hour test (participating more than 500 hours during the tax year).</p>
    <p>Activities that count toward material participation include managing the listing, responding to guest inquiries, coordinating cleanings, handling maintenance, and managing the property financials. Many STR investors easily meet these thresholds through normal property management activities.</p>

    <h2>What Gets Reclassified on an Airbnb Property</h2>
    <p>Vacation rental properties often contain a higher percentage of personal property and land improvements than traditional long-term rentals, making them especially well-suited for cost segregation. Common reclassified components include all furniture and furnishings (beds, sofas, tables, chairs), kitchen appliances and specialty equipment, hot tubs, fire pits, and outdoor entertainment areas, decorative lighting and smart home technology, landscaping, patios, driveways, and walkways, window treatments, artwork, and decor, and security cameras and keyless entry systems.</p>
    <p>A well-furnished Airbnb property can have 30-40% of its cost basis reclassified into 5, 7, and 15-year property, creating substantial first-year deductions when combined with bonus depreciation.</p>

    <h2>Timing Your Cost Segregation Study</h2>
    <p>The timing of your cost segregation study matters. Bonus depreciation rates have been phasing down, which means the earlier you conduct your study, the more you can deduct in the first year. Additionally, if you placed your property in service earlier this year or in prior years, a look-back study with Form 3115 allows you to capture the full benefit retroactively.</p>
    <p>Stratum delivers completed studies within 14 business days, ensuring you have your report in time for tax filing deadlines.</p>
""",
        "residential-vs-commercial-cost-segregation": f"""
    <h2>Understanding the Difference</h2>
    <p>Cost segregation is available for both residential and commercial properties, but there are important differences in how the studies are conducted and the resulting tax benefits. Understanding these differences is essential for real estate investors evaluating whether cost segregation makes sense for their specific property type.</p>

    <h2>Depreciation Periods</h2>
    <p>The most fundamental difference is the base depreciation period. Residential rental properties are depreciated over 27.5 years using the straight-line method under MACRS. Commercial properties are depreciated over 39 years. This means commercial property owners are spreading their depreciation over a longer period, making cost segregation even more impactful for commercial buildings in terms of the time-value benefit.</p>
    <p>However, residential properties often have a higher percentage of components eligible for reclassification, particularly fully furnished vacation rentals where furniture, appliances, and decor represent a significant portion of the property's value.</p>

    <h2>Eligible Components</h2>
    <p>Both residential and commercial properties contain components eligible for reclassification into 5, 7, and 15-year categories. Residential properties typically yield reclassification rates of 20-40% of the depreciable basis, while commercial properties can range from 15-35% depending on the property type and build-out.</p>
    <p>Residential-specific components often include carpeting, appliances, window treatments, cabinetry, countertops, decorative fixtures, landscaping, and outdoor improvements. Commercial properties may additionally include specialized electrical and plumbing systems, tenant improvement build-outs, signage, parking lots, and specialized HVAC configurations.</p>

    <h2>Tax Treatment Differences</h2>
    <p>The tax treatment of depreciation deductions also differs. Residential rental income is classified as passive income for most investors, with deductions limited to offsetting passive income unless the investor qualifies as a Real Estate Professional or meets the STR exception. Commercial property owners face similar passive activity limitations but may have different strategies available for utilizing the deductions.</p>
    <p>Both residential and commercial cost segregation studies qualify for bonus depreciation on 5, 7, and 15-year property, subject to the current phase-down schedule.</p>

    <h2>Study Methodology</h2>
    <p>The engineering methodology is similar for both property types, but commercial studies often require more detailed analysis due to the complexity of commercial building systems. Residential studies can often be completed using desktop analysis with property photographs and documents, while large commercial properties may warrant on-site inspections for optimal accuracy.</p>
    <p>Stratum specializes in residential cost segregation, delivering focused expertise and efficient pricing for STR and LTR investors.</p>

    <h2>Which Is Right for You?</h2>
    <p>If you own residential rental property, whether short-term or long-term, a residential cost segregation study from Stratum is the right choice. Our studies are tailored to the specific components and tax considerations of residential real estate, with pricing and turnaround optimized for individual and portfolio investors.</p>
""",
        "cost-segregation-study-cost-pricing": f"""
    <h2>What Determines the Cost of a Study?</h2>
    <p>The cost of a cost segregation study varies based on several factors, including property value, property type, the complexity of the building, and the provider you choose. Understanding these factors helps you evaluate pricing and make an informed decision.</p>
    <p>Property value is the primary driver. Larger, more valuable properties have more components to identify and classify, requiring more engineering analysis. Property type matters as well: a fully furnished vacation rental with extensive outdoor improvements will have more reclassifiable components than a basic unfurnished rental, potentially requiring more detailed analysis.</p>

    <h2>Typical Pricing Ranges</h2>
    <p>For residential rental properties, cost segregation studies typically range from $2,500 to $5,000 for a single property. Some providers charge based on a percentage of the property value, while others (like Stratum) use flat-fee pricing for transparency and predictability.</p>
    <p>Stratum's pricing is straightforward: $3,500 for a single property study, $2,900 per property for portfolios of 3-5 properties, and custom pricing for enterprise clients with 6 or more properties. There are no hidden fees, no hourly charges, and no surprise invoices.</p>

    <h2>Evaluating Return on Investment</h2>
    <p>The critical question is not how much the study costs, but how much it saves. For a $400,000 rental property, a cost segregation study might identify $80,000 to $120,000 in accelerated deductions. At a 32% marginal tax rate, that translates to $25,000 to $38,000 in tax savings. Even at the lowest end, the return on a $3,500 study is more than 7x.</p>
    <p>The study fee itself is tax-deductible as a business expense, further improving the economics. When you factor in the time value of money and the ability to reinvest the tax savings, the return on investment is compelling for virtually any residential property above $150,000 in value.</p>

    <h2>Red Flags in Pricing</h2>
    <p>Be cautious of cost segregation providers who charge very low fees ($500-$1,500) for what they claim is a full engineering study. These are often template-based reports that use percentage estimates rather than component-level analysis. They may not withstand IRS scrutiny and could create problems if your return is examined.</p>
    <p>On the other end, be wary of providers who charge premium fees ($7,000-$15,000) for residential properties without clear justification. Unless the property is highly complex or valued above $1 million, residential studies should not require that level of investment.</p>

    <h2>Making the Decision</h2>
    <p>If your property has a depreciable basis above $150,000, the math almost always works in your favor. Request a free estimate from Stratum to see your specific potential savings before committing. We will provide a preliminary analysis at no cost so you can make an informed decision.</p>
""",
        "signs-rental-property-needs-cost-segregation": f"""
    <h2>Sign 1: You Purchased a Property Worth $200,000 or More</h2>
    <p>The most straightforward indicator is property value. If your rental property has a depreciable cost basis (purchase price minus land value) of $200,000 or more, a cost segregation study will almost certainly generate tax savings that far exceed the cost of the study. Even properties in the $150,000-$200,000 range can be strong candidates, depending on the property type and your tax situation.</p>
    <p>The higher the property value, the larger the potential benefit. A $500,000 property can yield $100,000 or more in accelerated deductions, while a $1 million property can generate $200,000+ in first-year deductions when combined with bonus depreciation.</p>

    <h2>Sign 2: You Are in a High Tax Bracket</h2>
    <p>Cost segregation creates tax deductions, and the value of a deduction depends on your marginal tax rate. If you are in the 32%, 35%, or 37% federal bracket, every dollar of accelerated depreciation saves you $0.32 to $0.37 in federal taxes alone. Add state income taxes and the savings can be even more significant.</p>
    <p>High-income professionals, business owners, and dual-income households are ideal candidates for cost segregation because the deductions offset income that would otherwise be taxed at the highest rates.</p>

    <h2>Sign 3: Your Property Is Fully Furnished</h2>
    <p>Furnished properties, especially short-term rentals, contain a significantly higher percentage of components eligible for accelerated depreciation. Furniture, appliances, decor, electronics, hot tubs, outdoor entertainment areas, and specialty fixtures are all classified as 5 or 7-year property. A fully furnished vacation rental can have 30-40% of its cost basis reclassified, compared to 20-25% for an unfurnished long-term rental.</p>

    <h2>Sign 4: You Have Owned the Property for Multiple Years Without a Study</h2>
    <p>If you purchased your rental property years ago and have been depreciating it straight-line without a cost segregation study, you have been leaving money on the table every year. The good news is that a look-back study allows you to claim all missed accelerated depreciation from prior years in a single tax year using IRS Form 3115, without needing to amend previous returns.</p>
    <p>The longer you have owned the property without a study, the larger the catch-up deduction will be. An investor who has owned a $400,000 property for five years without a cost segregation study might claim $50,000 to $80,000 in previously unclaimed accelerated depreciation in a single year.</p>

    <h2>Sign 5: You Plan to Buy More Properties</h2>
    <p>If you are building a rental property portfolio, establishing a cost segregation strategy from the beginning sets you up for long-term tax efficiency. By conducting studies on each property as you acquire it, you create a systematic approach to maximizing deductions and managing your overall tax liability. Portfolio investors also benefit from volume pricing, making each individual study more cost-effective.</p>
""",
        "cost-segregation-str-tax-loophole": f"""
    <h2>What Is the STR Tax Strategy?</h2>
    <p>The short-term rental tax strategy is one of the most discussed tax planning approaches in real estate investing. It combines three elements: purchasing a short-term rental property, conducting a cost segregation study, and leveraging the IRS treatment of STR income to use accelerated depreciation against active income. It is not a loophole in the traditional sense; it is a legal application of existing tax code provisions that the IRS has acknowledged and addressed in its regulations.</p>

    <h2>How the Strategy Works</h2>
    <p>Under IRC Section 469, rental activities are generally treated as passive, meaning losses from rental properties can only offset passive income. However, Treasury Regulation 1.469-1T(e)(3)(ii) provides an exception for rental activities where the average customer use period is seven days or less. Short-term rentals that meet this definition are not treated as rental activities for passive loss purposes.</p>
    <p>When the STR is not treated as a rental activity and the owner materially participates, the income and losses are classified as non-passive. This means a paper loss generated by accelerated depreciation from a cost segregation study can offset W-2 wages, business income, and other active income sources.</p>

    <h2>The Numbers in Practice</h2>
    <p>Consider an investor earning $400,000 per year in W-2 income who purchases a $600,000 Airbnb property. After allocating $120,000 to land, the depreciable basis is $480,000. A cost segregation study identifies $144,000 in 5-year property, $24,000 in 7-year property, and $48,000 in 15-year property. Combined with bonus depreciation, the investor generates approximately $150,000 in first-year depreciation, plus the standard depreciation on the remaining 27.5-year property.</p>
    <p>Even after accounting for rental income and expenses, the investor might show a net tax loss of $80,000 to $120,000 on the STR. Because the property qualifies as non-passive, this loss offsets the investor's W-2 income, reducing taxable income from $400,000 to $280,000 to $320,000. At a 35% marginal rate, the tax savings can range from $28,000 to $42,000 in the first year alone.</p>

    <h2>Material Participation Requirements</h2>
    <p>The key to making this strategy work is material participation. The investor must meet one of the IRS's seven material participation tests. The most commonly used tests for STR investors are the 100-hour test (participating more than any other individual and more than 100 hours) and the 500-hour test (participating more than 500 hours during the year).</p>
    <p>Self-managing your Airbnb property, handling guest communications, coordinating cleanings, managing pricing, and overseeing maintenance all count toward material participation hours.</p>

    <h2>Important Considerations</h2>
    <p>While the strategy is legal and widely used, it requires careful implementation. Investors should maintain detailed records of their material participation hours, work with a CPA who understands the STR tax rules, and ensure their cost segregation study is prepared by a qualified provider with engineering methodology. Stratum Cost Segregation provides the engineering-based study that forms the foundation of this strategy.</p>
""",
        "bonus-depreciation-2026-rental-property": f"""
    <h2>The Current State of Bonus Depreciation</h2>
    <p>Bonus depreciation has been one of the most powerful tax incentives for real estate investors in recent years. Under the Tax Cuts and Jobs Act of 2017, 100% bonus depreciation was available for qualified property placed in service from September 2017 through 2022. Since then, the rate has been phasing down, and understanding the current rules is essential for investors planning their cost segregation strategy in 2026.</p>

    <h2>Phase-Down Schedule</h2>
    <p>The bonus depreciation rate has been decreasing by 20 percentage points each year. For property placed in service in 2023, the rate was 80%. In 2024, it dropped to 60%. In 2025, the rate is 40%. And in 2026, it is down to 20%. Without legislative action, bonus depreciation will be fully phased out for property placed in service after December 31, 2026.</p>
    <p>This phase-down makes timing critical. Every year you delay a cost segregation study, you lose access to a higher bonus depreciation rate on the 5, 7, and 15-year property identified in the study.</p>

    <h2>What This Means for 2026 Purchases</h2>
    <p>For a property purchased in 2026, a cost segregation study that identifies $120,000 in components eligible for bonus depreciation would allow the investor to deduct 20% of that amount ($24,000) as bonus depreciation in the first year. The remaining $96,000 would be depreciated over the applicable recovery periods (5, 7, or 15 years) using the standard MACRS tables.</p>
    <p>While 20% is significantly less than the 100% bonus depreciation available in earlier years, it still provides meaningful first-year acceleration compared to straight-line depreciation over 27.5 years. And the regular accelerated depreciation under MACRS (without bonus) continues to provide significant front-loading of deductions over the 5, 7, and 15-year recovery periods.</p>

    <h2>Legislative Outlook</h2>
    <p>There has been bipartisan interest in restoring higher bonus depreciation rates. Several proposals have been introduced in Congress to extend or restore 100% bonus depreciation, though none have been enacted as of the time of this writing. Investors should work with their tax advisors to monitor legislative developments and plan accordingly.</p>
    <p>Regardless of the bonus depreciation rate, cost segregation remains valuable because it reclassifies components from 27.5-year property into 5, 7, and 15-year property. Even without any bonus depreciation, the accelerated MACRS depreciation over these shorter periods provides significant tax benefits compared to straight-line depreciation.</p>

    <h2>Act Now</h2>
    <p>If you own rental property and have not yet conducted a cost segregation study, 2026 may be the last year to capture any bonus depreciation benefit. Stratum delivers studies within 14 business days, giving you time to implement the study before year-end deadlines.</p>
""",
        "how-to-choose-cost-segregation-company": f"""
    <h2>Engineering-Based vs. Estimate-Based Studies</h2>
    <p>The most important distinction among cost segregation providers is whether they perform engineering-based studies or estimate-based studies. An engineering-based study identifies and classifies individual building components using construction cost data, property inspection or photographs, and engineering judgment. An estimate-based study applies percentage assumptions to allocate costs without component-level analysis.</p>
    <p>The IRS Cost Segregation Audit Techniques Guide explicitly favors detailed, engineering-based methodologies. Studies that rely on percentages or templates without underlying component analysis are more susceptible to challenge during an audit. When choosing a provider, ask how they identify and classify individual components and whether the study includes a detailed asset listing.</p>

    <h2>Industry Specialization</h2>
    <p>Cost segregation firms range from large national companies that handle all property types to specialized firms focused on specific asset classes. For residential rental property investors, working with a firm that specializes in residential cost segregation offers several advantages. The firm will be more familiar with the specific components common to residential properties, the tax rules unique to STR and LTR investments, and the documentation standards that CPAs expect for residential filings.</p>
    <p>Stratum focuses exclusively on residential rental properties for STR and LTR investors, ensuring deep expertise in the specific property types our clients own.</p>

    <h2>Pricing Transparency</h2>
    <p>Look for a provider that offers clear, upfront pricing. Flat-fee pricing is preferable to percentage-based or hourly billing because you know exactly what the study will cost before you commit. Be wary of providers who are vague about pricing or who add fees for report delivery, CPA coordination, or Form 3115 guidance. These should be standard inclusions, not upsells.</p>

    <h2>Turnaround Time</h2>
    <p>Tax deadlines are real, and your cost segregation study needs to be completed before your CPA can file it with your return. Ask about standard turnaround time and whether expedited options are available. A reliable provider should be able to deliver a completed study within two to three weeks of receiving all required documents.</p>

    <h2>Audit Defense and Support</h2>
    <p>A cost segregation study is only as valuable as its ability to withstand IRS examination. Ask potential providers about their audit defense track record, the qualifications of their engineering staff, and what support they provide if your return is examined. A quality provider will stand behind their work and provide documentation and support in the event of an audit.</p>

    <h2>Questions to Ask Before Hiring</h2>
    <p>Before engaging a cost segregation provider, ask these key questions: Is the study prepared by licensed engineers or construction professionals? Does the study include a component-level asset listing? What is the standard turnaround time? Is the pricing flat-fee or variable? What documentation and support is provided for IRS audit defense? Does the fee include CPA coordination and Form 3115 guidance? How many residential studies has the firm completed? Can they provide references from other residential investors or CPAs?</p>
""",
        "cost-segregation-case-study-vacation-rental": f"""
    <h2>Property Overview</h2>
    <p>This case study examines a cost segregation analysis conducted for a vacation rental property located in Gatlinburg, Tennessee, one of the most popular short-term rental markets in the southeastern United States. The property was a four-bedroom, three-bathroom mountain cabin purchased for $520,000, with a land allocation of $78,000, resulting in a depreciable basis of $442,000.</p>
    <p>The property was purchased as a turnkey vacation rental, fully furnished and move-in ready for Airbnb and VRBO guests. It included a hot tub, game room, outdoor fire pit area, extensive landscaping, and premium interior finishes throughout.</p>

    <h2>Study Results</h2>
    <p>The Stratum cost segregation study identified the following reclassifications from 27.5-year property to shorter recovery periods:</p>
    <p>5-Year Personal Property: $92,820 (21.0% of depreciable basis). This included all furniture and furnishings, kitchen appliances, washer and dryer, hot tub, game room equipment, window treatments, decorative light fixtures, smart home technology, and all decor and accessories.</p>
    <p>7-Year Personal Property: $17,680 (4.0% of depreciable basis). This included specialty cabinetry, built-in entertainment systems, and security and camera systems.</p>
    <p>15-Year Land Improvements: $39,780 (9.0% of depreciable basis). This included landscaping, the gravel driveway, stone walkways, the outdoor fire pit and patio area, retaining walls, exterior lighting, and fencing.</p>
    <p>The remaining $291,720 (66.0%) was classified as 27.5-year real property, covering structural components such as the foundation, framing, roof, exterior walls, interior walls, plumbing, electrical, and HVAC systems.</p>

    <h2>Tax Savings Analysis</h2>
    <p>The total amount reclassified into accelerated categories was $150,280, representing 34.0% of the depreciable basis. With applicable bonus depreciation, the investor was able to claim substantially larger first-year deductions than would have been available under straight-line depreciation alone.</p>
    <p>Under straight-line depreciation, the annual deduction would have been approximately $16,073 ($442,000 divided by 27.5 years). With the cost segregation study, the first-year depreciation deduction was significantly higher, creating a paper loss that the investor used to offset active income under the STR tax exception.</p>
    <p>The investor's estimated first-year tax savings exceeded $45,000, representing a return of more than 12x the cost of the study. Over the first five years of ownership, the cumulative tax benefit was projected at approximately $65,000 in present-value terms.</p>

    <h2>Key Takeaways</h2>
    <p>This case study illustrates several important points for vacation rental investors. Fully furnished properties yield higher reclassification percentages due to the significant personal property content. The Gatlinburg market's typical cabin features, such as hot tubs, game rooms, and outdoor entertainment areas, provide substantial reclassifiable components. The STR tax exception allowed the investor to use the accelerated depreciation against active W-2 income. And the cost of the study was recovered many times over in the first year alone.</p>
""",
        "form-3115-look-back-cost-segregation": f"""
    <h2>What Is Form 3115?</h2>
    <p>IRS Form 3115, Application for Change in Accounting Method, is the mechanism that allows property owners to retroactively apply cost segregation to a property that has been depreciated using the straight-line method in prior years. It is one of the most powerful and underutilized tools in real estate tax planning.</p>
    <p>When you conduct a cost segregation study on a property you have owned for multiple years, Form 3115 allows you to claim all prior-year missed accelerated depreciation in a single tax year. This is called a Section 481(a) adjustment, and it does not require amending your previous tax returns. The entire catch-up amount is reported on your current-year return.</p>

    <h2>How the Look-Back Study Works</h2>
    <p>Here is a practical example. An investor purchased a rental property five years ago for $400,000 (with $320,000 in depreciable basis). For the past five years, the investor has been depreciating the property straight-line over 27.5 years, deducting approximately $11,636 per year.</p>
    <p>In year six, the investor commissions a cost segregation study. The study identifies $96,000 in 5-year property, $16,000 in 7-year property, and $32,000 in 15-year property. If the study had been conducted in year one, the investor would have claimed significantly larger deductions in years one through five through accelerated MACRS depreciation and bonus depreciation on these components.</p>
    <p>The Section 481(a) adjustment calculates the difference between what the investor actually deducted over the first five years (using straight-line on the entire building) and what the investor should have deducted (using accelerated depreciation on the reclassified components). This difference, which can amount to $50,000 to $100,000 or more depending on the property and the number of years, is claimed as a single deduction on the current-year tax return via Form 3115.</p>

    <h2>Advantages of the Look-Back Approach</h2>
    <p>The look-back study with Form 3115 offers several significant advantages. There is no need to amend prior-year returns, which saves time and complexity. The entire catch-up deduction is claimed in a single tax year, creating a large current-year benefit. The approach is explicitly sanctioned by the IRS through Revenue Procedure 2015-13 (as updated). And there is no statute of limitations issue because the change is implemented prospectively.</p>
    <p>For investors who have owned properties for three, five, or even ten years without a cost segregation study, the look-back approach often produces the largest single-year tax benefit of any strategy available.</p>

    <h2>Filing Requirements</h2>
    <p>Form 3115 must be filed with your current-year tax return and a copy must be sent to the IRS National Office. Your CPA handles the filing, using the detailed asset classifications and depreciation calculations from your Stratum cost segregation report. The change in accounting method is filed under the automatic consent procedures, meaning IRS approval is not required before filing.</p>
    <p>Stratum includes Form 3115 guidance and supporting calculations with every look-back study, ensuring your CPA has everything needed to file correctly.</p>

    <h2>Is a Look-Back Study Right for You?</h2>
    <p>If you own a rental property that you have been depreciating straight-line and have never had a cost segregation study, a look-back study is almost certainly worth pursuing. The longer you have owned the property, the larger the Section 481(a) adjustment will be, and the greater the current-year tax benefit.</p>
""",
    }

    content = articles.get(slug, "")
    body = f"""
<article class="article">
  <div class="breadcrumbs" style="padding:0; margin-bottom:24px;">
    <a href="../../index.html">Home</a> &raquo; <a href="../index.html">Blog</a> &raquo; <span>{title}</span>
  </div>
  <h1>{title}</h1>
  <div class="meta">{date} &middot; Stratum Cost Segregation</div>
  {content}
  {get_cta_banner(2)}
</article>
"""
    return wrap_page(f"{title} | Stratum Cost Segregation",
        desc, body, depth=2, canonical_path=f"blog/{slug}/")


# ============================================================
# CITY PAGES
# ============================================================
TIER1_CITIES = [
    ("New York", "NY"), ("Los Angeles", "CA"), ("Chicago", "IL"), ("Houston", "TX"),
    ("Phoenix", "AZ"), ("Philadelphia", "PA"), ("San Antonio", "TX"), ("San Diego", "CA"),
    ("Dallas", "TX"), ("Austin", "TX"), ("Jacksonville", "FL"), ("San Francisco", "CA"),
    ("Charlotte", "NC"), ("Indianapolis", "IN"), ("Seattle", "WA"), ("Denver", "CO"),
    ("Nashville", "TN"), ("Miami", "FL"), ("Atlanta", "GA"), ("Portland", "OR"),
    ("Las Vegas", "NV"), ("Memphis", "TN"), ("Louisville", "KY"), ("Baltimore", "MD"),
    ("Milwaukee", "WI"), ("Albuquerque", "NM"), ("Tucson", "AZ"), ("Fresno", "CA"),
    ("Sacramento", "CA"), ("Mesa", "AZ"), ("Kansas City", "MO"), ("Omaha", "NE"),
    ("Colorado Springs", "CO"), ("Raleigh", "NC"), ("Virginia Beach", "VA"),
    ("Minneapolis", "MN"), ("Tampa", "FL"), ("New Orleans", "LA"), ("Cleveland", "OH"),
    ("Pittsburgh", "PA"), ("Cincinnati", "OH"), ("St Louis", "MO"), ("Orlando", "FL"),
    ("San Jose", "CA"), ("Boise", "ID"), ("Salt Lake City", "UT"), ("Scottsdale", "AZ"),
    ("Savannah", "GA"), ("Charleston", "SC"), ("Asheville", "NC"),
]

TIER2_CITIES = [
    ("Gatlinburg", "TN"), ("Pigeon Forge", "TN"), ("Destin", "FL"), ("Panama City Beach", "FL"),
    ("Gulf Shores", "AL"), ("Myrtle Beach", "SC"), ("Hilton Head", "SC"), ("Outer Banks", "NC"),
    ("Cape Cod", "MA"), ("Poconos", "PA"), ("Branson", "MO"), ("Sedona", "AZ"),
    ("Joshua Tree", "CA"), ("Big Bear", "CA"), ("Lake Tahoe", "CA"), ("Mammoth Lakes", "CA"),
    ("Park City", "UT"), ("Steamboat Springs", "CO"), ("Breckenridge", "CO"), ("Vail", "CO"),
    ("Aspen", "CO"), ("Telluride", "CO"), ("Whitefish", "MT"), ("Coeur d Alene", "ID"),
    ("Bend", "OR"), ("Hood River", "OR"), ("Cannon Beach", "OR"), ("Leavenworth", "WA"),
    ("Chelan", "WA"), ("Suncadia", "WA"), ("Lake Geneva", "WI"), ("Door County", "WI"),
    ("Traverse City", "MI"), ("Mackinac Island", "MI"), ("Put in Bay", "OH"),
    ("Hocking Hills", "OH"), ("Deep Creek", "MD"), ("Shenandoah", "VA"), ("Broken Bow", "OK"),
    ("Fredericksburg", "TX"), ("Wimberley", "TX"), ("Galveston", "TX"),
    ("South Padre Island", "TX"), ("Pensacola", "FL"), ("Anna Maria Island", "FL"),
    ("Clearwater", "FL"), ("Key West", "FL"), ("Islamorada", "FL"), ("Marco Island", "FL"),
    ("Sanibel Island", "FL"),
]

# State full names
STATE_NAMES = {
    "AL": "Alabama", "AK": "Alaska", "AZ": "Arizona", "AR": "Arkansas", "CA": "California",
    "CO": "Colorado", "CT": "Connecticut", "DE": "Delaware", "FL": "Florida", "GA": "Georgia",
    "HI": "Hawaii", "ID": "Idaho", "IL": "Illinois", "IN": "Indiana", "IA": "Iowa",
    "KS": "Kansas", "KY": "Kentucky", "LA": "Louisiana", "MA": "Massachusetts", "MD": "Maryland",
    "ME": "Maine", "MI": "Michigan", "MN": "Minnesota", "MO": "Missouri", "MS": "Mississippi",
    "MT": "Montana", "NE": "Nebraska", "NV": "Nevada", "NH": "New Hampshire", "NJ": "New Jersey",
    "NM": "New Mexico", "NY": "New York", "NC": "North Carolina", "ND": "North Dakota",
    "OH": "Ohio", "OK": "Oklahoma", "OR": "Oregon", "PA": "Pennsylvania", "RI": "Rhode Island",
    "SC": "South Carolina", "SD": "South Dakota", "TN": "Tennessee", "TX": "Texas",
    "UT": "Utah", "VA": "Virginia", "VT": "Vermont", "WA": "Washington", "WI": "Wisconsin",
    "WV": "West Virginia", "WY": "Wyoming",
}

# Market details for unique city content
def get_city_details(city, state):
    """Return unique market-specific content for each city."""
    st = STATE_NAMES.get(state, state)
    slug = f"cost-segregation-{city.lower().replace(' ', '-')}-{state.lower()}"

    # Regional property data and market insights
    market_data = {
        # Tier 1 major cities
        "New York": {"median": "$680,000", "type": "multifamily brownstones and condos", "neighborhoods": "Brooklyn, Queens, Manhattan, Staten Island, and the Bronx", "str_note": "strict short-term rental regulations make long-term rental strategies particularly important for cost segregation", "growth": "consistent appreciation and dense housing stock"},
        "Los Angeles": {"median": "$920,000", "type": "single-family homes, duplexes, and ADU conversions", "neighborhoods": "Hollywood, Silver Lake, Venice, Downtown LA, and the San Fernando Valley", "str_note": "a major Airbnb market with city registration requirements for hosts", "growth": "one of the most valuable real estate markets in the nation"},
        "Chicago": {"median": "$320,000", "type": "multi-unit buildings, condos, and single-family rentals", "neighborhoods": "Lincoln Park, Wicker Park, Logan Square, Hyde Park, and Lakeview", "str_note": "a growing STR market with licensing requirements that favor compliant operators", "growth": "affordable entry points relative to coastal markets with strong rental demand"},
        "Houston": {"median": "$310,000", "type": "single-family homes and townhouses", "neighborhoods": "The Heights, Montrose, Midtown, Sugar Land, and Katy", "str_note": "no state income tax makes federal depreciation deductions even more impactful", "growth": "rapid population growth driving consistent rental demand"},
        "Phoenix": {"median": "$420,000", "type": "single-family homes and desert-style properties", "neighborhoods": "Scottsdale, Tempe, Mesa, Chandler, and Gilbert", "str_note": "a popular snowbird destination with strong winter STR demand", "growth": "one of the fastest-growing metro areas in the US"},
        "Philadelphia": {"median": "$280,000", "type": "row homes, duplexes, and converted multi-units", "neighborhoods": "Center City, Fishtown, Northern Liberties, Graduate Hospital, and Manayunk", "str_note": "growing Airbnb market with relatively affordable entry points for investors", "growth": "steady appreciation with strong university and medical center demand"},
        "San Antonio": {"median": "$275,000", "type": "single-family rentals and multi-family units", "neighborhoods": "Downtown, Alamo Heights, Stone Oak, Southtown, and Pearl District", "str_note": "tourism-driven STR demand near the Alamo and River Walk, no state income tax", "growth": "consistent military and healthcare employment driving housing demand"},
        "San Diego": {"median": "$880,000", "type": "coastal properties, condos, and single-family homes", "neighborhoods": "Pacific Beach, Mission Beach, North Park, La Jolla, and Hillcrest", "str_note": "premium beach market with high nightly rates and year-round demand", "growth": "military, biotech, and tourism supporting strong real estate fundamentals"},
        "Dallas": {"median": "$380,000", "type": "single-family homes, townhomes, and new construction", "neighborhoods": "Uptown, Deep Ellum, Bishop Arts, Preston Hollow, and Frisco", "str_note": "no state income tax and strong corporate relocation demand", "growth": "major corporate relocations driving population and housing growth"},
        "Austin": {"median": "$520,000", "type": "single-family homes, condos, and new builds", "neighborhoods": "East Austin, South Congress, Downtown, Zilker, and Cedar Park", "str_note": "one of the top STR markets in Texas with high tourism and tech worker demand", "growth": "tech industry growth has made Austin one of the hottest markets in the country"},
        "Jacksonville": {"median": "$310,000", "type": "single-family homes and beach properties", "neighborhoods": "Jacksonville Beach, Riverside, San Marco, Ponte Vedra, and Mandarin", "str_note": "affordable beach market with growing vacation rental demand", "growth": "largest city by land area in the continental US with diverse investment opportunities"},
        "San Francisco": {"median": "$1,200,000", "type": "Victorian homes, condos, and multi-unit buildings", "neighborhoods": "Mission District, SOMA, Pacific Heights, Noe Valley, and Hayes Valley", "str_note": "strict STR regulations but premium property values make cost seg highly valuable", "growth": "tech industry presence supports some of the highest property values in the nation"},
        "Charlotte": {"median": "$380,000", "type": "single-family homes and new construction communities", "neighborhoods": "South End, NoDa, Plaza Midwood, Dilworth, and Myers Park", "str_note": "growing financial sector and NASCAR events drive both LTR and STR demand", "growth": "banking industry hub with rapid population growth and new development"},
        "Indianapolis": {"median": "$240,000", "type": "single-family homes, duplexes, and multi-family units", "neighborhoods": "Broad Ripple, Fountain Square, Mass Ave, Carmel, and Fishers", "str_note": "major sporting events and conventions create consistent STR demand downtown", "growth": "affordable Midwest market with strong cash flow potential for investors"},
        "Seattle": {"median": "$780,000", "type": "single-family homes, condos, and ADU conversions", "neighborhoods": "Capitol Hill, Ballard, Fremont, Queen Anne, and West Seattle", "str_note": "tech worker demand and tourism create strong STR opportunities", "growth": "Amazon, Microsoft, and tech sector presence driving sustained demand"},
        "Denver": {"median": "$560,000", "type": "single-family homes, townhomes, and mountain-accessible properties", "neighborhoods": "LoDo, RiNo, Wash Park, Cherry Creek, and Capitol Hill", "str_note": "gateway to Colorado ski resorts and outdoor recreation driving tourism STR demand", "growth": "outdoor lifestyle and job growth making Denver one of the top relocation destinations"},
        "Nashville": {"median": "$430,000", "type": "single-family homes, condos, and bachelorette-party rentals", "neighborhoods": "East Nashville, The Gulch, 12 South, Germantown, and Sylvan Park", "str_note": "one of the top STR markets in the country with massive tourism demand", "growth": "music industry, healthcare, and tourism fueling consistent appreciation"},
        "Miami": {"median": "$580,000", "type": "condos, waterfront properties, and single-family homes", "neighborhoods": "Wynwood, Brickell, Coconut Grove, Little Havana, and Design District", "str_note": "international tourism destination with year-round STR demand", "growth": "influx of remote workers and international investment driving prices"},
        "Atlanta": {"median": "$380,000", "type": "single-family homes, townhomes, and bungalows", "neighborhoods": "Midtown, Buckhead, Old Fourth Ward, East Atlanta Village, and Decatur", "str_note": "major convention and film industry hub creating STR opportunities", "growth": "diverse economy with film, tech, and logistics sectors driving growth"},
        "Portland": {"median": "$500,000", "type": "craftsman homes, condos, and ADU-friendly properties", "neighborhoods": "Pearl District, Alberta, Hawthorne, Division, and Sellwood", "str_note": "eco-tourism and food scene driving vacation rental demand", "growth": "progressive city with strong rental market fundamentals"},
        "Las Vegas": {"median": "$400,000", "type": "single-family homes, condos, and resort-area properties", "neighborhoods": "Summerlin, Henderson, Downtown, Spring Valley, and the Strip corridor", "str_note": "massive tourism industry creates exceptional STR demand near the Strip", "growth": "entertainment capital with growing residential market beyond tourism"},
        "Memphis": {"median": "$195,000", "type": "single-family homes, duplexes, and historic properties", "neighborhoods": "Cooper-Young, Midtown, Downtown, Germantown, and Collierville", "str_note": "Beale Street and music tourism create niche STR opportunities", "growth": "affordable market with strong cash-on-cash returns for buy-and-hold investors"},
        "Louisville": {"median": "$230,000", "type": "shotgun houses, single-family homes, and historic properties", "neighborhoods": "The Highlands, NuLu, Germantown, Old Louisville, and St. Matthews", "str_note": "Kentucky Derby and bourbon tourism drive seasonal STR demand spikes", "growth": "revitalizing neighborhoods creating value-add investment opportunities"},
        "Baltimore": {"median": "$220,000", "type": "row homes, townhomes, and multi-unit conversions", "neighborhoods": "Federal Hill, Fells Point, Canton, Mt. Vernon, and Hampden", "str_note": "Inner Harbor tourism and Johns Hopkins medical demand create diverse rental options", "growth": "proximity to Washington DC and affordable prices attract commuter demand"},
        "Milwaukee": {"median": "$200,000", "type": "duplexes, multi-family homes, and single-family rentals", "neighborhoods": "Third Ward, Bay View, East Side, Walker's Point, and Tosa", "str_note": "festivals, breweries, and Bucks games create seasonal STR demand", "growth": "affordable Midwest market with improving downtown development"},
        "Albuquerque": {"median": "$310,000", "type": "adobe and pueblo-style homes and single-family rentals", "neighborhoods": "Nob Hill, Old Town, Downtown, Rio Rancho, and Corrales", "str_note": "Balloon Fiesta and cultural tourism create unique STR opportunities", "growth": "growing tech and film industry presence driving housing demand"},
        "Tucson": {"median": "$310,000", "type": "desert homes, casitas, and mid-century properties", "neighborhoods": "Sam Hughes, Armory Park, Catalina Foothills, Oro Valley, and Marana", "str_note": "snowbird and University of Arizona demand creating dual STR and LTR opportunities", "growth": "affordable desert market with growing retirement and remote worker migration"},
        "Fresno": {"median": "$360,000", "type": "single-family homes and agricultural area rentals", "neighborhoods": "Tower District, Woodward Park, Clovis, Fig Garden, and Old Town Clovis", "str_note": "gateway to Yosemite and Sierra Nevada recreation creating tourist STR demand", "growth": "Central Valley agriculture and proximity to national parks driving growth"},
        "Sacramento": {"median": "$480,000", "type": "single-family homes, Victorians, and new construction", "neighborhoods": "Midtown, East Sacramento, Land Park, Tahoe Park, and Folsom", "str_note": "state capital with growing tech overflow from the Bay Area", "growth": "Bay Area migration and remote work driving Sacramento real estate demand"},
        "Mesa": {"median": "$410,000", "type": "single-family homes and retirement community properties", "neighborhoods": "Downtown Mesa, Eastmark, Superstition Springs, Las Sendas, and Red Mountain", "str_note": "spring training baseball and desert tourism driving seasonal STR demand", "growth": "rapidly growing Phoenix suburb with diverse housing stock"},
        "Kansas City": {"median": "$250,000", "type": "single-family homes, duplexes, and historic properties", "neighborhoods": "Westport, Plaza, Brookside, Crossroads, and Waldo", "str_note": "BBQ tourism, sports events, and affordable entry points for STR investors", "growth": "affordable market with strong job growth and revitalizing neighborhoods"},
        "Omaha": {"median": "$240,000", "type": "single-family homes and multi-family properties", "neighborhoods": "Dundee, Benson, Midtown, Aksarben, and Blackstone", "str_note": "College World Series and Berkshire Hathaway events create STR demand spikes", "growth": "stable Midwest economy with consistent housing demand"},
        "Colorado Springs": {"median": "$440,000", "type": "single-family homes and mountain-view properties", "neighborhoods": "Old Colorado City, Broadmoor, Manitou Springs, Downtown, and Briargate", "str_note": "military bases, Garden of the Gods, and Pikes Peak tourism driving rental demand", "growth": "outdoor recreation hub with strong military and tech employment base"},
        "Raleigh": {"median": "$400,000", "type": "single-family homes and new construction in Research Triangle", "neighborhoods": "Downtown, North Hills, ITB, Cary, and Wake Forest", "str_note": "Research Triangle tech and university demand creating strong LTR market", "growth": "consistently ranked among the best places to live driving migration"},
        "Virginia Beach": {"median": "$350,000", "type": "beach homes, condos, and single-family rentals", "neighborhoods": "Oceanfront, Sandbridge, Town Center, Chic's Beach, and Great Neck", "str_note": "oceanfront vacation rental market with strong summer STR demand", "growth": "military presence and beach tourism creating diversified rental demand"},
        "Minneapolis": {"median": "$320,000", "type": "duplexes, single-family homes, and multi-unit buildings", "neighborhoods": "Uptown, Northeast, North Loop, Linden Hills, and St. Paul Grand Avenue", "str_note": "corporate headquarters, sports events, and cultural tourism driving STR demand", "growth": "Fortune 500 company concentration supporting strong employment and housing"},
        "Tampa": {"median": "$380,000", "type": "single-family homes, condos, and waterfront properties", "neighborhoods": "Ybor City, Seminole Heights, South Tampa, Channel District, and Wesley Chapel", "str_note": "year-round warm weather and beaches creating strong vacation rental potential", "growth": "rapidly growing Florida market with increasing tech and finance presence"},
        "New Orleans": {"median": "$280,000", "type": "shotgun doubles, Creole cottages, and historic rentals", "neighborhoods": "French Quarter, Marigny, Bywater, Garden District, and Treme", "str_note": "world-class tourism destination with evolving STR regulations investors must navigate", "growth": "unique architectural stock and cultural tourism driving consistent demand"},
        "Cleveland": {"median": "$175,000", "type": "single-family homes, duplexes, and multi-family units", "neighborhoods": "Ohio City, Tremont, Detroit Shoreway, Lakewood, and University Circle", "str_note": "Rock Hall, sports tourism, and medical district demand creating STR opportunities at low entry costs", "growth": "one of the most affordable major metros with strong cash flow potential"},
        "Pittsburgh": {"median": "$230,000", "type": "row houses, single-family homes, and converted multi-units", "neighborhoods": "Lawrenceville, Shadyside, East Liberty, Strip District, and Mt. Washington", "str_note": "tech growth, university demand, and sports tourism creating diverse rental opportunities", "growth": "eds and meds economy with Google, Meta, and CMU driving tech sector growth"},
        "Cincinnati": {"median": "$240,000", "type": "single-family homes, historic properties, and OTR conversions", "neighborhoods": "Over-the-Rhine, Hyde Park, Mt. Adams, Oakley, and Northside", "str_note": "brewery tourism, sports events, and BLINK festival creating STR demand", "growth": "revitalizing urban neighborhoods with strong investor returns"},
        "St Louis": {"median": "$200,000", "type": "brick homes, multi-family buildings, and historic properties", "neighborhoods": "Central West End, Soulard, Tower Grove, Lafayette Square, and Benton Park", "str_note": "Arch tourism, Cardinals games, and affordable prices making STR investment accessible", "growth": "extremely affordable major metro with value-add opportunities throughout"},
        "Orlando": {"median": "$380,000", "type": "single-family homes, resort condos, and vacation villas", "neighborhoods": "Lake Nona, Winter Park, Thornton Park, Baldwin Park, and Celebration", "str_note": "Walt Disney World and theme park proximity creating one of the largest STR markets in America", "growth": "tourism capital with year-round vacation rental demand near attractions"},
        "San Jose": {"median": "$1,350,000", "type": "single-family homes, condos, and townhomes", "neighborhoods": "Willow Glen, Downtown, Santana Row area, Campbell, and Los Gatos", "str_note": "Silicon Valley tech worker demand creating premium rental rates for both STR and LTR", "growth": "tech industry epicenter with some of the highest rents in the nation"},
        "Boise": {"median": "$440,000", "type": "single-family homes, new construction, and mountain properties", "neighborhoods": "North End, Downtown, Boise Bench, Eagle, and Meridian", "str_note": "outdoor recreation tourism and growing tech sector driving rental demand", "growth": "one of the fastest-growing cities with strong appreciation trajectory"},
        "Salt Lake City": {"median": "$480,000", "type": "single-family homes, condos, and ski-accessible properties", "neighborhoods": "Sugar House, The Avenues, 9th and 9th, Downtown, and Cottonwood Heights", "str_note": "world-class skiing and outdoor recreation creating strong seasonal STR demand", "growth": "tech boom, outdoor lifestyle, and young population driving sustained growth"},
        "Scottsdale": {"median": "$680,000", "type": "luxury homes, golf course properties, and desert estates", "neighborhoods": "Old Town, North Scottsdale, McCormick Ranch, DC Ranch, and Gainey Ranch", "str_note": "luxury tourism, golf, and spring training creating premium STR market with high nightly rates", "growth": "premium desert market with affluent demographics and tourism draw"},
        "Savannah": {"median": "$320,000", "type": "historic homes, townhomes, and Victorian properties", "neighborhoods": "Historic District, Victorian District, Starland, Tybee Island, and Midtown", "str_note": "historic charm and tourism making Savannah one of the top STR destinations in the Southeast", "growth": "preservation-focused market with strong tourism and military presence"},
        "Charleston": {"median": "$480,000", "type": "historic homes, Charleston singles, and beach properties", "neighborhoods": "Downtown, Mount Pleasant, Sullivan's Island, West Ashley, and Folly Beach", "str_note": "repeatedly named the best city in the US driving massive vacation rental demand", "growth": "premium coastal market with limited supply and high tourism demand"},
        "Asheville": {"median": "$420,000", "type": "mountain homes, craftsman bungalows, and cabin rentals", "neighborhoods": "West Asheville, North Asheville, Downtown, Biltmore area, and Black Mountain", "str_note": "brewery scene, Blue Ridge Parkway, and Biltmore Estate creating year-round STR demand", "growth": "arts and culture destination with strong vacation rental market"},
    }

    # Tier 2 vacation market details
    vacation_data = {
        "Gatlinburg": {"median": "$450,000", "type": "mountain cabins, chalets, and lodge-style properties", "draw": "Great Smoky Mountains National Park and Ober Mountain skiing", "str_note": "one of the top cabin rental markets in the US with over 12 million annual visitors to the Smokies"},
        "Pigeon Forge": {"median": "$400,000", "type": "cabins, chalets, and resort condos", "draw": "Dollywood, Smoky Mountains, and family entertainment attractions", "str_note": "Dollywood alone draws over 3 million visitors annually, driving massive STR demand"},
        "Destin": {"median": "$550,000", "type": "beachfront condos, Gulf-front homes, and resort properties", "draw": "emerald green Gulf waters, fishing, and white sand beaches", "str_note": "premier Gulf Coast vacation destination with high summer nightly rates"},
        "Panama City Beach": {"median": "$380,000", "type": "beachfront condos and Gulf-view homes", "draw": "beaches, spring break tourism, and family vacation destination", "str_note": "affordable Florida beach market with strong seasonal and year-round demand"},
        "Gulf Shores": {"median": "$420,000", "type": "beachfront condos and coastal homes", "draw": "Alabama's Gulf Coast beaches and Hangout Music Festival", "str_note": "growing vacation market with lower property costs than Florida alternatives"},
        "Myrtle Beach": {"median": "$300,000", "type": "oceanfront condos, beach houses, and resort properties", "draw": "60 miles of beaches, golf courses, and family entertainment", "str_note": "one of the most visited destinations on the East Coast with over 20 million tourists annually"},
        "Hilton Head": {"median": "$620,000", "type": "plantation villas, oceanfront condos, and golf course homes", "draw": "world-class golf, tennis, and upscale beach vacation experience", "str_note": "luxury island resort market with premium nightly rates and high-end clientele"},
        "Outer Banks": {"median": "$480,000", "type": "beach houses, oceanfront cottages, and stilted homes", "draw": "barrier island beaches, Wright Brothers history, and wild horse tours", "str_note": "traditional family vacation rental market with multi-generational booking patterns"},
        "Cape Cod": {"median": "$580,000", "type": "New England cottages, beach houses, and Cape-style homes", "draw": "iconic New England beaches, whale watching, and seafood culture", "str_note": "premium Northeast vacation market with strong summer rental demand"},
        "Poconos": {"median": "$280,000", "type": "mountain cabins, lakefront homes, and ski chalets", "draw": "ski resorts, lakes, and proximity to NYC and Philadelphia", "str_note": "accessible mountain escape for the largest metro areas on the East Coast"},
        "Branson": {"median": "$250,000", "type": "lakefront cabins, condos, and family-friendly properties", "draw": "live entertainment shows, Table Rock Lake, and Silver Dollar City", "str_note": "family entertainment capital of the Midwest with consistent tourism demand"},
        "Sedona": {"median": "$680,000", "type": "desert luxury homes, casitas, and red rock view properties", "draw": "red rock formations, hiking, vortex tourism, and spiritual retreats", "str_note": "premium desert destination with year-round appeal and high nightly rates"},
        "Joshua Tree": {"median": "$380,000", "type": "desert modern homes, A-frames, and unique architectural properties", "draw": "Joshua Tree National Park, stargazing, and desert aesthetics", "str_note": "Instagram-famous destination driving high demand for architecturally unique STRs"},
        "Big Bear": {"median": "$480,000", "type": "mountain cabins, A-frames, and lakefront homes", "draw": "skiing, Big Bear Lake, and year-round mountain recreation near Los Angeles", "str_note": "closest mountain getaway to LA creating consistent weekend and holiday demand"},
        "Lake Tahoe": {"median": "$780,000", "type": "lakefront properties, ski cabins, and mountain homes", "draw": "world-class skiing, crystal-clear lake, and year-round outdoor recreation", "str_note": "premium four-season market with some of the highest STR nightly rates in the West"},
        "Mammoth Lakes": {"median": "$620,000", "type": "ski condos, mountain cabins, and resort properties", "draw": "Mammoth Mountain skiing and Eastern Sierra outdoor recreation", "str_note": "premier California ski destination with strong winter and growing summer demand"},
        "Park City": {"median": "$1,100,000", "type": "ski chalets, luxury condos, and mountain homes", "draw": "two world-class ski resorts, Sundance Film Festival, and Olympic legacy", "str_note": "ultra-premium ski market with Sundance creating unique January demand spike"},
        "Steamboat Springs": {"median": "$720,000", "type": "ski condos, ranch homes, and mountain properties", "draw": "Steamboat Resort, hot springs, and authentic Colorado ranching culture", "str_note": "family-friendly ski town with strong repeat visitor rates driving consistent bookings"},
        "Breckenridge": {"median": "$850,000", "type": "ski-in/ski-out condos, luxury chalets, and historic homes", "draw": "highest ski resort in North America and charming Main Street shopping", "str_note": "one of the most visited ski towns in Colorado with year-round festival calendar"},
        "Vail": {"median": "$1,200,000", "type": "luxury ski properties, village condos, and mountain estates", "draw": "world-famous ski resort, European-style village, and summer festivals", "str_note": "ultra-luxury ski market with the highest average nightly rates in Colorado"},
        "Aspen": {"median": "$2,500,000", "type": "luxury ski homes, condos, and mountain estates", "draw": "legendary skiing, celebrity culture, and world-class dining", "str_note": "the most prestigious ski market in America with exceptional nightly rental rates"},
        "Telluride": {"median": "$1,800,000", "type": "ski properties, mountain homes, and festival-area rentals", "draw": "box canyon scenery, film and music festivals, and world-class skiing", "str_note": "remote luxury market with film and music festivals driving unique demand patterns"},
        "Whitefish": {"median": "$580,000", "type": "mountain cabins, lakefront homes, and ski properties", "draw": "Glacier National Park, Whitefish Mountain Resort, and Flathead Lake", "str_note": "gateway to Glacier National Park with growing tourism and remote worker migration"},
        "Coeur d Alene": {"median": "$520,000", "type": "lakefront homes, mountain cabins, and resort properties", "draw": "Lake Coeur d'Alene, world-famous golf course, and outdoor recreation", "str_note": "Idaho's premier lake destination with growing year-round tourism appeal"},
        "Bend": {"median": "$620,000", "type": "mountain homes, craftsman properties, and river-front rentals", "draw": "Mt. Bachelor skiing, brewery scene, and Deschutes River recreation", "str_note": "outdoor recreation mecca with year-round appeal and strong STR market"},
        "Hood River": {"median": "$540,000", "type": "craftsman homes, orchard properties, and river-view rentals", "draw": "windsurfing, kiteboarding, craft beer, and Columbia River Gorge", "str_note": "niche adventure sports destination with fruit loop agritourism appeal"},
        "Cannon Beach": {"median": "$720,000", "type": "beach cottages, coastal homes, and oceanfront properties", "draw": "Haystack Rock, Oregon coast beauty, and charming village atmosphere", "str_note": "iconic Oregon coast destination with premium summer rental demand"},
        "Leavenworth": {"median": "$580,000", "type": "Bavarian-style lodges, mountain cabins, and chalets", "draw": "Bavarian-themed village, Christmas lighting festival, and Cascade hiking", "str_note": "unique themed village creating year-round tourism with peak holiday demand"},
        "Chelan": {"median": "$480,000", "type": "lakefront homes, vineyard properties, and resort condos", "draw": "Lake Chelan wine country, water recreation, and summer resort lifestyle", "str_note": "Washington's premier lake destination with strong summer rental season"},
        "Suncadia": {"median": "$620,000", "type": "resort homes, golf properties, and mountain retreats", "draw": "Suncadia Resort, golf, spa, and Cascade Mountain recreation", "str_note": "master-planned resort community with built-in rental management programs"},
        "Lake Geneva": {"median": "$420,000", "type": "lakefront homes, historic estates, and resort properties", "draw": "historic lakeside resort town for Chicago and Milwaukee metro areas", "str_note": "Midwest lake destination with strong weekend and summer rental demand"},
        "Door County": {"median": "$380,000", "type": "waterfront cottages, cherry orchard homes, and cabins", "draw": "250 miles of shoreline, cherry orchards, and New England-style charm", "str_note": "Wisconsin's Cape Cod with strong family vacation and fall color tourism"},
        "Traverse City": {"median": "$380,000", "type": "lakefront homes, cherry farm properties, and downtown condos", "draw": "wine country, National Cherry Festival, and Sleeping Bear Dunes", "str_note": "Michigan's premier resort town with wine, food, and outdoor recreation tourism"},
        "Mackinac Island": {"median": "$450,000", "type": "Victorian homes, historic cottages, and island properties", "draw": "car-free island, Grand Hotel, and historic fudge shops", "str_note": "unique car-free island creating captive audience for vacation rentals"},
        "Put in Bay": {"median": "$350,000", "type": "island homes, waterfront cottages, and vacation properties", "draw": "Lake Erie island resort, Perry's Monument, and summer party destination", "str_note": "summer party island with compressed but intense peak rental season"},
        "Hocking Hills": {"median": "$280,000", "type": "hillside cabins, treehouse rentals, and luxury glamping properties", "draw": "Old Man's Cave, waterfalls, and forest hiking trails", "str_note": "Ohio's top outdoor destination with booming luxury cabin rental market"},
        "Deep Creek": {"median": "$420,000", "type": "lakefront homes, ski chalets, and mountain cabins", "draw": "Deep Creek Lake, Wisp Ski Resort, and four-season mountain recreation", "str_note": "mid-Atlantic's premier lake and ski destination serving DC, Baltimore, and Pittsburgh"},
        "Shenandoah": {"median": "$350,000", "type": "mountain cabins, farm stays, and vineyard properties", "draw": "Shenandoah National Park, Skyline Drive, and Virginia wine country", "str_note": "nature tourism and wine country driving growing STR demand from DC metro area"},
        "Broken Bow": {"median": "$350,000", "type": "luxury cabins, lakefront homes, and rustic retreats", "draw": "Beavers Bend State Park, Broken Bow Lake, and Oklahoma's cabin country", "str_note": "fastest-growing cabin rental market in the South Central US"},
        "Fredericksburg": {"median": "$450,000", "type": "Hill Country homes, wine country estates, and guest houses", "draw": "Texas Wine Country, German heritage, and Hill Country charm", "str_note": "Texas Hill Country's premier wine destination with growing luxury STR market"},
        "Wimberley": {"median": "$420,000", "type": "Hill Country retreats, river properties, and artistic homes", "draw": "Blue Hole swimming, artisan shopping, and Texas Hill Country escapes", "str_note": "artistic Hill Country town with Austin overflow driving weekend STR demand"},
        "Galveston": {"median": "$320,000", "type": "Victorian beach homes, beachfront condos, and historic properties", "draw": "Gulf beaches, Strand Historic District, and Moody Gardens", "str_note": "Houston's beach getaway with affordable coastal STR entry points"},
        "South Padre Island": {"median": "$380,000", "type": "beachfront condos, resort properties, and Gulf-view homes", "draw": "southernmost Texas beach, spring break destination, and eco-tourism", "str_note": "Texas's tropical beach destination with year-round warm weather appeal"},
        "Pensacola": {"median": "$320,000", "type": "beach cottages, Gulf-front condos, and historic homes", "draw": "Pensacola Beach, Blue Angels, and emerald coast waters", "str_note": "affordable Emerald Coast market with military and tourism demand"},
        "Anna Maria Island": {"median": "$850,000", "type": "beach cottages, Gulf-front homes, and Old Florida properties", "draw": "seven miles of white sand beaches and Old Florida charm", "str_note": "premium boutique island market with strict STR preservation creating supply limits"},
        "Clearwater": {"median": "$350,000", "type": "beach condos, waterfront properties, and resort units", "draw": "Clearwater Beach, consistently ranked among the top beaches in the US", "str_note": "major Florida beach destination with year-round tourism and high occupancy rates"},
        "Key West": {"median": "$780,000", "type": "conch houses, historic homes, and tropical properties", "draw": "southernmost point in the US, Duval Street, and island culture", "str_note": "unique island market with limited supply and premium nightly rates year-round"},
        "Islamorada": {"median": "$720,000", "type": "waterfront homes, fishing lodges, and tropical properties", "draw": "sportfishing capital of the world and Florida Keys relaxation", "str_note": "exclusive Keys market with fishing and diving tourism driving premium rates"},
        "Marco Island": {"median": "$680,000", "type": "beach condos, waterfront homes, and Gulf-view properties", "draw": "pristine beaches, shelling, and upscale Gulf Coast island experience", "str_note": "upscale island market with snowbird and vacation rental demand"},
        "Sanibel Island": {"median": "$750,000", "type": "beach homes, nature-adjacent properties, and island cottages", "draw": "world-class shelling beaches and J.N. Ding Darling Wildlife Refuge", "str_note": "nature-focused island with rebuilding demand post-hurricane creating investment opportunities"},
    }

    details = market_data.get(city, vacation_data.get(city, None))
    return slug, details


def generate_tier1_city(city, state):
    slug, details = get_city_details(city, state)
    st = STATE_NAMES.get(state, state)

    if details:
        median = details.get("median", "$350,000")
        prop_type = details.get("type", "single-family homes and rental properties")
        neighborhoods = details.get("neighborhoods", f"popular neighborhoods throughout {city}")
        str_note = details.get("str_note", f"a growing market for both short-term and long-term rental investors")
        growth = details.get("growth", f"steady growth and strong rental demand")
    else:
        median = "$350,000"
        prop_type = "single-family homes and rental properties"
        neighborhoods = f"popular neighborhoods throughout {city}"
        str_note = "a growing market for both short-term and long-term rental investors"
        growth = "steady growth and strong rental demand"

    body = f"""
<section class="hero" style="padding-bottom:60px;">
  <div class="container">
    <h1>Cost Segregation in <span>{city}, {state}</span></h1>
    <p>Professional, IRS-compliant cost segregation studies for rental property investors in {city}, {st}. Maximize your depreciation deductions and accelerate your tax savings.</p>
  </div>
</section>
<section class="section">
  <div class="container" style="max-width:800px;">
    <h2 style="color:var(--white); font-size:1.8rem; margin-bottom:16px;">Cost Segregation for {city} Rental Properties</h2>
    <p style="color:var(--text-muted); margin-bottom:20px;">The {city}, {st} real estate market offers compelling opportunities for rental property investors. With a median home price around {median} and a market characterized by {prop_type}, {city} presents strong fundamentals for investors seeking both cash flow and appreciation. Whether you own a short-term vacation rental or a long-term buy-and-hold property in {city}, a cost segregation study can significantly accelerate your depreciation deductions and improve your after-tax returns.</p>
    <p style="color:var(--text-muted); margin-bottom:20px;">Stratum Cost Segregation serves rental property investors throughout the {city} metro area, including properties in {neighborhoods}. Our engineering-based studies are tailored to the specific building types and construction methods common in the {city} market, ensuring accurate component identification and maximum reclassification.</p>

    <h2 style="color:var(--white); font-size:1.8rem; margin:40px 0 16px;">Why {city} Investors Need Cost Segregation</h2>
    <p style="color:var(--text-muted); margin-bottom:20px;">{city} is {str_note}. The area has seen {growth}, making it an attractive market for real estate investors looking to build wealth through rental properties. However, many investors in {city} are leaving money on the table by depreciating their properties straight-line over 27.5 years without a cost segregation study.</p>
    <p style="color:var(--text-muted); margin-bottom:20px;">A cost segregation study on a typical {city} rental property can reclassify 20-40% of the depreciable cost basis into 5, 7, and 15-year recovery periods. For a property purchased at {median} (after land allocation), this could mean $50,000 to $100,000 or more in accelerated first-year deductions, translating to significant tax savings depending on your marginal tax rate.</p>

    <h2 style="color:var(--white); font-size:1.8rem; margin:40px 0 16px;">The {city} Real Estate Market</h2>
    <p style="color:var(--text-muted); margin-bottom:20px;">With a median property value around {median}, {city} offers accessible entry points for investors at various stages of their portfolio-building journey. The market features {prop_type}, each with distinct component profiles that benefit from cost segregation analysis. Properties in {neighborhoods} are particularly popular among investors for their rental demand, appreciation potential, and proximity to employment centers and amenities.</p>
    <p style="color:var(--text-muted); margin-bottom:20px;">Whether you are acquiring your first rental property in {city} or adding to an existing portfolio, a cost segregation study should be part of your acquisition strategy. The tax savings can be reinvested into additional properties, renovations, or debt reduction, compounding your wealth-building trajectory.</p>

    <h2 style="color:var(--white); font-size:1.8rem; margin:40px 0 16px;">Components We Identify in {city} Properties</h2>
    <p style="color:var(--text-muted); margin-bottom:20px;">Our engineering team identifies building components specific to {city}-area construction, including appliances, flooring, cabinetry, countertops, lighting fixtures, window treatments, HVAC components, plumbing fixtures, landscaping, driveways, patios, fencing, and exterior improvements. Each component is individually classified according to IRS guidelines and MACRS recovery periods.</p>
    <p style="color:var(--text-muted); margin-bottom:20px;">For furnished short-term rentals in {city}, we also identify all furniture, decor, electronics, and specialty items such as hot tubs, fire pits, and outdoor entertainment areas that qualify for 5 or 7-year accelerated depreciation.</p>

    <h2 style="color:var(--white); font-size:1.8rem; margin:40px 0 16px;">Get Started with Your {city} Cost Segregation Study</h2>
    <p style="color:var(--text-muted); margin-bottom:20px;">Stratum Cost Segregation delivers completed, audit-ready studies within 14 business days. Our flat-fee pricing starts at $3,500 for a single property, with portfolio discounts available for {city} investors with multiple properties. Request your free estimate today to see how much you could save on your {city} rental property.</p>

    {get_cta_banner(1)}
  </div>
</section>
"""
    return wrap_page(
        f"Cost Segregation in {city}, {state} | Rental Property Tax Savings",
        f"Professional cost segregation studies for rental property investors in {city}, {st}. Accelerate depreciation and maximize tax savings on your {city} investment property.",
        body, depth=1, canonical_path=f"{slug}/"
    )


def generate_tier2_city(city, state):
    slug, details = get_city_details(city, state)
    st = STATE_NAMES.get(state, state)

    if details:
        median = details.get("median", "$400,000")
        prop_type = details.get("type", "vacation homes and cabin rentals")
        draw = details.get("draw", f"outdoor recreation and tourism")
        str_note = details.get("str_note", f"a popular vacation rental market with strong seasonal demand")
    else:
        median = "$400,000"
        prop_type = "vacation homes and cabin rentals"
        draw = "outdoor recreation and tourism"
        str_note = "a popular vacation rental market with strong seasonal demand"

    body = f"""
<section class="hero" style="padding-bottom:60px;">
  <div class="container">
    <h1>Cost Segregation in <span>{city}, {state}</span></h1>
    <p>Maximize depreciation deductions on your {city} vacation rental property with a professional, IRS-compliant cost segregation study.</p>
  </div>
</section>
<section class="section">
  <div class="container" style="max-width:800px;">
    <h2 style="color:var(--white); font-size:1.8rem; margin-bottom:16px;">Vacation Rental Cost Segregation in {city}</h2>
    <p style="color:var(--text-muted); margin-bottom:20px;">{city}, {st} is {str_note}. Known for {draw}, the area attracts visitors year-round and has become a prime market for short-term rental investors. With median property values around {median} for {prop_type}, {city} represents a strong investment opportunity, especially when paired with a cost segregation study to maximize tax benefits.</p>
    <p style="color:var(--text-muted); margin-bottom:20px;">Stratum Cost Segregation specializes in vacation rental properties like those found in the {city} market. Our engineering-based studies identify every building component eligible for accelerated depreciation, from the furniture and appliances inside to the landscaping and outdoor amenities that make vacation rentals stand out.</p>

    <h2 style="color:var(--white); font-size:1.8rem; margin:40px 0 16px;">Why {city} STR Investors Need Cost Segregation</h2>
    <p style="color:var(--text-muted); margin-bottom:20px;">Short-term rental properties in {city} are particularly well-suited for cost segregation because they are typically furnished with high-quality amenities that guests expect. Hot tubs, fire pits, game rooms, outdoor entertainment areas, premium furnishings, and smart home technology are all classified as 5 or 7-year personal property, eligible for accelerated depreciation.</p>
    <p style="color:var(--text-muted); margin-bottom:20px;">For a {city} vacation rental purchased at {median}, a cost segregation study typically identifies 25-40% of the depreciable basis in accelerated categories. When combined with the STR tax exception for properties with an average guest stay of seven days or less and active owner participation, the resulting deductions can offset W-2 wages and active business income, creating substantial tax savings.</p>

    <h2 style="color:var(--white); font-size:1.8rem; margin:40px 0 16px;">Start Saving on Your {city} Property</h2>
    <p style="color:var(--text-muted); margin-bottom:20px;">Whether you just purchased a vacation rental in {city} or have owned one for years without a cost segregation study, Stratum can help. Our 14-day turnaround and flat-fee pricing make it easy to get started. For existing properties, we include Form 3115 look-back guidance so you can claim years of missed accelerated depreciation in a single tax year.</p>

    {get_cta_banner(1)}
  </div>
</section>
"""
    return wrap_page(
        f"Cost Segregation in {city}, {state} | Vacation Rental Tax Savings",
        f"Professional cost segregation studies for vacation rental investors in {city}, {st}. Accelerate depreciation on your STR property and maximize tax savings.",
        body, depth=1, canonical_path=f"{slug}/"
    )


# ============================================================
# 404 PAGE
# ============================================================
def generate_404():
    body = """
<section class="hero" style="min-height:60vh; display:flex; align-items:center;">
  <div class="container" style="text-align:center;">
    <h1 style="font-size:6rem; margin-bottom:0;"><span>404</span></h1>
    <p style="font-size:1.4rem; color:var(--text-muted); margin-bottom:32px;">Page not found. The page you are looking for does not exist or has been moved.</p>
    <a href="index.html" class="btn btn-gold">Return to Homepage</a>
  </div>
</section>
"""
    return wrap_page("Page Not Found | Stratum Cost Segregation",
        "The page you are looking for does not exist.", body, depth=0)


# ============================================================
# SITEMAP & ROBOTS
# ============================================================
def generate_sitemap(all_paths):
    urls = ""
    for path in all_paths:
        full_url = f"{SITE_URL}/{path}" if path else SITE_URL
        urls += f"  <url><loc>{full_url}</loc><changefreq>weekly</changefreq><priority>0.8</priority></url>\n"
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{urls}</urlset>"""


def generate_robots():
    return f"""User-agent: *
Allow: /

Sitemap: {SITE_URL}/sitemap.xml
"""


# ============================================================
# MAIN GENERATOR
# ============================================================
def main():
    print("=" * 60)
    print("Stratum Cost Segregation - Site Generator")
    print("=" * 60)

    all_paths = []

    # Style CSS is maintained separately in style.css
    # (no longer generated from SHARED_CSS)

    # Core pages
    print("\n--- Core Pages ---")
    write_file("index.html", generate_homepage())
    all_paths.append("")

    core_pages = [
        ("about/index.html", generate_about()),
        ("services/index.html", generate_services()),
        ("short-term-rental-cost-segregation/index.html", generate_str()),
        ("long-term-rental-cost-segregation/index.html", generate_ltr()),
        ("how-it-works/index.html", generate_how_it_works()),
        ("pricing/index.html", generate_pricing()),
        ("faq/index.html", generate_faq()),
        ("contact/index.html", generate_contact()),
        ("blog/index.html", generate_blog_index()),
        ("reviews/index.html", generate_reviews()),
        ("free-estimate/index.html", generate_free_estimate()),
    ]
    for path, content in core_pages:
        write_file(path, content)
        all_paths.append(path.replace("/index.html", "/"))

    # Blog posts
    print("\n--- Blog Posts ---")
    for slug, title, desc, date in get_blog_posts():
        path = f"blog/{slug}/index.html"
        write_file(path, generate_blog_post(slug, title, desc, date))
        all_paths.append(f"blog/{slug}/")

    # Tier 1 city pages
    print("\n--- Tier 1 City Pages (50) ---")
    for city, state in TIER1_CITIES:
        slug, _ = get_city_details(city, state)
        path = f"{slug}/index.html"
        write_file(path, generate_tier1_city(city, state))
        all_paths.append(f"{slug}/")

    # Tier 2 city pages
    print("\n--- Tier 2 City Pages (50) ---")
    for city, state in TIER2_CITIES:
        slug, _ = get_city_details(city, state)
        path = f"{slug}/index.html"
        write_file(path, generate_tier2_city(city, state))
        all_paths.append(f"{slug}/")

    # 404
    print("\n--- Utility Pages ---")
    write_file("404.html", generate_404())

    # Sitemap
    write_file("sitemap.xml", generate_sitemap(all_paths))
    all_paths.append("sitemap.xml")

    # Robots.txt
    write_file("robots.txt", generate_robots())

    print(f"\n{'=' * 60}")
    print(f"COMPLETE: Generated {len(all_paths)} pages/files")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
