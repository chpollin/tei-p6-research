"""Validate source registry, locks, manifests, and normalized object hashes."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

import yaml

from tools.corpus.manifest import sha256_file


def load_yaml(path: Path) -> dict[str, Any]:
    value = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"expected mapping in {path}")
    return value


def validate(root: Path) -> list[str]:
    errors: list[str] = []
    registry_path = root / "sources" / "registry.yaml"
    registry = load_yaml(registry_path)
    source_ids: set[str] = set()
    aliases: set[str] = set()
    for source in registry.get("sources", []):
        source_id = str(source.get("source_id", ""))
        if not source_id or source_id in source_ids:
            errors.append(f"duplicate or empty registry source_id: {source_id!r}")
            continue
        source_ids.add(source_id)
        aliases.update(str(alias) for alias in source.get("aliases", []))
        lock_value = source.get("lock")
        if not lock_value:
            errors.append(f"{source_id}: registry entry has no lock")
            continue
        lock_path = root / str(lock_value)
        if not lock_path.exists():
            errors.append(f"{source_id}: missing lock {lock_value}")
            continue
        lock = load_yaml(lock_path)
        if lock.get("source_id") != source_id:
            errors.append(
                f"{source_id}: lock source_id is {lock.get('source_id')!r} in {lock_value}"
            )

    known_ids = source_ids | aliases
    for manifest_path in sorted((root / "sources" / "manifests").rglob("*.yaml")):
        manifest = load_yaml(manifest_path)
        source_id = manifest.get("source_id")
        if source_id is None:
            continue
        if str(source_id) not in known_ids:
            errors.append(f"{manifest_path.relative_to(root)}: unknown source_id {source_id!r}")
        for item in manifest.get("objects", []) or []:
            object_path_value = item.get("path")
            expected_hash = item.get("sha256")
            if not object_path_value:
                errors.append(f"{manifest_path.relative_to(root)}: object has no path")
                continue
            object_path = root / str(object_path_value)
            if not object_path.exists():
                errors.append(
                    f"{manifest_path.relative_to(root)}: missing object {object_path_value}"
                )
            elif expected_hash and sha256_file(object_path) != expected_hash:
                errors.append(
                    f"{manifest_path.relative_to(root)}: SHA-256 mismatch for {object_path_value}"
                )
    return errors


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", type=Path, default=Path("."))
    return parser.parse_args()


def main() -> int:
    errors = validate(parse_args().root.resolve())
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        print(f"FAILED: {len(errors)} control-plane error(s)")
        return 1
    print("OK: source control plane is internally consistent")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
