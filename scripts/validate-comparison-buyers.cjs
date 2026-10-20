const fs=require('fs'),path=require('path'),assert=require('node:assert/strict');
const root=path.join(__dirname,'../public'),providers=require('../content/competitor-comparisons/providers.json'),priority=require('../content/competitor-comparisons/priority-research.json'),buyers=require('../comparison-buyers.cjs');
assert(providers.length>=55);assert(new Set(providers.map(buyers.family)).size>=50);
const introductions=new Set();
for(const p of providers){
 const shortlist=buyers.shortlist(p,providers);assert.equal(shortlist.length,4);assert.equal(new Set(shortlist.map(buyers.family)).size,4);assert(shortlist.every(q=>buyers.family(q)!==buyers.family(p)));
 for(const suffix of ['-vs-stratum','-alternatives']){
  const h=fs.readFileSync(path.join(root,'compare',p.slug+suffix,'index.html'),'utf8');
  assert(h.includes('id="decision-summary"'));assert(h.includes('id="buyer-questions"'));assert(h.includes('$1 per square foot. $2,000 minimum per property.'));
  assert(h.includes(p.slug+'-proposal-checklist.csv'));assert(h.includes('/assets/comparison-buyers.css'));assert(h.includes('/_vercel/insights/script.js'));
  if(priority[p.slug]){assert(h.includes('id="provider-research"'));assert(h.includes(priority[p.slug].reviewed));const count=(suffix==='-vs-stratum'?priority[p.slug].direct:priority[p.slug].alternatives).length;assert(count>=2);}
 }
 introductions.add(p.scenario);const csv=fs.readFileSync(path.join(root,'assets/downloads',p.slug+'-proposal-checklist.csv'),'utf8');assert(csv.includes(p.source));assert(csv.includes(p.question));assert(csv.includes('$2,000 minimum per property'));
}
assert.equal(introductions.size,providers.length);
for(const route of ['compare/index.html','compare/alternatives/index.html']){
 const h=fs.readFileSync(path.join(root,route),'utf8');for(const key of Object.keys(priority))for(const suffix of ['-vs-stratum','-alternatives'])assert(h.includes('/compare/'+key+suffix+'/'));
}
console.log(JSON.stringify({providerPages:providers.length*2,providerBrands:providers.length,documentedBrandGroups:new Set(providers.map(buyers.family)).size,detailedPriorityPages:Object.keys(priority).length*2,downloadableChecklists:providers.length,shortlistsDistinct:true,pricingConsistent:true}));
