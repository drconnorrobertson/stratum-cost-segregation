const fs=require('fs'),path=require('path'),assert=require('assert');
const root=path.join(__dirname,'../public'),base='https://www.stratumcostsegregation.com',providers=require('../content/competitor-comparisons/providers.json');
const routes=['/compare/alternatives/',...providers.map(p=>'/compare/'+p.slug+'-alternatives/')];
const xml=fs.readFileSync(path.join(root,'sitemap.xml'),'utf8'),titles=new Set();
for(const route of routes){const h=fs.readFileSync(path.join(root,route,'index.html'),'utf8');const title=h.match(/<title>(.*?)<\/title>/)[1];assert(!titles.has(title));titles.add(title);assert.equal((h.match(/<h1>/g)||[]).length,1);assert(h.includes('rel="canonical" href="'+base+route+'"'));assert.equal(xml.split('<loc>'+base+route+'</loc>').length-1,1);assert(h.includes('not an independent ranking'));assert(h.includes('/cost-seg-discovery/?'));for(const m of h.matchAll(/href="(\/[^"?#]*)(?:\?[^"#]*)?"/g))assert(fs.existsSync(path.join(root,m[1],m[1].endsWith('/')?'index.html':'')),route+' broken '+m[1]);for(const m of h.matchAll(/<script type="application\/ld\+json">(.*?)<\/script>/g))JSON.parse(m[1]);}
for(const p of providers){const direct=fs.readFileSync(path.join(root,'compare',p.slug+'-vs-stratum/index.html'),'utf8'),alt=fs.readFileSync(path.join(root,'compare',p.slug+'-alternatives/index.html'),'utf8');assert(direct.includes('/compare/'+p.slug+'-alternatives/'));assert(alt.includes('/compare/'+p.slug+'-vs-stratum/'));assert(alt.includes(p.reviewed));assert(alt.includes(p.source));assert(alt.includes('Other providers to investigate'));}
const bedford=fs.readFileSync(path.join(root,'compare/bedford-cost-segregation-alternatives/index.html'),'utf8');assert(bedford.includes('not presented as two independent alternatives'));assert(fs.readFileSync(path.join(root,'compare/index.html'),'utf8').includes('/compare/alternatives/'));assert(fs.existsSync(path.join(root,'assets/downloads/provider-comparison-coverage.csv')));
console.log(JSON.stringify({providerEntries:providers.length,alternativesPages:routes.length,uniqueTitles:true,canonicals:true,internalLinks:true,reciprocalLinks:true,sources:true,legacyBrandDisclosure:true,csv:true}));

for(const [a,b] of [['mvo-cost-segregation','costsegez'],['kbkg','costsegregation-com'],['source-advisors','bedford-cost-segregation']]){
 for(const [subject,related] of [[a,b],[b,a]]){
  const h=fs.readFileSync(path.join(root,'compare',subject+'-alternatives/index.html'),'utf8');
  const shortlist=h.split('<h2>Other providers to investigate</h2>')[1].split('</table>')[0];
  assert(!shortlist.includes('/compare/'+related+'-vs-stratum/'),'related brand offered as independent alternative: '+subject);
 }
}
for(const route of ['/compare/','/compare/alternatives/']){
 const h=fs.readFileSync(path.join(root,route,'index.html'),'utf8');
 assert(h.includes('Research providers by property need'));
 for(const p of providers.filter(p=>p.segments))assert(h.includes('/compare/'+p.slug+'-vs-stratum/'));
}
