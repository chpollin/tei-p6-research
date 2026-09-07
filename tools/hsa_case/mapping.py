"""Construct records through explicit source claims and separate preservation steps."""

from __future__ import annotations

import hashlib
import json
import xml.etree.ElementTree as ET
from dataclasses import dataclass

from rdflib import Graph, Literal, URIRef
from rdflib.namespace import RDF, XSD

from tools.hsa_case.config import (
    ATTRIBUTION,
    CASE,
    CONCEPTS,
    CONTEXTS,
    LICENSE,
    NS,
    P6,
    PREDICATES,
    PROFILE,
    PROJECTION,
    REFERENTS,
    SHA256,
    SOURCE,
    TEI,
    VOC,
)
from tools.hsa_case.source import one, project, resolve, source_tree


def add_literal(
    graph: Graph,
    subject: URIRef,
    predicate: URIRef,
    value: str,
    datatype: URIRef = XSD.string,
) -> None:
    graph.add((subject, predicate, Literal(value, datatype=datatype, normalize=False)))


def record(graph: Graph, identifier: str, kind: str, label: str = "") -> URIRef:
    subject = CASE[identifier]
    graph.add((subject, RDF.type, P6[kind]))
    graph.add((CASE.package, P6.member, subject))
    graph.add((subject, P6.responsibleAgent, CASE.importer))
    if label:
        add_literal(graph, subject, P6.preferredLabel, label)
    return subject


@dataclass(frozen=True)
class ClaimSpec:
    identifier: str
    subject: str
    predicate: str
    obj: str
    context: str
    element: ET.Element | None = None
    attribute: str | None = None
    datatype: URIRef | None = None
    construction: str | None = None


def source_location(
    graph: Graph,
    tree: ET.Element,
    paths: dict,
    element: ET.Element,
    attribute: str | None = None,
) -> URIRef:
    xpath = paths[element] + ("/@" + attribute if attribute else "")
    identifier = "source-location-" + hashlib.sha256(xpath.encode()).hexdigest()[:16]
    subject = record(graph, identifier, "Record", "Checked source location")
    add_literal(graph, subject, VOC.sourceXPath, xpath)
    add_literal(graph, subject, VOC.sourceValue, resolve(tree, xpath))
    graph.add((subject, VOC.sourceSnapshot, CASE["source-snapshot"]))
    return subject


def add_initial_records(graph: Graph, payload: bytes, contents: dict) -> None:
    graph.add((CASE.package, RDF.type, P6.Package))
    graph.add((CASE.package, P6.responsibleAgent, CASE.importer))
    for predicate, value, datatype in (
        (VOC.profile, PROFILE, XSD.anyURI),
        (VOC.sourceURL, SOURCE, XSD.anyURI),
        (VOC.license, LICENSE, XSD.anyURI),
        (VOC.attribution, ATTRIBUTION, XSD.string),
        (VOC.sha256, SHA256, XSD.string),
        (VOC.projection, PROJECTION, XSD.string),
    ):
        add_literal(graph, CASE.package, predicate, value, datatype)
    record(
        graph,
        "importer",
        "AgentRecord",
        "Deterministic HSA 4493 importer; source metadata reports, no historical verification",
    )
    record(graph, "source-snapshot", "Record", "Admitted HSA 4493 XML snapshot")
    add_literal(graph, CASE["source-snapshot"], VOC.sourceURL, SOURCE, XSD.anyURI)
    add_literal(graph, CASE["source-snapshot"], VOC.sha256, SHA256)
    record(
        graph,
        "representation-source-xml",
        "RepresentationRecord",
        "Exact archived XML decoded as UTF-8",
    )
    add_literal(
        graph, CASE["representation-source-xml"], P6.content, payload.decode("utf-8")
    )
    graph.add(
        (CASE["source-snapshot"], P6.representation, CASE["representation-source-xml"])
    )
    record(
        graph,
        "text-letter",
        "TextRecord",
        "Linguistic content of the letter in the admitted HSA source",
    )
    add_literal(
        graph,
        CASE["text-letter"],
        P6.identityCriteria,
        "The linguistic content attributed to this single letter, delimited by the source's original-letter div and excluding separately encoded editorial note subtrees. The criterion retains opener, dateline, signature and postscript; shared wording in another letter would not establish identity.",
    )
    for identifier, content in contents.items():
        record(graph, identifier, "RepresentationRecord", identifier)
        add_literal(graph, CASE[identifier], P6.content, content)
        add_literal(graph, CASE[identifier], VOC.projection, PROJECTION)
        graph.add((CASE[identifier], VOC.sourceSnapshot, CASE["source-snapshot"]))


def add_referents(graph: Graph) -> None:
    for identifier, label in REFERENTS.items():
        record(graph, identifier, "ReferentRecord", label)
    for identifier, definition, referents in CONCEPTS:
        concept = record(graph, "concept-" + identifier, "ConceptRecord", identifier)
        add_literal(graph, concept, P6.definition, definition)
        for identifier in referents:
            graph.add((CASE[identifier], P6.expectedReferentType, concept))
            add_literal(
                graph,
                CASE[identifier],
                VOC.construction,
                "Revisable expected referent type assigned by this bounded import profile from the stated source context; no foreign class membership or independent historical verification.",
            )


def add_contexts(graph: Graph) -> None:
    for identifier, scope in CONTEXTS.items():
        record(graph, identifier, "ContextRecord", scope)
        add_literal(graph, CASE[identifier], P6.scope, scope)
    for identifier, (subject_mode, object_mode, definition) in PREDICATES.items():
        term = record(graph, "predicate-" + identifier, "PredicateRecord", identifier)
        add_literal(graph, term, P6.definition, definition)
        add_literal(graph, term, P6.subjectInterpretation, subject_mode)
        add_literal(graph, term, P6.objectInterpretation, object_mode)


def source_claims(tree: ET.Element) -> list[ClaimSpec]:
    div = one(tree, "./tei:text/tei:body/tei:div")
    specs = []

    def claim(
        identifier: str,
        subject: str,
        predicate: str,
        obj: str,
        context: str,
        element: ET.Element | None = None,
        attribute: str | None = None,
        datatype: URIRef | None = None,
        construction: str | None = None,
    ) -> None:
        specs.append(
            ClaimSpec(
                identifier,
                subject,
                predicate,
                obj,
                context,
                element,
                attribute,
                datatype,
                construction,
            )
        )

    claim(
        "representation-assignment",
        "representation-letter",
        "representation-of",
        "text-letter",
        "context-construction",
        construction=PROJECTION
        + " Assignment follows text-letter's explicit delimitation criterion.",
    )
    claim(
        "text-document",
        "text-letter",
        "text-of-document",
        "letter",
        "context-construction",
        div,
        construction="The importer assigns the delimited linguistic content of the source's original-letter div to its described letter document, retaining dateline, opener, signature and postscript while excluding editorial note subtrees. This is an explicit mapping construction supported by that source container.",
    )
    header = one(tree, "./tei:teiHeader")
    title = one(header, "./tei:fileDesc/tei:titleStmt")
    publication = one(header, "./tei:fileDesc/tei:publicationStmt")
    manuscript = one(header, "./tei:fileDesc/tei:sourceDesc/tei:msDesc")
    origin = one(manuscript, "./tei:history/tei:origin")
    correspondence = one(header, "./tei:profileDesc/tei:correspDesc")
    sent = one(correspondence, "./tei:correspAction[@type='sent']")
    received = one(correspondence, "./tei:correspAction[@type='received']")
    if (
        received.find("tei:date", NS) is not None
        or received.find("tei:placeName", NS) is not None
    ):
        raise ValueError("unexpected received date or place")
    author = one(title, "./tei:author/tei:persName")
    sender = one(sent, "./tei:persName")
    recipient = one(received, "./tei:persName")
    claim(
        "author", "letter", "author", "person-schuchardt", "context-catalogue", author
    )
    claim(
        "document-carrier",
        "letter",
        "carrier",
        "carrier",
        "context-construction",
        manuscript,
        construction="The importer distinguishes the document described by the edition from the material carrier described in msDesc and relates these two handles within this single-source case.",
    )
    claim(
        "origin-carrier",
        "event-origin",
        "origin-of",
        "carrier",
        "context-origin",
        origin,
    )
    claim(
        "sent-document",
        "event-sending",
        "sent-document",
        "letter",
        "context-sending",
        sent,
    )
    claim(
        "sender",
        "event-sending",
        "sender",
        "person-schuchardt",
        "context-sending",
        sender,
    )
    claim(
        "recipient",
        "letter",
        "recipient",
        "person-hasdeu",
        "context-correspondence",
        recipient,
    )
    for identifier, subject, predicate, context, element in (
        (
            "carrier-material",
            "carrier",
            "material",
            "context-catalogue",
            one(manuscript, ".//tei:material"),
        ),
        (
            "carrier-repository",
            "carrier",
            "repository",
            "context-catalogue",
            one(manuscript, ".//tei:repository"),
        ),
        (
            "carrier-shelfmark",
            "carrier",
            "shelfmark",
            "context-catalogue",
            one(manuscript, ".//tei:idno[@type='shelfmark']"),
        ),
        (
            "source-pid",
            "letter",
            "source-identifier",
            "context-publication",
            one(publication, "./tei:idno[@type='PID']"),
        ),
        (
            "dateline",
            "text-letter",
            "dateline",
            "context-letter",
            one(div, "./tei:dateline"),
        ),
        (
            "geo-lexical",
            "place-graz",
            "geo-lexical",
            "context-normalized-place",
            one(header, ".//tei:geo"),
        ),
    ):
        claim(
            identifier,
            subject,
            predicate,
            "".join(element.itertext()),
            context,
            element,
            datatype=XSD.string,
        )
    claim(
        "source-div-id",
        "letter",
        "source-identifier",
        div.attrib["{" + NS["xml"] + "}id"],
        "context-letter",
        div,
        "xml:id",
        XSD.string,
    )
    for identifier, subject, context, element in (
        (
            "origin-date",
            "event-origin",
            "context-origin",
            one(origin, "./tei:origDate"),
        ),
        ("sending-date", "event-sending", "context-sending", one(sent, "./tei:date")),
    ):
        claim(
            identifier,
            subject,
            "date",
            element.attrib["when"],
            context,
            element,
            "when",
            XSD.date,
        )
    issued = one(publication, "./tei:date")
    claim(
        "publication-year",
        "publication",
        "publication-year",
        issued.attrib["when"],
        "context-publication",
        issued,
        "when",
        XSD.gYear,
    )
    for identifier, subject, context, element in (
        (
            "origin-place",
            "event-origin",
            "context-origin",
            one(origin, "./tei:origPlace"),
        ),
        (
            "sending-place",
            "event-sending",
            "context-sending",
            one(sent, "./tei:placeName"),
        ),
    ):
        claim(identifier, subject, "place", "place-graz", context, element)

    for identifier, subject, element, context in (
        ("author", "person-schuchardt", author, "context-catalogue"),
        ("sender", "person-schuchardt", sender, "context-sending"),
        ("recipient", "person-hasdeu", recipient, "context-correspondence"),
        ("graz-origin", "place-graz", one(origin, "./tei:origPlace"), "context-origin"),
        ("graz-sending", "place-graz", one(sent, "./tei:placeName"), "context-sending"),
    ):
        claim(
            "name-" + identifier,
            subject,
            "name-use",
            "form-" + identifier,
            context,
            element,
        )
        for attribute in ("ref", "corresp"):
            if attribute in element.attrib:
                claim(
                    f"reference-{identifier}-{attribute}",
                    subject,
                    "source-reference",
                    element.attrib[attribute],
                    context,
                    element,
                    attribute,
                    XSD.anyURI,
                )

    mentions = list(div.iter("{" + TEI + "}persName"))
    mention_specs = (
        ("diez", "person-diez"),
        ("frollo", "person-frollo"),
        ("frollo-note", "person-frollo"),
        ("signature", "person-schuchardt"),
    )
    for element, (identifier, referent) in zip(mentions, mention_specs, strict=True):
        context = "context-notes" if identifier == "frollo-note" else "context-letter"
        claim(
            "denotation-" + identifier,
            "mention-" + identifier,
            "denotes",
            referent,
            context,
            element,
            "ref",
        )
        claim(
            "realization-" + identifier,
            "mention-" + identifier,
            "realizes-form",
            "form-" + identifier,
            context,
            element,
        )
        claim(
            "name-" + identifier,
            referent,
            "name-use",
            "form-" + identifier,
            context,
            element,
        )
        claim(
            "reference-" + identifier,
            referent,
            "source-reference",
            element.attrib["ref"],
            context,
            element,
            "ref",
            XSD.anyURI,
        )
    return specs


def add_claim(graph: Graph, tree: ET.Element, paths: dict, spec: ClaimSpec) -> None:
    identifier, subject, predicate, obj, context = (
        spec.identifier,
        spec.subject,
        spec.predicate,
        spec.obj,
        spec.context,
    )
    element, attribute, datatype, construction = (
        spec.element,
        spec.attribute,
        spec.datatype,
        spec.construction,
    )
    proposition = record(
        graph, "proposition-" + identifier, "PropositionRecord", identifier
    )
    graph.add((proposition, P6.propositionSubject, CASE[subject]))
    graph.add((proposition, P6.propositionPredicate, CASE["predicate-" + predicate]))
    if datatype:
        add_literal(graph, proposition, P6.propositionObjectLiteral, obj, datatype)
    else:
        graph.add((proposition, P6.propositionObjectReference, CASE[obj]))
    graph.add((proposition, P6.context, CASE[context]))
    statement = record(graph, "claim-" + identifier, "ClaimRecord", identifier)
    graph.add((statement, P6.claimContent, proposition))
    graph.add((statement, P6.claimAgent, CASE.importer))
    add_literal(graph, statement, P6.stance, "assert" if construction else "report")
    add_literal(graph, statement, P6.lifecycle, "active")
    if element is not None:
        support = source_location(graph, tree, paths, element, attribute)
        graph.add((proposition, VOC.sourceLocation, support))
        graph.add((statement, VOC.sourceLocation, support))
    if construction:
        add_literal(graph, statement, VOC.construction, construction)


def selection(
    graph: Graph,
    contents: dict,
    identifier: str,
    representation: str,
    start: int,
    end: int,
) -> URIRef:
    selected = record(graph, identifier, "TextRangeSelectionRecord")
    graph.add((selected, P6.representation, CASE[representation]))
    add_literal(graph, selected, P6.start, str(start), XSD.nonNegativeInteger)
    add_literal(graph, selected, P6.end, str(end), XSD.nonNegativeInteger)
    add_literal(graph, selected, P6.quote, contents[representation][start:end])
    return selected


def add_annotations(
    graph: Graph,
    tree: ET.Element,
    paths: dict,
    contents: dict,
    spans: dict,
    anchors: dict,
) -> None:
    div = one(tree, "./tei:text/tei:body/tei:div")
    for spec in source_claims(tree):
        if spec.predicate == "name-use" and spec.identifier in {
            "name-author",
            "name-sender",
            "name-recipient",
            "name-graz-origin",
            "name-graz-sending",
        }:
            form = record(
                graph,
                spec.obj,
                "NameFormRecord",
                "Exact source name character data: "
                + spec.identifier.removeprefix("name-"),
            )
            add_literal(graph, form, P6.form, "".join(spec.element.itertext()))
            graph.add(
                (
                    form,
                    VOC.sourceLocation,
                    source_location(graph, tree, paths, spec.element),
                )
            )
    for note in div.iter("{" + TEI + "}note"):
        number = f"{int(note.attrib['n']):02}"
        annotation = record(
            graph, "note-" + number, "AnnotationRecord", "Editorial note " + number
        )
        insertion = selection(
            graph,
            contents,
            "selection-note-insertion-" + number,
            "representation-letter",
            anchors[number],
            anchors[number],
        )
        graph.add((annotation, P6.targetSelection, insertion))
        graph.add(
            (annotation, P6.annotationBody, CASE["representation-note-" + number])
        )
        graph.add(
            (annotation, VOC.sourceLocation, source_location(graph, tree, paths, note))
        )
        add_literal(
            graph,
            annotation,
            VOC.construction,
            "Anchor is the source note's insertion point in the letter projection; no entire semantic target is inferred.",
        )

    mentions = list(div.iter("{" + TEI + "}persName"))
    mention_specs = (
        ("diez", "person-diez"),
        ("frollo", "person-frollo"),
        ("frollo-note", "person-frollo"),
        ("signature", "person-schuchardt"),
    )
    for element, (identifier, _referent) in zip(mentions, mention_specs, strict=True):
        representation, start, end = spans[element]
        mention = record(graph, "mention-" + identifier, "MentionRecord", identifier)
        chosen = selection(
            graph,
            contents,
            "selection-mention-" + identifier,
            representation,
            start,
            end,
        )
        graph.add((mention, P6.targetSelection, chosen))
        graph.add(
            (mention, VOC.sourceLocation, source_location(graph, tree, paths, element))
        )
        form = record(
            graph,
            "form-" + identifier,
            "NameFormRecord",
            "Exact source name form: " + identifier,
        )
        add_literal(graph, form, P6.form, contents[representation][start:end])
        graph.add(
            (form, VOC.sourceLocation, source_location(graph, tree, paths, element))
        )
        graph.add((mention, P6.annotationClaim, CASE["claim-denotation-" + identifier]))
        graph.add((mention, P6.annotationBody, form))


def add_preservation(
    graph: Graph, tree: ET.Element, paths: dict, contents: dict, spans: dict
) -> None:
    body = one(tree, "./tei:text/tei:body")
    reading = record(
        graph,
        "structure-source-body",
        "StructuralReadingRecord",
        "Preservation view of every P5 body element",
    )
    add_literal(graph, reading, VOC.preservationRole, "preservation-only")
    body_nodes = list(body.iter())
    node_ids = {
        element: CASE[f"source-node-{index:03}"]
        for index, element in enumerate(body_nodes)
    }
    parents = {child: parent for parent in body.iter() for child in parent}
    for index, element in enumerate(body_nodes):
        node = record(graph, f"source-node-{index:03}", "StructuralNodeRecord")
        parent = parents.get(element)
        graph.add(
            (node, VOC.parent, node_ids[parent] if parent is not None else reading)
        )
        add_literal(
            graph,
            node,
            VOC.position,
            str(list(parent).index(element) if parent is not None else 0),
            XSD.nonNegativeInteger,
        )
        add_literal(graph, node, VOC.xmlName, element.tag)
        add_literal(
            graph,
            node,
            VOC.xmlAttributes,
            json.dumps(element.attrib, ensure_ascii=False, sort_keys=True),
            RDF.JSON,
        )
        add_literal(graph, node, VOC.xmlText, element.text or "")
        add_literal(graph, node, VOC.xmlTail, element.tail or "")
        add_literal(graph, node, VOC.sourceXPath, paths[element])
        add_literal(graph, node, VOC.preservationRole, "preservation-only")
        graph.add((node, VOC.sourceSnapshot, CASE["source-snapshot"]))
        if element in spans:
            graph.add(
                (
                    node,
                    VOC.selection,
                    selection(
                        graph, contents, f"selection-node-{index:03}", *spans[element]
                    ),
                )
            )


def coverage_report(tree: ET.Element, graph: Graph, anchors: dict) -> dict:
    body_nodes = list(one(tree, "./tei:text/tei:body").iter())
    mentions = list(
        one(tree, "./tei:text/tei:body/tei:div").iter("{" + TEI + "}persName")
    )
    coverage = {
        "profile": PROFILE,
        "source_sha256": SHA256,
        "source_url": SOURCE,
        "license": LICENSE,
        "attribution": ATTRIBUTION,
        "projection": PROJECTION,
        "counts": {
            "body_elements": len(body_nodes),
            "editorial_notes": len(anchors),
            "named_mentions": len(mentions),
            "triples": len(graph),
        },
        "semantic_map": [
            "document and carrier",
            "text and fixed representation",
            "author, sender and recipient roles",
            "separate carrier-origin and sending events, places and dates",
            "XML publication year 2022",
            "exact dateline",
            "four encoded person mentions and independent exact forms",
            "reported source URI fields",
            "eleven note bodies and insertion anchors",
        ],
        "preservation_only": [
            "all body element names, attributes, hierarchy, text and tails",
            "uninterpreted rend/rendition, references, page and line milestones",
            "entire remaining header and trailing xml-model instructions in the byte-identical source",
            "bibl year 2016 as cited-edition metadata",
            "normalized-place country Austria without a historical-country assertion",
        ],
        "source_observations": {
            "pid": "o:hsa.letter.4493",
            "div_xml_id": "L.4492",
            "repository": "Unbekannt",
            "geo": "15.45,47.06667",
            "unknown_rendition": {"rend": "unknown", "rendition": "#none"},
        },
        "limits": [
            "No full P5 semantic roundtrip, OWL reasoning or P5 schema validation.",
            "Imported claims report source metadata under importer responsibility; no independent historical verification.",
            "No receipt date/place, writing-agent attribution, residence, historical country, geographic axis normalization or manuscript image evidence inferred.",
            "No note language inferred from inherited xml:lang; encoding metadata are preserved.",
            "The Frollo professorship passage is preserved without inferring appointment.",
            "Archival byte recovery and parsed Unicode projection are separate preservation guarantees.",
        ],
    }
    return coverage


def create_case(payload: bytes) -> tuple[Graph, dict]:
    tree, paths = source_tree(payload)
    contents, spans, anchors = project(one(tree, "./tei:text/tei:body/tei:div"))
    graph = Graph()
    add_initial_records(graph, payload, contents)
    add_referents(graph)
    add_contexts(graph)
    for spec in source_claims(tree):
        add_claim(graph, tree, paths, spec)
    add_annotations(graph, tree, paths, contents, spans, anchors)
    add_preservation(graph, tree, paths, contents, spans)
    return graph, coverage_report(tree, graph, anchors)
