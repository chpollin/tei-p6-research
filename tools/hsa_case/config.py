"""Namespaces and vocabulary of the fixed HSA profile."""

from pathlib import Path

from rdflib import Namespace
from rdflib.namespace import RDF, XSD

ROOT = Path(__file__).resolve().parents[2]
BASE = Path("experiments/hsa_letter_4493")
REPRESENTATION = Path("10_markdown/documents/hsa-letter-4493-2026-09-07.md")
SHA256 = "f37ff85df57405753aa0b6d1db63f3a24fcbd33ab1ef7fb54b68844e556e2438"
SOURCE = "https://gams.uni-graz.at/o:hsa.letter.4493/TEI_SOURCE"
LICENSE = "https://creativecommons.org/licenses/by-nc/4.0/"
ATTRIBUTION = "Hugo Schuchardt Archiv, Universität Graz; detailed editorial and institutional attribution retained in p5.xml"
PROFILE = "https://example.org/tei-p6-research/profile/hsa-4493/1"
P6 = Namespace("https://example.org/tei-p6-research/ontology/")
CASE = Namespace("https://example.org/tei-p6-research/case/hsa-4493/")
VOC = Namespace("https://example.org/tei-p6-research/case-vocabulary/hsa-4493/")
XML_BINDING = "https://example.org/tei-p6-research/binding/hsa-4493/1"
COMPACT_BINDING = "https://example.org/tei-p6-research/binding/hsa-4493/2"
TEI = "http://www.tei-c.org/ns/1.0"
REFERENTS = {
    "letter": "Letter document described by HSA PID 4493",
    "carrier": "Material carrier described in msDesc",
    "person-schuchardt": "Hugo Schuchardt, source referential handle",
    "person-hasdeu": "Bogdan Petriceicu Hasdeu, source referential handle",
    "person-diez": "Diez, source referential handle",
    "person-frollo": "Frollo, shared source reference P.1537",
    "place-graz": "Graz, source referential handle",
    "event-origin": "Carrier origin context recorded by msDesc/history/origin",
    "event-sending": "Sending event described by correspAction sent",
    "publication": "XML edition publication described in publicationStmt",
}

CONCEPTS = (
    (
        "Person",
        "Revisable expectation that this source handle concerns a person; documentary records remain distinct from any externally identified person.",
        ("person-schuchardt", "person-hasdeu", "person-diez", "person-frollo"),
    ),
    (
        "Place",
        "Revisable expectation of a place described in the source; historical country and coordinate interpretation remain unspecified.",
        ("place-graz",),
    ),
    (
        "LetterDocument",
        "Revisable expectation of the letter as a documentary object distinguished from its linguistic content and material carrier.",
        ("letter",),
    ),
    (
        "MaterialCarrier",
        "Revisable expectation of the material carrier described by msDesc; neither physical inspection nor image evidence is supplied.",
        ("carrier",),
    ),
    (
        "CarrierOrigin",
        "Revisable expectation of an origin occurrence for the carrier as framed by msDesc/history/origin; no writing action or actor is implied.",
        ("event-origin",),
    ),
    (
        "SendingEvent",
        "Revisable expectation of a sending occurrence described by the source correspondence action; source metadata remain reports.",
        ("event-sending",),
    ),
    (
        "Publication",
        "Revisable expectation of the XML edition publication described by publicationStmt, distinct from snapshot acquisition and cited bibliography.",
        ("publication",),
    ),
)

CONTEXTS = {
    "context-origin": "source-carrier-origin",
    "context-sending": "source-correspondence-sent",
    "context-correspondence": "source-correspondence-roles",
    "context-publication": "source-xml-publication",
    "context-catalogue": "source-description",
    "context-letter": "source-letter-transcription",
    "context-notes": "source-editorial-annotation",
    "context-construction": "importer-construction",
    "context-normalized-place": "source-normalized-place-metadata",
}
NS = {"tei": TEI, "xml": "http://www.w3.org/XML/1998/namespace"}
PROJECTION = "ElementTree XML character data in document order, retaining parsed XML whitespace and child tails; note subtrees excluded from letter, each separately projected; no separators inserted for markup. XML line-end normalization differs from archival bytes."

VOCABULARY = {
    "profile": (
        "literal",
        XSD.anyURI,
        "Fixed semantic profile identifier, distinct from the binding version; no model 0.3 conformance is claimed.",
    ),
    "sourceURL": (
        "literal",
        XSD.anyURI,
        "Source URI recorded as a value; no world identity or automatic dereference is asserted.",
    ),
    "sha256": ("literal", XSD.string, "SHA-256 of the exact archived UTF-8 XML bytes."),
    "license": (
        "literal",
        XSD.anyURI,
        "Licence applying to copied and derived source text.",
    ),
    "attribution": (
        "literal",
        XSD.string,
        "Attribution for source text; does not attribute every imported claim to a source editor.",
    ),
    "sourceSnapshot": (
        "reference",
        P6.Record,
        "References the documentary record of the fixed source snapshot.",
    ),
    "sourceLocation": (
        "reference",
        P6.Record,
        "References an indexed source location supporting an import report. This is a bounded import support relation, not a universal evidence model.",
    ),
    "sourceXPath": (
        "literal",
        XSD.string,
        "Absolute indexed tei:-prefixed element XPath, optionally ending in a named attribute; tei denotes the TEI namespace.",
    ),
    "sourceValue": (
        "literal",
        XSD.string,
        "Checked element character data or attribute value at the recorded XPath, after XML parser line-end normalization.",
    ),
    "construction": (
        "literal",
        XSD.string,
        "Explicit deterministic construction or scoping decision made by this importer.",
    ),
    "projection": (
        "literal",
        XSD.string,
        "Reproducible character-data projection policy; no silent whitespace normalization.",
    ),
    "parent": (
        "reference",
        P6.StructureRecord,
        "Parent in the preserved source body tree, or its structural reading root.",
    ),
    "position": (
        "literal",
        XSD.nonNegativeInteger,
        "Zero-based element-child position within the preserved source parent.",
    ),
    "xmlName": (
        "literal",
        XSD.string,
        "Preserved expanded XML element name in Clark notation.",
    ),
    "xmlAttributes": (
        "literal",
        RDF.JSON,
        "All source element attributes as a JSON object of expanded names to exact parsed values.",
    ),
    "xmlText": (
        "literal",
        XSD.string,
        "Parsed XML character data immediately inside the element, or the empty string when absent.",
    ),
    "xmlTail": (
        "literal",
        XSD.string,
        "Parsed XML character data after the element, or the empty string when absent; note tails belong to the letter projection.",
    ),
    "selection": (
        "reference",
        P6.SelectionRecord,
        "Projected character span associated with a preserved source node.",
    ),
    "preservationRole": (
        "literal",
        XSD.string,
        "Marks preservation-only source tree records; their retained markup is not assigned an expanded semantic interpretation.",
    ),
}

PREDICATES = {
    "text-of-document": (
        "record",
        "referent",
        "The linguistic content described by this TextRecord is the content of the described document under the record's explicit boundary and identity criterion.",
    ),
    "author": (
        "referent",
        "referent",
        "The source names this person as author of the described letter.",
    ),
    "carrier": (
        "referent",
        "referent",
        "The bounded mapping distinguishes the letter document from the material carrier described in msDesc.",
    ),
    "material": (
        "referent",
        "record",
        "The source records the literal material description for the carrier; the object is a literal value.",
    ),
    "repository": (
        "referent",
        "record",
        "The source records the literal repository field for the carrier, including an explicit unknown value.",
    ),
    "shelfmark": (
        "referent",
        "record",
        "The source records a shelfmark string for the carrier.",
    ),
    "origin-of": (
        "referent",
        "referent",
        "The source history/origin supplies an origin context for the described carrier; no writing action or agent is inferred.",
    ),
    "sent-document": (
        "referent",
        "referent",
        "The source correspAction of type sent concerns the described letter.",
    ),
    "sender": (
        "referent",
        "referent",
        "The source correspAction of type sent names this person in the sender role.",
    ),
    "recipient": (
        "referent",
        "referent",
        "The correspondence source's received action names this recipient; no receipt date or place is inferred.",
    ),
    "date": (
        "referent",
        "record",
        "The source supplies this literal date within the specifically identified event context.",
    ),
    "place": (
        "referent",
        "referent",
        "The source supplies this place in the specifically identified origin or sending context.",
    ),
    "publication-year": (
        "referent",
        "record",
        "The publicationStmt supplies the year of the XML edition's publication, as a literal gYear.",
    ),
    "source-reference": (
        "record",
        "record",
        "An identified source field supplies this URI value for the described record; no equivalence, external identity or retrieval is inferred.",
    ),
    "name-use": (
        "referent",
        "record",
        "The source uses the exact character-data form documented by the NameFormRecord for the subject referent in this context.",
    ),
    "denotes": (
        "record",
        "referent",
        "The source's encoded person reference supports an import report assigning this mention to the described referent handle.",
    ),
    "realizes-form": (
        "record",
        "record",
        "The mention's exact projected character data realizes the form documented by the NameFormRecord.",
    ),
    "representation-of": (
        "record",
        "record",
        "The importer assigns this constructed representation to the delimited linguistic content recorded by this TextRecord.",
    ),
    "dateline": (
        "record",
        "record",
        "The source records this literal dateline within the letter body; its short year is retained without reconciliation to metadata dates.",
    ),
    "source-identifier": (
        "record",
        "record",
        "The named source context supplies this identifier string; distinct source fields are not silently reconciled.",
    ),
    "geo-lexical": (
        "record",
        "record",
        "The source's normalized-place metadata contains this exact geo string. Axis order and historical geography remain uninterpreted.",
    ),
}
