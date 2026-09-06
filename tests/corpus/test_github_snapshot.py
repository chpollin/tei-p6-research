"""GitHub work-item snapshot: status follows the recorded gaps, never a constant."""

import json
import subprocess

import pytest

from tools.corpus import github_snapshot
from tools.corpus.github_snapshot import api_url, collect, metadata, next_link

GRAPHQL_GAP = "graphql-relations-not-yet-collected"
ISSUE = {"id": 11, "node_id": "I_1", "number": 1, "title": "Issue", "state": "open"}
PULL = {
    "id": 12,
    "node_id": "PR_1",
    "number": 2,
    "title": "Pull request",
    "state": "closed",
    "pull_request": {"url": "https://api.github.com/repos/o/r/pulls/2"},
}


def serve_repository(fake_http, work_items: list[dict] | None = None) -> None:
    items = [ISSUE, PULL] if work_items is None else work_items
    fake_http.serve_json(api_url("o", "r", ""), {"id": 1, "node_id": "R_1", "url": "u"})
    fake_http.serve_json(api_url("o", "r", "labels", per_page=100), [{"name": "bug"}])
    fake_http.serve_json(api_url("o", "r", "milestones", state="all", per_page=100), [])
    fake_http.serve_json(api_url("o", "r", "releases", per_page=100), [])
    fake_http.serve_json(
        api_url(
            "o", "r", "issues", state="all", sort="created", direction="asc", per_page=100
        ),
        items,
    )
    for item in items:
        number = item["number"]
        fake_http.serve_json(api_url("o", "r", f"issues/{number}"), item)
        fake_http.serve_json(api_url("o", "r", f"issues/{number}/comments", per_page=100), [])
        fake_http.serve_json(api_url("o", "r", f"issues/{number}/timeline", per_page=100), [])
        if "pull_request" not in item:
            continue
        fake_http.serve_json(api_url("o", "r", f"pulls/{number}"), item)
        for endpoint in ("reviews", "comments", "commits", "files"):
            fake_http.serve_json(
                api_url("o", "r", f"pulls/{number}/{endpoint}", per_page=100), []
            )


def run(tmp_path, **overrides) -> dict:
    arguments = {
        "owner": "o",
        "repository": "r",
        "source_id": "github-teic-tei-work-items",
        "raw_root": tmp_path / "raw",
        "normalized_output": tmp_path / "work-items.jsonl",
        "manifest_output": tmp_path / "2026-09-06-work-items.yaml",
        "max_items": None,
        "allow_unauthenticated": True,
    }
    return collect(**(arguments | overrides))


def test_next_link() -> None:
    header = (
        '<https://api.github.com/items?page=2>; rel="next", '
        '<https://api.github.com/items?page=8>; rel="last"'
    )
    assert next_link(header) == "https://api.github.com/items?page=2"
    assert next_link(None) is None


def test_metadata_excludes_body_and_login() -> None:
    record = metadata(
        "issue",
        {
            "id": 1,
            "node_id": "I_1",
            "number": 7,
            "title": "Example",
            "body": "untrusted full text",
            "user": {"node_id": "U_1", "login": "person"},
            "labels": [{"name": "bug"}],
        },
    )
    assert record["title"] == "Example"
    assert record["author_node_id"] == "U_1"
    assert record["labels"] == ["bug"]
    assert "body" not in record
    assert "login" not in record


def test_a_clean_run_records_only_the_known_missing_stage(tmp_path, fake_http) -> None:
    serve_repository(fake_http)

    manifest = run(tmp_path)

    assert [gap["code"] for gap in manifest["gaps"]] == [GRAPHQL_GAP]
    assert manifest["status"] == "partial"
    rows = [
        json.loads(line)
        for line in (tmp_path / "work-items.jsonl").read_text(encoding="utf-8").splitlines()
    ]
    assert {row["kind"] for row in rows} == {
        "repository",
        "label",
        "issue",
        "pull-request-summary",
        "work-item-detail",
        "pull-request",
    }
    assert manifest["counts"]["http_requests"] == len(manifest["requests"])


def test_the_max_items_gap_appears_only_when_the_limit_binds(tmp_path, fake_http) -> None:
    serve_repository(fake_http)

    unbounded = run(tmp_path, max_items=5)
    bounded = run(tmp_path, max_items=1)

    assert [gap["code"] for gap in unbounded["gaps"]] == [GRAPHQL_GAP]
    assert [gap["code"] for gap in bounded["gaps"]] == ["max-items-limit", GRAPHQL_GAP]


def test_a_rate_limit_stop_is_recorded_as_its_own_gap(tmp_path, fake_http) -> None:
    serve_repository(fake_http)
    fake_http.serve_json(
        api_url("o", "r", "labels", per_page=100),
        [],
        headers={"X-RateLimit-Remaining": "1"},
    )

    manifest = run(tmp_path)

    assert [gap["code"] for gap in manifest["gaps"]] == ["rate-limit-stop", GRAPHQL_GAP]
    assert manifest["status"] == "partial"


def test_a_failed_request_is_recorded_as_a_collection_error(tmp_path, fake_http) -> None:
    serve_repository(fake_http)
    fake_http.serve_json(api_url("o", "r", ""), {"message": "Not Found"}, status=404)

    manifest = run(tmp_path)

    assert [gap["code"] for gap in manifest["gaps"]] == ["collection-error", GRAPHQL_GAP]
    assert manifest["requests"][0]["status"] == 404


def test_an_unauthenticated_run_is_refused_unless_allowed(tmp_path, fake_http, monkeypatch) -> None:
    monkeypatch.setattr(github_snapshot, "resolve_github_token", lambda: None)

    with pytest.raises(RuntimeError, match="authenticated GitHub session"):
        run(tmp_path, allow_unauthenticated=False)


@pytest.mark.parametrize(
    ("returncode", "stdout", "token"),
    [(0, "gh-token\n", "gh-token"), (1, "", None)],
)
def test_resolve_github_token_reads_the_gh_session(
    monkeypatch, returncode, stdout, token
) -> None:
    monkeypatch.delenv("GITHUB_TOKEN", raising=False)
    monkeypatch.setattr(
        github_snapshot.subprocess,
        "run",
        lambda *args, **kwargs: subprocess.CompletedProcess(args, returncode, stdout, ""),
    )
    assert github_snapshot.resolve_github_token() == token


def test_resolve_github_token_prefers_the_environment(monkeypatch) -> None:
    monkeypatch.setenv("GITHUB_TOKEN", "environment-token")
    monkeypatch.setattr(
        github_snapshot.subprocess,
        "run",
        lambda *args, **kwargs: pytest.fail("gh must not run when the environment has a token"),
    )
    assert github_snapshot.resolve_github_token() == "environment-token"


def test_resolve_github_token_survives_a_missing_gh(monkeypatch) -> None:
    monkeypatch.delenv("GITHUB_TOKEN", raising=False)

    def missing(*args, **kwargs):
        raise OSError("gh not found")

    monkeypatch.setattr(github_snapshot.subprocess, "run", missing)
    assert github_snapshot.resolve_github_token() is None


def test_main_exit_code_follows_the_recorded_gaps(tmp_path, fake_http, monkeypatch, capsys) -> None:
    serve_repository(fake_http)
    monkeypatch.setattr(
        github_snapshot.subprocess,
        "run",
        lambda *args, **kwargs: subprocess.CompletedProcess(args, 0, "gh-token\n", ""),
    )
    monkeypatch.setattr(
        "sys.argv",
        [
            "github_snapshot",
            "--owner",
            "o",
            "--repository",
            "r",
            "--source-id",
            "github-teic-tei-work-items",
            "--raw-root",
            str(tmp_path / "raw"),
            "--normalized-output",
            str(tmp_path / "work-items.jsonl"),
            "--manifest-output",
            str(tmp_path / "run.yaml"),
        ],
    )

    exit_code = github_snapshot.main()

    assert exit_code == 2
    assert capsys.readouterr().out.startswith("partial: github-teic-tei-work-items ->")
    assert fake_http.headers_seen[0]["authorization"] == "Bearer gh-token"


def test_api_url_never_ends_with_a_slash_for_the_repository_itself() -> None:
    """GitHub answers 404 to a trailing slash on the repository resource."""
    assert api_url("TEIC", "TEI", "") == "https://api.github.com/repos/TEIC/TEI"
    assert api_url("TEIC", "TEI", "/") == "https://api.github.com/repos/TEIC/TEI"
    assert api_url("TEIC", "TEI", "issues/1") == "https://api.github.com/repos/TEIC/TEI/issues/1"
    assert api_url("TEIC", "TEI", "labels", per_page=100).endswith("/labels?per_page=100")


def test_wait_for_reset_sleeps_past_the_reset_instant_instead_of_stopping(tmp_path, monkeypatch) -> None:
    collector = github_snapshot.GitHubCollector(tmp_path / "raw", wait_for_reset=True)
    record = {"headers": {"x-ratelimit-remaining": "3", "x-ratelimit-reset": "1000"}}
    monkeypatch.setattr(collector.store, "fetch_json", lambda url, journal=None: ({"ok": True}, record))
    slept: list[float] = []
    monkeypatch.setattr(github_snapshot.time, "time", lambda: 940.0)
    monkeypatch.setattr(github_snapshot.time, "sleep", slept.append)
    payload, _ = collector.get_json("https://api.github.com/repos/o/r")
    assert payload == {"ok": True}
    assert slept == [65.0]


def test_without_wait_for_reset_the_low_quota_still_stops(tmp_path, monkeypatch) -> None:
    collector = github_snapshot.GitHubCollector(tmp_path / "raw")
    record = {"headers": {"x-ratelimit-remaining": "3", "x-ratelimit-reset": "1000"}}
    monkeypatch.setattr(collector.store, "fetch_json", lambda url, journal=None: ({}, record))
    with pytest.raises(github_snapshot.RateLimitStop):
        collector.get_json("https://api.github.com/repos/o/r")
