"""Fetch explicitly enumerated large release assets into the raw store."""

from __future__ import annotations

import argparse
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import yaml

from tools.corpus.http_store import HttpStore, canonical_url, utc_now
from tools.corpus.manifest import sha256_file, write_json, write_yaml


def snapshot(
    *,
    source_id: str,
    urls: list[str],
    raw_root: Path,
    normalized_output: Path,
    manifest_output: Path,
    staged_file: Path | None = None,
    staged_url: str | None = None,
    expected_bytes: int | None = None,
    workers: int = 4,
    input_manifest: Path | None = None,
) -> dict[str, object]:
    started_at = utc_now()
    store = HttpStore(raw_root, timeout=120, retries=3)
    records: list[dict[str, object]] = []
    gaps: list[dict[str, object]] = []
    if staged_file is not None:
        staging_root = (raw_root / "staging").resolve()
        resolved_staged = staged_file.resolve()
        if not resolved_staged.is_relative_to(staging_root):
            raise RuntimeError(f"staged file must be inside {staging_root}")
        byte_count = resolved_staged.stat().st_size
        if expected_bytes is not None and byte_count != expected_bytes:
            raise RuntimeError(
                f"staged file size mismatch: expected {expected_bytes}, observed {byte_count}"
            )
        digest = sha256_file(resolved_staged)
        relative = Path("sha256") / digest[:2] / digest[2:]
        destination = raw_root / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        if destination.exists():
            resolved_staged.unlink()
        else:
            os.replace(resolved_staged, destination)
        records.append(
            {
                "requested_url": canonical_url(str(staged_url)),
                "canonical_url": canonical_url(str(staged_url)),
                "final_url": canonical_url(str(staged_url)),
                "observed_at": utc_now(),
                "status": 200,
                "media_type": "application/zip",
                "byte_count": byte_count,
                "sha256": digest,
                "raw_path": relative.as_posix(),
                "headers": {},
                "transfer": "resumed-external-download-then-local-import",
            }
        )
    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {executor.submit(store.fetch_stream, url): url for url in urls}
        for future in as_completed(futures):
            url = futures[future]
            try:
                records.append(future.result().as_record())
            except RuntimeError as error:
                gaps.append({"code": "asset-fetch-failed", "url": url, "detail": str(error)})
    requested_count = len(urls) + int(staged_file is not None)
    records.sort(key=lambda record: str(record["canonical_url"]))
    write_json(normalized_output, {"schema_version": 1, "source_id": source_id, "assets": records})
    manifest: dict[str, object] = {
        "schema_version": 1,
        "run_id": manifest_output.stem,
        "source_id": source_id,
        "started_at": started_at,
        "finished_at": utc_now(),
        "status": "observable-complete" if not gaps and len(records) == requested_count else "partial",
        "adapter": {"name": "tools.corpus.asset_snapshot", "version": 1},
        "requests": ([{"url": staged_url, "transfer": "resumed"}] if staged_file else [])
        + [{"url": url, "transfer": "streamed"} for url in urls],
        "derived_from_manifests": [input_manifest.as_posix()] if input_manifest else [],
        "objects": [
            {
                "kind": "release-asset-inventory",
                "path": normalized_output.as_posix(),
                "sha256": sha256_file(normalized_output),
            }
        ],
        "counts": {
            "requested_assets": requested_count,
            "retrieved_assets": len(records),
            "bytes": sum(int(record["byte_count"]) for record in records),
            "gaps": len(gaps),
        },
        "assets": records,
        "gaps": gaps,
        "rights_exceptions": ["Release assets remain in ignored content-addressed raw storage."],
    }
    write_yaml(manifest_output, manifest)
    return manifest


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-id", required=True)
    parser.add_argument("--url", action="append", default=[])
    parser.add_argument("--gap-manifest", type=Path)
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--staged-file", type=Path)
    parser.add_argument("--staged-url")
    parser.add_argument("--expected-bytes", type=int)
    parser.add_argument("--raw-root", type=Path, default=Path("corpus/raw"))
    parser.add_argument("--normalized-output", type=Path, required=True)
    parser.add_argument("--manifest-output", type=Path, required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.workers < 1 or args.workers > 8:
        raise SystemExit("workers must be between 1 and 8")
    urls = list(args.url)
    if args.gap_manifest:
        source_manifest = yaml.safe_load(args.gap_manifest.read_text(encoding="utf-8"))
        urls.extend(
            str(gap["url"])
            for gap in source_manifest.get("gaps", [])
            if gap.get("url")
        )
    urls = sorted(set(urls))
    if not urls and args.staged_file is None:
        raise SystemExit("at least one --url or --staged-file is required")
    if (args.staged_file is None) != (args.staged_url is None):
        raise SystemExit("--staged-file and --staged-url must be used together")
    manifest = snapshot(
        source_id=args.source_id,
        urls=urls,
        raw_root=args.raw_root,
        normalized_output=args.normalized_output,
        manifest_output=args.manifest_output,
        staged_file=args.staged_file,
        staged_url=args.staged_url,
        expected_bytes=args.expected_bytes,
        workers=args.workers,
        input_manifest=args.gap_manifest,
    )
    print(
        f"{manifest['status']}: {manifest['source_id']} -> "
        f"{manifest['counts']['retrieved_assets']} assets, "  # type: ignore[index]
        f"{manifest['counts']['bytes']} bytes"  # type: ignore[index]
    )
    return 0 if manifest["status"] == "observable-complete" else 2


if __name__ == "__main__":
    raise SystemExit(main())
