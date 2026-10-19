const fs=require('fs'),path=require('path'),assert=require('assert');
const root=path.join(__dirname,'../public'),base='https://www.stratumcostsegregation.com';
const providers=require('../content/competitor-comparisons/providers.json');
const paths=['/compare/','/compare/quote-checklist/','/compare/stratum-and-ae-tax-advisors/',...providers.map(p=>'/compare/'+p.slug+'-vs-stratum/')];
const sitemap=fs.readFileSync(path.join(root,'sitemap.xml'),'utf8');const titles=new Set();
for(const rel of paths){const h=fs.readFileSync(path.join(root,rel,'index.html'),'utf8');
 assert(h.includes('rel="canonical" href="'+base+rel+'"'),rel+' canonical');assert.equal((h.match(/<h1>/g)||[]).length,1);
 const title=h.match(/<title>(.*?)<\/title>/)[1];assert(!titles.has(title));titles.add(title);
 assert(h.includes('AE Tax Advisors hosts discovery'));assert(h.includes('Stratum prepares the property-level'));
 assert(!/noindex|AggregateRating|Review"|guaranteed savings/i.test(h));assert(h.includes('not an independent ranking'));
 assert(h.includes('utm_campaign=provider_comparisons'));assert(/href="\/cost-seg-discovery\/(?:\?[^"]*)?"/.test(h));
 for(const m of h.matchAll(/href="(\/[^"#?]*)(?:\?[^"#]*)?"/g)){let u=m[1];let file=path.join(root,u,u.endsWith('/')?'index.html':'');assert(fs.existsSync(file),rel+' broken internal link '+u)}
 for(const m of h.matchAll(/<script type="application\/ld\+json">(.*?)<\/script>/g))JSON.parse(m[1]);
 assert.equal(sitemap.split('<loc>'+base+rel+'</loc>').length-1,1);
}
const booking=fs.readFileSync(path.join(root,'cost-seg-discovery/index.html'),'utf8');assert(booking.includes('31bqciSJCSb2R44l0EML'));assert(booking.includes("['utm_source','utm_medium','utm_campaign','utm_content']"));assert(booking.includes('AE Tax Advisors, Stratum’s tax strategy partner'));
for(const rel of ['index.html','services/index.html','pricing/index.html','about/index.html','cost-segregation-resources/index.html'])assert(fs.readFileSync(path.join(root,rel),'utf8').includes('href="/compare/"'));
console.log(JSON.stringify({pages:paths.length,providers:providers.length,canonical:true,internalLinks:true,aeConnection:true,bookingCalendarMatchesAE:true,attribution:true}));
