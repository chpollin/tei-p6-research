(() => {
  'use strict';
  const form = document.querySelector('.knowledge-filters');
  const search = document.getElementById('knowledge-search');
  const layer = document.getElementById('knowledge-layer');
  const entries = Array.from(document.querySelectorAll('.artifact'));
  function filter() {
    const terms = search.value.toLocaleLowerCase().trim().split(/\s+/).filter(Boolean);
    let count = 0;
    for (const entry of entries) {
      const matches = (!layer.value || entry.dataset.kind === layer.value) && terms.every(term => entry.dataset.search.toLocaleLowerCase().includes(term));
      entry.hidden = !matches;
      if (matches) count++;
    }
    for (const group of document.querySelectorAll('.knowledge-group')) group.hidden = !Array.from(group.querySelectorAll('.artifact')).some(entry => !entry.hidden);
    document.getElementById('knowledge-results').textContent = `${count} of ${entries.length} artifacts`;
    document.getElementById('knowledge-empty').hidden = count !== 0;
  }
  function reveal() {
    let id;
    try { id = decodeURIComponent(location.hash.slice(1)); } catch { return; }
    const target = document.getElementById(id);
    if (!target) return;
    const entry = target.closest('.artifact');
    if (entry) {
      search.value = ''; layer.value = ''; filter();
      entry.open = true;
      requestAnimationFrame(() => {
        target.scrollIntoView({block: 'start'});
        (target === entry ? entry.querySelector('summary') : target).focus({preventScroll: true});
      });
    }
  }
  form.addEventListener('submit', event => event.preventDefault());
  form.addEventListener('input', filter);
  form.addEventListener('reset', () => requestAnimationFrame(filter));
  window.addEventListener('hashchange', reveal);
  filter(); reveal();
})();
