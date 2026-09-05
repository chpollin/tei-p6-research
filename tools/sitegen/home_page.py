"""Render the proposal home from a validated view model, with no input reads."""
from __future__ import annotations

import html
import json
import posixpath
import re
from pathlib import PurePosixPath
from urllib.parse import urlsplit

from sitegen.assets import read_asset
from sitegen.chrome import render_footer, render_header
from sitegen.home_view import repository_link, wiki_path


def esc(value: object) -> str:
    return html.escape(str(value), quote=True)


def slug(text: str) -> str:
    return re.sub(r"[^\w-]+", "-", text.lower()).strip("-")


def safe_url(value: str) -> str:
    parsed = urlsplit(value)
    if parsed.scheme and parsed.scheme not in ("https", "http", "mailto"):
        raise ValueError(f"Unsafe link scheme: {parsed.scheme}")
    if value.startswith("//") or any(ord(c) < 32 for c in value):
        raise ValueError("Unsafe link")
    return value


class Markdown:
    """Escaping-first rendering of the repository's documented Markdown subset."""

    token = re.compile(r"(`[^`]+`|\[\^[\w.-]+\]|\[\[[^\]]+\]\]|\[[^\]]+\]\([^)]+\)|\*\*.+?\*\*|(?<!\w)\*[^*\n]+\*)")

    def __init__(self, view: dict):
        self.view = view
        self.notes = {n["id"]: n for n in view["notes"]}
        self.references: dict[str, list[str]] = {}
        self.headings: list[tuple[str, str]] = []
        self.ids: dict[str, int] = {}

    def inline(self, text: str, source: str) -> str:
        result = []
        offset = 0
        for match in self.token.finditer(text):
            result.append(esc(text[offset:match.start()]))
            token = match.group()
            if token.startswith("`"):
                result.append(f"<code>{esc(token[1:-1])}</code>")
            elif token.startswith("[^"):
                key = token[2:-1]
                note = self.notes[key]
                refs = self.references.setdefault(key, [])
                ref = f"ref-{key}-{len(refs) + 1}"
                refs.append(ref)
                label = "Source-grounded premise" if note["kind"] == "grounded" else "Project posit"
                result.append(f'<sup class="note-ref {note["kind"]}"><a id="{ref}" href="#note-{key}" aria-label="{label} {note["label"]}">{note["label"]}</a></sup>')
            elif token.startswith("[["):
                target, _, alias = token[2:-2].partition("|")
                href = repository_link(wiki_path(target), self.view["base"])
                label = alias or target.split("/")[-1].split("#")[0].replace("-", " ")
                result.append(f'<a href="{esc(href)}">{esc(label)}</a>')
            elif token.startswith("["):
                label, target = token[1:-1].split("](", 1)
                if target.startswith("#example="):
                    if target[9:] not in {case["id"] for case in self.view["comparisons"]["cases"]}:
                        raise ValueError(f"Unknown example link: {target}")
                    href = target
                elif target.startswith("#"):
                    href = "#proposal-" + slug(target[1:])
                elif urlsplit(target).scheme or target.startswith("//"):
                    href = safe_url(target)
                else:
                    path = posixpath.normpath(str(PurePosixPath(source).parent / target))
                    if path.startswith("../"):
                        raise ValueError("Link escapes repository")
                    href = repository_link(path, self.view["base"])
                result.append(f'<a href="{esc(href)}">{esc(label)}</a>')
            elif token.startswith("**"):
                result.append(f"<strong>{self.inline(token[2:-2], source)}</strong>")
            else:
                result.append(f"<em>{self.inline(token[1:-1], source)}</em>")
            offset = match.end()
        result.append(esc(text[offset:]))
        return "".join(result)

    def blocks(self, text: str, source: str, headings: bool = False) -> str:
        lines = text.splitlines()
        output = []
        i = 0
        while i < len(lines):
            line = lines[i]
            if not line.strip():
                i += 1
                continue
            if line.startswith("```"):
                i += 1
                code = []
                while i < len(lines) and not lines[i].startswith("```"):
                    code.append(lines[i])
                    i += 1
                if i == len(lines):
                    raise ValueError("Unclosed Markdown code fence")
                output.append("<pre><code>" + esc("\n".join(code)) + "</code></pre>")
                i += 1
                continue
            heading = re.match(r"^(#{1,6})\s+(.*)", line)
            if heading:
                level = len(heading.group(1))
                label = heading.group(2)
                base = "proposal-" + slug(label)
                self.ids[base] = self.ids.get(base, 0) + 1
                anchor = base if self.ids[base] == 1 else f"{base}-{self.ids[base]}"
                if headings and len(heading.group(1)) == 2:
                    self.headings.append((anchor, label))
                output.append(f'<h{level} id="{anchor}">{self.inline(label, source)}</h{level}>')
                i += 1
                continue
            if line.startswith("|") and i + 1 < len(lines) and re.match(r"^\s*\|[\s:|-]+\|\s*$", lines[i + 1]):
                cells = lambda row: [c.strip() for c in row.strip().strip("|").split("|")]
                header = "".join(f'<th scope="col">{self.inline(c, source)}</th>' for c in cells(line))
                i += 2
                rows = []
                while i < len(lines) and lines[i].startswith("|"):
                    rows.append("<tr>" + "".join(f"<td>{self.inline(c, source)}</td>" for c in cells(lines[i])) + "</tr>")
                    i += 1
                output.append(f'<div class="table-scroll" tabindex="0" role="region" aria-label="Proposal comparison table"><table><thead><tr>{header}</tr></thead><tbody>{"".join(rows)}</tbody></table></div>')
                continue
            if line.startswith(">"):
                quote_lines = []
                while i < len(lines) and lines[i].startswith(">"):
                    quote_lines.append(lines[i][1:].lstrip())
                    i += 1
                output.append("<blockquote>" + self.blocks("\n".join(quote_lines), source) + "</blockquote>")
                continue
            item = re.match(r"^(\s*)([-*]|\d+[.)])\s+(.*)", line)
            if item:
                indent = len(item.group(1))
                ordered = item.group(2)[0].isdigit()
                items = []
                while i < len(lines):
                    next_item = re.match(r"^(\s*)([-*]|\d+[.)])\s+(.*)", lines[i])
                    if not next_item or len(next_item.group(1)) != indent:
                        break
                    content = [next_item.group(3)]
                    i += 1
                    while i < len(lines):
                        continuation = lines[i]
                        if continuation.strip() and len(continuation) - len(continuation.lstrip()) > indent:
                            content.append(continuation[indent + 2:])
                            i += 1
                        elif not continuation.strip() and i + 1 < len(lines) and (lines[i + 1].startswith(" " * (indent + 2)) or re.match(r"^([-*]|\d+[.)])\s", lines[i + 1])):
                            content.append("")
                            i += 1
                        else:
                            break
                    items.append("<li>" + self.blocks("\n".join(content), source) + "</li>")
                tag = "ol" if ordered else "ul"
                output.append(f"<{tag}>{''.join(items)}</{tag}>")
                continue
            paragraph = [line]
            i += 1
            while i < len(lines) and lines[i].strip() and not re.match(r"^(#{1,6}\s|```|>|\||\s*[-*]\s|\s*\d+[.)]\s)", lines[i]):
                paragraph.append(lines[i])
                i += 1
            output.append("<p>" + self.inline(" ".join(p.strip() for p in paragraph), source) + "</p>")
        return "\n".join(output)


def render_notes(view: dict, md: Markdown) -> str:
    output = []
    for note in view["notes"]:
        key = note["id"]
        if note["kind"] == "posit":
            content = '<p class="note-type">Project posit · rationale</p>' + md.blocks(note["rationale"], view["paths"]["proposal"])
            content += '<p class="question-label">Open evidence question</p>' + md.blocks(note["question"], view["paths"]["proposal"])
        else:
            content = '<p class="note-type">Source-grounded premise</p>' + md.blocks(note["text"], view["paths"]["proposal"])
            for assertion in note["assertions"]:
                links = []
                knowledge_id = "doc-" + re.sub(r"[^a-z0-9]+", "-", assertion["path"].split("#")[0].removesuffix(".md").lower()).strip("-")
                links.append(f'<li><a href="knowledge.html#{knowledge_id}">Inspect provenance</a></li>')
                for link in assertion["links"]:
                    href = safe_url(link["url"]) if "url" in link else repository_link(link["path"], view["base"])
                    links.append(f'<li><a href="{esc(href)}">{esc(link["label"])}</a></li>')
                content += '<details><summary>Read the assertion and follow its source</summary><div class="evidence-content">'
                content += md.blocks(assertion["statement"], assertion["path"])
                content += '<ol class="source-chain" aria-label="Provenance chain">' + "".join(links) + "</ol>"
                content += '<p class="evidence-boundary">Grounding records traceability. It does not establish truth or human verification.</p></div></details>'
        back = " ".join(f'<a href="#{ref}" aria-label="Return to reference {note["label"]}, occurrence {i + 1}">Back to text{(" " + str(i + 1)) if i else ""} ↑</a>' for i, ref in enumerate(md.references.get(key, [])))
        output.append(f'<li id="note-{key}" class="evidence-note {note["kind"]}"><span class="note-number">{note["label"]}</span><div>{content}<p class="backlinks">{back}</p></div></li>')
    return '<ol class="evidence-notes">' + "".join(output) + "</ol>"


def link_list(links: list[dict]) -> str:
    return '<ul class="source-links">' + "".join(
        f'<li><a href="{esc(safe_url(link["url"]))}">{esc(link["label"])}</a></li>'
        for link in links
    ) + "</ul>"


def paragraphs(items: object) -> str:
    if isinstance(items, str):
        items = [items]
    return "".join(f"<p>{esc(item)}</p>" for item in (items or []))


def code_view(value: str, language: str, objects: list[str]) -> str:
    """Keep source code inert while marking whole object IDs for inspection."""
    tokens = sorted(set(objects), key=len, reverse=True)
    pattern = re.compile(r"(?<![\w-])(" + "|".join(re.escape(t) for t in tokens) + r")(?![\w-])") if tokens else None
    parts = []
    start = 0
    for match in pattern.finditer(value) if pattern else []:
        parts.append(esc(value[start:match.start()]))
        parts.append(f'<span data-object="{esc(match.group())}">{esc(match.group())}</span>')
        start = match.end()
    parts.append(esc(value[start:]))
    return f'<pre tabindex="0" aria-label="{esc(language)} representation"><code>{"".join(parts)}</code></pre>'


def graph_view(graph: dict, namespace: str, title: str, interactive: bool = True) -> str:
    nodes = graph.get("nodes", [])
    edges = graph.get("edges", [])
    if not nodes:
        return "<p>No instance graph is available for this case.</p>"
    positions = {node["id"]: (25 + (i % 2) * 270, 30 + (i // 2) * 100) for i, node in enumerate(nodes)}
    height = 55 + ((len(nodes) + 1) // 2) * 100
    lines = []
    rows = []
    for edge in edges:
        if edge["source"] not in positions or edge["target"] not in positions:
            raise ValueError("Diagram edge has a missing endpoint")
        x1, y1 = positions[edge["source"]]
        x2, y2 = positions[edge["target"]]
        if y1 == y2:
            start, end = ((x1 + 220, y1 + 30), (x2, y2 + 30)) if x1 < x2 else ((x1, y1 + 30), (x2 + 220, y2 + 30))
        else:
            start, end = ((x1 + 110, y1 + 60), (x2 + 110, y2)) if y1 < y2 else ((x1 + 110, y1), (x2 + 110, y2 + 60))
        lines.append(f'<path data-edge-source="{esc(edge["source"])}" data-edge-target="{esc(edge["target"])}" d="M{start[0]},{start[1]} L{end[0]},{end[1]}" marker-end="url(#{namespace}-arrow)"><title>{esc(edge["source"])} — {esc(edge["label"])} → {esc(edge["target"])}</title></path>')
        rows.append(f'<tr><td><code>{esc(edge["source"])}</code></td><td>{esc(edge["label"])}</td><td><code>{esc(edge["target"])}</code></td></tr>')
    boxes = []
    for node in nodes:
        x, y = positions[node["id"]]
        control = f' role="button" tabindex="0" aria-pressed="false" aria-label="Inspect {esc(node["id"])}: {esc(node["label"])}" data-object-node="{esc(node["id"])}"' if interactive else ""
        boxes.append(f'<g{control}><rect x="{x}" y="{y}" width="220" height="60" rx="2"/><text x="{x + 12}" y="{y + 23}">{esc(node["id"])}</text><text class="graph-kind" x="{x + 12}" y="{y + 44}">{esc(str(node.get("kind", ""))[:30])}</text></g>')
    interaction = " Select an object to mark its ID in the candidate representations." if interactive else " Relationship cardinalities are stated in the table."
    return f'<figure class="formal-graph"><svg viewBox="0 0 540 {height}" role="group" aria-label="{esc(title)}"><defs><marker id="{namespace}-arrow" markerWidth="8" markerHeight="8" refX="7" refY="3" orient="auto"><path d="M0,0 L0,6 L8,3 z"/></marker></defs><g class="graph-edges">{"".join(lines)}</g>{"".join(boxes)}</svg><figcaption>{esc(title)}.{interaction}</figcaption></figure><details><summary>Relationships as a table</summary><div class="table-scroll"><table><thead><tr><th>Source</th><th>Relationship</th><th>Target</th></tr></thead><tbody>{"".join(rows)}</tbody></table></div></details>'


def render_case(case: dict) -> str:
    key = case["id"]
    if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", key):
        raise ValueError(f"Unsafe example ID: {key}")
    prefix = "case-" + key
    candidate = case["candidate"]
    objects = [node["id"] for node in case.get("graph", {}).get("nodes", [])]
    variant_options = "".join(f'<option value="{esc(v["id"])}">{esc(v["title"])}</option>' for v in case["p5"])
    variants = []
    for variant in case["p5"]:
        variants.append(f'<section data-p5-variant="{esc(variant["id"])}"><h4>{esc(variant["title"])}</h4>{code_view(variant["xml"], "TEI P5 XML", [])}<details><summary>Encoding notes and sources</summary><p class="record-status">{esc(variant["status"])}</p>{paragraphs(variant.get("notes"))}{link_list(variant.get("sources", []))}</details></section>')
    available = candidate.get("serializations", {})
    serializations = {name: available[name] for name in ("xml", "json", "yaml") if name in available}
    serializations.update({name: value for name, value in available.items() if name not in serializations})
    binding_options = "".join(f'<option value="{esc(name)}">{esc(name.upper())}</option>' for name in serializations)
    bindings = "".join(f'<section data-binding="{esc(name)}"><h4>{esc(name.upper())}</h4>{code_view(value, name.upper(), objects)}</section>' for name, value in serializations.items())
    validation = candidate.get("validation", {})
    if not available:
        validation_label = "No candidate mapping"
    elif validation.get("valid") is True:
        validation_label = "Pass — candidate model validation"
    elif validation.get("valid") is False:
        validation_label = "Fail — candidate model validation"
    else:
        validation_label = "No candidate model validation result"
    tabs = [("comparison", "Comparison"), ("formal", "Model"), ("validation", "Checks")]
    tab_buttons = "".join(f'<button type="button" role="tab" id="{prefix}-tab-{name}" aria-controls="{prefix}-{name}" aria-selected="{"true" if i == 0 else "false"}" tabindex="{0 if i == 0 else -1}" data-case-tab="{name}">{label}</button>' for i, (name, label) in enumerate(tabs))
    attribution = ""
    if case["source_kind"].startswith("Real edition"):
        attribution = '<div class="source-attribution"><h4>Source and rights</h4>' + "".join(paragraphs(variant.get("notes")) + link_list(variant.get("sources", [])) for variant in case["p5"]) + "</div>"
    type_graph = {
        "nodes": [{"id": "Version", "kind": "immutable content", "label": "Version"}, {"id": "Selection", "kind": "located in one version", "label": "Selection"}, {"id": "Reading", "kind": "attributed structure", "label": "Reading"}, {"id": "Node", "kind": "structural occurrence", "label": "Node"}, {"id": "Agent", "kind": "responsible actor", "label": "Agent"}],
        "edges": [{"source": "Selection", "target": "Version", "label": "addresses exactly one"}, {"source": "Reading", "target": "Version", "label": "describes exactly one"}, {"source": "Reading", "target": "Agent", "label": "attributed to exactly one"}, {"source": "Reading", "target": "Node", "label": "contains one or more"}, {"source": "Node", "target": "Selection", "label": "addresses exactly one"}],
    }
    instance = graph_view(case.get("graph", {}), prefix + "-instance", "Objects in this example")
    selection_feedback = '<p class="selection-feedback" aria-live="polite">Select an object to mark its identifier in the encodings.</p>' if objects else ""
    licence = ""
    if case["source_kind"].startswith("Real edition"):
        licence = '<p class="case-license">' + esc(case["source_kind"]) + ' · <a href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA 4.0</a></p>'
    candidate_content = bindings or '<p class="mapping-unavailable">' + esc(candidate["status"]) + "</p>"
    return f'''<section class="comparison-case" id="example={key}" data-case="{key}" aria-labelledby="{prefix}-title">
<header class="case-heading"><h2 id="{prefix}-title">{esc(case["title"])}</h2></header>
<p class="case-task">{esc(case["description"] if isinstance(case["description"], str) else " ".join(case["description"]))}</p>
<div class="case-tabs" role="tablist" aria-label="Example views">{tab_buttons}</div>
<section id="{prefix}-comparison" role="tabpanel" aria-labelledby="{prefix}-tab-comparison" data-case-panel="comparison"><div class="encoding-grid"><section><h3>TEI P5</h3><label class="variant-control" for="{prefix}-p5"><span class="sr-only">Encoding variant</span><select id="{prefix}-p5" data-p5-select>{variant_options}</select></label>{"".join(variants) or "<p>No documented P5 variant in this case.</p>"}</section><section><h3>Candidate model 0.1</h3><label class="variant-control" for="{prefix}-binding"><span class="sr-only">Serialization</span><select id="{prefix}-binding" data-binding-select>{binding_options}</select></label>{candidate_content}<details><summary>Binding and mapping notes</summary><p class="record-status">{esc(candidate["status"])}</p>{paragraphs(candidate.get("notes"))}</details></section></div></section>
<section id="{prefix}-formal" role="tabpanel" aria-labelledby="{prefix}-tab-formal" data-case-panel="formal"><ol class="formal-rules">{"".join(f"<li>{esc(rule)}</li>" for rule in case.get("formal", []))}</ol><details><summary>Core type relationships</summary>{graph_view(type_graph, prefix + "-types", "Selected type relationships", interactive=False)}</details><h3>Instance relationships</h3>{instance}{selection_feedback}</section>
<section id="{prefix}-validation" role="tabpanel" aria-labelledby="{prefix}-tab-validation" data-case-panel="validation"><p class="validation-result">{esc(validation_label)}</p>{paragraphs(validation.get("summary"))}{code_view(json.dumps(validation, ensure_ascii=False, indent=2, sort_keys=True), "Validation result", [])}</section>
<details class="case-context"><summary>Context, sources and limits</summary><p>{esc(case["source_kind"])} · {esc(case["phenomenon"])}</p><div class="primary-text"><span>Text under examination</span><p>{esc(case.get("primary_text", ""))}</p></div>{paragraphs(case.get("limits"))}{link_list(case.get("links", []))}{attribution}<p><a class="case-permalink" href="#example={key}">Link to this example</a></p></details>{licence}</section>'''


def render_page(view: dict) -> str:
    md = Markdown(view)
    article = md.blocks(view["body"], view["paths"]["proposal"], headings=True)
    toc = "".join(f'<li><a href="#{anchor}">{esc(label)}</a></li>' for anchor, label in md.headings)
    notes = render_notes(view, md)
    repo = lambda key: esc(repository_link(view["paths"][key], view["base"]))
    comparisons = view["comparisons"]
    case_links = "".join(f'<li><a href="#example={esc(case["id"])}" data-open-case="{esc(case["id"])}">{esc(case["title"])} <span aria-hidden="true">↗</span></a></li>' for case in comparisons["cases"])
    case_options = "".join(f'<option value="{esc(case["id"])}">{esc(case["title"])}</option>' for case in comparisons["cases"])
    cases = "".join(render_case(case) for case in comparisons["cases"])
    definitions = "".join(f'<dt>{esc(name)}</dt><dd>{md.inline(definition, view["paths"]["model"])}</dd>' for name, definition in view["definitions"].items() if name in ("Version", "Selection", "Reading", "Node", "Annotation", "Relation", "Agent"))
    coverage_rows = []
    for row in comparisons["coverage"]:
        values = [row["module"], row["title"], row["status"], " · ".join(row.get("phenomena", [])), " · ".join(row.get("document_types", []))]
        coverage_rows.append(f'<tr data-coverage-row data-search="{esc(" ".join(values).lower())}"><th scope="row"><code>{esc(values[0])}</code><span>{esc(values[1])}</span></th><td>{esc(values[2])}</td><td>{esc(values[3])}</td><td>{esc(values[4])}</td></tr>')
    bindings = "".join(f'<li><strong>{esc(binding["label"])}</strong> · {esc(binding["status"])}</li>' for binding in comparisons["bindings"])
    return f'''<!doctype html>
<html lang="en">
<head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="Abstract Text Model 0.1: technical proposal, TEI P5 comparisons, formal constraints and model serializations.">
<meta name="color-scheme" content="light"><title>Abstract Text Model 0.1 · TEI P6 Research</title>
<style>
{read_asset("workbench.css")}
{read_asset("home.css")}</style></head>
<body>
<a class="skip-link" href="#main">Skip to proposal</a>
{render_header("home")}
<main id="main" class="document-layout">
<aside class="proposal-toc"><nav aria-label="Proposal contents"><p class="toc-label">Contents</p><ol>{toc}<li><a href="#evidence">Sources and open questions</a></li><li><a href="#model-reference">Model reference</a></li><li><a href="#coverage">P5 module coverage</a></li></ol></nav><nav class="case-index" aria-label="Comparison examples"><p class="toc-label">Examples</p><ul>{case_links}</ul></nav><p class="document-meta">Research draft · Model 0.1<br><a href="{repo("proposal")}">Canonical Markdown</a></p></aside>
<div class="reading-column">
<details class="mobile-contents"><summary>Proposal contents</summary><nav aria-label="Mobile proposal contents"><ol>{toc}<li><a href="#evidence">Sources and open questions</a></li><li><a href="#model-reference">Model reference</a></li><li><a href="#examples">Examples</a></li><li><a href="#coverage">P5 module coverage</a></li></ol></nav></details>
<section id="proposal" aria-label="Proposal"><article class="proposal-text" aria-label="Complete canonical proposal">{article}</article></section>
<section class="evidence-section" id="evidence" aria-labelledby="evidence-title"><h2 id="evidence-title">Sources and open questions</h2><p><span class="legend grounded">G</span> Source-grounded premise. <span class="legend posit">P</span> Project posit. Grounding records traceability, not human verification.</p>{notes}</section>
<section id="model-reference" class="reference-section"><h2>Model reference</h2><dl class="definition-list">{definitions}</dl><p><a href="{repo("model")}">Complete definitions, identities and invariants</a></p><h3>Serialization bindings</h3><ul>{bindings}</ul></section>
<section id="examples" class="reference-section"><h2>Examples</h2><p>Open a case beside the proposal to compare its encodings, formal requirements and validation result.</p><ul class="example-list">{case_links}</ul><noscript><p>JavaScript is disabled. Complete comparison cases remain readable below the module index.</p></noscript></section>
<section id="coverage" class="reference-section"><h2>P5 modules and research coverage</h2><p>Modules organize the P5 specification. Document types, media and textual phenomena are separate dimensions. This index defines the research scope. Model support must be evaluated for each domain.</p><label class="coverage-filter" for="coverage-search">Filter modules, phenomena or document types<input type="search" id="coverage-search" placeholder="Letters, correction, manuscript"></label><p id="coverage-count" aria-live="polite">{len(coverage_rows)} modules</p><div class="table-scroll" tabindex="0" role="region" aria-label="P5 module coverage"><table class="coverage-table"><thead><tr><th scope="col">P5 module</th><th scope="col">Research status</th><th scope="col">Phenomena</th><th scope="col">Document types</th></tr></thead><tbody>{"".join(coverage_rows)}</tbody></table></div><p id="coverage-empty" hidden>No modules match this filter.</p></section>
</div></main>
<aside id="comparison-workspace" class="comparison-workspace" aria-label="Example comparison workspace" tabindex="-1"><div class="workspace-toolbar"><label for="case-select"><span class="sr-only">Example beside the proposal</span><select id="case-select">{case_options}</select></label><button type="button" id="close-comparison" aria-label="Close example and return to proposal">Close <span aria-hidden="true">×</span></button></div>{cases}</aside>
<aside class="home-source-license" aria-label="Editorial excerpt rights">Editorial excerpts: {esc(view["attribution"])} <a href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA 4.0</a>.</aside>
{render_footer(view["date"])}
<script>
{read_asset("home.js")}</script></body></html>
'''
