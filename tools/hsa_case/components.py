"""Partition one unchanged graph into semantic and preservation components."""

from rdflib import Graph
from rdflib.namespace import RDF

from tools.hsa_case.config import CASE, P6, VOC


def split_graph(graph: Graph) -> tuple[Graph, Graph]:
    preserved = {
        subject
        for subject in graph.subjects()
        if str(subject).startswith(
            (str(CASE["source-node-"]), str(CASE["selection-node-"]))
        )
    } | {CASE["representation-source-xml"], CASE["structure-source-body"]}
    semantic, preservation = Graph(), Graph()
    for triple in graph:
        subject, predicate, obj = triple
        target = (
            preservation
            if (
                subject in preserved
                or predicate == VOC.sourceValue
                or (predicate in (P6.member, P6.representation) and obj in preserved)
            )
            else semantic
        )
        target.add(triple)
    for subject in set(preservation.subjects()):
        for kind in graph.objects(subject, RDF.type):
            preservation.add((subject, RDF.type, kind))
    if set(semantic) | set(preservation) != set(graph):
        raise ValueError("component partition changed the complete graph")
    return semantic, preservation
