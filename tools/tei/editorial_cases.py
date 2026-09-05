"""Bounded TEI fragment comparison; neither mapping establishes adequacy.

The primary tree preserves parsed XML structure. The character-sequence
candidate uses real base-model reading nodes plus the explicit annotation
binding below. That binding is an additional dependency, not core semantics.
"""

from __future__ import annotations

import hashlib
import json
import re
import xml.etree.ElementTree as ET
from typing import Any

from tools.models.abstract_text import COLLECTIONS, validate_model


TEI = "http://www.tei-c.org/ns/1.0"
XML = "http://www.w3.org/XML/1998/namespace"
BINDING = "tei-fragment-0.1"
SUPPORTED_TAGS = frozenset({"head", "p", "date", "hi", "placeName", "persName",
                            "name", "ref", "note", "lb"})
MAPPING_RULES = {
    "version": BINDING,
    "namespace": TEI,
    "known_tags": sorted(SUPPORTED_TAGS),
    "text": "Exclude note descendants; collapse Unicode whitespace to one space and trim.",
    "coordinates": "Codepoint offsets in that projection; trim each element's extent edges.",
    "hierarchy": "Every nonempty main-text element is a distinct reading node, including equal extents.",
    "empty_elements": "Point selections plus attributed metadata; lb is a separate point observation.",
    "notes": "Separate structured bodies retain own projected text, attributes, nested note parents, and ref facts; only note/ref markup inside notes is supported.",
    "attributes": "Retain string values verbatim; XML namespace IDs use xml:id, other namespaced attributes retain expanded names. No pointer dereferencing.",
    "binding": "Each annotation body is a JSON object with binding, kind, element, parent, attributes; element adds tag/node, note adds own_text/refs, break adds no fields. Ref facts have id,parent,attributes,text.",
    "validation": "Closed body schemas, full node/selection coverage, node type/parent/selection correspondence, and base validation are required when decoding candidate observations.",
    "unknown": "Unknown tags, foreign namespaces, comments/PIs, and unsupported note markup refuse the candidate; the primary tree retains parsed structure.",
    "security": "Reject DTD/entity declarations, XML declarations, malformed XML, and multiple fragment roots.",
}


def _project(value: str) -> str:
    return " ".join(value.split())


def _name(tag: Any) -> tuple[str, str]:
    if tag is ET.Comment:
        return "#comment", ""
    if tag is ET.ProcessingInstruction:
        return "#processing-instruction", ""
    if tag.startswith("{"):
        namespace, local = tag[1:].split("}", 1)
        return local, namespace
    return tag, ""


def _attrs(attributes: dict) -> dict:
    return {("xml:" + key[len(XML) + 2:] if key.startswith("{" + XML + "}") else key): value
            for key, value in sorted(attributes.items())}


def _parse(xml: Any) -> ET.Element:
    if type(xml) is not str:
        raise ValueError("Fragment must be a Unicode string")
    if re.search(r"<!\s*(?:DOCTYPE|ENTITY)\b|<\?xml\b", xml, re.IGNORECASE):
        raise ValueError("DTD, entity, and XML declarations are outside the fragment contract")
    parser = ET.XMLParser(target=ET.TreeBuilder(insert_comments=True, insert_pis=True))
    try:
        wrapper = ET.fromstring(f'<fragment xmlns="{TEI}">{xml}</fragment>', parser=parser)
    except (ET.ParseError, ValueError) as exc:
        raise ValueError("Malformed XML fragment") from exc
    if (len(wrapper) != 1 or (wrapper.text or "").strip()
            or (wrapper[0].tail or "").strip()):
        raise ValueError("Exactly one fragment root is required")
    return wrapper[0]


def _tree(element: ET.Element, identifier: str = "e0") -> dict:
    tag, namespace = _name(element.tag)
    return {"id": identifier, "tag": tag, "namespace": namespace,
            "attributes": _attrs(element.attrib), "text": element.text or "",
            "tail": element.tail or "",
            "children": [_tree(child, f"{identifier}.{i}") for i, child in enumerate(element)]}


def _projection_coordinates(raw: str) -> tuple[str, list[int]]:
    """Map raw character boundaries into the stated whitespace projection."""
    parts: list[str] = []
    origins: list[int] = []
    pending = None
    for i, char in enumerate(raw):
        if char.isspace():
            if parts and pending is None:
                pending = i
        else:
            if pending is not None:
                parts.append(" ")
                origins.append(pending)
            pending = None
            parts.append(char)
            origins.append(i)
    boundaries = []
    cursor = 0
    for offset in range(len(raw) + 1):
        while cursor < len(origins) and origins[cursor] < offset:
            cursor += 1
        boundaries.append(cursor)
    return "".join(parts), boundaries


def _extent(raw: str, boundaries: list[int], start: int, end: int) -> list[int]:
    while start < end and raw[start].isspace():
        start += 1
    while end > start and raw[end - 1].isspace():
        end -= 1
    return [boundaries[start], boundaries[end]]


def _pointers(elements: list[dict], notes: list[dict], breaks: list[dict]) -> list[dict]:
    records = [*elements, *notes, *breaks]
    records.extend(ref for note in notes for ref in note["refs"])
    return sorted([{"element": item["id"], "attribute": key, "value": value}
                   for item in records for key, value in item["attributes"].items()
                   if key in {"xml:id", "ref", "corresp", "resp", "hand", "calendar", "rendition", "target"}],
                  key=lambda item: (item["element"], item["attribute"]))


def _observations(text: str, elements: list[dict], notes: list[dict], breaks: list[dict]) -> dict:
    return {"text": text, "elements": sorted(elements, key=lambda item: item["id"]),
            "notes": sorted(notes, key=lambda item: item["id"]),
            "breaks": sorted(breaks, key=lambda item: item["id"]),
            "pointers": _pointers(elements, notes, breaks)}


def _observe_tree(tree: dict) -> tuple[dict, list[dict]]:
    """Independently inspect the stored primary tree, not the model package."""
    raw_parts: list[str] = []
    records, notes, breaks, stand_off = [], [], [], []
    raw_length = 0

    def add(text: str) -> None:
        nonlocal raw_length
        raw_parts.append(text)
        raw_length += len(text)

    def note_text(node: dict) -> str:
        value = node["text"]
        for child in node["children"]:
            if child["tag"] != "note" and not child["tag"].startswith("#"):
                value += note_text(child)
            value += child["tail"]
        return value

    def note(node: dict, parent: str | None) -> None:
        refs = []

        def descendants(current: dict) -> None:
            for child in current["children"]:
                if child["tag"] == "note":
                    note(child, current["id"])
                else:
                    if child["tag"] == "ref":
                        refs.append({"id": child["id"], "parent": current["id"],
                                     "attributes": dict(child["attributes"]),
                                     "text": _project(note_text(child))})
                    descendants(child)

        descendants(node)
        notes.append({"id": node["id"], "parent": parent, "attributes": dict(node["attributes"]),
                      "own_text": _project(note_text(node)), "refs": sorted(refs, key=lambda item: item["id"])})
        stand_off.append({"kind": "note", "element": node["id"]})

    def walk(node: dict, parent: str | None) -> None:
        start = raw_length
        if node["tag"] == "note":
            note(node, parent)
            return
        if node["tag"].startswith("#"):
            return
        if node["tag"] == "lb":
            breaks.append({"id": node["id"], "parent": parent,
                           "attributes": dict(node["attributes"]), "offset": start})
            stand_off.append({"kind": "break", "element": node["id"]})
            return
        add(node["text"])
        for child in node["children"]:
            walk(child, node["id"])
            add(child["tail"])
        records.append({"id": node["id"], "tag": node["tag"],
                        "attributes": dict(node["attributes"]), "parent": parent,
                        "extent": [start, raw_length]})

    walk(tree, None)
    raw = "".join(raw_parts)
    text, boundaries = _projection_coordinates(raw)
    for item in records:
        item["extent"] = _extent(raw, boundaries, *item["extent"])
    for item in breaks:
        item["offset"] = boundaries[item["offset"]]
    return _observations(text, records, notes, breaks), sorted(stand_off, key=lambda item: item["element"])


def _candidate(root: ET.Element) -> tuple[dict | None, list[str]]:
    """Map the source DOM independently of the baseline's observations."""
    unsupported = set()
    descriptors = []
    chunks: list[str] = []
    length = 0

    def add(value: str | None) -> None:
        nonlocal length
        value = value or ""
        chunks.append(value)
        length += len(value)

    def classify(element: ET.Element, in_note: bool) -> str:
        tag, namespace = _name(element.tag)
        if namespace != TEI or tag not in SUPPORTED_TAGS:
            unsupported.add(tag if namespace in (TEI, "") else "{" + namespace + "}" + tag)
        if in_note and tag not in {"note", "ref"}:
            unsupported.add("note/" + tag)
        return tag

    def own_text(element: ET.Element) -> str:
        parts = [element.text or ""]
        for child in element:
            if _name(child.tag)[0] != "note":
                parts.append(own_text(child))
            parts.append(child.tail or "")
        return "".join(parts)

    def walk(element: ET.Element, identifier: str, parent: str | None,
             in_note: bool = False) -> None:
        tag = classify(element, in_note)
        attributes = _attrs(element.attrib)
        start = length
        common = {"binding": BINDING, "element": identifier, "parent": parent,
                  "attributes": attributes}
        if tag == "note":
            refs = []
            for i, child in enumerate(element):
                child_id = f"{identifier}.{i}"
                child_tag = classify(child, True)
                if child_tag == "ref":
                    refs.append({"id": child_id, "parent": identifier,
                                 "attributes": _attrs(child.attrib), "text": _project(own_text(child))})
                    if len(child):
                        unsupported.add("note/ref-children")
                else:
                    walk(child, child_id, identifier, True)
            descriptors.append(({**common, "kind": "note", "own_text": _project(own_text(element)),
                                 "refs": refs}, start, start))
        elif in_note:
            for i, child in enumerate(element):
                walk(child, f"{identifier}.{i}", identifier, True)
        elif tag == "lb":
            if len(element) or (element.text or "").strip():
                unsupported.add("lb/content")
            descriptors.append(({**common, "kind": "break"}, start, start))
        else:
            add(element.text)
            for i, child in enumerate(element):
                walk(child, f"{identifier}.{i}", identifier)
                add(child.tail)
            descriptors.append(({**common, "kind": "element", "tag": tag,
                                 "node": None}, start, length))

    walk(root, "e0", None)
    if unsupported:
        return None, sorted(unsupported)
    raw = "".join(chunks)
    text, boundaries = _projection_coordinates(raw)
    model = {kind: [] for kind in COLLECTIONS}
    model.update(model_version="0.1", agents=[{"id": "mapper", "label": "Bounded fragment mapping policy"}],
                 versions=[{"id": "v-main", "content": text,
                            "sha256": hashlib.sha256(text.encode("utf-8")).hexdigest(), "parents": []}])
    nodes = []
    nonempty = set()
    for body, start, end in descriptors:
        if body["kind"] == "element" and _extent(raw, boundaries, start, end)[0] < _extent(raw, boundaries, start, end)[1]:
            nonempty.add(body["element"])
    for body, start, end in sorted(descriptors, key=lambda item: item[0]["element"]):
        identifier = body["element"]
        begin, finish = _extent(raw, boundaries, start, end)
        selector = ({"kind": "ranges", "segments": [{"start": begin, "end": finish, "quote": text[begin:finish]}]}
                    if begin < finish else {"kind": "point", "offset": begin})
        selection = "s-" + identifier
        model["selections"].append({"id": selection, "version": "v-main", "selector": selector})
        if identifier in nonempty:
            body["node"] = "n-" + identifier
            nodes.append({"id": body["node"], "type": "tei-" + body["tag"], "selection": selection,
                          "parent": "n-" + body["parent"] if body["parent"] in nonempty else None})
        model["annotations"].append({"id": "a-" + identifier, "agent": "mapper", "selection": selection,
                                     "body": json.dumps(body, ensure_ascii=False, sort_keys=True, separators=(",", ":"))})
    if nodes:
        model["readings"] = [{"id": "r-main", "version": "v-main", "agent": "mapper",
                               "label": "TEI main-text element hierarchy", "nodes": nodes}]
    tags = sorted({body["tag"] for body, _, _ in descriptors if body["kind"] == "element"})
    model["concepts"] = [{"id": "tei-" + tag, "label": tag, "definition": "TEI element " + tag,
                          "applies_to": "node"} for tag in tags]
    return model, []


def candidate_observations(package: Any) -> dict:
    """Decode the strict scoped binding; missing or inconsistent metadata rejects.

    Source correctness still needs an independently authored source oracle.
    Base validation alone cannot interpret these annotation-body records.
    """
    validation = validate_model(package)
    if not validation["valid"]:
        raise ValueError(validation["diagnostics"])
    if len(package["versions"]) != 1 or len(package["readings"]) > 1:
        raise ValueError("Binding requires one primary version and at most one reading")
    nodes = {node["id"]: node for reading in package["readings"] for node in reading["nodes"]}
    bodies, selections, used_nodes, ref_ids = {}, set(), set(), set()
    elements, notes, breaks = [], [], []

    def strings(value: Any) -> bool:
        return type(value) is dict and all(type(key) is str and type(item) is str for key, item in value.items())

    def identifier(value: Any) -> bool:
        return type(value) is str and re.fullmatch(r"e0(?:\.[0-9]+)*", value) is not None

    for annotation in package["annotations"]:
        try:
            body = json.loads(annotation["body"])
        except (ValueError, TypeError) as exc:
            raise ValueError("Annotation body is not binding JSON") from exc
        common = {"binding", "kind", "element", "parent", "attributes"}
        fields = {"element": {"tag", "node"}, "note": {"own_text", "refs"}, "break": set()}
        if (type(body) is not dict or type(body.get("kind")) is not str
                or body["kind"] not in fields or set(body) != common | fields[body["kind"]]
                or body["binding"] != BINDING or not identifier(body["element"])
                or (body["parent"] is not None and not identifier(body["parent"]))
                or not strings(body["attributes"]) or body["element"] in bodies):
            raise ValueError("Malformed or duplicate annotation binding")
        bodies[body["element"]] = body
        selection = annotation["selection"]
        if selection in selections:
            raise ValueError("Binding selection used more than once")
        selections.add(selection)
        resolution = validation["resolutions"][selection]
        if resolution["status"] != "resolved" or len(resolution["targets"]) != 1:
            raise ValueError("Binding needs exactly one resolved target")
        target = resolution["targets"][0]
        point = target["kind"] == "point"
        if not point and len(target["segments"]) != 1:
            raise ValueError("Binding needs one contiguous segment")
        extent = ([target["offset"], target["offset"]] if point else
                  [target["segments"][0]["start"], target["segments"][0]["end"]])
        common_observation = {"id": body["element"], "parent": body["parent"],
                              "attributes": dict(body["attributes"])}
        if body["kind"] == "element":
            if type(body["tag"]) is not str or body["tag"] not in SUPPORTED_TAGS - {"note", "lb"}:
                raise ValueError("Unknown binding element tag")
            if point:
                if body["node"] is not None:
                    raise ValueError("Empty element must use a point without a reading node")
            else:
                if type(body["node"]) is not str or body["node"] not in nodes:
                    raise ValueError("Element metadata lacks its reading node")
                node = nodes[body["node"]]
                if (body["node"] in used_nodes or node["selection"] != selection
                        or node["type"] != "tei-" + body["tag"]):
                    raise ValueError("Element metadata disagrees with its reading node")
                used_nodes.add(body["node"])
            elements.append({**common_observation, "tag": body["tag"], "extent": extent})
        elif body["kind"] == "break":
            if not point:
                raise ValueError("Break metadata must target a point")
            breaks.append({**common_observation, "offset": extent[0]})
        else:
            if not point or type(body["own_text"]) is not str or type(body["refs"]) is not list:
                raise ValueError("Malformed note metadata")
            refs = []
            for ref in body["refs"]:
                if (type(ref) is not dict or set(ref) != {"id", "parent", "attributes", "text"}
                        or not identifier(ref["id"]) or ref["parent"] != body["element"]
                        or ref["id"].rsplit(".", 1)[0] != body["element"] or ref["id"] in ref_ids
                        or not strings(ref["attributes"]) or type(ref["text"]) is not str):
                    raise ValueError("Malformed note reference metadata")
                ref_ids.add(ref["id"])
                refs.append({**ref, "attributes": dict(ref["attributes"])})
            notes.append({**common_observation, "own_text": body["own_text"], "refs": refs})
    if "e0" not in bodies or ref_ids.intersection(bodies):
        raise ValueError("Missing root or duplicate source element identity")
    if used_nodes != set(nodes) or selections != {item["id"] for item in package["selections"]}:
        raise ValueError("Incomplete metadata coverage of nodes or selections")
    for body in bodies.values():
        parent = bodies.get(body["parent"])
        if ((body["element"] == "e0") != (body["parent"] is None)
                or (body["parent"] is not None and (parent is None
                    or body["element"].rsplit(".", 1)[0] != body["parent"]))):
            raise ValueError("Missing or inconsistent source parent metadata")
        if body["kind"] == "element" and body["node"] is not None:
            expected_parent = parent.get("node") if parent is not None else None
            if nodes[body["node"]]["parent"] != expected_parent:
                raise ValueError("Source hierarchy disagrees with actual reading hierarchy")
    return _observations(package["versions"][0]["content"], elements, notes, breaks)


def compare_fragment(xml: str) -> dict:
    """Return deterministic representations and their independently decoded observations."""
    root = _parse(xml)
    tree = _tree(root)
    baseline_observations, stand_off = _observe_tree(tree)
    package, unsupported = _candidate(root)
    baseline_limits = [
        "Parsed XML preserves hierarchy, attribute values, and text/tail; lexical entity spelling, attribute order, quote style, and original namespace prefixes are not retained.",
        "Task observations apply the same declared text projection; unsupported constructs remain in the tree without a domain interpretation.",
    ]
    candidate_limits = [
        "Whitespace collapse/trim and note exclusion define a new primary text projection; source bytes must be retained separately.",
        "TEI attribute and note interpretation depends on the explicit tei-fragment-0.1 annotation binding; base 0.1 alone does not validate that meaning.",
        "Pointers retain values without resolution, authority, or external referent validation; no full P5/ODD conformance or lexical round-trip is claimed.",
        "Synthetic inspection checks do not measure editor time, learnability, or architecture preference.",
    ]
    observations = candidate_observations(package) if package is not None else None
    return {
        "baseline": {"representation": {"tree": tree, "stand_off": stand_off},
                     "observations": baseline_observations, "limitations": baseline_limits},
        "candidate": {"package": package, "valid": package is not None,
                      "observations": observations, "unsupported": unsupported,
                      "limitations": candidate_limits},
        "observations_equal": observations == baseline_observations,
    }
