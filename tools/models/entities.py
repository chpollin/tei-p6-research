"""Executable entity extension 0.2; see experiments/entities_v02/spec.json.

Section 14 of knowledge/text-model.md is the contract, built on the claim
pattern of section 13. The extension adds the collections entities, names,
denotations and statements, the nested alignment claims, the package fields
base and former_bases, the optional concept of an annotation and the concept
role statement.

Validation runs the unchanged v0.1 validator over a projection of the package
that hides every additive field, then checks the extension itself, so one
implementation of the v0.1 contract serves both versions. Diagnostics
establish structural consistency only, never editorial truth; an alignment or
a denotation entails nothing. Every public operation is nonmutating.
"""

from __future__ import annotations

import calendar
import copy
import datetime
import json
import re
from typing import Any

from tools.models.abstract_text import COLLECTIONS as BASE_COLLECTIONS
from tools.models.abstract_text import ID, check_revision, validate_model

MODEL_VERSION = "0.2"
BASE_MODEL_VERSION = "0.1"
NEW_COLLECTIONS = ("entities", "names", "denotations", "statements")
PACKAGE_FIELDS = ("base", "former_bases")
CARRIERS = ("concepts", "agents", "entities")
ENTITY_KINDS = ("person", "group", "place", "event", "object", "other")
STATEMENT_KINDS = ("trait", "state", "event", "relation")
NAME_PART_KINDS = ("surname", "forename", "role-name", "add-name", "name-link", "gen-name")
ALIGNMENT_RELATIONS = ("exact", "close", "broader", "narrower")
CLAIM_STATUSES = ("proposed", "asserted", "withdrawn")
CERTAINTIES = ("high", "medium", "low")
CONCEPT_ROLES = ("node", "relation", "statement")
MENTION_CONCEPTS = (
    {
        "id": "en-proper-noun",
        "label": "Proper noun",
        "definition": "The selected extent is a proper noun or proper-noun phrase used to refer.",
        "applies_to": "node",
    },
    {
        "id": "en-referring-string",
        "label": "Referring string",
        "definition": "The selected extent is a referring string that is no proper noun, "
        "such as a description or a title used to refer.",
        "applies_to": "node",
    },
    {
        "id": "en-pronoun",
        "label": "Pronoun",
        "definition": "The selected extent is a pronoun used to refer.",
        "applies_to": "node",
    },
)
MENTION_CONCEPT_IDS = tuple(concept["id"] for concept in MENTION_CONCEPTS)
CLAIM_FIELDS = ("created", "status", "certainty", "valid", "supersedes")
V01_CLAIM_COLLECTIONS = ("continuities", "readings", "annotations", "relations")
# Subject field of every claim kind; a statement's subject is its participant set.
SUBJECTS = {"names": "entity", "denotations": "mention", "statements": "participants",
            "alignments": "carrier", "former_bases": "package", "continuities": "text",
            "readings": "version", "annotations": "selection", "relations": "source"}
_REQUIRED = {"id", "agent", "created", "status"}
_OPTIONAL = {"certainty", "valid", "supersedes"}
FIELDS = {
    "entities": ({"id", "label", "kind"}, {"alignments"}),
    "names": (_REQUIRED | {"entity", "form", "language"}, _OPTIONAL | {"parts"}),
    "denotations": (_REQUIRED | {"mention", "entity"}, set(_OPTIONAL)),
    "statements": (_REQUIRED | {"kind", "type", "participants"}, _OPTIONAL | {"value"}),
    "alignments": (_REQUIRED | {"iri", "relation"}, set(_OPTIONAL)),
    "former_bases": (_REQUIRED | {"base"}, set(_OPTIONAL)),
}
EXTENSION_DIAGNOSTICS = (
    "E_ALIGNMENT", "E_BASE", "E_CLAIM_CYCLE", "E_CLAIM_FIELD", "E_CLAIM_REWRITE",
    "E_CLAIM_SUPERSESSION", "E_ENTITY_KIND", "E_LANGUAGE", "E_MENTION", "E_NAME_PART",
    "E_PARTICIPANTS", "E_STATEMENT_KIND", "W_UNDENOTED",
)
DIAGNOSTICS = tuple(sorted({
    "E_SHAPE", "E_ID", "E_DUPLICATE_ID", "E_REFERENCE", "E_TYPE", "E_HASH", "E_VERSION_CYCLE",
    "E_CONTINUITY", "E_SELECTOR", "E_BOUNDS", "E_QUOTE", "E_READING_TARGET", "E_READING_PARENT",
    "E_READING_CYCLE", "E_CONTAINMENT", "E_SIBLING_OVERLAP", "E_VERSION_REWRITE",
    "W_ABSENT", "W_AMBIGUOUS", *EXTENSION_DIAGNOSTICS,
}))

_LANGUAGE = re.compile(r"[A-Za-z]{2,3}(-[A-Za-z0-9]{1,8})*\Z")
_INSTANT = re.compile(r"([0-9]{4})-([0-9]{2})-([0-9]{2})T([0-9]{2}):([0-9]{2}):([0-9]{2})(\.[0-9]+)?Z\Z")
_DATE = re.compile(r"([0-9]{4})(?:-([0-9]{2})(?:-([0-9]{2}))?)?\Z")
# Form check only: a scheme and no whitespace, control or RFC 3987 delimiter character.
_IRI = re.compile(r"[A-Za-z][A-Za-z0-9+.-]*:[^\s\x00-\x20\x7f<>\"{}|\\^`]+\Z")


def _text(value: Any) -> bool:
    return type(value) is str and bool(value)


def _id(value: Any) -> bool:
    return type(value) is str and ID.fullmatch(value) is not None


def _one_of(value: Any, options: tuple[str, ...]) -> bool:
    return type(value) is str and value in options


def _instant(value: Any) -> bool:
    """RFC 3339 date-time with a Z designator, checked lexically and for calendar validity."""
    match = _INSTANT.fullmatch(value) if type(value) is str else None
    if match is None:
        return False
    year, month, day, hour, minute, second = (int(part) for part in match.groups()[:6])
    try:
        datetime.date(year, month, day)
    except ValueError:
        return False
    return hour <= 23 and minute <= 59 and second <= 60  # RFC 3339 admits the leap second


def _bound(value: Any, *, end: bool) -> tuple[int, int, int] | None:
    """Expand a year, month or day date to the first or last day of its calendar unit."""
    match = _DATE.fullmatch(value) if type(value) is str else None
    if match is None:
        return None
    year, month, day = (int(part) if part is not None else None for part in match.groups())
    if month is None:
        month = 12 if end else 1
    elif not 1 <= month <= 12:
        return None
    if day is None:
        day = calendar.monthrange(year, month)[1] if end else 1
    try:
        datetime.date(year, month, day)
    except ValueError:
        return None
    return (year, month, day)


def _iri(value: Any) -> bool:
    return type(value) is str and _IRI.fullmatch(value) is not None


def _base_iri(value: Any) -> bool:
    """Base grammar of section 13: an IRI without a query, ending in '/' or '#'."""
    return (_iri(value) and "?" not in value and value[-1] in "/#"
            and value.count("#") == (1 if value.endswith("#") else 0))


def _ordered(diagnostics: list[dict]) -> list[dict]:
    return [{"code": code, "path": path} for path, code in sorted(
        {(item["path"], item["code"]) for item in diagnostics}
    )]


def _has_errors(diagnostics: list[dict]) -> bool:
    return any(item["code"].startswith("E_") for item in diagnostics)


def _result(diagnostics: list[dict], resolutions: dict | None) -> dict:
    ordered = _ordered(diagnostics)
    valid = not _has_errors(ordered)
    return {"valid": valid,
            "all_selections_resolved": valid and all(
                item["status"] == "resolved" for item in (resolutions or {}).values()),
            "diagnostics": ordered,
            "resolutions": resolutions if valid and resolutions is not None else {}}


def _records(package: Any, kind: str) -> list:
    collection = package.get(kind) if type(package) is dict else None
    return collection if type(collection) is list else []


def _claim_records(package: Any):
    """Yield (kind, path, carrier, record) for every claim record of a 0.2 package."""
    for kind in (*V01_CLAIM_COLLECTIONS, "names", "denotations", "statements", "former_bases"):
        for i, record in enumerate(_records(package, kind)):
            if type(record) is dict:
                yield kind, f"/{kind}/{i}", None, record
    for carrier in CARRIERS:
        for i, holder in enumerate(_records(package, carrier)):
            if type(holder) is not dict or type(holder.get("alignments")) is not list:
                continue
            for j, record in enumerate(holder["alignments"]):
                if type(record) is dict:
                    yield "alignments", f"/{carrier}/{i}/alignments/{j}", holder.get("id"), record


def _extension_ids(package: Any) -> set[str]:
    identifiers = {record["id"] for record in _records(package, "entities")
                   if type(record) is dict and _id(record.get("id"))}
    for _, _, _, record in _claim_records(package):
        if _id(record.get("id")):
            identifiers.add(record["id"])
    return identifiers - {record["id"] for kind in V01_CLAIM_COLLECTIONS
                          for record in _records(package, kind)
                          if type(record) is dict and _id(record.get("id"))}


def _mentions(package: Any) -> dict[str, str]:
    """Return the ID and path of every reading node or annotation with a mention concept."""
    found = {}
    for i, record in enumerate(_records(package, "annotations")):
        if type(record) is dict and _one_of(record.get("concept"), MENTION_CONCEPT_IDS):
            found[record["id"]] = f"/annotations/{i}"
    for i, reading in enumerate(_records(package, "readings")):
        for j, node in enumerate(reading.get("nodes", []) if type(reading) is dict else []):
            if type(node) is dict and _one_of(node.get("type"), MENTION_CONCEPT_IDS):
                found[node["id"]] = f"/readings/{i}/nodes/{j}"
    return found


def _envelope(package: Any) -> tuple[bool, list[dict]]:
    """Check the package frame; a fatal defect stops before the base projection is built."""
    required = {"model_version", *BASE_COLLECTIONS, *NEW_COLLECTIONS}
    if (type(package) is not dict or not required.issubset(package)
            or not set(package).issubset(required | set(PACKAGE_FIELDS))):
        return True, [{"code": "E_SHAPE", "path": ""}]
    fatal = [{"code": "E_SHAPE", "path": "/" + kind}
             for kind in (*BASE_COLLECTIONS, *NEW_COLLECTIONS, "former_bases")
             if kind in package and type(package[kind]) is not list]
    if fatal:
        return True, fatal
    if package["model_version"] != MODEL_VERSION:
        return False, [{"code": "E_SHAPE", "path": "/model_version"}]
    return False, []


def _projection(package: dict) -> dict:
    """Return the v0.1 package hidden inside a 0.2 package.

    The nine v0.1 collections keep their order, so every base diagnostic path is
    also a path in the 0.2 package. Two rewrites keep the base validator usable:
    a concept with the new role `statement` is projected to `node`, and the
    extension re-checks the role of every node and annotation concept; a relation
    endpoint naming an extension record is redirected to the relation itself,
    because a relation may link any package record while the base index holds
    v0.1 records only.
    """
    base = {"model_version": BASE_MODEL_VERSION}
    for kind in BASE_COLLECTIONS:
        base[kind] = copy.deepcopy(package[kind])
    for record in base["concepts"]:
        if type(record) is dict:
            record.pop("alignments", None)
            if record.get("applies_to") == "statement":
                record["applies_to"] = "node"
    for record in base["agents"]:
        if type(record) is dict:
            record.pop("alignments", None)
    for kind in V01_CLAIM_COLLECTIONS:
        for record in base[kind]:
            if type(record) is dict:
                for field in CLAIM_FIELDS:
                    record.pop(field, None)
    for record in base["annotations"]:
        if type(record) is dict:
            record.pop("concept", None)
    extension = _extension_ids(package)
    for record in base["relations"]:
        if type(record) is dict and _id(record.get("id")):
            for endpoint in ("source", "target"):
                value = record.get(endpoint)
                if type(value) is str and value in extension:
                    record[endpoint] = record["id"]
    return base


class _Extension:
    """Section 14 checks over a package whose v0.1 projection already validated."""

    def __init__(self, package: dict) -> None:
        self.package = package
        self.errors: list[dict] = []
        self.ids: set[str] = set()
        self.concepts: dict[str, dict] = {}
        self.agents: set[str] = set()
        self.entities: dict[str, dict] = {}
        self.occurrences: set[str] = set()
        self.mentions = _mentions(package)
        self.claims: dict[str, dict] = {}
        self.superseded: set[str] = set()

    def error(self, code: str, path: str) -> None:
        self.errors.append({"code": code, "path": path})

    def index(self) -> None:
        for kind in BASE_COLLECTIONS:
            for record in self.package[kind]:
                self.ids.add(record["id"])
                if kind == "concepts":
                    self.concepts[record["id"]] = record
                elif kind == "agents":
                    self.agents.add(record["id"])
                elif kind == "annotations":
                    self.occurrences.add(record["id"])
                elif kind == "readings":
                    for node in record["nodes"]:
                        self.ids.add(node["id"])
                        self.occurrences.add(node["id"])

    def shape(self, record: Any, kind: str, path: str) -> bool:
        required, optional = FIELDS[kind]
        if (type(record) is not dict or not required.issubset(record)
                or not set(record).issubset(required | optional)):
            self.error("E_SHAPE", path)
            return False
        return True

    def identity(self, record: dict, path: str) -> None:
        if not _id(record["id"]):
            self.error("E_ID", path + "/id")
        elif record["id"] in self.ids:
            self.error("E_DUPLICATE_ID", path + "/id")
        else:
            self.ids.add(record["id"])

    def reference(self, record: dict, key: str, allowed, path: str) -> bool:
        """A reference field holds an ID resolving in its category; anything else fails."""
        value = record.get(key)
        if type(value) is not str or value not in allowed:
            self.error("E_REFERENCE", f"{path}/{key}")
            return False
        return True

    def role(self, record: dict, key: str, expected: str, path: str) -> None:
        if self.reference(record, key, self.concepts, path) and (
                self.concepts[record[key]]["applies_to"] != expected):
            self.error("E_TYPE", f"{path}/{key}")

    def validity(self, scope: Any, path: str) -> None:
        if (type(scope) is not dict or not set(scope).issubset({"from", "until"})
                or not scope):
            self.error("E_CLAIM_FIELD", path)
            return
        bounds = {}
        for key, end in (("from", False), ("until", True)):
            if key in scope:
                bounds[key] = _bound(scope[key], end=end)
                if bounds[key] is None:
                    self.error("E_CLAIM_FIELD", f"{path}/{key}")
        if (bounds.get("from") is not None and bounds.get("until") is not None
                and bounds["from"] > bounds["until"]):
            self.error("E_CLAIM_FIELD", path)

    def pattern(self, record: dict, path: str) -> None:
        """The section 13 claim fields, checked once for every claim kind."""
        if "created" in record and not _instant(record["created"]):
            self.error("E_CLAIM_FIELD", path + "/created")
        if "status" in record and not _one_of(record["status"], CLAIM_STATUSES):
            self.error("E_CLAIM_FIELD", path + "/status")
        if "certainty" in record and not _one_of(record["certainty"], CERTAINTIES):
            self.error("E_CLAIM_FIELD", path + "/certainty")
        if "valid" in record:
            self.validity(record["valid"], path + "/valid")
        if "supersedes" in record:
            # An unresolvable entry is a reference failure of the supersession stage.
            listed = record["supersedes"]
            named = [item for item in listed if type(item) is str] if type(listed) is list else []
            if type(listed) is not list or len(named) != len(set(named)):
                self.error("E_SHAPE", path + "/supersedes")

    def parts(self, record: dict, path: str) -> None:
        value = record["parts"]
        if type(value) is not list:
            self.error("E_NAME_PART", path + "/parts")
            return
        for i, part in enumerate(value):
            subpath = f"{path}/parts/{i}"
            if type(part) is not dict or set(part) != {"kind", "form"}:
                self.error("E_NAME_PART", subpath)
                continue
            if not _one_of(part["kind"], NAME_PART_KINDS):
                self.error("E_NAME_PART", subpath + "/kind")
            if not _text(part["form"]):
                self.error("E_NAME_PART", subpath + "/form")

    def participants(self, record: dict, path: str) -> Any:
        """Check the participant list and return the subject, the set of its entities."""
        value = record["participants"]
        if type(value) is not list or not value:
            self.error("E_PARTICIPANTS", path + "/participants")
            return None
        subject, seen, sound = set(), set(), True
        for i, participant in enumerate(value):
            subpath = f"{path}/participants/{i}"
            if (type(participant) is not dict or set(participant) != {"entity", "role"}
                    or not _text(participant["role"]) or not _id(participant.get("entity"))):
                self.error("E_PARTICIPANTS", subpath)
                sound = False
                continue
            pair = (participant["entity"], participant["role"])
            if pair in seen:
                self.error("E_PARTICIPANTS", subpath)
                sound = False
            seen.add(pair)
            if self.reference(participant, "entity", self.entities, subpath):
                subject.add(participant["entity"])
            else:
                sound = False
        return tuple(sorted(subject)) if sound else None

    def record(self, kind: str, record: Any, path: str, carrier: Any = None) -> None:
        if not self.shape(record, kind, path):
            return
        self.identity(record, path)
        subject: Any = carrier
        if kind == "entities":
            if not _text(record["label"]):
                self.error("E_SHAPE", path + "/label")
            if not _one_of(record["kind"], ENTITY_KINDS):
                self.error("E_ENTITY_KIND", path + "/kind")
            self.entities[record["id"]] = record
            return
        self.reference(record, "agent", self.agents, path)
        self.pattern(record, path)
        if kind == "names":
            subject = record["entity"] if self.reference(record, "entity", self.entities, path) else None
            if not _text(record["form"]):
                self.error("E_SHAPE", path + "/form")
            if type(record["language"]) is not str or _LANGUAGE.fullmatch(record["language"]) is None:
                self.error("E_LANGUAGE", path + "/language")
            if "parts" in record:
                self.parts(record, path)
        elif kind == "denotations":
            subject = record["mention"] if self.reference(record, "mention", self.occurrences, path) else None
            if subject is not None and subject not in self.mentions:
                self.error("E_MENTION", path + "/mention")
            self.reference(record, "entity", self.entities, path)
        elif kind == "statements":
            if not _one_of(record["kind"], STATEMENT_KINDS):
                self.error("E_STATEMENT_KIND", path + "/kind")
            self.role(record, "type", "statement", path)
            subject = self.participants(record, path)
            if "value" in record and not _text(record["value"]):
                self.error("E_SHAPE", path + "/value")
        elif kind == "alignments":
            if not _iri(record["iri"]):
                self.error("E_ALIGNMENT", path + "/iri")
            if not _one_of(record["relation"], ALIGNMENT_RELATIONS):
                self.error("E_ALIGNMENT", path + "/relation")
        elif kind == "former_bases":
            subject = ""
            if not _base_iri(record["base"]):
                self.error("E_BASE", path + "/base")
        if _id(record.get("id")):
            self.claims.setdefault(record["id"], {
                "kind": kind, "agent": record.get("agent"), "subject": subject,
                "record": record, "path": path, "container": path.rsplit("/", 1)[0]})

    def records(self) -> None:
        for i, record in enumerate(self.package["concepts"]):
            expected = next((item for item in MENTION_CONCEPTS if item["id"] == record["id"]), None)
            # A reserved concept may carry alignments; its four defining fields may not change.
            if expected is not None and {key: value for key, value in record.items()
                                         if key != "alignments"} != expected:
                self.error("E_MENTION", f"/concepts/{i}")
        for kind in NEW_COLLECTIONS:
            for i, record in enumerate(self.package[kind]):
                self.record(kind, record, f"/{kind}/{i}")
        for carrier in CARRIERS:
            for i, holder in enumerate(self.package[carrier]):
                if "alignments" not in holder:
                    continue
                path = f"/{carrier}/{i}/alignments"
                if type(holder["alignments"]) is not list:
                    self.error("E_SHAPE", path)
                    continue
                for j, record in enumerate(holder["alignments"]):
                    self.record("alignments", record, f"{path}/{j}", holder["id"])
        for i, record in enumerate(self.package.get("former_bases", [])):
            self.record("former_bases", record, f"/former_bases/{i}")

    def occurrence_concepts(self) -> None:
        """The base validator sees the projected role, so the real role is checked here."""
        for i, record in enumerate(self.package["annotations"]):
            if "concept" in record:
                self.role(record, "concept", "node", f"/annotations/{i}")
        for i, reading in enumerate(self.package["readings"]):
            for j, node in enumerate(reading["nodes"]):
                if self.concepts[node["type"]]["applies_to"] != "node":
                    self.error("E_TYPE", f"/readings/{i}/nodes/{j}/type")

    def package_fields(self) -> None:
        if "base" in self.package and not _base_iri(self.package["base"]):
            self.error("E_BASE", "/base")

    def v01_claims(self) -> None:
        """Register the four v0.1 claim kinds, whose pattern fields stay optional."""
        for kind in V01_CLAIM_COLLECTIONS:
            for i, record in enumerate(self.package[kind]):
                path = f"/{kind}/{i}"
                self.pattern(record, path)
                self.claims.setdefault(record["id"], {
                    "kind": kind, "agent": record["agent"], "subject": record[SUBJECTS[kind]],
                    "record": record, "path": path, "container": f"/{kind}"})

    def supersession(self) -> None:
        graph: dict[str, list[str]] = {}
        for identifier, claim in self.claims.items():
            targets = []
            field = claim["path"] + "/supersedes"
            listed = claim["record"].get("supersedes", [])
            for j, target in enumerate(listed if type(listed) is list else []):
                other = self.claims.get(target) if type(target) is str else None
                if other is None:
                    self.error("E_REFERENCE", f"{field}/{j}")
                elif (other["kind"] != claim["kind"] or other["agent"] != claim["agent"]
                        or other["subject"] != claim["subject"] or claim["subject"] is None):
                    self.error("E_CLAIM_SUPERSESSION", field)
                else:
                    targets.append(target)
                    self.superseded.add(target)
            if claim["record"].get("status") == "withdrawn" and not targets:
                self.error("E_CLAIM_SUPERSESSION", field)
            graph[identifier] = targets
        for identifier in _cyclic(graph):
            self.error("E_CLAIM_CYCLE", self.claims[identifier]["container"])

    def warnings(self) -> None:
        """A claim is current when no claim supersedes it, its status notwithstanding."""
        denoted = {record["mention"] for record in self.package["denotations"]
                   if type(record) is dict and _id(record.get("mention"))
                   and record.get("id") not in self.superseded}
        for identifier, path in self.mentions.items():
            if identifier not in denoted:
                self.error("W_UNDENOTED", path)

    def run(self) -> list[dict]:
        self.index()
        self.package_fields()
        self.records()
        self.occurrence_concepts()
        self.v01_claims()
        self.supersession()
        # The warning stage of section 5 runs over an otherwise error-free package.
        if not _has_errors(self.errors):
            self.warnings()
        return self.errors


def _cyclic(graph: dict[str, list[str]]) -> list[str]:
    """Return every node on or leading into a cycle, by removing sinks until none remain."""
    remaining = {node: [target for target in targets if target in graph]
                 for node, targets in graph.items()}
    while True:
        sinks = [node for node, targets in remaining.items() if not targets]
        if not sinks:
            return sorted(remaining)
        for node in sinks:
            del remaining[node]
        for targets in remaining.values():
            targets[:] = [target for target in targets if target in remaining]


def validate_extension(package: Any) -> dict:
    """Validate a 0.2 package: the v0.1 contract on its projection, then section 14."""
    fatal, diagnostics = _envelope(package)
    if fatal:
        return _result(diagnostics, None)
    base = validate_model(_projection(package))
    diagnostics = diagnostics + list(base["diagnostics"])
    if not base["valid"]:
        return _result(diagnostics, None)
    return _result(diagnostics + _Extension(package).run(), base["resolutions"])


def canonical_bytes(package: Any) -> bytes:
    """Return canonical UTF-8 JSON under R11; raise ValueError for an invalid package."""
    result = validate_extension(package)
    if not result["valid"]:
        raise ValueError(result["diagnostics"])
    canonical = copy.deepcopy(package)
    for kind in (*BASE_COLLECTIONS, *NEW_COLLECTIONS):
        canonical[kind].sort(key=lambda item: item["id"])
    for version in canonical["versions"]:
        version["parents"].sort()
    for continuity in canonical["continuities"]:
        continuity["versions"].sort()
    for reading in canonical["readings"]:
        reading["nodes"].sort(key=lambda item: item["id"])
    for carrier in CARRIERS:
        for holder in canonical[carrier]:
            if "alignments" in holder:
                holder["alignments"].sort(key=lambda item: item["id"])
    if "former_bases" in canonical:
        canonical["former_bases"].sort(key=lambda item: item["id"])
    for statement in canonical["statements"]:
        statement["participants"].sort(key=lambda item: (item["entity"], item["role"]))
    for _, _, _, record in _claim_records(canonical):
        if "supersedes" in record:
            record["supersedes"].sort()
    return json.dumps(canonical, ensure_ascii=False, sort_keys=True, separators=(",", ":"),
                      allow_nan=False).encode("utf-8")


def equivalent(left: Any, right: Any) -> bool:
    """Compare valid 0.2 packages under R11; invalid inputs raise ValueError."""
    return canonical_bytes(left) == canonical_bytes(right)


def check_claim_revision(before: Any, after: Any) -> dict:
    """Check two packages in a caller-declared shared ID scope for rewritten records.

    A claim of a valid earlier package must survive unchanged under its ID, and a
    reused version ID keeps its frozen v0.1 information. Callers must not infer a
    rewrite from coincidental local IDs of independent packages.
    """
    diagnostics: list[dict] = []
    results = [validate_extension(package) for package in (before, after)]
    for prefix, result in zip(("/before", "/after"), results, strict=True):
        diagnostics.extend({"code": item["code"], "path": prefix + item["path"]}
                           for item in result["diagnostics"])
    if all(result["valid"] for result in results):
        diagnostics.extend(item for item in check_revision(_projection(before), _projection(after))
                           ["diagnostics"] if item["code"] == "E_VERSION_REWRITE")
    if results[0]["valid"]:
        later: dict[str, list[dict]] = {}
        for _, _, _, record in _claim_records(after):
            if type(record.get("id")) is str:
                later.setdefault(record["id"], []).append(record)
        for _, path, _, record in _claim_records(before):
            if later.get(record["id"]) != [record]:
                diagnostics.append({"code": "E_CLAIM_REWRITE", "path": "/before" + path})
    return {"valid": not _has_errors(diagnostics), "diagnostics": _ordered(diagnostics)}


def _current(package: dict, kind: str, *, include_withdrawn: bool) -> list[dict]:
    """Claims of one collection that no claim supersedes, withdrawal only on request."""
    superseded = {target for _, _, _, record in _claim_records(package)
                  for target in record.get("supersedes", [])}
    return [record for record in package[kind] if record["id"] not in superseded
            and (include_withdrawn or record["status"] != "withdrawn")]


def denotations_of(package: Any, mention_id: Any, include_withdrawn: bool = False) -> dict:
    """Current denotation claims of one mention, with the label and kind of their entity.

    Ordered by agent and then by claim ID. The order conveys no authority and the
    result decides nothing between agents; coexisting claims are all returned.
    """
    validation = validate_extension(package)
    if not validation["valid"]:
        return {"diagnostics": validation["diagnostics"], "denotations": None}
    if type(mention_id) is not str or mention_id not in _mentions(package):
        return {"diagnostics": [{"code": "E_MENTION", "path": "/operation/mention"}],
                "denotations": None}
    entities = {record["id"]: record for record in package["entities"]}
    selected = sorted((record for record in _current(package, "denotations",
                                                     include_withdrawn=include_withdrawn)
                       if record["mention"] == mention_id),
                      key=lambda record: (record["agent"], record["id"]))
    return {"diagnostics": [], "denotations": [
        copy.deepcopy(record) | {"label": entities[record["entity"]]["label"],
                                 "kind": entities[record["entity"]]["kind"]}
        for record in selected]}


def _validity_order(record: dict) -> tuple:
    """Claims without validity first, then ascending by from, then by until, then by ID.

    Dates compare as strings, which orders a calendar unit before its subunits and
    follows calendar order for the grammar of section 13.
    """
    scope = record.get("valid")
    if scope is None:
        return (0, 0, "", 0, "", record["id"])
    start, end = scope.get("from"), scope.get("until")
    return (1, int(start is not None), start or "", int(end is None), end or "", record["id"])


def names_of(package: Any, entity_id: Any, include_withdrawn: bool = False) -> dict:
    """Current name claims of one entity in validity order, without a base form."""
    validation = validate_extension(package)
    if not validation["valid"]:
        return {"diagnostics": validation["diagnostics"], "names": None}
    if type(entity_id) is not str or not any(
            record["id"] == entity_id for record in package["entities"]):
        return {"diagnostics": [{"code": "E_REFERENCE", "path": "/operation/entity"}], "names": None}
    selected = [record for record in _current(package, "names", include_withdrawn=include_withdrawn)
                if record["entity"] == entity_id]
    return {"diagnostics": [], "names": copy.deepcopy(sorted(selected, key=_validity_order))}
