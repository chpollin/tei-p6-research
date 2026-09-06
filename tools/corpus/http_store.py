"""Controlled HTTP access with content-addressed local raw storage."""

from __future__ import annotations

import hashlib
import json
import os
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any
from uuid import uuid4

from tools.corpus.manifest import sha256_bytes

USER_AGENT = "tei-p6-research-vault/0 (+https://github.com/TEIC/TEI)"
RECORDED_HEADERS = {
    "content-length",
    "content-type",
    "date",
    "etag",
    "last-modified",
    "link",
    "retry-after",
    "x-github-api-version-selected",
    "x-ratelimit-limit",
    "x-ratelimit-remaining",
    "x-ratelimit-reset",
    "x-ratelimit-resource",
}


def utc_now() -> str:
    return datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def canonical_url(url: str) -> str:
    parsed = urllib.parse.urlsplit(url)
    query = urllib.parse.parse_qsl(parsed.query, keep_blank_values=True)
    return urllib.parse.urlunsplit(
        (
            parsed.scheme.lower(),
            parsed.netloc.lower(),
            parsed.path or "/",
            urllib.parse.urlencode(sorted(query)),
            "",
        )
    )


@dataclass(frozen=True)
class FetchResult:
    requested_url: str
    canonical_url: str
    final_url: str
    observed_at: str
    status: int
    media_type: str
    byte_count: int
    sha256: str
    raw_path: str
    headers: dict[str, str]

    def as_record(self) -> dict[str, object]:
        return {
            "requested_url": self.requested_url,
            "canonical_url": self.canonical_url,
            "final_url": self.final_url,
            "observed_at": self.observed_at,
            "status": self.status,
            "media_type": self.media_type,
            "byte_count": self.byte_count,
            "sha256": self.sha256,
            "raw_path": self.raw_path,
            "headers": self.headers,
        }


class HttpStore:
    def __init__(
        self,
        raw_root: Path,
        *,
        timeout: int = 60,
        retries: int = 3,
        github_token: str | None = None,
    ):
        self.raw_root = raw_root
        self.timeout = timeout
        self.retries = retries
        self.github_token = github_token

    def _headers(self, url: str) -> dict[str, str]:
        headers = {"Accept": "*/*", "User-Agent": USER_AGENT}
        host = urllib.parse.urlsplit(url).hostname
        token = self.github_token or os.environ.get("GITHUB_TOKEN")
        if host == "api.github.com":
            headers["Accept"] = "application/vnd.github+json"
            headers["X-GitHub-Api-Version"] = "2022-11-28"
            if token:
                headers["Authorization"] = f"Bearer {token}"
        return headers

    def fetch(self, url: str) -> tuple[FetchResult, bytes]:
        requested = canonical_url(url)
        last_error: Exception | None = None
        for attempt in range(self.retries):
            request = urllib.request.Request(requested, headers=self._headers(requested))
            observed_at = utc_now()
            try:
                with urllib.request.urlopen(request, timeout=self.timeout) as response:
                    body = response.read()
                    status = response.status
                    final_url = canonical_url(response.geturl())
                    headers = response.headers
                return self._store(requested, final_url, observed_at, status, headers, body)
            except urllib.error.HTTPError as error:
                body = error.read()
                if error.code not in {429, 500, 502, 503, 504}:
                    return self._store(
                        requested,
                        canonical_url(error.geturl()),
                        observed_at,
                        error.code,
                        error.headers,
                        body,
                    )
                last_error = error
                retry_after = error.headers.get("Retry-After")
                delay = min(int(retry_after), 30) if retry_after and retry_after.isdigit() else 2**attempt
                self._back_off(attempt, delay)
            except (OSError, urllib.error.URLError) as error:
                last_error = error
                self._back_off(attempt, 2**attempt)
        raise RuntimeError(f"failed to fetch {requested}: {last_error}")

    def fetch_json(
        self, url: str, journal: list[dict[str, object]] | None = None
    ) -> tuple[Any, dict[str, object]]:
        """Fetch one JSON response, journal it, and parse it.

        The response record reaches ``journal`` before an HTTP or parse failure
        raises, so a request journal stays complete across a failed run.
        """

        result, body = self.fetch(url)
        record = result.as_record()
        if journal is not None:
            journal.append(record)
        if result.status >= 400:
            raise RuntimeError(f"HTTP {result.status} for {result.canonical_url}")
        try:
            return json.loads(body), record
        except json.JSONDecodeError as error:
            raise RuntimeError(f"invalid JSON for {result.canonical_url}: {error}") from error

    def fetch_stream(self, url: str) -> FetchResult:
        """Fetch a large object without retaining its response body in memory."""

        requested = canonical_url(url)
        last_error: Exception | None = None
        staging = self.raw_root / "staging"
        staging.mkdir(parents=True, exist_ok=True)
        for attempt in range(self.retries):
            temporary = staging / f"{os.getpid()}-{uuid4().hex}.part"
            request = urllib.request.Request(requested, headers=self._headers(requested))
            observed_at = utc_now()
            try:
                with urllib.request.urlopen(request, timeout=self.timeout) as response:
                    status = response.status
                    final_url = canonical_url(response.geturl())
                    headers = response.headers
                    digest = hashlib.sha256()
                    byte_count = 0
                    with temporary.open("wb") as output:
                        while chunk := response.read(1024 * 1024):
                            output.write(chunk)
                            digest.update(chunk)
                            byte_count += len(chunk)
                hexdigest = digest.hexdigest()
                relative = Path("sha256") / hexdigest[:2] / hexdigest[2:]
                destination = self.raw_root / relative
                destination.parent.mkdir(parents=True, exist_ok=True)
                if destination.exists():
                    temporary.unlink()
                else:
                    temporary.replace(destination)
                safe_headers = {
                    key.lower(): value
                    for key, value in headers.items()
                    if key.lower() in RECORDED_HEADERS
                }
                return FetchResult(
                    requested_url=requested,
                    canonical_url=canonical_url(requested),
                    final_url=final_url,
                    observed_at=observed_at,
                    status=status,
                    media_type=safe_headers.get("content-type", "application/octet-stream").split(";", 1)[0],
                    byte_count=byte_count,
                    sha256=hexdigest,
                    raw_path=relative.as_posix(),
                    headers=safe_headers,
                )
            except (OSError, urllib.error.URLError) as error:
                temporary.unlink(missing_ok=True)
                last_error = error
                self._back_off(attempt, 2**attempt)
        raise RuntimeError(f"failed to fetch {requested}: {last_error}")

    def _back_off(self, attempt: int, delay: float) -> None:
        """Wait between attempts; the last attempt is never followed by a wait."""

        if attempt + 1 < self.retries:
            time.sleep(delay)

    def _store(
        self,
        requested_url: str,
        final_url: str,
        observed_at: str,
        status: int,
        headers: object,
        body: bytes,
    ) -> tuple[FetchResult, bytes]:
        digest = sha256_bytes(body)
        relative = Path("sha256") / digest[:2] / digest[2:]
        destination = self.raw_root / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        if destination.exists():
            if destination.read_bytes() != body:
                raise RuntimeError(f"raw hash collision at {destination}")
        else:
            # Short staging name keeps the path under the Windows limit that a
            # digest-length temporary name next to the destination can exceed.
            staging = self.raw_root / "staging"
            staging.mkdir(parents=True, exist_ok=True)
            temporary = staging / f"{os.getpid()}-{uuid4().hex}.part"
            temporary.write_bytes(body)
            temporary.replace(destination)

        safe_headers = {
            key.lower(): value
            for key, value in headers.items()  # type: ignore[attr-defined]
            if key.lower() in RECORDED_HEADERS
        }
        media_type = safe_headers.get("content-type", "application/octet-stream").split(";", 1)[0]
        result = FetchResult(
            requested_url=requested_url,
            canonical_url=canonical_url(requested_url),
            final_url=final_url,
            observed_at=observed_at,
            status=status,
            media_type=media_type,
            byte_count=len(body),
            sha256=digest,
            raw_path=relative.as_posix(),
            headers=safe_headers,
        )
        return result, body
