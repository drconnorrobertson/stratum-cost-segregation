// Public HTTPS release verification. No tokens, client records or private data.
const pages = [
 ['/blog/cost-segregation-retail-properties/', 'Retail Center Cost Segregation Studies | Stratum', 'Discuss My Retail Property'],
 ['/blog/cost-segregation-apartment-buildings/', 'Apartment Cost Segregation: Study Scope | Stratum', 'Prepare an apartment-building study review'],
 ['/blog/cost-segregation-medical-office-buildings/', 'Medical Office Cost Segregation Studies | Stratum', 'Define your medical-office study scope'],
];
(async()=>{
 for(const [path,title,content] of pages){
  const url='https://www.stratumcostsegregation.com'+path;
  try{
   const response=await fetch(url,{signal:AbortSignal.timeout(20000)});
   const body=await response.text();
   const actual=body.match(/<title>(.*?)<\/title>/s)?.[1].replaceAll('&amp;','&');
   const passed=response.status===200&&new URL(response.url).hostname==='www.stratumcostsegregation.com'&&actual===title&&body.includes(content)&&body.split('<!-- search-intent:start -->').length===2;
   console.log(JSON.stringify({releaseVerification:true,url,status:response.status,title:actual,passed}));
  }catch(error){console.log(JSON.stringify({releaseVerification:true,url,passed:false,error:error.message}));}
 }
})();
