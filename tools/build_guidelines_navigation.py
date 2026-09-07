"""Join tracked Guidelines coverage and the declaration atlas for navigation.

Run ``python -m tools.build_guidelines_navigation [--check]``. The contract in
knowledge/architecture.md keeps rule-based topic suggestions outside grounding.
No original, Git mirror, network access or source mutation is involved.
"""
from __future__ import annotations

import argparse
import json
import re
from hashlib import sha256
from pathlib import Path

from tools.sitegen.documents import read_document

OUTPUT = "corpus/projections/guidelines-navigation-4.12.0.json"
COVERAGE = "corpus/projections/guidelines-4.12.0.json"
ATLAS = "corpus/projections/p5-specs-4.12.0.json"
MODULE_TOPICS = {
    "analysis": "Annotation and Overlap", "certainty": "Metadata and Entities",
    "cmc": "Text and Document Structures", "core": "Text and Document Structures",
    "corpus": "Text and Document Structures", "dictionaries": "Text and Document Structures",
    "drama": "Text and Document Structures", "figures": "Text and Document Structures",
    "gaiji": "Interoperability and Processing", "header": "Metadata and Entities",
    "iso-fs": "Annotation and Overlap", "linking": "Annotation and Overlap",
    "msdescription": "Metadata and Entities", "namesdates": "Metadata and Entities",
    "nets": "Text and Document Structures", "spoken": "Text and Document Structures",
    "tagdocs": "ODD and Customization", "tei": "P5 Architecture",
    "textcrit": "Critical Apparatus", "textstructure": "Text and Document Structures",
    "transcr": "Text and Document Structures", "verse": "Text and Document Structures",
}
CHAPTER_MODULES = {
    "AI": "analysis", "CC": "corpus", "CE": "certainty", "CH": "gaiji",
    "CMC": "cmc", "CO": "core", "DI": "dictionaries", "DR": "drama",
    "DS": "textstructure", "FS": "iso-fs", "FT": "figures", "GD": "nets",
    "HD": "header", "MS": "msdescription", "ND": "namesdates", "NH": "linking",
    "PH": "transcr", "SA": "linking", "ST": "tei", "TC": "textcrit",
    "TD": "tagdocs", "TS": "spoken", "VE": "verse", "WD": "gaiji",
}


def passage_locations(body: str) -> dict[str, str]:
    result = {}
    for section in re.split(r"^### (?:Block|Reading) \d+\s*$", body, flags=re.M)[1:]:
        location = re.search(r"^XML location: `([^`]+)`\.", section, re.M)
        anchor = re.search(r"\^([A-Za-z0-9-]+)\s*\Z", section)
        if location and anchor:
            result[location[1]] = anchor[1]
    return result


def locate(locator: str, locations: dict[str, str]) -> dict:
    local = re.sub(r"\{[^}]+\}", "", locator)
    candidates = [p for p in locations if local == p or local.startswith(p + "/")]
    if candidates:
        path = max(candidates, key=len)
        return {"anchor": locations[path], "anchor_scope": "exact" if path == local else "containing-block"}
    return {"anchor": None, "anchor_reason": "No existing block covers this XML location; open the complete representation."}


def build(root: Path) -> dict:
    root = Path(root)
    inputs = {}

    def read(path: str) -> bytes:
        payload = (root / path).read_bytes()
        inputs[path] = sha256(payload).hexdigest()
        return payload

    coverage, atlas = json.loads(read(COVERAGE)), json.loads(read(ATLAS))
    if coverage["commit"] != atlas["source"]["commit"] or coverage["release"] != atlas["source"]["version"]:
        raise ValueError("Guidelines and atlas release identities differ")
    topics = {}
    for path in sorted((root / "30_assertions").glob("MOC-*.md"), key=lambda p: p.name):
        relative = path.relative_to(root).as_posix()
        read(relative)
        meta, _ = read_document(root, relative)
        if meta.get("type") != "moc" or not meta.get("topic"):
            raise ValueError(f"Invalid topic map: {relative}")
        topics[meta["topic"]] = relative
    specs = {r["source"]["path"]: r for r in atlas["records"]}
    if len(specs) != len(atlas["records"]):
        raise ValueError("Duplicate atlas source")
    rows, locations = {}, {}
    for source in coverage["sources"]:
        path, representation = source["source"], source["representation"]
        if path in rows or not representation.startswith("10_markdown/documents/") or ".." in Path(representation).parts:
            raise ValueError(f"Invalid or duplicate source: {path}")
        read(representation)
        meta, body = read_document(root, representation)
        if meta.get("type") != "representation" or meta.get("metadata", {}).get("confidential"):
            raise ValueError(f"Invalid public representation: {representation}")
        locations[path] = passage_locations(body)
        spec = specs.get(path)
        prefix = Path(path).stem.split("-")[0]
        module = spec["module_declared"] if spec else CHAPTER_MODULES.get(prefix)
        category = spec["category"] if spec else ("chapter" if prefix in CHAPTER_MODULES else "support")
        suggestions = []

        def suggest(topic: str, rule: str, *, suggestions: list = suggestions) -> None:
            if topic not in topics:
                raise ValueError(f"Topic rule names absent MOC: {topic}")
            suggestions.append({"topic": topic, "moc": topics[topic], "rule": rule})

        if spec:
            suggest("Elements and Classes", f"spec-category:{category}")
        if module in MODULE_TOPICS:
            suggest(MODULE_TOPICS[module], f"{'declared-module' if spec else 'chapter-module-map'}:{module}")
        if not spec and prefix == "REF":
            suggest("Elements and Classes", "reference-section:REF")
        if not spec and prefix in {"AB", "SG", "USE"}:
            suggest("P5 Architecture", f"chapter-prefix:{prefix}")
        rows[path] = {
            "source": path, "representation": representation,
            "representation_sha256": inputs[representation], "title": source["title"],
            "kind": category, "module": module, "module_basis": "declared" if spec else "chapter-map",
            "ident": spec["ident"] if spec else None, "topic_suggestions": suggestions,
            "unclassified_reason": None if suggestions else "No topic rule for this support source; scholarly classification remains open.",
            "references": [], "referenced_by": [],
        }
    if set(specs) - set(rows):
        raise ValueError("Atlas specifications missing from admitted coverage")
    by_ident = {r["ident"]: rows[p] for p, r in specs.items()}
    for path, spec in specs.items():
        if spec["source"]["commit"] != coverage["commit"]:
            raise ValueError(f"Specification commit mismatch: {path}")
        row = rows[path]
        for ref in spec["references"]:
            destination = by_ident.get(ref["target"])
            resolved = ref["resolution"] == "declaration-present"
            if resolved and (destination is None or destination["kind"] != ref["expected_category"]):
                raise ValueError(f"Invalid resolved atlas reference: {path}")
            edge = {"relation": ref["name"].split("}")[-1], "target": ref["target"],
                    "xml_location": ref["locator"], **locate(ref["locator"], locations[path]),
                    "resolution": ref["resolution"],
                    "target_representation": destination["representation"] if resolved else None,
                    "reason": None if resolved else ref.get("reason", "Unresolved in declaration atlas")}
            row["references"].append(edge)
            if resolved:
                destination["referenced_by"].append({"ident": row["ident"], "representation": row["representation"],
                                                     "relation": edge["relation"], "xml_location": edge["xml_location"],
                                                     **locate(ref["locator"], locations[path])})
    return {"schema_version": 1, "generated": True, "generator": "tools.build_guidelines_navigation v1",
            "use": "navigation-only; never grounding", "classification": "rule-based topic suggestions; not scholarly assessment",
            "instruction_trust": "none", "release": coverage["release"], "commit": coverage["commit"],
            "inputs": dict(sorted(inputs.items())), "topics": topics,
            "counts": {"sources": len(rows), "specifications": len(specs),
                       "unclassified": sum(not r["topic_suggestions"] for r in rows.values())},
            "sources": [rows[p] for p in sorted(rows)]}


def serialized(view: dict) -> str:
    return json.dumps(view, ensure_ascii=False, indent=2, sort_keys=True) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = serialized(build(args.root))
    output = args.root / OUTPUT
    if args.check:
        if not output.exists() or output.read_bytes() != result.encode("utf-8"):
            raise ValueError("Guidelines navigation missing or stale; regenerate it")
    else:
        output.write_text(result, encoding="utf-8", newline="\n")
    print("OK: Guidelines navigation reproduces" if args.check else f"Built {output}")


if __name__ == "__main__":
    main()
