"""Release-asset retrieval and the local import of a resumed download."""

import hashlib
import json

import pytest

from tools.corpus.asset_snapshot import snapshot

ASSET_URL = "https://example.org/release/tei-4.12.0.zip"


def run(tmp_path, **overrides) -> dict:
    arguments = {
        "source_id": "tei-p5-4.12.0-release-asset",
        "urls": [ASSET_URL],
        "raw_root": tmp_path / "raw",
        "normalized_output": tmp_path / "assets.json",
        "manifest_output": tmp_path / "run.yaml",
        "workers": 1,
    }
    return snapshot(**(arguments | overrides))


def staged(tmp_path, body: bytes) -> "object":
    staging = tmp_path / "raw" / "staging"
    staging.mkdir(parents=True)
    path = staging / "download.part"
    path.write_bytes(body)
    return path


def test_a_retrieved_asset_is_observable_complete(tmp_path, fake_http) -> None:
    body = b"PK\x03\x04payload"
    fake_http.serve(ASSET_URL, body, media_type="application/zip")

    manifest = run(tmp_path)

    digest = hashlib.sha256(body).hexdigest()
    assert manifest["status"] == "observable-complete"
    assert manifest["counts"] == {
        "requested_assets": 1,
        "retrieved_assets": 1,
        "bytes": len(body),
        "gaps": 0,
    }
    assert (tmp_path / "raw" / "sha256" / digest[:2] / digest[2:]).read_bytes() == body
    normalized = json.loads((tmp_path / "assets.json").read_text(encoding="utf-8"))
    assert normalized["assets"][0]["sha256"] == digest


def test_a_failed_asset_is_a_gap(tmp_path, fake_http) -> None:
    manifest = run(tmp_path)

    assert [gap["code"] for gap in manifest["gaps"]] == ["asset-fetch-failed"]
    assert manifest["gaps"][0]["url"] == ASSET_URL
    assert manifest["status"] == "partial"
    assert manifest["counts"]["retrieved_assets"] == 0


def test_a_staged_download_is_imported_into_the_raw_store(tmp_path, fake_http) -> None:
    body = b"resumed release bundle"
    path = staged(tmp_path, body)

    manifest = run(
        tmp_path,
        urls=[],
        staged_file=path,
        staged_url=ASSET_URL,
        expected_bytes=len(body),
    )

    digest = hashlib.sha256(body).hexdigest()
    assert manifest["status"] == "observable-complete"
    assert manifest["counts"]["requested_assets"] == 1
    assert (tmp_path / "raw" / "sha256" / digest[:2] / digest[2:]).read_bytes() == body
    assert not path.exists()
    assert manifest["assets"][0]["transfer"] == "resumed-external-download-then-local-import"


def test_a_staged_file_without_its_url_is_refused(tmp_path, fake_http) -> None:
    path = staged(tmp_path, b"body")

    with pytest.raises(RuntimeError, match="staged_url"):
        run(tmp_path, urls=[], staged_file=path)


def test_a_staged_file_outside_the_staging_root_is_refused(tmp_path, fake_http) -> None:
    outside = tmp_path / "elsewhere.zip"
    outside.write_bytes(b"body")

    with pytest.raises(RuntimeError, match="staged file must be inside"):
        run(tmp_path, urls=[], staged_file=outside, staged_url=ASSET_URL)


def test_a_staged_file_of_the_wrong_size_is_refused(tmp_path, fake_http) -> None:
    path = staged(tmp_path, b"short")

    with pytest.raises(RuntimeError, match="staged file size mismatch"):
        run(tmp_path, urls=[], staged_file=path, staged_url=ASSET_URL, expected_bytes=999)
