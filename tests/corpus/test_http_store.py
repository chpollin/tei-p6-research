"""Offline behaviour of the controlled HTTP store: retry, storage, JSON access.

Every test replaces ``urllib.request.urlopen`` with a fake opener; no test in
this module may reach the network.
"""

import hashlib
import io
import json
import urllib.error

import pytest

from tools.corpus import http_store
from tools.corpus.http_store import HttpStore, canonical_url


class FakeResponse:
    def __init__(
        self,
        body: bytes,
        *,
        status: int = 200,
        url: str = "https://example.org/resource",
        headers: dict[str, str] | None = None,
    ) -> None:
        self._stream = io.BytesIO(body)
        self.status = status
        self._url = url
        self.headers = headers or {"Content-Type": "application/json"}

    def read(self, size: int | None = None) -> bytes:
        return self._stream.read() if size is None else self._stream.read(size)

    def geturl(self) -> str:
        return self._url

    def __enter__(self) -> "FakeResponse":
        return self

    def __exit__(self, *_: object) -> None:
        return None


def http_error(code: int, *, headers: dict[str, str] | None = None) -> urllib.error.HTTPError:
    return urllib.error.HTTPError(
        "https://example.org/resource",
        code,
        "error",
        headers or {},  # type: ignore[arg-type]
        io.BytesIO(b'{"error": true}'),
    )


@pytest.fixture
def recorded_sleeps(monkeypatch) -> list[float]:
    delays: list[float] = []
    monkeypatch.setattr(http_store.time, "sleep", delays.append)
    monkeypatch.delenv("GITHUB_TOKEN", raising=False)
    return delays


def install_opener(monkeypatch, responses: list[object]) -> list[str]:
    """Serve one queued response or exception per attempt and record the URLs."""

    seen: list[str] = []

    def fake_urlopen(request, timeout=None):
        seen.append(request.full_url)
        outcome = responses.pop(0)
        if isinstance(outcome, Exception):
            raise outcome
        return outcome

    monkeypatch.setattr(http_store.urllib.request, "urlopen", fake_urlopen)
    return seen


def test_canonical_url_removes_fragment_and_sorts_query() -> None:
    assert canonical_url("HTTPS://EXAMPLE.org/a?z=2&a=1#part") == "https://example.org/a?a=1&z=2"
    assert canonical_url("https://example.org") == "https://example.org/"


def test_fetch_stores_body_content_addressed(tmp_path, monkeypatch, recorded_sleeps) -> None:
    body = b'{"value": 1}'
    install_opener(monkeypatch, [FakeResponse(body)])
    store = HttpStore(tmp_path)

    result, returned = store.fetch("HTTPS://EXAMPLE.org/resource?b=2&a=1#part")

    digest = hashlib.sha256(body).hexdigest()
    assert returned == body
    assert result.sha256 == digest
    assert result.canonical_url == "https://example.org/resource?a=1&b=2"
    assert result.media_type == "application/json"
    assert (tmp_path / "sha256" / digest[:2] / digest[2:]).read_bytes() == body
    assert recorded_sleeps == []


def test_fetch_retries_transient_status_then_succeeds(
    tmp_path, monkeypatch, recorded_sleeps
) -> None:
    install_opener(monkeypatch, [http_error(503), FakeResponse(b'{"ok": true}')])
    store = HttpStore(tmp_path)

    result, _ = store.fetch("https://example.org/resource")

    assert result.status == 200
    assert recorded_sleeps == [1]


@pytest.mark.parametrize(
    ("retry_after", "delay"),
    [("5", 5), ("120", 30), ("Wed, 21 Oct 2015 07:28:00 GMT", 1), (None, 1)],
)
def test_retry_after_header_governs_the_first_backoff(
    tmp_path, monkeypatch, recorded_sleeps, retry_after, delay
) -> None:
    headers = {"Retry-After": retry_after} if retry_after is not None else {}
    install_opener(monkeypatch, [http_error(429, headers=headers), FakeResponse(b"{}")])
    store = HttpStore(tmp_path)

    store.fetch("https://example.org/resource")

    assert recorded_sleeps == [delay]


def test_fetch_does_not_sleep_after_the_final_attempt(
    tmp_path, monkeypatch, recorded_sleeps
) -> None:
    install_opener(monkeypatch, [urllib.error.URLError("down")] * 3)
    store = HttpStore(tmp_path, retries=3)

    with pytest.raises(RuntimeError, match="failed to fetch"):
        store.fetch("https://example.org/resource")

    assert recorded_sleeps == [1, 2]


def test_fetch_records_a_permanent_http_error_instead_of_retrying(
    tmp_path, monkeypatch, recorded_sleeps
) -> None:
    install_opener(monkeypatch, [http_error(404)])
    store = HttpStore(tmp_path)

    result, body = store.fetch("https://example.org/resource")

    assert result.status == 404
    assert body == b'{"error": true}'
    assert recorded_sleeps == []


def test_fetch_reports_a_hash_collision(tmp_path, monkeypatch, recorded_sleeps) -> None:
    body = b'{"value": 1}'
    digest = hashlib.sha256(body).hexdigest()
    destination = tmp_path / "sha256" / digest[:2] / digest[2:]
    destination.parent.mkdir(parents=True)
    destination.write_bytes(b"different bytes under the same digest")
    install_opener(monkeypatch, [FakeResponse(body)])

    with pytest.raises(RuntimeError, match="raw hash collision"):
        HttpStore(tmp_path).fetch("https://example.org/resource")


def test_fetch_leaves_no_temporary_file_beside_the_object(
    tmp_path, monkeypatch, recorded_sleeps
) -> None:
    body = b"payload"
    install_opener(monkeypatch, [FakeResponse(body)])
    result, _ = HttpStore(tmp_path).fetch("https://example.org/resource")

    stored = tmp_path / "sha256" / result.sha256[:2]
    assert [path.name for path in stored.iterdir()] == [result.sha256[2:]]


def test_fetch_stream_writes_and_deduplicates(tmp_path, monkeypatch, recorded_sleeps) -> None:
    body = b"a" * 2048
    digest = hashlib.sha256(body).hexdigest()
    install_opener(monkeypatch, [FakeResponse(body), FakeResponse(body)])
    store = HttpStore(tmp_path)

    first = store.fetch_stream("https://example.org/asset.zip")
    second = store.fetch_stream("https://example.org/asset.zip")

    assert first.sha256 == second.sha256 == digest
    assert first.byte_count == len(body)
    assert (tmp_path / "sha256" / digest[:2] / digest[2:]).read_bytes() == body
    assert list((tmp_path / "staging").iterdir()) == []


def test_fetch_stream_retries_and_cleans_its_partial_file(
    tmp_path, monkeypatch, recorded_sleeps
) -> None:
    install_opener(monkeypatch, [urllib.error.URLError("reset"), FakeResponse(b"asset")])
    store = HttpStore(tmp_path)

    result = store.fetch_stream("https://example.org/asset.zip")

    assert result.byte_count == 5
    assert recorded_sleeps == [1]
    assert list((tmp_path / "staging").iterdir()) == []


def test_fetch_stream_does_not_sleep_after_the_final_attempt(
    tmp_path, monkeypatch, recorded_sleeps
) -> None:
    install_opener(monkeypatch, [urllib.error.URLError("down")] * 2)
    store = HttpStore(tmp_path, retries=2)

    with pytest.raises(RuntimeError, match="failed to fetch"):
        store.fetch_stream("https://example.org/asset.zip")

    assert recorded_sleeps == [1]


def test_fetch_json_parses_and_journals(tmp_path, monkeypatch, recorded_sleeps) -> None:
    install_opener(monkeypatch, [FakeResponse(json.dumps({"count": 2}).encode("utf-8"))])
    journal: list[dict[str, object]] = []

    payload, record = HttpStore(tmp_path).fetch_json(
        "https://example.org/resource", journal=journal
    )

    assert payload == {"count": 2}
    assert journal == [record]
    assert record["canonical_url"] == canonical_url("https://example.org/resource")


def test_fetch_json_journals_a_failed_response_before_raising(
    tmp_path, monkeypatch, recorded_sleeps
) -> None:
    install_opener(monkeypatch, [http_error(404)])
    journal: list[dict[str, object]] = []

    with pytest.raises(RuntimeError, match="HTTP 404"):
        HttpStore(tmp_path).fetch_json("https://example.org/resource", journal=journal)

    assert [record["status"] for record in journal] == [404]


def test_fetch_json_reports_invalid_json(tmp_path, monkeypatch, recorded_sleeps) -> None:
    install_opener(monkeypatch, [FakeResponse(b"<html>not json</html>")])
    journal: list[dict[str, object]] = []

    with pytest.raises(RuntimeError, match="invalid JSON"):
        HttpStore(tmp_path).fetch_json("https://example.org/resource", journal=journal)

    assert len(journal) == 1


def test_github_authorization_is_scoped_to_the_github_api(tmp_path, monkeypatch) -> None:
    monkeypatch.delenv("GITHUB_TOKEN", raising=False)
    store = HttpStore(tmp_path, github_token="secret-token")

    github = store._headers("https://api.github.com/repos/o/r")
    elsewhere = store._headers("https://example.org/resource")

    assert github["Authorization"] == "Bearer secret-token"
    assert github["X-GitHub-Api-Version"] == "2022-11-28"
    assert "Authorization" not in elsewhere


def test_recorded_headers_exclude_authorization(tmp_path, monkeypatch, recorded_sleeps) -> None:
    install_opener(
        monkeypatch,
        [
            FakeResponse(
                b"{}",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": "Bearer secret-token",
                    "Set-Cookie": "session=1",
                    "ETag": '"abc"',
                },
            )
        ],
    )

    result, _ = HttpStore(tmp_path).fetch("https://example.org/resource")

    assert set(result.headers) == {"content-type", "etag"}
