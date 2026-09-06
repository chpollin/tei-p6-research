"""Read and validate canonical inputs; no HTML and no network access."""
from __future__ import annotations

import json
import re
from pathlib import Path
from urllib.parse import urlsplit

from tools.sitegen import comparison_view
from tools.sitegen.documents import WIKI, first_table_rows, read_document

PROPOSAL = "40_output/12-p6-design.md"
MODEL = "knowledge/text-model.md"
CASES = "experiments/editorial_cases/cases.json"
SYNTHETIC = "experiments/abstract_text_v01/examples/competing-readings.json"


def wiki_path(value: str) -> str:
    match = WIKI.fullmatch(value)
    target = match.group(1) if match else value
    path, _, anchor = target.partition("#")
    return path + ("" if Path(path).suffix in (".md", ".xml", ".pdf", ".json", ".yaml") else ".md") + (f"#{anchor}" if anchor else "")


def check_editorial_excerpt(root: Path, cases: dict) -> None:
    """Gate the build on the pinned, licensed excerpt the page attributes."""
    case = next((c for c in cases["cases"] if c["case_id"] == "case-2-interrupted-heading" and not c.get("holdout")), None)
    if case is None:
        raise ValueError("Required development editorial case is missing")
    for required in ("primary_text", "primary_segments", "unknown_hand_note_text", "editorial_note_text", "original_xml"):
        if required not in case:
            raise ValueError(f"Editorial case lacks {required}")
    if len(case["primary_segments"]) != 2:
        raise ValueError("Interrupted-heading presentation requires two primary segments")
    metadata, _ = read_document(root, f"10_markdown/documents/{cases['source']}.md")
    metadata = metadata.get("metadata", {})
    if not metadata.get("identifier") or metadata.get("license") != "CC-BY-SA-4.0" or not cases.get("attribution"):
        raise ValueError("Editorial excerpt lacks pinned source, attribution or expected license")


def check_synthetic_illustration(synthetic: dict) -> None:
    """Gate the build on extents that reconcile with the version they select."""
    version = synthetic["versions"][0]
    selections = {s["id"]: s for s in synthetic["selections"]}
    agents = {a["id"] for a in synthetic["agents"]}
    for reading in synthetic["readings"]:
        if reading["agent"] not in agents:
            raise ValueError("Synthetic illustration attributes a reading to an unknown agent")
        for node in reading["nodes"]:
            selection = selections[node["selection"]]
            for segment in selection["selector"]["segments"]:
                if not all(type(segment.get(key)) is int for key in ("start", "end")) or not 0 <= segment["start"] < segment["end"] <= len(version["content"]):
                    raise ValueError("Synthetic illustration has an invalid extent")
                if selection["version"] != version["id"] or version["content"][segment["start"]:segment["end"]] != segment["quote"]:
                    raise ValueError("Synthetic illustration does not reconcile to its version")


def statement(body: str) -> str:
    match = re.search(r"^## Statement\s*\n(.*?)(?=^## |\Z)", body, re.M | re.S)
    if not match or not match.group(1).strip():
        raise ValueError("Assertion has no Statement section")
    return match.group(1).strip()


def build_view(root: Path, date: str, repository_base: str | None = None) -> dict:
    if repository_base:
        parsed = urlsplit(repository_base)
        if parsed.scheme != "https" or not parsed.netloc or parsed.query or parsed.fragment:
            raise ValueError("repository_base must be an HTTPS repository path")
        repository_base = repository_base.rstrip("/") + "/"
    _, body = read_document(root, PROPOSAL)
    _, model = read_document(root, MODEL)
    cases = json.loads((root / CASES).read_text(encoding="utf-8"))
    synthetic = json.loads((root / SYNTHETIC).read_text(encoding="utf-8"))
    references = {}
    for path in sorted((root / "references").glob("*.json")):
        records = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(records, list):
            references.update({r["id"]: r for r in records if isinstance(r, dict) and "id" in r})
    footnotes = {}
    text_lines = []
    current = None
    for line in body.splitlines():
        match = re.match(r"^\[\^([\w.-]+)\]:\s*(.*)", line)
        if match:
            current = match.group(1)
            if current in footnotes:
                raise ValueError(f"Duplicate footnote: {current}")
            footnotes[current] = match.group(2)
        elif current and line.startswith(("    ", "\t")):
            footnotes[current] += "\n" + line.strip()
        else:
            current = None
            text_lines.append(line)
    body = "\n".join(text_lines).strip()
    used = list(dict.fromkeys(re.findall(r"\[\^([\w.-]+)\]", body)))
    if set(used) != set(footnotes):
        raise ValueError("Proposal footnote definitions and references do not reconcile")
    notes = []
    counters = {"grounded": 0, "posit": 0}
    for key in used:
        definition = footnotes[key]
        grounded = WIKI.findall(definition)
        kind = "posit" if definition.startswith("Posit:") else "grounded"
        if kind == "grounded" and not grounded:
            raise ValueError(f"Footnote has neither posit nor assertion: {key}")
        counters[kind] += 1
        note = {"id": key, "kind": kind, "label": ("P" if kind == "posit" else "G") + str(counters[kind]), "text": definition, "assertions": []}
        if kind == "posit":
            rationale, marker, question = definition.removeprefix("Posit:").strip().partition("Open evidence question:")
            if not marker or not question.strip():
                raise ValueError(f"Posit lacks open evidence question: {key}")
            note.update(rationale=rationale.strip(), question=question.strip())
        else:
            for target, _ in grounded:
                assertion_path = wiki_path(target)
                if not assertion_path.startswith("30_assertions/"):
                    raise ValueError("Premise must link directly to an assertion")
                ameta, abody = read_document(root, assertion_path.split("#")[0])
                links = [{"label": "Assertion", "path": assertion_path}]
                if not ameta.get("grounding"):
                    raise ValueError(f"Assertion has no grounding: {assertion_path}")
                for grounding in ameta["grounding"]:
                    dist_path = wiki_path(grounding)
                    if not dist_path.startswith("20_distillates/"):
                        raise ValueError("Assertion grounding must target a distillate")
                    dmeta, dbody = read_document(root, dist_path.split("#")[0])
                    block = dist_path.partition("#")[2]
                    if block and not re.search(re.escape(block) + r"(?:\s|$)", dbody):
                        raise ValueError(f"Missing distillate block: {dist_path}")
                    links.append({"label": "Distillate " + block, "path": dist_path})
                    if dmeta.get("representation"):
                        rep_path = wiki_path(dmeta["representation"])
                        rmeta, _ = read_document(root, rep_path.split("#")[0])
                        links.append({"label": "Source representation", "path": rep_path})
                        identifier = rmeta.get("metadata", {}).get("identifier")
                        if identifier:
                            links.append({"label": "Pinned original", "url": identifier})
                    elif dmeta.get("reference"):
                        ref = references.get(dmeta["reference"])
                        if not ref or not ref.get("URL"):
                            raise ValueError(f"Missing source citation: {dmeta['reference']}")
                        links.append({"label": ref.get("title", "Source citation"), "url": ref["URL"]})
                    else:
                        raise ValueError(f"Distillate lacks source: {dist_path}")
                note["assertions"].append({"statement": statement(abody), "path": assertion_path, "links": links})
        notes.append(note)
    object_definitions = {cells[0]: cells[1] for cells in first_table_rows(model) if len(cells) >= 2}
    for required in ("Version", "Reading", "Annotation", "Relation"):
        if required not in object_definitions:
            raise ValueError(f"Model definition missing {required}")
    check_editorial_excerpt(root, cases)
    check_synthetic_illustration(synthetic)
    return {"date": date, "base": repository_base, "body": body, "notes": notes,
            "definitions": object_definitions, "attribution": cases["attribution"],
            "comparisons": comparison_view.build_comparisons(root),
            "paths": {"proposal": PROPOSAL, "model": MODEL, "cases": CASES, "synthetic": SYNTHETIC}}
