const fs=require('fs'),path=require('path'),assert=require('node:assert/strict');
const root=path.join(__dirname,'../public');let count=0;
function walk(dir){for(const e of fs.readdirSync(dir,{withFileTypes:true})){
 const f=path.join(dir,e.name);if(e.isDirectory()){walk(f);continue;}if(!f.endsWith('.html'))continue;
 const h=fs.readFileSync(f,'utf8');if(!/<body\b/.test(h))continue;count++;
 assert.equal((h.match(/id="main-nav"/g)||[]).length,1,f);
 assert.equal((h.match(/<footer class="footer"/g)||[]).length,1,f);
 assert.equal((h.match(/src="\/assets\/shared-site-navigation.js"/g)||[]).length,1,f);
 assert(h.includes('/assets/sitewide-consistency.css'),f);
 assert(h.includes('$1 per square foot')&&h.includes('$2,000 minimum'),f);
 assert(!h.includes('href="/assets/decision-library.css"'),f);
 assert(!h.includes('// Navigation behavior'),f);
 assert(!h.includes('A professional study from Stratum typically ranges'),f);
 if(!f.endsWith('/404.html'))for(const a of h.matchAll(/<a\b[^>]*class="[^"]*\b(?:btn|button|nav-cta)\b[^>]*>[\s\S]*?<\/a>/g))assert(/href="(?:\/cost-seg-discovery\/|#schedule)"/.test(a[0]),f+' '+a[0]);
 for(const m of h.matchAll(/<script type="application\/ld\+json">([\s\S]*?)<\/script>/g))JSON.parse(m[1]);
}}
walk(root);assert(count>=1338);console.log(JSON.stringify({allPublicPages:count,homepageShell:true,pricing:true,conversionDestinations:true,jsonLd:true}));
