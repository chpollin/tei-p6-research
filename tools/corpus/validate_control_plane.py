"""Validate source registry, locks, manifests, and normalized object hashes.

The check reconciles control records with each other, never with the network:
registry and lock identity and ``retrieval_status``, every run manifest a lock
names through ``manifest``, ``manifests`` or ``records[].manifest``, manifest
source IDs, and the path and SHA-256 of every declared object. Every reference
must stay inside the repository, locks below ``sources/locks/`` and run
manifests below ``sources/manifests/``.

A lock status stays a judgment about the whole family. A completed run never
raises it, so runs are compared with a lock only where the lock makes an
explicit claim: a family-wide ``no-retrieval-run-yet`` gap contradicted by a
named run of the same source, and a complete lock that still carries a gap
whose status blocks completion.

Usage:
    python -m tools.corpus.validate_control_plane .
"""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

import yaml

from tools.corpus.manifest import (
    LOCK_DIRECTORY,
    MANIFEST_DIRECTORY,
    lock_manifest_references,
    repository_path,
    sha256_file,
)

# Manifest kinds that record intent rather than a source run and therefore
# carry no source_id.
NON_RUN_MANIFEST_KINDS = {"planning-census"}

# A run with one of these statuses shows that retrieval began
# (knowledge/data.md, Completion states); only ``planned`` does not.
RETRIEVAL_RUN_STATUSES = frozenset(
    {"partial", "observable-complete", "bounded-complete", "not-completable"}
)
COMPLETE_STATUSES = frozenset({"observable-complete", "bounded-complete"})
NO_RUN_GAP = "no-retrieval-run-yet"


def load_yaml(path: Path) -> dict[str, Any]:
    value = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"expected mapping in {path}")
    return value


def lock_errors(root: Path, source_id: str, lock_value: str, lock: dict[str, Any]) -> list[str]:
    """Return the reference, gap and status contradictions of one lock.

    Only runs of the lock's own source can contradict ``no-retrieval-run-yet``,
    because a lock may also name a run of another source it reads from. No run
    status is compared with the lock status: a completed part leaves the family
    as the lock judges it.
    """

    label = f"{source_id}: lock {lock_value}"
    try:
        references = lock_manifest_references(lock)
    except ValueError as error:
        return [f"{label}: {error}"]
    errors: list[str] = []
    runs: list[tuple[str, dict[str, Any]]] = []
    for reference in references:
        try:
            manifest_path = repository_path(root, reference, prefix=MANIFEST_DIRECTORY)
        except ValueError as error:
            errors.append(f"{label}: {error}")
            continue
        if not manifest_path.is_file():
            errors.append(f"{label} names missing manifest {reference}")
            continue
        runs.append((reference, load_yaml(manifest_path)))

    gaps = [gap for gap in lock.get("gaps") or [] if isinstance(gap, dict)]
    if any(gap.get("code") == NO_RUN_GAP for gap in gaps):
        recorded = [
            reference
            for reference, manifest in runs
            if manifest.get("source_id") == source_id
            and manifest.get("status") in RETRIEVAL_RUN_STATUSES
        ]
        if recorded:
            errors.append(
                f"{label} declares {NO_RUN_GAP} but names recorded run(s): {', '.join(recorded)}"
            )
    status = lock.get("retrieval_status")
    if status in COMPLETE_STATUSES:
        blocking = [
            str(gap.get("code"))
            for gap in gaps
            if str(gap.get("status", "")).startswith("blocks-")
        ]
        if blocking:
            errors.append(f"{label} is {status} but gap(s) block completion: {', '.join(blocking)}")
    return errors


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
        try:
            lock_path = repository_path(root, lock_value, prefix=LOCK_DIRECTORY)
        except ValueError as error:
            errors.append(f"{source_id}: {error}")
            continue
        if not lock_path.is_file():
            errors.append(f"{source_id}: missing lock {lock_value}")
            continue
        lock = load_yaml(lock_path)
        if lock.get("source_id") != source_id:
            errors.append(
                f"{source_id}: lock source_id is {lock.get('source_id')!r} in {lock_value}"
            )
        if lock.get("retrieval_status") != source.get("retrieval_status"):
            errors.append(
                f"{source_id}: registry retrieval_status {source.get('retrieval_status')!r} "
                f"differs from {lock.get('retrieval_status')!r} in {lock_value}"
            )
        errors.extend(lock_errors(root, source_id, str(lock_value), lock))

    for manifest_path in sorted((root / "sources" / "manifests").rglob("*.yaml")):
        manifest = load_yaml(manifest_path)
        # POSIX form keeps the message identical on every platform.
        relative = manifest_path.relative_to(root).as_posix()
        source_id = manifest.get("source_id")
        if source_id is None:
            if str(manifest.get("manifest_kind")) not in NON_RUN_MANIFEST_KINDS:
                errors.append(f"{relative}: manifest has no source_id")
        elif str(source_id) in aliases and str(source_id) not in source_ids:
            errors.append(
                f"{relative}: {str(source_id)!r} is a registry alias; "
                "a manifest names the canonical source_id"
            )
        elif str(source_id) not in source_ids:
            errors.append(f"{relative}: unknown source_id {source_id!r}")
        for item in manifest.get("objects", []) or []:
            object_path_value = item.get("path")
            expected_hash = item.get("sha256")
            if not object_path_value:
                errors.append(f"{relative}: object has no path")
                continue
            try:
                object_path = repository_path(root, object_path_value)
            except ValueError as error:
                errors.append(f"{relative}: {error}")
                continue
            if not object_path.is_file():
                errors.append(f"{relative}: missing object {object_path_value}")
            elif expected_hash and sha256_file(object_path) != expected_hash:
                errors.append(f"{relative}: SHA-256 mismatch for {object_path_value}")
    return errors


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", type=Path, default=Path())
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
