"""Reproduce the bounded pilot and check its source-support review audit."""

from __future__ import annotations

import argparse
from dataclasses import replace
import hashlib
import json
import subprocess
import sys
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "tools"))
from review import _load_docs, cut_pairs  # noqa: E402
from validate import Report, _chapter_scope, _parse_doc  # noqa: E402
from tools.ingest_text_identity import XML_LANG, embedded_source  # noqa: E402

DOCUMENTS = {
    "20_distillates/documents/tei-p5-anchor-4.12.0",
    "20_distillates/documents/tei-p5-span-4.12.0",
    "20_distillates/documents/tei-p5-annotation-4.12.0",
    "30_assertions/p5-anchor-identifies-a-textual-point",
    "30_assertions/p5-span-associates-interpretation-with-text",
    "30_assertions/p5-span-from-identifies-start-or-whole-node",
    "30_assertions/p5-annotation-refers-to-web-annotation-model",
}
AUDIT = ROOT / "experiments/text_identity/review"


def prompt_hash(pair: dict) -> str:
    return hashlib.sha256(pair["prompt"].encode("utf-8")).hexdigest()


def source_context(root: Path, pair, docs: dict) -> str:
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
    index = int(anchor.removeprefix("r")) - 1
    if not anchor.startswith("r") or index < 0 or index >= len(contexts):
        raise ValueError("unknown source reading-block context")
    metadata = doc.fm["metadata"]
    return (f"Source identity: {metadata['title']}\n"
            f"Source locator: {metadata['identifier']}\n"
            f"XML heading path: {contexts[index]}\n{pair.location}")


def current_pairs(root: Path = ROOT) -> list[dict]:
    docs = _load_docs(root)
    report = Report()
    chapter = _parse_doc(root / "40_output/02-abstract-model.md", root, report)
    if chapter is None or report.errors:
        raise ValueError("pilot chapter cannot be parsed")
    closure = _chapter_scope(chapter, docs)
    required = {name for name, doc in closure.items()
                if doc.fm.get("type") in {"distillate", "assertion"}}
    if required != DOCUMENTS:
        raise ValueError("chapter review scope changed; update and review the complete evidence closure")
    problems: list[str] = []
    selected = [p for p in cut_pairs(root, problems) if p.document in required]
    pairs = [replace(p, location=source_context(root, p, docs)).to_dict()
             if p.kind == "source" else p.to_dict() for p in selected]
    if problems:
        raise ValueError("; ".join(problems))
    if {p["document"] for p in pairs} != DOCUMENTS:
        raise ValueError("pilot review document coverage is incomplete")
    return pairs


def check_review(pairs: list[dict], stored: list[dict], verdicts: list[dict]) -> None:
    """Fail closed on stale prompts, omissions, duplicates, or nonpassing review."""
    if stored != pairs:
        raise ValueError("review pairs are stale; re-emit and independently review changes")
    expected = {p["id"]: p for p in pairs}
    if len(expected) != len(pairs) or not expected:
        raise ValueError("review pairs must have unique IDs and be nonempty")
    seen: set[str] = set()
    for verdict in verdicts:
        pair_id = verdict.get("id")
        if not isinstance(pair_id, str) or pair_id not in expected or pair_id in seen:
            raise ValueError("unknown or duplicate review verdict")
        seen.add(pair_id)
        if verdict.get("verdict") != "fully supports":
            raise ValueError(f"nonpassing verdict: {pair_id}")
        if verdict.get("prompt_sha256") != prompt_hash(expected[pair_id]):
            raise ValueError(f"review input hash mismatch: {pair_id}")
        if not isinstance(verdict.get("reason"), str) or not verdict["reason"].strip():
            raise ValueError(f"review rationale missing: {pair_id}")
        if not isinstance(verdict.get("reviewer"), str) or not verdict["reviewer"].strip():
            raise ValueError(f"reviewer attribution missing: {pair_id}")
    if seen != set(expected):
        raise ValueError("unreviewed pairs remain")


def read_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def run(*args: str) -> None:
    subprocess.run([sys.executable, *args], cwd=ROOT, check=True)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--emit-review", action="store_true", help="emit support pairs after validation")
    args = parser.parse_args()
    try:
        run("tools/validate.py", ".")
        run("tools/validate.py", ".", "--chapter", "40_output/02-abstract-model.md")
        run("-m", "tools.ingest_text_identity", "--check")
        pairs = current_pairs()
        if args.emit_review:
            AUDIT.mkdir(parents=True, exist_ok=True)
            payload = "".join(json.dumps(p, ensure_ascii=False) + "\n" for p in pairs)
            (AUDIT / "pairs.jsonl").write_text(payload, encoding="utf-8", newline="\n")
            print(f"Emitted {len(pairs)} pairs; independent review is still required.")
            return 0
        check_review(pairs, read_jsonl(AUDIT / "pairs.jsonl"), read_jsonl(AUDIT / "verdicts.jsonl"))
        print(f"OK: {len(pairs)} source-support verdicts match current prompts.", flush=True)
        run("-m", "tools.corpus.validate_control_plane", ".")
        run("-m", "tools.pilots.text_identity", "--check")
        run("-m", "pytest", "tests", "-q")
    except (OSError, ValueError, subprocess.CalledProcessError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        return 1
    print("OK: pilot technical gate passed. Human acceptance and verification remain separate.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
