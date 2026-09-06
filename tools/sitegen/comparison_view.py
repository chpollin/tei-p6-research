"""Assemble bounded example comparisons; navigation, never Vault grounding.

P5 fragments are authored illustrations unless explicitly taken from the
pinned diary. Candidate validation and binding round trips run during build.
"""
from __future__ import annotations

import copy
import hashlib
import json
import xml.etree.ElementTree as ET
from pathlib import Path

from tools.ingest_editorial_cases import embedded_source
from tools.models.abstract_text import equivalent, propose_reanchor, validate_model
from tools.models.bindings import decode_model, encode_model
from tools.sitegen.markup import doc_id
from tools.tei.editorial_cases import compare_fragment

P5_COMMIT = "113e933e21f016e2655518321e9d10214b8d9fcb"
P5_BASE = f"https://github.com/TEIC/TEI/blob/{P5_COMMIT}/P5/Source/"
TEI = "http://www.tei-c.org/ns/1.0"

# Coverage axes are project-authored indexing suggestions. Module names follow
# the P5 4.12.0 Infrastructure module table, not the candidate ontology.
MODULES = [
    ("tei", "TEI infrastructure", ["classes", "datatypes", "model composition"], []),
    ("header", "Common metadata", ["description", "responsibility", "correspondence"], ["letter", "charter"]),
    ("core", "Common core", ["paragraph", "quotation", "note"], ["prose", "letter", "diary"]),
    ("textstructure", "Default text structure", ["containment", "composite text"], ["book", "anthology"]),
    ("gaiji", "Characters and glyphs", ["character identity", "glyph", "writing mode"], ["inscription"]),
    ("verse", "Verse", ["verse line", "stanza", "metre"], ["poem"]),
    ("drama", "Performance texts", ["speaker", "stage direction", "performance"], ["play"]),
    ("spoken", "Transcribed speech", ["turn", "pause", "simultaneity"], ["interview", "conversation"]),
    ("cmc", "Computer-mediated communication", ["message", "reply", "digital context"], ["chat", "forum"]),
    ("dictionaries", "Dictionaries", ["headword", "sense", "pronunciation"], ["dictionary entry"]),
    ("msdescription", "Manuscript description", ["carrier", "hand", "provenance"], ["manuscript", "charter"]),
    ("transcr", "Primary-source representation", ["addition", "deletion", "spatial position"], ["draft", "letter"]),
    ("textcrit", "Critical apparatus", ["witness", "variant", "lemma"], ["critical edition"]),
    ("namesdates", "Names, dates, people and places", ["entity reference", "dating", "identity"], ["letter", "charter", "encyclopedia entry"]),
    ("figures", "Tables, formulae, graphics and notated music", ["tabular order", "formula", "media"], ["scientific text", "score"]),
    ("corpus", "Language-corpus metadata", ["collection", "sampling", "classification"], ["corpus"]),
    ("linking", "Linking, segmentation and alignment", ["overlap", "discontinuity", "alignment"], []),
    ("analysis", "Analysis and interpretation", ["annotation", "interpretation", "segmentation"], []),
    ("iso-fs", "Feature structures", ["feature", "value", "unification"], []),
    ("nets", "Graphs, networks and trees", ["typed relation", "graph", "tree"], []),
    ("certainty", "Certainty, precision and responsibility", ["uncertainty", "responsibility", "precision"], []),
    ("tagdocs", "Documentation elements", ["ODD", "customization", "documentation"], []),
]


def read_json(root: Path, path: str):
    return json.loads((root / path).read_text(encoding="utf-8"))


def p5_variant(identifier, title, xml, notes, specs, status="Authored P5 illustration; no full ODD conformance claim"):
    """Parse inert namespace-bound fragments, without claiming schema validity."""
    if "<!DOCTYPE" in xml or "<!ENTITY" in xml:
        raise ValueError("external declarations in P5 illustration")
    ET.fromstring(f'<example xmlns="{TEI}">{xml}</example>')
    return {"id": identifier, "title": title, "xml": xml, "status": status,
            "notes": notes, "sources": [{"label": f"P5 4.12.0 {spec}", "url": P5_BASE + f"Specs/{spec}.xml"} for spec in specs]}


def graph_for(package):
    nodes, edges = [], []
    for collection, kind in [("versions", "Version"), ("selections", "Selection"),
                             ("readings", "Reading"), ("annotations", "Annotation"),
                             ("agents", "Agent"), ("continuities", "Continuity"), ("texts", "Text"),
                             ("concepts", "Concept"), ("relations", "Relation")]:
        for record in package[collection]:
            nodes.append({"id": record["id"], "label": record["id"] + " · " + kind, "kind": kind})
            for key in ("version", "agent", "selection", "text", "type", "source", "target"):
                if key in record:
                    edges.append({"source": record["id"], "target": record[key], "label": key})
            for target in record.get("versions", []):
                edges.append({"source": record["id"], "target": target, "label": "membership"})
            for target in record.get("parents", []):
                edges.append({"source": record["id"], "target": target, "label": "technical input"})
            for node in record.get("nodes", []):
                nodes.append({"id": node["id"], "label": node["id"] + " · " + node["type"], "kind": "Node"})
                edges.append({"source": record["id"], "target": node["id"], "label": "contains"})
                edges.append({"source": node["id"], "target": node["selection"], "label": "selection"})
                edges.append({"source": node["id"], "target": node["type"], "label": "type"})
                if node["parent"] is not None:
                    edges.append({"source": node["id"], "target": node["parent"], "label": "parent"})
    return {"nodes": nodes, "edges": edges}


def candidate(package, notes):
    validation = validate_model(package)
    if not validation["valid"]:
        raise ValueError("invalid candidate in example catalogue")
    serializations = {binding: encode_model(package, binding) for binding in ("json", "xml", "yaml")}
    for binding, payload in serializations.items():
        if not equivalent(package, decode_model(payload, binding)):
            raise ValueError("example binding round trip failed: " + binding)
    return {"status": "Valid model 0.1; JSON/XML/YAML round trips preserve declared equivalence",
            "serializations": serializations, "validation": validation, "notes": notes}


def case_record(identifier, title, phenomenon, package, description, p5, formal, limits, source_kind="Synthetic example", notes=""):
    return {"id": identifier, "title": title, "phenomenon": phenomenon,
            "source_kind": source_kind, "description": description,
            "primary_text": package["versions"][0]["content"], "p5": p5,
            "candidate": candidate(package, notes), "formal": formal, "limits": limits,
            "graph": graph_for(package), "links": []}


def build_comparisons(root: Path) -> dict:
    root = Path(root)
    suite = read_json(root, "experiments/abstract_text_v01/cases.json")
    cases = []
    overlap = copy.deepcopy(read_json(root, "experiments/abstract_text_v01/examples/competing-readings.json"))
    content = "Der alte Baum steht."
    overlap["versions"][0].update(content=content, sha256=hashlib.sha256(content.encode()).hexdigest())
    overlap["relations"] = []  # syntactic and verse structures need not disagree
    overlap["concepts"] = [
        {"id": "noun-phrase", "label": "Nominalgruppe", "definition": "Syntactic phrase asserted in this constructed example.", "applies_to": "node"},
        {"id": "verse-line", "label": "Verszeile", "definition": "Verse line proposed in this constructed example; not a source observation.", "applies_to": "node"},
    ]
    for selection, start, end in zip(overlap["selections"], [0, 9], [13, 20], strict=True):
        selection["selector"]["segments"] = [{"start": start, "end": end, "quote": content[start:end]}]
    for reading, kind in zip(overlap["readings"], ["noun-phrase", "verse-line"], strict=True):
        reading["nodes"][0]["type"] = kind
        reading["label"] = kind
    overlap_p5 = [
        p5_variant("stand-off", "Anchors and two stand-off layers", '<p><anchor xml:id="p0"/>Der alte <anchor xml:id="p9"/>Baum<anchor xml:id="p13"/> steht.<anchor xml:id="p20"/></p>\n<spanGrp type="syntax">\n  <span xml:id="n1" from="#p0" to="#p13" resp="#editorA">Nominalgruppe</span>\n</spanGrp>\n<spanGrp type="versification">\n  <span xml:id="n2" from="#p9" to="#p20" resp="#editorB">Verszeile</span>\n</spanGrp>', "Fragments within a TEI document. Agent definitions are omitted. Both ranges are expressed by pointers; this example does not claim that overlap is new to the candidate.", ["anchor", "span", "spanGrp"]),
        p5_variant("primary-tree", "Inline phrase and stand-off verse layer", '<p><seg xml:id="n1" type="nounPhrase" resp="#editorA">Der alte <anchor xml:id="b"/>Baum</seg> steht.<anchor xml:id="e"/></p>\n<spanGrp type="versification">\n  <span xml:id="n2" from="#b" to="#e" resp="#editorB">Verszeile</span>\n</spanGrp>', "One structure is inline; the other uses pointers. The task must define how each structure is exposed to processors. The candidate does not establish lower authoring or query cost.", ["seg", "anchor", "span"]),
    ]
    cases.append(case_record("overlap", "Crossing structural readings", "Overlap and attributed structure", overlap,
        "Inspect a syntactic phrase and a proposed verse line over one unchanged character sequence. These descriptions can coexist without disagreeing.", overlap_p5,
        ["v1 = 20 Unicode code points. nodeA selects [0,13), nodeB selects [9,20).",
         "Each node belongs to exactly one reading and refers to one contiguous resolved selection in that reading's version.",
         "Crossing extents are allowed across readings; siblings within one reading cannot overlap.",
         "Node identity, extent and type are separate. Record order does not rank readings."],
        ["The verse line is invented for this example, not a philological finding.", "P5 fragments are parsed illustrations; an effective ODD and complete document are still needed for a P5 conformance verdict."]))

    parts = copy.deepcopy(suite["models"]["discontinuous"])
    cases.append(case_record("discontinuous", "One target with separated parts", "Discontinuous annotation target", parts,
        "Select ab and ef in abcdef as the two components of one annotation target; cd is excluded.",
        [p5_variant("join", "Join separately identified segments", '<p><seg xml:id="a">ab</seg>cd<seg xml:id="b">ef</seg></p>\n<join xml:id="parts" target="#a #b" result="seg" scope="branches"/>', "join describes an aggregation of possibly discontiguous elements. This illustration joins the text children of the two segments. Its virtual-element semantics and the candidate's aggregate region need an explicit mapping contract.", ["join", "seg"])],
        ["One Selection(parts) has ordered segments [0,2) and [4,6) in v1.", "Resolution returns one region target containing two segments, not two independently selected targets.", "Segments must be ascending, disjoint and nonempty; an annotation can refer to the aggregate."],
        ["A noncontiguous selection cannot be a structural node in model 0.1.", "Automatic reanchoring of multisegment selections is unsupported."]))

    ambiguous = copy.deepcopy(suite["models"]["ambiguous_annotation"])
    cases.append(case_record("ambiguous-target", "A quotation with several possible locations", "Unresolved single-target intent", ambiguous,
        "The annotation seeks one occurrence of aa in aaaa. Three overlapping occurrences exist; none is accepted.",
        [p5_variant("explicit-alternatives", "Explicit candidate spans and exclusive alternatives", '<p><anchor xml:id="p0"/>a<anchor xml:id="p1"/>a<anchor xml:id="p2"/>a<anchor xml:id="p3"/>a<anchor xml:id="p4"/></p>\n<spanGrp type="candidateLocation">\n  <span xml:id="c1" from="#p0" to="#p2"/>\n  <span xml:id="c2" from="#p1" to="#p3"/>\n  <span xml:id="c3" from="#p2" to="#p4"/>\n</spanGrp>\n<alt mode="excl" target="#c1 #c2 #c3"/>', "An authored alternative-location convention using explicit spans and alt. The application still needs to define how this alternative group is the unresolved target of its annotation and how candidates are generated. This is not a tested P5 converter.", ["anchor", "span", "alt"])],
        ["quote(exact='aa', match='one') yields candidates [0,2), [1,3), [2,4).", "valid=true, status=ambiguous, accepted targets=[], diagnostic=W_AMBIGUOUS.", "match='all' instead yields three independent targets; this is different intent."],
        ["Selection ambiguity is not a probability of transcription correctness.", "The P5 illustration enumerates candidates; model 0.1 computes literal matches over a frozen sequence."]))

    identity = read_json(root, "experiments/abstract_text_v01/examples/identity-and-reanchoring.json")
    identity_case = case_record("identity-reanchoring", "Keep an annotation stable after editing", "Version identity and reanchoring", identity,
        "red fox becomes a red fox!, then red fox / red fox. An existing annotation retains its source; proposed locations in new versions require separate acceptance.",
        [p5_variant("identified-states", "Identify textual states and keep the original target", '<p xml:id="v1"><seg xml:id="source">red fox</seg></p>\n<p xml:id="v2">a red fox!</p>\n<p xml:id="v3">red fox / red fox</p>\n<span from="#source" resp="#editor">Original annotation</span>', "This illustration identifies states and an annotation target. It does not by itself specify immutable version records, editorial continuity criteria, or a reanchoring algorithm; those require an explicit project contract. It makes no claim that P5 cannot carry such a contract.", ["span", "seg"])],
        ["Reused version IDs retain exact content, hash and declared technical parent membership.", "Reanchoring requires an explicit attributed continuity claim covering source and destination versions.", "A unique match, several candidates, or no match is returned as an unaccepted proposal; source records are unchanged."],
        ["Technical construction inputs are distinct from historical derivation hypotheses.", "This synthetic example is not a historical finding about an edition."])
    outcomes = {version: propose_reanchor(identity, "source_range", version, "continuity") for version in ["v2", "v3", "v4"]}
    identity_case["candidate"]["notes"] = "Computed reanchoring outcomes:\n" + json.dumps(outcomes, ensure_ascii=False, indent=2)
    cases.append(identity_case)

    source_payload = embedded_source(root)
    editorial = read_json(root, "experiments/editorial_cases/cases.json")
    source_info = read_json(root, "experiments/editorial_cases/intake.json")
    case_specs = [
        ("case-1-hierarchy", False, "equal-extents", "Different objects with the same extent", "humboldt-diary-encodes-a-dated-nested-heading"),
        ("case-2-interrupted-heading", False, "editorial-notes", "Main reading and nested editorial notes", "humboldt-diary-separates-an-unknown-hand-note-and-editorial-explanation"),
        ("case-3-holdout-media", True, "page-foliation", "Page break, foliation and image pointer", "humboldt-diary-encodes-a-page-pointer-and-separate-foliation"),
    ]
    by_id = {item["case_id"]: item for item in editorial["cases"]}
    if len(editorial["cases"]) != 3 or set(by_id) != {item[0] for item in case_specs}:
        raise ValueError("editorial comparison case boundary changed")
    for source_id, holdout, identifier, title, assertion in case_specs:
        original = by_id[source_id]
        if original["holdout"] is not holdout:
            raise ValueError("editorial comparison holdout role changed")
        raw = source_payload[original["start_byte"]:original["end_byte"]]
        if raw.decode("utf-8") != original["original_xml"] or hashlib.sha256(raw).hexdigest() != original["fragment_sha256"]:
            raise ValueError("editorial example source drift")
        result = compare_fragment(original["original_xml"])
        variant = p5_variant("source-encoding", "Pinned edition XML", original["original_xml"],
            "Exact source fragment; inherited TEI namespace. " + editorial["attribution"] + " Original and adapted source observations: CC BY-SA 4.0. Full RNG/ODD conformance was not established.", [], "Real edition fragment at pinned commit")
        source_url = source_info["edition_url"] + f'#L{original["start_line"]}-L{original["end_line"]}'
        provenance_url = "knowledge.html#" + doc_id(f"30_assertions/{assertion}.md")
        variant["sources"] = [{"label": "Pinned diary passage", "url": source_url},
                              {"label": "Assertion and provenance chain", "url": provenance_url},
                              {"label": "CC BY-SA 4.0", "url": "https://creativecommons.org/licenses/by-sa/4.0/"}]
        formal = (["The heading, date and outer highlighting retain distinct node IDs despite equal extents.", "Parent and child extents may be equal. Containment remains acyclic."]
                  if identifier == "equal-extents" else
                  ["The declared main-text projection excludes note characters, collapses whitespace, and trims its ends.",
                   "Note nesting and reference relationships are encoded inside annotation bodies using tei-fragment-0.1. They are not core Relation records and are not shown as relationships in the core instance diagram."])
        limits = ["Three fragments of one diary do not represent all TEI practice.", "Source pointers and responsibility tokens are retained without external resolution."]
        if result["candidate"]["valid"]:
            limits.append("Source attributes and note metadata require the tei-fragment-0.1 decoder. Core model validation treats annotation bodies as strings and does not check these meanings.")
            case = case_record(identifier, title, title, result["candidate"]["package"], original["editorial_task"], [variant], formal, limits,
                "Real edition: Humboldt diary H0017682", "Bounded mapping under the declared projection and tei-fragment-0.1 metadata binding. " + editorial["projection_policy"])
        else:
            case = {"id": identifier, "title": title, "phenomenon": title,
                    "source_kind": "Real edition: reserved adverse fragment", "description": original["editorial_task"],
                    "primary_text": original["primary_text"], "p5": [variant],
                    "candidate": {"status": "Mapping refused. pb and fw are unsupported. No candidate package exists.", "serializations": {},
                                  "validation": {"valid": False, "diagnostics": result["candidate"]["unsupported"]},
                                  "notes": "Explicit refusal is a passed failure-detection check, not a successful migration. The baseline tree retains markup but its primary prose projection also fails this task."},
                    "formal": ["Preserve the distinction between primary prose, page boundary, foliation and lexical image pointer.", "The current frozen mapper returns no package. No candidate binding or instance diagram exists for this fragment."],
                    "limits": [*limits, "No image alignment or full-document migration is established."], "graph": {"nodes": [], "edges": []}, "links": []}
        case["links"] = [{"label": "Assertion and provenance chain", "url": provenance_url}]
        cases.append(case)

    coverage = [{"module": module, "title": title, "status": "Coverage inventory; domain evaluation pending",
                 "phenomena": phenomena, "document_types": documents} for module, title, phenomena, documents in MODULES]
    return {"cases": cases, "coverage": coverage,
            "bindings": [{"id": key, "label": label, "status": status} for key, label, status in
                         [("json", "JSON", "Implemented reference binding"), ("xml", "XML", "Implemented experimental binding"),
                          ("yaml", "YAML", "Implemented experimental binding"), ("jsonld", "JSON-LD", "Not implemented"), ("rdf", "RDF", "Not implemented")]]}
