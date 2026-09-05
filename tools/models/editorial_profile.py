"""Optional editorial provenance profile for Abstract Text Model 0.1.

See experiments/editorial_cases/profile.json. These attributed hypotheses do
not establish historical truth, technical parentage, continuity, or permission
to reanchor. Calling the base model alone does not enforce this profile.
"""

from __future__ import annotations

import copy
from typing import Any

from tools.models.abstract_text import check_revision, validate_model


PROFILE_VERSION = "editorial-provenance-0.1"
BASE_MODEL_VERSION = "0.1"
DERIVED_FROM = "ep-derived-from"
SUPERSEDES = "ep-supersedes"
RESERVED_CONCEPTS = (
    {
        "id": DERIVED_FROM,
        "label": "Historical derivation claim",
        "definition": "An agent's hypothesis that the source version derives historically "
        "from the target version; not a technical construction dependency or a continuity assertion.",
        "applies_to": "relation",
    },
    {
        "id": SUPERSEDES,
        "label": "Supersedes derivation claim",
        "definition": "The source derivation claim supersedes the target derivation claim "
        "for the same subject version and agent, retaining both claims without asserting historical truth.",
        "applies_to": "relation",
    },
)


def _result(diagnostics: list[dict]) -> dict:
    ordered = [{"code": code, "path": path} for path, code in sorted(
        {(item["path"], item["code"]) for item in diagnostics}
    )]
    return {"valid": not any(item["code"].startswith("E_") for item in ordered),
            "diagnostics": ordered}


def _cyclic(graph: dict[str, list[str]]) -> bool:
    """Kahn traversal supports long histories and multiple surviving branches."""
    incoming = dict.fromkeys(graph, 0)
    for targets in graph.values():
        for target in targets:
            incoming[target] += 1
    ready = [identifier for identifier, count in incoming.items() if count == 0]
    visited = 0
    while ready:
        identifier = ready.pop()
        visited += 1
        for target in graph[identifier]:
            incoming[target] -= 1
            if incoming[target] == 0:
                ready.append(target)
    return visited != len(graph)


def validate_profile(package: Any) -> dict:
    """Validate base structure and the optional profile, without resolving truth.

    Base diagnostics (including selection warnings) are retained. Profile
    relationship checks follow successful base validation so malformed fields
    cannot be mistaken for usable identifiers or references.
    """
    base = validate_model(package)
    diagnostics = list(base["diagnostics"])
    if not base["valid"]:
        return _result(diagnostics)

    concepts = {item["id"]: (i, item) for i, item in enumerate(package["concepts"])}
    for expected in RESERVED_CONCEPTS:
        actual = concepts.get(expected["id"])
        if actual is None or actual[1] != expected:
            path = "/concepts" if actual is None else f"/concepts/{actual[0]}"
            diagnostics.append({"code": "E_PROFILE_CONCEPT", "path": path})

    versions = {item["id"] for item in package["versions"]}
    derivations = {item["id"]: item for item in package["relations"]
                   if item["type"] == DERIVED_FROM}
    graph: dict[str, list[str]] = {identifier: [] for identifier in derivations}
    for i, relation in enumerate(package["relations"]):
        path = f"/relations/{i}"
        if relation["type"] == DERIVED_FROM:
            for endpoint in ("source", "target"):
                if relation[endpoint] not in versions:
                    diagnostics.append({"code": "E_PROFILE_ENDPOINT",
                                        "path": path + "/" + endpoint})
        elif relation["type"] == SUPERSEDES:
            newer = derivations.get(relation["source"])
            older = derivations.get(relation["target"])
            if (newer is None or older is None or newer["id"] == older["id"]
                    or newer["agent"] != older["agent"]
                    or newer["agent"] != relation["agent"]
                    or newer["source"] != older["source"]):
                diagnostics.append({"code": "E_PROFILE_SUPERSESSION", "path": path})
            # Only derivation IDs enter this graph. Even ill-attributed edges
            # with derivation endpoints can reveal an additional cycle defect.
            if newer is not None and older is not None:
                graph[newer["id"]].append(older["id"])
    if _cyclic(graph):
        diagnostics.append({"code": "E_PROFILE_CYCLE", "path": "/relations"})
    return _result(diagnostics)


def check_profile_revision(before: Any, after: Any) -> dict:
    """Check a caller-declared shared ID scope, preserving prior claim records.

    Base version immutability still applies. All previous reserved relations,
    including supersession edges, must remain exactly present by ID; changing
    an old relation to an unrelated type does not evade the history check.
    """
    diagnostics = list(check_revision(before, after)["diagnostics"])
    validations = [validate_profile(package) for package in (before, after)]
    for prefix, validation in zip(("/before", "/after"), validations):
        diagnostics.extend({"code": item["code"], "path": prefix + item["path"]}
                           for item in validation["diagnostics"])

    # A previously valid history is still protected when its deletion makes
    # the new package invalid (for example by leaving a dangling edge).
    if (validations[0]["valid"] and type(after) is dict
            and type(after.get("relations")) is list):
        new_records: dict[str, list[dict]] = {}
        for record in after["relations"]:
            if type(record) is dict and type(record.get("id")) is str:
                new_records.setdefault(record["id"], []).append(record)
        for i, record in enumerate(before["relations"]):
            if (record["type"] in (DERIVED_FROM, SUPERSEDES)
                    and new_records.get(record["id"]) != [record]):
                diagnostics.append({"code": "E_CLAIM_REWRITE",
                                    "path": f"/before/relations/{i}"})
    return _result(diagnostics)


def current_derivations(package: Any, agent: Any = None, subject: Any = None) -> list[dict]:
    """Return every unsuperseded claim, sorted by ID without preferring a claim.

    Filters identify a package agent or version; invalid packages and unknown
    or wrong-type filters raise ValueError. Returned records are deep copies.
    """
    validation = validate_profile(package)
    if not validation["valid"]:
        raise ValueError(validation["diagnostics"])
    for name, value, collection in (("agent", agent, "agents"),
                                    ("subject", subject, "versions")):
        if value is not None and (type(value) is not str or not any(
                item["id"] == value for item in package[collection])):
            raise ValueError(f"Unknown or wrong-type {name} filter")

    superseded = {item["target"] for item in package["relations"] if item["type"] == SUPERSEDES}
    current = [item for item in package["relations"]
               if item["type"] == DERIVED_FROM and item["id"] not in superseded
               and (agent is None or item["agent"] == agent)
               and (subject is None or item["source"] == subject)]
    return copy.deepcopy(sorted(current, key=lambda item: item["id"]))
