"""Read canonical model contracts and render an inspectable class reference.

The diagram is a navigation projection, not an additional ontology. Fields,
rules, operation contracts, and the complete definition are read on every build.
"""
from __future__ import annotations

import json
import re
from pathlib import Path
from urllib.parse import urlsplit

from tools.sitegen.assets import read_asset
from tools.sitegen.chrome import render_footer, render_header
from tools.sitegen.documents import first_table_rows, read_document
from tools.sitegen.home_page import Markdown
from tools.sitegen.markup import esc, repository_link

DEFINITION = "knowledge/text-model.md"
SPEC = "experiments/abstract_text_v01/spec.json"
PROFILE = "experiments/editorial_cases/profile.json"

# Keys bind presentation names to the existing record contracts. The third
# column identifies the exact object-table row in the canonical definition.
KINDS = (
    ("Agent", "agents", "Agent"),
    ("Concept", "concepts", "Concept"),
    ("Text", "texts", "Text"),
    ("Version", "versions", "Version"),
    ("Continuity", "continuities", "Continuity claim"),
    ("Selection", "selections", "Selection"),
    ("Reading", "readings", "Reading"),
    ("ReadingNode", "node", "Reading node"),
    ("Annotation", "annotations", "Annotation"),
    ("Relation", "relations", "Relation"),
)

# Cardinalities are measured from one source record. Inverse requirements and
# graph constraints are explicitly stated below; an arrow alone cannot express
# them. The existence of these fields is checked against the input contract.
REFERENCES = (
    ("Version", "parents", "Version", "0..n", "Acyclic; declared technical construction inputs, frozen under a reused version ID."),
    ("Continuity", "text", "Text", "1", "Every Text has at least one incoming continuity claim."),
    ("Continuity", "versions", "Version", "1..n", "Positive membership; a Version may belong to several claims or none."),
    ("Continuity", "agent", "Agent", "1", "The claim is attributed to one responsible record."),
    ("Selection", "version", "Version", "1", "The selector is interpreted against this exact version."),
    ("Reading", "version", "Version", "1", "All node extents refer to this version."),
    ("Reading", "agent", "Agent", "1", "Responsibility belongs to the reading."),
    ("Reading", "nodes", "ReadingNode", "1..n", "Each node is contained in exactly one reading; IDs remain package-wide unique."),
    ("ReadingNode", "type", "Concept", "1", "The referenced concept has applies_to=node."),
    ("ReadingNode", "selection", "Selection", "1", "Exactly one resolved, nonempty contiguous region in the containing reading's version."),
    ("ReadingNode", "parent", "ReadingNode", "0..1", "Same reading; acyclic forest, containment, nonoverlapping siblings including roots."),
    ("Annotation", "agent", "Agent", "1", "The body is attributed; its interpretation is not evaluated."),
    ("Annotation", "selection", "Selection", "1", "An absent or ambiguous quotation selection may remain unresolved."),
    ("Relation", "type", "Concept", "1", "The referenced concept has applies_to=relation; its label adds no endpoint rule."),
    ("Relation", "source", "IdentifiedRecord", "1", "Any of the ten record kinds, including Relation itself; self-links are permitted."),
    ("Relation", "target", "IdentifiedRecord", "1", "Any of the ten record kinds, including Relation itself; relation cycles are permitted."),
    ("Relation", "agent", "Agent", "1", "The directed link is attributed to one responsible record."),
)

POSITIONS = {
    "Text": (20, 35), "Continuity": (325, 35), "Agent": (630, 35), "Concept": (935, 35),
    "Version": (20, 235), "Selection": (325, 235), "Reading": (630, 235), "ReadingNode": (935, 235),
    "Annotation": (325, 435), "Relation": (630, 435), "IdentifiedRecord": (935, 435),
}


def build_view(root: Path, date: str, repository_base: str | None = None) -> dict:
    if repository_base is not None:
        parsed = urlsplit(repository_base)
        if parsed.scheme != "https" or not parsed.netloc or parsed.query or parsed.fragment:
            raise ValueError("repository_base must be an HTTPS repository path")
        if any(ord(char) < 32 for char in repository_base):
            raise ValueError("Unsafe repository base")
        repository_base = repository_base.rstrip("/") + "/"
    # The definition is a knowledge document; its YAML frontmatter is metadata, not model text.
    _, definition = read_document(root, DEFINITION)
    spec = json.loads((root / SPEC).read_text(encoding="utf-8"))
    profile = json.loads((root / PROFILE).read_text(encoding="utf-8"))
    if spec["model_version"] != "0.1" or profile["base_model_version"] != "0.1":
        raise ValueError("Model reference supports the explicit 0.1 contract")
    meanings = {cells[0]: cells[1] for cells in first_table_rows(definition) if len(cells) == 3}
    classes = []
    for name, key, canonical_name in KINDS:
        if canonical_name not in meanings:
            raise ValueError(f"Canonical definition lacks object row: {canonical_name}")
        fields = spec["input"][key]["required"]
        if not isinstance(fields, dict) or "id" not in fields:
            raise ValueError(f"Missing identified record contract: {name}")
        classes.append({"name": name, "key": key, "meaning": meanings[canonical_name], "fields": fields})
    by_name = {item["name"]: item for item in classes}
    for source, field, *_ in REFERENCES:
        if field not in by_name[source]["fields"]:
            raise ValueError(f"Diagram field no longer exists: {source}.{field}")
    if set(spec["input"]["selectors"]) != {"point", "ranges", "quote"}:
        raise ValueError("Unknown selector variant needs a reference update")
    return {"date": date, "base": repository_base, "definition": definition,
            "spec": spec, "profile": profile, "classes": classes}


def fields_table(fields: dict, *, optional: bool = False) -> str:
    rows = "".join(f'<tr><th scope="row"><code>{esc(key)}</code></th><td>{esc(value)}</td></tr>' for key, value in fields.items())
    label = "Optional fields" if optional else "Required fields"
    return f'<div class="model-table-scroll" tabindex="0" role="region" aria-label="{label}"><table><caption>{label}</caption><thead><tr><th scope="col">Field</th><th scope="col">Contract</th></tr></thead><tbody>{rows}</tbody></table></div>'


def diagram(view: dict) -> str:
    paths = []
    # Every reference is included. Selecting a class isolates outgoing edges;
    # the adjacent textual list supplies the exact field and multiplicity.
    for source, field, target, count, _ in REFERENCES:
        sx, sy = POSITIONS[source]
        tx, ty = POSITIONS[target]
        detours = {
            ("Relation", "agent"): "M630,483 C585,483 585,83 630,83",
            ("Relation", "type"): "M850,460 L895,460 L895,10 L1045,10 L1045,35",
            ("Annotation", "agent"): "M325,483 L280,483 L280,170 L740,170 L740,131",
            ("Reading", "version"): "M630,283 C580,175 290,175 240,283",
            ("ReadingNode", "selection"): "M935,310 C885,385 435,385 435,331",
        }
        if (source, field) in detours:
            d = detours[source, field]
        elif source == target:
            d = f"M{sx + 190},{sy + 20} C{sx + 265},{sy - 35} {sx + 270},{sy + 105} {sx + 190},{sy + 78}"
        elif sy == ty:
            start, end = (sx + 220, tx) if tx > sx else (sx, tx + 220)
            offset = 34 if field == "source" else 66 if field == "target" else 48
            d = f"M{start},{sy + offset} L{end},{ty + offset}"
        else:
            start_y, end_y = (sy + 96, ty) if ty > sy else (sy, ty + 96)
            mid = (start_y + end_y) / 2
            d = f"M{sx + 110},{start_y} C{sx + 110},{mid} {tx + 110},{mid} {tx + 110},{end_y}"
        paths.append(f'<g class="model-edge" data-source="{source}" data-target="{target}" data-field="{field}"><title>{source}.{field} → {target} ({count})</title><path d="{d}" marker-end="url(#model-arrow)"/></g>')
    nodes = []
    for item in view["classes"]:
        name = item["name"]
        x, y = POSITIONS[name]
        fields = list(item["fields"])
        summary = ", ".join(fields[:3])
        rest = ", ".join(fields[3:])
        nodes.append(f'<a href="#class-{name}" class="model-node" data-class="{name}" aria-label="Inspect {name}"><g transform="translate({x} {y})"><rect width="220" height="96" rx="4"/><text x="14" y="27" class="model-node-name">{name}</text><text x="14" y="51">{esc(summary)}</text><text x="14" y="72">{esc(rest)}</text></g></a>')
    x, y = POSITIONS["IdentifiedRecord"]
    nodes.append(f'<a href="#record-union" class="model-node model-abstract" data-class="IdentifiedRecord" aria-label="Read endpoint union: not a record kind"><g transform="translate({x} {y})"><rect width="220" height="96" rx="4"/><text x="14" y="27" class="model-node-name">IdentifiedRecord</text><text x="14" y="51">Union of all 10 kinds</text><text x="14" y="72">not an extra record kind</text></g></a>')
    return '<svg class="model-diagram" viewBox="0 0 1240 575" role="group" aria-labelledby="model-diagram-title model-diagram-desc"><title id="model-diagram-title">Abstract Text Model 0.1: record kinds and references</title><desc id="model-diagram-desc">Arrows run from a record to a referenced record. Select a class to inspect its fields and outgoing references. The complete accessible relationship table follows this diagram. IdentifiedRecord is the endpoint union, not an eleventh record kind.</desc><defs><marker id="model-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z"/></marker></defs>' + "".join(paths + nodes) + '</svg>'


def render_page(view: dict) -> str:
    spec, profile = view["spec"], view["profile"]
    md = Markdown({"notes": [], "base": view["base"], "comparisons": {"cases": []}})
    # Keep the full canonical text and hierarchy, under one page-level h1.
    canonical = re.sub(r"^(#{1,5}) ", r"#\1 ", view["definition"], flags=re.M)
    definition = md.blocks(canonical, DEFINITION)
    class_buttons = "".join(f'<button type="button" data-select-class="{item["name"]}" aria-pressed="false">{item["name"]}</button>' for item in view["classes"])
    cards = []
    for item in view["classes"]:
        name = item["name"]
        references = [(field, target, count, rule) for source, field, target, count, rule in REFERENCES if source == name]
        refs = "".join(f'<li><code>{field}</code> → <a href="#{"record-union" if target == "IdentifiedRecord" else "class-" + target}">{target}</a> <span class="model-count">{count}</span>. {esc(rule)}</li>' for field, target, count, rule in references)
        cards.append(f'<section id="class-{name}" class="model-class" data-kind="{name}" tabindex="-1"><h3>{name}</h3><p>{md.inline(item["meaning"], DEFINITION)}</p><p class="model-location">Package location: <code>{"readings[].nodes[]" if name == "ReadingNode" else item["key"] + "[]"}</code></p>{fields_table(item["fields"])}<div class="model-class-references"><h4>References from one {name}</h4><ul>{refs or "<li>No outgoing record reference fields.</li>"}</ul></div></section>')
    ref_rows = "".join(f'<tr><th scope="row"><a href="#class-{source}">{source}</a>.<code>{field}</code></th><td><a href="#{"record-union" if target == "IdentifiedRecord" else "class-" + target}">{target}</a></td><td>{count}</td><td>{esc(rule)}</td></tr>' for source, field, target, count, rule in REFERENCES)
    selectors = "".join(f'<section id="selector-{esc(name)}"><h3><code>{esc(name)}</code></h3>{fields_table(shape["required"])}' + (fields_table(shape["optional"], optional=True) if shape.get("optional") else "") + '</section>' for name, shape in spec["input"]["selectors"].items())
    rules = "".join(f'<dt id="rule-{esc(key)}"><a href="#rule-{esc(key)}">{esc(key)}</a></dt><dd>{esc(value)}</dd>' for key, value in spec["rules"].items())
    operations = "".join(f'<dt id="operation-{esc(key)}"><code>{esc(key)}</code></dt><dd>{esc(value)}</dd>' for key, value in spec["operations"].items())
    profile_rules = "".join(f'<dt id="profile-{esc(key)}">{esc(key)}</dt><dd>{esc(value)}</dd>' for key, value in profile["rules"].items())
    profile_concepts = "".join(f'<dt><code>{esc(item["id"])}</code></dt><dd><pre><code>{esc(json.dumps(item, ensure_ascii=False, indent=2))}</code></pre></dd>' for item in profile["concepts"])
    profile_operations = "".join(f'<dt><code>{esc(key)}</code></dt><dd>{esc(value)}</dd>' for key, value in profile["operations"].items())
    profile_limits = "".join(f'<li>{esc(value)}</li>' for value in profile["limits"])
    source_links = " · ".join(f'<a href="{esc(repository_link(path, view["base"]))}">{label}</a>' for path, label in ((DEFINITION, "Canonical definition"), (SPEC, "Machine-readable contract"), ("tools/models/abstract_text.py", "Reference implementation")))
    css = read_asset("workbench.css") + "\n" + read_asset("model.css")
    js = read_asset("model.js")
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="Record kinds, references, constraints and complete definition of the experimental Abstract Text Model 0.1."><title>Abstract Text Model 0.1 · TEI P6 Research</title><style>{css}</style></head>
<body><a class="skip-link" href="#main">Skip to model reference</a>{render_header("model")}
<main id="main" class="wb-main model-main"><h1>Abstract Text Model 0.1</h1><p class="wb-description">{esc(spec["authority"])}</p>
<nav class="model-sections" aria-label="Model reference sections"><a href="#class-diagram">Diagram</a><a href="#classes">Classes</a><a href="#references">Relationships</a><a href="#selectors">Selectors</a><a href="#formal-rules">Rules</a><a href="#operations">Operations</a><a href="#editorial-profile">Optional profile</a><a href="#definition">Full definition</a></nav>
<section id="class-diagram"><h2>Classes and references</h2><p>The model defines ten identified record kinds. Arrows point to referenced records. Cardinalities count targets per source record. Select a class to inspect its fields and relationships.</p>
<div class="model-controls" hidden><div class="model-class-choices" role="group" aria-label="Select a record kind">{class_buttons}</div><button type="button" id="model-show-all">Show all relationships</button></div>
<div class="model-diagram-scroll" tabindex="0" role="region" aria-label="Class diagram; scroll horizontally on small screens">{diagram(view)}</div>
<div id="model-inspector" class="model-inspector" hidden><p id="model-selection-status" aria-live="polite"></p><div id="model-inspector-content"></div></div>
<p id="record-union"><strong>IdentifiedRecord</strong> is the union of the ten record kinds. It introduces no extra class. Generic Relation endpoints can be any of these, including a relation or the same record at both ends.</p><p><code>Agent ∪ Concept ∪ Text ∪ Version ∪ Continuity ∪ Selection ∪ Reading ∪ ReadingNode ∪ Annotation ∪ Relation</code></p></section>
<section id="classes"><h2>Record contracts</h2><p>{esc(spec["input"]["package"])}</p><p>{esc(spec["input"]["id"])}</p><p><code>string</code> · {esc(spec["input"]["string"])}</p><p>These record classes define the experimental contract. Subtype inference, domain entity classes and description-logic reasoning remain outside its scope. Every listed field is required, including a parent field whose value may be null.</p><div class="model-classes">{"".join(cards)}</div></section>
<section id="references"><h2>Relationship cardinalities</h2><p>A target can have zero or many incoming references unless an inverse requirement is stated explicitly. Reading nodes are nested records with exactly one containing Reading. Other reference relationships do not imply containment.</p><div class="model-table-scroll" tabindex="0" role="region" aria-label="Complete relationship cardinalities"><table><thead><tr><th scope="col">Source field</th><th scope="col">Target kind</th><th scope="col">Per source</th><th scope="col">Additional constraint</th></tr></thead><tbody>{ref_rows}</tbody></table></div></section>
<section id="selectors"><h2>Selector value types</h2><p>Each Selection contains exactly one selector value. Point, ranges and quote are three alternatives. Resolution results are operation outputs. Neither selectors nor results are identified package records.</p>{selectors}<h3>Resolution contract</h3>{fields_table(spec["validation_result"])}<h3>Resolved target shapes</h3><pre><code>{esc(json.dumps(spec["target_shapes"], ensure_ascii=False, indent=2))}</code></pre></section>
<section id="formal-rules"><h2>Class logic and invariants</h2><p>The constraints below are generated directly from the executable model contract. They define identity, typed references, graph structure, selection and change operations. Formal validity does not evaluate the truth or logical consistency of a concept definition or annotation body.</p><dl class="model-rules">{rules}</dl></section>
<section id="operations"><h2>Operations</h2><dl class="model-operations">{operations}</dl><p>All public operations leave inputs unchanged. A reanchor result is a proposal with <code>accepted: false</code>.</p></section>
<section id="editorial-profile"><h2>Optional editorial provenance profile</h2><p>{esc(profile["authority"])}</p><p>This profile constrains the existing Concept and Relation records. It introduces no new record kinds and requires its own validation.</p><p><a href="{esc(repository_link(PROFILE, view["base"]))}">Profile contract {esc(profile["profile_version"])}</a></p><dl class="model-operations">{profile_concepts}</dl><dl class="model-rules">{profile_rules}</dl><h3>Profile operations</h3><dl class="model-operations">{profile_operations}</dl><h3>Profile boundaries</h3><ul>{profile_limits}</ul></section>
<section id="definition" class="model-definition"><h2>Complete canonical definition</h2><p>{source_links}</p><p>The text below is rendered from the maintained definition on every build. The diagram and tables above are navigation aids to this contract, outside the source-grounding chain. Its source-supported argument and project posits are available in the <a href="index.html#proposal">proposal</a>.</p><article>{definition}</article></section>
</main>{render_footer(view["date"])}<script>{js}</script></body></html>'''
