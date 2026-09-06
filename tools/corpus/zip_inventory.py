"""Create a deterministic inventory of a ZIP release artifact."""

from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path
from zipfile import BadZipFile, ZipFile

from tools.corpus.http_store import utc_now
from tools.corpus.manifest import (
    build_manifest,
    report_status,
    sha256_file,
    status_from,
    write_json,
    write_yaml,
)


def inventory(
    *,
    source_id: str,
    archive: Path,
    normalized_output: Path,
    manifest_output: Path,
) -> dict[str, object]:
    started_at = utc_now()
    entries: list[dict[str, object]] = []
    gaps: list[dict[str, object]] = []
    # A truncated or damaged archive still produces a manifest: the run records
    # what it could read and names the failure as a gap.
    try:
        with ZipFile(archive) as release:
            bad_member = release.testzip()
            for item in release.infolist():
                entries.append(
                    {
                        "path": item.filename,
                        "directory": item.is_dir(),
                        "uncompressed_bytes": item.file_size,
                        "compressed_bytes": item.compress_size,
                        "crc32": f"{item.CRC:08x}",
                    }
                )
    except BadZipFile as error:
        bad_member = None
        gaps.append({"code": "archive-unreadable", "detail": str(error)})
    if bad_member is not None:
        gaps.append({"code": "zip-crc-failure", "path": bad_member})
    entries.sort(key=lambda row: str(row["path"]))
    suffixes = Counter(
        Path(str(row["path"])).suffix.lower() or "[none]"
        for row in entries
        if not row["directory"]
    )
    archive_sha256 = sha256_file(archive)
    normalized = {
        "schema_version": 1,
        "source_id": source_id,
        "archive_sha256": archive_sha256,
        "entries": entries,
    }
    write_json(normalized_output, normalized)
    manifest = build_manifest(
        run_id=manifest_output.stem,
        source_id=source_id,
        adapter="tools.corpus.zip_inventory",
        started_at=started_at,
        finished_at=utc_now(),
        status=status_from(gaps),
        requests=[{"archive": archive.as_posix(), "sha256": archive_sha256}],
        objects=[
            {
                "kind": "zip-member-inventory",
                "path": normalized_output.as_posix(),
                "sha256": sha256_file(normalized_output),
            }
        ],
        counts={
            "members": len(entries),
            "files": sum(not bool(row["directory"]) for row in entries),
            "directories": sum(bool(row["directory"]) for row in entries),
            "uncompressed_bytes": sum(int(row["uncompressed_bytes"]) for row in entries),
            "suffixes": dict(sorted(suffixes.items())),
            "gaps": len(gaps),
        },
        gaps=gaps,
    )
    write_yaml(manifest_output, manifest)
    return manifest


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-id", required=True)
    parser.add_argument("--archive", type=Path, required=True)
    parser.add_argument("--normalized-output", type=Path, required=True)
    parser.add_argument("--manifest-output", type=Path, required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    manifest = inventory(
        source_id=args.source_id,
        archive=args.archive,
        normalized_output=args.normalized_output,
        manifest_output=args.manifest_output,
    )
    return report_status(manifest, f"{manifest['counts']['files']} files")


if __name__ == "__main__":
    raise SystemExit(main())
