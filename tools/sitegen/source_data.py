"""Load and reconcile source-control records used by the public workbench."""

from __future__ import annotations

import json
from pathlib import Path, PurePosixPath
from typing import Any

import yaml

from tools.sitegen.markup import repository_link

_ALLOWED_OVERVIEW_PATHS = (
    ("sources", "locks"),
    ("sources", "manifests"),
    ("corpus", "normalized"),
    ("corpus", "projections"),
    ("10_markdown", "documents"),
)


def load_yaml(path: Path) -> dict[str, Any]:
    value = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"expected mapping in {path}")
    return value


def manifest_references(lock: dict[str, Any]) -> list[str]:
    references: list[str] = []
    single = lock.get("manifest")
    if isinstance(single, str):
        references.append(single)
    many = lock.get("manifests")
    if isinstance(many, list):
        references.extend(item for item in many if isinstance(item, str))
    records = lock.get("records")
    if isinstance(records, list):
        for record in records:
            if isinstance(record, dict) and isinstance(record.get("manifest"), str):
                references.append(record["manifest"])
    return list(dict.fromkeys(references))


def allowed_control_path(path: str) -> PurePosixPath:
    """Return the normalized path of a record the overview may link or read."""
    normalized = PurePosixPath(path.replace("\\", "/"))
    if normalized.is_absolute() or ".." in normalized.parts:
        raise ValueError(f"unsafe local overview link: {path}")
    bibliography = len(normalized.parts) == 2 and normalized.parts[0] == "references" and normalized.suffix == ".json"
    experiment_intake = normalized.parts == ("experiments", "identity_evidence", "intake.json")
    if not (bibliography or experiment_intake) and not any(
        normalized.parts[: len(prefix)] == prefix
        for prefix in _ALLOWED_OVERVIEW_PATHS
    ):
        raise ValueError(f"unexpected local overview link: {path}")
    return normalized


def control_href(path: str, base: str | None) -> str:
    """Resolve an allowed record locally or against the deployment base."""
    return repository_link(allowed_control_path(path).as_posix(), base)


def resolve_repo_file(root: Path, reference: str) -> Path:
    """Resolve an allowed overview input and require it to exist below root."""
    normalized = allowed_control_path(reference)
    resolved_root = root.resolve()
    candidate = (resolved_root / Path(*normalized.parts)).resolve()
    if not candidate.is_relative_to(resolved_root) or not candidate.is_file():
        raise FileNotFoundError(f"missing or unsafe overview input: {reference}")
    if normalized.parts[0] == "references":
        records = json.loads(candidate.read_text(encoding="utf-8"))
        if not isinstance(records, list) or not records or any(
            not isinstance(record, dict) or not all(isinstance(record.get(key), str) and record[key] for key in ("id", "type"))
            for record in records
        ):
            raise ValueError(f"expected CSL JSON bibliography: {reference}")
    return candidate


def load_source_records(root: Path) -> list[dict[str, Any]]:
    """Load registry rows with their reconciled lock and manifest records."""
    registry = load_yaml(root / "sources" / "registry.yaml")
    sources = registry.get("sources")
    if not isinstance(sources, list):
        raise ValueError("sources/registry.yaml has no sources list")

    loaded: list[dict[str, Any]] = []
    seen_source_ids: set[str] = set()
    for source in sources:
        if not isinstance(source, dict):
            continue
        source_id = str(source.get("source_id", ""))
        if not source_id or source_id in seen_source_ids:
            raise ValueError(f"missing or duplicate source_id: {source_id!r}")
        seen_source_ids.add(source_id)

        lock_ref = source.get("lock")
        if not isinstance(lock_ref, str):
            raise ValueError(f"source {source.get('source_id')} has no lock")
        lock = load_yaml(resolve_repo_file(root, lock_ref))
        if lock.get("source_id") != source_id:
            raise ValueError(f"source_id mismatch between registry and {lock_ref}")

        registry_status = source.get("retrieval_status")
        lock_status = lock.get("retrieval_status")
        if registry_status != lock_status:
            raise ValueError(f"retrieval_status mismatch for {source_id}")

        manifest_refs = manifest_references(lock)
        missing_manifests = [
            reference
            for reference in manifest_refs
            if not (root / reference).resolve().is_file()
        ]
        if missing_manifests:
            raise FileNotFoundError(
                f"missing manifest(s) for {source_id}: {', '.join(missing_manifests)}"
            )
        manifests = [
            load_yaml(resolve_repo_file(root, reference)) for reference in manifest_refs
        ]
        loaded.append(
            {
                "source": source,
                "source_id": source_id,
                "lock_ref": lock_ref,
                "lock": lock,
                "status": str(lock_status),
                "manifest_refs": manifest_refs,
                "manifests": manifests,
            }
        )
    return loaded
