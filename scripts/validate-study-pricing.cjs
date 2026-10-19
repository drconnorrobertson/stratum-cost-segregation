const fs=require('fs'),path=require('path'),assert=require('node:assert/strict');
const root=path.join(__dirname,'../public'),policy=require('../content/study-pricing.json');
assert.equal(policy.perSquareFoot,1);assert.equal(policy.minimumPerProperty,2000);
let pages=0,bookingLinks=0;
function walk(dir){for(const e of fs.readdirSync(dir,{withFileTypes:true})){
 const f=path.join(dir,e.name);if(e.isDirectory()){walk(f);continue;}if(!f.endsWith('.html'))continue;
 const h=fs.readFileSync(f,'utf8');pages++;
 for(const phrase of ['single-property fee is $3,500','portfolio fee is $2,900','$2,900 per property','pricing is $3,500','publishes $3,500','residential pricing: $3,500','single-residential-property study fee','study itself runs between $1,500 and $3,500'])assert(!h.includes(phrase),f+' stale pricing: '+phrase);
 for(const m of h.matchAll(/<script type="application\/ld\+json">([\s\S]*?)<\/script>/g))JSON.parse(m[1]);
 for(const m of h.matchAll(/href="(\/cost-seg-discovery\/[^"<>]*)"/g)){bookingLinks++;assert(fs.existsSync(path.join(root,m[1].split('?')[0],'index.html')));}
}}
walk(root);
for(const rel of ['pricing/','cost-segregation-calculator/']){
 const h=fs.readFileSync(path.join(root,rel,'index.html'),'utf8');
 assert(h.includes('data-study-fee'));assert(h.includes('$1 per square foot'));assert(h.includes('$2,000 minimum'));
 assert.equal((h.match(/id="study-square-feet"/g)||[]).length,1);
 for(const asset of ['study-pricing.css','study-pricing.js','study-pricing-policy.json'])assert(fs.existsSync(path.join(root,'assets',asset)));
 assert(h.indexOf('data-study-fee')<h.indexOf('<footer'));
}
const home=fs.readFileSync(path.join(root,'index.html'),'utf8');
assert(home.includes('studies cost $1 per square foot'));assert(!home.includes('studies cost <div'));assert(!home.includes('Explore 500 new'));
const price=fs.readFileSync(path.join(root,'pricing/index.html'),'utf8');
assert(price.includes('"unitText":"square foot"'));assert(price.includes('"price":1'));assert(price.includes('Study fee examples'));
console.log(JSON.stringify({pages,bookingLinks,pricingConsistent:true,structuredDataValid:true,feeCalculatorAssets:true}));
