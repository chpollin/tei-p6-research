"""Control-plane reconciliation: lock references, status agreement and run gaps.

Every tree is a synthetic registry, lock and manifest set built for one case. A
second registered source supplies a completed run that the example lock may
name without it counting as a run of the example source.
"""

from pathlib import Path, PureWindowsPath

import pytest
import yaml

from tools.corpus.validate_control_plane import validate

LOCK = "sources/locks/example.yaml"
RUN = "sources/manifests/2026-09-06-example-part.yaml"
OTHER_RUN = "sources/manifests/2026-09-06-other-source.yaml"
BLOCKING_GAP = {"code": "second-part-not-run", "status": "blocks-bounded-complete"}
NO_RUN_GAP = {"code": "no-retrieval-run-yet", "status": "blocks-bounded-complete"}


def write_yaml(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(value, sort_keys=False), encoding="utf-8")


def control_tree(
    root: Path,
    lock: dict,
    *,
    registry_status: str = "partial",
    run_status: str = "bounded-complete",
    lock_reference: str = LOCK,
    run_objects: list[dict] | None = None,
) -> Path:
    """Write the example source with ``lock`` beside a second registered source."""

    write_yaml(
        root / "sources" / "registry.yaml",
        {
            "schema_version": 1,
            "sources": [
                {
                    "source_id": "example-source",
                    "lock": lock_reference,
                    "retrieval_status": registry_status,
                },
                {
                    "source_id": "other-source",
                    "lock": "sources/locks/other.yaml",
                    "retrieval_status": "observable-complete",
                },
            ],
        },
    )
    write_yaml(
        root / LOCK,
        {"schema_version": 1, "source_id": "example-source", "retrieval_status": "partial", **lock},
    )
    write_yaml(
        root / "sources" / "locks" / "other.yaml",
        {
            "schema_version": 1,
            "source_id": "other-source",
            "retrieval_status": "observable-complete",
            "manifest": OTHER_RUN,
        },
    )
    write_yaml(
        root / RUN,
        {
            "schema_version": 1,
            "run_id": "2026-09-06-example-part",
            "source_id": "example-source",
            "status": run_status,
            "objects": run_objects or [],
            "gaps": [],
        },
    )
    write_yaml(
        root / OTHER_RUN,
        {
            "schema_version": 1,
            "run_id": "2026-09-06-other-source",
            "source_id": "other-source",
            "status": "observable-complete",
            "gaps": [],
        },
    )
    return root


def test_a_partial_family_may_name_a_completed_run_of_one_part(tmp_path) -> None:
    """A completed subrun leaves the family status and its blocking gap alone."""

    root = control_tree(tmp_path, {"manifests": [RUN], "gaps": [BLOCKING_GAP]})

    assert validate(root) == []


def test_registry_and_lock_must_agree_on_the_retrieval_status(tmp_path) -> None:
    root = control_tree(tmp_path, {"manifests": [RUN]}, registry_status="bounded-complete")

    assert validate(root) == [
        "example-source: registry retrieval_status 'bounded-complete' "
        f"differs from 'partial' in {LOCK}"
    ]


@pytest.mark.parametrize("run_status", ["partial", "bounded-complete", "observable-complete"])
@pytest.mark.parametrize("form", ["manifest", "manifests", "records"])
def test_no_retrieval_run_yet_is_contradicted_by_a_named_run(tmp_path, form, run_status) -> None:
    reference = {
        "manifest": RUN,
        "manifests": [RUN],
        "records": [{"kind": "part", "manifest": RUN}],
    }[form]
    root = control_tree(tmp_path, {form: reference, "gaps": [NO_RUN_GAP]}, run_status=run_status)

    assert validate(root) == [
        f"example-source: lock {LOCK} declares no-retrieval-run-yet but names recorded run(s): {RUN}"
    ]


@pytest.mark.parametrize(
    ("references", "run_status"),
    [([], "bounded-complete"), ([OTHER_RUN], "bounded-complete"), ([RUN], "planned")],
)
def test_no_retrieval_run_yet_stands_without_a_run_of_its_own_source(
    tmp_path, references, run_status
) -> None:
    root = control_tree(
        tmp_path, {"manifests": references, "gaps": [NO_RUN_GAP]}, run_status=run_status
    )

    assert validate(root) == []


def test_a_complete_family_cannot_keep_a_blocking_gap(tmp_path) -> None:
    root = control_tree(
        tmp_path,
        {
            "retrieval_status": "bounded-complete",
            "manifests": [RUN],
            "gaps": [BLOCKING_GAP, {"code": "note", "status": "open"}],
        },
        registry_status="bounded-complete",
    )

    assert validate(root) == [
        f"example-source: lock {LOCK} is bounded-complete but gap(s) block completion: "
        "second-part-not-run"
    ]


def test_a_missing_record_manifest_is_an_error(tmp_path) -> None:
    absent = "sources/manifests/2026-09-06-absent.yaml"
    root = control_tree(tmp_path, {"records": [{"kind": "part", "manifest": absent}]})

    assert validate(root) == [f"example-source: lock {LOCK} names missing manifest {absent}"]


@pytest.mark.parametrize(
    ("reference", "finding"),
    [
        ("sources/manifests/../../outside.yaml", "unsafe"),
        ("/sources/manifests/run.yaml", "unsafe"),
        ("C:/sources/manifests/run.yaml", "unsafe"),
        (str(PureWindowsPath("sources/manifests/run.yaml")), "unsafe"),
        ("corpus/normalized/run.yaml", "outside"),
        ("sources/manifests", "outside"),
    ],
)
def test_a_manifest_reference_outside_the_manifest_directory_is_an_error(
    tmp_path, reference, finding
) -> None:
    root = control_tree(tmp_path, {"manifests": [reference]})
    message = (
        f"unsafe repository reference {reference!r}"
        if finding == "unsafe"
        else f"reference {reference!r} lies outside sources/manifests/"
    )

    assert validate(root) == [f"example-source: lock {LOCK}: {message}"]


def test_a_malformed_lock_reference_is_an_error(tmp_path) -> None:
    root = control_tree(tmp_path, {"manifests": RUN})

    assert validate(root) == [
        f"example-source: lock {LOCK}: lock manifests must be a list of path strings"
    ]


@pytest.mark.parametrize(
    ("reference", "message"),
    [
        ("sources/locks/../../lock.yaml", "unsafe repository reference 'sources/locks/../../lock.yaml'"),
        ("corpus/example.yaml", "reference 'corpus/example.yaml' lies outside sources/locks/"),
    ],
)
def test_a_lock_reference_outside_the_lock_directory_is_an_error(
    tmp_path, reference, message
) -> None:
    root = control_tree(tmp_path, {"manifests": [RUN]}, lock_reference=reference)

    assert validate(root) == [f"example-source: {message}"]


def test_an_object_path_that_leaves_the_repository_is_an_error(tmp_path) -> None:
    root = control_tree(
        tmp_path,
        {"manifests": [RUN]},
        run_objects=[{"path": "../outside.json", "sha256": "0" * 64}],
    )

    assert validate(root) == [f"{RUN}: unsafe repository reference '../outside.json'"]
