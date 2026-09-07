"""Validate explicit records against the fixed source and declared mappings."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

from rdflib import Graph, Literal, URIRef
from rdflib.namespace import OWL, RDF, RDFS, XSD

from tools.hsa_case.config import (
    ATTRIBUTION,
    CASE,
    CONCEPTS,
    CONTEXTS,
    LICENSE,
    P6,
    PREDICATES,
    PROFILE,
    PROJECTION,
    REFERENTS,
    ROOT,
    SHA256,
    SOURCE,
    VOC,
    VOCABULARY,
)
from tools.hsa_case.mapping import source_claims
from tools.hsa_case.source import one, project, resolve, source_tree


def _value(graph: Graph, subject: URIRef, predicate: URIRef) -> URIRef | Literal:
    values = list(graph.objects(subject, predicate))
    if len(values) != 1:
        raise ValueError(f"expected exactly one {predicate} on {subject}")
    return values[0]


REQUIRED = {
    P6.Package: (
        VOC.profile,
        VOC.sourceURL,
        VOC.license,
        VOC.attribution,
        VOC.sha256,
        VOC.projection,
    ),
    P6.AgentRecord: (P6.preferredLabel,),
    P6.TextRecord: (P6.preferredLabel, P6.identityCriteria),
    P6.ReferentRecord: (P6.preferredLabel, P6.expectedReferentType, VOC.construction),
    P6.RepresentationRecord: (P6.preferredLabel, P6.content),
    P6.NameFormRecord: (P6.preferredLabel, P6.form, VOC.sourceLocation),
    P6.ContextRecord: (P6.preferredLabel, P6.scope),
    P6.ConceptRecord: (P6.preferredLabel, P6.definition),
    P6.PredicateRecord: (
        P6.preferredLabel,
        P6.definition,
        P6.subjectInterpretation,
        P6.objectInterpretation,
    ),
    P6.PropositionRecord: (
        P6.preferredLabel,
        P6.propositionSubject,
        P6.propositionPredicate,
        P6.context,
    ),
    P6.ClaimRecord: (
        P6.preferredLabel,
        P6.claimContent,
        P6.claimAgent,
        P6.stance,
        P6.lifecycle,
    ),
    P6.AnnotationRecord: (
        P6.preferredLabel,
        P6.targetSelection,
        P6.annotationBody,
        VOC.sourceLocation,
        VOC.construction,
    ),
    P6.MentionRecord: (
        P6.preferredLabel,
        P6.targetSelection,
        P6.annotationBody,
        P6.annotationClaim,
        VOC.sourceLocation,
    ),
    P6.TextRangeSelectionRecord: (P6.representation, P6.start, P6.end, P6.quote),
    P6.StructuralReadingRecord: (P6.preferredLabel, VOC.preservationRole),
    P6.StructuralNodeRecord: (
        VOC.parent,
        VOC.position,
        VOC.xmlName,
        VOC.xmlAttributes,
        VOC.xmlText,
        VOC.xmlTail,
        VOC.sourceXPath,
        VOC.preservationRole,
        VOC.sourceSnapshot,
    ),
}
OPTIONAL = {
    P6.Package: (P6.member,),
    P6.RepresentationRecord: (VOC.projection, VOC.sourceSnapshot),
    P6.PropositionRecord: (
        P6.propositionObjectReference,
        P6.propositionObjectLiteral,
        VOC.sourceLocation,
    ),
    P6.ClaimRecord: (VOC.sourceLocation, VOC.construction),
    P6.StructuralNodeRecord: (VOC.selection,),
}


def validate_shapes(graph: Graph, core: Graph, *, semantic: bool) -> None:
    """Use explicit profile constraints; no inferred triples are materialized."""
    kinds = {
        subject: _value(graph, subject, RDF.type) for subject in set(graph.subjects())
    }
    for subject, kind in kinds.items():
        required = REQUIRED.get(kind)
        if kind == P6.Record:
            required = (
                (P6.preferredLabel, VOC.sourceURL, VOC.sha256)
                if subject == CASE["source-snapshot"]
                else (P6.preferredLabel, VOC.sourceXPath, VOC.sourceSnapshot)
            )
            if subject != CASE["source-snapshot"] and not semantic:
                required += (VOC.sourceValue,)
        if required is None:
            raise ValueError(f"record class outside the HSA profile: {kind}")
        required = (*required, RDF.type, P6.responsibleAgent)
        allowed = {*required, *OPTIONAL.get(kind, ())}
        if subject == CASE["source-snapshot"] and not semantic:
            required = (*required, P6.representation)
            allowed.add(P6.representation)
        for predicate in required:
            _value(graph, subject, predicate)
        if set(graph.predicates(subject)) - allowed:
            raise ValueError(f"unexpected record property: {subject}")
        for predicate in allowed - {P6.member}:
            if len(list(graph.objects(subject, predicate))) > 1:
                raise ValueError(f"multiple values for {predicate} on {subject}")
        if _value(graph, subject, P6.responsibleAgent) != CASE.importer:
            raise ValueError("record lacks importer responsibility")
        if kind == P6.PropositionRecord:
            objects = [
                *graph.objects(subject, P6.propositionObjectLiteral),
                *graph.objects(subject, P6.propositionObjectReference),
            ]
            if len(objects) != 1:
                raise ValueError("proposition requires exactly one object kind")
    for _subject, predicate, obj in graph:
        if predicate == RDF.type:
            continue
        if str(predicate).startswith(str(VOC)):
            mode, expected, _ = VOCABULARY[str(predicate)[len(str(VOC)) :]]
        else:
            mode = (
                "reference"
                if (predicate, RDF.type, OWL.ObjectProperty) in core
                else "literal"
            )
            expected = core.value(predicate, RDFS.range)
        if mode == "reference":
            if not isinstance(obj, URIRef) or obj not in kinds:
                raise ValueError(f"expected typed record reference: {predicate}")
            lineage = set(core.transitive_objects(kinds[obj], RDFS.subClassOf))
            if expected not in lineage:
                raise ValueError(f"reference has wrong record class: {predicate}")
        elif not isinstance(obj, Literal) or (
            expected != RDFS.Literal and obj.datatype != expected
        ):
            raise ValueError(f"wrong literal datatype: {predicate}")
        elif obj.language or obj.datatype is None or obj.ill_typed:
            raise ValueError(f"unsupported or ill-typed profile literal: {predicate}")
        elif (
            expected == RDFS.Literal
            and obj.datatype != XSD.string
            and predicate != P6.propositionObjectLiteral
        ):
            raise ValueError(f"expected profile string literal: {predicate}")


def validate_claim_mappings(graph: Graph, tree, paths: dict) -> None:
    """Check every declared source-to-proposition mapping without invoking a builder."""
    specs = source_claims(tree)
    for kind, prefix in (
        (P6.ClaimRecord, "claim-"),
        (P6.PropositionRecord, "proposition-"),
    ):
        expected = {CASE[prefix + spec.identifier] for spec in specs}
        if set(graph.subjects(RDF.type, kind)) != expected:
            raise ValueError("mapped claim/proposition coverage mismatch")
    for spec in specs:
        proposition = CASE["proposition-" + spec.identifier]
        statement = CASE["claim-" + spec.identifier]
        obj_predicate = (
            P6.propositionObjectLiteral
            if spec.datatype
            else P6.propositionObjectReference
        )
        obj = (
            Literal(spec.obj, datatype=spec.datatype, normalize=False)
            if spec.datatype
            else CASE[spec.obj]
        )
        expected = {
            P6.propositionSubject: CASE[spec.subject],
            P6.propositionPredicate: CASE["predicate-" + spec.predicate],
            obj_predicate: obj,
            P6.context: CASE[spec.context],
        }
        for predicate, value in expected.items():
            if _value(graph, proposition, predicate) != value:
                raise ValueError(
                    f"source mapping mismatch: {spec.identifier} / {predicate}"
                )
        for predicate, value in (
            (P6.claimContent, proposition),
            (
                P6.stance,
                Literal(
                    "assert" if spec.construction else "report", datatype=XSD.string
                ),
            ),
            (P6.lifecycle, Literal("active", datatype=XSD.string)),
        ):
            if _value(graph, statement, predicate) != value:
                raise ValueError(
                    f"claim mapping mismatch: {spec.identifier} / {predicate}"
                )
        reasons = set(graph.objects(statement, VOC.construction))
        expected_reasons = (
            {Literal(spec.construction, datatype=XSD.string)}
            if spec.construction
            else set()
        )
        if reasons != expected_reasons:
            raise ValueError(f"construction rationale mismatch: {spec.identifier}")
        for record in (proposition, statement):
            supports = list(graph.objects(record, VOC.sourceLocation))
            if spec.element is None:
                if supports:
                    raise ValueError("unexpected construction source")
            else:
                xpath = paths[spec.element] + (
                    "/@" + spec.attribute if spec.attribute else ""
                )
                if (
                    len(supports) != 1
                    or str(_value(graph, supports[0], VOC.sourceXPath)) != xpath
                ):
                    raise ValueError(
                        f"source mapping location mismatch: {spec.identifier}"
                    )
        if spec.predicate == "name-use":
            form = CASE[spec.obj]
            if str(_value(graph, form, P6.form)) != "".join(spec.element.itertext()):
                raise ValueError("name form differs from source")
            support = _value(graph, form, VOC.sourceLocation)
            if str(_value(graph, support, VOC.sourceXPath)) != paths[spec.element]:
                raise ValueError("name form source location mismatch")
        if spec.predicate == "denotes":
            mention = CASE[spec.subject]
            if (
                _value(graph, mention, P6.annotationClaim) != statement
                or _value(graph, mention, P6.annotationBody)
                != CASE["form-" + spec.identifier.removeprefix("denotation-")]
            ):
                raise ValueError("mention claim/form assignment mismatch")
    for name, (subject_mode, object_mode, definition) in PREDICATES.items():
        for predicate, value in (
            (P6.definition, definition),
            (P6.subjectInterpretation, subject_mode),
            (P6.objectInterpretation, object_mode),
        ):
            if _value(graph, CASE["predicate-" + name], predicate) != Literal(
                value, datatype=XSD.string
            ):
                raise ValueError(f"changed predicate interpretation: {name}")


def validate_references(graph: Graph, root: Path) -> Graph:
    subjects = set(graph.subjects(RDF.type, None))
    core = Graph().parse(root / "ontology/core.ttl", format="turtle")
    types = set(core.subjects(RDF.type, OWL.Class))
    properties = {
        RDF.type,
        *core.subjects(RDF.type, OWL.ObjectProperty),
        *core.subjects(RDF.type, OWL.DatatypeProperty),
        *(VOC[name] for name in VOCABULARY),
    }
    for subject, predicate, obj in graph:
        if (
            not isinstance(subject, URIRef)
            or not str(subject).startswith(str(CASE))
            or subject not in subjects
        ):
            raise ValueError("undeclared case subject")
        if predicate == RDF.type and obj not in types:
            raise ValueError("non-documentary case type")
        if predicate not in properties:
            raise ValueError(
                f"undeclared predicate or world-identity triple: {predicate}"
            )
        if predicate != RDF.type and isinstance(obj, URIRef) and obj not in subjects:
            raise ValueError(f"unresolved record reference: {obj}")
    if set(graph.objects(CASE.package, P6.member)) != subjects - {CASE.package}:
        raise ValueError("package membership does not close over every record")
    for predicate, expected, datatype in (
        (VOC.profile, PROFILE, XSD.anyURI),
        (VOC.sourceURL, SOURCE, XSD.anyURI),
        (VOC.license, LICENSE, XSD.anyURI),
        (VOC.attribution, ATTRIBUTION, XSD.string),
        (VOC.sha256, SHA256, XSD.string),
        (VOC.projection, PROJECTION, XSD.string),
    ):
        if _value(graph, CASE.package, predicate) != Literal(
            expected, datatype=datatype
        ):
            raise ValueError("package provenance/rights mismatch")
    for predicate, expected, datatype in (
        (VOC.sourceURL, SOURCE, XSD.anyURI),
        (VOC.sha256, SHA256, XSD.string),
    ):
        if _value(graph, CASE["source-snapshot"], predicate) != Literal(
            expected, datatype=datatype
        ):
            raise ValueError("snapshot provenance mismatch")
    return core


def validate_classifications(graph: Graph) -> None:
    for kind, identifiers in (
        (P6.Package, {"package"}),
        (P6.AgentRecord, {"importer"}),
        (P6.TextRecord, {"text-letter"}),
        (P6.ReferentRecord, set(REFERENTS)),
        (P6.ContextRecord, set(CONTEXTS)),
        (P6.ConceptRecord, {"concept-" + name for name, _, _ in CONCEPTS}),
    ):
        if set(graph.subjects(RDF.type, kind)) != {CASE[name] for name in identifiers}:
            raise ValueError("fixed record inventory mismatch")
    for name, scope in CONTEXTS.items():
        if _value(graph, CASE[name], P6.scope) != Literal(scope, datatype=XSD.string):
            raise ValueError("context scope mismatch")
    for name, definition, referents in CONCEPTS:
        concept = CASE["concept-" + name]
        if _value(graph, concept, P6.definition) != Literal(
            definition, datatype=XSD.string
        ):
            raise ValueError("concept definition mismatch")
        for referent in referents:
            if _value(graph, CASE[referent], P6.expectedReferentType) != concept:
                raise ValueError("expected referent type mismatch")


def validate_source(
    graph: Graph,
    payload: bytes,
    tree,
    paths: dict,
    contents: dict,
    anchors: dict,
    *,
    semantic: bool,
) -> None:
    for identifier, expected in contents.items():
        if str(_value(graph, CASE[identifier], P6.content)) != expected:
            raise ValueError(f"letter/note projection mismatch: {identifier}")
    if not semantic and (
        str(_value(graph, CASE["representation-source-xml"], P6.content)).encode(
            "utf-8"
        )
        != payload
    ):
        raise ValueError("archival source representation mismatch")
    for subject in graph.subjects(VOC.sourceXPath, None):
        xpath = str(_value(graph, subject, VOC.sourceXPath))
        actual = resolve(tree, xpath)
        if (subject, VOC.sourceValue, None) in graph and str(
            _value(graph, subject, VOC.sourceValue)
        ) != actual:
            raise ValueError("source location value mismatch")
        if _value(graph, subject, VOC.sourceSnapshot) != CASE["source-snapshot"]:
            raise ValueError("source location lacks fixed snapshot")
    for selected in graph.subjects(RDF.type, P6.TextRangeSelectionRecord):
        representation = _value(graph, selected, P6.representation)
        content = str(_value(graph, representation, P6.content))
        start, end = (
            int(str(_value(graph, selected, predicate)))
            for predicate in (P6.start, P6.end)
        )
        if (
            not 0 <= start <= end <= len(content)
            or str(_value(graph, selected, P6.quote)) != content[start:end]
        ):
            raise ValueError(f"invalid selector range or quote: {selected}")
    for number, anchor in anchors.items():
        annotation = CASE["note-" + number]
        if (
            _value(graph, annotation, P6.annotationBody)
            != CASE["representation-note-" + number]
        ):
            raise ValueError("flattened or redirected note body")
        selected = _value(graph, annotation, P6.targetSelection)
        if _value(graph, selected, P6.representation) != CASE[
            "representation-letter"
        ] or any(
            str(_value(graph, selected, predicate)) != str(anchor)
            for predicate in (P6.start, P6.end)
        ):
            raise ValueError("note insertion point mismatch")
        support = _value(graph, annotation, VOC.sourceLocation)
        expected_note = one(tree, f".//tei:note[@n='{int(number)}']")
        if str(_value(graph, support, VOC.sourceXPath)) != paths[expected_note]:
            raise ValueError("note source location mismatch")
    for statement in graph.subjects(RDF.type, P6.ClaimRecord):
        if (
            _value(graph, statement, P6.claimAgent) != CASE.importer
            or _value(graph, statement, P6.responsibleAgent) != CASE.importer
        ):
            raise ValueError("claim lacks explicit importer responsibility")
        proposition = _value(graph, statement, P6.claimContent)
        _value(graph, proposition, P6.context)
        stance = str(_value(graph, statement, P6.stance))
        if stance == "report":
            support = _value(graph, statement, VOC.sourceLocation)
            if _value(graph, proposition, VOC.sourceLocation) != support:
                raise ValueError(
                    "imported proposition and claim source locations differ"
                )
            _value(graph, support, VOC.sourceXPath)
            literals = list(graph.objects(proposition, P6.propositionObjectLiteral))
            if (
                not semantic
                and literals
                and str(literals[0]) != str(_value(graph, support, VOC.sourceValue))
            ):
                raise ValueError("reported literal differs from checked source value")
        elif stance == "assert":
            _value(graph, statement, VOC.construction)
        else:
            raise ValueError("unsupported import stance")


def validate_preservation(graph: Graph, tree, paths: dict, spans: dict) -> None:
    expected_nodes = {
        paths[element]: element for element in one(tree, "./tei:text/tei:body").iter()
    }
    nodes = list(graph.subjects(RDF.type, P6.StructuralNodeRecord))
    if len(nodes) != len(expected_nodes):
        raise ValueError("body preservation coverage mismatch")
    node_by_path = {str(_value(graph, node, VOC.sourceXPath)): node for node in nodes}
    parents = {
        child: parent
        for parent in one(tree, "./tei:text/tei:body").iter()
        for child in parent
    }
    for node in nodes:
        xpath = str(_value(graph, node, VOC.sourceXPath))
        if xpath not in expected_nodes:
            raise ValueError("duplicate or unexpected preserved body path")
        element = expected_nodes.pop(xpath)
        if (
            str(_value(graph, node, VOC.xmlName)) != element.tag
            or json.loads(str(_value(graph, node, VOC.xmlAttributes))) != element.attrib
        ):
            raise ValueError("preserved source name/attributes changed")
        if str(_value(graph, node, VOC.xmlText)) != (element.text or "") or str(
            _value(graph, node, VOC.xmlTail)
        ) != (element.tail or ""):
            raise ValueError("preserved source text/tail changed")
        parent = parents.get(element)
        expected_parent = (
            node_by_path[paths[parent]]
            if parent is not None
            else CASE["structure-source-body"]
        )
        expected_position = list(parent).index(element) if parent is not None else 0
        if (
            _value(graph, node, VOC.parent) != expected_parent
            or int(str(_value(graph, node, VOC.position))) != expected_position
        ):
            raise ValueError("preserved source hierarchy/order changed")
        if element in spans:
            selected = _value(graph, node, VOC.selection)
            representation, start, end = spans[element]
            if _value(graph, selected, P6.representation) != CASE[
                representation
            ] or any(
                int(str(_value(graph, selected, predicate))) != expected
                for predicate, expected in ((P6.start, start), (P6.end, end))
            ):
                raise ValueError("preserved source projection range changed")
    for mention in graph.subjects(RDF.type, P6.MentionRecord):
        support = _value(graph, mention, VOC.sourceLocation)
        xpath = str(_value(graph, support, VOC.sourceXPath))
        node = node_by_path[xpath]
        selection = _value(graph, mention, P6.targetSelection)
        preserved = _value(graph, node, VOC.selection)
        if any(
            _value(graph, selection, predicate) != _value(graph, preserved, predicate)
            for predicate in (P6.representation, P6.start, P6.end, P6.quote)
        ):
            raise ValueError("mention differs from checked source projection range")


def validate_case(
    graph: Graph, payload: bytes, root: Path = ROOT, *, semantic: bool = False
) -> None:
    if hashlib.sha256(payload).hexdigest() != SHA256:
        raise ValueError("source snapshot hash mismatch")
    tree, paths = source_tree(payload)
    contents, spans, anchors = project(one(tree, "./tei:text/tei:body/tei:div"))
    core = validate_references(graph, root)
    validate_source(graph, payload, tree, paths, contents, anchors, semantic=semantic)
    validate_shapes(graph, core, semantic=semantic)
    validate_classifications(graph)
    validate_claim_mappings(graph, tree, paths)
    validate_mentions(graph, tree, paths, spans)
    if not semantic:
        validate_preservation(graph, tree, paths, spans)


def validate_mentions(graph: Graph, tree, paths: dict, spans: dict) -> None:
    expected = {
        paths[element]: span
        for element, span in spans.items()
        if element.tag.endswith("}persName")
    }
    mentions = list(graph.subjects(RDF.type, P6.MentionRecord))
    if len(mentions) != len(expected):
        raise ValueError("mention coverage mismatch")
    for mention in mentions:
        support = _value(graph, mention, VOC.sourceLocation)
        xpath = str(_value(graph, support, VOC.sourceXPath))
        if xpath not in expected:
            raise ValueError("unexpected or duplicate mention source")
        representation, start, end = expected.pop(xpath)
        selection = _value(graph, mention, P6.targetSelection)
        if (
            _value(graph, selection, P6.representation) != CASE[representation]
            or int(_value(graph, selection, P6.start)) != start
            or int(_value(graph, selection, P6.end)) != end
        ):
            raise ValueError("mention differs from checked source projection range")
