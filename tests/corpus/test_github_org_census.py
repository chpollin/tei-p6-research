"""Organization repository census: authenticated access and rate-limit stop."""

from tools.corpus import github_org_census
from tools.corpus.github_org_census import census, repository_metadata

CENSUS_URL = (
    "https://api.github.com/orgs/TEIC/repos"
    "?type=all&sort=full_name&direction=asc&per_page=100"
)
REPOSITORY = {
    "id": 1,
    "node_id": "R_1",
    "name": "TEI",
    "full_name": "TEIC/TEI",
    "clone_url": "https://github.com/TEIC/TEI.git",
    "license": {"spdx_id": "BSD-2-Clause"},
}


def run(tmp_path) -> dict:
    return census(
        organization="TEIC",
        source_id="teic-github-organization",
        raw_root=tmp_path / "raw",
        normalized_output=tmp_path / "repositories.jsonl",
        manifest_output=tmp_path / "run.yaml",
    )


def test_repository_metadata() -> None:
    result = repository_metadata(REPOSITORY)
    assert result["full_name"] == "TEIC/TEI"
    assert result["license_spdx_id"] == "BSD-2-Clause"


def test_census_uses_the_shared_token_resolution(tmp_path, fake_http, monkeypatch) -> None:
    monkeypatch.setattr(github_org_census, "resolve_github_token", lambda: "census-token")
    fake_http.serve_json(CENSUS_URL, [REPOSITORY])

    manifest = run(tmp_path)

    assert fake_http.headers_seen[0]["authorization"] == "Bearer census-token"
    assert manifest["status"] == "observable-complete"
    assert manifest["counts"]["repositories"] == 1


def test_a_low_remaining_quota_stops_the_census(tmp_path, fake_http, monkeypatch) -> None:
    monkeypatch.setattr(github_org_census, "resolve_github_token", lambda: "census-token")
    fake_http.serve_json(CENSUS_URL, [REPOSITORY], headers={"X-RateLimit-Remaining": "1"})

    manifest = run(tmp_path)

    assert [gap["code"] for gap in manifest["gaps"]] == ["rate-limit-stop"]
    assert manifest["status"] == "partial"
    assert manifest["counts"]["repositories"] == 0
