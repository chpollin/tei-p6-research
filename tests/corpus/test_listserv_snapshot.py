"""TEI-L archive collector: month boundary, LISTSERV parsing, and the sender rule.

Every fixture page is synthetic markup written for this test in the layouts the
two LISTSERV generations use, the Penn State archive and the retired Brown
archive whose indexes address a message by byte position. Live pages carry
third-party names and addresses and are never copied into the repository, so the
sender in these fixtures is a placeholder whose absence from the normalized
stream is what the rights test actually checks.
"""

import json

import pytest

from tools.corpus import http_store, listserv_snapshot
from tools.corpus.http_store import canonical_url
from tools.corpus.listserv_snapshot import (
    BROWN_ARCHIVE,
    PSU_ARCHIVE,
    cdx_url,
    enumerate_months,
    measure_wayback_coverage,
    message_url_variants,
    month_index_url,
    parse_message,
    parse_month_index,
    preferred_capture,
    snapshot_psu,
    snapshot_wayback,
    wayback_url,
)

LIST = "TEI-L"
SENDER = "Placeholder Sender"
BODY = "Synthetic message body written for this test."
MESSAGES = [
    ("aaaa0001.2512", "Element content model question", "Mon, 1 Dec 2025 09:00:00 +0100"),
    ("bbbb0002.2512", "Re: Element content model question", "Mon, 1 Dec 2025 11:30:00 +0100"),
    ("cccc0003.2512", "Customization workflow report", "Tue, 2 Dec 2025 08:15:00 -0500"),
]


def month_index(entries: list[tuple[str, str, str]], *, subject_link: bool = True) -> bytes:
    """Build a month index in the archive's subject, sender, date table layout."""

    rows = ""
    for position, (message_id, subject, date) in enumerate(entries):
        anchor = (
            f'<a href="/cgi-bin/wa?A2={LIST};{message_id}&S=">{subject}</a>'
            if subject_link
            else f'<span data-href="/cgi-bin/wa?A2={LIST};{message_id}&S=">{subject}</span>'
        )
        rows += (
            '<tr><td class="normalgroup row-l" scope="row">'
            f'<div class="archive forcewrap"><span onmouseover="showDesc()">{anchor}</span></div></td>'
            f'<td class="normalgroup row-l"><div class="archive forcewrap">{SENDER} {position}</div></td>'
            f'<td class="normalgroup nowrap row-l"><div class="archive forcewrap">{date}</div></td></tr>'
        )
    return (
        f'<html><body><table id="{LIST}-a1-table"><thead><tr>'
        "<th>Subject</th><th>From</th><th>Date</th></tr></thead>"
        f"<tbody>{rows}</tbody></table></body></html>"
    ).encode()


def message_page(message_id: str, subject: str, date: str, *, in_thread: bool = False) -> bytes:
    """Build a message page with the navigation and header block LISTSERV renders."""

    topic = (
        '<a href="/cgi-bin/wa?A2=2512&L=TEI-L&D=0&P=17">&lt;&lt; First</a> '
        '<a href="/cgi-bin/wa?A2=2512&L=TEI-L&D=0&P=41">&lt; Prev</a>'
        if in_thread
        else "[&lt;&lt; First] [&lt; Prev]"
    )
    return (
        "<html><body>"
        '<table class="nopadding">'
        '<tr><td><b>Message:</b></td><td>'
        '<a href="/cgi-bin/wa?A2=2512&L=TEI-L&D=0&P=9">&lt;&lt; First</a></td></tr>'
        f"<tr><td><b>Topic:</b></td><td>{topic}</td></tr>"
        f"<tr><td><b>Author:</b></td><td>{SENDER}</td></tr>"
        "</table>"
        '<table class="width-90 nopadding">'
        f'<tr><td><b>Subject:</b></td><td><div class="forcewrap">'
        f'<a href="/cgi-bin/wa?A2={LIST};{message_id}&S=">{subject}</a></div></td></tr>'
        f'<tr><td><b>From:</b></td><td><div class="forcewrap">{SENDER}</div></td></tr>'
        f'<tr><td><b>Reply To:</b></td><td><div class="forcewrap">{SENDER}</div></td></tr>'
        f'<tr><td><b>Date:</b></td><td><div class="forcewrap">{date}</div></td></tr>'
        '<tr><td><b>Content-Type:</b></td><td><div class="forcewrap">text/plain</div></td></tr>'
        "</table>"
        f'<div id="printable">{BODY}</div>'
        "</body></html>"
    ).encode()


def message_href(archive: str, message_id: str) -> str:
    return f"{archive}?A2={LIST};{message_id}&S="


def serve_psu(fake_http, month: str, entries: list[tuple[str, str, str]]) -> None:
    fake_http.serve(month_index_url(PSU_ARCHIVE, LIST, month), month_index(entries))
    for message_id, subject, date in entries:
        fake_http.serve(
            message_href(PSU_ARCHIVE, message_id), message_page(message_id, subject, date)
        )


def run_psu(tmp_path, **overrides) -> dict:
    arguments = {
        "list_name": LIST,
        "archive": PSU_ARCHIVE,
        "first_month": "2512",
        "last_month": "2512",
        "delay_seconds": 0.0,
        "max_messages": None,
        "raw_root": tmp_path / "raw",
        "normalized_output": tmp_path / "messages.jsonl",
        "manifest_output": tmp_path / "psu-run.yaml",
    }
    return snapshot_psu(**(arguments | overrides))


def records(path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]


def test_month_enumeration_is_inclusive_and_zero_padded() -> None:
    assert enumerate_months("2511", "2602") == ["2511", "2512", "2601", "2602"]
    assert enumerate_months("2512", "2512") == ["2512"]
    assert enumerate_months("9001", "9003") == ["9001", "9002", "9003"]
    assert len(enumerate_months("9001", "2512")) == 36 * 12


@pytest.mark.parametrize("interval", [("2602", "2511"), ("2513", "2602"), ("251", "2602")])
def test_month_enumeration_rejects_an_impossible_interval(interval) -> None:
    with pytest.raises(ValueError):
        enumerate_months(*interval)


def test_month_index_parsing_reads_every_message() -> None:
    parsed = parse_month_index(month_index(MESSAGES), "2512", f"{PSU_ARCHIVE}?A1=ind2512&L=TEI-L")

    assert [row["message_id"] for row in parsed] == [row[0] for row in MESSAGES]
    assert [row["index_subject"] for row in parsed] == [row[1] for row in MESSAGES]
    assert [row["index_date"] for row in parsed] == [row[2] for row in MESSAGES]
    assert parsed[0]["url"] == message_href(PSU_ARCHIVE, MESSAGES[0][0])
    assert {row["list"] for row in parsed} == {LIST}


def test_month_index_parsing_ignores_other_months() -> None:
    entries = [*MESSAGES, ("dddd0004.2511", "Older message", "Sun, 30 Nov 2025 12:00:00 +0100")]

    parsed = parse_month_index(month_index(entries), "2512", f"{PSU_ARCHIVE}?A1=ind2512&L=TEI-L")

    assert [row["message_id"] for row in parsed] == [row[0] for row in MESSAGES]


def test_month_index_parsing_recovers_a_message_outside_the_table_layout() -> None:
    """A link the row reader misses is still inside the declared month boundary."""

    body = month_index(MESSAGES, subject_link=False).replace(b"data-href", b"href")

    parsed = parse_month_index(body, "2512", f"{PSU_ARCHIVE}?A1=ind2512&L=TEI-L")

    assert [row["message_id"] for row in parsed] == [row[0] for row in MESSAGES]
    assert [row["index_subject"] for row in parsed] == ["", "", ""]


def test_message_parsing_keeps_headers_and_thread_pointers_and_drops_the_sender() -> None:
    message_id, subject, date = MESSAGES[1]

    parsed = parse_message(message_page(message_id, subject, date, in_thread=True))

    assert parsed["headers"] == {
        "subject": subject,
        "date": date,
        "content_type": "text/plain",
    }
    assert parsed["thread_position"] == {"first": "17", "prev": "41"}


def test_message_parsing_reports_no_thread_pointers_for_a_standalone_message() -> None:
    parsed = parse_message(message_page(*MESSAGES[0]))

    assert parsed["thread_position"] == {}


def test_legacy_header_spacer_cells_preserve_metadata_and_exclude_sender() -> None:
    page = message_page(*MESSAGES[1], in_thread=True)
    spaced = page.replace(b"</b></td><td>", b'</b></td><td><img alt="" src="blank.gif"></td><td>')
    expected = parse_message(page)
    actual = parse_message(spaced)
    assert actual == expected
    assert actual["headers"]["content_type"] == "text/plain"
    assert SENDER not in json.dumps(actual)


def test_a_clean_bounded_run_is_bounded_complete(tmp_path, fake_http) -> None:
    serve_psu(fake_http, "2512", MESSAGES)

    manifest = run_psu(tmp_path)

    assert manifest["gaps"] == []
    assert manifest["status"] == "bounded-complete"
    assert manifest["adapter"] == {"name": "tools.corpus.listserv_snapshot", "version": 2}
    assert manifest["counts"] == {
        "months_requested": 1,
        "months_indexed": 1,
        "messages_listed": 3,
        "messages": 3,
        "http_responses": 4,
        "gaps": 0,
    }


def test_a_normalized_row_carries_identity_metadata_and_no_sender(tmp_path, fake_http) -> None:
    serve_psu(fake_http, "2512", MESSAGES)

    run_psu(tmp_path)
    rows = records(tmp_path / "messages.jsonl")

    assert [row["message_id"] for row in rows] == [row[0] for row in MESSAGES]
    first = rows[0]
    assert first["list"] == LIST
    assert first["month"] == "2512"
    assert first["subject"] == MESSAGES[0][1]
    assert first["date"] == MESSAGES[0][2]
    assert first["via"] == "psu"
    assert first["archive_url"] == message_href(PSU_ARCHIVE, MESSAGES[0][0])
    assert len(first["raw_sha256"]) == 64
    assert first["raw_path"].startswith("sha256/")
    assert first["in_reply_to"] is None
    serialized = json.dumps(rows)
    assert SENDER not in serialized
    assert BODY not in serialized
    assert not {key for row in rows for key in row if "sender" in key or "from" in key}


def test_a_failing_month_is_a_gap_and_the_run_is_partial(tmp_path, fake_http) -> None:
    serve_psu(fake_http, "2512", MESSAGES)
    fake_http.serve(month_index_url(PSU_ARCHIVE, LIST, "2601"), b"gone", status=404)

    manifest = run_psu(tmp_path, last_month="2601")

    assert manifest["status"] == "partial"
    assert [gap["code"] for gap in manifest["gaps"]] == ["month-index-failed"]
    assert manifest["gaps"][0]["month"] == "2601"
    assert "A1=ind2601" in manifest["gaps"][0]["url"]
    assert manifest["counts"]["months_indexed"] == 1


def test_a_failing_message_is_a_gap_that_keeps_the_other_rows(tmp_path, fake_http) -> None:
    serve_psu(fake_http, "2512", MESSAGES)
    fake_http.serve(message_href(PSU_ARCHIVE, MESSAGES[1][0]), b"gone", status=404)

    manifest = run_psu(tmp_path)

    assert manifest["status"] == "partial"
    assert [gap["code"] for gap in manifest["gaps"]] == ["message-fetch-failed"]
    assert manifest["gaps"][0]["message_id"] == MESSAGES[1][0]
    assert manifest["counts"]["messages"] == 2


@pytest.mark.parametrize(("bound", "expected"), [(3, []), (None, []), (2, ["max-messages-limit"])])
def test_the_message_bound_is_a_gap_only_when_it_binds(
    tmp_path, fake_http, bound, expected
) -> None:
    serve_psu(fake_http, "2512", MESSAGES)

    manifest = run_psu(tmp_path, max_messages=bound)

    assert [gap["code"] for gap in manifest["gaps"]] == expected
    assert manifest["status"] == ("partial" if expected else "bounded-complete")
    assert manifest["counts"]["messages"] == (bound or 3)


def brown_index(month: str) -> str:
    return month_index_url(BROWN_ARCHIVE, LIST, month)


def serve_coverage(fake_http, month: str, timestamp: str | None) -> None:
    if timestamp is None:
        for name in (LIST, LIST.lower()):
            fake_http.serve_json(cdx_url(month_index_url(BROWN_ARCHIVE, name, month)), [])
        return
    fake_http.serve_json(
        cdx_url(brown_index(month)),
        [
            ["timestamp", "original", "statuscode"],
            [timestamp, brown_index(month), "200"],
        ],
    )


def run_coverage(tmp_path, **overrides) -> dict:
    arguments = {
        "list_name": LIST,
        "archive": BROWN_ARCHIVE,
        "first_month": "2505",
        "last_month": "2506",
        "delay_seconds": 0.0,
        "raw_root": tmp_path / "raw",
        "normalized_output": tmp_path / "coverage.jsonl",
        "manifest_output": tmp_path / "coverage-run.yaml",
    }
    return measure_wayback_coverage(**(arguments | overrides))


def test_the_coverage_run_counts_captured_and_missing_months(tmp_path, fake_http) -> None:
    serve_coverage(fake_http, "2505", "20250512120000")
    serve_coverage(fake_http, "2506", None)

    manifest = run_coverage(tmp_path)
    rows = records(tmp_path / "coverage.jsonl")

    assert manifest["counts"]["months_measured"] == 2
    assert manifest["counts"]["months_captured"] == 1
    assert manifest["counts"]["months_missing"] == 1
    assert manifest["counts"]["months_without_disposition"] == 0
    assert [gap["code"] for gap in manifest["gaps"]] == ["wayback-month-missing"]
    # A measured absence is the result of the measurement, so it does not
    # withdraw the completion claim of a run that dispositioned every month.
    assert manifest["status"] == "bounded-complete"
    assert [row["captured"] for row in rows] == [True, False]
    assert rows[0]["latest_capture"] == "20250512120000"
    assert rows[1]["queried_urls"] == [
        month_index_url(BROWN_ARCHIVE, LIST, "2506"),
        month_index_url(BROWN_ARCHIVE, LIST.lower(), "2506"),
    ]


def test_a_failed_coverage_query_leaves_the_month_without_a_disposition(
    tmp_path, fake_http
) -> None:
    serve_coverage(fake_http, "2505", "20250512120000")
    for name in (LIST, LIST.lower()):
        fake_http.serve(cdx_url(month_index_url(BROWN_ARCHIVE, name, "2506")), b"", status=503)

    manifest = run_coverage(tmp_path)

    assert [gap["code"] for gap in manifest["gaps"]] == ["wayback-cdx-query-failed"]
    assert manifest["counts"]["months_without_disposition"] == 1
    assert manifest["status"] == "partial"


def serve_wayback_month(fake_http, month, timestamp, entries) -> None:
    fake_http.serve(wayback_url(timestamp, brown_index(month)), month_index(entries))


def serve_wayback_message(fake_http, message_id, subject, date, timestamp) -> None:
    original = message_href(BROWN_ARCHIVE, message_id)
    fake_http.serve_json(
        cdx_url(original),
        [["timestamp", "original", "statuscode"], [timestamp, original, "200"]],
    )
    fake_http.serve(
        wayback_url(timestamp, original), message_page(message_id, subject, date, in_thread=True)
    )


def serve_missing_wayback_message(fake_http, message_id) -> None:
    for target in message_url_variants(message_href(BROWN_ARCHIVE, message_id)):
        fake_http.serve_json(cdx_url(target), [])


def run_wayback(tmp_path, **overrides) -> dict:
    arguments = {
        "coverage_input": tmp_path / "coverage.jsonl",
        "months": [],
        "delay_seconds": 0.0,
        "max_messages": None,
        "raw_root": tmp_path / "raw",
        "normalized_output": tmp_path / "wayback-messages.jsonl",
        "manifest_output": tmp_path / "wayback-run.yaml",
    }
    return snapshot_wayback(**(arguments | overrides))


def test_the_wayback_fetch_uses_the_original_byte_form(tmp_path, fake_http) -> None:
    entries = [("eeee0001.2505", "Archived thread", "Thu, 1 May 2025 10:00:00 +0000")]
    serve_coverage(fake_http, "2505", "20250512120000")
    run_coverage(tmp_path, first_month="2505", last_month="2505")
    serve_wayback_month(fake_http, "2505", "20250512120000", entries)
    serve_wayback_message(fake_http, *entries[0], "20250601090000")

    manifest = run_wayback(tmp_path)
    rows = records(tmp_path / "wayback-messages.jsonl")

    assert manifest["status"] == "bounded-complete"
    assert manifest["counts"]["messages"] == 1
    assert rows[0]["via"] == "wayback"
    assert rows[0]["capture_timestamp"] == "20250601090000"
    assert rows[0]["month_capture_timestamp"] == "20250512120000"
    assert rows[0]["wayback_url"].startswith(
        "https://web.archive.org/web/20250601090000id_/https://listserv.brown.edu/"
    )
    assert SENDER not in json.dumps(rows)
    assert sum("id_/" in url for url in fake_http.requested) == 2


def test_a_message_without_a_capture_is_a_gap(tmp_path, fake_http) -> None:
    entries = [
        ("eeee0001.2505", "Archived thread", "Thu, 1 May 2025 10:00:00 +0000"),
        ("ffff0002.2505", "Lost thread", "Fri, 2 May 2025 10:00:00 +0000"),
    ]
    serve_coverage(fake_http, "2505", "20250512120000")
    run_coverage(tmp_path, first_month="2505", last_month="2505")
    serve_wayback_month(fake_http, "2505", "20250512120000", entries)
    serve_wayback_message(fake_http, *entries[0], "20250601090000")
    serve_missing_wayback_message(fake_http, entries[1][0])

    manifest = run_wayback(tmp_path)

    assert [gap["code"] for gap in manifest["gaps"]] == ["wayback-message-missing"]
    assert manifest["gaps"][0]["message_id"] == entries[1][0]
    assert manifest["counts"]["messages_missing"] == 1
    assert manifest["status"] == "partial"


BROWN_MONTH = "1911"
BROWN_MESSAGES = [
    ("10398", "Content model of the header", "Fri, 1 Nov 2019 09:12:00 -0500", "42 lines"),
    ("21483", "Re: Content model of the header", "Fri, 1 Nov 2019 14:40:00 +0100", "88 lines"),
    ("40627", "Customization release note", "Mon, 4 Nov 2019 08:05:00 -0500", "17 lines"),
]
BROWN_SORT_LINKS = (
    f'<a href="/cgi-bin/wa?A1=ind{BROWN_MONTH}&amp;L={LIST}&amp;O=D&amp;H=0&amp;D=0&amp;T=1">'
    "Sort by date</a>"
    f'<a href="/cgi-bin/wa?A1=ind{BROWN_MONTH}&amp;L={LIST}&amp;O=A&amp;H=0&amp;D=0&amp;T=1">'
    "Sort by author</a>"
)
WAYBACK_PLACEHOLDER = (
    b"<!DOCTYPE html><html><head><title>Wayback Machine</title></head>"
    b'<body><div id="error"><div class="error-text">'
    b"The Wayback Machine has not archived that URL.</div></div></body></html>"
)


def brown_message_url(month: str, position: str) -> str:
    return f"{BROWN_ARCHIVE}?A2=ind{month}&L={LIST}&P={position}"


def brown_month_index(month: str, entries: list[tuple[str, str, str, str]]) -> bytes:
    """Build a month index in the layout of the retired archive's older LISTSERV.

    Its message links carry a byte position inside the monthly log and write the
    query separator as a character reference, its rows add a size cell after the
    date, its sort links address the index itself, and a grouping row whose
    anchor names the thread opens every thread. A reply is filed under the
    thread its subject continues.
    """

    rows = ""
    thread = 0
    for ordinal, (position, subject, date, size) in enumerate(entries):
        if not subject.startswith("Re: "):
            thread += 1
            rows += (
                '<tr><td colspan="4" class="headergroup" scope="row">'
                '<table cellpadding="0"><tr>'
                '<td><img src="/archives/images/b-thread.png" alt="New Thread"></td>'
                f'<td><a name="{thread}"></a><a href="#{thread}">{subject}</a></td>'
                "</tr></table></td></tr>"
            )
        href = (
            f"https://listserv.brown.edu/cgi-bin/wa?A2=ind{month}"
            f"&amp;L={LIST}&amp;P={position}"
        )
        rows += (
            '<tr class="normalgroup">'
            '<td scope="row"><p class="archive"><img src="/archives/images/b-blank.gif" alt="">'
            f"<span onmouseover=\"showDesc('preview')\"><a href=\"{href}\">{subject}</a></span>"
            "</p></td>"
            f'<td nowrap><p class="archive">{SENDER} {ordinal}</p></td>'
            f'<td nowrap><p class="archive">{date}</p></td>'
            f'<td align="right" nowrap><p class="archive">{size}</p></td>'
            "</tr>"
        )
    return (
        "<html><head><title>LISTSERV 16.5 - TEI-L Archives - November 2019</title></head>"
        f"<body><p>{BROWN_SORT_LINKS}</p>"
        f'<table border="0"><tbody>{rows}</tbody></table></body></html>'
    ).encode()


def serve_brown_month(fake_http, month: str, timestamp: str, entries) -> None:
    fake_http.serve(wayback_url(timestamp, brown_index(month)), brown_month_index(month, entries))


def serve_brown_message(fake_http, month: str, position: str, timestamp: str, body: bytes) -> None:
    original = brown_message_url(month, position)
    fake_http.serve_json(
        cdx_url(original),
        [["timestamp", "original", "statuscode"], [timestamp, original, "200"]],
    )
    fake_http.serve(wayback_url(timestamp, original), body)


def test_the_older_index_form_yields_position_ids_and_ignores_sort_links() -> None:
    parsed = parse_month_index(
        brown_month_index(BROWN_MONTH, BROWN_MESSAGES), BROWN_MONTH, brown_index(BROWN_MONTH)
    )

    assert [row["message_id"] for row in parsed] == [
        f"P{entry[0]}.{BROWN_MONTH}" for entry in BROWN_MESSAGES
    ]
    assert [row["index_subject"] for row in parsed] == [entry[1] for entry in BROWN_MESSAGES]
    assert [row["index_date"] for row in parsed] == [entry[2] for entry in BROWN_MESSAGES]
    assert parsed[0]["url"] == brown_message_url(BROWN_MONTH, BROWN_MESSAGES[0][0])
    assert {row["list"] for row in parsed} == {LIST}
    # The reply is filed under the thread it continues; the third message opens
    # its own.
    assert [row["index_thread"] for row in parsed] == ["1", "1", "2"]
    assert SENDER not in json.dumps(parsed)


def test_the_older_message_lookup_asks_both_list_name_spellings() -> None:
    variants = message_url_variants(brown_message_url(BROWN_MONTH, "40627"))

    assert variants == [
        brown_message_url(BROWN_MONTH, "40627"),
        brown_message_url(BROWN_MONTH, "40627").replace(f"L={LIST}", f"L={LIST.lower()}"),
    ]


def test_a_wayback_placeholder_is_a_missing_message_and_never_a_stored_body(
    tmp_path, fake_http
) -> None:
    position, subject, date, _size = BROWN_MESSAGES[0]
    serve_coverage(fake_http, BROWN_MONTH, "20191209195430")
    run_coverage(tmp_path, first_month=BROWN_MONTH, last_month=BROWN_MONTH)
    serve_brown_month(fake_http, BROWN_MONTH, "20191209195430", BROWN_MESSAGES[:1])
    serve_brown_message(fake_http, BROWN_MONTH, position, "20191210120000", WAYBACK_PLACEHOLDER)

    manifest = run_wayback(tmp_path)
    rows = records(tmp_path / "wayback-messages.jsonl")

    assert [gap["code"] for gap in manifest["gaps"]] == ["wayback-message-missing"]
    assert manifest["gaps"][0]["message_id"] == f"P{position}.{BROWN_MONTH}"
    assert manifest["counts"]["messages_missing"] == 1
    assert manifest["status"] == "partial"
    # The index observation stands on its own; only the placeholder is discarded.
    assert len(rows) == 1
    assert rows[0]["subject"] == subject
    assert rows[0]["date"] == date
    assert rows[0]["http_status"] == 200
    assert rows[0]["archive_url"] == brown_message_url(BROWN_MONTH, position)
    assert rows[0]["content_type"] is None
    assert rows[0]["thread_position"] is None


def test_an_older_message_is_fetched_under_the_lower_case_list_name(tmp_path, fake_http) -> None:
    position, subject, date, _size = BROWN_MESSAGES[2]
    lowered = brown_message_url(BROWN_MONTH, position).replace(f"L={LIST}", f"L={LIST.lower()}")
    serve_coverage(fake_http, BROWN_MONTH, "20191209195430")
    run_coverage(tmp_path, first_month=BROWN_MONTH, last_month=BROWN_MONTH)
    serve_brown_month(fake_http, BROWN_MONTH, "20191209195430", BROWN_MESSAGES[2:])
    fake_http.serve_json(cdx_url(brown_message_url(BROWN_MONTH, position)), [])
    fake_http.serve_json(
        cdx_url(lowered),
        [["timestamp", "original", "statuscode"], ["20191210120000", lowered, "200"]],
    )
    fake_http.serve(
        wayback_url("20191210120000", lowered),
        message_page(f"P{position}.{BROWN_MONTH}", subject, date, in_thread=True),
    )

    manifest = run_wayback(tmp_path)
    rows = records(tmp_path / "wayback-messages.jsonl")

    assert manifest["gaps"] == []
    assert manifest["status"] == "bounded-complete"
    assert rows[0]["message_id"] == f"P{position}.{BROWN_MONTH}"
    assert rows[0]["subject"] == subject
    assert rows[0]["wayback_url"] == wayback_url("20191210120000", lowered)
    assert SENDER not in json.dumps(rows)


def test_a_message_the_wayback_index_lacks_leaves_the_row_the_index_observed(
    tmp_path, fake_http
) -> None:
    serve_coverage(fake_http, BROWN_MONTH, "20191209195430")
    run_coverage(tmp_path, first_month=BROWN_MONTH, last_month=BROWN_MONTH)
    serve_brown_month(fake_http, BROWN_MONTH, "20191209195430", BROWN_MESSAGES[:2])
    for position, *_rest in BROWN_MESSAGES[:2]:
        for target in message_url_variants(brown_message_url(BROWN_MONTH, position)):
            fake_http.serve_json(cdx_url(target), [])

    manifest = run_wayback(tmp_path)
    rows = records(tmp_path / "wayback-messages.jsonl")

    assert [gap["code"] for gap in manifest["gaps"]] == ["wayback-message-missing"] * 2
    assert manifest["counts"]["messages"] == 2
    assert manifest["counts"]["messages_missing"] == 2
    assert manifest["counts"]["messages_index_only"] == 2
    assert manifest["status"] == "partial"
    position, subject, date, _size = BROWN_MESSAGES[1]
    assert rows[1] == {
        "schema_version": 1,
        "source_id": "tei-l-archive",
        "object_type": "mailing-list-message",
        "via": "wayback-index",
        "list": LIST,
        "month": BROWN_MONTH,
        "message_id": f"P{position}.{BROWN_MONTH}",
        "subject": subject,
        "date": date,
        "index_subject": subject,
        "index_date": date,
        "content_type": None,
        "in_reply_to": None,
        "upstream_message_id": None,
        "references": None,
        "thread_position": None,
        "archive_url": brown_message_url(BROWN_MONTH, position),
        "requested_url": None,
        "http_status": None,
        "observed_at": None,
        "media_type": None,
        "byte_count": None,
        "raw_sha256": None,
        "raw_path": None,
        "capture_timestamp": None,
        "month_capture_timestamp": "20191209195430",
        "wayback_url": None,
        "index_thread": "1",
    }
    assert SENDER not in json.dumps(rows)


def test_a_capture_the_crawl_never_served_loses_to_an_older_served_one(
    tmp_path, fake_http
) -> None:
    position, subject, date, _size = BROWN_MESSAGES[0]
    original = brown_message_url(BROWN_MONTH, position)
    serve_coverage(fake_http, BROWN_MONTH, "20191209195430")
    run_coverage(tmp_path, first_month=BROWN_MONTH, last_month=BROWN_MONTH)
    serve_brown_month(fake_http, BROWN_MONTH, "20191209195430", BROWN_MESSAGES[:1])
    fake_http.serve_json(
        cdx_url(original),
        [
            ["timestamp", "original", "statuscode"],
            ["20191210120000", original, "200"],
            ["20221217092239", original, "404"],
        ],
    )
    # Only the served capture is routed, so choosing the newer row would fail the
    # fetch instead of quietly storing an error page.
    fake_http.serve(
        wayback_url("20191210120000", original),
        message_page(f"P{position}.{BROWN_MONTH}", subject, date, in_thread=True),
    )

    manifest = run_wayback(tmp_path)
    rows = records(tmp_path / "wayback-messages.jsonl")

    assert manifest["gaps"] == []
    assert manifest["status"] == "bounded-complete"
    assert manifest["counts"]["messages_index_only"] == 0
    assert rows[0]["via"] == "wayback"
    assert rows[0]["capture_timestamp"] == "20191210120000"
    assert rows[0]["index_thread"] == "1"


@pytest.mark.parametrize(
    ("captures", "expected"),
    [
        ([("20191210120000", "200"), ("20221217092239", "404")], "20191210120000"),
        ([("20191210120000", "200"), ("20221217092239", "200")], "20221217092239"),
        ([("20191210120000", "404"), ("20221217092239", "301")], "20221217092239"),
        ([], None),
    ],
)
def test_the_capture_choice_prefers_a_served_row_over_a_newer_one(captures, expected) -> None:
    rows = [{"timestamp": timestamp, "statuscode": status} for timestamp, status in captures]

    chosen = preferred_capture(rows)

    assert (chosen["timestamp"] if chosen else None) == expected


def test_the_cli_help_lists_the_three_commands(capsys) -> None:
    with pytest.raises(SystemExit):
        listserv_snapshot.parse_args(["--help"])

    output = capsys.readouterr().out
    assert "psu" in output
    assert "wayback-coverage" in output
    assert "wayback-fetch" in output


@pytest.mark.parametrize(
    ("argv", "message"),
    [
        (["psu", "--from-month", "2602", "--to-month", "2512"], "lies after"),
        (["psu", "--from-month", "2512", "--to-month", "2601", "--max-messages", "0"], "max-messages"),
        (["psu", "--from-month", "2512", "--to-month", "2601", "--delay-seconds", "-1"], "delay-seconds"),
    ],
)
def test_the_cli_rejects_an_impossible_boundary(tmp_path, argv, message) -> None:
    arguments = [
        *argv,
        "--normalized-output",
        str(tmp_path / "messages.jsonl"),
        "--manifest-output",
        str(tmp_path / "run.yaml"),
        "--raw-root",
        str(tmp_path / "raw"),
    ]

    with pytest.raises(SystemExit, match=message):
        listserv_snapshot.main(arguments)


FIXED_TIME = "2026-09-11T08:00:00Z"
TWO_MONTHS = {BROWN_MONTH: "20191209195430", "2505": "20250512120000"}
LATER_MESSAGES = [("eeee0001.2505", "Archived thread", "Thu, 1 May 2025 10:00:00 +0000")]


class Interrupted(BaseException):
    """Stands in for a crash that no handler in the collector may absorb."""


@pytest.fixture
def fixed_clock(monkeypatch) -> None:
    """Pin every timestamp so that two runs compare byte for byte."""

    monkeypatch.setattr(http_store, "utc_now", lambda: FIXED_TIME)
    monkeypatch.setattr(listserv_snapshot, "utc_now", lambda: FIXED_TIME)


def write_coverage(path, captures: dict[str, str]) -> None:
    """Write the captured rows a coverage run leaves, without running one."""

    rows = [
        {
            "schema_version": 1,
            "source_id": "tei-l-archive",
            "object_type": "wayback-month-coverage",
            "list": LIST,
            "month": month,
            "queried_urls": [brown_index(month)],
            "captured": True,
            "capture_count": 1,
            "latest_capture": timestamp,
            "latest_capture_original": brown_index(month),
            "latest_capture_status": "200",
        }
        for month, timestamp in captures.items()
    ]
    path.write_text("".join(json.dumps(row) + "\n" for row in rows), encoding="utf-8")


def serve_two_months(fake_http) -> None:
    """Serve an older month with a fetched, a placeholder and an index-only message.

    A later month in the Penn State link form follows with one fetched message.
    """

    fetched, placeholder, index_only = BROWN_MESSAGES
    serve_brown_month(fake_http, BROWN_MONTH, TWO_MONTHS[BROWN_MONTH], BROWN_MESSAGES)
    serve_brown_message(
        fake_http,
        BROWN_MONTH,
        fetched[0],
        "20191210120000",
        message_page(f"P{fetched[0]}.{BROWN_MONTH}", fetched[1], fetched[2], in_thread=True),
    )
    serve_brown_message(
        fake_http, BROWN_MONTH, placeholder[0], "20191210130000", WAYBACK_PLACEHOLDER
    )
    for target in message_url_variants(brown_message_url(BROWN_MONTH, index_only[0])):
        fake_http.serve_json(cdx_url(target), [])
    serve_wayback_month(fake_http, "2505", TWO_MONTHS["2505"], LATER_MESSAGES)
    serve_wayback_message(fake_http, *LATER_MESSAGES[0], "20250601090000")


def crash_at(monkeypatch, fake_http, url: str) -> None:
    """Route every request to the fake archive except ``url``, which crashes the run."""

    target = canonical_url(url)

    def open_or_crash(request, timeout=None):
        if canonical_url(request.full_url) == target:
            raise Interrupted
        return fake_http.open(request, timeout)

    monkeypatch.setattr(http_store.urllib.request, "urlopen", open_or_crash)


def fetch_run(tmp_path, name: str, **overrides) -> dict:
    """Run a wayback fetch whose raw store, outputs and default checkpoint carry ``name``."""

    return run_wayback(
        tmp_path,
        **(
            {
                "raw_root": tmp_path / f"raw-{name}",
                "normalized_output": tmp_path / f"{name}.jsonl",
                "manifest_output": tmp_path / f"{name}.yaml",
            }
            | overrides
        ),
    )


def default_checkpoint(tmp_path, name: str):
    return tmp_path / f"raw-{name}" / "checkpoints" / name


def sealed_months(checkpoint) -> list[str]:
    return sorted(path.stem for path in (checkpoint / "months").glob("*.json"))


def provenance(manifest: dict) -> dict:
    """Return a manifest without the fields that name its invocation or its paths."""

    kept = {
        key: value for key, value in manifest.items() if key not in {"run_id", "objects", "resume"}
    }
    kept["requests"] = {
        key: value
        for key, value in manifest["requests"].items()
        if key not in {"checkpoint", "resume_from"}
    }
    kept["objects"] = [
        {"kind": item["kind"], "sha256": item["sha256"]} for item in manifest["objects"]
    ]
    return kept


@pytest.mark.parametrize("bound", [None, 2])
def test_an_interrupted_fetch_resumes_to_the_uninterrupted_result(
    tmp_path, fake_http, fixed_clock, monkeypatch, bound
) -> None:
    """A crash inside the second month loses only that month.

    The resumed run reuses the sealed first month without a request and writes
    the bytes and provenance of a run that was never interrupted, with the
    placeholder, the index-only row and the message bound intact.
    """

    write_coverage(tmp_path / "coverage.jsonl", TWO_MONTHS)
    serve_two_months(fake_http)
    straight = fetch_run(tmp_path, "straight", max_messages=bound)

    crash_at(monkeypatch, fake_http, wayback_url(TWO_MONTHS["2505"], brown_index("2505")))
    with pytest.raises(Interrupted):
        fetch_run(tmp_path, "resumed", max_messages=bound)
    checkpoint = default_checkpoint(tmp_path, "resumed")
    assert sealed_months(checkpoint) == [BROWN_MONTH]
    assert not (tmp_path / "resumed.jsonl").exists()

    monkeypatch.setattr(http_store.urllib.request, "urlopen", fake_http.open)
    fake_http.requested.clear()
    resumed = fetch_run(tmp_path, "resumed", max_messages=bound, resume_from=checkpoint)

    assert fake_http.requested
    assert not any(f"ind{BROWN_MONTH}" in url for url in fake_http.requested)
    assert (tmp_path / "resumed.jsonl").read_bytes() == (tmp_path / "straight.jsonl").read_bytes()
    assert provenance(resumed) == provenance(straight)
    assert resumed["resume"] == {"invocations": [FIXED_TIME, FIXED_TIME], "months_reused": 1}
    assert "resume" not in straight
    assert sealed_months(checkpoint) == [BROWN_MONTH, "2505"]
    rows = records(tmp_path / "resumed.jsonl")
    if bound is None:
        assert [row["via"] for row in rows] == ["wayback", "wayback", "wayback-index", "wayback"]
        assert [gap["code"] for gap in resumed["gaps"]] == ["wayback-message-missing"] * 2
    else:
        assert [row["via"] for row in rows] == ["wayback", "wayback"]
        assert [gap["code"] for gap in resumed["gaps"]] == [
            "max-messages-limit",
            "wayback-message-missing",
        ]
    assert resumed["status"] == "partial"


def test_resuming_a_finished_checkpoint_rebuilds_the_output_without_a_request(
    tmp_path, fake_http, fixed_clock
) -> None:
    write_coverage(tmp_path / "coverage.jsonl", TWO_MONTHS)
    serve_two_months(fake_http)
    first = fetch_run(tmp_path, "first")
    fake_http.requested.clear()

    again = fetch_run(
        tmp_path,
        "again",
        raw_root=tmp_path / "raw-first",
        resume_from=default_checkpoint(tmp_path, "first"),
    )

    assert fake_http.requested == []
    assert (tmp_path / "again.jsonl").read_bytes() == (tmp_path / "first.jsonl").read_bytes()
    assert provenance(again) == provenance(first)
    assert again["resume"]["months_reused"] == 2


@pytest.mark.parametrize("existing_suffix", [".jsonl", ".yaml"])
def test_fetch_preserves_existing_run_outputs(tmp_path, fake_http, existing_suffix) -> None:
    write_coverage(tmp_path / "coverage.jsonl", TWO_MONTHS)
    output = tmp_path / f"existing{existing_suffix}"
    output.write_bytes(b"preserved run artifact\n")
    with pytest.raises(ValueError, match="already exists; use new output paths"):
        fetch_run(tmp_path, "existing")
    assert output.read_bytes() == b"preserved run artifact\n"
    assert fake_http.requested == []
    assert not default_checkpoint(tmp_path, "existing").exists()


@pytest.mark.parametrize("failure", ["month-index", "message-cdx"])
def test_a_failed_month_is_not_sealed_and_is_asked_again(tmp_path, fake_http, failure) -> None:
    """A failure that asking again may cure never becomes a reusable result."""

    write_coverage(tmp_path / "coverage.jsonl", TWO_MONTHS)
    position, subject, date, _size = BROWN_MESSAGES[0]
    serve_brown_month(fake_http, BROWN_MONTH, TWO_MONTHS[BROWN_MONTH], BROWN_MESSAGES[:1])
    serve_brown_message(
        fake_http,
        BROWN_MONTH,
        position,
        "20191210120000",
        message_page(f"P{position}.{BROWN_MONTH}", subject, date),
    )
    if failure == "month-index":
        fake_http.serve(wayback_url(TWO_MONTHS["2505"], brown_index("2505")), b"", status=503)
    else:
        serve_wayback_month(fake_http, "2505", TWO_MONTHS["2505"], LATER_MESSAGES)
        for target in message_url_variants(message_href(BROWN_ARCHIVE, LATER_MESSAGES[0][0])):
            fake_http.serve(cdx_url(target), b"", status=503)

    first = fetch_run(tmp_path, "run")
    checkpoint = default_checkpoint(tmp_path, "run")

    assert first["status"] == "partial"
    assert [gap["code"] for gap in first["gaps"]] == (
        ["month-index-failed"] if failure == "month-index" else ["wayback-message-missing"]
    )
    assert sealed_months(checkpoint) == [BROWN_MONTH]

    serve_wayback_month(fake_http, "2505", TWO_MONTHS["2505"], LATER_MESSAGES)
    serve_wayback_message(fake_http, *LATER_MESSAGES[0], "20250601090000")
    fake_http.requested.clear()
    resumed = fetch_run(
        tmp_path, "run-resumed", raw_root=tmp_path / "raw-run", resume_from=checkpoint
    )

    assert resumed["status"] == "bounded-complete"
    assert resumed["gaps"] == []
    assert resumed["counts"]["months_indexed"] == 2
    assert resumed["resume"]["months_reused"] == 1
    assert not any(f"ind{BROWN_MONTH}" in url for url in fake_http.requested)
    assert sealed_months(checkpoint) == [BROWN_MONTH, "2505"]


@pytest.mark.parametrize(
    ("change", "message"),
    [
        ("coverage", "different coverage_input_sha256"),
        ("month-filter", "different month_filter"),
        ("bound", "different max_messages"),
        ("raw-changed", "raw bytes"),
        ("raw-missing", "raw bytes"),
        ("block-edited", "does not match its seal"),
        ("foreign", "is not a tei-l-archive wayback-fetch checkpoint"),
        ("older-parser", "is not a tei-l-archive wayback-fetch checkpoint"),
    ],
)
def test_a_resume_rejects_a_checkpoint_that_no_longer_matches(
    tmp_path, fake_http, change, message
) -> None:
    coverage = tmp_path / "coverage.jsonl"
    write_coverage(coverage, TWO_MONTHS)
    serve_two_months(fake_http)
    fetch_run(tmp_path, "run")
    checkpoint = default_checkpoint(tmp_path, "run")
    month_file = checkpoint / "months" / f"{BROWN_MONTH}.json"
    block = json.loads(month_file.read_text(encoding="utf-8"))
    raw = tmp_path / "raw-run" / block["responses"][0]["raw_path"]
    overrides = {}
    if change == "coverage":
        write_coverage(coverage, {**TWO_MONTHS, "2505": "20250513120000"})
    elif change == "month-filter":
        overrides["months"] = [BROWN_MONTH]
    elif change == "bound":
        overrides["max_messages"] = 1
    elif change == "raw-changed":
        raw.write_bytes(raw.read_bytes() + b" ")
    elif change == "raw-missing":
        raw.unlink()
    elif change == "block-edited":
        block["records"][0]["subject"] = "Edited after sealing"
        month_file.write_text(json.dumps(block), encoding="utf-8")
    else:
        state_file = checkpoint / "checkpoint.json"
        state = json.loads(state_file.read_text(encoding="utf-8"))
        if change == "older-parser":
            state["schema_version"] = 1
        else:
            state["source_id"] = "other-source"
        state_file.write_text(json.dumps(state), encoding="utf-8")
    fake_http.requested.clear()

    with pytest.raises(ValueError, match=message):
        fetch_run(
            tmp_path, "resumed", raw_root=tmp_path / "raw-run", resume_from=checkpoint, **overrides
        )
    assert fake_http.requested == []
    assert not (tmp_path / "resumed.jsonl").exists()


def test_a_new_run_never_writes_into_an_existing_checkpoint(tmp_path, fake_http) -> None:
    write_coverage(tmp_path / "coverage.jsonl", TWO_MONTHS)
    serve_two_months(fake_http)
    fetch_run(tmp_path, "run")
    fake_http.requested.clear()

    with pytest.raises(ValueError, match="already exists"):
        fetch_run(tmp_path, "run")
    assert fake_http.requested == []


def test_the_fetch_cli_offers_resume_and_rejects_an_unusable_checkpoint(tmp_path, capsys) -> None:
    with pytest.raises(SystemExit):
        listserv_snapshot.parse_args(["wayback-fetch", "--help"])
    output = capsys.readouterr().out
    assert "--resume-from" in output
    assert "--checkpoint" in output

    write_coverage(tmp_path / "coverage.jsonl", TWO_MONTHS)
    outputs = [
        "--coverage-input",
        str(tmp_path / "coverage.jsonl"),
        "--normalized-output",
        str(tmp_path / "messages.jsonl"),
        "--manifest-output",
        str(tmp_path / "run.yaml"),
        "--raw-root",
        str(tmp_path / "raw"),
    ]
    with pytest.raises(SystemExit, match="different directories"):
        listserv_snapshot.main(
            [
                "wayback-fetch",
                *outputs,
                "--checkpoint",
                str(tmp_path / "a"),
                "--resume-from",
                str(tmp_path / "b"),
            ]
        )
    with pytest.raises(SystemExit, match="no checkpoint to resume"):
        listserv_snapshot.main(["wayback-fetch", *outputs, "--resume-from", str(tmp_path / "absent")])
