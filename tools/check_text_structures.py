"""Emit and audit source-support pairs for the bounded structure run.

The global pair cutter remains unchanged. This run adds mechanically recovered
XML ancestor labels to its source context, following the review contract.
Use --emit --scope source before review; the default audits both recorded
batches against current sources and claims, without booking research statuses.
"""

import argparse
import json
import re
from dataclasses import replace
from pathlib import Path

import yaml

from tools import ingest_git_blobs as ingest
from tools import review
from tools.admit_text_structure_citations import REFERENCES
from tools.ingest_guidelines import MANIFEST, XML_ID, parse_xml
from tools.ingest_text_structures import RUN

DIRECTORY = "workbench/reviews/2026-09-07-text-structures-run1"
SLUGS = (
    "tei-p5-guidelines-nh-non-hierarchical-4.12.0",
    "tei-p5-guidelines-ds-defaulttextstructure-4.12.0",
    "tei-p5-att.fragmentable-4.12.0", "tei-p5-att.global.linking-4.12.0",
    "tei-p5-join-4.12.0", "tei-p5-milestone-4.12.0", "tei-p5-pb-4.12.0",
    "tei-p5-div-4.12.0", "tei-p5-note-4.12.0", "tei-p5-test-testoverlap-4.12.0",
)
DOCUMENTS = frozenset(
    [f"20_distillates/documents/{slug}" for slug in SLUGS]
    + [f"20_distillates/publications/teic-tei-issue-{number}" for number in (1400, 1505)]
)


def ancestor_context(payload: bytes, locator: str) -> str:
    node = parse_xml(payload)
    segments = locator.strip("/").split("/")
    labels = []
    for depth, segment in enumerate(segments):
        match = re.fullmatch(r"([A-Za-z0-9_-]+)\[(\d+)\]", segment)
        if not match:
            raise ValueError(f"unsupported source locator: {locator}")
        tag, number = match[1], int(match[2])
        if depth == 0:
            if node.tag.split("}")[-1] != tag or number != 1:
                raise ValueError(f"root locator mismatch: {locator}")
        else:
            children = [child for child in node if child.tag.split("}")[-1] == tag]
            if number < 1 or number > len(children):
                raise ValueError(f"source locator does not resolve: {locator}")
            node = children[number - 1]
        attrs = {key.split("}")[-1]: value for key, value in node.attrib.items()
                 if key in {"ident", "key", "type", "n", XML_ID}}
        label = tag + (" " + json.dumps(attrs, ensure_ascii=False, sort_keys=True) if attrs else "")
        head = next((child for child in node if child.tag.split("}")[-1] == "head"), None)
        if head is not None:
            label += " heading=" + json.dumps(" ".join("".join(head.itertext()).split()), ensure_ascii=False)
        labels.append(label)
    return "XML ancestor context (from the unchanged source): " + " > ".join(labels)


def current_pairs(root: Path, scope: str) -> list[dict]:
    problems = []
    pairs = review.cut_pairs(root, problems)
    if problems:
        raise ValueError("Pair cutter problems: " + "; ".join(problems))
    if scope == "assertion":
        selected = [pair for pair in pairs if pair.kind == scope and pair.document.startswith("30_assertions/structure-")]
        if not selected:
            raise ValueError("No structure assertions to review")
        return [pair.to_dict() for pair in selected]
    rows = {}
    for path in (MANIFEST, RUN.manifest):
        data = yaml.safe_load((root / path).read_text(encoding="utf-8"))
        for row in data["admissions"]:
            rows[row["representation_path"].removesuffix(".md")] = row
    bibliography = {item["id"]: item for item in json.loads((root / REFERENCES).read_bytes())}
    result, payloads = [], {}
    selected = [pair for pair in pairs if pair.kind == "source" and pair.document in DOCUMENTS]
    if {pair.document for pair in selected} != DOCUMENTS:
        raise ValueError("Source review must cover all twelve selected sources")
    for pair in selected:
        if pair.anchor.startswith("10_markdown/"):
            path = pair.anchor.split("#")[0]
            row = rows[path]
            if path not in payloads:
                admission = ingest.Admission(row["git_path"], row["git_blob_id"], row["original_bytes"],
                                             Path(path).name, "", "", "guidelines-reference")
                payloads[path] = ingest.embedded_source(admission, (root / row["representation_path"]).read_bytes())
            location = re.search(r"XML location: `([^`]+)`", pair.location)
            if not location:
                raise ValueError(f"Source passage lacks XML location: {pair.id}")
            context = ancestor_context(payloads[path], location[1])
        else:
            citation = bibliography[pair.anchor]
            context = "Bibliographic source identity: " + citation["title"] + " (" + citation["URL"] + ")"
        result.append(replace(pair, location=context + "\n" + pair.location).to_dict())
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--scope", choices=("source", "assertion", "all"), default="all")
    parser.add_argument("--emit", action="store_true")
    args = parser.parse_args()
    directory = args.root / DIRECTORY
    for scope in ("source", "assertion") if args.scope == "all" else (args.scope,):
        current = current_pairs(args.root, scope)
        pair_path = directory / f"{scope}-pairs.jsonl"
        if args.emit:
            payload = "".join(json.dumps(pair, ensure_ascii=False) + "\n" for pair in current).encode()
            ingest.immutable_output(pair_path, payload, check=False)
            print(f"OK: {len(current)} {scope} pairs emitted")
        else:
            verdicts = review.read_jsonl(directory / f"{scope}-verdicts.jsonl")
            audit = review.check_review_records(current, review.read_jsonl(pair_path), verdicts,
                                               required_fields=(*review.REQUIRED_VERDICT_FIELDS, "reviewer", "model"))
            if any(verdict["model"] == "gpt-6-astra" for verdict in verdicts):
                raise ValueError("The structure author and reviewer must use different models")
            print(f"OK: {audit.pairs} {scope} verdicts reconcile; no human verification established")


if __name__ == "__main__":
    main()
