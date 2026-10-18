'use strict';
const fs=require('node:fs'),path=require('node:path');
const hosts=new Set(['www.stratumcostsegregation.com','stratumcostsegregation.com','stratumcostseg.com','www.stratumcostseg.com']);
function clean(href){
 if(!/[?&](?:amp;)?utm_/i.test(href)||!href.startsWith('/')&&!href.startsWith('https://'))return href;
 const decoded=href.replace(/&amp;/g,'&'),url=new URL(decoded,'https://www.stratumcostsegregation.com');
 if(!hosts.has(url.hostname))return href;
 for(const key of [...url.searchParams.keys()])if(/^utm_/i.test(key))url.searchParams.delete(key);
 const result=href.startsWith('/')?url.pathname+url.search+url.hash:url.href;
 return result.replace(/&/g,'&amp;');
}
function apply(root){let links=0;function walk(dir){for(const e of fs.readdirSync(dir,{withFileTypes:true})){const p=path.join(dir,e.name);if(e.isDirectory())walk(p);else if(e.name.endsWith('.html')){const s=fs.readFileSync(p,'utf8'),t=s.replace(/(href=")([^"]+)(")/g,(_,a,u,b)=>{const v=clean(u);if(v!==u)links++;return a+v+b;});if(t!==s)fs.writeFileSync(p,t);}}}walk(root);console.log(`Cleaned ${links} same-site campaign links; external referral tags retained.`);}
if(require.main===module)apply(path.resolve(__dirname,'../public'));
module.exports={clean,apply};
