"""Build the fixed HSA case; maintained contract: knowledge/hsa-profile.md."""

from __future__ import annotations

import argparse
import json
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

from rdflib import Graph, Literal
from rdflib.namespace import OWL, RDF, RDFS

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tools.hsa_case.bindings import json_data, turtle, xml_data
from tools.hsa_case.bindings import parse_json as parse_json
from tools.hsa_case.bindings import parse_xml as parse_xml
from tools.hsa_case.components import split_graph
from tools.hsa_case.config import (
    BASE as BASE,
)
from tools.hsa_case.config import (
    CASE as CASE,
)
from tools.hsa_case.config import (
    P6 as P6,
)
from tools.hsa_case.config import (
    REPRESENTATION as REPRESENTATION,
)
from tools.hsa_case.config import (
    ROOT as ROOT,
)
from tools.hsa_case.config import (
    SHA256 as SHA256,
)
from tools.hsa_case.config import (
    VOC as VOC,
)
from tools.hsa_case.config import (
    VOCABULARY,
)
from tools.hsa_case.mapping import create_case as create_case
from tools.hsa_case.source import source_bytes as source_bytes
from tools.hsa_case.validation import validate_case as validate_case


def vocabulary() -> Graph:
    graph = Graph()
    for name, (kind, range_iri, definition) in VOCABULARY.items():
        subject = VOC[name]
        graph.add(
            (
                subject,
                RDF.type,
                OWL.ObjectProperty if kind == "reference" else OWL.DatatypeProperty,
            )
        )
        graph.add((subject, RDFS.range, range_iri))
        graph.add((subject, RDFS.label, Literal(name, lang="en")))
        graph.add((subject, RDFS.comment, Literal(definition, lang="en")))
    return graph


def diagram() -> bytes:
    return b"""%% Complete case overview; combine p6.* with preservation.* for the full graph.
flowchart LR
    source["HSA 4493 source snapshot"] -. source description .-> letter["letter document"]
    letter -->|import construction| carrier["material carrier"]
    origin["carrier-origin context + 1878-04-17"] -. import report .-> carrier
    sending["sending context + 1878-04-17"] -. import report .-> letter
    sending -. import report .-> sender["Schuchardt: sender role"]
    correspondence["correspondence recipient role"] -. import report .-> recipient["Hasdeu; no receipt date/place"]
    text["text identity criterion"] --> representation["letter character data; notes excluded"]
    text -->|import construction| letter
    representation --> mentions["Diez / Frollo / H. Schuchardt mentions"]
    representation --> anchors["11 source insertion points"]
    anchors --> notes["11 separate editorial-note representations"]
    notes --> frollo["G.L. Frollo mention in note 8"]
    source --> structure["all body XML nodes, attributes, hierarchy"]
    source --> archive["byte-identical P5 XML including remaining header"]
    source -. publicationStmt report .-> publication["XML edition publication: 2022; distinct from snapshot date"]
"""


def build(root: Path = ROOT, *, check: bool = False) -> dict:
    payload = source_bytes(root)
    graph, coverage = create_case(payload)
    validate_case(graph, payload, root)
    semantic, preservation = split_graph(graph)
    validate_case(semantic, payload, root, semantic=True)
    coverage["components"] = {
        "p6": {"component": "semantic", "triples": len(semantic)},
        "preservation": {"component": "preservation", "triples": len(preservation)},
        "union_triples": len(graph),
        "shared_type_triples": len(set(semantic) & set(preservation)),
        "rule": "Set union reconstructs the complete graph; preservation adds source values, source XML and body structure.",
    }
    outputs = {
        "p5.xml": payload,
        "vocabulary.ttl": turtle(vocabulary()),
        "instance.mmd": diagram(),
    }
    for name, component in (("p6", semantic), ("preservation", preservation)):
        data = json_data(component, component=coverage["components"][name]["component"])
        outputs[name + ".json"] = (
            json.dumps(data, ensure_ascii=False, indent=2) + "\n"
        ).encode("utf-8")
        outputs[name + ".xml"] = xml_data(data)
        outputs[name + ".ttl"] = turtle(component)
        views = (
            parse_json(outputs[name + ".json"]),
            parse_xml(outputs[name + ".xml"]),
            Graph().parse(data=outputs[name + ".ttl"], format="turtle"),
        )
        if any(set(view) != set(component) for view in views):
            raise ValueError("JSON/XML/RDF component data disagree")
    coverage["artifact_bytes"] = {
        name: len(content) for name, content in sorted(outputs.items())
    }
    outputs["coverage.json"] = (
        json.dumps(coverage, ensure_ascii=False, indent=2) + "\n"
    ).encode("utf-8")
    folder = root / BASE
    if check:
        for name, content in outputs.items():
            if not (folder / name).exists() or (folder / name).read_bytes() != content:
                raise ValueError(f"stale generated case file: {name}")
    else:
        folder.mkdir(parents=True, exist_ok=True)
        for name, content in outputs.items():
            target = folder / name
            temporary = target.with_suffix(target.suffix + ".tmp")
            temporary.write_bytes(content)
            temporary.replace(target)
    return coverage


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    try:
        coverage = build(args.root, check=args.check)
    except (OSError, ValueError, ET.ParseError) as exc:
        print(f"FEHLER: {exc}", file=sys.stderr)
        return 1
    print(
        f"OK: HSA 4493 case {'reproduced' if args.check else 'generated'}; {coverage['counts']}. No historical verification or OWL reasoning."
    )
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
