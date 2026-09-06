"""Crawl a bounded official web index into the local raw and normalized corpus."""

from __future__ import annotations

import argparse
import re
import urllib.parse
from collections import deque
from html.parser import HTMLParser
from pathlib import Path

from tools.corpus.http_store import HttpStore, canonical_url, utc_now
from tools.corpus.manifest import (
    build_manifest,
    report_status,
    sha256_file,
    status_from,
    write_jsonl,
    write_yaml,
)

TEXT_EXTENSIONS = {
    "",
    ".css",
    ".csv",
    ".dtd",
    ".htm",
    ".html",
    ".json",
    ".md",
    ".odd",
    ".rdf",
    ".rng",
    ".sch",
    ".txt",
    ".xhtml",
    ".xml",
    ".xsd",
    ".xsl",
    ".xslt",
    ".yaml",
    ".yml",
}


class LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        candidate = None
        if tag in {"a", "link"}:
            candidate = attributes.get("href")
        elif tag in {"img", "script", "iframe", "source"}:
            candidate = attributes.get("src")
        elif tag == "object":
            candidate = attributes.get("data")
        if candidate:
            self.links.append(candidate)


def extract_links(base_url: str, body: bytes, media_type: str) -> list[str]:
    if media_type not in {"text/html", "application/xhtml+xml", "application/xml", "text/xml"}:
        return []
    parser = LinkParser()
    text = body.decode("utf-8", errors="replace")
    try:
        parser.feed(text)
        candidates = parser.links
    except (AssertionError, ValueError):
        # Some early TEI Archive pages contain SGML declarations that Python's
        # HTML parser rejects. A conservative attribute fallback preserves the
        # link census without interpreting arbitrary markup.
        candidates = re.findall(
            r'''(?i)\b(?:href|src|data)\s*=\s*["']([^"']+)["']''',
            text,
        )
    links: set[str] = set()
    for link in candidates:
        resolved = urllib.parse.urljoin(base_url, link)
        parsed = urllib.parse.urlsplit(resolved)
        if parsed.scheme not in {"http", "https"}:
            continue
        links.add(canonical_url(resolved))
    return sorted(links)


def is_allowed(url: str, prefixes: list[str], include_binary: bool) -> bool:
    if not any(url.startswith(prefix) for prefix in prefixes):
        return False
    if include_binary:
        return True
    path = urllib.parse.urlsplit(url).path
    # Dotted version directories such as ``/Vault/P5/4.12.0/`` are HTML
    # indexes, not binary files.
    suffix = "" if path.endswith("/") else Path(path).suffix.lower()
    return suffix in TEXT_EXTENSIONS


def crawl(
    *,
    source_id: str,
    root_url: str,
    allow_prefixes: list[str],
    depth: int,
    max_pages: int,
    include_binary: bool,
    raw_root: Path,
    normalized_output: Path,
    manifest_output: Path,
) -> dict[str, object]:
    started_at = utc_now()
    store = HttpStore(raw_root)
    root = canonical_url(root_url)
    prefixes = [canonical_url(prefix) for prefix in allow_prefixes]
    queue: deque[tuple[str, int]] = deque([(root, 0)])
    queued = {root}
    records: list[dict[str, object]] = []
    external_links: set[str] = set()
    skipped_binary: set[str] = set()
    boundary_links: set[str] = set()
    gaps: list[dict[str, object]] = []
    truncated = False

    while queue:
        if len(records) >= max_pages:
            truncated = True
            break
        url, current_depth = queue.popleft()
        try:
            result, body = store.fetch(url)
        except RuntimeError as error:
            gaps.append({"code": "fetch-failed", "url": url, "detail": str(error)})
            continue

        links = extract_links(result.final_url, body, result.media_type)
        records.append(
            {
                "schema_version": 1,
                "source_id": source_id,
                "depth": current_depth,
                "response": result.as_record(),
                "links": links,
            }
        )
        if result.status >= 400:
            gaps.append({"code": "http-error", "url": url, "status": result.status})
            continue
        for link in links:
            if not any(link.startswith(prefix) for prefix in prefixes):
                external_links.add(link)
                continue
            if not is_allowed(link, prefixes, include_binary):
                skipped_binary.add(link)
                continue
            if current_depth >= depth:
                if link not in queued:
                    boundary_links.add(link)
                continue
            if link not in queued:
                queued.add(link)
                queue.append((link, current_depth + 1))

    records.sort(key=lambda row: str(row["response"]["canonical_url"]))  # type: ignore[index]
    write_jsonl(normalized_output, records)
    normalized_hash = sha256_file(normalized_output)
    if truncated:
        gaps.append(
            {
                "code": "page-limit-reached",
                "max_pages": max_pages,
                "remaining_queue": len(queue),
            }
        )
    for link in sorted(skipped_binary):
        gaps.append({"code": "binary-link-inventoried-not-fetched", "url": link})

    manifest = build_manifest(
        run_id=manifest_output.stem,
        source_id=source_id,
        adapter="tools.corpus.web_census",
        started_at=started_at,
        finished_at=utc_now(),
        status=status_from(gaps),
        requests=[
            {
                "root_url": root,
                "allow_prefixes": prefixes,
                "depth": depth,
                "max_pages": max_pages,
                "include_binary": include_binary,
            }
        ],
        objects=[
            {
                "kind": "web-census",
                "path": normalized_output.as_posix(),
                "sha256": normalized_hash,
            }
        ],
        counts={
            "responses": len(records),
            "successful_responses": sum(
                1 for row in records if int(row["response"]["status"]) < 400  # type: ignore[index]
            ),
            "external_links_inventoried": len(external_links),
            "depth_boundary_links_inventoried": len(boundary_links),
            "binary_links_inventoried_not_fetched": len(skipped_binary),
            "gaps": len(gaps),
        },
        gaps=gaps,
        rights_exceptions=[
            "Raw response bodies remain local until per-item redistribution rights are reviewed."
        ],
        extra={
            "external_links": sorted(external_links),
            "depth_boundary_links": sorted(boundary_links),
        },
    )
    write_yaml(manifest_output, manifest)
    return manifest


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-id", required=True)
    parser.add_argument("--root-url", required=True)
    parser.add_argument("--allow-prefix", action="append", required=True)
    parser.add_argument("--depth", type=int, default=1)
    parser.add_argument("--max-pages", type=int, default=1000)
    parser.add_argument("--include-binary", action="store_true")
    parser.add_argument("--raw-root", type=Path, default=Path("corpus/raw"))
    parser.add_argument("--normalized-output", type=Path, required=True)
    parser.add_argument("--manifest-output", type=Path, required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.depth < 0 or args.max_pages < 1:
        raise SystemExit("depth must be >= 0 and max-pages must be >= 1")
    manifest = crawl(
        source_id=args.source_id,
        root_url=args.root_url,
        allow_prefixes=args.allow_prefix,
        depth=args.depth,
        max_pages=args.max_pages,
        include_binary=args.include_binary,
        raw_root=args.raw_root,
        normalized_output=args.normalized_output,
        manifest_output=args.manifest_output,
    )
    counts = manifest["counts"]
    return report_status(manifest, f"{counts['responses']} responses, {counts['gaps']} gaps")


if __name__ == "__main__":
    raise SystemExit(main())
