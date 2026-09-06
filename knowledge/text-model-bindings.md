---
title: Text Model Bindings
project:
  name: "TEI P6 Research"
  repository: "tei-p6-research"
method:
  name: Promptotyping
  url: https://dhcraft.org/Promptotyping/
status: draft
language: en
created: "2026-09-06"
updated: "2026-09-06"
related: [text-model, experiments, testing, state]
---

# Text Model Bindings

These independent project bindings encode the
[[knowledge/text-model|Abstract Text Model 0.1]]. They are neither official
TEI P6 syntax nor converters from TEI P5. Their vocabulary and preservation
contract are project posits. The candidate serialization and conformance
contract they instantiate, with the bindings that remain candidates, is
section 12 of the text model.

Sections 2 to 4 hold the JSON, XML and YAML bindings, which encode and decode
one package under an equality law. Section 6 holds the RDF export of an
entity-extension 0.2 package, which runs one way and has no decoder.

## 1. Model and encoding

An instance is the same package of agents, concepts, texts, versions,
continuity claims, selections, readings, annotations, and relations in all
three bindings. Selecting XML, JSON, or YAML changes its notation. It does not
change object identities, responsibility, selector resolution, or model rules.
The XML binding represents objects explicitly. It does not infer a
primary textual hierarchy or place annotation boundaries inside version text.

The reference API in `tools/models/bindings.py` provides two operations.

```python
encode_model(package, binding) -> str
decode_model(text, binding) -> dict
```

The binding name is exactly `json`, `xml`, or `yaml`. Both operations validate
the package against the core model. Invalid syntax, unknown fields, invalid
references, incorrect hashes, and other structural errors raise `ValueError`.
Ambiguous or absent quote selections remain valid when allowed by the core.
Successful decoding does not mean that every selection resolves. Operations
do not mutate their inputs and perform no external retrieval.

Let `E_b` encode and `D_b` decode binding `b`. For every valid package `p`, the
required preservation laws are the following.

```text
D_b(E_b(p)) = p
canonical_bytes(D_c(E_c(D_b(E_b(p))))) = canonical_bytes(p)
```

The first equality is exact data equality, including array order, optional
field presence, scalar types, and every string code point. Object-key order is
irrelevant. The second expresses the model's R11 equivalence after a binding
change. Registry order need not be significant under R11, but the bindings
preserve it nevertheless. XML root collection order is emitted consistently
with the core collection order. Segments are never merged or reordered.

These laws concern decoded data. An arbitrary input document need not retain
its original indentation, quotation style, namespace prefix, or other lexical
choices after re-encoding. The API accepts Unicode strings. Callers writing
files must use UTF-8 without automatic newline conversion.

## 2. JSON binding

JSON directly represents the existing reference package. Object keys must be
unique strings, and no unknown model fields are accepted. Arrays, strings,
integers, and `null` retain their types. Non-finite numbers, floating-point
values, booleans, and lone Unicode surrogates are outside the model. The
encoder uses readable indentation and JSON escapes where required. It does
not normalize whitespace, line endings, Unicode, or identifiers inside data.

## 3. XML binding

The root is `model` in namespace
`urn:tei-p6-research:abstract-text:0.1`. Its required unqualified attributes are
`binding_version="0.1"` and `model_version="0.1"`. All nine collections must
appear exactly once, including empty collections. No other root attributes or
collections are permitted. Every element belongs to the model namespace.

| Collection | Child record name |
|---|---|
| `agents` | `agent` |
| `concepts` | `concept` |
| `texts` | `text` |
| `versions` | `version` |
| `continuities` | `continuity` |
| `selections` | `selection` |
| `readings` | `reading` |
| `annotations` | `annotation` |
| `relations` | `relation` |

Record and field names match the model. Each record or field has an explicit
`type` of `object`, `array`, `string`, `integer`, or `null`. An object contains
one element per field, with no duplicate field names. Arrays preserve child
order. The `nodes` array uses `node` children, `segments` uses `segment`
children, and other arrays use `item`. A null field has neither text nor
children. An empty array is distinct from null and from an absent field.
Integers use decimal JSON notation without a leading plus sign or leading
zeroes. Strings are element text, not attribute values.

This complete minimal package contains a single version of `abc`.

```xml
<model xmlns="urn:tei-p6-research:abstract-text:0.1"
       binding_version="0.1" model_version="0.1">
  <agents />
  <concepts />
  <texts />
  <versions>
    <version type="object">
      <id type="string">v1</id>
      <content type="string">abc</content>
      <sha256 type="string">ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad</sha256>
      <parents type="array" />
    </version>
  </versions>
  <continuities />
  <selections />
  <readings />
  <annotations />
  <relations />
</model>
```

Readable literal text is used whenever XML 1.0 can preserve it. An individual
string containing a carriage return or an XML-incompatible character instead
uses `encoding="json-string"`. Its element text is one complete JSON string
literal, with XML escaping applied as necessary.

```xml
<content type="string" encoding="json-string">"A\r\nB\u0000"</content>
```

This field decodes to `A`, carriage return, line feed, `B`, and U+0000.
Encoding applies to that string only. Records and relationships remain
explicit XML elements. Literal carriage returns anywhere in an XML input
are rejected to avoid silent XML line-ending normalization. A character
reference such as `&#13;` in an ordinary string is also accepted and preserved.
Strings containing only spaces, tabs, or line feeds retain those characters.

XML declarations are optional. When present they must specify XML 1.0 and,
if an encoding is named, UTF-8. DTD declarations, custom entities, comments,
processing instructions, mixed content between fields, unknown types,
unknown attributes, and foreign-namespace elements are rejected. Predefined
XML escaping and valid character references remain ordinary XML syntax.
The decoder and core validator implement conformance. There is no separate
XSD, Relax NG schema, or Schematron schema.

## 4. YAML binding

YAML represents the same nested mappings and sequences as JSON. The encoder
quotes every string, including keys, and emits no anchors or aliases. Quoting
prevents values such as `null`, `true`, `01`, `yes`, and dates from changing
type under readers with different YAML scalar conventions. Escapes preserve
controls, carriage returns, and other characters requiring special spelling.

The decoder uses a restricted safe-loader contract.

- Mapping keys are unique strings. Merge-key processing is not performed.
- Implicit integers use decimal JSON notation. The null spelling is `null`.
- JSON boolean and non-integer number spellings are recognized and rejected.
  The core model has no corresponding fields.
- Other unquoted scalars are strings. In particular, YAML's legacy boolean,
  timestamp, hexadecimal, and octal conventions are not inferred.
- Explicit tags are limited to mappings, sequences, strings, decimal integers,
  and `null`. Object construction, binary data, timestamps, sets, anchors,
  aliases, and multiple documents are rejected.

YAML quotation and block-scalar choices determine the decoded string. The reference
encoder always emits the quoted form that preserves the existing model value.
The YAML dependency is PyYAML, already used by repository tools.

## 5. Validation and limits

`tests/models/test_bindings.py` runs every valid existing core case, every
valid existing editorial-profile fixture, and both standalone model examples
through all three bindings and across binding changes. Invalid model fixtures
must fail encoding. Additional cases exercise controls, carriage returns,
Unicode combining sequences, supplementary characters, whitespace-only
strings, duplicate keys, malformed structures, unsafe syntax, incorrect
references, and incorrect version hashes.

The bindings preserve profile relation records as ordinary core data. Callers
using the editorial provenance profile must separately invoke its validator
and revision operation.
Neither round-trip equality nor core validation establishes an annotation's
truth, historical derivation, the adequacy of a concept definition, TEI P5
conformance, or successful migration from an external edition.

The decoder imposes a nesting guard beyond the depth of any valid core
package, but no general document-size or resource quota. Applications accepting
large untrusted uploads must set their own resource limits. RDF reaches only
the one-way export of section 6, which carries a preservation law of its own
and no decoder. JSON-LD, database layouts, and other bindings remain separate
design work. A new format requires an explicit mapping and the same
preservation checks.

## 6. RDF export

This export runs one way. It writes a package of the entity extension 0.2 of
[[knowledge/text-model]] as RDF and reads nothing back, so no importer exists
and no round trip is claimed. Section 14.5 of the text model states the
direction of the mapping and section 13 the identifier policy and the claim
pattern, and this section fixes what those sections leave to the binding. Its
vocabulary choices are project posits. They are no official TEI P6 syntax and
record no ontology commitment of the TEI.

### 6.1 What the export is

The JSON, XML and YAML bindings of sections 2 to 4 encode one package and
decode it again under an equality law. The RDF export carries record identity,
the claim structure and every reference edge into RDF and leaves version
content and selection targets in the package.

```python
to_triples(package) -> list[tuple[str, str, str]]
to_turtle(package) -> str
describe(triples) -> dict
```

`to_triples` returns the sorted unique triples of one package. Subject,
predicate and object are terms in N-Triples lexical form, an absolute IRI in
angle brackets, a quoted literal, a literal with a datatype IRI, or a literal
with a language tag. Literal escaping follows N-Triples, and a character below
U+0020 as well as U+007F is written as an escape, so no control character
reaches the output. `to_turtle` renders the same triples with the fixed prefix
block of section 6.2, grouped by subject and sorted, so one package always
yields one byte sequence.

Both export operations validate the package with `validate_extension` and raise
`ValueError` on any error diagnostic. A warning leaves a package exportable, so
an absent or ambiguous selection and a mention without a denotation claim reach
RDF. Two further refusals belong to the identifier policy. A package without the
field `base` cannot be exported, because every record IRI is minted from the
base. A base that a reserved namespace of this binding prefixes, or that is
itself a prefix of one, is refused, because a record IRI could then collide with
a vocabulary term. Inputs are never mutated, and nothing is retrieved from the
network.

### 6.2 Prefixes and identifiers

`to_turtle` writes this prefix block unchanged in front of every export.

| Prefix | Namespace |
|---|---|
| `crm` | `http://www.cidoc-crm.org/cidoc-crm/` |
| `dcterms` | `http://purl.org/dc/terms/` |
| `oa` | `http://www.w3.org/ns/oa#` |
| `prov` | `http://www.w3.org/ns/prov#` |
| `rdf` | `http://www.w3.org/1999/02/22-rdf-syntax-ns#` |
| `rdfs` | `http://www.w3.org/2000/01/rdf-schema#` |
| `skos` | `http://www.w3.org/2004/02/skos/core#` |
| `tei6` | `urn:tei-p6-research:rdf:0.2:` |
| `xsd` | `http://www.w3.org/2001/XMLSchema#` |

`tei6` is the project namespace of this binding. It carries every field for
which sections 13 and 14.5 name no external target, and a term under it asserts
what this project's model defines and nothing beyond it. The namespace is a URN,
so no resolvable document is implied.

The record IRI of a record is the package base followed by its local ID, code
point by code point and without escaping, as section 13 requires. The package
itself is addressed by the base IRI. `to_turtle` abbreviates an IRI to a
prefixed name where a reserved namespace prefixes it and the local part is a
legal Turtle name; a record IRI is written in full. Abbreviation is lexical and
changes no IRI.

Four constructs of the model have no identity of their own and receive a derived
IRI below the record they belong to. A local ID contains no slash, so a derived
IRI is never a record IRI, and `describe` ignores it.

| Derived IRI | Node |
|---|---|
| `<selection>/selector` | the selector of a selection |
| `<selection>/selector/<n>` | the nth segment of an aggregate selector |
| `<annotation>/body` | the textual body of an annotation |
| `<name>/part/<n>` | the nth part of a name claim |
| `<statement>/participant/<n>` | the nth participant in canonical order |

Every record carries `tei6:recordKind` with the name of its collection, `nodes`
for a reading node and `package` for the package. The marker is what tells a
denotation claim from a reading node when both are an `oa:Annotation`, and it is
the first half of the preservation law of section 6.5.

### 6.3 Record kinds

Each table names the fields of one record kind and the RDF that carries them.
`recordKind` is omitted from the tables and present on every record.

#### Package and identity records

| `package` | RDF |
|---|---|
| the base | subject of the record, typed `tei6:Package` |
| `model_version` | `tei6:modelVersion` |
| binding version | `tei6:bindingVersion` |

| `agents` | RDF |
|---|---|
| record | typed `prov:Agent` |
| `label` | `rdfs:label` |
| `alignments` | as in the alignment table below |

| `concepts` | RDF |
|---|---|
| record | typed `skos:Concept` |
| `label` | `skos:prefLabel` |
| `definition` | `skos:definition` |
| `applies_to` | `tei6:conceptRole` |
| `alignments` | as in the alignment table below |

| `texts` | RDF |
|---|---|
| record | typed `tei6:Text` |
| `label` | `rdfs:label` |

| `versions` | RDF |
|---|---|
| record | typed `tei6:Version`, and the `oa:hasSource` target of every selection on it |
| `sha256` | `tei6:contentHash` |
| `parents` | `tei6:versionParent` per parent |
| `content` | outside the export |

| `entities` | RDF |
|---|---|
| record | typed by `kind`, `person` as `crm:E21_Person`, `group` as `crm:E74_Group`, `place` as `crm:E53_Place`, `event` as `crm:E5_Event`, `object` as `crm:E22_Human-Made_Object`, `other` as `crm:E1_CRM_Entity` |
| `label` | `rdfs:label` |
| `kind` | `tei6:entityKind`, because the class assertion above is already a statement and the constitutive kind is part of the identity |
| `alignments` | as in the alignment table below |

#### Selection and occurrence records

| `selections` | RDF |
|---|---|
| record | typed `oa:SpecificResource` |
| `version` | `oa:hasSource` |
| `selector` | `oa:hasSelector` to the derived selector node |
| resolution status | `tei6:resolutionStatus` with `resolved`, `absent` or `ambiguous` |
| unresolved candidates | `tei6:unresolvedCandidates` with the number of candidates, present only for an ambiguous selection |

| Selector | RDF on the selector node |
|---|---|
| `point` | `oa:TextPositionSelector` whose `oa:start` and `oa:end` are the offset |
| `ranges` with one segment | `oa:TextPositionSelector` with `oa:start`, `oa:end` and `tei6:segmentQuote` |
| `ranges` with several segments | `oa:List` with one `oa:items` per segment, each segment a position selector with `tei6:segmentIndex`, so the order of the one aggregate target survives without an RDF collection |
| `quote` | `oa:TextQuoteSelector` with `oa:exact` and, where present, `oa:prefix` and `oa:suffix`, plus `tei6:matchPolicy` |

| `readings` | RDF |
|---|---|
| record | typed `oa:Annotation` with `oa:motivatedBy oa:classifying` |
| `version` | `oa:hasTarget` |
| `label` | `rdfs:label` |
| claim fields | as in section 6.4 |

| `nodes` | RDF |
|---|---|
| record | typed `oa:Annotation` with `oa:motivatedBy oa:classifying` |
| `type` | `oa:hasBody` to the concept |
| `selection` | `oa:hasTarget` |
| `parent` | `tei6:nodeParent`, absent for a root node |
| containment | `tei6:inReading` to the reading that holds the node |

| `annotations` | RDF |
|---|---|
| record | typed `oa:Annotation` |
| `selection` | `oa:hasTarget` |
| `body` | `oa:hasBody` to the derived body node, typed `oa:TextualBody` with `rdf:value` |
| `concept` | `oa:hasBody` to the concept and `oa:motivatedBy oa:classifying`, both present only with the field |
| claim fields | as in section 6.4 |

#### Claim records

| `continuities` | RDF |
|---|---|
| record | typed `tei6:ContinuityClaim` |
| `text` | `tei6:subject` |
| `versions` | `tei6:continuityVersion` per version |
| `criterion` | `tei6:criterion` |
| claim fields | as in section 6.4 |

| `relations` | RDF |
|---|---|
| record | typed `crm:E13_Attribute_Assignment` |
| `source` | `crm:P140_assigned_attribute_to` |
| `target` | `crm:P141_assigned` |
| `type` | `crm:P177_assigned_property_of_type` |
| claim fields | as in section 6.4 |

| `names` | RDF |
|---|---|
| record | typed `crm:E41_Appellation` |
| `entity` | `tei6:subject`, and `crm:P1_is_identified_by` from the entity to the name claim |
| `form` and `language` | one `rdfs:label` literal with the language tag |
| `parts` | `tei6:hasNamePart` per part, each part node with `tei6:namePartKind`, `tei6:namePartForm` and `tei6:namePartIndex` |
| claim fields | as in section 6.4 |

| `denotations` | RDF |
|---|---|
| record | typed `oa:Annotation` with `oa:motivatedBy oa:identifying` |
| `mention` | `oa:hasTarget` |
| `entity` | `oa:hasBody` |
| claim fields | as in section 6.4 |

| `statements` | RDF |
|---|---|
| record | typed `crm:E13_Attribute_Assignment` |
| `kind` | `tei6:statementKind` |
| `type` | `crm:P177_assigned_property_of_type` |
| `participants` | `crm:P140_assigned_attribute_to` per participant entity, and one `tei6:hasParticipant` per pair, whose node carries `tei6:participantEntity` and `tei6:participantRole` |
| `value` | `crm:P141_assigned` |
| claim fields | as in section 6.4 |

| `alignments` | RDF |
|---|---|
| record | typed `tei6:AlignmentClaim` |
| carrier | `tei6:subject`, and the mapping triple on the carrier, `exact` as `skos:exactMatch`, `close` as `skos:closeMatch`, `broader` as `skos:broadMatch`, `narrower` as `skos:narrowMatch` |
| `relation` | `tei6:alignmentRelation` |
| `iri` | `tei6:alignmentTarget` |
| claim fields | as in section 6.4 |

| `former_bases` | RDF |
|---|---|
| record | typed `tei6:FormerBaseClaim` |
| the package as subject | `tei6:subject` to the base IRI |
| `base` | `tei6:formerBase`, and `prov:alternateOf` from the former IRI of every record to its current record IRI |
| claim fields | as in section 6.4 |

Section 14.5 also names `crm:E5_Event` for a statement of kind `event` and
`crm:P4_has_time-span` for a validity scope. The export writes neither, because
an event class on the assignment node would conflate the claim with the thing
claimed and a time span would need a node whose only content is the two bounds.
Both stay available to a consumer that adds them.

### 6.4 Claim fields

Every claim of every kind, the four v0.1 kinds included, carries the section 13
pattern on its own node. A plain mapping triple beside it, such as
`skos:exactMatch` on an aligned entity or `crm:P1_is_identified_by` on a named
entity, drops all of it, which is why the claim node exists.

| Field | RDF | Note |
|---|---|---|
| `id` | the record IRI | the node every other field hangs on |
| `agent` | `dcterms:creator` | one attribution predicate for every claim kind; `prov:wasAttributedTo` and `crm:P14_carried_out_by` are alternatives this binding does not write |
| `created` | `prov:generatedAtTime` typed `xsd:dateTime` | transaction time |
| `status` | `tei6:status` | no external target; CRMinf belief values are a candidate |
| `certainty` | `tei6:certainty` | the claiming agent's own qualification |
| `valid` | `tei6:validFrom` and `tei6:validUntil` as plain literals | the model's three date precisions survive as written and commit to no xsd date type |
| `supersedes` | `prov:wasRevisionOf` per entry | currency follows this structure alone |

An absent optional field emits no triple, so `tei6:status` is missing where a
v0.1 claim declares none, and section 13 reads such a claim as `asserted`.

### 6.5 Preservation law

A round trip is out of scope. What the export must hold is identity and
structure, expressed through one projection over the triples. `describe` reads
the record-kind markers and the designated edge predicates, and it returns the
record IRIs by kind together with every reference edge as a triple of source
IRI, model field name and target IRI. An edge is read only where both ends carry
a record kind, so a derived node and an external alignment IRI stay out of it.

```text
describe(to_triples(p)) = projection(p)
```

The right side is the same projection taken directly from the package, the
record IRIs of each collection and every reference field of every record
including the subject fields of section 13, the participant entities of a
statement, the containment of a reading node and the entries of `supersedes`.
The law holds for every case package of the entity extension that the 0.2
validator accepts, with a test base supplied where a case declares none, and for
both standalone examples.

Each reference field is carried by exactly one predicate per record kind. Where
a vocabulary predicate repeats an edge, as `crm:P1_is_identified_by` repeats the
subject of a name claim and `crm:P140_assigned_attribute_to` repeats the
participants of a statement, `describe` reads the designated predicate and
ignores the repetition.

`tests/models/test_rdf_binding.py` derives the package side of the law from the
record contract rather than from the export's own table, so one mistake in that
table cannot make the comparison pass. The suite further holds determinism, the
two refusals, language-tagged name forms with ordered parts, several alignments
of one entity, a superseded claim, the alias triples of a former base, and a
minimal syntax check of the Turtle over hostile strings, balanced statements,
absolute IRIs and escaped control characters.

### 6.6 Limits

The export asserts no inference. It runs no reasoner, publishes no SHACL shape,
no OWL ontology and no RDFS schema, and validates nothing about an external
resource. Two alignments of one entity to one IRI stay two claims, and an
entity's alignment reaches none of its mentions. Every entailment a consumer
draws from PROV, SKOS, CIDOC CRM or the Web Annotation vocabulary is the
consumer's.

Three choices that sections 13 and 14.5 leave open are settled here.

1. One IRI per record. A CRM class and an `rdfs:label` are written on the record
   IRI, which lets a consumer read it as the thing the record is about, while
   the claim nodes take the same IRI as the record they are claims about.
   Section 11 keeps the record and the thing apart, and the export offers no
   second IRI for the record as an object of discourse.
2. An `exact` alignment is `skos:exactMatch`. The export never writes
   `owl:sameAs`, so no identity entailment enters RDF, and a consumer that needs
   identity states it under its own responsibility.
3. A former base yields `prov:alternateOf`, which presents two IRIs as aspects
   of one thing without entailing that the two packages are the same package.

What has no external target and therefore lives under `tei6:` is the record kind
of every record, the constitutive kind of an entity, the role of a concept, the
discriminator of a statement, the role string of a participant, the criterion of
a continuity claim, the content hash and the technical parents of a version, the
match policy and the resolution of a selection, the order of name parts, the
containment and parent of a reading node, and the fields `status`, `certainty`
and `valid` of every claim. Whole record kinds with no external class are the
package, texts, versions, continuity claims, alignment claims and former-base
claims.

Version content is not exported. A consumer receives the SHA-256 of the content
and the quote of every range segment, and it cannot reconstruct the text of a
version from the triples. Selection resolution is exported as a status and, for
an ambiguous selection, the number of candidates; the resolved targets
themselves stay in the package, because resolution computes them from the
version content that the export omits. Section 13 names `oa:Independents` as a
candidate for a quote selector that yields separate targets, and the export
writes the match policy instead, because the plurality is a fact of resolution
and belongs to no field of the selection record.

`prov:generatedAtTime` is typed `xsd:dateTime`. RFC 3339 admits second 60 and
the value space of `xsd:dateTime` excludes it, so a claim dated on a leap second
produces an ill-typed literal. The model keeps the leap second, and a consumer
that rejects it must say so.

The section 12 conformance contract of the model asks a binding for a loss
matrix and a loss report. This section names what is dropped in prose and
leaves the matrix and the report to the same work that specifies the P5
projection.

### 6.7 Run and inspect

```powershell
python -m pytest tests/models/test_rdf_binding.py -q
python -c "import json; from tools.models.rdf_binding import to_turtle; print(to_turtle(json.load(open('experiments/entities_v02/examples/statements-and-revision.json', encoding='utf-8'))))"
```

The two Turtle files beside the JSON examples in
`experiments/entities_v02/examples/` are exports of those packages. They
regenerate with `to_turtle` over the matching JSON file, and the test suite
compares the committed bytes with a fresh export, so a change to the mapping
fails the suite until the examples are regenerated intentionally.

### 6.8 Human acceptance

Review each item with a separate **accept / revise / defer** decision and an
example or reason, as section 14.6 does for the extension itself. These are
editorial decisions, and none of them approves source truth.

1. Does one IRI per record, read as the thing the record is about, serve the
   consuming projects, or does the export owe a second IRI for the record?
2. Is `skos:exactMatch` without `owl:sameAs` the right reading of an `exact`
   alignment for the intended reuse, and which consumer expects the identity
   entailment?
3. Does a claim node with agent, instant, status, certainty, validity and
   revision carry a disagreement usefully into RDF, or do consuming projects
   expect RDF-star or named graphs in its place?
4. Are the fields under `tei6:` the ones a consumer actually needs, and which of
   them should instead map to an established vocabulary before the export is
   offered outside this project?
