"""Validate and inspect source-attributed claims over the existing 0.2 model.

The contract lives in knowledge/identity-evidence.md. Exact source bytes are
provided by the caller; these operations never retrieve external resources or
judge whether a quotation supports a claim. Inputs remain unchanged.
"""

from __future__ import annotations

import copy
import hashlib
from itertools import pairwise
from typing import Any
from urllib.parse import urlsplit

from tools.models.entities import check_claim_revision, validate_extension

PROFILE = "identity-evidence-0.1"
PASSAGE = "ie-source-passage"
QUALIFICATION = "ie-source-qualification"
ASSESSMENT = "ie-assessment"
SUPPORT = "ie-supported-by"
QUALIFIES = "ie-qualified-by"
ASSESSES = "ie-assesses"
WORK = "ie-work-assignment"
HAND = "ie-hand-attribution"
CONTRIBUTOR = "ie-contributor"
ORIGIN = "ie-origin-date"
SENT = "ie-sent-date"
DATELINE = "ie-dateline"
REPORT_TYPES = (WORK, HAND, CONTRIBUTOR, ORIGIN, SENT, DATELINE)
SOURCE_FIELDS = {"version", "snapshot", "uri", "sha256", "start_byte", "end_byte", "xpath"}
RESERVED_CONCEPTS = tuple(
    {"id": identifier, "label": label, "definition": definition, "applies_to": role}
    for identifier, label, definition, role in (
        (PASSAGE, "Exact source passage", "An exact selected passage from a frozen source snapshot.", "node"),
        (QUALIFICATION, "Source qualification", "The source's literal qualification, without assigning the importer a certainty.", "node"),
        (ASSESSMENT, "Separate assessment", "An agent's reasoned assessment of a reported claim; it leaves the report unchanged.", "node"),
        (SUPPORT, "Has source passage", "The source claim cites the target passage; this link does not establish semantic support.", "relation"),
        (QUALIFIES, "Has source qualification", "The source claim retains the target source qualification verbatim.", "relation"),
        (ASSESSES, "Assesses report", "The source assessment addresses the target reported claim under the assessment agent's responsibility.", "relation"),
        (WORK, "Reported work assignment", "The catalogue assigns an artifact to a work; no text or artifact identity follows.", "statement"),
        (HAND, "Reported hand attribution", "The source attributes a described hand; the importer does not authenticate it.", "statement"),
        (CONTRIBUTOR, "Reported contribution", "The source records a person's contribution independently of hand identification.", "statement"),
        (ORIGIN, "Reported origin date", "The source encodes an origin date; no independent historical dating follows.", "statement"),
        (SENT, "Reported sent-action date", "The source encodes a date in sent-action metadata; actual dispatch is not independently established.", "statement"),
        (DATELINE, "Reported dateline", "The edition transcribes a dateline whose spelling is retained.", "statement"),
    )
)


def _result(diagnostics: list[dict]) -> dict:
    ordered = [{"code": code, "path": path} for path, code in sorted(
        {(item["path"], item["code"]) for item in diagnostics})]
    return {"valid": not any(item["code"].startswith("E_") for item in ordered),
            "diagnostics": ordered}


def _extent(resolution: dict) -> tuple[int, int] | None:
    targets = resolution.get("targets", [])
    if resolution.get("status") != "resolved" or len(targets) != 1 or targets[0]["kind"] != "region":
        return None
    segments = targets[0]["segments"]
    if not segments or any(left["end"] != right["start"] for left, right in pairwise(segments)):
        return None
    return segments[0]["start"], segments[-1]["end"]


def validate_profile(dossier: Any, snapshots: dict[str, bytes]) -> dict:
    diagnostics = []
    if (type(dossier) is not dict or set(dossier) != {"profile", "package", "sources"}
            or dossier["profile"] != PROFILE or type(dossier["sources"]) is not list):
        return _result([{"code": "E_PROFILE_SHAPE", "path": "/"}])
    package = dossier["package"]
    base = validate_extension(package)
    diagnostics.extend(base["diagnostics"])
    if not base["valid"]:
        return _result(diagnostics)

    concepts = {item["id"]: item for item in package["concepts"]}
    for concept in RESERVED_CONCEPTS:
        if concepts.get(concept["id"]) != concept:
            diagnostics.append({"code": "E_PROFILE_CONCEPT", "path": "/concepts/" + concept["id"]})
    versions = {item["id"]: item for item in package["versions"]}
    seen = set()
    for index, source in enumerate(dossier["sources"]):
        path = f"/sources/{index}"
        if (type(source) is not dict or set(source) != SOURCE_FIELDS
                or any(type(source[key]) is not str or not source[key]
                       for key in SOURCE_FIELDS - {"start_byte", "end_byte"})
                or type(source["start_byte"]) is not int or type(source["end_byte"]) is not int):
            diagnostics.append({"code": "E_SOURCE_SHAPE", "path": path})
            continue
        version = versions.get(source["version"])
        if version is None or source["version"] in seen:
            diagnostics.append({"code": "E_SOURCE_REFERENCE", "path": path})
        seen.add(source["version"])
        try:
            uri = urlsplit(source["uri"])
            if uri.scheme not in {"https", "http"} or not uri.netloc:
                raise ValueError("source URL is not absolute HTTP(S)")
        except ValueError:
            diagnostics.append({"code": "E_SOURCE_URI", "path": path})
        payload = snapshots.get(source["snapshot"])
        if type(payload) is not bytes or hashlib.sha256(payload).hexdigest() != source["sha256"]:
            diagnostics.append({"code": "E_SOURCE_HASH", "path": path})
            continue
        start, end = source["start_byte"], source["end_byte"]
        if not 0 <= start < end <= len(payload):
            diagnostics.append({"code": "E_SOURCE_BOUNDS", "path": path})
            continue
        try:
            content = payload[start:end].decode("utf-8")
        except UnicodeDecodeError:
            content = None
        if version is not None and content != version["content"]:
            diagnostics.append({"code": "E_SOURCE_CONTENT", "path": path})
    if seen != set(versions):
        diagnostics.append({"code": "E_SOURCE_COVERAGE", "path": "/sources"})

    annotations = {item["id"]: item for item in package["annotations"]}
    reports = {item["id"]: item for item in package["statements"] if item["type"] in REPORT_TYPES}
    selections = {item["id"]: item for item in package["selections"]}
    positions = {}
    for identifier, annotation in annotations.items():
        concept = annotation.get("concept")
        if concept not in {PASSAGE, QUALIFICATION, ASSESSMENT}:
            continue
        selection = selections[annotation["selection"]]
        extent = _extent(base["resolutions"][selection["id"]])
        if extent is None:
            diagnostics.append({"code": "E_EVIDENCE_TARGET", "path": "/annotations/" + identifier})
            continue
        positions[identifier] = (selection["version"], *extent)
        if concept in {PASSAGE, QUALIFICATION}:
            actual = versions[selection["version"]]["content"][extent[0]:extent[1]]
            if actual != annotation["body"] or "certainty" in annotation:
                diagnostics.append({"code": "E_EVIDENCE_LITERAL", "path": "/annotations/" + identifier})
        elif not annotation["body"].strip():
            diagnostics.append({"code": "E_ASSESSMENT_REASON", "path": "/annotations/" + identifier})

    supporting: dict[str, list[str]] = {identifier: [] for identifier in reports}
    qualifications: dict[str, list[str]] = {identifier: [] for identifier in reports}
    for index, link in enumerate(package["relations"]):
        if link["type"] not in {SUPPORT, QUALIFIES, ASSESSES}:
            continue
        path = f"/relations/{index}"
        if link["type"] == ASSESSES:
            annotation = annotations.get(link["source"])
            report = reports.get(link["target"])
            concept = ASSESSMENT
        else:
            report = reports.get(link["source"])
            annotation = annotations.get(link["target"])
            concept = PASSAGE if link["type"] == SUPPORT else QUALIFICATION
        if report is None or annotation is None or annotation.get("concept") != concept:
            diagnostics.append({"code": "E_EVIDENCE_ENDPOINT", "path": path})
            continue
        expected_agent = annotation["agent"] if concept == ASSESSMENT else report["agent"]
        if link["agent"] != expected_agent:
            diagnostics.append({"code": "E_EVIDENCE_AGENT", "path": path})
        if concept == PASSAGE:
            supporting[report["id"]].append(annotation["id"])
        elif concept == QUALIFICATION:
            qualifications[report["id"]].append(annotation["id"])
    entities = {item["id"]: item for item in package["entities"]}
    for identifier, report in reports.items():
        path = "/statements/" + identifier
        if not supporting[identifier]:
            diagnostics.append({"code": "E_EVIDENCE_REQUIRED", "path": path})
        if "certainty" in report:
            diagnostics.append({"code": "E_REPORTED_CERTAINTY", "path": path})
        if report["type"] == WORK:
            members = report["participants"]
            kinds = sorted((member["role"], entities[member["entity"]]["kind"]) for member in members)
            if kinds != [("artifact", "object"), ("work", "other")]:
                diagnostics.append({"code": "E_WORK_PARTICIPANTS", "path": path})
        for qualification in qualifications[identifier]:
            where = positions.get(qualification)
            supports = [positions[item] for item in supporting[identifier] if item in positions]
            if where is not None and not any(
                    where[0] == support[0] and support[1] <= where[1] < where[2] <= support[2]
                    for support in supports):
                diagnostics.append({"code": "E_QUALIFICATION_SCOPE", "path": path})
    return _result(diagnostics)


def inspect_claim(dossier: dict, claim_id: str, snapshots: dict[str, bytes]) -> dict:
    result = validate_profile(dossier, snapshots)
    if not result["valid"]:
        raise ValueError(result["diagnostics"])
    package = dossier["package"]
    report = next((item for item in package["statements"]
                   if item["id"] == claim_id and item["type"] in REPORT_TYPES), None)
    if report is None:
        raise ValueError("unknown profile report")
    origins = {item["version"]: item for item in dossier["sources"]}
    agents = {item["id"]: item for item in package["agents"]}
    selections = {item["id"]: item for item in package["selections"]}
    annotations = {item["id"]: item for item in package["annotations"]}
    output = {"claim": report, "record_agent": agents[report["agent"]],
              "source_support_review": "not-established-by-this-operation",
              "passages": [], "qualifications": [], "assessments": []}
    for link in sorted(package["relations"], key=lambda item: item["id"]):
        if link["source"] == claim_id and link["type"] in {SUPPORT, QUALIFIES}:
            annotation = annotations[link["target"]]
            selection = selections[annotation["selection"]]
            key = "passages" if link["type"] == SUPPORT else "qualifications"
            output[key].append({"annotation": annotation, "link": link,
                                "selection": selection, "origin": origins[selection["version"]]})
        elif link["target"] == claim_id and link["type"] == ASSESSES:
            annotation = annotations[link["source"]]
            output["assessments"].append({"annotation": annotation, "link": link,
                                           "agent": agents[annotation["agent"]]})
    return copy.deepcopy(output)


def check_profile_revision(before: dict, after: dict, snapshots: dict[str, bytes]) -> dict:
    """The caller declares a shared ID scope; original source descriptors are frozen."""
    diagnostics = []
    for name, dossier in (("before", before), ("after", after)):
        result = validate_profile(dossier, snapshots)
        diagnostics.extend({"code": item["code"], "path": f"/{name}" + item["path"]}
                           for item in result["diagnostics"])
    if any(item["code"].startswith("E_") for item in diagnostics):
        return _result(diagnostics)
    diagnostics.extend(check_claim_revision(before["package"], after["package"])["diagnostics"])
    later = {item["version"]: item for item in after["sources"]}
    for source in before["sources"]:
        if later.get(source["version"]) != source:
            diagnostics.append({"code": "E_SOURCE_REWRITE", "path": "/sources/" + source["version"]})
    later_entities = {item["id"]: item for item in after["package"]["entities"]}
    for entity in before["package"]["entities"]:
        if entity["id"] not in later_entities or later_entities[entity["id"]]["kind"] != entity["kind"]:
            diagnostics.append({"code": "E_IDENTITY_REWRITE", "path": "/entities/" + entity["id"]})
    return _result(diagnostics)
