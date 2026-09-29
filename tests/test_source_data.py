"""Workbench source records: shared lock references, boundaries and reconciliation.

The fixture trees are synthetic control records written for these cases; the
repository test reads the tracked registry, locks and manifests.
"""

from pathlib import Path, PureWindowsPath

import pytest
import yaml

from tools.corpus.manifest import lock_manifest_references
from tools.sitegen.source_data import load_source_records

REPO = Path(__file__).parents[1]
MANIFEST = "sources/manifests/2026-09-06-example.yaml"


def write_yaml(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(value, sort_keys=False), encoding="utf-8")


def source_tree(root: Path, lock: dict, *, registry_status: str = "partial") -> Path:
    """Write one registered source whose lock adds ``lock`` to its identity."""

    write_yaml(
        root / "sources" / "registry.yaml",
        {
            "schema_version": 1,
            "sources": [
                {
                    "source_id": "example-source",
                    "lock": "sources/locks/example.yaml",
                    "retrieval_status": registry_status,
                }
            ],
        },
    )
    write_yaml(
        root / "sources" / "locks" / "example.yaml",
        {"schema_version": 1, "source_id": "example-source", "retrieval_status": "partial", **lock},
    )
    write_yaml(
        root / MANIFEST,
        {
            "schema_version": 1,
            "run_id": "2026-09-06-example",
            "source_id": "example-source",
            "status": "bounded-complete",
            "gaps": [],
        },
    )
    return root


def test_lock_references_cover_all_three_forms_once() -> None:
    lock = {
        "manifest": "sources/manifests/a.yaml",
        "manifests": ["sources/manifests/b.yaml", "sources/manifests/a.yaml"],
        "records": [
            {"kind": "sample", "manifest": "sources/manifests/c.yaml"},
            {"kind": "reading-without-run"},
        ],
    }

    assert lock_manifest_references(lock) == [
        "sources/manifests/a.yaml",
        "sources/manifests/b.yaml",
        "sources/manifests/c.yaml",
    ]


@pytest.mark.parametrize(
    "lock",
    [
        {"manifest": ["sources/manifests/a.yaml"]},
        {"manifests": "sources/manifests/a.yaml"},
        {"manifests": [None]},
        {"records": {"manifest": "sources/manifests/a.yaml"}},
        {"records": ["sources/manifests/a.yaml"]},
        {"records": [{"manifest": 3}]},
    ],
)
def test_a_malformed_lock_reference_is_rejected_rather_than_skipped(lock) -> None:
    with pytest.raises(ValueError, match="lock"):
        lock_manifest_references(lock)


def test_repository_tei_l_record_preserves_coverage_pilots_and_completed_month() -> None:
    loaded = {record["source_id"]: record for record in load_source_records(REPO)}
    tei_l = loaded["tei-l-archive"]

    assert tei_l["status"] == tei_l["source"]["retrieval_status"] == "partial"
    assert tei_l["manifest_refs"] == [
        "sources/manifests/2026-09-06-tei-l-psu.yaml",
        "sources/manifests/2026-09-06-tei-l-wayback-coverage.yaml",
        "sources/manifests/2026-09-11-tei-l-wayback-pilot.yaml",
        "sources/manifests/2026-09-11-tei-l-wayback-pilot-resumed.yaml",
        "sources/manifests/2026-09-11-tei-l-wayback-0001-v2.yaml",
        "sources/manifests/2026-09-11-tei-l-wayback-0001-v2-resumed.yaml",
    ]
    assert [manifest["status"] for manifest in tei_l["manifests"]] == [
        "bounded-complete",
        "bounded-complete",
        "partial",
        "partial",
        "bounded-complete",
        "bounded-complete",
    ]
    assert "no-retrieval-run-yet" not in {gap["code"] for gap in tei_l["lock"]["gaps"]}


def test_a_record_manifest_is_loaded(tmp_path) -> None:
    root = source_tree(tmp_path, {"records": [{"kind": "sample", "manifest": MANIFEST}]})

    [record] = load_source_records(root)

    assert record["manifest_refs"] == [MANIFEST]
    assert record["manifests"][0]["run_id"] == "2026-09-06-example"


def test_a_status_disagreement_between_registry_and_lock_is_rejected(tmp_path) -> None:
    root = source_tree(tmp_path, {"manifests": [MANIFEST]}, registry_status="planned")

    with pytest.raises(ValueError, match="retrieval_status mismatch for example-source"):
        load_source_records(root)


def test_a_missing_record_manifest_is_rejected(tmp_path) -> None:
    root = source_tree(
        tmp_path, {"records": [{"manifest": "sources/manifests/2026-09-06-absent.yaml"}]}
    )

    with pytest.raises(FileNotFoundError, match="2026-09-06-absent"):
        load_source_records(root)


@pytest.mark.parametrize(
    ("reference", "message"),
    [
        ("sources/manifests/../locks/example.yaml", "unsafe repository reference"),
        ("/sources/manifests/run.yaml", "unsafe repository reference"),
        ("C:/sources/manifests/run.yaml", "unsafe repository reference"),
        (str(PureWindowsPath("sources/manifests/run.yaml")), "unsafe repository reference"),
        ("corpus/normalized/run.yaml", "lies outside sources/manifests/"),
    ],
)
def test_a_manifest_reference_outside_the_manifest_directory_is_rejected(
    tmp_path, reference, message
) -> None:
    root = source_tree(tmp_path, {"manifests": [reference]})

    with pytest.raises(ValueError, match=message):
        load_source_records(root)
