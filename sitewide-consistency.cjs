// Final pass over every public page; verification files are deliberately left intact.
const fs=require('fs'),path=require('path');
module.exports=function(out){
 const home=fs.readFileSync(path.join(out,'index.html'),'utf8');
 const nav=home.match(/<nav class="nav"[\s\S]*?<\/nav>/)[0];
 const footer=home.match(/<footer class="footer"[\s\S]*?<\/footer>/)[0];
 const band='<section class="site-study-cta" aria-label="Study pricing and discovery call"><div><h2>Cost segregation. Clear pricing.</h2><p><strong>$1 per square foot</strong> · $2,000 minimum per property.</p></div><a class="btn btn-gold" href="/cost-seg-discovery/">Book a Cost Seg Discovery Call</a></section>';
 let pages=0,legacy=0;
 function walk(dir){for(const e of fs.readdirSync(dir,{withFileTypes:true})){
 const f=path.join(dir,e.name);if(e.isDirectory()){walk(f);continue;}if(!f.endsWith('.html'))continue;
 let h=fs.readFileSync(f,'utf8');if(!/<body\b/i.test(h))continue;
 const rel=path.relative(out,f),library=h.includes('href="/assets/decision-library.css"');
 // Replace retained navigation without touching article breadcrumb/contents navigation.
 if(/<nav class="nav"/.test(h))h=h.replace(/<nav class="nav"[\s\S]*?<\/nav>/,()=>nav);
 else if(library)h=h.replace(/<header>[\s\S]*?<\/header>/,()=>nav);
 else h=h.replace(/<body[^>]*>/,m=>m+nav);
 h=h.replace(/<footer(?: class="footer")?>[\s\S]*?<\/footer>/,()=>footer);
 if(!h.includes('<footer class="footer"'))h=h.replace('</body>',footer+'</body>');
 // One navigation listener prevents double toggles on pages that already had inline navigation.
 h=h.replace(/\/\/ Navigation behavior[\s\S]*?(?=\/\/ Scroll-triggered)/g,'');
 h=h.replace(/<script\b[^>]*src="\/assets\/shared-site-navigation.js"[^>]*><\/script>/g,'');
 h=h.replace(/<link\b[^>]*href="(?:\.\.\/|\.\/)*\/?style\.css[^"<>]*"[^>]*>/g,'');
 if(library){
  legacy++;h=h.replace(/<link\b[^>]*href="\/assets\/(?:decision-library|topical-depth)\.css"[^>]*>/g,'');
  h=h.replace('<body>','<body class="site-library">');
 }
 h=h.replace('</head>','<link rel="stylesheet" href="/style.css?v=20261019"><link rel="stylesheet" href="/assets/sitewide-consistency.css?v=20261019"><script defer src="/assets/shared-site-navigation.js"></script></head>');
 if(!h.includes('name="viewport"'))h=h.replace('</head>','<meta name="viewport" content="width=device-width, initial-scale=1"></head>');
 // Editorial links and calculator controls stay functional; conversion buttons use one destination.
 h=h.replace(/<a\b([^>]*class="[^"]*\b(?:btn|button|nav-cta)\b[^>]*")([^>]*)>[\s\S]*?<\/a>/g,(a)=>{
  if(rel==='404.html'||/href="#schedule"/.test(a))return a;
  return a.replace(/href="[^"]*"/,'href="/cost-seg-discovery/"').replace(/>[\s\S]*?<\/a>$/,'>Book a Cost Seg Discovery Call</a>');
 });
 if(rel!=='cost-seg-discovery/index.html'&&!h.includes('site-study-cta'))h=h.replace(/<footer class="footer"/,band+'<footer class="footer"');
 if(rel==='cost-seg-discovery/index.html')h=h.replace(/href="\/cost-seg-discovery\/"/g,'href="#schedule"');
 // Wrap tables that were missing a contained horizontal scroll region.
 h=h.replace(/<table\b[\s\S]*?<\/table>/g,(table,offset)=>{
  const before=h.slice(Math.max(0,offset-250),offset);return /<div[^>]*class="(?:table-scroll|table-wrap)"[^>]*>\s*$/.test(before)?table:'<div class="table-scroll" tabindex="0" role="region" aria-label="Scrollable data table">'+table+'</div>';
 });
 fs.writeFileSync(f,h);pages++;
 }}walk(out);
 console.log(JSON.stringify({sitewidePages:pages,legacyLibraryPages:legacy}));
};
