"""Offline scaffolding for the collector tests.

Collectors reach the network only through ``tools.corpus.http_store``. These
fixtures replace its opener and its backoff, so no test in ``tests/corpus`` may
open a socket or wait.
"""

import io
import json
import urllib.error
from typing import Any

import pytest

from tools.corpus import http_store
from tools.corpus.http_store import canonical_url


class FakeResponse:
    def __init__(
        self,
        body: bytes,
        *,
        status: int = 200,
        url: str = "https://example.org/",
        headers: dict[str, str] | None = None,
    ) -> None:
        self._stream = io.BytesIO(body)
        self.status = status
        self._url = url
        self.headers = headers or {}

    def read(self, size: int | None = None) -> bytes:
        return self._stream.read() if size is None else self._stream.read(size)

    def geturl(self) -> str:
        return self._url

    def __enter__(self) -> "FakeResponse":
        return self

    def __exit__(self, *_: object) -> None:
        return None


class FakeHttp:
    """Route canonical URLs to canned responses and record what was requested."""

    def __init__(self) -> None:
        self.routes: dict[str, dict[str, Any]] = {}
        self.requested: list[str] = []
        self.headers_seen: list[dict[str, str]] = []

    def serve(
        self,
        url: str,
        body: bytes,
        *,
        status: int = 200,
        media_type: str = "text/html",
        headers: dict[str, str] | None = None,
    ) -> None:
        self.routes[canonical_url(url)] = {
            "body": body,
            "status": status,
            "headers": {"Content-Type": media_type, **(headers or {})},
            "url": url,
        }

    def serve_json(self, url: str, payload: Any, **kwargs: Any) -> None:
        self.serve(
            url,
            json.dumps(payload).encode("utf-8"),
            media_type="application/json",
            **kwargs,
        )

    def open(self, request: Any, timeout: int | None = None) -> FakeResponse:
        url = canonical_url(request.full_url)
        self.requested.append(url)
        self.headers_seen.append({key.lower(): value for key, value in request.headers.items()})
        route = self.routes.get(url)
        if route is None:
            raise urllib.error.URLError(f"no route for {url}")
        if route["status"] >= 400:
            raise urllib.error.HTTPError(
                route["url"],
                route["status"],
                "error",
                route["headers"],  # type: ignore[arg-type]
                io.BytesIO(route["body"]),
            )
        return FakeResponse(
            route["body"],
            status=route["status"],
            url=route["url"],
            headers=route["headers"],
        )


@pytest.fixture
def fake_http(monkeypatch) -> FakeHttp:
    fake = FakeHttp()
    monkeypatch.setattr(http_store.urllib.request, "urlopen", fake.open)
    monkeypatch.setattr(http_store.time, "sleep", lambda _seconds: None)
    monkeypatch.delenv("GITHUB_TOKEN", raising=False)
    return fake
