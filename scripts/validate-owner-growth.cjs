const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
const root=path.join(__dirname,'..'),out=path.join(root,'public'),manifest=require('../outputs/owner-growth-manifest.json'),D=require('../content/owner-growth.json'),api=require('../assets/owner-growth.js');
// Financial edge cases matter: minimum applies per property, zero usability is not savings.
assert.equal(api.calculate(1500,24000,32,100,500).net,5180);
assert.equal(api.calculate(1500,24000,32,0,500).net,-2500);
assert.equal(api.calculate(1500,24000,0,100,500).breakEvenDeduction,null);
assert.equal(api.calculate(3500,0,24,100,0).studyFee,3500);
assert.throws(()=>api.calculate(0,100,24,100,0));assert.throws(()=>api.calculate(1000,100,24,101,0));assert.throws(()=>api.calculate(NaN,100,24,100,0));
assert.equal(api.groupProperty({label:'One',sq:1000,records:'ready',cpa:'yes',sale:'no'}).group,'Ready for a scoped proposal');
assert.equal(api.groupProperty({label:'Two',sq:1500,records:'missing',cpa:'yes',sale:'no'}).group,'Records needed');
assert.equal(api.groupProperty({label:'Three',sq:1500,records:'ready',cpa:'yes',sale:'yes'}).group,'Preparer review needed');
assert.equal([1000,1500,1900].map(sq=>api.groupProperty({label:'Home',sq}).fee).reduce((a,b)=>a+b),6000);
assert(api.checklist(['conversion','furnished']).includes('Conversion-date value support and preparer basis calculation'));
assert(!api.checklist([]).includes('Seller inventory and items actually transferred'));
for(const p of D.pages.filter(p=>p.example)){const e=p.example,r=api.calculate(e.squareFeet,e.incremental,e.rate,e.usable,e.implementation);assert.equal(r.studyFee,e.fee);assert.equal(r.net,e.net);assert.equal(r.taxReduction,e.taxReduction);}
const urls=[...fs.readFileSync(path.join(out,'sitemap.xml'),'utf8').matchAll(/<loc>(.*?)<\/loc>/g)].map(m=>m[1]);assert.equal(new Set(urls).size,urls.length);
assert.equal(manifest.newPages.length,25);assert.equal(manifest.updatedPages.length,25);assert.equal(manifest.templates.length,6);assert(manifest.navigationPages>=170);
let internalLinks=0;
for(const url of [...manifest.newPages,...manifest.updatedPages]){
 assert(urls.includes(url));const file=path.join(out,new URL(url).pathname,'index.html'),h=fs.readFileSync(file,'utf8');
 assert(h.includes('rel="canonical" href="'+url+'"'),url);assert.equal((h.match(/<h1\b/g)||[]).length,1,url);assert(!/name="robots"[^>]*noindex/.test(h));
 const ids=[...h.matchAll(/\bid="([^"]+)"/g)].map(m=>m[1]);assert.equal(new Set(ids).size,ids.length,'Duplicate ID '+url);
 for(const m of h.matchAll(/<script[^>]*type="application\/ld\+json"[^>]*>([\s\S]*?)<\/script>/g))JSON.parse(m[1]);
 for(const m of h.matchAll(/(?:href|src)="(\/[^"<>]*)"/g)){
  const u=new URL(m[1].replaceAll('&amp;','&'),'https://www.stratumcostsegregation.com');if(u.pathname.startsWith('/_vercel/'))continue;const f=path.join(out,u.pathname,u.pathname.endsWith('/')?'index.html':'');assert(fs.existsSync(f),'Missing target '+f+' from '+url);if(u.hash&&f.endsWith('.html'))assert(fs.readFileSync(f,'utf8').includes('id="'+u.hash.slice(1)+'"'),'Missing fragment '+u.href);internalLinks++;
 }
 if(manifest.newPages.includes(url)){assert(h.includes('id="main-nav"'));assert(h.includes('data-owner-cta'));assert(h.includes('$2,000 minimum per property'));assert(h.indexOf('owner-cta')<h.indexOf('<footer'));}
}
for(const p of D.pages.filter(p=>p.illustrative)){const h=fs.readFileSync(path.join(out,'rental-owner-guide',p.slug,'index.html'),'utf8');assert(h.includes('Fictional worked example.'));}
for(const t of manifest.templates){const csv=fs.readFileSync(path.join(out,t),'utf8');assert(csv.includes('\r\n'));assert(csv.split('\r\n')[0].includes('"'));}
console.log(JSON.stringify({ownerGrowthValid:true,newPages:25,retainedPagesImproved:25,navigationPages:manifest.navigationPages,templates:6,internalLinks,financialEdgeCases:true,illustrationsDisclosed:true}));
