(() => {
  'use strict';
  const form = document.querySelector('.knowledge-filters');
  const search = document.getElementById('knowledge-search');
  const layer = document.getElementById('knowledge-layer');
  const status = document.getElementById('knowledge-status');
  const topic = document.getElementById('knowledge-topic');
  const moduleFilter = document.getElementById('knowledge-module');
  const sourceKind = document.getElementById('knowledge-source-kind');
  const ranked = document.getElementById('knowledge-ranked');
  const hits = document.getElementById('knowledge-hits');
  const entries = Array.from(document.querySelectorAll('.artifact'));
  const words = text => text.toLowerCase().match(/[\p{L}\p{N}_]+(?:[.-][\p{L}\p{N}_]+)*/gu) || [];
  const records = entries.map((entry, order) => {
    const title = entry.querySelector('.artifact-title').textContent;
    const passages = Array.from(entry.querySelectorAll('.passage'));
    const body = passages.map(passage => passage.textContent).join(' ').toLowerCase();
    return {entry, order, title, titleWords: new Set(words(title)),
      passageWords: passages.map(passage => new Set(words(passage.textContent))),
      words: new Set(words(entry.dataset.search + ' ' + body)),
      body, passages, topics: JSON.parse(entry.dataset.topics || '[]')};
  });
  function showHits(matches, terms) {
    hits.replaceChildren();
    ranked.hidden = terms.length === 0 || matches.length === 0;
    if (ranked.hidden) return;
    for (const record of matches.slice(0, 20)) {
      const item = document.createElement('li');
      const link = document.createElement('a');
      const passage = record.passages[record.matchIndex];
      const anchor = passage?.closest('.anchored-passage')?.id || record.entry.id;
      link.href = '#' + anchor;
      link.textContent = record.title;
      const scope = document.createElement('span');
      scope.className = 'muted';
      scope.textContent = ' · ' + record.entry.dataset.kind + ' · ' + (record.entry.dataset.status || 'no research status');
      item.append(link, scope);
      if (passage) {
        const excerpt = document.createElement('p');
        const text = passage.textContent.replace(/\s+/g, ' ').trim();
        const offset = Math.max(0, text.toLowerCase().indexOf(terms[0]) - 70);
        excerpt.textContent = (offset ? '…' : '') + text.slice(offset, offset + 240) + (text.length > offset + 240 ? '…' : '');
        item.append(excerpt);
      }
      hits.append(item);
    }
  }
  function filter() {
    const terms = words(search.value);
    const phrase = search.value.trim().toLowerCase();
    const ident = phrase.replace(/^<|\/?>$|^@/g, '');
    const matches = [];
    for (const record of records) {
      const entry = record.entry;
      const matched = (!layer.value || entry.dataset.kind === layer.value)
        && (!status.value || (status.value === 'unassigned' ? !entry.dataset.status : entry.dataset.status === status.value))
        && (!topic?.value || record.topics.includes(topic.value))
        && (!moduleFilter?.value || entry.dataset.module === moduleFilter.value)
        && (!sourceKind?.value || entry.dataset.sourceKind === sourceKind.value)
        && terms.every(term => record.words.has(term));
      entry.hidden = !matched;
      if (matched) {
        record.matchIndex = terms.length ? record.passageWords.findIndex(tokens => terms.every(term => tokens.has(term))) : -1;
        record.score = (entry.dataset.ident.toLowerCase() === ident && ident ? 10000 : 0)
          + (record.title.toLowerCase().includes(phrase) && phrase ? 1000 : 0)
          + terms.filter(term => record.titleWords.has(term)).length * 100
          + (record.body.includes(phrase) && phrase ? 30 : 0)
          + (entry.dataset.kind === 'assertion' ? 10 : 0)
          + (record.matchIndex >= 0 ? 200 : 0);
        matches.push(record);
      }
    }
    matches.sort((a, b) => b.score - a.score || a.order - b.order);
    for (const group of document.querySelectorAll('.knowledge-group')) group.hidden = !Array.from(group.querySelectorAll('.artifact')).some(entry => !entry.hidden);
    document.getElementById('knowledge-results').textContent = matches.length + ' of ' + entries.length + ' artifacts';
    document.getElementById('knowledge-empty').hidden = matches.length !== 0;
    showHits(matches, terms);
  }
  function reveal() {
    let id;
    try { id = decodeURIComponent(location.hash.slice(1)); } catch { return; }
    const target = document.getElementById(id);
    if (!target) return;
    const entry = target.closest('.artifact');
    if (entry) {
      search.value = ''; layer.value = ''; status.value = '';
      for (const control of [topic, moduleFilter, sourceKind]) if (control) control.value = '';
      filter();
      entry.open = true;
      for (let parent = target.parentElement; parent; parent = parent.parentElement) {
        if (parent.tagName === 'DETAILS') parent.open = true;
      }
      requestAnimationFrame(() => {
        target.scrollIntoView({block: 'start'});
        (target === entry ? entry.querySelector('summary') : target).focus({preventScroll: true});
      });
    }
  }
  let pending;
  form.addEventListener('submit', event => event.preventDefault());
  form.addEventListener('input', () => {
    clearTimeout(pending);
    pending = setTimeout(filter, 120);
  });
  form.addEventListener('reset', () => requestAnimationFrame(filter));
  window.addEventListener('hashchange', reveal);
  filter(); reveal();
})();
