"""Executable Abstract Text Model v0.1; see experiments/abstract_text_v01/spec.json.

The model is an independent project posit. Validation establishes only the
specified structural consistency, not editorial truth or practical adequacy.
Inputs are closed JSON-shaped packages; every public operation is nonmutating.
"""

from __future__ import annotations

import copy
import hashlib
import itertools
import json
import re
from typing import Any

COLLECTIONS = (
    "agents", "concepts", "texts", "versions", "continuities", "selections",
    "readings", "annotations", "relations",
)
FIELDS = {
    "agents": {"id", "label"},
    "concepts": {"id", "label", "definition", "applies_to"},
    "texts": {"id", "label"},
    "versions": {"id", "content", "sha256", "parents"},
    "continuities": {"id", "text", "versions", "agent", "criterion"},
    "selections": {"id", "version", "selector"},
    "readings": {"id", "version", "agent", "label", "nodes"},
    "nodes": {"id", "type", "selection", "parent"},
    "annotations": {"id", "agent", "selection", "body"},
    "relations": {"id", "type", "source", "target", "agent"},
}
ID = re.compile(r"[A-Za-z][A-Za-z0-9._:-]*\Z")


def _unicode(value: Any, *, empty: bool = False) -> bool:
    if type(value) is not str or (not empty and not value):
        return False
    try:
        value.encode("utf-8")
        return True
    except UnicodeEncodeError:
        return False


def _id(value: Any) -> bool:
    return type(value) is str and ID.fullmatch(value) is not None


def _diagnostics(items: list[dict]) -> list[dict]:
    return [{"code": code, "path": path} for path, code in sorted(
        {(item["path"], item["code"]) for item in items}
    )]


def _has_errors(items: list[dict]) -> bool:
    return any(item["code"].startswith("E_") for item in items)


def _region(start: int, end: int) -> dict:
    return {"kind": "region", "segments": [{"start": start, "end": end}]}


def _resolve(content: str, version: str, selector: dict) -> dict:
    kind = selector["kind"]
    candidates = []
    status = "resolved"
    if kind == "point":
        targets = [{"kind": "point", "offset": selector["offset"]}]
    elif kind == "ranges":
        targets = [{"kind": "region", "segments": [
            {"start": part["start"], "end": part["end"]}
            for part in selector["segments"]
        ]}]
    else:
        exact = selector["exact"]
        prefix, suffix = selector.get("prefix", ""), selector.get("suffix", "")
        matches = []
        offset = 0
        while (start := content.find(exact, offset)) >= 0:
            end = start + len(exact)
            if content[:start].endswith(prefix) and content[end:].startswith(suffix):
                matches.append(_region(start, end))
            offset = start + 1
        targets = matches
        if not matches:
            status = "absent"
        elif selector["match"] == "one" and len(matches) > 1:
            status, targets, candidates = "ambiguous", [], matches
    return {"version": version, "status": status, "targets": targets, "candidates": candidates}


def _cyclic(graph: dict[str, list[str]]) -> bool:
    """Iterative traversal avoids a recursion limit on valid long histories."""
    done = set()
    for start in graph:
        if start in done:
            continue
        active = set()
        stack = [(start, False)]
        while stack:
            node, leaving = stack.pop()
            if leaving:
                active.remove(node)
                done.add(node)
            elif node in active:
                return True
            elif node not in done:
                active.add(node)
                stack.append((node, True))
                stack.extend((parent, False) for parent in graph[node])
    return False


class _Validator:
    def __init__(self, package: Any):
        self.package = package
        self.errors: list[dict] = []
        self.index = {kind: {} for kind in (*COLLECTIONS, "nodes")}
        self.all_ids: set[str] = set()
        self.resolutions: dict[str, dict] = {}

    def error(self, code: str, path: str) -> None:
        self.errors.append({"code": code, "path": path})

    def shape(self, obj: Any, required: set[str], path: str,
              optional: set[str] | None = None, code: str = "E_SHAPE") -> bool:
        if (type(obj) is not dict or not required.issubset(obj)
                or not set(obj).issubset(required | (optional or set()))):
            self.error(code, path)
            return False
        return True

    def ids(self, value: Any, path: str, *, nonempty: bool = False) -> None:
        if type(value) is not list or (nonempty and not value):
            self.error("E_SHAPE", path)
        elif any(not _id(item) for item in value):
            self.error("E_ID", path)
        elif len(set(value)) != len(value):
            self.error("E_SHAPE", path)

    def selector_shape(self, obj: Any, path: str) -> None:
        if type(obj) is not dict or type(obj.get("kind")) is not str:
            self.error("E_SELECTOR", path)
            return
        kind = obj["kind"]
        if kind == "point":
            if (self.shape(obj, {"kind", "offset"}, path, code="E_SELECTOR")
                    and type(obj["offset"]) is not int):
                self.error("E_SELECTOR", path + "/offset")
        elif kind == "ranges":
            if not self.shape(obj, {"kind", "segments"}, path, code="E_SELECTOR"):
                return
            if type(obj["segments"]) is not list or not obj["segments"]:
                self.error("E_SELECTOR", path + "/segments")
                return
            for i, segment in enumerate(obj["segments"]):
                subpath = f"{path}/segments/{i}"
                if not self.shape(segment, {"start", "end", "quote"}, subpath, code="E_SELECTOR"):
                    continue
                if type(segment["start"]) is not int or type(segment["end"]) is not int:
                    self.error("E_SELECTOR", subpath)
                if not _unicode(segment["quote"]):
                    self.error("E_QUOTE", subpath + "/quote")
        elif kind == "quote":
            if not self.shape(obj, {"kind", "exact", "match"}, path,
                              {"prefix", "suffix"}, "E_SELECTOR"):
                return
            if not _unicode(obj["exact"]):
                self.error("E_QUOTE", path + "/exact")
            if type(obj["match"]) is not str or obj["match"] not in ("one", "all"):
                self.error("E_SELECTOR", path + "/match")
            for key in ("prefix", "suffix"):
                if key in obj and not _unicode(obj[key], empty=True):
                    self.error("E_QUOTE", path + "/" + key)
        else:
            self.error("E_SELECTOR", path + "/kind")

    def record(self, kind: str, obj: Any, path: str) -> None:
        if not self.shape(obj, FIELDS[kind], path):
            return
        identifier = obj["id"]
        if not _id(identifier):
            self.error("E_ID", path + "/id")
        elif identifier in self.all_ids:
            self.error("E_DUPLICATE_ID", path + "/id")
        else:
            self.all_ids.add(identifier)
            self.index[kind][identifier] = obj
        for key in ("label", "definition", "criterion", "body"):
            if key in obj and not _unicode(obj[key]):
                self.error("E_SHAPE", path + "/" + key)
        for key in ("agent", "text", "version", "type", "selection", "source", "target"):
            if key in obj and not _id(obj[key]):
                self.error("E_ID", path + "/" + key)
        if kind == "concepts":
            if type(obj["applies_to"]) is not str or obj["applies_to"] not in ("node", "relation"):
                self.error("E_TYPE", path + "/applies_to")
        elif kind == "versions":
            if not _unicode(obj["content"], empty=True):
                self.error("E_SHAPE", path + "/content")
            if (type(obj["sha256"]) is not str
                    or re.fullmatch(r"[0-9a-f]{64}", obj["sha256"]) is None):
                self.error("E_HASH", path + "/sha256")
            self.ids(obj["parents"], path + "/parents")
        elif kind == "continuities":
            self.ids(obj["versions"], path + "/versions", nonempty=True)
        elif kind == "selections":
            self.selector_shape(obj["selector"], path + "/selector")
        elif kind == "readings":
            if type(obj["nodes"]) is not list or not obj["nodes"]:
                self.error("E_SHAPE", path + "/nodes")
            else:
                for i, node in enumerate(obj["nodes"]):
                    self.record("nodes", node, f"{path}/nodes/{i}")
        elif kind == "nodes" and obj["parent"] is not None and not _id(obj["parent"]):
            self.error("E_ID", path + "/parent")

    def reference(self, obj: dict, key: str, kind: str, path: str) -> None:
        if obj[key] not in self.index[kind]:
            self.error("E_REFERENCE", path + "/" + key)

    def references(self) -> None:
        for kind in COLLECTIONS:
            for i, obj in enumerate(self.package[kind]):
                path = f"/{kind}/{i}"
                for key, category in (("agent", "agents"), ("text", "texts"),
                                      ("version", "versions"), ("selection", "selections"),
                                      ("type", "concepts")):
                    if key in obj:
                        self.reference(obj, key, category, path)
                if kind in ("versions", "continuities"):
                    key = "parents" if kind == "versions" else "versions"
                    for j, target in enumerate(obj[key]):
                        if target not in self.index["versions"]:
                            self.error("E_REFERENCE", f"{path}/{key}/{j}")
                if kind == "relations":
                    for key in ("source", "target"):
                        if obj[key] not in self.all_ids:
                            self.error("E_REFERENCE", path + "/" + key)
                    if (obj["type"] in self.index["concepts"]
                            and self.index["concepts"][obj["type"]]["applies_to"] != "relation"):
                        self.error("E_TYPE", path + "/type")
                if kind == "readings":
                    local_ids = {node["id"] for node in obj["nodes"]}
                    for j, node in enumerate(obj["nodes"]):
                        subpath = f"{path}/nodes/{j}"
                        self.reference(node, "type", "concepts", subpath)
                        self.reference(node, "selection", "selections", subpath)
                        if node["parent"] is not None and node["parent"] not in local_ids:
                            self.error("E_READING_PARENT", subpath + "/parent")
                        if (node["type"] in self.index["concepts"]
                                and self.index["concepts"][node["type"]]["applies_to"] != "node"):
                            self.error("E_TYPE", subpath + "/type")
                        selection = self.index["selections"].get(node["selection"])
                        if selection is not None and selection["version"] != obj["version"]:
                            self.error("E_READING_TARGET", subpath + "/selection")

    def semantics(self) -> None:
        versions = self.index["versions"]
        if _cyclic({key: item["parents"] for key, item in versions.items()}):
            self.error("E_VERSION_CYCLE", "/versions")
        grouped = {obj["text"] for obj in self.package["continuities"]}
        for i, obj in enumerate(self.package["texts"]):
            if obj["id"] not in grouped:
                self.error("E_CONTINUITY", f"/texts/{i}")
        for i, version in enumerate(self.package["versions"]):
            if hashlib.sha256(version["content"].encode("utf-8")).hexdigest() != version["sha256"]:
                self.error("E_HASH", f"/versions/{i}/sha256")
        for i, selection in enumerate(self.package["selections"]):
            selector = selection["selector"]
            content = versions[selection["version"]]["content"]
            path = f"/selections/{i}/selector"
            if selector["kind"] == "point":
                if not 0 <= selector["offset"] <= len(content):
                    self.error("E_BOUNDS", path + "/offset")
            elif selector["kind"] == "ranges":
                previous_end = 0
                for j, part in enumerate(selector["segments"]):
                    start, end = part["start"], part["end"]
                    if not 0 <= start < end <= len(content):
                        self.error("E_BOUNDS", f"{path}/segments/{j}")
                    else:
                        if start < previous_end:
                            self.error("E_SELECTOR", f"{path}/segments/{j}")
                        if content[start:end] != part["quote"]:
                            self.error("E_QUOTE", f"{path}/segments/{j}/quote")
                    previous_end = end
        for i, reading in enumerate(self.package["readings"]):
            if _cyclic({node["id"]: [] if node["parent"] is None else [node["parent"]]
                        for node in reading["nodes"]}):
                self.error("E_READING_CYCLE", f"/readings/{i}/nodes")

    def reading_extents(self) -> None:
        for i, reading in enumerate(self.package["readings"]):
            intervals = {}
            paths = {}
            for j, node in enumerate(reading["nodes"]):
                path = f"/readings/{i}/nodes/{j}"
                paths[node["id"]] = path
                result = self.resolutions[node["selection"]]
                targets = result["targets"]
                if result["status"] != "resolved" or len(targets) != 1 or targets[0]["kind"] != "region":
                    self.error("E_READING_TARGET", path + "/selection")
                    continue
                segments = targets[0]["segments"]
                if any(left["end"] != right["start"] for left, right in itertools.pairwise(segments)):
                    self.error("E_READING_TARGET", path + "/selection")
                    continue
                intervals[node["id"]] = (segments[0]["start"], segments[-1]["end"])
            siblings: dict[str | None, list] = {}
            for node in reading["nodes"]:
                if node["id"] not in intervals:
                    continue
                start, end = intervals[node["id"]]
                parent = node["parent"]
                if parent in intervals:
                    pstart, pend = intervals[parent]
                    if not pstart <= start < end <= pend:
                        self.error("E_CONTAINMENT", paths[node["id"]])
                siblings.setdefault(parent, []).append((start, end, node["id"]))
            for group in siblings.values():
                greatest_end = -1
                for start, end, identifier in sorted(group):
                    if start < greatest_end:
                        self.error("E_SIBLING_OVERLAP", paths[identifier])
                    greatest_end = max(greatest_end, end)

    def result(self) -> dict:
        valid = not _has_errors(self.errors)
        return {"valid": valid,
                "all_selections_resolved": valid and all(
                    result["status"] == "resolved" for result in self.resolutions.values()),
                "diagnostics": _diagnostics(self.errors),
                "resolutions": self.resolutions if valid else {}}

    def run(self) -> dict:
        if not self.shape(self.package, {*COLLECTIONS, "model_version"}, ""):
            return self.result()
        if self.package["model_version"] != "0.1":
            self.error("E_SHAPE", "/model_version")
        for kind in COLLECTIONS:
            if type(self.package[kind]) is not list:
                self.error("E_SHAPE", "/" + kind)
                continue
            for i, obj in enumerate(self.package[kind]):
                self.record(kind, obj, f"/{kind}/{i}")
        if _has_errors(self.errors):
            return self.result()
        self.references()
        if _has_errors(self.errors):
            return self.result()
        self.semantics()
        if _has_errors(self.errors):
            return self.result()
        for i, selection in enumerate(self.package["selections"]):
            version = selection["version"]
            result = _resolve(self.index["versions"][version]["content"], version, selection["selector"])
            self.resolutions[selection["id"]] = result
            if result["status"] != "resolved":
                self.error("W_" + result["status"].upper(), f"/selections/{i}/selector")
        self.reading_extents()
        return self.result()


def validate_model(package: Any) -> dict:
    """Return deterministic diagnostics and resolutions for a closed package."""
    return _Validator(package).run()


def canonical_bytes(package: Any) -> bytes:
    """Return canonical UTF-8 JSON; raise ValueError for structurally invalid input."""
    result = validate_model(package)
    if not result["valid"]:
        raise ValueError(result["diagnostics"])
    canonical = copy.deepcopy(package)
    for kind in COLLECTIONS:
        canonical[kind].sort(key=lambda item: item["id"])
    for version in canonical["versions"]:
        version["parents"].sort()
    for continuity in canonical["continuities"]:
        continuity["versions"].sort()
    for reading in canonical["readings"]:
        reading["nodes"].sort(key=lambda item: item["id"])
    return json.dumps(canonical, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False).encode("utf-8")


def equivalent(left: Any, right: Any) -> bool:
    """Compare valid packages under R11; invalid inputs raise ValueError."""
    return canonical_bytes(left) == canonical_bytes(right)


def check_revision(before: Any, after: Any) -> dict:
    """Check reused version IDs in a caller-declared shared identity scope.

    Callers must not infer rewrites from coincidental local IDs in independent
    packages. Removing a version is allowed when the remaining package is valid.
    """
    diagnostics = []
    results = [validate_model(package) for package in (before, after)]
    for prefix, result in zip(("/before", "/after"), results, strict=True):
        diagnostics.extend({"code": item["code"], "path": prefix + item["path"]}
                           for item in result["diagnostics"])
    if all(result["valid"] for result in results):
        old = {version["id"]: version for version in before["versions"]}
        for i, version in enumerate(after["versions"]):
            previous = old.get(version["id"])
            if previous is not None and (
                previous["content"] != version["content"]
                or previous["sha256"] != version["sha256"]
                or set(previous["parents"]) != set(version["parents"])
            ):
                diagnostics.append({"code": "E_VERSION_REWRITE", "path": f"/after/versions/{i}"})
    return {"valid": not _has_errors(diagnostics), "diagnostics": _diagnostics(diagnostics)}


def propose_reanchor(package: Any, selection_id: Any, target_version_id: Any,
                     continuity_id: Any) -> dict:
    """Return an unaccepted, explicit-continuity proposal without altering input."""
    validation = validate_model(package)
    if not validation["valid"]:
        return {"diagnostics": validation["diagnostics"], "proposal": None}
    selection = next((item for item in package["selections"] if item["id"] == selection_id), None)
    version = next((item for item in package["versions"] if item["id"] == target_version_id), None)
    continuity = next((item for item in package["continuities"] if item["id"] == continuity_id), None)
    if (not all(_id(value) for value in (selection_id, target_version_id, continuity_id))
            or selection is None or version is None or continuity is None
            or selection["version"] not in continuity["versions"]
            or target_version_id not in continuity["versions"]
            or validation["resolutions"][selection_id]["status"] != "resolved"):
        return {"diagnostics": [{"code": "E_REANCHOR", "path": "/reanchor"}], "proposal": None}
    selector = selection["selector"]
    if selector["kind"] == "point" or (selector["kind"] == "ranges" and len(selector["segments"]) != 1):
        return {"diagnostics": [{"code": "E_REANCHOR_UNSUPPORTED", "path": "/reanchor"}], "proposal": None}
    if selector["kind"] == "ranges":
        selector = {"kind": "quote", "exact": selector["segments"][0]["quote"], "match": "one"}
    resolution = _resolve(version["content"], target_version_id, selector)
    diagnostics = []
    if resolution["status"] != "resolved":
        diagnostics.append({"code": "W_" + resolution["status"].upper(), "path": "/reanchor/resolution"})
    return {"diagnostics": diagnostics, "proposal": {
        "source_selection": selection_id, "target_version": target_version_id,
        "continuity": continuity_id, "resolution": resolution, "accepted": False,
    }}
