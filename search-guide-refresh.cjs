// Retain curated guide revisions without adding a Python deployment dependency.
const fs=require('fs'),path=require('path');
const regex=s=>s.replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
module.exports=function(out){
 fs.copyFileSync(path.join(__dirname,"df96e877fd4023ffc463bfe1ffbc9a1b.txt"),path.join(out,"df96e877fd4023ffc463bfe1ffbc9a1b.txt"));
 const overrides=JSON.parse(fs.readFileSync(path.join(__dirname,'content/search-guide-overrides.json'),'utf8'));
 for(const item of overrides){
  const file=path.join(out,item.path),url='https://www.stratumcostsegregation.com/'+item.path.replace(/index.html$/,'');
  let text=fs.readFileSync(file,'utf8');
  if(!/<article class="article"[^>]*>[\s\S]*?<\/article>/.test(text))throw Error('Missing guide shell '+file);
  text=text.replace(/<article class="article"[^>]*>[\s\S]*?<\/article>/,()=>item.article);
  text=text.replace(/<title>[\s\S]*?<\/title>/,()=>item.titleTag);
  for(const meta of item.meta){const re=new RegExp('<meta (?:name|property)="'+regex(meta.key)+'" content="[^"]*">');text=text.replace(re,()=>meta.tag);}
  text=text.replace(/<script type="application\/ld\+json">[\s\S]*?<\/script>/,()=>item.schema);
  fs.writeFileSync(file,text);
  const sm=path.join(out,'sitemap.xml');let xml=fs.readFileSync(sm,'utf8');
  const re=new RegExp('(<url>\\s*<loc>'+regex(url)+'</loc>)([\\s\\S]*?)(</url>)');
  if(!re.test(xml))throw Error('Missing sitemap entry '+url);
  xml=xml.replace(re,(_,start,tail,end)=>start+'<lastmod>2026-10-09</lastmod>'+tail.replace(/<lastmod>.*?<\/lastmod>/g,'').trim()+end);fs.writeFileSync(sm,xml);
 }
 console.log('Applied '+overrides.length+' curated search guide revisions.');
};
