// Explicitly approved six-article release: two new URLs and four retained owners.
const fs=require('node:fs'),path=require('node:path'),base='https://www.stratumcostsegregation.com';
const D=JSON.parse(fs.readFileSync(path.join(__dirname,'content/str-faq-release/release.json'),'utf8'));
const esc=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
module.exports=function(out){
 const template=fs.readFileSync(path.join(out,'blog/cost-segregation-airbnb-properties/index.html'),'utf8');
 const sm=path.join(out,'sitemap.xml');let xml=fs.readFileSync(sm,'utf8');
 for(const a of D.pages){
  const url=base+a.route,f=path.join(out,a.route,'index.html');
  if(!a.new&&!fs.existsSync(f))throw Error('Missing existing owner '+a.route);
  let h=a.new?template:fs.readFileSync(f,'utf8');const pub=a.new?D.date:h.match(/"datePublished"\s*:\s*"([^"]+)"/)?.[1];
  const fragment=fs.readFileSync(path.join(__dirname,'content/str-faq-release',a.fragment),'utf8');
  if(a.new){
   const main='<main class="article" data-str-faq-release="'+a.id+'"><div class="breadcrumbs"><a href="/">Home</a> / <a href="/str-cost-segregation-resources/">STR resources</a></div><h1>'+esc(a.title)+'</h1><p class="meta">Published October 28, 2026 · Stratum Cost Segregation · <a href="/editorial-policy/">Editorial policy</a></p>'+fragment+'<aside class="str-owner-next"><h2>Continue your STR study review</h2><p><a href="/str-cost-segregation-resources/">STR and Airbnb resource center</a> · <a href="/blog/best-str-cost-segregation-company/">Compare study providers</a> · <a href="/cost-seg-discovery/">Discuss your property</a></p></aside></main>';
   h=h.replace(/<main\b[^>]*class="article"[^>]*>[\s\S]*?<\/main>/,()=>main);
   h=h.replace(/<title>[\s\S]*?<\/title>/,()=>'<title>'+esc(a.title)+' | Stratum</title>');
   h=h.replace(/<link\b[^>]*rel="canonical"[^>]*>/g,'').replace('</head>',()=>'<link rel="canonical" href="'+url+'"></head>');
   for(const [k,v]of [['description',a.description],['og:title',a.title+' | Stratum'],['twitter:title',a.title+' | Stratum'],['og:description',a.description],['twitter:description',a.description],['og:url',url],['twitter:url',url]]){const re=new RegExp('<meta\\s+(?:name|property)="'+k+'"\\s+content="[^"]*"\\s*/?>','i'),tag='<meta '+(k.startsWith('og:')?'property':'name')+'="'+k+'" content="'+esc(v)+'">';h=re.test(h)?h.replace(re,()=>tag):h.replace('</head>',()=>tag+'</head>');}
   h=h.replace(/<script\b[^>]*type="application\/ld\+json"[^>]*>[\s\S]*?<\/script>/g,'');
   const graph=[{'@type':'WebPage','@id':url+'#webpage',url,name:a.title,description:a.description,datePublished:D.date,dateModified:D.date},{'@type':'Organization','@id':base+'/#organization',name:'Stratum Cost Segregation',url:base+'/'},{'@type':'BlogPosting',headline:a.title,description:a.description,url,mainEntityOfPage:{'@id':url+'#webpage'},datePublished:D.date,dateModified:D.date,author:{'@id':base+'/#organization'},publisher:{'@id':base+'/#organization'}},{'@type':'BreadcrumbList',itemListElement:[{'@type':'ListItem',position:1,name:'Home',item:base+'/'},{'@type':'ListItem',position:2,name:a.title,item:url}]}];
   h=h.replace('</head>',()=>'<script type="application/ld+json">'+JSON.stringify({'@context':'https://schema.org','@graph':graph})+'</script></head>');
   fs.mkdirSync(path.dirname(f),{recursive:true});if(!xml.includes('<loc>'+url+'</loc>'))xml=xml.replace('</urlset>','<url><loc>'+url+'</loc><lastmod>'+D.date+'</lastmod></url>\n</urlset>');
  }else{
   const marker='<section id="str-faq-'+a.id+'" data-str-faq-release="'+a.id+'"><p class="meta">FAQ expansion updated October 28, 2026</p>'+fragment+'</section>';
   if(h.includes('data-str-faq-release'))throw Error('Duplicate FAQ expansion '+a.route);
   const target=h.includes('<aside class="str-owner-next">')?'<aside class="str-owner-next">':h.includes('<div class="cta-banner">')?'<div class="cta-banner">':'</main>';h=h.replace(target,()=>marker+target);
   h=h.replace(/<script\b([^>]*type="application\/ld\+json"[^>]*)>([\s\S]*?)<\/script>/g,(all,attrs,j)=>{const d=JSON.parse(j);for(const n of d['@graph']||[d])if(['WebPage','BlogPosting','Article'].includes(n['@type']))n.dateModified=D.date;return '<script'+attrs+'>'+JSON.stringify(d)+'</script>'});
  }
  if(!h.includes('data-str-faq-release="'+a.id+'"'))throw Error('FAQ content not inserted '+a.route);
  fs.writeFileSync(f,h);
 }
 const allLinks='<section class="section" data-str-faq-hub><div class="container"><h2>Detailed STR and Airbnb owner FAQs</h2><p>Work through financing, launch dates, ownership, participation and personal-use questions with practical records and primary references.</p><ul>'+D.pages.map(a=>'<li><a href="'+a.route+(a.new?'':'#str-faq-'+a.id)+'">'+esc(a.title)+'</a></li>').join('')+'</ul></div></section>';
 const hub=path.join(out,'str-cost-segregation-resources/index.html');let h=fs.readFileSync(hub,'utf8');h=h.replace('</main>',()=>allLinks+'</main>');fs.writeFileSync(hub,h);
 const blog=path.join(out,'blog/index.html');h=fs.readFileSync(blog,'utf8');const news='<section class="section" data-str-faq-blog><div class="container"><h2>New STR ownership FAQs</h2><ul>'+D.pages.filter(a=>a.new).map(a=>'<li><a href="'+a.route+'">'+esc(a.title)+'</a></li>').join('')+'</ul><p><a href="/str-cost-segregation-resources/">All STR and Airbnb guides</a></p></div></section>';h=h.includes('</main>')?h.replace('</main>',()=>news+'</main>'):h.replace('<footer',()=>news+'<footer');fs.writeFileSync(blog,h);
 const updated=new Set([...D.pages.map(a=>base+a.route),base+'/str-cost-segregation-resources/',base+'/blog/']);xml=xml.replace(/<url>\s*<loc>(.*?)<\/loc>([\s\S]*?)<\/url>/g,(all,u,tail)=>updated.has(u)?'<url><loc>'+u+'</loc>'+tail.replace(/<lastmod>.*?<\/lastmod>/g,'')+'<lastmod>'+D.date+'</lastmod></url>':all);fs.writeFileSync(sm,xml);
 fs.writeFileSync(path.join(__dirname,'outputs/str-faq-publication-manifest.json'),JSON.stringify({...D,newPageCount:D.pages.filter(a=>a.new).length,existingOwnerCount:D.pages.filter(a=>!a.new).length,hub:base+'/str-cost-segregation-resources/'},null,2)+'\n');
 console.log(JSON.stringify({strFaqNew:2,strFaqExisting:4,hubLinked:6}));
};
