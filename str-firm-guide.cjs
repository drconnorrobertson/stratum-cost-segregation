// Preserve the existing STR buying-intent URL; never generate a competing landing page.
const fs=require('node:fs'),path=require('node:path');
const route='/blog/best-str-cost-segregation-company/',date='2026-10-28',base='https://www.stratumcostsegregation.com';
module.exports=function(out){
 const file=path.join(out,route,'index.html');let h=fs.readFileSync(file,'utf8');
 const body=fs.readFileSync(path.join(__dirname,'content/str-firm-guide.html'),'utf8');
 if(!/<main class="article">[\s\S]*?<\/main>/.test(h))throw Error('STR buying guide shell changed');
 h=h.replace(/<main class="article">[\s\S]*?<\/main>/,()=>'<main class="article" data-str-firm-guide>'+body+'</main>');
 const title='Best STR Cost Seg Firm: Compare Scope & Fees | Stratum';
 const desc='Choose the best STR cost seg firm for your Airbnb or vacation rental. Compare study evidence, fees, CPA handoff and provider questions with a practical checklist.';
 const esc=s=>s.replaceAll('&','&amp;').replaceAll('"','&quot;');
 h=h.replace(/<title>[\s\S]*?<\/title>/,()=>'<title>'+esc(title)+'</title>');
 for(const [key,value] of [['description',desc],['og:title',title],['og:description',desc],['twitter:title',title],['twitter:description',desc]]){
  const re=new RegExp('<meta (?:name|property)="'+key+'" content="[^"]*">');
  const tag='<meta '+(key.startsWith('og:')?'property':'name')+'="'+key+'" content="'+esc(value)+'">';
  h=re.test(h)?h.replace(re,()=>tag):h.replace('</head>',()=>tag+'</head>');
 }
 h=h.replace(/<script type="application\/ld\+json">([\s\S]*?)<\/script>/g,(all,json)=>{
  const data=JSON.parse(json);for(const n of data['@graph']||[data])if(['WebPage','BlogPosting'].includes(n['@type'])){n.dateModified=date;if(n['@type']==='WebPage'){n.name=title;n.description=desc}else{n.headline='How to Choose the Best STR Cost Seg Firm';n.description=desc}}
  return '<script type="application/ld+json">'+JSON.stringify(data)+'</script>';
 });
 h=h.replace('</head>','<link rel="stylesheet" href="/assets/str-firm-guide.css"></head>');fs.writeFileSync(file,h);
 const targets=['/','/short-term-rental-cost-segregation/','/str-cost-segregation-resources/','/resources/','/compare/','/blog/how-to-choose-cost-segregation-company/'];
 for(const r of targets){const f=path.join(out,r,'index.html');let s=fs.readFileSync(f,'utf8');
  const block='<section class="section str-firm-entry" data-str-firm-entry><div class="container"><h2>Choosing a cost seg firm for your STR?</h2><p>Compare the written scope, furnishing records, study fee and CPA handoff for your Airbnb or vacation rental.</p><p><a href="'+route+'">How to choose the best STR cost seg firm</a> · <a href="/assets/downloads/str-firm-proposal-comparison.csv" download>Download the proposal checklist</a></p></div></section>';
  if(s.includes('data-str-firm-entry'))throw Error('Duplicate STR guide entry '+r);
  const close=s.includes('</main>')?'</main>':'<footer';s=s.replace(close,()=>block+close);fs.writeFileSync(f,s);
 }
 const rows=[['Selection criterion','Provider A written answer','Provider B written answer','Provider C written answer','Source or proposal date','Open question'],...['Preparer and reviewer','Inspection and missing records','Basis and furniture reconciliation','Component evidence and report example','Report and schedule format','Total fee and exclusions','Delivery dependencies','CPA implementation responsibility','Correction and examination support'].map(x=>[x,'','','','',''])];
 fs.writeFileSync(path.join(out,'assets/downloads/str-firm-proposal-comparison.csv'),rows.map(r=>r.map(x=>'"'+x.replaceAll('"','""')+'"').join(',')).join('\r\n')+'\r\n');
 fs.writeFileSync(path.join(out,'assets/str-firm-guide.css'),'.str-firm-table{max-width:100%;overflow-x:auto;margin:24px 0}.str-firm-table table{width:100%;border-collapse:collapse;font-size:.95rem}.str-firm-table th,.str-firm-table td{padding:12px;text-align:left;vertical-align:top;border-bottom:1px solid #ccd4df;overflow-wrap:anywhere}.str-firm-table th{font-weight:700}.str-firm-table caption{text-align:left;font-weight:700;padding:12px 0}.str-firm-entry p{max-width:75ch}@media(max-width:600px){.str-firm-table th,.str-firm-table td{padding:8px;font-size:.85rem}main[data-str-firm-guide] nav ul{padding-left:20px}}');
 const sm=path.join(out,'sitemap.xml');let xml=fs.readFileSync(sm,'utf8');for(const r of [route,...targets]){const url=base+r;xml=xml.replace(/<url>\s*<loc>(.*?)<\/loc>([\s\S]*?)<\/url>/g,(all,u,tail)=>u===url?'<url><loc>'+u+'</loc>'+tail.replace(/<lastmod>.*?<\/lastmod>/g,'')+'<lastmod>'+date+'</lastmod></url>':all)}fs.writeFileSync(sm,xml);
 console.log('Updated existing STR firm buying guide and six contextual entry points.');
};
