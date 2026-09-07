"""Export admitted Guidelines XML without a mirror or network access.

Run ``python -m tools.export_guidelines --output PATH`` and add ``--check``
to verify an existing export. The export inventory is a navigation product;
original identities and bytes remain governed by the admission manifest.
"""

import argparse
import json
import os
import stat
import sys
import tempfile
from pathlib import Path, PurePosixPath

import yaml

from tools import ingest_git_blobs as ingest
from tools import ingest_guidelines as guidelines

INVENTORY = "guidelines-export.json"


def safe_destination(root: Path, relative: str) -> Path:
    """Reject traversal, symlinks and Windows reparse points before writing."""
    parts = PurePosixPath(relative).parts
    if not parts or "\\" in relative or ":" in relative or any(
        part in {"..", ".", "/"} for part in parts
    ) or PurePosixPath(relative).is_absolute():
        raise ValueError(f"unsafe export path: {relative}")
    target = root / relative
    for path in (*reversed(target.parents), target):
        try:
            info = path.lstat()
        except FileNotFoundError:
            continue
        if stat.S_ISLNK(info.st_mode) or getattr(info, "st_file_attributes", 0) & getattr(
            stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0
        ):
            raise ValueError(f"symlink or reparse point in export destination: {path}")
        if path != target and not stat.S_ISDIR(info.st_mode):
            raise ValueError(f"non-directory export ancestor: {path}")
    return target


def checked_payloads(root: Path) -> tuple[dict, dict[str, bytes]]:
    view = guidelines.build(root, check=True)
    payloads = guidelines.load_payloads(root, ingest.pinned_inventory(root), check=True)
    admission = yaml.safe_load((root / guidelines.MANIFEST).read_text(encoding="utf-8"))
    inventory = {
        "schema_version": 1,
        "kind": "export-inventory",
        "instruction_trust": "none",
        "release": view["release"],
        "commit": view["commit"],
        "boundary": view["boundary"],
        "admission_manifest": guidelines.MANIFEST,
        "admission_sha256": ingest.sha256((root / guidelines.MANIFEST).read_bytes()),
        "rights": admission["rights"],
        "files": [{"path": path, "bytes": len(payload),
                   "sha256": ingest.sha256(payload), "git_blob_id": ingest.blob_id(payload)}
                  for path, payload in sorted(payloads.items())],
        "not_exported_dependencies": [row for row in view["dependencies"]
                                      if row.get("target") not in payloads],
        "limits": ["XML source export only; no generated HTML, schemas or image assets.",
                   "Inventory is navigation outside the evidence chain and creates no anchors.",
                   *admission["known_limits"]],
    }
    return inventory, payloads


def write_new(path: Path, payload: bytes) -> None:
    """Publish a complete file atomically without replacing an existing file."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(dir=path.parent, prefix=".guidelines-", delete=False) as handle:
        temporary = Path(handle.name)
        handle.write(payload)
    try:
        os.link(temporary, path)
    finally:
        temporary.unlink()


def export(root: Path, output: Path, *, check: bool = False) -> dict:
    inventory, payloads = checked_payloads(root)
    output = output.absolute()
    products = {**payloads, INVENTORY: (json.dumps(inventory, ensure_ascii=False, indent=2) + "\n").encode()}
    for relative, payload in products.items():
        path = safe_destination(output, relative)
        if path.exists():
            if not path.is_file() or path.read_bytes() != payload:
                raise ValueError(f"incompatible existing export file: {path}")
        elif check:
            raise FileNotFoundError(f"missing export file: {path}")
    if not check:
        for relative, payload in products.items():
            path = safe_destination(output, relative)
            if not path.exists():
                write_new(path, payload)
    return inventory


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="Research repository root (default: current directory)")
    parser.add_argument("--output", type=Path, required=True, help="Export directory; upstream Git paths are preserved")
    parser.add_argument("--check", action="store_true", help="Verify every exported XML file and inventory without writing")
    args = parser.parse_args()
    try:
        inventory = export(args.root, args.output, check=args.check)
    except (OSError, ValueError) as exc:
        print(f"FEHLER: {exc}", file=sys.stderr)
        return 1
    print(f"OK: {len(inventory['files'])} XML sources {'verified' if args.check else 'exported'} in {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
