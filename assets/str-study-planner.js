"use strict";
(function(){
 const form=document.getElementById('study-planner');if(!form)return;
 const list=document.getElementById('checklist-items');
 const base=Array.from(list.children).map(item=>item.textContent);
 const groups={"furnished": ["Furnished purchase", ["Executed seller inventory and bill of sale", "Closing credits and excluded items", "Post-closing furniture receipts and replacement log"]], "condo": ["Condo or shared property", ["Deed and condominium declaration", "Association assessment notices and project descriptions", "Owner-versus-association asset inventory"]], "renovation": ["Renovations", ["Final contractor scope and approved change orders", "Payment reconciliation including deposits and credits", "Improvement completion dates and replaced-asset records"]], "personal": ["Personal or mixed use", ["Floor plan of guest-only, owner-only, and shared space", "Rental and personal-use calendar", "Conversion history and basis questions for the preparer"]], "manager": ["Manager records", ["Vendor invoices underlying capital charges", "Management agreement and asset-ownership explanation", "Manager inventory and rental-availability timeline"]], "portfolio": ["Multiple properties", ["Entity-to-property identifier map", "Separate basis and acquisition file for each property", "Bulk purchase allocations and furniture-transfer register"]], "existing": ["Previously depreciated property", ["Latest depreciation and fixed-asset schedules", "Prior study, if any, and implementation records", "List of assets retained, removed, replaced, or transferred"]]};
 function items(){
  return base.concat(Array.from(form.querySelectorAll('input:checked')).flatMap(input=>groups[input.value][1]));
 }
 function render(){
  const records=items();list.replaceChildren();
  for(const record of records){const li=document.createElement('li');li.textContent=record;list.appendChild(li);}
  document.getElementById('planner-status').textContent=records.length+' records or questions on your checklist. This is document planning, not an eligibility result.';
 }
 form.addEventListener('change',render);
 form.addEventListener('submit',event=>event.preventDefault());
 form.addEventListener('reset',()=>setTimeout(render,0));
 document.getElementById('print-checklist').addEventListener('click',()=>window.print());
 document.getElementById('download-checklist').addEventListener('click',()=>{
  const content='STR study preparation checklist\n\n'+items().map(item=>'[ ] '+item).join('\n')+'\n\nOrganizing aid only; confirm the scope and tax treatment with your advisers.\n';
  const url=URL.createObjectURL(new Blob([content],{type:'text/plain;charset=utf-8'}));
  const a=document.createElement('a');a.href=url;a.download='str-study-checklist.txt';document.body.appendChild(a);a.click();a.remove();setTimeout(()=>URL.revokeObjectURL(url),1000);
 });
})();
