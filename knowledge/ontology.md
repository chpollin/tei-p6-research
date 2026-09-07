---
title: Ontology
project:
  name: "TEI P6 Research"
  repository: "tei-p6-research"
method:
  name: Promptotyping
  url: https://dhcraft.org/Promptotyping/
status: draft
language: en
created: "2026-09-07"
updated: "2026-09-07"
related: [model-design, model-examples, text-model, architecture, testing, state]
---

# Ontology

The experimental ontology defines documentary records used to describe texts
and their interpretation. Its purpose is to make class meanings, subclass
edges and reference relationships inspectable in a machine-readable artifact.
It formalizes a selected part of [[knowledge/model-design]]. It introduces no
version 0.3 package contract and does not alter the executable 0.1/0.2 models.

## Identity and interpretation boundary

A `ReferentRecord` identifies a referential intention within a description.
The record can be used to discuss a person, an unidentified place or a
narrative object. It is an information record with a documentary identity.
Its IRI is never silently reused for an externally identified person or place.
The expected referent type is a revisable description. It is not a reason to
make the record a subclass instance of an external Person or Place class.

Every predicate definition specifies how its subject and object are read.
`record` concerns the identified record, `referent` the object described by
a referent record, `concept` a defined vocabulary value, and `proposition`
a recorded content. A proposed name assignment therefore concerns the
referent of its subject handle and the form described by its object record.
An unfamiliar predicate has no licensed external interpretation.

An IRI does not by itself establish physical existence. The relevant questions
are what a class or property means, which axioms apply and what context an
assertion has. Context-qualified interpretation is carried as structured
content and a separate stance, rather than materialized as an unqualified
world statement.

## Classes and hierarchy

The class vocabulary has one documentary root, `Record`. Text, representation,
selection, name form, referent, context, responsibility, vocabulary, structure,
proposition and claim records have different identity or processing contracts.
`MentionRecord` specializes `AnnotationRecord`. Concept and predicate records
specialize `VocabularyRecord`; structural reading and node records specialize
`StructureRecord`. `Package` groups exchanged records and is separate from a
`CollectionRecord` describing a corpus or another collection.

`SelectionRecord` is the generic documentary selection. The subclass
`TextRangeSelectionRecord` specifies a contiguous Unicode interval; other
coordinate and resolution contracts can specialize the general class. This
experiment leaves the richer implemented 0.1 selectors intact.

The complete generated hierarchy is [record-hierarchy.mmd](../ontology/record-hierarchy.mmd).
The proposed domain hierarchy in [[knowledge/model-design]] classifies what
records can describe. Its edges are not asserted between these Record classes.
Organization activity, name-use type and historical or narrative qualification
remain extensible classifications and claim context.

## Claims and propositions

A `PropositionRecord` records a structured content with its interpretation
context. A `ClaimRecord` records an agent's stance toward that content.
Assertion, reporting, questioning and denial are distinct stances. Withdrawing
a claim describes its lifecycle and is not denial of its content. An annotation
selects a target and can refer to the relevant proposition or claim.

A compact authoring form may put proposition fields inside a claim. Its
expansion creates an explicitly identified proposition while retaining the
agent, context, stance and source references. Reusing an identical proposition
record supports several attitudes to the same specified content. It does not
prove semantic equivalence between differently formulated contents.

The example envelope's source selection documents proposition content.
Individual grounds for different stances need separate claim-level source
support. The ontology vocabulary does not yet supply a full evidence, temporal
uncertainty or nested-source-report profile.

## External alignment policy

`alignment-candidates.ttl` is a separate register of local term, external
target, comparison relation, source URL and rationale. Its relations are
annotations used to guide review. Candidate mappings add no subclass,
equivalence, identity or import axioms. Target definitions must be inspected
before activating a mapping, including domain, range, identity, time and
contextual commitments.

The external target is a term IRI where a particular term has been selected.
An ontology-level comparison can instead point to the documented ontology
repository, explicitly labeled as such. This avoids inventing a class mapping
before its module and version have been chosen. Register entries remain
`candidate` even when their rationale rejects a direct classification.

The distinction between axioms and input requirements follows the
[OWL 2 Primer](https://www.w3.org/TR/owl2-primer/). OWL domain and range
statements classify resources through inference; they do not check that a
required field appears in an input file. The core uses them only for its
documentary classes. Closed input checks and full logical consistency would
require separate, explicitly scoped validation or reasoning contracts.

Foundational ontologies such as BFO and DOLCE address different decisions from
domain and application vocabularies such as CIDOC CRM, LRMoo, RiC-O, SKOS,
PROV-O and Web Annotation. Connecting all of them is not an acceptance goal.
A later bridge must name a specific task and version, state its formal
consequences and pass positive and adverse cases before it is adopted.

## Artifact and generation contract

| Artifact | Authority and role |
|---|---|
| `ontology/core.ttl` | Hand-authored draft class and property definitions in the local namespace `https://example.org/tei-p6-research/ontology/`. |
| `ontology/alignment-candidates.ttl` | Hand-authored, non-entailing comparison register with primary-source pointers. |
| `ontology/core.rdf`, `ontology/core.jsonld` | Generated RDF/XML and JSON-LD views of exactly the core RDF graph. These are RDF serializations, not TEI XML and plain model JSON bindings. |
| `ontology/record-hierarchy.mmd` | Generated Mermaid subclass hierarchy of the core. It contains class edges only. |
| `tools/check_ontology.py`, `tests/test_check_ontology.py` | Limited parsing, structural policy and reproduction checks. No general OWL reasoner or complete SHACL validation. |

These artifacts are project design outputs outside the evidence chain. They
cannot ground a historical finding, a P5 fact or an official P6 statement.
Examples remain in [[knowledge/model-examples]] and retain their explicitly
illustrative syntax. No converter between that envelope and this ontology is
claimed unless separately implemented and checked.

The [HSA letter case](../experiments/hsa_letter_4493/README.md) is a separate
instance experiment using this core directly. Its own case vocabulary defines
source locations, import-report support and preservation of P5 structure.
The maintained contract is [[knowledge/hsa-profile]], including its
separate semantic and preservation components.
Its plain XML and JSON views are bindings of the case records; `p6.ttl` is
their RDF graph. This bounded source-report relation supplies no general
claim-evidence profile. Byte-preserved P5 and interpreted records have separate
coverage contracts.

Regenerate and check the machine-readable views with:

```powershell
python tools/check_ontology.py
python tools/check_ontology.py --check
python -m pytest tests/test_check_ontology.py -q
```

The check parses local files without fetching imports, compares the three RDF
graphs and regenerates the hierarchy. It checks labels, definitions, declared
local references, absence of foreign class inheritance and unsupported import
or equivalence axioms, acyclic subclass edges and mapping-register completeness.
These checks establish the declared structural policy. They do not prove a
complete OWL profile, global logical consistency or adequacy for TEI practice.
