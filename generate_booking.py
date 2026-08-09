#!/usr/bin/env python3
"""Generate the Stratum booking / consultation page with the GHL calendar embed."""

import json
import os

from stratum_render import BASE_URL, EMAIL, PHONE, PHONE_HREF, SCRIPTS, _org_nodes, footer, nav

ROOT = os.path.dirname(os.path.abspath(__file__))

# GoHighLevel / LeadConnector booking widget
GHL_CALENDAR_URL = "https://api.leadconnectorhq.com/widget/booking/FggCeBoxIuOuZZrTaVV1"

URL = f"{BASE_URL}/booking/"
TITLE = "Book a Cost Segregation Consultation | Stratum Cost Segregation"
DESC = ("Schedule a free 30-minute cost segregation consultation. Review your property, estimate your "
        "first-year deduction, and get a clear answer on whether a study makes sense.")

graph = _org_nodes() + [
    {
        "@type": "BreadcrumbList",
        "@id": f"{URL}#breadcrumb",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{BASE_URL}/"},
            {"@type": "ListItem", "position": 2, "name": "Book a Call", "item": URL},
        ],
    },
    {
        "@type": "WebPage",
        "@id": f"{URL}#webpage",
        "url": URL,
        "name": TITLE,
        "description": DESC,
        "isPartOf": {"@id": f"{BASE_URL}/#website"},
        "about": {"@id": f"{BASE_URL}/#business"},
        "breadcrumb": {"@id": f"{URL}#breadcrumb"},
    },
    {
        "@type": "ReserveAction",
        "@id": f"{URL}#reserve",
        "name": "Book a Cost Segregation Consultation",
        "target": {"@type": "EntryPoint", "urlTemplate": URL, "actionPlatform": "http://schema.org/DesktopWebPlatform"},
        "provider": {"@id": f"{BASE_URL}/#organization"},
    },
]

LD = json.dumps({"@context": "https://schema.org", "@graph": graph})

PAGE = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{TITLE}</title>
  <meta name="description" content="{DESC}">
  <meta property="og:title" content="{TITLE}">
  <meta property="og:description" content="{DESC}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{URL}">
  <meta property="og:site_name" content="Stratum Cost Segregation">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{TITLE}">
  <meta name="twitter:description" content="{DESC}">
  <link rel="canonical" href="{URL}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="preconnect" href="https://api.leadconnectorhq.com">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../style.css">

<script type="application/ld+json">{LD}</script>
</head>
<body>
{nav(1)}

<section class="hero" style="padding-bottom:50px;">
  <div class="container">
    <h1>Book Your <span>Cost Segregation</span> Consultation</h1>
    <p>A free 30-minute call with a Stratum specialist. We review your property, give you a realistic first-year
    deduction range, and tell you honestly whether a study is worth it for your situation.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <style>
      .booking-grid {{ display:grid; grid-template-columns: 1fr 1.15fr; gap:56px; align-items:start; max-width:1150px; margin:0 auto; }}
      .booking-list {{ list-style:none; padding:0; margin:0; }}
      .booking-list li {{ padding:14px 0 14px 32px; position:relative; border-bottom:1px solid rgba(255,255,255,0.08); }}
      .booking-list li:last-child {{ border-bottom:none; }}
      .booking-list .tick {{ position:absolute; left:0; color:var(--gold); font-weight:700; }}
      .booking-list p {{ font-size:0.95rem; color:var(--text-muted); margin:6px 0 0 0; }}
      .ghl-calendar-iframe {{ width:100%; height:750px; border:none; border-radius:8px; }}
      #ghl-calendar {{ min-height:750px; border-radius:8px; overflow:visible; -webkit-overflow-scrolling:touch; }}
      @media (max-width: 900px) {{
        .booking-grid {{ grid-template-columns:1fr !important; gap:32px !important; }}
        .ghl-calendar-iframe {{ height:850px !important; min-height:850px !important; }}
        #ghl-calendar {{ min-height:850px !important; overflow:visible !important; -webkit-overflow-scrolling:touch !important; }}
      }}
    </style>
    <div class="booking-grid">
      <div>
        <h2 style="margin-top:0;">What You Get on the Call</h2>
        <ul class="booking-list">
          <li>
            <span class="tick">&#10003;</span>
            <strong>Property-Specific Deduction Estimate</strong>
            <p>We walk through your purchase price, placed-in-service date, and property type to size up a realistic
            reclassification percentage and first-year deduction.</p>
          </li>
          <li>
            <span class="tick">&#10003;</span>
            <strong>A Straight Answer on Fit</strong>
            <p>Cost segregation is not right for every property. If the numbers do not work for you, we will say so
            on the call rather than sell you a study.</p>
          </li>
          <li>
            <span class="tick">&#10003;</span>
            <strong>Look-Back Review</strong>
            <p>Already own the property? We check whether a Form 3115 catch-up study can recover missed depreciation
            from prior years without amending a single return.</p>
          </li>
          <li>
            <span class="tick">&#10003;</span>
            <strong>Timeline and Pricing Up Front</strong>
            <p>Flat-fee pricing and a 14-business-day turnaround. No surprises, no obligation.</p>
          </li>
        </ul>
        <p style="margin-top:28px; color:var(--text-muted); font-size:0.95rem;">
          <strong>Prefer to start with numbers?</strong> Request a
          <a href="../free-estimate/index.html" style="color:var(--gold);">free written estimate</a>
          instead, or call us directly at
          <a href="tel:{PHONE_HREF}" style="color:var(--gold);">{PHONE}</a>.
        </p>
      </div>
      <div>
        <div class="card" style="padding:32px;">
          <h3 style="margin-top:0; margin-bottom:6px;">Pick a Time</h3>
          <p style="color:var(--text-muted); font-size:0.95rem; margin-bottom:24px;">
            Choose a date and time below. You will receive a confirmation and video conference link immediately.
          </p>
          <!-- GHL Calendar Embed -->
          <div id="ghl-calendar">
            <iframe class="ghl-calendar-iframe"
                    src="{GHL_CALENDAR_URL}"
                    title="Schedule a cost segregation consultation"
                    loading="lazy"
                    frameborder="0"
                    scrolling="yes"></iframe>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container" style="max-width:900px;">
    <h2 class="section-title">Come Prepared and We Can Go Deeper</h2>
    <p class="section-subtitle">None of this is required, but having it handy makes the 30 minutes far more useful.</p>
    <div class="card-grid">
      <div class="card">
        <div class="card-icon">&#128196;</div>
        <h3>Closing Statement</h3>
        <p>Your settlement statement or HUD-1 establishes the purchase price and capitalized closing costs that form
        the depreciable basis.</p>
      </div>
      <div class="card">
        <div class="card-icon">&#128197;</div>
        <h3>Placed-In-Service Date</h3>
        <p>The date the property was ready and available for rent. It drives which bonus depreciation rate applies and
        whether a look-back study is needed.</p>
      </div>
      <div class="card">
        <div class="card-icon">&#128202;</div>
        <h3>Prior Depreciation Schedule</h3>
        <p>If you have owned the property for a year or more, your existing schedule tells us the size of a potential
        Section 481(a) catch-up adjustment.</p>
      </div>
      <div class="card">
        <div class="card-icon">&#127968;</div>
        <h3>Property Details</h3>
        <p>Square footage, year built, renovation history, and whether the property is a short-term rental, long-term
        rental, or commercial building.</p>
      </div>
    </div>
    <p style="text-align:center; margin-top:40px; color:var(--text-muted);">
      Questions before you book? Email
      <a href="mailto:{EMAIL}" style="color:var(--gold);">{EMAIL}</a>
      or read our <a href="../faq/index.html" style="color:var(--gold);">frequently asked questions</a>.
    </p>
  </div>
</section>

{footer(1)}

{SCRIPTS}
</body>
</html>"""


def main():
    out_dir = os.path.join(ROOT, "booking")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(PAGE)
    print("Wrote booking/index.html")


if __name__ == "__main__":
    main()
