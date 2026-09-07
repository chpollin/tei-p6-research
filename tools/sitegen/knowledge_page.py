"""Escaping-first static view of vault artifacts and precise provenance."""
from __future__ import annotations

import re

from tools.sitegen.assets import read_asset
from tools.sitegen.chrome import render_footer, render_header
from tools.sitegen.knowledge_view import LAYERS, block_id
from tools.sitegen.markup import esc, repository_link, safe_url


def link(url: str, label: str) -> str:
    return f'<a href="{esc(url)}">{esc(label)}</a>'


def literal(text: str) -> str:
    """Preserve source whitespace in the DOM without trailing HTML-file spaces."""
    return re.sub(r"[ \t]+(?=\r?$)",
                  lambda match: ''.join('&#32;' if char == ' ' else '&#9;' for char in match[0]),
                  esc(text).replace('\t', '&#9;'), flags=re.M)


def _edges(edges: list[dict], label: str) -> str:
    if not edges:
        return ""
    return '<div class="chain-links"><h4>' + esc(label) + '</h4><ul>' + ''.join(
        '<li>' + link(e['href'], e['title'] + (' · ^' + e['anchor'] if e.get('anchor') else '')) +
        (' <span class="muted">cites ^' + esc(e['target_anchor']) + '</span>' if e.get('target_anchor') else '') + '</li>'
        for e in edges) + '</ul></div>'


def _metadata(entry: dict, base: str | None) -> str:
    source = entry['source']
    values = []
    for key, label in (('creator', 'Attribution'), ('date', 'Source date'), ('version', 'Pinned version / commit'),
                       ('license', 'Source license'), ('authority', 'Recorded authority'), ('observed', 'Acquisition record date'),
                       ('rights', 'Rights / attribution record'), ('sha256', 'Original SHA-256')):
        if source.get(key):
            values.append((label, esc(source[key])))
    if source and not source.get('authority'):
        values.append(('Recorded authority', 'Not recorded in the matched admission; no authority inferred.'))
    if source.get('identifier'):
        values.append(('Original source', link(safe_url(source['identifier']), 'Open the identified source')))
    if source.get('local_original'):
        values.append(('Local original', '<code>' + esc(source['local_original']) + '</code> · local-only; not served here'))
    if source.get('citation'):
        citation = source['citation']
        values.append(('Cited source', link(safe_url(citation['URL']), citation.get('title', citation['id']))))
        if citation.get('DOI'):
            values.append(('DOI', esc(citation['DOI'])))
        if citation.get('issued', {}).get('date-parts'):
            values.append(('Publication date', esc('-'.join(str(n) for n in citation['issued']['date-parts'][0]))))
        if citation.get('note'):
            values.append(('Bibliographic note', esc(citation['note'])))
        values.append(('Admission form', 'Citation and checked quotation. No Markdown representation or local original is held.'))
    if source.get('manifest'):
        values.append(('Admission manifest', link(repository_link(source['manifest'], base), source['manifest'])))
    for check, date in entry['checked'].items():
        values.append(('Recorded check: ' + check, esc(date)))
    if not values:
        return ''
    return '<dl class="artifact-metadata">' + ''.join('<div><dt>' + esc(label) + '</dt><dd>' + value + '</dd></div>' for label, value in values) + '</dl>'


def render_entry(entry: dict, base: str | None) -> str:
    kind, path = entry['kind'], entry['path']
    status = entry['status'] or 'No research status assigned'
    search = ' '.join((entry['title'], path, status, str(entry['metadata'].get('topics', [])), entry['excerpt'], ' '.join(entry['blocks'].values())))
    if kind == 'representation':
        excerpt = '<p class="muted">Anchored passages appear below. The repository holds the complete representation. Local originals are not published here.</p>'
    else:
        excerpt = '<pre class="passage">' + esc(entry['excerpt']) + '</pre>' if entry['excerpt'] else ''
    blocks = []
    for anchor, text in entry['blocks'].items():
        edges = [edge for edge in entry['edges'] if edge['from_anchor'] == anchor]
        blocks.append(f'<section id="{esc(block_id(path, anchor))}" class="anchored-passage" tabindex="-1"><h4>{link("#" + block_id(path, anchor), "^" + anchor)}</h4><pre class="passage">{literal(text)}</pre>{_edges(edges, "Grounding passage")}</section>')
    direct = [edge for edge in entry['edges'] if not edge['from_anchor']]
    canonical = link(repository_link(path, base), 'Canonical Markdown')
    if path == '40_output/12-p6-design.md':
        canonical += ' · ' + link('index.html#proposal', 'Read the complete proposal')
    posit = ''
    if kind == 'chapter':
        posit = '<p class="muted">The chapter records ' + esc(entry['metadata'].get('posits', 'an unspecified number of')) + ' explicit project posits. These express authorial proposals.</p>'
    return f'''<details class="artifact" id="{esc(entry['id'])}" data-kind="{esc(kind)}" data-search="{literal(search)}">
<summary><span class="artifact-title">{esc(entry['title'])}</span><span class="artifact-state">{esc(status)}</span></summary>
<div class="artifact-content"><p class="artifact-path"><code>{esc(path)}</code> · {canonical}</p>{excerpt}{posit}{_edges(direct, 'Grounding')}{''.join(blocks)}{_metadata(entry, base)}{_edges(entry['backlinks'], 'Used by')}</div></details>'''


def render_page(view: dict) -> str:
    groups = []
    for kind, label in LAYERS.items():
        entries = [entry for entry in view['entries'] if entry['kind'] == kind]
        groups.append(f'<section class="knowledge-group" data-group="{kind}" aria-labelledby="group-{kind}"><h2 id="group-{kind}">{esc(label)} <span class="count">{len(entries)}</span></h2>' + ''.join(render_entry(e, view['base']) for e in entries) + '</section>')
    nav = []
    for kind in dict.fromkeys(item['kind'] for item in view['navigation']):
        nav.append('<section><h3>' + esc(kind) + '</h3><ul>' + ''.join('<li>' + link(repository_link(item['path'], view['base']), item['title']) + '</li>' for item in view['navigation'] if item['kind'] == kind) + '</ul></section>')
    options = ''.join(f'<option value="{kind}">{esc(label)}</option>' for kind, label in LAYERS.items())
    css = read_asset('workbench.css') + '\n' + read_asset('knowledge.css')
    js = read_asset('knowledge.js')
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="description" content="Source representations, distillates, assertions and output chapters in this repository, with their exact provenance links."><title>Knowledge and provenance · TEI P6 Research</title><style>{css}</style></head>
<body><a class="skip-link" href="#main">Skip to content</a>{render_header('knowledge')}
<main id="main" class="knowledge-main"><header class="page-heading"><h1>Knowledge and provenance</h1>
<p>Actual source representations, distillates, assertions, and output chapters in this repository. Follow a claim to its exact source passage, or inspect where a passage is used.</p>
<p class="muted">Browse admitted sources, distillates, assertions and output. <a href="corpus.html">Materials</a> records the broader acquired and planned holdings. Citation-only admissions end at a checked quotation and citation. Grounded means traceable. Validated records machine checks. Verified requires recorded human verification.</p></header>
<nav class="layer-navigation" aria-label="Vault layers">{''.join(link('#group-' + kind, label + ' (' + str(view['counts'][kind]) + ')') for kind, label in LAYERS.items())}{link('#documents', 'Project documents')}</nav>
<form class="knowledge-filters" role="search"><label>Search the vault<input id="knowledge-search" type="search" placeholder="Title, statement, topic, or path" autocomplete="off"></label><label>Layer<select id="knowledge-layer"><option value="">All layers</option>{options}</select></label><button type="reset">Clear filters</button><output id="knowledge-results" aria-live="polite">{len(view['entries'])} artifacts</output></form>
<p id="knowledge-empty" hidden>No artifacts match these filters.</p>{''.join(groups)}
<section id="documents" class="document-navigation"><h2>Project documents</h2><p class="muted">Control contracts, topic maps, and provisional design documents are navigation and project reasoning. They are not substitutes for the evidence chain.</p><div class="document-columns">{''.join(nav)}</div></section>
</main>{render_footer(view['date'])}<script>{js}</script></body></html>'''
