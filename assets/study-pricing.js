(() => {
  const money = new Intl.NumberFormat('en-US', {style: 'currency', currency: 'USD', maximumFractionDigits: 2});
  const script = document.currentScript;
  fetch(new URL('study-pricing-policy.json', script.src)).then(r => {
    if (!r.ok) throw new Error('Pricing unavailable');
    return r.json();
  }).then(policy => {
    document.querySelectorAll('[data-study-fee]').forEach(form => {
      form.addEventListener('submit', event => {
        event.preventDefault();
        if (!form.reportValidity()) return;
        const sqft = Number(form.elements.squareFeet.value);
        if (!Number.isFinite(sqft) || sqft <= 0) return;
        form.querySelector('[data-fee-result]').textContent = 'Study fee: ' + money.format(Math.max(policy.minimumPerProperty, sqft * policy.perSquareFoot)) + ' for this property.';
        if (window.va) window.va('event', {name: 'Study Fee Calculated', data: {path: location.pathname}});
      });
    });
  }).catch(() => {
    document.querySelectorAll('[data-fee-result]').forEach(el => {el.textContent = 'Study fee = the greater of $2,000 or square footage × $1. Review pricing with our team.';});
  });
  document.addEventListener('click', event => {
    const link = event.target.closest('a[href^="/cost-seg-discovery/"]');
    if (link && window.va) window.va('event', {name: 'Cost Seg Discovery Click', data: {path: location.pathname, placement: link.closest('nav') ? 'navigation' : link.closest('footer') ? 'footer' : 'content'}});
  });
})();
