"""Reproduce the bounded pilot and check its source-support review audit."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import xml.etree.ElementTree as ET
from dataclasses import replace
from pathlib import Path

if __package__ in (None, ""):  # run as a script, so the package root is not on the path
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tools.ingest_text_identity import XML_LANG, embedded_source
from tools.review import (
    Pair,
    ReviewAudit,
    _load_docs,
    check_review_records,
    read_jsonl,
    select_pairs,
)
from tools.validate import _chapter_scope

ROOT = Path(__file__).resolve().parents[1]
DOCUMENTS = {
    "20_distillates/documents/tei-p5-anchor-4.12.0",
    "20_distillates/documents/tei-p5-span-4.12.0",
    "20_distillates/documents/tei-p5-annotation-4.12.0",
    "30_assertions/p5-anchor-identifies-a-textual-point",
    "30_assertions/p5-span-associates-interpretation-with-text",
    "30_assertions/p5-span-from-identifies-start-or-whole-node",
    "30_assertions/p5-annotation-refers-to-web-annotation-model",
}
AUDIT = ROOT / "workbench/reviews/2026-09-05-text-identity"


def source_context(pair: Pair, docs: dict) -> str:
    """Supply source identity and XML ancestor labels, never producer rationale."""
    representation, anchor = pair.anchor.split("#^", 1)
    name = representation.rsplit("/tei-p5-", 1)[1].removesuffix("-4.12.0")
    doc = docs[representation]
    source = ET.fromstring(embedded_source(name, doc.path.read_bytes()))
    contexts: list[str] = []

    def walk(element, ancestors: list[str], parent=None):
        tag = element.tag.rsplit("}", 1)[-1]
        label = tag + (f"[@ident='{element.attrib['ident']}']" if "ident" in element.attrib else "")
        chain = [*ancestors, label]
        if (tag == "desc" and element.get(XML_LANG) == "en") or (
            tag == "p" and parent is not None
            and parent.tag.rsplit("}", 1)[-1] == "remarks"
            and parent.get(XML_LANG) == "en"
        ):
            contexts.append(" > ".join(chain))
        for child in element:
            walk(child, chain, element)

    walk(source, [])
    number = anchor.removeprefix("r") if anchor.startswith("r") else ""
    index = int(number) - 1 if number.isdigit() else -1
    if not 0 <= index < len(contexts):
        raise ValueError(f"unknown source reading-block context: ^{anchor}")
    metadata = doc.fm["metadata"]
    return (f"Source identity: {metadata['title']}\n"
            f"Source locator: {metadata['identifier']}\n"
            f"XML heading path: {contexts[index]}\n{pair.location}")


def current_pairs(root: Path = ROOT) -> list[dict]:
    """Recheck the bounded pilot sources independently of the growing proposal."""
    docs = _load_docs(root)
    if DOCUMENTS - docs.keys():
        raise ValueError("pilot review document coverage is incomplete")
    closure = {}
    for name in sorted(DOCUMENTS):
        closure.update(_chapter_scope(docs[name], docs))
    required = {name for name, doc in closure.items()
                if doc.fm.get("type") in {"distillate", "assertion"}}
    if required != DOCUMENTS:
        raise ValueError("pilot review scope changed; update and review its complete evidence closure")
    selected = select_pairs(root, lambda pair: pair.document in required, required)
    pairs = [replace(p, location=source_context(p, docs)).to_dict()
             if p.kind == "source" else p.to_dict() for p in selected]
    if {p["document"] for p in pairs} != DOCUMENTS:
        raise ValueError("pilot review document coverage is incomplete")
    return pairs


def check_review(
    pairs: list[dict], stored: list[dict], verdicts: list[dict]
) -> ReviewAudit:
    """Fail closed on stale prompts, omissions, duplicates, or nonpassing review."""
    return check_review_records(pairs, stored, verdicts)


def run(*args: str) -> None:
    subprocess.run([sys.executable, *args], cwd=ROOT, check=True)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--emit-review", action="store_true", help="emit support pairs after validation")
    args = parser.parse_args()
    try:
        run("-m", "tools.ingest_text_identity", "--check")
        pairs = current_pairs()
        if args.emit_review:
            AUDIT.mkdir(parents=True, exist_ok=True)
            payload = "".join(json.dumps(p, ensure_ascii=False) + "\n" for p in pairs)
            (AUDIT / "pairs.jsonl").write_text(payload, encoding="utf-8", newline="\n")
            print(f"Emitted {len(pairs)} pairs; independent review is still required.")
            return 0
        audit = check_review(pairs, read_jsonl(AUDIT / "pairs.jsonl"),
                             read_jsonl(AUDIT / "verdicts.jsonl"))
        if audit.without_reviewer:
            print(f"WARN: verdicts without a reviewer: {', '.join(audit.without_reviewer)}",
                  file=sys.stderr)
        print(f"OK: {audit.pairs} bounded pilot source-support verdicts match current prompts; "
              "this audit does not review the expanded chapter.", flush=True)
        run("-m", "tools.pilots.text_identity", "--check")
    except (OSError, ValueError, subprocess.CalledProcessError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        return 1
    print("OK: bounded pilot reproduction and source review passed. Repository completion and human acceptance are separate.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
