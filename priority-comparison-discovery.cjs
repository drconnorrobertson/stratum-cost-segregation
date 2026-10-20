const fs=require('fs'),path=require('path');
module.exports=function(out){
 const providers=require('./content/competitor-comparisons/providers.json');
 const research=require('./content/competitor-comparisons/priority-research.json');
 const names={'seneca-cost-segregation':'Seneca','re-cost-seg':'RE Cost Seg',kbkg:'KBKG','maven-cost-segregation':'Maven',cssi:'CSSI'};
 const block='<section class="priority-directory priority-site-entry" aria-label="Cost segregation provider comparisons"><p class="eyebrow">Compare your options</p><h2>Comparing cost segregation companies?</h2><p>Review pricing, study scope, property evidence and CPA handoff before choosing a provider. Stratum charges $1 per square foot with a $2,000 minimum per property.</p><div class="comparison-grid">'+Object.keys(names).map(key=>{const p=providers.find(p=>p.slug===key);return '<div class="comparison-card"><h3>'+p.name+'</h3><p>'+research[key].decision+'</p><p><a href="/compare/'+key+'-vs-stratum/">'+names[key]+' vs Stratum</a></p><p><a href="/compare/'+key+'-alternatives/">'+names[key]+' alternatives</a></p><p><a href="/compare/'+key+'-reviews/">'+names[key]+' reviews</a> · <a href="/compare/'+key+'-pricing/">pricing guide</a></p></div>';}).join('')+'</div><p><a href="/compare/">Browse all provider comparisons</a></p></section>';
 const targets=['index.html','pricing/index.html','resources/index.html','blog/how-to-choose-cost-segregation-company/index.html','blog/cost-segregation-study-cost-pricing/index.html'];
 let count=0;
 function walk(dir){for(const e of fs.readdirSync(dir,{withFileTypes:true})){
 const f=path.join(dir,e.name);if(e.isDirectory()){walk(f);continue;}if(!f.endsWith('.html'))continue;
 let h=fs.readFileSync(f,'utf8'),before=h,rel=path.relative(out,f);
 h=h.replace('<a href="/blog/how-to-choose-cost-segregation-company/">Compare providers</a>','<a href="/compare/">Compare providers</a>');
 if(targets.includes(rel))h=h.replace('<section class="site-study-cta"',block+'<section class="site-study-cta"');
 for(const [key,name] of Object.entries(names))for(const type of ['vs-stratum','alternatives'])if(rel==='compare/'+key+'-'+type+'/index.html'){
 const title=type==='vs-stratum'?name+' vs Stratum: Cost Segregation Pricing & Scope':name+' Alternatives: Cost Segregation Comparison';
 const desc=type==='vs-stratum'?'Compare '+name+' and Stratum on study pricing, inspection scope, report delivery and CPA support. Stratum: $1/sq ft, $2,000 minimum per property.':'Compare alternatives to '+name+' by study scope, pricing and CPA handoff. Review source-backed provider details and Stratum’s $1/sq ft, $2,000 minimum.';
 h=h.replace(/<title>[\s\S]*?<\/title>/,'<title>'+title+' | Stratum</title>').replace(/(<meta\b[^>]*(?:name="description"|property="og:description"|name="twitter:description")[^>]*content=")[^"]*"/g,(_,prefix)=>prefix+desc+'"').replace(/(<meta\b[^>]*(?:property="og:title"|name="twitter:title")[^>]*content=")[^"]*"/g,(_,prefix)=>prefix+title+' | Stratum"');
 }
 if(h!==before){fs.writeFileSync(f,h);count++;}
 }}walk(out);console.log('Priority comparison discovery improvements: '+count+' pages');
};
