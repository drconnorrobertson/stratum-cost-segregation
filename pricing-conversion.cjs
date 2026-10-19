// Final publishing pass: one pricing policy across retained and generated pages.
const fs = require('fs'), path = require('path');
const policy = require('./content/study-pricing.json');
module.exports = function(out) {
 const statement = 'Stratum cost segregation studies cost $1 per square foot, with a $2,000 minimum per property.';
 const cta = `<a class="btn btn-gold" href="${policy.bookingPath}">${policy.cta}</a>`;
 const examples = '<div class="table-scroll"><table><caption>Study fee examples, not tax-savings estimates</caption><thead><tr><th>Property size</th><th>Study fee</th></tr></thead><tbody><tr><td>1,500 square feet</td><td>$2,000 minimum</td></tr><tr><td>2,000 square feet</td><td>$2,000</td></tr><tr><td>3,500 square feet</td><td>$3,500</td></tr><tr><td>10,000 square feet</td><td>$10,000</td></tr></tbody></table></div>';
 const estimator = `<section class="study-fee-panel" aria-labelledby="study-fee-heading"><div><p class="eyebrow">Transparent cost segregation pricing</p><h2 id="study-fee-heading">$1 per square foot. $2,000 minimum.</h2><p>${statement} For portfolios, calculate each property separately. Confirm property measurements and engagement scope during discovery.</p><form data-study-fee><label for="study-square-feet">Property square footage</label><input id="study-square-feet" name="squareFeet" type="number" inputmode="decimal" min="1" step="any" placeholder="e.g. 3500" required><button class="btn btn-outline" type="submit">Calculate Study Fee</button><p aria-live="polite" data-fee-result>Enter square footage to see your study fee.</p></form><p class="calc-note">Study fee = the greater of $2,000 or square footage × $1. Tax planning, return preparation, Form 3115 filing and other separately engaged services are not included by assumption.</p>${cta}</div><div>${examples}<p><a href="/pricing/">Review pricing and engagement scope</a> · <a href="/reviews/">Explore study standards</a></p></div></section>`;
 const replacements = [
  ['The published single-property fee is $3,500. The published portfolio fee is $2,900 per property for three to five properties. Six or more properties use a custom quote.', statement+' The same rate and minimum apply to each property in a portfolio.'],
  ['Published residential pricing is $3,500 for a single property and $2,900 per property for portfolios of three to five; complex commercial work needs its own scope and quote.', statement+' Confirm the written scope for your building.'],
  ['Stratum publishes $3,500 for one residential property and $2,900 per property for three to five. Those prices do not quote a complex commercial engagement.',statement],
  ['Published residential pricing: $3,500 for one property; $2,900 per property for three to five.','$1 per square foot, with a $2,000 minimum per property.'],
  ['Stratum publishes a $3,500 single-residential-property study fee and $2,900 per property for three to five properties.',statement],
  ['Stratum’s published residential fee does not price a complex commercial engagement;', 'Stratum charges $1 per square foot with a $2,000 minimum per property; confirm the commercial engagement scope, and'],
  ['Residential published fees do not establish a price for a complex commercial building.',statement],
  ['is a reference for that scope, not a quote for complex commercial work.', 'is $1 per square foot, with a $2,000 minimum per property; confirm the scope for your building.'],
  ['published residential pricing','published study pricing'],['Published residential study pricing','Cost segregation study pricing'],
  ['Stratum residential pricing and scope','Stratum study pricing and scope'],
  ['<tr><th scope="row">Single residential property</th><td>$3,500 published fee</td></tr><tr><th scope="row">Portfolio of 3 to 5 properties</th><td>$2,900 per property published fee</td></tr><tr><th scope="row">6 or more properties</th><td>Custom scope and quote</td></tr>', '<tr><th scope="row">Study rate</th><td>$1 per square foot</td></tr><tr><th scope="row">Minimum study fee</th><td>$2,000 per property</td></tr><tr><th scope="row">Portfolios</th><td>Apply the rate and minimum to each property</td></tr>'],
  ['The cost of the study itself runs between $1,500 and $3,500 for a property of this size. The net benefit in the first year, after the study cost, is roughly $24,000 to $26,000. The ROI on the study is measured in multiples, not percentages.', statement+' Compare that fee with the tax benefit your preparer determines you can use.'],
  ['The study costs between $1,500 and $3,500 for a typical ADU,', 'Stratum charges $1 per square foot, with a $2,000 minimum per property,'],
  ['against a study cost of $2,500 to $3,500.', 'before study fees. Stratum charges $1 per square foot, with a $2,000 minimum per property.'],
  ['The difference between a $2,000 DIY report and a $3,500 professional study is trivial compared to the deductions at stake.', statement+' Compare documentation, technical review and support alongside the fee.'],
  ['The study cost is typically $3,500 to $6,500 depending on the property,', 'Stratum charges $1 per square foot with a $2,000 minimum per property,'],
  ['Self-storage facilities typically generate cost segregation study fees in the $3,500 to $8,000 range depending on facility size and complexity, consistent with other commercial property types.',statement]
 ];
 const updatedURLs=new Set();
 const searchCopy={
  'index.html':['Cost Segregation Studies: $1/Sq Ft | Stratum','Engineering-based cost segregation for rental and commercial properties. $1 per square foot, $2,000 minimum. Explore study standards and book a discovery call.'],
  'services/index.html':['Cost Segregation Study Services & Pricing | Stratum','Compare cost segregation studies for STRs, rental homes, multifamily and commercial buildings. $1 per square foot with a $2,000 minimum per property.'],
  'short-term-rental-cost-segregation/index.html':['STR & Airbnb Cost Segregation Studies | Stratum','Explore cost segregation for short-term rentals and Airbnb properties. Review study scope, records and pricing: $1 per square foot with a $2,000 minimum.'],
  'long-term-rental-cost-segregation/index.html':['Rental Property Cost Segregation Studies | Stratum','Evaluate cost segregation for long-term rental properties, study documentation and CPA coordination. $1 per square foot with a $2,000 minimum per property.'],
  'commercial-cost-segregation/index.html':['Commercial Cost Segregation Studies & Pricing | Stratum','Cost segregation for office, retail, industrial and mixed-use buildings. Review engineering scope and pricing: $1 per square foot, $2,000 minimum per property.'],
  'multifamily-cost-segregation/index.html':['Multifamily & Apartment Cost Segregation | Stratum','Evaluate apartment and multifamily cost segregation studies. Review unit sampling, records and study fees: $1 per square foot, $2,000 minimum per property.'],
  'small-property-cost-segregation/index.html':['Small Rental Property Cost Segregation | Stratum','Cost segregation for rental homes, duplexes and small multifamily properties. Compare study economics at $1 per square foot with a $2,000 minimum per property.'],
  'cost-segregation-calculator/index.html':['Cost Segregation Calculator & Study Fee Estimate | Stratum','Estimate accelerated depreciation and potential tax deferral, then calculate your study fee at $1 per square foot with a $2,000 minimum per property.'],
  'pricing/index.html':['Cost Segregation Pricing: $1/Sq Ft, $2,000 Minimum | Stratum','Calculate your cost segregation study fee: $1 per square foot with a $2,000 minimum per property. Review fee examples, study scope and book a discovery call.'],
  'blog/cost-segregation-study-cost-pricing/index.html':['How Much Does a Cost Segregation Study Cost? | Stratum','Understand cost segregation study fees, what to compare and implementation costs. Stratum pricing is $1 per square foot with a $2,000 minimum per property.']
 };
 const priority = new Set(['index.html','pricing/index.html','cost-segregation-calculator/index.html','services/index.html','short-term-rental-cost-segregation/index.html','long-term-rental-cost-segregation/index.html','commercial-cost-segregation/index.html','multifamily-cost-segregation/index.html','small-property-cost-segregation/index.html','blog/cost-segregation-study-cost-pricing/index.html','cost-seg-discovery/index.html']);
 let changed=0;
 function walk(dir) { for(const e of fs.readdirSync(dir,{withFileTypes:true})) {
  const file=path.join(dir,e.name); if(e.isDirectory()){walk(file);continue;} if(!file.endsWith('.html'))continue;
  let h=fs.readFileSync(file,'utf8'),before=h,rel=path.relative(out,file);
  for(const [from,to] of replacements)h=h.split(from).join(to);
  // Preserve comparison editorial labels; standardize actual booking buttons/navigation.
  h=h.replace(/(<a\b[^>]*href="\/cost-seg-discovery\/(?:\?[^"<>]*)?"[^>]*>)([\s\S]*?)(<\/a>)/gi,(all,a,label,b)=>/class=|data-discovery/.test(a)?a+policy.cta+b:all);
  if(rel==='index.html') {
   h=h.replace(/<a href="\/blog\/">Blog<\/a>/,'').replace(/<a href="\/contact\/">Contact<\/a>/,'');
   h=h.replace(/<h1>Cost Segregation Built Around <span>Your Property<\/span><\/h1>/, '<h1>Cost Segregation Studies.<br><span>Clear Pricing.</span></h1>');
   h=h.replace(/<p>Explore cost segregation for commercial buildings,[\s\S]*?<\/p>/,'<p>Find out whether cost segregation makes sense for your rental or commercial property. Engineering-based analysis at $1 per square foot, with a $2,000 minimum, and tax strategy coordination through AE Tax Advisors.</p>');
   h=h.replace(/<section data-topic-depth>[\s\S]*?<\/section>/g,'');
   h=h.replace(/<h2>Resolve the details behind your property study<\/h2>/,'<h2>Find answers for your property study</h2>').replace(/Explore 500 new practical guides/,'Explore practical guides');
  }
  if(rel==='cost-seg-discovery/index.html') {
   h=h.replace('<h2>Schedule a Call</h2>',`<h2>Schedule a Call</h2><p>${statement} <a href="/pricing/">Calculate your study fee</a> before choosing a time.</p>`);
  }
  if(priority.has(rel)&&rel!=='cost-seg-discovery/index.html') {
   const block = rel==='pricing/index.html'||rel==='cost-segregation-calculator/index.html'?estimator:`<section class="study-fee-strip"><div><h2>Know the study fee before you book.</h2><p>${statement}</p><p><a href="/pricing/">Calculate your study fee</a> · <a href="/cost-segregation-calculator/">Estimate potential accelerated depreciation</a></p></div><div>${cta}<p>Discuss your property, study scope and next steps with AE Tax Advisors.</p></div></section>`;
   if(rel==='pricing/index.html')h=h.replace(/<p class="guide-summary">[\s\S]*?<\/p>/,match=>match+block);
   else if(rel==='cost-segregation-calculator/index.html')h=h.replace('</section>',match=>match+block);
   else if(rel==='index.html')h=h.replace(/(<div class="social-proof-bar">)/,match=>block+match);
   else if(/<\/main>/.test(h))h=h.replace('</main>',block+'</main>');
   else h=h.replace(/<footer\b/,block+'<footer');
   h=h.replace('</head>','<link rel="stylesheet" href="/assets/study-pricing.css"><script defer src="/assets/study-pricing.js"></script></head>');
  }
  if(rel==='pricing/index.html') {
   const title='Cost Segregation Pricing: $1/Sq Ft, $2,000 Minimum | Stratum';
   const description='Calculate your cost segregation study fee: $1 per square foot with a $2,000 minimum per property. Review fee examples, study scope and book a discovery call.';
   h=h.replace(/<title>[^<]*<\/title>/,`<title>${title}</title>`).replace(/(<meta (?:name="description"|property="og:description"|name="twitter:description") content=")[^"]*"/g,(_,prefix)=>prefix+description+'"').replace(/<h1>[^<]*<\/h1>/,'<h1>Cost Segregation Pricing: $1 per Square Foot</h1>').replace(/<p class="guide-summary">[\s\S]*?<\/p>/,`<p class="guide-summary">${statement} Calculate the fee for your building, review the study scope, and discuss your property with our team.</p>`);
   const schema={'@context':'https://schema.org','@type':'Service',name:'Cost segregation study',provider:{'@id':'https://www.stratumcostsegregation.com/#organization'},areaServed:'US',url:'https://www.stratumcostsegregation.com/pricing/',offers:{'@type':'Offer',url:'https://www.stratumcostsegregation.com/pricing/',priceCurrency:'USD',description:statement,priceSpecification:{'@type':'UnitPriceSpecification',price:policy.perSquareFoot,priceCurrency:policy.currency,unitText:'square foot',description:'Minimum study fee: $2,000 per property.'}}};
   h=h.replace('</head>',`<script type="application/ld+json">${JSON.stringify(schema)}</script></head>`);
  }
  if(searchCopy[rel]) {
   const [title,description]=searchCopy[rel];
   h=h.replace(/<title>[^<]*<\/title>/,()=>`<title>${title}</title>`)
    .replace(/(<meta (?:name="description"|property="og:description"|name="twitter:description") content=")[^"]*"/g,(_,prefix)=>prefix+description+'"')
    .replace(/(<meta (?:property="og:title"|name="twitter:title") content=")[^"]*"/g,(_,prefix)=>prefix+title+'"');
   h=h.replace(/(<script type="application\/ld\+json">)([\s\S]*?)(<\/script>)/g,(all,a,json,b)=>{
    const data=JSON.parse(json);
    const visit=node=>{if(!node||typeof node!=='object')return;if(node['@type']==='WebPage'){node.name=title;node.description=description;}Object.values(node).forEach(v=>{if(Array.isArray(v))v.forEach(visit);else if(typeof v==='object')visit(v);});};
    visit(data);return a+JSON.stringify(data)+b;
   });
  }
  if(h!==before){fs.writeFileSync(file,h);changed++;updatedURLs.add('https://www.stratumcostsegregation.com/'+(rel==='index.html'?'':rel.replace(/index\.html$/,'')));}
 }}
 walk(out);
 const sitemap=path.join(out,'sitemap.xml');
 let xml=fs.readFileSync(sitemap,'utf8').replace(/<url>\s*<loc>(.*?)<\/loc>([\s\S]*?)<\/url>/g,(all,url,tail)=>updatedURLs.has(url)?'<url><loc>'+url+'</loc>'+(/<lastmod>/.test(tail)?tail.replace(/<lastmod>.*?<\/lastmod>/,'<lastmod>'+policy.effectiveDate+'</lastmod>'):tail+'<lastmod>'+policy.effectiveDate+'</lastmod>')+'</url>':all);
 fs.writeFileSync(sitemap,xml);
 fs.writeFileSync(path.join(out,'assets/study-pricing-policy.json'),JSON.stringify(policy));
 console.log('Unified pricing and conversion updates: '+changed+' pages');
};
