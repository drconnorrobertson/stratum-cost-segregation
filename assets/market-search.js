"use strict";
(function(){
 const input=document.getElementById('market-search');if(!input)return;
 const entries=Array.from(document.querySelectorAll('.market-entry'));
 function filter(){
  const terms=input.value.toLowerCase().trim().split(/\s+/).filter(Boolean);let count=0;
  for(const entry of entries){entry.hidden=!terms.every(term=>entry.dataset.search.includes(term));if(!entry.hidden)count++;}
  for(const group of document.querySelectorAll('.market-state'))group.hidden=!Array.from(group.querySelectorAll('.market-entry')).some(entry=>!entry.hidden);
  document.getElementById('market-count').textContent=count?count+(count===1?' service area shown.':' service areas shown.'):'No matching service areas. Try a state or another city.';
 }
 input.addEventListener('input',filter);filter();
})();
