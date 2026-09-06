"""Shared manifest skeleton, status rule, and CLI epilogue."""

import importlib
import json

import pytest

from tools.corpus.manifest import (
    build_manifest,
    read_jsonl,
    report_status,
    status_from,
    write_jsonl,
)

# The only completion states corpus/COMPLETENESS.md permits.
COMPLETION_STATES = {
    "planned",
    "partial",
    "observable-complete",
    "bounded-complete",
    "not-completable",
}

GAP = [{"code": "example-gap"}]

# Every collector whose manifest status comes from status_from.
COLLECTORS = [
    "asset_snapshot",
    "git_snapshot",
    "github_org_census",
    "github_org_git_snapshot",
    "github_snapshot",
    "sourceforge_snapshot",
    "web_census",
    "zip_inventory",
]


@pytest.mark.parametrize(
    ("gaps", "expected", "observed", "status"),
    [
        ([], None, None, "observable-complete"),
        ([], 5, 5, "observable-complete"),
        ([], 0, 0, "observable-complete"),
        ([], None, 3, "observable-complete"),
        ([], 5, 4, "partial"),
        ([], 5, 6, "partial"),
        ([], 5, None, "partial"),
        (GAP, None, None, "partial"),
        (GAP, 5, 5, "partial"),
    ],
)
def test_status_rule(gaps, expected, observed, status) -> None:
    result = status_from(gaps, expected=expected, observed=observed)
    assert result == status
    assert result in COMPLETION_STATES


def test_build_manifest_keeps_the_shared_key_order() -> None:
    manifest = build_manifest(
        run_id="2026-09-06-example",
        source_id="example-source",
        adapter="tools.corpus.example",
        started_at="2026-09-06T00:00:00Z",
        finished_at="2026-09-06T00:01:00Z",
        status="partial",
        requests=[{"url": "https://example.org/"}],
        objects=[{"kind": "example", "path": "corpus/normalized/example.json"}],
        counts={"objects": 1},
        gaps=[{"code": "example-gap"}],
        rights_exceptions=["Raw bodies stay local."],
        extra={"scope": {"boundary": "example"}},
    )
    assert list(manifest) == [
        "schema_version",
        "run_id",
        "source_id",
        "started_at",
        "finished_at",
        "status",
        "adapter",
        "requests",
        "objects",
        "counts",
        "scope",
        "gaps",
        "rights_exceptions",
    ]
    assert manifest["schema_version"] == 1
    assert manifest["adapter"] == {"name": "tools.corpus.example", "version": 2}


def test_build_manifest_omits_absent_optional_blocks() -> None:
    manifest = build_manifest(
        run_id="run",
        source_id="example-source",
        adapter="tools.corpus.example",
        started_at="2026-09-06T00:00:00Z",
        finished_at="2026-09-06T00:00:01Z",
        status="observable-complete",
        requests=[],
        counts={},
        gaps=[],
    )
    assert "rights_exceptions" not in manifest
    assert "objects" not in manifest
    assert manifest["gaps"] == []


@pytest.mark.parametrize("module_name", COLLECTORS)
def test_every_collector_stamps_adapter_version_2(module_name) -> None:
    """Each collector takes its adapter block from the shared builder, so the
    version it stamps is the builder's. Version 2 says the status of the
    manifest was derived from the gaps the run recorded."""

    module = importlib.import_module(f"tools.corpus.{module_name}")
    assert module.build_manifest is build_manifest
    manifest = build_manifest(
        run_id="run",
        source_id="example-source",
        adapter=f"tools.corpus.{module_name}",
        started_at="2026-09-06T00:00:00Z",
        finished_at="2026-09-06T00:00:01Z",
        status="partial",
        requests=[],
        counts={},
        gaps=[{"code": "example-gap"}],
    )
    assert manifest["adapter"] == {"name": f"tools.corpus.{module_name}", "version": 2}


@pytest.mark.parametrize(
    ("status", "code"),
    [("observable-complete", 0), ("partial", 2), ("bounded-complete", 2)],
)
def test_report_status_maps_status_to_exit_code(status, code, capsys) -> None:
    manifest = {"status": status, "source_id": "example-source"}
    assert report_status(manifest, "3 objects") == code
    assert capsys.readouterr().out == f"{status}: example-source -> 3 objects\n"


def test_jsonl_roundtrip(tmp_path) -> None:
    path = tmp_path / "rows.jsonl"
    rows = [{"b": 1, "a": "ä"}, {"a": "z"}]
    write_jsonl(path, rows)
    assert read_jsonl(path) == rows
    assert path.read_text(encoding="utf-8").splitlines()[0] == json.dumps(
        {"a": "ä", "b": 1}, ensure_ascii=False, sort_keys=True
    )


def test_read_jsonl_skips_blank_lines(tmp_path) -> None:
    path = tmp_path / "rows.jsonl"
    path.write_text('{"a": 1}\n\n{"a": 2}\n', encoding="utf-8")
    assert read_jsonl(path) == [{"a": 1}, {"a": 2}]
