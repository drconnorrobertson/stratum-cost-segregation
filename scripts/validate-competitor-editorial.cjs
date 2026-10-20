const fs=require('fs'),path=require('path'),assert=require('node:assert/strict');
const root=path.join(__dirname,'../public'),r=require('../content/competitor-comparisons/editorial-research.json');const sm=fs.readFileSync(path.join(root,'sitemap.xml'),'utf8');let n=0;
for(const [key,p] of Object.entries(r))for(const suffix of ['-reviews','-pricing']){
 const route='/compare/'+key+suffix+'/',h=fs.readFileSync(path.join(root,route,'index.html'),'utf8');
 assert(h.includes('href="https://www.stratumcostsegregation.com'+route+'"'));assert(sm.includes('<loc>https://www.stratumcostsegregation.com'+route+'</loc>'));assert.equal((h.match(/<h1\b/g)||[]).length,1);assert(h.includes(p.source));assert(h.includes(p.checked));assert(h.includes('/assets/shared-site-shell.css'));assert(h.includes('$2,000 minimum per property'));
 assert(!/"@type":"(?:Review|AggregateRating)"/.test(h));
 if(suffix==='-reviews'){assert(h.includes('competing cost segregation provider'));assert(h.includes('We do not assign stars'));assert(h.includes(p.reviewSource));}
 for(const m of h.matchAll(/href="(\/[^"<>]+)"/g)){const u=new URL(m[1].replaceAll('&amp;','&'),'https://example.com');assert(fs.existsSync(path.join(root,u.pathname,u.pathname.endsWith('/')?'index.html':'')),m[1]);}
 n++;
}
assert.equal(n,10);console.log(JSON.stringify({newEditorialPages:n,sources:true,noInventedRatings:true,pricing:true,links:true}));
