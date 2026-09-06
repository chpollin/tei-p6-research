"""Check wave-one publication quotations against local immutable source bytes.

This checks quotation fidelity and identity, not whether a claim follows from a
quotation. It neither fetches sources nor changes research check dates/statuses.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from typing import ClassVar

import yaml

if __package__ in (None, ""):  # run as a script, so the package root is not on the path
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tools.review import (
    ReviewAudit,
    _load_docs,
    check_review_records,
    read_jsonl,
    select_pairs,
)
from tools.validate import _link_targets

DEFAULT_MANIFEST = "sources/manifests/2026-09-05-research-wave-1-citations.yaml"
REFERENCES = "references/research-wave-1.json"
REVIEW_DIRECTORY = "workbench/reviews/2026-09-05-wave1"
REVIEW_CHAPTER = "40_output/06-annotation-and-overlap.md"


class VisibleText(HTMLParser):
    """Join inline text without invented spaces; separate block boundaries."""

    ignored: ClassVar[set[str]] = {"script", "style", "head", "template"}
    blocks: ClassVar[set[str]] = {
        "address", "article", "aside", "blockquote", "br", "dd", "div", "dl",
        "dt", "fieldset", "figcaption", "figure", "footer", "form", "h1",
        "h2", "h3", "h4", "h5", "h6", "header", "hr", "li", "main", "nav",
        "ol", "p", "pre", "section", "table", "td", "th", "tr", "ul",
    }

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []
        self.suppressed: list[str] = []

    def handle_starttag(self, tag: str, attrs: list) -> None:
        if tag in self.ignored:
            self.suppressed.append(tag)
        if not self.suppressed and tag in self.blocks:
            self.parts.append(" ")

    def handle_endtag(self, tag: str) -> None:
        if self.suppressed:
            if tag == self.suppressed[-1]:
                self.suppressed.pop()
            return
        if tag in self.blocks:
            self.parts.append(" ")

    def handle_data(self, data: str) -> None:
        if not self.suppressed:
            self.parts.append(data)


def extract_text(raw: bytes, extraction: dict) -> str:
    """Decode once; JSON fields remain literal, including HTML-like escapes."""
    decoded = raw.decode("utf-8-sig")
    kind = extraction.get("kind")
    if kind == "html-visible-text":
        parser = VisibleText()
        parser.feed(decoded)
        parser.close()
        return " ".join("".join(parser.parts).split())
    if kind == "json-field":
        path = extraction.get("path")
        if not isinstance(path, list) or not path:
            raise ValueError("JSON field path must be a nonempty list")
        value = json.loads(decoded)
        for key in path:
            addressable = (isinstance(value, dict) and isinstance(key, str) and key in value) or (
                isinstance(value, list) and type(key) is int and 0 <= key < len(value))
            if not addressable:
                raise ValueError(f"JSON field path does not resolve: {path!r}")
            value = value[key]
        if not isinstance(value, str):
            raise ValueError("JSON field path must resolve to a string")
        return value
    raise ValueError(f"unsupported extraction kind: {kind!r}")


def local_path(base: Path, value: object, label: str) -> Path:
    if not isinstance(value, str) or not value or Path(value).is_absolute():
        raise ValueError(f"{label} must be a nonempty relative path")
    result = (base / value).resolve()
    if not result.is_relative_to(base.resolve()):
        raise ValueError(f"{label} escapes its local directory")
    return result


def read_distillate(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8-sig")
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].strip() != "---":
        raise ValueError("distillate has no YAML frontmatter")
    end = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), None)
    if end is None:
        raise ValueError("distillate frontmatter is not closed")
    metadata = yaml.safe_load("".join(lines[1:end]))
    if not isinstance(metadata, dict):
        raise ValueError("distillate frontmatter must be a mapping")
    return metadata, "".join(lines[end + 1:])


def check(root: Path, manifest: str = DEFAULT_MANIFEST) -> tuple[int, int]:
    root = root.resolve()
    data = yaml.safe_load(local_path(root, manifest, "manifest").read_text(encoding="utf-8"))
    admissions = data.get("admissions") if isinstance(data, dict) else None
    if not isinstance(admissions, list) or not admissions:
        raise ValueError("manifest admissions must be a nonempty list")
    bibliography = json.loads((root / REFERENCES).read_text(encoding="utf-8"))
    if not isinstance(bibliography, list) or not bibliography:
        raise ValueError("CSL bibliography must be a nonempty list")
    refs: set[str] = set()
    for record in bibliography:
        identifier = record.get("id") if isinstance(record, dict) else None
        if not isinstance(identifier, str) or not identifier or identifier in refs:
            raise ValueError("CSL reference IDs must be nonempty and unique")
        refs.add(identifier)
    seen: set[str] = set()
    quotation_count = 0
    for admission in admissions:
        if not isinstance(admission, dict):
            raise ValueError("admission must be a mapping")
        identifier = admission.get("reference_id")
        if not isinstance(identifier, str) or identifier not in refs or identifier in seen:
            raise ValueError(f"missing, unknown or duplicate admission reference ID: {identifier!r}")
        seen.add(identifier)
        try:
            if admission.get("source_type") != "publication":
                raise ValueError("admission source_type must be publication")
            response = admission.get("response")
            if not isinstance(response, dict):
                raise ValueError("response must be a mapping")
            status = response.get("status")
            if type(status) is not int or not 200 <= status < 300:
                raise ValueError("source response status must be successful (2xx)")
            digest = response.get("sha256")
            if not isinstance(digest, str) or not re.fullmatch(r"[0-9a-f]{64}", digest):
                raise ValueError("response sha256 must contain 64 lowercase hexadecimal digits")
            size = response.get("byte_count")
            if type(size) is not int or size < 0:
                raise ValueError("response byte_count must be a nonnegative integer")
            raw_path = local_path(root / "corpus/raw", response.get("raw_path"), "raw_path")
            if not raw_path.is_file():
                raise ValueError(f"local raw source unavailable: {raw_path}")
            raw = raw_path.read_bytes()
            if len(raw) != size:
                raise ValueError("raw byte_count mismatch")
            if hashlib.sha256(raw).hexdigest() != digest:
                raise ValueError("raw sha256 mismatch")
            extraction = admission.get("extraction")
            if not isinstance(extraction, dict):
                raise ValueError("extraction must be a mapping")
            source_text = extract_text(raw, extraction)
            metadata, body = read_distillate(local_path(
                root, admission.get("distillate_path"), "distillate_path"))
            if metadata.get("source-type") != "publication" or metadata.get("type") != "distillate":
                raise ValueError("distillate metadata must declare a publication distillate")
            if metadata.get("reference") != identifier:
                raise ValueError("distillate reference does not match admission reference ID")
            quotes = admission.get("quotes")
            if not isinstance(quotes, list) or not quotes:
                raise ValueError("quotes must be a nonempty list")
            for quote in quotes:
                if not isinstance(quote, dict):
                    raise ValueError("quote must be a mapping")
                text, locator = quote.get("text"), quote.get("locator")
                if not isinstance(text, str) or not text.strip():
                    raise ValueError("quote text must be nonempty")
                if not isinstance(locator, str) or not locator.strip():
                    raise ValueError("quote locator must be nonempty")
                if text not in source_text:
                    raise ValueError(f"quotation absent from extracted source at {locator}")
                if text not in body:
                    raise ValueError(f"quotation absent verbatim from distillate at {locator}")
                quotation_count += 1
        except (OSError, ValueError, yaml.YAMLError) as error:
            raise ValueError(f"{identifier}: {error}") from error
    if seen != refs:
        raise ValueError("CSL bibliography and admission reference IDs do not match")
    return len(seen), quotation_count


def current_review_pairs(root: Path, manifest: str = DEFAULT_MANIFEST) -> list[dict]:
    """Derive four source pairs and their reviewed chapter's direct assertions."""
    root = root.resolve()
    data = yaml.safe_load(local_path(root, manifest, "manifest").read_text(encoding="utf-8"))
    admissions = data.get("admissions") if isinstance(data, dict) else None
    if not isinstance(admissions, list) or len(admissions) != 4:
        raise ValueError("wave-one review scope requires exactly four admissions")
    sources: dict[str, str] = {}
    for admission in admissions:
        if not isinstance(admission, dict) or admission.get("source_type") != "publication":
            raise ValueError("review admissions must be publications")
        path = local_path(root, admission.get("distillate_path"), "distillate_path")
        relative = path.relative_to(root).with_suffix("").as_posix()
        reference = admission.get("reference_id")
        if not isinstance(reference, str) or not reference or reference in sources.values() or relative in sources:
            raise ValueError("review admissions require unique references and distillates")
        if not relative.startswith("20_distillates/publications/") or path.suffix != ".md":
            raise ValueError("review admission must name a canonical publication distillate")
        metadata, _ = read_distillate(path)
        if (metadata.get("type") != "distillate" or metadata.get("source-type") != "publication"
                or metadata.get("reference") != reference):
            raise ValueError("review distillate metadata does not match admission")
        sources[relative] = reference
    bibliography = json.loads((root / REFERENCES).read_text(encoding="utf-8"))
    if (not isinstance(bibliography, list) or len(bibliography) != 4
            or any(not isinstance(record, dict) for record in bibliography)
            or sorted(str(record.get("id")) for record in bibliography) != sorted(sources.values())):
        raise ValueError("review bibliography and admission reference IDs do not match")
    docs = _load_docs(root)
    required_anchors = {f"{source}#^s1" for source in sources}
    chapter_path = local_path(root, data.get("review_chapter", REVIEW_CHAPTER), "review_chapter")
    chapter, _ = read_distillate(chapter_path)
    mirror = chapter.get("assertions")
    if chapter.get("type") != "chapter" or not isinstance(mirror, list) or not mirror:
        raise ValueError("review chapter must declare a nonempty assertions mirror")
    chapter_roots: set[str] = set()
    for raw in mirror:
        links = _link_targets(str(raw))
        if len(links) != 1:
            raise ValueError("review chapter assertion mirror entries must name one assertion")
        target, block = links[0]
        if block or target in chapter_roots or target not in docs or docs[target].fm.get("type") != "assertion":
            raise ValueError("review chapter assertion root is missing, invalid or duplicated")
        chapter_roots.add(target)
    assertions: dict[str, str] = {}
    for relative in sorted(chapter_roots):
        doc = docs[relative]
        grounding = doc.fm.get("grounding") or []
        if not isinstance(grounding, list):
            raise ValueError(f"{relative}: assertion grounding must be a list")
        links = [link for raw in grounding for link in _link_targets(str(raw))]
        if not any(target in sources for target, _ in links):
            continue
        anchors = [f"{target}#^{block}" for target, block in links]
        if len(grounding) != 1 or len(anchors) != 1 or anchors[0] not in required_anchors:
            raise ValueError(f"{relative}: wave-one assertion must ground only one admitted s1")
        assertions[relative] = anchors[0]
    if len(assertions) != 4 or set(assertions.values()) != required_anchors:
        raise ValueError("wave-one review scope requires four assertions, one for each admitted s1")
    documents = set(sources) | set(assertions)
    selected = select_pairs(root, lambda pair: pair.document in documents, documents)
    expected_ids = required_anchors | {f"{doc}<-{anchor}" for doc, anchor in assertions.items()}
    if len(selected) != 8 or {pair.id for pair in selected} != expected_ids:
        raise ValueError("wave-one review requires exactly eight canonical pairs")
    result = []
    for pair in selected:
        record = pair.to_dict()
        record["prompt_sha256"] = hashlib.sha256(pair.prompt.encode("utf-8")).hexdigest()
        result.append(record)
    return result


def check_review(root: Path, manifest: str = DEFAULT_MANIFEST) -> ReviewAudit:
    """Audit the recorded wave-one review against the pairs the vault cuts today."""
    audit = root / REVIEW_DIRECTORY
    return check_review_records(
        current_review_pairs(root, manifest),
        read_jsonl(audit / "pairs.jsonl"),
        read_jsonl(audit / "verdicts.jsonl"),
        expected=8,
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path, nargs="?", default=Path())
    parser.add_argument("--manifest", default=DEFAULT_MANIFEST, help="manifest path relative to root")
    parser.add_argument("--review-only", action="store_true", help="check eight saved support reviews without local raw sources")
    args = parser.parse_args(argv)
    try:
        if args.review_only:
            audit = check_review(args.root, args.manifest)
            if audit.without_reviewer:
                print(f"WARN: verdicts without a reviewer: {', '.join(audit.without_reviewer)}",
                      file=sys.stderr)
            print(f"OK: {audit.pairs} passing review verdicts bind all current wave-one canonical pairs.")
            return 0
        sources, quotes = check(args.root, args.manifest)
    except (OSError, ValueError, yaml.YAMLError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        return 1
    print(f"OK: {quotes} quotations match {sources} local publication sources and distillates.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
