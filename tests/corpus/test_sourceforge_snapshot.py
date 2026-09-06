"""SourceForge tracker snapshot: enumeration, reconciliation, resume, CLI."""

import json

import pytest
import yaml

from tools.corpus import sourceforge_snapshot
from tools.corpus.sourceforge_snapshot import (
    enumerate_tracker,
    paged_url,
    public_ticket_metadata,
    snapshot,
)

PROJECT_URL = "https://sourceforge.example/rest/p/tei"
BUGS_URL = "https://sourceforge.example/rest/p/tei/bugs"


def serve_project(fake_http) -> None:
    fake_http.serve_json(
        PROJECT_URL,
        {"shortname": "tei", "name": "TEI", "status": "active", "moved_to_url": None},
    )


def serve_pages(fake_http, base: str, pages: list[dict]) -> None:
    for number, payload in enumerate(pages):
        fake_http.serve_json(paged_url(base, number), payload)


def canned_ticket(monkeypatch) -> list[int]:
    """Replace ticket retrieval; enumeration and reconciliation are under test."""

    fetched: list[int] = []

    def fake_fetch_ticket(base, tracker, ticket_num, raw_root, delay_seconds, source_id):
        fetched.append(ticket_num)
        return {
            "record": {
                "source_id": source_id,
                "tracker": tracker,
                "ticket_num": ticket_num,
                "comment_count": 0,
                "raw_responses": [{"sha256": f"raw-{ticket_num}"}],
            },
            "detail_response": {"status": 200},
            "thread_responses": [],
        }

    monkeypatch.setattr(sourceforge_snapshot, "fetch_ticket", fake_fetch_ticket)
    return fetched


def run_snapshot(tmp_path, **overrides) -> dict:
    arguments = {
        "source_id": "tei-legacy-sourceforge",
        "project_url": PROJECT_URL,
        "trackers": {"bugs": BUGS_URL},
        "workers": 1,
        "raw_root": tmp_path / "raw",
        "normalized_output": tmp_path / "normalized.jsonl",
        "manifest_output": tmp_path / "manifest.yaml",
    }
    return snapshot(**(arguments | overrides))


def test_public_ticket_metadata_carries_the_given_source_id() -> None:
    record = public_ticket_metadata({"ticket_num": 7}, "bugs", "other-sourceforge-project")
    assert record["source_id"] == "other-sourceforge-project"


def test_public_ticket_metadata_excludes_description() -> None:
    record = public_ticket_metadata(
        {
            "ticket_num": 7,
            "description": "raw prose",
            "summary": "Short title",
            "discussion_thread": {"_id": "thread-1"},
        },
        "bugs",
        "tei-legacy-sourceforge",
    )
    assert record["body_present_in_raw"] is True
    assert "description" not in record


def test_pagination_url_is_canonical() -> None:
    assert paged_url("https://sourceforge.net/rest/p/tei/bugs/", 2) == (
        "https://sourceforge.net/rest/p/tei/bugs?limit=100&page=2"
    )


def test_enumeration_deduplicates_overlapping_pages(tmp_path, fake_http) -> None:
    serve_pages(
        fake_http,
        BUGS_URL,
        [
            {"count": 5, "tickets": [{"ticket_num": 1}, {"ticket_num": 2}, {"ticket_num": 3}]},
            {"count": 5, "tickets": [{"ticket_num": 3}, {"ticket_num": 4}]},
            {"count": 5, "tickets": []},
        ],
    )
    store = sourceforge_snapshot.HttpStore(tmp_path / "raw")

    numbers, reported, responses = enumerate_tracker(store, BUGS_URL)

    assert numbers == [1, 2, 3, 4]
    assert reported == 5
    assert len(responses) == 3


def test_overlapping_pages_produce_a_ticket_count_mismatch(
    tmp_path, fake_http, monkeypatch
) -> None:
    serve_project(fake_http)
    serve_pages(
        fake_http,
        BUGS_URL,
        [
            {"count": 5, "tickets": [{"ticket_num": 1}, {"ticket_num": 2}, {"ticket_num": 3}]},
            {"count": 5, "tickets": [{"ticket_num": 3}, {"ticket_num": 4}]},
            {"count": 5, "tickets": []},
        ],
    )
    fetched = canned_ticket(monkeypatch)

    manifest = run_snapshot(tmp_path)

    assert sorted(fetched) == [1, 2, 3, 4]
    assert manifest["status"] == "partial"
    assert {"code": "ticket-count-mismatch", "expected": 5, "observed": 4} in manifest["gaps"]
    assert manifest["counts"]["tickets_reported_by_tracker"] == {"bugs": 5}
    assert manifest["counts"]["tickets_expected"] == 5
    assert manifest["counts"]["tickets"] == 4


def test_reconciled_run_is_observable_complete(tmp_path, fake_http, monkeypatch) -> None:
    serve_project(fake_http)
    serve_pages(
        fake_http,
        BUGS_URL,
        [{"count": 2, "tickets": [{"ticket_num": 1}, {"ticket_num": 2}]}],
    )
    canned_ticket(monkeypatch)

    manifest = run_snapshot(tmp_path)

    assert manifest["gaps"] == []
    assert manifest["status"] == "observable-complete"
    assert manifest["source_id"] == "tei-legacy-sourceforge"
    written = yaml.safe_load((tmp_path / "manifest.yaml").read_text(encoding="utf-8"))
    assert written["status"] == "observable-complete"
    assert written["requests"]["project_response"]["status"] == 200


def test_a_tracker_without_a_reported_count_stays_partial(
    tmp_path, fake_http, monkeypatch
) -> None:
    serve_project(fake_http)
    serve_pages(
        fake_http,
        BUGS_URL,
        [{"tickets": [{"ticket_num": 1}]}, {"tickets": []}],
    )
    canned_ticket(monkeypatch)

    manifest = run_snapshot(tmp_path)

    assert {"code": "tracker-count-unavailable", "tracker": "bugs"} in manifest["gaps"]
    assert manifest["status"] == "partial"
    assert manifest["counts"]["tickets_expected"] is None


def test_a_failed_enumeration_is_a_gap(tmp_path, fake_http, monkeypatch) -> None:
    serve_project(fake_http)
    fake_http.serve_json(paged_url(BUGS_URL, 0), {"error": "gone"}, status=404)
    canned_ticket(monkeypatch)

    manifest = run_snapshot(tmp_path)

    assert [gap["code"] for gap in manifest["gaps"]] == ["tracker-enumeration-failed"]
    assert manifest["status"] == "partial"


def test_normalized_rows_carry_the_run_source_id(tmp_path, fake_http, monkeypatch) -> None:
    serve_project(fake_http)
    serve_pages(fake_http, BUGS_URL, [{"count": 1, "tickets": [{"ticket_num": 1}]}])
    canned_ticket(monkeypatch)

    run_snapshot(tmp_path, source_id="other-sourceforge-project")

    rows = [
        json.loads(line)
        for line in (tmp_path / "normalized.jsonl").read_text(encoding="utf-8").splitlines()
    ]
    assert [row["source_id"] for row in rows] == ["other-sourceforge-project"]


def test_fetch_ticket_records_the_requested_source_id(tmp_path, fake_http) -> None:
    fake_http.serve_json(
        f"{BUGS_URL}/7",
        {"ticket": {"ticket_num": 7, "summary": "Example", "description": "raw prose"}},
    )

    fetched = sourceforge_snapshot.fetch_ticket(
        BUGS_URL, "bugs", 7, tmp_path / "raw", 0.0, "other-sourceforge-project"
    )

    assert fetched["record"]["source_id"] == "other-sourceforge-project"
    assert fetched["record"]["comment_count"] == 0
    assert "description" not in fetched["record"]


def test_resume_counts_loaded_reused_and_refetched_rows(tmp_path, fake_http, monkeypatch) -> None:
    serve_project(fake_http)
    resume_path = tmp_path / "resume.jsonl"
    resume_path.write_text(
        "\n".join(
            json.dumps(record)
            for record in (
                {
                    "tracker": "bugs",
                    "ticket_num": 1,
                    "comment_count": 0,
                    "raw_responses": [{"sha256": "already-linked"}],
                },
                {"tracker": "bugs", "ticket_num": 2, "comment_count": 0},
            )
        )
        + "\n",
        encoding="utf-8",
    )
    fetched = canned_ticket(monkeypatch)
    monkeypatch.setattr(
        sourceforge_snapshot,
        "enumerate_tracker",
        lambda store, base: ([1, 2, 3], 3, [{"status": 200}]),
    )

    manifest = run_snapshot(tmp_path, resume_from=resume_path, refresh_missing_raw_links=True)

    assert sorted(fetched) == [2, 3]
    assert manifest["counts"]["tickets_loaded_from_prior_run"] == 2
    assert manifest["counts"]["tickets_reused_without_fetch"] == 1
    assert manifest["counts"]["tickets_fetched_or_refetched"] == 2
    assert manifest["counts"]["tickets_reused_from_prior_run"] == 1
    assert manifest["status"] == "observable-complete"
    assert manifest["scope"] == {
        "boundary": "tracker-rest-interfaces",
        "status_applies_to": "requests.trackers",
        "completion_rule": (
            "Every ticket exposed by the listed tracker REST interfaces, "
            "together with its observable discussion pages."
        ),
    }


@pytest.mark.parametrize(
    ("argument", "message"),
    [
        ("--workers=0", "workers must be between 1 and 32"),
        ("--workers=33", "workers must be between 1 and 32"),
        ("--delay-seconds=-1", "delay-seconds must be 0 or greater"),
    ],
)
def test_cli_rejects_out_of_range_arguments(monkeypatch, tmp_path, argument, message) -> None:
    monkeypatch.setattr(
        "sys.argv",
        [
            "sourceforge_snapshot",
            "--tracker",
            f"bugs={BUGS_URL}",
            "--normalized-output",
            str(tmp_path / "normalized.jsonl"),
            "--manifest-output",
            str(tmp_path / "manifest.yaml"),
            argument,
        ],
    )
    with pytest.raises(SystemExit, match=message):
        sourceforge_snapshot.main()
