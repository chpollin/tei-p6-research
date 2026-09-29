"""Run declared, read-only selection queries over tracked corpus snapshots.

Run ``python -m tools.select_sources --queries FILE`` or give inline queries
with ``--github-title REGEX``, ``--github-label LABEL``, ``--sourceforge-summary
REGEX``, ``--sourceforge-label LABEL``, ``--tei-l-subject REGEX``,
``--atlas-ident IDENT``, ``--atlas-member CLASS`` and ``--atlas-attribute NAME``.
``--output PATH`` writes the JSON result; ``select(root, queries)`` is the API.

A query file is YAML or JSON: a list of queries or a mapping with ``queries``.
Each query names a ``stream`` and exactly one form: ``pattern`` (with optional
``field`` and ``ignore_case``, default true) or ``label`` for the GitHub,
SourceForge and TEI-L streams, and ``ident``, ``member_of`` or ``attribute``
(with optional ``category``) for the declaration atlas.

Each stream is one normalized record file read once together with its run
manifest and lock, filtered to one record kind. An issue that the snapshot also
holds as a detail record therefore counts once, and duplicate upstream IDs
within that kind are reported. The result records the exact file, manifest and
lock hashes, the declared queries and their matches. It changes no admission,
status or selection record and never opens raw bodies (workbench/selections).
A missing stream yields ``count: null`` and a gap, never zero. Relations are
those the snapshot already records; a SourceForge ticket and a GitHub issue
with the same title stay distinct records whose migration relation is unknown
(knowledge/data.md, reconciliation invariants).
"""
from __future__ import annotations

import argparse
import contextlib
import hashlib
import json
import re
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

import yaml

from tools.corpus.manifest import lock_manifest_references

GENERATOR = "tools.select_sources v1"
USE = "selection candidates for a recorded run; no admission, status or grounding"
MIGRATION_UNKNOWN = ("The snapshot records no SourceForge-to-GitHub relation for this ticket; equal titles "
                     "or dates do not establish identity.")
RAW_UNKNOWN = "Raw bodies are local-only; this tool neither opens nor checks them, so their availability is unknown."
ATLAS_LIMIT = ("Direct declarations of immediate P5/Source/Specs files only; inherited attributes and "
               "transitive class membership are not resolved.")
SUBJECT_NOTE = ("Grouped by subject without reply prefixes; recorded thread pointers are incomplete, so a "
                "group is a lead and not a thread identity.")
COMPLETE = ("observable-complete", "bounded-complete")
SUBJECT_PREFIX = re.compile(r"^(?:(?:re|aw|fwd?|sv|antw)\s*:\s*)+", re.I)
HEADER = re.compile(rb"^(schema_version|run_id|source_id|started_at|finished_at|status):[ \t]*(\S.*?)[ \t]*\r?$", re.M)
OBJECTS = re.compile(rb"^objects:[ \t]*\r?\n.*?(?=^[A-Za-z_][A-Za-z_0-9-]*:|\Z)", re.M | re.S)
QUERY_KEYS = frozenset({"id", "stream", "field", "pattern", "ignore_case", "label", "ident", "member_of",
                        "attribute", "category"})
ATLAS_FORMS = ("ident", "member_of", "attribute")


@dataclass(frozen=True)
class Stream:
    records: str
    manifest: str | None
    lock: str | None
    kind_field: str
    kind: str | None
    identities: tuple[tuple[str, ...], ...]
    text_fields: tuple[str, ...] = ()
    label_field: str | None = None
    companions: tuple[str, ...] = ()


STREAMS = {
    "github": Stream("corpus/normalized/github/teic-tei-work-items.jsonl",
                     "sources/manifests/2026-09-06-github-teic-tei-work-items.yaml",
                     "sources/locks/github-teic-tei.yaml", "kind", "work-item-detail",
                     (("node_id",), ("number",)), ("title",), "labels", ("issue", "pull-request-summary")),
    "github-relations": Stream("corpus/normalized/github/teic-tei-relations.jsonl",
                               "sources/manifests/2026-09-06-github-teic-tei-relations.yaml",
                               "sources/locks/github-teic-tei.yaml", "kind", "relation", ()),
    "sourceforge": Stream("corpus/normalized/sourceforge/tei-legacy-trackers-r4.jsonl",
                          "sources/manifests/2026-09-06-tei-legacy-sourceforge-r4.yaml",
                          "sources/locks/legacy-sourceforge.yaml", "object_type", "ticket",
                          (("object_id",), ("tracker", "ticket_num")), ("summary",), "labels"),
    "tei-l": Stream("corpus/normalized/mail/tei-l-psu.jsonl", "sources/manifests/2026-09-06-tei-l-psu.yaml",
                    "sources/locks/tei-l-archive.yaml", "object_type", "mailing-list-message",
                    (("message_id",),), ("subject",)),
    "atlas": Stream("corpus/projections/p5-specs-4.12.0.json", None, None, "category", None, (("ident",),)),
}
QUERYABLE = ("github", "sourceforge", "tei-l", "atlas")
INLINE = (("github-title", "github", "pattern"), ("github-label", "github", "label"),
          ("sourceforge-summary", "sourceforge", "pattern"), ("sourceforge-label", "sourceforge", "label"),
          ("tei-l-subject", "tei-l", "pattern"), ("atlas-ident", "atlas", "ident"),
          ("atlas-member", "atlas", "member_of"), ("atlas-attribute", "atlas", "attribute"))


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _header(data: bytes) -> dict:
    """Top-level scalar identity of a run manifest, read without parsing its request lists."""
    result = {}
    for key, value in HEADER.findall(data):
        name, raw = key.decode("ascii"), value.decode("utf-8")
        if name not in result:
            parsed = yaml.safe_load(raw)
            result[name] = parsed if isinstance(parsed, int | str) else raw.strip("'\"")
    return result


def _check(query: dict, position: int) -> dict:
    """Normalize one declared query; an undeclared shape is an error, not a guess."""
    if not isinstance(query, dict):
        raise ValueError(f"Query {position} is not a mapping")
    unknown = set(query) - QUERY_KEYS
    if unknown:
        raise ValueError(f"Query {position} has undeclared keys: {sorted(unknown)}")
    stream = query.get("stream")
    if stream not in QUERYABLE:
        raise ValueError(f"Query {position} names no queryable stream: {stream!r}")
    declared = {"id": str(query.get("id") or f"q{position}"), "stream": stream}
    forms = [key for key in ATLAS_FORMS if key in query]
    if stream == "atlas":
        if len(forms) != 1 or {"field", "pattern", "label", "ignore_case"} & set(query):
            raise ValueError(f"Query {position} needs exactly one of {', '.join(ATLAS_FORMS)}")
        declared[forms[0]] = str(query[forms[0]])
        if query.get("category"):
            declared["category"] = str(query["category"])
        return declared
    spec = STREAMS[stream]
    if forms or "category" in query or ("pattern" in query) == ("label" in query):
        raise ValueError(f"Query {position} needs exactly one of pattern or label")
    if "label" in query:
        if not spec.label_field or {"field", "ignore_case"} & set(query):
            raise ValueError(f"Query {position}: stream {stream} has no label query of this shape")
        declared["label"] = str(query["label"])
        return declared
    text_field = query.get("field", spec.text_fields[0])
    if text_field not in spec.text_fields:
        raise ValueError(f"Query {position}: stream {stream} matches only {', '.join(spec.text_fields)}")
    declared.update(field=text_field, pattern=str(query["pattern"]), ignore_case=bool(query.get("ignore_case", True)))
    try:
        re.compile(declared["pattern"])
    except re.error as error:
        raise ValueError(f"Query {position} pattern is invalid: {error}") from error
    return declared


def _control(root: Path, stream: Stream, gaps: list, records_hash: str | None) -> dict:
    """Manifest header and lock membership of one stream."""
    info = {"manifest": stream.manifest, "lock": stream.lock}
    header = {}
    manifest = root / stream.manifest
    if manifest.is_file():
        data = manifest.read_bytes()
        header = _header(data)
        info.update(manifest_sha256=_sha256(data), manifest_run_id=header.get("run_id"),
                    manifest_source_id=header.get("source_id"), manifest_status=header.get("status"),
                    manifest_finished_at=header.get("finished_at"))
        block = OBJECTS.search(data)
        objects = (yaml.safe_load(block[0]) or {}).get("objects", []) if block else []
        declarations = [item for item in objects if item.get("path") == stream.records]
        expected = declarations[0].get("sha256") if len(declarations) == 1 else None
        info["manifest_records_sha256"] = expected
        info["records_sha256_matches_manifest"] = records_hash == expected if records_hash and expected else None
        if not expected:
            gaps.append({"code": "stream-identity-unconfirmed", "path": stream.manifest,
                         "detail": "The manifest does not uniquely name this stream with a checksum."})
        elif records_hash and records_hash != expected:
            gaps.append({"code": "stream-hash-mismatch", "path": stream.records,
                         "detail": "The current stream bytes differ from the completed manifest; queries describe these current bytes only."})
        if header.get("status") not in COMPLETE:
            gaps.append({"code": "run-not-complete", "path": stream.manifest,
                         "detail": f"The run manifest records status {header.get('status')!r}; matches hold for the recorded run only."})
    else:
        gaps.append({"code": "manifest-missing", "path": stream.manifest,
                     "detail": "The run manifest is absent; the snapshot identity is unconfirmed."})
    lock = root / stream.lock
    if not lock.is_file():
        gaps.append({"code": "lock-missing", "path": stream.lock, "detail": "The lock is absent; the control-plane link is unconfirmed."})
        return info
    data = lock.read_bytes()
    content = yaml.safe_load(data) or {}
    listed = stream.manifest in lock_manifest_references(content)
    repository = content.get("repository") or {}
    info.update(lock_sha256=_sha256(data), lock_source_id=content.get("source_id"),
                lock_retrieval_status=content.get("retrieval_status"), manifest_listed_in_lock=listed,
                lock_repository=(f"{repository['owner']}/{repository['name']}"
                                 if repository.get("owner") and repository.get("name") else None))
    if not listed:
        gaps.append({"code": "manifest-not-listed-in-lock", "path": stream.lock,
                     "detail": f"The lock does not name {stream.manifest}; the snapshot's control-plane link is unconfirmed."})
    if header.get("source_id") and content.get("source_id") and header["source_id"] != content["source_id"]:
        gaps.append({"code": "manifest-source-mismatch", "path": stream.manifest,
                     "detail": f"Manifest source {header['source_id']} differs from lock source {content['source_id']}."})
    return info


def _load(root: Path, name: str) -> dict:
    stream = STREAMS[name]
    info = {"records": stream.records, "record_kind": stream.kind, "kind_field": stream.kind_field}
    gaps: list[dict] = []
    rows, companions = None, {kind: set() for kind in stream.companions}
    file = root / stream.records
    if not file.is_file():
        gaps.append({"code": "stream-missing", "path": stream.records,
                     "detail": "The stream is absent here; its queries have no result, which is not zero matches."})
    elif name == "atlas":
        data = file.read_bytes()
        atlas = json.loads(data)
        rows = list(atlas.get("records") or [])
        source = atlas.get("source") or {}
        info.update(records_sha256=_sha256(data), records_total=len(rows), records_of_kind=len(rows),
                    atlas_use=atlas.get("use"),
                    declared_source={key: source.get(key) for key in ("source_id", "version", "commit", "manifest",
                                                                     "manifest_sha256", "lock", "lock_sha256")})
        declared = root / source["manifest"] if source.get("manifest") else None
        if declared and declared.resolve().is_relative_to(root.resolve()) and declared.is_file():
            info["declared_manifest_sha256_matches"] = _sha256(declared.read_bytes()) == source.get("manifest_sha256")
        else:
            gaps.append({"code": "manifest-missing", "path": source.get("manifest"),
                         "detail": "The manifest the atlas declares is absent here."})
    else:
        data = file.read_bytes()
        rows, total = [], 0
        for number, line in enumerate(data.decode("utf-8").splitlines(), 1):
            if not line.strip():
                continue
            try:
                record = json.loads(line)
            except json.JSONDecodeError:
                gaps.append({"code": "unreadable-record", "path": stream.records, "line": number})
                continue
            total += 1
            kind = record.get(stream.kind_field)
            if kind == stream.kind:
                rows.append(record)
            elif kind in companions and record.get("number") is not None:
                companions[kind].add(record["number"])
        info.update(records_sha256=_sha256(data), records_total=total, records_of_kind=len(rows))
        gaps.append({"code": "raw-availability-unknown", "path": stream.records, "detail": RAW_UNKNOWN})
    duplicated: set[int] = set()
    for fields in stream.identities if rows is not None else ():
        keys = Counter(tuple(row.get(f) for f in fields) for row in rows)
        repeated = {key for key, count in keys.items() if count > 1}
        if repeated:
            gaps.append({"code": "duplicate-upstream-id", "path": stream.records, "record_kind": stream.kind,
                         "identity": "+".join(fields),
                         "values": sorted((list(k) if len(k) > 1 else k[0] for k in repeated), key=str)})
            duplicated.update(id(row) for row in rows if tuple(row.get(f) for f in fields) in repeated)
    if stream.manifest:
        info.update(_control(root, stream, gaps, info.get("records_sha256")))
    return {"info": info, "rows": rows, "gaps": gaps, "duplicated": duplicated,
            "companions": companions if any(companions.values()) else None}


def _relations(node: str | None, relations: dict | None) -> dict:
    if relations is None or relations["rows"] is None:
        return {"status": "unknown", "detail": "The relations stream is absent; relations are unknown, not absent."}
    rows = relations["by_source"].get(node, [])
    targeted = [row for row in rows if row.get("target_node_id") or row.get("target_number") is not None]
    return {"status": "recorded", "manifest": relations["info"].get("manifest"),
            "items": [{key: row.get(key) for key in ("relation", "target_number", "target_node_id", "created_at")}
                      for row in targeted],
            "untargeted_events": len(rows) - len(targeted)}


def _github(record: dict, state: dict, relations: dict | None) -> dict:
    number, node = record.get("number"), record.get("node_id")
    companions, repository = state["companions"], state["info"].get("lock_repository")
    work_kind = "unknown"
    if companions is not None and repository:
        if number in companions.get("pull-request-summary", ()):
            work_kind = "pull-request"
        elif number in companions.get("issue", ()):
            work_kind = "issue"
    short = {"issue": "issue", "pull-request": "pr"}.get(work_kind)
    return {"identity": f"github:{repository}:{short}:{number}" if short else (f"github-node:{node}" if node else None),
            "node_identity": f"github-node:{node}" if node else None, "record_kind": STREAMS["github"].kind,
            "work_item_kind": work_kind,
            **{key: record.get(key) for key in ("number", "title", "state", "labels", "created_at", "closed_at",
                                                  "comments", "html_url")},
            "duplicate_identity": id(record) in state["duplicated"], "relations": _relations(node, relations)}


def _sourceforge(record: dict, state: dict) -> dict:
    tracker, ticket = record.get("tracker"), record.get("ticket_num")
    return {"identity": f"sourceforge:tei:{tracker}:{ticket}",
            **{key: record.get(key) for key in ("object_id", "tracker", "ticket_num", "summary", "status", "labels",
                                                  "created_date", "modified_date", "comment_count", "private")},
            "related_artifacts": record.get("related_artifacts") or [],
            "migration": {"status": "unknown", "detail": MIGRATION_UNKNOWN},
            "raw_pointers": [r.get("raw_path") for r in record.get("raw_responses") or [] if r.get("raw_path")],
            "raw_availability": "unknown", "duplicate_identity": id(record) in state["duplicated"]}


def _message(record: dict, state: dict) -> dict:
    message = record.get("message_id")
    return {"identity": f"tei-l:psu:{message}",
            **{key: record.get(key) for key in ("message_id", "month", "subject", "date", "archive_url",
                                                  "in_reply_to", "thread_position")},
            "raw_pointer": record.get("raw_path"), "raw_sha256": record.get("raw_sha256"),
            "raw_availability": "unknown", "duplicate_identity": id(record) in state["duplicated"]}


def _subject_groups(matches: list[dict]) -> list[dict]:
    groups: dict[str, dict] = {}
    for match in matches:
        key = " ".join(SUBJECT_PREFIX.sub("", match["subject"] or "").split()).casefold()
        group = groups.setdefault(key, {"subject_key": key, "messages": 0, "months": set()})
        group["messages"] += 1
        group["months"].add(match["month"])
    return [{**group, "months": sorted(group["months"])} for _, group in sorted(groups.items())]


def _atlas(declared: dict, rows: list[dict], gaps: list) -> list[dict]:
    category = declared.get("category")
    pool = [row for row in rows if not category or row.get("category") == category]
    if "ident" in declared:
        selected = [row for row in pool if row.get("ident") == declared["ident"]]
    elif "member_of" in declared:
        member_of = declared["member_of"]
        target = [row for row in rows if row.get("ident") == member_of]
        if not target:
            gaps.append({"code": "membership-target-not-declared",
                         "detail": member_of + " has no declaration in the atlas."})
        elif target[0].get("category") != "classSpec":
            gaps.append({"code": "membership-target-not-a-class",
                         "detail": member_of + " is declared as " + str(target[0].get("category")) + "."})
        selected = [row for row in pool if any(c.get("key") == member_of for c in row.get("classes_declared") or [])]
    else:
        name = declared["attribute"]
        selected = [row for row in pool if any(a.get("ident") == name for a in row.get("local_attributes") or [])]
    matches = []
    for row in sorted(selected, key=lambda item: (str(item.get("ident")), str(item.get("category")))):
        source = row.get("source") or {}
        match = {"ident": row.get("ident"), "category": row.get("category"), "module": row.get("module_declared"),
                 "source_path": source.get("path"), "source_commit": source.get("commit"),
                 "source_sha256": source.get("sha256")}
        if "attribute" in declared:
            match["attribute_locators"] = [a.get("locator") for a in row.get("local_attributes") or []
                                           if a.get("ident") == declared["attribute"]]
        matches.append(match)
    return matches


def _run(declared: dict, loaded: dict, relations: dict | None) -> dict:
    stream, state = declared["stream"], loaded[declared["stream"]]
    result = {"id": declared["id"], "declaration": declared, "stream": stream, "count": None, "matches": None,
              "gaps": [gap for gap in state["gaps"] if gap["code"] == "stream-missing"]}
    rows = state["rows"]
    if rows is None:
        return result
    if stream == "atlas":
        matches = _atlas(declared, rows, result["gaps"])
        result["limits"] = [ATLAS_LIMIT]
    else:
        if "label" in declared:
            label_field = STREAMS[stream].label_field
            selected = [row for row in rows if declared["label"] in (row.get(label_field) or [])]
        else:
            regex = re.compile(declared["pattern"], re.I if declared["ignore_case"] else 0)
            selected = [row for row in rows if regex.search(str(row.get(declared["field"]) or ""))]
        if stream == "github":
            matches = [_github(row, state, relations) for row in selected]
        elif stream == "sourceforge":
            matches = [_sourceforge(row, state) for row in selected]
        else:
            matches = [_message(row, state) for row in selected]
            result.update(subject_groups=_subject_groups(matches), subject_groups_note=SUBJECT_NOTE)
    result.update(count=len(matches), matches=matches)
    return result


def select(root: Path, queries: list[dict], *, declaration: dict | None = None) -> dict:
    """Run declared queries read-only against the tracked snapshot at ``root``."""
    root = Path(root)
    declared = [_check(query, position) for position, query in enumerate(queries, 1)]
    if not declared:
        raise ValueError("No query declared")
    if len({query["id"] for query in declared}) != len(declared):
        raise ValueError("Query ids must be unique")
    needed = {query["stream"] for query in declared}
    if "github" in needed:
        needed.add("github-relations")
    loaded = {name: _load(root, name) for name in sorted(needed)}
    relations = loaded.get("github-relations")
    if relations and relations["rows"] is not None:
        relations["by_source"] = {}
        for row in relations["rows"]:
            relations["by_source"].setdefault(row.get("source_node_id"), []).append(row)
    streams = {name: loaded[name]["info"] for name in sorted(needed)}
    gaps = [{"stream": name, **gap} for name in sorted(needed) for gap in loaded[name]["gaps"]]
    return {"schema_version": 1, "generator": GENERATOR, "use": USE, "instruction_trust": "none",
            "declaration": declaration, "queries": [_run(query, loaded, relations) for query in declared],
            "snapshot": {"streams": streams, "gaps": gaps}}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run declared read-only selection queries over tracked snapshots.")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--queries", type=Path, help="YAML or JSON list of declared queries, or a mapping with queries")
    for flag, _, _ in INLINE:
        parser.add_argument("--" + flag, action="append", default=[])
    parser.add_argument("--case-sensitive", action="store_true", help="match inline patterns case-sensitively")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    queries, declaration = [], None
    if args.queries:
        data = args.queries.read_bytes()
        content = yaml.safe_load(data)
        queries = list((content.get("queries") if isinstance(content, dict) else content) or [])
        declaration = {"path": args.queries.as_posix(), "sha256": _sha256(data)}
    for flag, stream, key in INLINE:
        for position, value in enumerate(getattr(args, flag.replace("-", "_")), 1):
            query = {"id": f"{flag}-{position}", "stream": stream, key: value}
            if key == "pattern":
                query["ignore_case"] = not args.case_sensitive
            queries.append(query)
    try:
        result = select(args.root, queries, declaration=declaration)
    except ValueError as error:
        parser.error(str(error))
    text = json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8", newline="\n")
    else:
        with contextlib.suppress(AttributeError, ValueError):
            sys.stdout.reconfigure(encoding="utf-8")
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
