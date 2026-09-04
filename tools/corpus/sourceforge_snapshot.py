"""Snapshot legacy SourceForge trackers with exhaustive API pagination."""

from __future__ import annotations

import argparse
import json
import time
import urllib.parse
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any

from tools.corpus.http_store import HttpStore, canonical_url, utc_now
from tools.corpus.manifest import sha256_file, write_jsonl, write_yaml


def paged_url(base: str, page: int, limit: int = 100) -> str:
    return f"{base.rstrip('/')}?{urllib.parse.urlencode({'limit': limit, 'page': page})}"


def public_ticket_metadata(ticket: dict[str, Any], tracker: str) -> dict[str, Any]:
    """Return searchable metadata while keeping prose and comment bodies raw-only."""

    thread = ticket.get("discussion_thread") or {}
    attachments = ticket.get("attachments") or []
    return {
        "schema_version": 1,
        "source_id": "tei-legacy-sourceforge",
        "object_type": "ticket",
        "tracker": tracker,
        "ticket_num": ticket.get("ticket_num"),
        "object_id": ticket.get("_id"),
        "summary": ticket.get("summary"),
        "status": ticket.get("status"),
        "created_date": ticket.get("created_date"),
        "modified_date": ticket.get("mod_date"),
        "labels": ticket.get("labels") or [],
        "reported_by": ticket.get("reported_by"),
        "assigned_to": ticket.get("assigned_to"),
        "private": bool(ticket.get("private", False)),
        "related_artifacts": ticket.get("related_artifacts") or [],
        "attachments": [
            {
                key: attachment.get(key)
                for key in ("url", "filename", "bytes", "type")
                if attachment.get(key) is not None
            }
            for attachment in attachments
            if isinstance(attachment, dict)
        ],
        "discussion_thread_id": thread.get("_id"),
        "discussion_url": ticket.get("discussion_thread_url"),
        "body_present_in_raw": bool(ticket.get("description")),
    }


def fetch_json(store: HttpStore, url: str) -> tuple[dict[str, Any], dict[str, Any]]:
    result, body = store.fetch(url)
    if result.status >= 400:
        raise RuntimeError(f"HTTP {result.status} for {canonical_url(url)}")
    try:
        data = json.loads(body)
    except json.JSONDecodeError as error:
        raise RuntimeError(f"invalid JSON for {canonical_url(url)}: {error}") from error
    return data, result.as_record()


def enumerate_tracker(store: HttpStore, base: str) -> tuple[list[int], list[dict[str, Any]]]:
    ticket_numbers: list[int] = []
    responses: list[dict[str, Any]] = []
    page = 0
    expected: int | None = None
    while expected is None or len(ticket_numbers) < expected:
        data, response = fetch_json(store, paged_url(base, page))
        rows = data.get("tickets") or []
        if expected is None:
            expected = int(data.get("count", 0))
        responses.append(response)
        ticket_numbers.extend(int(row["ticket_num"]) for row in rows)
        if not rows:
            break
        page += 1
    return sorted(set(ticket_numbers)), responses


def fetch_thread(
    store: HttpStore, url: str, delay_seconds: float
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    posts: list[dict[str, Any]] = []
    responses: list[dict[str, Any]] = []
    page = 0
    while True:
        data, response = fetch_json(store, paged_url(url, page))
        if delay_seconds:
            time.sleep(delay_seconds)
        responses.append(response)
        thread = data.get("thread") or {}
        rows = thread.get("posts") or []
        posts.extend(rows)
        if len(rows) < int(thread.get("limit") or 100):
            break
        page += 1
    return posts, responses


def fetch_ticket(
    base: str,
    tracker: str,
    ticket_num: int,
    raw_root: Path,
    delay_seconds: float,
) -> dict[str, Any]:
    store = HttpStore(raw_root)
    data, detail_response = fetch_json(store, f"{base.rstrip('/')}/{ticket_num}")
    if delay_seconds:
        time.sleep(delay_seconds)
    ticket = data.get("ticket") or {}
    posts: list[dict[str, Any]] = []
    thread_responses: list[dict[str, Any]] = []
    if ticket.get("discussion_thread_url"):
        posts, thread_responses = fetch_thread(
            store, str(ticket["discussion_thread_url"]), delay_seconds
        )
    record = public_ticket_metadata(ticket, tracker)
    record["comment_count"] = len(posts)
    record["comment_metadata"] = [
        {
            key: post.get(key)
            for key in ("_id", "timestamp", "author", "last_edited")
            if post.get(key) is not None
        }
        for post in posts
        if isinstance(post, dict)
    ]
    record["raw_responses"] = [
        {
            key: response.get(key)
            for key in (
                "canonical_url",
                "final_url",
                "observed_at",
                "status",
                "media_type",
                "byte_count",
                "sha256",
                "raw_path",
            )
        }
        for response in [detail_response, *thread_responses]
    ]
    return {
        "record": record,
        "detail_response": detail_response,
        "thread_responses": thread_responses,
    }


def snapshot(
    *,
    source_id: str,
    project_url: str,
    trackers: dict[str, str],
    workers: int,
    raw_root: Path,
    normalized_output: Path,
    manifest_output: Path,
    resume_from: Path | None = None,
    delay_seconds: float = 0.0,
    refresh_missing_raw_links: bool = False,
) -> dict[str, object]:
    started_at = utc_now()
    store = HttpStore(raw_root)
    project, project_response = fetch_json(store, project_url)
    records: list[dict[str, Any]] = []
    if resume_from is not None and resume_from.exists():
        records = [
            json.loads(line)
            for line in resume_from.read_text(encoding="utf-8").splitlines()
            if line
        ]
    resumed_count = len(records)
    records_by_key = {
        (str(row["tracker"]), int(row["ticket_num"])): row for row in records
    }
    existing = {
        key
        for key, row in records_by_key.items()
        if not refresh_missing_raw_links or bool(row.get("raw_responses"))
    }
    response_count = 1
    gaps: list[dict[str, Any]] = []
    enumerated: dict[str, list[int]] = {}

    for tracker, base in trackers.items():
        try:
            enumerated[tracker], page_responses = enumerate_tracker(store, base)
            response_count += len(page_responses)
        except RuntimeError as error:
            enumerated[tracker] = []
            gaps.append({"code": "tracker-enumeration-failed", "tracker": tracker, "detail": str(error)})

    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {
            executor.submit(
                fetch_ticket,
                trackers[tracker],
                tracker,
                number,
                raw_root,
                delay_seconds,
            ): (tracker, number)
            for tracker, numbers in enumerated.items()
            for number in numbers
            if (tracker, number) not in existing
        }
        for future in as_completed(futures):
            tracker, number = futures[future]
            try:
                fetched = future.result()
            except RuntimeError as error:
                gaps.append(
                    {"code": "ticket-fetch-failed", "tracker": tracker, "ticket_num": number, "detail": str(error)}
                )
                continue
            records_by_key[(tracker, number)] = fetched["record"]
            response_count += 1 + len(fetched["thread_responses"])

    records = list(records_by_key.values())
    records.sort(key=lambda row: (str(row["tracker"]), int(row["ticket_num"])))
    write_jsonl(normalized_output, records)
    expected = sum(len(numbers) for numbers in enumerated.values())
    if len(records) != expected:
        gaps.append({"code": "ticket-count-mismatch", "expected": expected, "observed": len(records)})
    status = "observable-complete" if not gaps else "partial"
    manifest: dict[str, object] = {
        "schema_version": 1,
        "run_id": manifest_output.stem,
        "source_id": source_id,
        "started_at": started_at,
        "finished_at": utc_now(),
        "status": status,
        "adapter": {"name": "tools.corpus.sourceforge_snapshot", "version": 1},
        "requests": {
            "project": canonical_url(project_url),
            "trackers": {name: canonical_url(url) for name, url in trackers.items()},
            "workers": workers,
            "resume_from": resume_from.as_posix() if resume_from else None,
            "delay_seconds": delay_seconds,
            "refresh_missing_raw_links": refresh_missing_raw_links,
        },
        "project": {
            "shortname": project.get("shortname"),
            "name": project.get("name"),
            "status": project.get("status"),
            "moved_to_url": project.get("moved_to_url"),
        },
        "objects": [
            {
                "kind": "sourceforge-ticket-metadata",
                "path": normalized_output.as_posix(),
                "sha256": sha256_file(normalized_output),
            }
        ],
        "counts": {
            "tickets_by_tracker": {name: len(numbers) for name, numbers in enumerated.items()},
            "tickets": len(records),
            "tickets_reused_from_prior_run": resumed_count,
            "comments": sum(int(record["comment_count"]) for record in records),
            "http_responses": response_count,
            "gaps": len(gaps),
        },
        "gaps": gaps,
        "rights_exceptions": [
            "Ticket and discussion prose remain in local content-addressed raw storage.",
            "Normalized output contains metadata, summaries, links, and relationship identifiers only.",
        ],
    }
    write_yaml(manifest_output, manifest)
    return manifest


def parse_tracker(value: str) -> tuple[str, str]:
    try:
        name, url = value.split("=", 1)
    except ValueError as error:
        raise argparse.ArgumentTypeError("tracker must be NAME=URL") from error
    if not name or not url:
        raise argparse.ArgumentTypeError("tracker must be NAME=URL")
    return name, url


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-id", default="tei-legacy-sourceforge")
    parser.add_argument("--project-url", default="https://sourceforge.net/rest/p/tei")
    parser.add_argument("--tracker", action="append", type=parse_tracker, required=True)
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--resume-from", type=Path)
    parser.add_argument("--delay-seconds", type=float, default=0.0)
    parser.add_argument("--refresh-missing-raw-links", action="store_true")
    parser.add_argument("--raw-root", type=Path, default=Path("corpus/raw"))
    parser.add_argument("--normalized-output", type=Path, required=True)
    parser.add_argument("--manifest-output", type=Path, required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.workers < 1 or args.workers > 32 or args.delay_seconds < 0:
        raise SystemExit("workers must be between 1 and 32")
    manifest = snapshot(
        source_id=args.source_id,
        project_url=args.project_url,
        trackers=dict(args.tracker),
        workers=args.workers,
        raw_root=args.raw_root,
        normalized_output=args.normalized_output,
        manifest_output=args.manifest_output,
        resume_from=args.resume_from,
        delay_seconds=args.delay_seconds,
        refresh_missing_raw_links=args.refresh_missing_raw_links,
    )
    print(
        f"{manifest['status']}: {manifest['source_id']} -> "
        f"{manifest['counts']['tickets']} tickets, "  # type: ignore[index]
        f"{manifest['counts']['comments']} comments, "  # type: ignore[index]
        f"{manifest['counts']['gaps']} gaps"  # type: ignore[index]
    )
    return 0 if manifest["status"] == "observable-complete" else 2


if __name__ == "__main__":
    raise SystemExit(main())
