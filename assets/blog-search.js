"use strict";
(() => {
  const input = document.getElementById('blog-search');
  if (!input) return;
  const cards = Array.from(document.querySelectorAll('.blog-card'));
  const entries = cards.map(card => ({card, text: card.textContent.toLowerCase()}));
  function filter() {
    const terms = input.value.toLowerCase().trim().split(/\s+/).filter(Boolean);
    let count = 0;
    for (const {card, text} of entries) {
      card.hidden = !terms.every(term => text.includes(term));
      if (!card.hidden) count++;
    }
    document.getElementById('blog-count').textContent = count
      ? `${count} ${count === 1 ? 'article' : 'articles'} shown.`
      : 'No matching articles. Try another topic or browse the resource center.';
  }
  input.addEventListener('input', filter);
  filter();
})();
