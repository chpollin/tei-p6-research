"""Snapshot the TEI-L mailing-list archive across its three declared parts.

TEI-L moved from the retired Brown University LISTSERV to the Penn State
LISTSERV, so no single interface holds the list's history. The source lock
`sources/locks/tei-l-archive.yaml` declares three parts and this module
implements the two that are machine-retrievable:

``psu``
    Enumerate a declared month interval on the Penn State archive, fetch every
    month index and every message page it lists, and write message metadata.
``wayback-coverage``
    Measure, month by month, whether the Internet Archive holds a capture of the
    retired Brown month index. The run is a measurement; a month without a
    capture is its result, not a failed request.
``wayback-fetch``
    Fetch the captured Brown month indexes and their messages through the
    Wayback Machine, using the ``id_`` form that serves the original bytes. The
    retired archive ran an older LISTSERV whose indexes address a message by its
    byte position inside the monthly log, so both published link forms are read
    and an uncaptured message reaches us as the Wayback error page under HTTP
    200 rather than as a status. A message the Wayback index does not hold at all
    still leaves the row the month index observed, marked ``wayback-index``.

The third lock part, a consortium export for the months neither archive holds,
is an operator action with no interface to call.

A month interval is a declared finite interface rather than an enumerable
object boundary, so a clean run is ``bounded-complete``, which is the strongest
state the community-records family admits (knowledge/data.md, Completion
vocabulary). The gap rule itself stays the shared one in
``tools.corpus.manifest``.

Message bodies and sender identity never leave the local raw store. The
normalized streams carry list, month, message identity, subject, the date the
archive shows, thread pointers and the raw pointer, and no field about the
sender (knowledge/data.md, Rights and redistribution).

Usage:
    python -m tools.corpus.listserv_snapshot psu --from-month 2512 --to-month 2609 \
        --normalized-output corpus/normalized/mail/tei-l-psu.jsonl \
        --manifest-output sources/manifests/YYYY-MM-DD-tei-l-psu.yaml
"""

from __future__ import annotations

import argparse
import html
import re
import time
import urllib.parse
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path
from typing import Any

from tools.corpus.http_store import FetchResult, HttpStore, canonical_url, utc_now
from tools.corpus.manifest import (
    build_manifest,
    read_jsonl,
    report_status,
    sha256_file,
    status_from,
    write_jsonl,
    write_yaml,
)

SOURCE_ID = "tei-l-archive"
ADAPTER = "tools.corpus.listserv_snapshot"
PSU_ARCHIVE = "https://lists.psu.edu/cgi-bin/wa"
BROWN_ARCHIVE = "https://listserv.brown.edu/cgi-bin/wa"
CDX_ENDPOINT = "https://web.archive.org/cdx/search/cdx"
WAYBACK_PREFIX = "https://web.archive.org/web"
BOUNDED_COMPLETE = "bounded-complete"

RIGHTS_EXCEPTIONS = [
    "Message bodies and sender identity remain in local content-addressed raw storage.",
    "The normalized stream carries list, month, message identity, subject, date, "
    "thread pointers, and raw pointers only.",
    "TEI-L posts are user-generated content; redistribution stays metadata and links "
    "until per-item rights review.",
]

# LISTSERV writes the year of a month label with two digits. This list's archive
# starts in 1990, so any pivot between 26 and 89 separates its two centuries.
# 60 holds that separation until 2059, when the pivot has to be revisited.
CENTURY_PIVOT = 60

# A measured absence is the result of a coverage run rather than a failure of
# it, so it is recorded as a gap without withdrawing the run's completion claim.
MEASUREMENT_FINDING_CODES = frozenset({"wayback-month-missing"})

# Header fields the normalized stream may carry, mapped to their record field.
# The map is an allowlist: sender, recipient and reply-to fields are absent by
# construction and cannot reach the normalized stream through a parser change.
RETAINED_HEADERS = {
    "subject": "subject",
    "date": "date",
    "content-type": "content_type",
    "in-reply-to": "in_reply_to",
    "message-id": "upstream_message_id",
    "references": "references",
}

MESSAGE_HREF = re.compile(r"[?&]A2=([^;&]+);([0-9a-fA-F]+\.\d{4})")
HREF_ATTRIBUTE = re.compile(r"""(?i)\bhref\s*=\s*["']([^"']+)["']""")
POSITION_HREF = re.compile(r"[?&]P=(\d+)")
MONTH_LABEL = re.compile(r"^\d{4}$")
INDEX_MONTH = re.compile(r"ind(\d{4})")
LIST_PARAMETER = re.compile(r"(?i)([?&]L=)([^&;]+)")
THREAD_ANCHOR = re.compile(r"#(\d+)")
NAVIGATION_NAMES = {"first", "prev", "next", "last"}

# Response fields of a normalized row. A row the index alone supports carries
# them as null, so the absence of a fetch is visible in the row itself.
FETCH_FIELDS = (
    "requested_url",
    "http_status",
    "observed_at",
    "media_type",
    "byte_count",
    "raw_sha256",
    "raw_path",
)

TITLE_TAG = re.compile(r"(?is)<title[^>]*>(.*?)</title>")
WAYBACK_PLACEHOLDER_TITLE = "wayback machine"


def month_ordinal(month: str) -> int:
    """Return a sortable ordinal for a LISTSERV ``yymm`` month label."""

    if not MONTH_LABEL.match(month):
        raise ValueError(f"month must be four digits (yymm): {month!r}")
    year, part = int(month[:2]), int(month[2:])
    if not 1 <= part <= 12:
        raise ValueError(f"month part must be 01 to 12: {month!r}")
    century = 1900 if year >= CENTURY_PIVOT else 2000
    return (century + year) * 12 + part - 1


def ordinal_month(ordinal: int) -> str:
    year, part = divmod(ordinal, 12)
    return f"{year % 100:02d}{part + 1:02d}"


def enumerate_months(first: str, last: str) -> list[str]:
    """Return every month label from ``first`` to ``last``, both included."""

    start, end = month_ordinal(first), month_ordinal(last)
    if start > end:
        raise ValueError(f"from-month {first} lies after to-month {last}")
    return [ordinal_month(value) for value in range(start, end + 1)]


def month_index_url(archive: str, list_name: str, month: str) -> str:
    return f"{archive}?A1=ind{month}&L={list_name}"


def wayback_url(timestamp: str, original: str) -> str:
    """Return the Wayback URL that serves the original bytes without rewriting."""

    return f"{WAYBACK_PREFIX}/{timestamp}id_/{original}"


def list_variants(list_name: str) -> list[str]:
    """Return the list-name spellings the archives used in their URLs."""

    return list(dict.fromkeys([list_name, list_name.lower()]))


def message_url_variants(resolved: str) -> list[str]:
    """Return the spellings under which one message may have been archived.

    The Penn State index publishes message links with a trailing empty ``S``
    parameter that the archive itself drops in other views. The older form
    carries the list name in an ``L`` parameter that the archive wrote in either
    case, so the lower-case spelling is asked for as well. The URL is otherwise
    left exactly as the index published it, because the Wayback index knows a
    message under that spelling and not under a rewritten one.
    """

    forms = [resolved, resolved.removesuffix("&S=")]
    lowered = [
        LIST_PARAMETER.sub(lambda found: found.group(1) + found.group(2).lower(), form)
        for form in forms
    ]
    return list(dict.fromkeys(forms + lowered))


def is_wayback_placeholder(body: bytes) -> bool:
    """Report whether the Wayback Machine served its own page instead of a capture.

    A URL the archive does not hold answers under HTTP 200 with the archive's
    error page, so the absence shows in the body rather than in the status line.
    """

    found = TITLE_TAG.search(body.decode("utf-8", errors="replace"))
    return found is not None and collapse(found.group(1)).lower() == WAYBACK_PLACEHOLDER_TITLE


def bounded_status(gaps: list[dict[str, Any]]) -> str:
    """Return the run status of a declared finite interface.

    The shared gap rule decides; only the label for a clean run differs, because
    a month interval is declared rather than enumerated from the interface.
    """

    status = status_from(gaps)
    return BOUNDED_COMPLETE if status == "observable-complete" else status


def measurement_status(gaps: list[dict[str, Any]]) -> str:
    """Return the status of a coverage measurement, ignoring measured absences."""

    return bounded_status([gap for gap in gaps if gap["code"] not in MEASUREMENT_FINDING_CODES])


def report_bounded_status(manifest: dict[str, Any], detail: str) -> int:
    """Print the shared result line, treating a bounded run as a clean exit."""

    exit_code = report_status(manifest, detail)
    return 0 if manifest["status"] == BOUNDED_COMPLETE else exit_code


def collapse(value: str) -> str:
    return " ".join(value.split())


@dataclass(frozen=True)
class Cell:
    text: str
    links: tuple[tuple[str, str], ...]


class TableRowParser(HTMLParser):
    """Collect table rows as cells of collapsed text and anchor text/href pairs.

    LISTSERV nests tables several levels deep and does not always close a row, so
    a pending row is flushed whenever a row or a table starts or ends rather than
    on ``</tr>`` alone.
    """

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.rows: list[list[Cell]] = []
        self._text: list[list[str]] = []
        self._links: list[list[tuple[str, str]]] = []
        self._href: str | None = None
        self._anchor: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "tr":
            self.flush_pending()
        elif tag in {"td", "th"}:
            self._text.append([])
            self._links.append([])
        elif tag == "a":
            self._close_anchor()
            self._href = dict(attrs).get("href")
            self._anchor = []
        elif tag == "br" and self._text:
            self._text[-1].append(" ")

    def handle_data(self, data: str) -> None:
        if self._text:
            self._text[-1].append(data)
        if self._href is not None:
            self._anchor.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag == "a":
            self._close_anchor()
        elif tag in {"tr", "table"}:
            self.flush_pending()

    def close(self) -> None:
        super().close()
        self.flush_pending()

    def flush_pending(self) -> None:
        self._close_anchor()
        if self._text:
            self.rows.append(
                [
                    Cell(collapse("".join(chunks)), tuple(links))
                    for chunks, links in zip(self._text, self._links, strict=True)
                ]
            )
        self._text = []
        self._links = []

    def _close_anchor(self) -> None:
        if self._href is None:
            return
        if self._links:
            self._links[-1].append((collapse("".join(self._anchor)), self._href))
        self._href = None
        self._anchor = []


def parse_rows(body: bytes) -> list[list[Cell]]:
    """Return the table rows of an archive page, keeping what parsed before a failure."""

    parser = TableRowParser()
    try:
        parser.feed(body.decode("utf-8", errors="replace"))
        parser.close()
    except (AssertionError, ValueError):
        # Legacy archive pages carry SGML declarations Python's HTML parser
        # rejects. What parsed stays usable, and the month-index reader
        # reconciles the rows against a plain href scan.
        parser.flush_pending()
    return parser.rows


def message_from_href(href: str) -> tuple[str, str, str] | None:
    """Return list, message id and message URL for one archive link.

    LISTSERV published two message-link forms. The Penn State archive addresses a
    message by list name and hexadecimal id (``A2=TEI-L;<hex>.<yymm>``). The
    retired Brown archive ran an older LISTSERV that addresses it by month index
    and byte position inside the monthly log
    (``A2=ind<yymm>&L=TEI-L&P=<n>``), whose identity becomes ``P<n>.<yymm>`` so
    that both forms carry the month the boundary check reads. The sort and view
    links of an index address the index itself through ``A1=`` and match neither
    form. The href is read as it stands in the markup, so a link the raw scan
    finds with its character references intact yields the same URL and the same
    identity as the one the row reader takes from the parsed attribute.
    """

    url = urllib.parse.unquote(html.unescape(href))
    listed = MESSAGE_HREF.search(url)
    if listed:
        return listed.group(1), listed.group(2), url
    query = dict(urllib.parse.parse_qsl(urllib.parse.urlsplit(url).query))
    month = INDEX_MONTH.fullmatch(query.get("A2", ""))
    position = query.get("P", "")
    list_name = query.get("L", "")
    if month is None or not list_name or not position.isdigit():
        return None
    return list_name, f"P{position}.{month.group(1)}", url


def scan_message_links(body: bytes) -> list[tuple[str, str, str]]:
    """Return every message link on a page as list, message id and URL."""

    found: list[tuple[str, str, str]] = []
    for match in HREF_ATTRIBUTE.finditer(body.decode("utf-8", errors="replace")):
        message = message_from_href(match.group(1))
        if message is not None:
            found.append(message)
    return found


def _row_message(row: list[Cell]) -> tuple[str, str, str, str] | None:
    """Return list, message id, URL and anchor text of the first message link."""

    for cell in row:
        for text, href in cell.links:
            message = message_from_href(href)
            if message is not None:
                return (*message, text)
    return None


def _row_thread(row: list[Cell]) -> str:
    """Return the thread ordinal a grouping row of the older index opens.

    That archive opens each thread with a row whose anchor names the thread's
    place in the index, and the message rows that follow belong to it. The Penn
    State index carries no such row, so its entries stay ungrouped.
    """

    for cell in row:
        for _text, href in cell.links:
            match = THREAD_ANCHOR.fullmatch(href)
            if match:
                return match.group(1)
    return ""


def parse_month_index(body: bytes, month: str, base_url: str) -> list[dict[str, str]]:
    """Return one entry per message the month index lists.

    Both archive generations open a row with subject, sender and date in that
    order, so the subject comes from the message anchor and the date from the
    third cell, and the older archive's trailing size cell is ignored along with
    the sender cell, which is never read. Either published link form identifies a
    message (``message_from_href``), and the grouping rows of the older index
    give each message the thread it was filed under. A message whose row cannot
    be read is still returned from a plain href scan, ungrouped, so a table
    surprise never drops a message from the boundary.
    """

    suffix = f".{month}"
    listed: dict[str, dict[str, str]] = {}
    thread = ""
    for row in parse_rows(body):
        found = _row_message(row)
        if found is None:
            thread = _row_thread(row) or thread
            continue
        list_name, message_id, href, subject = found
        if not message_id.endswith(suffix):
            continue
        listed[message_id] = {
            "list": list_name,
            "month": month,
            "message_id": message_id,
            "url": urllib.parse.urljoin(base_url, href),
            "index_subject": subject,
            "index_date": row[2].text if len(row) > 2 else "",
            "index_thread": thread,
        }
    for list_name, message_id, href in scan_message_links(body):
        if message_id.endswith(suffix) and message_id not in listed:
            listed[message_id] = {
                "list": list_name,
                "month": month,
                "message_id": message_id,
                "url": urllib.parse.urljoin(base_url, href),
                "index_subject": "",
                "index_date": "",
                "index_thread": "",
            }
    return [listed[key] for key in sorted(listed)]


def _navigation(cell: Cell) -> dict[str, str]:
    """Return the topic navigation pointers a message page exposes, by position."""

    pointers: dict[str, str] = {}
    for text, href in cell.links:
        name = re.sub(r"[^a-z]", "", text.lower())
        match = POSITION_HREF.search(href)
        if name in NAVIGATION_NAMES and match:
            pointers[name] = match.group(1)
    return pointers


def parse_message(body: bytes) -> dict[str, Any]:
    """Return the retained header fields and the thread pointers of a message page.

    LISTSERV lays the header block out as label and value rows and the thread
    navigation as a ``Topic:`` row of first, previous, next and last links. Only
    the fields in ``RETAINED_HEADERS`` are kept, so the sender rows are dropped
    here and cannot be carried forward by a later step.
    """

    headers: dict[str, str] = {}
    thread: dict[str, str] = {}
    for row in parse_rows(body):
        if len(row) < 2:
            continue
        label = row[0].text.rstrip(":").strip().lower()
        field = RETAINED_HEADERS.get(label)
        if field and row[1].text:
            headers.setdefault(field, row[1].text)
        if label == "topic":
            thread.update(_navigation(row[1]))
    return {"headers": headers, "thread_position": thread}


def fetch_page(
    store: HttpStore, url: str, delay_seconds: float
) -> tuple[FetchResult | None, bytes, str | None]:
    """Fetch one archive page, returning the failure reason instead of raising."""

    try:
        result, body = store.fetch(url)
    except RuntimeError as error:
        return None, b"", str(error)
    finally:
        if delay_seconds:
            time.sleep(delay_seconds)
    if result.status >= 400:
        return result, body, f"HTTP {result.status}"
    return result, body, None


def cdx_url(target: str) -> str:
    """Return the CDX query that lists the captures of one original URL."""

    query = urllib.parse.urlencode(
        {"url": target, "output": "json", "fl": "timestamp,original,statuscode"}
    )
    return f"{CDX_ENDPOINT}?{query}"


def cdx_captures(
    store: HttpStore, target: str, delay_seconds: float
) -> tuple[list[dict[str, str]], str | None]:
    """Return the captures the Wayback CDX index reports for one URL."""

    try:
        payload, _record = store.fetch_json(cdx_url(target))
    except RuntimeError as error:
        return [], str(error)
    finally:
        if delay_seconds:
            time.sleep(delay_seconds)
    if not isinstance(payload, list) or len(payload) < 2:
        return [], None
    header = [str(name) for name in payload[0]]
    # A short or long row is tolerated; the CDX index has added fields before.
    return [
        dict(zip(header, [str(value) for value in row], strict=False)) for row in payload[1:]
    ], None


def first_captures(
    store: HttpStore, targets: list[str], delay_seconds: float
) -> tuple[list[dict[str, str]], list[str], str | None]:
    """Query each URL spelling in turn and return the first non-empty capture list."""

    failure: str | None = None
    tried: list[str] = []
    for target in targets:
        tried.append(target)
        captures, error = cdx_captures(store, target, delay_seconds)
        if error is not None:
            failure = error
            continue
        if captures:
            return captures, tried, None
    return [], tried, failure


def preferred_capture(captures: list[dict[str, str]]) -> dict[str, str] | None:
    """Return the capture worth fetching from a CDX listing.

    A listing mixes captures the crawl served with captures of an error page, so
    the newest row is not necessarily a usable one. The newest served capture
    wins, and the newest row decides only where the crawl never served the URL.
    """

    served = [row for row in captures if row.get("statuscode") == "200"]
    return max(served or captures, key=lambda row: row.get("timestamp", ""), default=None)


def fetch_fields(result: FetchResult | None) -> dict[str, Any]:
    """Return what the response contributes to a row, all null where none was made."""

    if result is None:
        return dict.fromkeys(FETCH_FIELDS)
    return {
        "requested_url": result.canonical_url,
        "http_status": result.status,
        "observed_at": result.observed_at,
        "media_type": result.media_type,
        "byte_count": result.byte_count,
        "raw_sha256": result.sha256,
        "raw_path": result.raw_path,
    }


def message_record(
    entry: dict[str, str],
    parsed: dict[str, Any],
    result: FetchResult | None,
    *,
    via: str,
    extra: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Assemble one normalized message row.

    The row carries message identity, the subject and date the archive shows,
    thread pointers and the raw pointer. Nothing about the sender enters it; the
    sender stays in the raw page under the rights rule in knowledge/data.md. A
    row the month index alone supports keeps the same shape and states the
    absence of a response through null response fields.
    """

    headers = parsed["headers"]
    record: dict[str, Any] = {
        "schema_version": 1,
        "source_id": SOURCE_ID,
        "object_type": "mailing-list-message",
        "via": via,
        "list": entry["list"],
        "month": entry["month"],
        "message_id": entry["message_id"],
        "subject": headers.get("subject") or entry["index_subject"],
        "date": headers.get("date") or entry["index_date"],
        "index_subject": entry["index_subject"],
        "index_date": entry["index_date"],
        "content_type": headers.get("content_type"),
        "in_reply_to": headers.get("in_reply_to"),
        "upstream_message_id": headers.get("upstream_message_id"),
        "references": headers.get("references"),
        "thread_position": parsed["thread_position"] or None,
        "archive_url": entry["url"],
        **fetch_fields(result),
    }
    record.update(extra or {})
    return record


def wayback_fields(
    entry: dict[str, str], *, capture_timestamp: str | None, message_capture: str | None
) -> dict[str, Any]:
    """Return what a row owes to the Wayback Machine and to the month index.

    Both kinds of row of a wayback run carry these fields, so a row the index
    alone supports differs from a fetched one in their values and not in shape.
    """

    return {
        "capture_timestamp": capture_timestamp,
        "month_capture_timestamp": entry["month_capture_timestamp"],
        "wayback_url": message_capture,
        "index_thread": entry["index_thread"] or None,
    }


def bound_messages(
    listed: list[dict[str, str]], max_messages: int | None, gaps: list[dict[str, Any]]
) -> list[dict[str, str]]:
    """Apply the smoke-run bound and record a gap only where it actually binds."""

    if max_messages is None or len(listed) <= max_messages:
        return listed
    gaps.append(
        {
            "code": "max-messages-limit",
            "max_messages": max_messages,
            "messages_listed": len(listed),
            "messages_not_fetched": len(listed) - max_messages,
        }
    )
    return listed[:max_messages]


def snapshot_psu(
    *,
    list_name: str,
    archive: str,
    first_month: str,
    last_month: str,
    delay_seconds: float,
    max_messages: int | None,
    raw_root: Path,
    normalized_output: Path,
    manifest_output: Path,
) -> dict[str, Any]:
    """Snapshot a declared month interval of the Penn State TEI-L archive."""

    started_at = utc_now()
    store = HttpStore(raw_root)
    months = enumerate_months(first_month, last_month)
    gaps: list[dict[str, Any]] = []
    listed: list[dict[str, str]] = []
    records: list[dict[str, Any]] = []
    responses = 0
    indexed_months = 0

    for month in months:
        index_url = month_index_url(archive, list_name, month)
        result, body, failure = fetch_page(store, index_url, delay_seconds)
        if result is not None:
            responses += 1
        if failure is not None:
            gaps.append(
                {
                    "code": "month-index-failed",
                    "month": month,
                    "url": canonical_url(index_url),
                    "detail": failure,
                }
            )
            continue
        indexed_months += 1
        listed.extend(parse_month_index(body, month, result.final_url))

    for entry in bound_messages(listed, max_messages, gaps):
        result, body, failure = fetch_page(store, entry["url"], delay_seconds)
        if result is not None:
            responses += 1
        if failure is not None:
            gaps.append(
                {
                    "code": "message-fetch-failed",
                    "month": entry["month"],
                    "message_id": entry["message_id"],
                    "url": canonical_url(entry["url"]),
                    "detail": failure,
                }
            )
            continue
        parsed = parse_message(body)
        if not parsed["headers"]:
            gaps.append(
                {
                    "code": "message-parse-failed",
                    "month": entry["month"],
                    "message_id": entry["message_id"],
                    "url": canonical_url(entry["url"]),
                }
            )
        records.append(message_record(entry, parsed, result, via="psu"))

    records.sort(key=lambda row: (str(row["month"]), str(row["message_id"])))
    write_jsonl(normalized_output, records)
    manifest = build_manifest(
        run_id=manifest_output.stem,
        source_id=SOURCE_ID,
        adapter=ADAPTER,
        started_at=started_at,
        finished_at=utc_now(),
        status=bounded_status(gaps),
        requests={
            "archive": archive,
            "list": list_name,
            "from_month": first_month,
            "to_month": last_month,
            "months": months,
            "delay_seconds": delay_seconds,
            "max_messages": max_messages,
        },
        objects=[
            {
                "kind": "tei-l-message-metadata",
                "path": normalized_output.as_posix(),
                "sha256": sha256_file(normalized_output),
            }
        ],
        counts={
            "months_requested": len(months),
            "months_indexed": indexed_months,
            "messages_listed": len(listed),
            "messages": len(records),
            "http_responses": responses,
            "gaps": len(gaps),
        },
        gaps=gaps,
        rights_exceptions=RIGHTS_EXCEPTIONS,
        extra={
            "scope": {
                "boundary": "declared-month-interval-on-the-penn-state-archive",
                "status_applies_to": "requests.months",
                "completion_rule": (
                    "Every message the month indexes of the declared interval list, "
                    "retrieved or recorded as a gap."
                ),
            }
        },
    )
    write_yaml(manifest_output, manifest)
    return manifest


def measure_wayback_coverage(
    *,
    list_name: str,
    archive: str,
    first_month: str,
    last_month: str,
    delay_seconds: float,
    raw_root: Path,
    normalized_output: Path,
    manifest_output: Path,
) -> dict[str, Any]:
    """Measure which months of the retired archive the Wayback Machine captured."""

    started_at = utc_now()
    store = HttpStore(raw_root)
    months = enumerate_months(first_month, last_month)
    gaps: list[dict[str, Any]] = []
    records: list[dict[str, Any]] = []

    for month in months:
        targets = [month_index_url(archive, name, month) for name in list_variants(list_name)]
        captures, tried, failure = first_captures(store, targets, delay_seconds)
        if failure is not None and not captures:
            gaps.append({"code": "wayback-cdx-query-failed", "month": month, "detail": failure})
            continue
        newest = preferred_capture(captures)
        records.append(
            {
                "schema_version": 1,
                "source_id": SOURCE_ID,
                "object_type": "wayback-month-coverage",
                "list": list_name,
                "month": month,
                "queried_urls": tried,
                "captured": bool(captures),
                "capture_count": len(captures),
                "latest_capture": newest["timestamp"] if newest else None,
                "latest_capture_original": newest["original"] if newest else None,
                "latest_capture_status": newest.get("statuscode") if newest else None,
            }
        )
        if not captures:
            gaps.append({"code": "wayback-month-missing", "month": month, "queried_urls": tried})

    records.sort(key=lambda row: str(row["month"]))
    write_jsonl(normalized_output, records)
    captured = sum(1 for row in records if row["captured"])
    manifest = build_manifest(
        run_id=manifest_output.stem,
        source_id=SOURCE_ID,
        adapter=ADAPTER,
        started_at=started_at,
        finished_at=utc_now(),
        status=measurement_status(gaps),
        requests={
            "cdx_endpoint": CDX_ENDPOINT,
            "archive": archive,
            "list": list_name,
            "list_spellings": list_variants(list_name),
            "from_month": first_month,
            "to_month": last_month,
            "months": months,
            "delay_seconds": delay_seconds,
        },
        objects=[
            {
                "kind": "tei-l-wayback-month-coverage",
                "path": normalized_output.as_posix(),
                "sha256": sha256_file(normalized_output),
            }
        ],
        counts={
            "months_requested": len(months),
            "months_measured": len(records),
            "months_captured": captured,
            "months_missing": len(records) - captured,
            "months_without_disposition": len(months) - len(records),
            "captures_total": sum(int(row["capture_count"]) for row in records),
            "gaps": len(gaps),
        },
        gaps=gaps,
        rights_exceptions=RIGHTS_EXCEPTIONS,
        extra={
            "scope": {
                "boundary": "declared-month-interval-measured-against-the-wayback-cdx-index",
                "status_applies_to": "requests.months",
                "completion_rule": (
                    "Every month of the declared interval received a capture "
                    "disposition. A month without a capture is a recorded result of "
                    "the measurement, not an unfinished request."
                ),
            }
        },
    )
    write_yaml(manifest_output, manifest)
    return manifest


def snapshot_wayback(
    *,
    coverage_input: Path,
    months: list[str],
    delay_seconds: float,
    max_messages: int | None,
    raw_root: Path,
    normalized_output: Path,
    manifest_output: Path,
) -> dict[str, Any]:
    """Fetch the captured months of the retired archive through the Wayback Machine."""

    started_at = utc_now()
    store = HttpStore(raw_root)
    coverage = [row for row in read_jsonl(coverage_input) if row.get("captured")]
    if months:
        selected = set(months)
        coverage = [row for row in coverage if str(row["month"]) in selected]
    coverage.sort(key=lambda row: str(row["month"]))
    gaps: list[dict[str, Any]] = []
    listed: list[dict[str, str]] = []
    records: list[dict[str, Any]] = []
    responses = 0
    indexed_months = 0
    missing_messages = 0
    index_only_messages = 0

    for row in coverage:
        month = str(row["month"])
        timestamp = str(row["latest_capture"])
        original = str(row["latest_capture_original"])
        index_url = wayback_url(timestamp, original)
        result, body, failure = fetch_page(store, index_url, delay_seconds)
        if result is not None:
            responses += 1
        if failure is not None:
            gaps.append(
                {
                    "code": "month-index-failed",
                    "month": month,
                    "url": canonical_url(index_url),
                    "capture_timestamp": timestamp,
                    "detail": failure,
                }
            )
            continue
        indexed_months += 1
        for entry in parse_month_index(body, month, original):
            entry["month_capture_timestamp"] = timestamp
            listed.append(entry)

    for entry in bound_messages(listed, max_messages, gaps):
        targets = message_url_variants(entry["url"])
        captures, tried, failure = first_captures(store, targets, delay_seconds)
        newest = preferred_capture(captures)
        if newest is None:
            # The Wayback index holds the month but not this message. What the
            # month index observed is the whole record then, so the row states
            # the observation and its null response fields state the absence.
            missing_messages += 1
            index_only_messages += 1
            gaps.append(
                {
                    "code": "wayback-message-missing",
                    "month": entry["month"],
                    "message_id": entry["message_id"],
                    "queried_urls": tried,
                    "detail": failure,
                }
            )
            records.append(
                message_record(
                    entry,
                    {"headers": {}, "thread_position": {}},
                    None,
                    via="wayback-index",
                    extra=wayback_fields(entry, capture_timestamp=None, message_capture=None),
                )
            )
            continue
        message_capture = wayback_url(newest["timestamp"], newest["original"])
        result, body, fetch_failure = fetch_page(store, message_capture, delay_seconds)
        if result is not None:
            responses += 1
        if fetch_failure is not None:
            gaps.append(
                {
                    "code": "message-fetch-failed",
                    "month": entry["month"],
                    "message_id": entry["message_id"],
                    "url": canonical_url(message_capture),
                    "capture_timestamp": newest["timestamp"],
                    "detail": fetch_failure,
                }
            )
            continue
        parsed = parse_message(body)
        if is_wayback_placeholder(body) or not parsed["headers"]:
            # The archive answers an uncaptured message with its own page under
            # HTTP 200, and an older message view may carry no header block the
            # parser recognises. Neither is stored as a message: the page
            # contributes nothing to the row, which keeps the index observation
            # and the status of the attempt.
            parsed = {"headers": {}, "thread_position": {}}
            missing_messages += 1
            gaps.append(
                {
                    "code": "wayback-message-missing",
                    "month": entry["month"],
                    "message_id": entry["message_id"],
                    "url": canonical_url(message_capture),
                    "capture_timestamp": newest["timestamp"],
                }
            )
        records.append(
            message_record(
                entry,
                parsed,
                result,
                via="wayback",
                extra=wayback_fields(
                    entry,
                    capture_timestamp=newest["timestamp"],
                    message_capture=message_capture,
                ),
            )
        )

    records.sort(key=lambda row: (str(row["month"]), str(row["message_id"])))
    write_jsonl(normalized_output, records)
    manifest = build_manifest(
        run_id=manifest_output.stem,
        source_id=SOURCE_ID,
        adapter=ADAPTER,
        started_at=started_at,
        finished_at=utc_now(),
        status=bounded_status(gaps),
        requests={
            "coverage_input": coverage_input.as_posix(),
            "cdx_endpoint": CDX_ENDPOINT,
            "wayback_prefix": WAYBACK_PREFIX,
            "months": [str(row["month"]) for row in coverage],
            "month_filter": months,
            "delay_seconds": delay_seconds,
            "max_messages": max_messages,
        },
        objects=[
            {
                "kind": "tei-l-wayback-message-metadata",
                "path": normalized_output.as_posix(),
                "sha256": sha256_file(normalized_output),
            }
        ],
        counts={
            "months_requested": len(coverage),
            "months_indexed": indexed_months,
            "messages_listed": len(listed),
            "messages": len(records),
            "messages_missing": missing_messages,
            "messages_index_only": index_only_messages,
            "http_responses": responses,
            "gaps": len(gaps),
        },
        gaps=gaps,
        rights_exceptions=RIGHTS_EXCEPTIONS,
        extra={
            "scope": {
                "boundary": "captured-brown-months-served-through-the-wayback-machine",
                "status_applies_to": "requests.months",
                "completion_rule": (
                    "Every message the captured month indexes list, retrieved from a "
                    "capture or recorded as a gap."
                ),
            }
        },
    )
    write_yaml(manifest_output, manifest)
    return manifest


def add_output_arguments(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--raw-root", type=Path, default=Path("corpus/raw"))
    parser.add_argument("--normalized-output", type=Path, required=True)
    parser.add_argument("--manifest-output", type=Path, required=True)
    parser.add_argument("--delay-seconds", type=float, default=1.0)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="listserv_snapshot",
        description="Snapshot the TEI-L mailing-list archive in its three declared parts.",
    )
    commands = parser.add_subparsers(dest="command", required=True)

    psu = commands.add_parser("psu", help="Snapshot a month interval of the Penn State archive")
    psu.add_argument("--archive", default=PSU_ARCHIVE)
    psu.add_argument("--list", dest="list_name", default="TEI-L")
    psu.add_argument("--from-month", required=True)
    psu.add_argument("--to-month", required=True)
    psu.add_argument("--max-messages", type=int)
    add_output_arguments(psu)

    coverage = commands.add_parser(
        "wayback-coverage", help="Measure Wayback captures of the retired Brown month indexes"
    )
    coverage.add_argument("--archive", default=BROWN_ARCHIVE)
    coverage.add_argument("--list", dest="list_name", default="TEI-L")
    coverage.add_argument("--from-month", required=True)
    coverage.add_argument("--to-month", required=True)
    add_output_arguments(coverage)

    fetch = commands.add_parser(
        "wayback-fetch", help="Fetch captured Brown months through the Wayback Machine"
    )
    fetch.add_argument("--coverage-input", type=Path, required=True)
    fetch.add_argument("--month", action="append", default=[], dest="months")
    fetch.add_argument("--max-messages", type=int)
    add_output_arguments(fetch)

    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    if args.delay_seconds < 0:
        raise SystemExit("delay-seconds must be 0 or greater")
    if getattr(args, "max_messages", None) is not None and args.max_messages < 1:
        raise SystemExit("max-messages must be 1 or greater")
    try:
        if args.command == "psu":
            manifest = snapshot_psu(
                list_name=args.list_name,
                archive=args.archive,
                first_month=args.from_month,
                last_month=args.to_month,
                delay_seconds=args.delay_seconds,
                max_messages=args.max_messages,
                raw_root=args.raw_root,
                normalized_output=args.normalized_output,
                manifest_output=args.manifest_output,
            )
            detail = f"{manifest['counts']['messages']} messages"
        elif args.command == "wayback-coverage":
            manifest = measure_wayback_coverage(
                list_name=args.list_name,
                archive=args.archive,
                first_month=args.from_month,
                last_month=args.to_month,
                delay_seconds=args.delay_seconds,
                raw_root=args.raw_root,
                normalized_output=args.normalized_output,
                manifest_output=args.manifest_output,
            )
            detail = (
                f"{manifest['counts']['months_captured']} months captured, "
                f"{manifest['counts']['months_missing']} missing"
            )
        else:
            manifest = snapshot_wayback(
                coverage_input=args.coverage_input,
                months=args.months,
                delay_seconds=args.delay_seconds,
                max_messages=args.max_messages,
                raw_root=args.raw_root,
                normalized_output=args.normalized_output,
                manifest_output=args.manifest_output,
            )
            detail = (
                f"{manifest['counts']['messages']} messages, "
                f"{manifest['counts']['messages_missing']} without a capture"
            )
    except ValueError as error:
        raise SystemExit(str(error)) from error
    return report_bounded_status(manifest, f"{detail}, {manifest['counts']['gaps']} gaps")


if __name__ == "__main__":
    raise SystemExit(main())
