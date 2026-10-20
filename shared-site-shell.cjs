// Reuse the homepage's actual navigation, footer and design tokens on generated pages.
const fs=require('fs'),path=require('path');
module.exports=function(out){
 const home=fs.readFileSync(path.join(out,'index.html'),'utf8');
 const nav=home.match(/<nav class="nav"[\s\S]*?<\/nav>/)?.[0];
 const footer=home.match(/<footer class="footer"[\s\S]*?<\/footer>/)?.[0];
 const navigation=home.match(/\/\/ Navigation behavior([\s\S]*?)\/\/ Scroll-triggered/)?.[1];
 if(!nav||!footer||!navigation)throw Error('Homepage shared navigation/footer not found');
 fs.writeFileSync(path.join(out,'assets/shared-site-navigation.js'),navigation);
 const fonts='<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">';
 const styles='<link rel="stylesheet" href="/style.css?v=20261019"><link rel="stylesheet" href="/assets/shared-site-shell.css?v=20261019"><script defer src="/assets/shared-site-navigation.js"></script>';
 const pricing='<section class="comparison-price-band" aria-label="Stratum study pricing"><div><span class="eyebrow">Stratum cost segregation pricing</span><p><strong>$1 per square foot</strong><span>$2,000 minimum per property</span></p></div><a class="btn btn-gold" href="/cost-seg-discovery/">Book a Cost Seg Discovery Call</a></section>';
 let count=0;
 function walk(dir){for(const entry of fs.readdirSync(dir,{withFileTypes:true})){
  const file=path.join(dir,entry.name);if(entry.isDirectory()){walk(file);continue;}if(!file.endsWith('.html'))continue;
  let h=fs.readFileSync(file,'utf8');const rel=path.relative(out,file),booking=rel==='cost-seg-discovery/index.html';
  if(!booking&&!h.includes('href="/assets/provider-comparisons.css"'))continue;
  if(booking){
   h=h.replace(/<style>[\s\S]*?<\/style>/g,'');
   h=h.replace(/<link\b[^>]*(?:fonts\.googleapis\.com|fonts\.gstatic\.com)[^>]*>/g,'');
   h=h.replace(/<body[^>]*>/,'<body class="comparison-page discovery-page">'+nav);
   h=h.replace(/<main class="wrap">/,'<main class="comparison-main discovery-main">');
   h=h.replace(/<a href="\/" class="brand"[^>]*>[\s\S]*?<\/a>/,'');
   h=h.replace('<div class="cols">','<div class="discovery-layout">');
   h=h.replace(/scrolling="no"/,'scrolling="yes"');
   h=h.replace(/<section>\s*<h2>Schedule a Call<\/h2>/,'<section class="calendar-section" id="schedule"><h2>Schedule a Call</h2>');
   h=h.replace('<div class="discovery-layout">','<div class="discovery-price"><strong>$1 per square foot</strong><span>$2,000 minimum per property</span><a href="/pricing/">Review study pricing</a></div><div class="discovery-layout">');
   h=h.replace('</main>','</main>'+footer);
   h=h.replace(/(<a\b[^>]*href=")\/cost-seg-discovery\/("[^>]*>)/g,'$1#schedule$2');
   h=h.replace('</head>','<link rel="preconnect" href="https://api.leadconnectorhq.com"></head>');
  }else{
   h=h.replace('<body>','<body class="comparison-page">').replace(/<header>[\s\S]*?<\/header>/,()=>nav).replace(/<footer>[\s\S]*?<\/footer>/,()=>footer);
   h=h.replace(/<main>([\s\S]*?)(?=<section\b)/,(_,intro)=>'<main class="comparison-main"><div class="comparison-hero">'+intro+'</div>'+pricing);
   h=h.replace(/class="button"/g,'class="btn btn-gold"');
   h=h.replace(/<div class="table-scroll">/g,'<div class="table-scroll" tabindex="0" role="region" aria-label="Scrollable comparison table">');
   h=h.replace('<link rel="stylesheet" href="/assets/provider-comparisons.css">','');
   if(rel==='compare/cost-segregation-company-pricing/index.html'){
    h=h.replace('<tbody>','<tbody><tr class="stratum-price-row" data-provider><th scope="row"><a href="/pricing/">Stratum Cost Segregation pricing</a></th><td><strong>$1 per square foot, with a $2,000 minimum per property.</strong> Apply the rate and minimum separately to each property in a portfolio.</td><td><a href="/pricing/">Current Stratum pricing</a></td></tr>');
    h=h.replace(/\d+ provider entries/,'56 provider entries');
   }
  }
  h=h.replace('</head>',fonts+styles+'</head>');
  if(!h.includes('/_vercel/insights/script.js'))h=h.replace('</head>','<script>window.va=window.va||function(){(window.vaq=window.vaq||[]).push(arguments)};</script><script defer src="/_vercel/insights/script.js"></script></head>');
  fs.writeFileSync(file,h);count++;
 }}walk(out);
 console.log('Applied homepage navigation, footer and responsive design to '+count+' pages');
};
