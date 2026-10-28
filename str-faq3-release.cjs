// Third human-approved FAQ batch: expand four existing canonical owners, without adding URLs.
const fs=require('node:fs'),path=require('node:path'),base='https://www.stratumcostsegregation.com';
const D=JSON.parse(fs.readFileSync(path.join(__dirname,'content/str-faq3-release/release.json'),'utf8'));
const esc=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
module.exports=function(out){
 const template=fs.readFileSync(path.join(out,'blog/cost-segregation-airbnb-properties/index.html'),'utf8');
 const sm=path.join(out,'sitemap.xml');let xml=fs.readFileSync(sm,'utf8');
 for(const a of D.pages){
  const url=base+a.route,f=path.join(out,a.route,'index.html');if(!a.new&&!fs.existsSync(f))throw Error('Missing canonical owner '+a.route);
  let h=a.new?template:fs.readFileSync(f,'utf8');const publication=a.new?D.date:h.match(/"datePublished"\s*:\s*"([^"]+)"/)?.[1];
  const fragment=fs.readFileSync(path.join(__dirname,'content/str-faq3-release',a.fragment),'utf8');
  const main='<main class="article" data-str-faq-release="'+a.id+'"><div class="breadcrumbs"><a href="/">Home</a> / <a href="/str-cost-segregation-resources/">STR resources</a></div><h1>'+esc(a.title)+'</h1><p class="meta">'+(publication?'Published '+publication+' · ':'')+'Updated October 28, 2026 · Stratum Cost Segregation · <a href="/editorial-policy/">Editorial policy</a></p>'+fragment+'<aside class="str-owner-next"><h2>Continue your STR study review</h2><p><a href="/str-cost-segregation-resources/">STR and Airbnb resource center</a> · <a href="/blog/best-str-cost-segregation-company/">Compare study providers</a> · <a href="/cost-seg-discovery/">Discuss your property</a></p></aside></main>';
  const shell=/<(main|article)\b[^>]*class="article(?: [^"]*)?"[^>]*>[\s\S]*?<\/\1>/;if(!shell.test(h))throw Error('Missing article shell '+a.route);h=h.replace(shell,()=>main);
  h=h.replace(/<title>[\s\S]*?<\/title>/,()=>'<title>'+esc(a.title)+' | Stratum</title>').replace(/<link\b[^>]*rel="canonical"[^>]*>/g,'').replace('</head>',()=>'<link rel="canonical" href="'+url+'"></head>');
  for(const[k,v]of[['description',a.description],['og:title',a.title+' | Stratum'],['twitter:title',a.title+' | Stratum'],['og:description',a.description],['twitter:description',a.description],['og:url',url],['twitter:url',url]]){const re=new RegExp('<meta\\s+(?:name|property)="'+k+'"\\s+content="[^"]*"\\s*/?>','i'),tag='<meta '+(k.startsWith('og:')?'property':'name')+'="'+k+'" content="'+esc(v)+'">';h=re.test(h)?h.replace(re,()=>tag):h.replace('</head>',()=>tag+'</head>');}
  h=h.replace(/<script\b[^>]*type="application\/ld\+json"[^>]*>[\s\S]*?<\/script>/g,'');
  const graph=[{'@type':'WebPage','@id':url+'#webpage',url,name:a.title,description:a.description,dateModified:D.date},{'@type':'Organization','@id':base+'/#organization',name:'Stratum Cost Segregation',url:base+'/'},{'@type':a.route.startsWith('/blog/')?'BlogPosting':'Article',headline:a.title,description:a.description,url,mainEntityOfPage:{'@id':url+'#webpage'},...(publication?{datePublished:publication}:{}),dateModified:D.date,author:{'@id':base+'/#organization'},publisher:{'@id':base+'/#organization'}},{'@type':'BreadcrumbList',itemListElement:[{'@type':'ListItem',position:1,name:'Home',item:base+'/'},{'@type':'ListItem',position:2,name:a.title,item:url}]}];
  h=h.replace('</head>',()=>'<script type="application/ld+json">'+JSON.stringify({'@context':'https://schema.org','@graph':graph})+'</script></head>');fs.mkdirSync(path.dirname(f),{recursive:true});fs.writeFileSync(f,h);
  if(a.new&&!xml.includes('<loc>'+url+'</loc>'))xml=xml.replace('</urlset>','<url><loc>'+url+'</loc><lastmod>'+D.date+'</lastmod></url>\n</urlset>');
 }
 const links='<section class="section" data-str-faq3-hub><div class="container"><h2>Conversion, ADU, smaller-property and furnishing FAQs</h2><p>Review conversion basis, shared ADU costs, smaller-property economics and missing furniture records.</p><ul>'+D.pages.map(a=>'<li><a href="'+a.route+'">'+esc(a.title)+'</a></li>').join('')+'</ul></div></section>';
 const hub=path.join(out,'str-cost-segregation-resources/index.html');let h=fs.readFileSync(hub,'utf8');h=h.replace('</main>',()=>links+'</main>');fs.writeFileSync(hub,h);

 const changed=new Set([...D.pages.map(a=>base+a.route),base+'/str-cost-segregation-resources/',base+'/blog/']);xml=xml.replace(/<url>\s*<loc>(.*?)<\/loc>([\s\S]*?)<\/url>/g,(all,u,tail)=>changed.has(u)?'<url><loc>'+u+'</loc>'+tail.replace(/<lastmod>.*?<\/lastmod>/g,'')+'<lastmod>'+D.date+'</lastmod></url>':all);fs.writeFileSync(sm,xml);
 fs.writeFileSync(path.join(__dirname,'outputs/str-faq3-publication-manifest.json'),JSON.stringify(D,null,2)+'\n');console.log(JSON.stringify({strFaqBatch3:4,newPages:0,existingOwners:4}));
};
