"""Shared deterministic file and manifest helpers for corpus collectors."""

from __future__ import annotations

import hashlib
import json
import tempfile
from pathlib import Path
from typing import Any

import yaml


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _atomic_write(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(dir=path.parent, delete=False) as handle:
        handle.write(data)
        temporary = Path(handle.name)
    temporary.replace(path)


def write_json(path: Path, value: Any) -> None:
    payload = json.dumps(
        value,
        ensure_ascii=False,
        indent=2,
        sort_keys=True,
    ).encode("utf-8") + b"\n"
    _atomic_write(path, payload)


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    payload = b"".join(
        json.dumps(row, ensure_ascii=False, sort_keys=True).encode("utf-8") + b"\n"
        for row in rows
    )
    _atomic_write(path, payload)


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    return [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line
    ]


def write_yaml(path: Path, value: Any) -> None:
    payload = yaml.safe_dump(
        value,
        allow_unicode=True,
        sort_keys=False,
    ).encode("utf-8")
    _atomic_write(path, payload)


def status_from(
    gaps: list[dict[str, Any]],
    *,
    expected: int | None = None,
    observed: int | None = None,
) -> str:
    """Return the run status from the recorded gaps and the count reconciliation.

    This is the single completion rule of the acquisition layer, stated in
    ``knowledge/data.md`` (Completion vocabulary): a run is ``observable-complete`` only when it
    recorded no gap and, where the boundary reports an expected count, acquired
    exactly that many objects. Every other outcome is ``partial``. Wider states
    (``planned``, ``bounded-complete``, ``not-completable``) describe a source
    family or a search protocol and are set in registry and lock files, never by
    a collector run.
    """

    if gaps:
        return "partial"
    if expected is not None and observed != expected:
        return "partial"
    return "observable-complete"


def build_manifest(
    *,
    run_id: str,
    source_id: str,
    adapter: str,
    started_at: str,
    finished_at: str,
    status: str,
    requests: Any,
    counts: dict[str, Any],
    gaps: list[dict[str, Any]],
    objects: list[dict[str, Any]] | None = None,
    rights_exceptions: list[str] | None = None,
    extra: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Assemble the run-manifest skeleton every collector shares.

    ``objects`` stays absent for an adapter that writes no normalized object of
    its own. ``extra`` carries adapter-specific blocks (scope, refs,
    repositories, link inventories) and is merged after ``counts`` so the shared
    keys keep one order across adapters.
    """

    manifest: dict[str, Any] = {
        "schema_version": 1,
        "run_id": run_id,
        "source_id": source_id,
        "started_at": started_at,
        "finished_at": finished_at,
        "status": status,
        # Adapter version 2 marks a manifest whose status was derived from the
        # gaps the run recorded. Version 1 manifests carry a status that was
        # partly assigned rather than derived.
        "adapter": {"name": adapter, "version": 2},
        "requests": requests,
    }
    if objects is not None:
        manifest["objects"] = objects
    manifest["counts"] = counts
    manifest.update(extra or {})
    manifest["gaps"] = gaps
    if rights_exceptions:
        manifest["rights_exceptions"] = rights_exceptions
    return manifest


def report_status(manifest: dict[str, Any], detail: str) -> int:
    """Print the collector result line and return the shared process exit code."""

    print(f"{manifest['status']}: {manifest['source_id']} -> {detail}")
    return 0 if manifest["status"] == "observable-complete" else 2
