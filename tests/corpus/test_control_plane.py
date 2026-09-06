"""Control-plane validation: the live tree and each error branch on fixtures."""

import hashlib
from pathlib import Path

import pytest
import yaml

from tools.corpus.validate_control_plane import validate


def write_yaml(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(value, sort_keys=False), encoding="utf-8")


def control_plane(
    root: Path,
    *,
    sources: list[dict] | None = None,
    locks: dict[str, dict] | None = None,
    manifests: dict[str, dict] | None = None,
) -> Path:
    """Build the smallest consistent registry/lock/manifest tree, then vary it."""

    default_lock = {"schema_version": 1, "source_id": "example-source", "manifests": []}
    default_manifest = {
        "schema_version": 1,
        "run_id": "2026-09-06-example",
        "source_id": "example-source",
        "status": "observable-complete",
        "objects": [],
        "gaps": [],
    }
    write_yaml(
        root / "sources" / "registry.yaml",
        {
            "schema_version": 1,
            "sources": sources
            if sources is not None
            else [
                {
                    "source_id": "example-source",
                    "aliases": ["example-alias"],
                    "lock": "sources/locks/example.yaml",
                }
            ],
        },
    )
    for name, lock in (locks if locks is not None else {"example": default_lock}).items():
        write_yaml(root / "sources" / "locks" / f"{name}.yaml", lock)
    manifest_dir = root / "sources" / "manifests"
    manifest_dir.mkdir(parents=True, exist_ok=True)
    for name, manifest in (
        manifests if manifests is not None else {"2026-09-06-example": default_manifest}
    ).items():
        write_yaml(manifest_dir / f"{name}.yaml", manifest)
    return root


def test_repository_source_control_plane_is_consistent() -> None:
    assert validate(Path(__file__).resolve().parents[2]) == []


def test_a_consistent_fixture_tree_passes(tmp_path) -> None:
    assert validate(control_plane(tmp_path)) == []


def test_a_duplicate_registry_source_id_is_an_error(tmp_path) -> None:
    entry = {"source_id": "example-source", "lock": "sources/locks/example.yaml"}
    root = control_plane(tmp_path, sources=[entry, dict(entry)])

    assert validate(root) == ["duplicate or empty registry source_id: 'example-source'"]


def test_a_registry_entry_without_a_lock_is_an_error(tmp_path) -> None:
    root = control_plane(tmp_path, sources=[{"source_id": "example-source"}])

    assert validate(root) == ["example-source: registry entry has no lock"]


def test_a_missing_lock_file_is_an_error(tmp_path) -> None:
    root = control_plane(tmp_path, locks={"other": {"source_id": "example-source"}})

    assert validate(root) == ["example-source: missing lock sources/locks/example.yaml"]


def test_a_lock_naming_another_source_is_an_error(tmp_path) -> None:
    root = control_plane(tmp_path, locks={"example": {"source_id": "other-source"}})

    assert validate(root) == [
        "example-source: lock source_id is 'other-source' in sources/locks/example.yaml"
    ]


@pytest.mark.parametrize("key", ["manifest", "manifests"])
def test_a_lock_naming_a_missing_manifest_is_an_error(tmp_path, key) -> None:
    reference = "sources/manifests/2026-09-06-absent.yaml"
    root = control_plane(
        tmp_path,
        locks={
            "example": {
                "source_id": "example-source",
                key: reference if key == "manifest" else [reference],
            }
        },
    )

    assert validate(root) == [
        f"example-source: lock sources/locks/example.yaml names missing manifest {reference}"
    ]


def test_a_lock_naming_an_existing_manifest_passes(tmp_path) -> None:
    root = control_plane(
        tmp_path,
        locks={
            "example": {
                "source_id": "example-source",
                "manifests": ["sources/manifests/2026-09-06-example.yaml"],
            }
        },
    )

    assert validate(root) == []


def test_a_manifest_without_a_source_id_is_an_error(tmp_path) -> None:
    root = control_plane(
        tmp_path,
        manifests={"2026-09-06-example": {"schema_version": 1, "status": "partial"}},
    )

    assert validate(root) == [
        "sources/manifests/2026-09-06-example.yaml: manifest has no source_id"
    ]


def test_a_planning_census_needs_no_source_id(tmp_path) -> None:
    root = control_plane(
        tmp_path,
        manifests={
            "planning-census": {
                "schema_version": 1,
                "manifest_kind": "planning-census",
                "status": "planned",
            }
        },
    )

    assert validate(root) == []


def test_an_alias_is_not_a_manifest_source_id(tmp_path) -> None:
    root = control_plane(
        tmp_path,
        manifests={
            "2026-09-06-example": {"schema_version": 1, "source_id": "example-alias"}
        },
    )

    assert validate(root) == [
        "sources/manifests/2026-09-06-example.yaml: 'example-alias' is a registry alias; "
        "a manifest names the canonical source_id"
    ]


def test_an_unknown_manifest_source_id_is_an_error(tmp_path) -> None:
    root = control_plane(
        tmp_path,
        manifests={"2026-09-06-example": {"schema_version": 1, "source_id": "not-registered"}},
    )

    assert validate(root) == [
        "sources/manifests/2026-09-06-example.yaml: unknown source_id 'not-registered'"
    ]


def test_a_manifest_object_without_a_path_is_an_error(tmp_path) -> None:
    root = control_plane(
        tmp_path,
        manifests={
            "2026-09-06-example": {
                "schema_version": 1,
                "source_id": "example-source",
                "objects": [{"sha256": "0" * 64}],
            }
        },
    )

    assert validate(root) == ["sources/manifests/2026-09-06-example.yaml: object has no path"]


def test_a_missing_object_is_an_error(tmp_path) -> None:
    root = control_plane(
        tmp_path,
        manifests={
            "2026-09-06-example": {
                "schema_version": 1,
                "source_id": "example-source",
                "objects": [{"path": "corpus/normalized/absent.json", "sha256": "0" * 64}],
            }
        },
    )

    assert validate(root) == [
        "sources/manifests/2026-09-06-example.yaml: missing object corpus/normalized/absent.json"
    ]


def test_an_object_hash_mismatch_is_an_error(tmp_path) -> None:
    root = control_plane(
        tmp_path,
        manifests={
            "2026-09-06-example": {
                "schema_version": 1,
                "source_id": "example-source",
                "objects": [{"path": "corpus/normalized/object.json", "sha256": "0" * 64}],
            }
        },
    )
    object_path = root / "corpus" / "normalized" / "object.json"
    object_path.parent.mkdir(parents=True)
    object_path.write_bytes(b"{}\n")

    assert validate(root) == [
        "sources/manifests/2026-09-06-example.yaml: SHA-256 mismatch for corpus/normalized/object.json"
    ]


def test_a_matching_object_hash_passes(tmp_path) -> None:
    payload = b"{}\n"
    root = control_plane(
        tmp_path,
        manifests={
            "2026-09-06-example": {
                "schema_version": 1,
                "source_id": "example-source",
                "objects": [
                    {
                        "path": "corpus/normalized/object.json",
                        "sha256": hashlib.sha256(payload).hexdigest(),
                    }
                ],
            }
        },
    )
    object_path = root / "corpus" / "normalized" / "object.json"
    object_path.parent.mkdir(parents=True)
    object_path.write_bytes(payload)

    assert validate(root) == []
