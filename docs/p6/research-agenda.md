# P6 research agenda

Status: stable question map
Authority: independent project planning document

This document identifies the questions that must be answered before a formal
P6 design candidate can be justified. It does not track progress; current work,
owners, and blockers belong in `knowledge/state.md`.

## From P5 to requirements

The project must establish which P5 distinctions are conceptual, which are
serialization-driven, which arise from compatibility or governance, and which
are merely conventional. It must also distinguish demonstrated friction from
isolated preference and identify successful P5 patterns that a redesign must
preserve.

Resolution requires the pinned ODD model, prose Guidelines, representative
customizations, issue and decision trails, processing evidence, teaching
experience, and real examples. The output is a grounded requirement and
counterexample set, not a list of complaints.

## Core-model questions

The candidate model must answer:

- What are the irreducible primitives for text, structure, annotation,
  identity, relation, order, and constraint?
- Is a typed ordered graph sufficient, or are hyperedges, regions, events, or
  other primitives required?
- How are mixed content and multiple hierarchies represented without privileging
  one syntax?
- How are spans anchored, and how do anchors behave under editing and version
  change?
- Which distinctions belong to the shared core, to a domain model, to a
  blueprint, or only to a serialization binding?
- Which semantics are closed-world constraints and which permit open-world
  extension?

Resolution requires formal sketches, executable prototypes, counterexamples,
and comparison against representative P5 modules.

## Blueprint and customization questions

The design must determine whether blueprints are subsets, compositions,
profiles, inheritance structures, transformations, or a combination of these.
It needs deterministic rules for selection, restriction, extension, conflict,
defaults, aliases, version dependencies, and local vocabulary.

The critical test is whether independent customizations can exchange data under
a meaningful shared contract. A formally valid customization that destroys
interoperability without declaring it is not a successful customization model.

## Serialization questions

For each proposed binding, the project must establish how it represents order,
mixed content, identity, references, language, datatypes, spans, multiple
hierarchies, inferred values, and package context. It must decide which
roundtrips are lossless, which preserve only declared semantics, and which are
intentional projections.

The central comparison is not “XML versus JSON.” It is whether the abstract
model and binding contracts preserve the required distinctions in tools and
real workflows. XML, JSON-LD, RDF, and YAML form the initial contrast set;
additional syntaxes require a concrete use case.

## Validation questions

The project must decide which invariants are expressible in generated native
schemas and which require a shared rule engine. Diagnostics need stable IDs,
locations, severity, explanation, and the responsible model or blueprint rule.

Validation must also cover the model definition itself, blueprint composition,
instances, external references, conversion loss, and cross-binding equivalence.
The limits of schema validation, semantic graph validation, and processor
behavior must be documented explicitly.

## Equivalence and canonicalization questions

A canonical comparison form must preserve every normative semantic distinction
while ignoring differences declared non-semantic by a binding. The project must
therefore decide how to canonicalize order, identifiers, datatypes, language,
defaults, whitespace, Unicode, blank nodes, namespace aliases, and external
references.

Two representations may be equivalent for one blueprint and not for another.
Equivalence must always name its model, blueprint, binding versions, and
comparison class.

## Migration questions

The migration study must determine which P5 documents and customizations map
exactly, which require normalization or policy, and which cannot be represented
without loss. It must cover documents, ODDs, schemas, processors, identifiers,
stylesheets, APIs, training material, and institutional workflows.

Migration quality is measured through representative corpora and explicit loss
reports. A converter that handles only clean TEI All examples cannot establish
general migratability.

## Implementation questions

Candidate metamodeling technologies must be evaluated rather than selected by
familiarity. The comparison should include support for ordered mixed content,
graphs, context-sensitive constraints, schema generation, versioning,
diagnostics, extensibility, and long-term implementation independence.

A prototype may use LinkML, UML-like models, JSON Schema, SHACL, ShEx,
Schematron, or a custom intermediate representation, but the normative semantics
must remain describable independently of a single tool.

## Human and governance questions

The project must investigate whether the model can be taught at progressive
levels, inspected without specialist tooling, localized, and used by
communities with different technical resources. It must also define ownership
and review of the core, blueprints, bindings, identifiers, deprecations, test
suites, and compatibility policies.

A formally elegant architecture that cannot be governed, implemented, or
adopted is not an optimized standard.

## Required decision evidence

Each resolved question should leave three connected results: grounded findings
about P5 and stakeholder needs, a reproducible example or prototype, and a
comparative decision record with alternatives and migration consequences.
Only then can the result be promoted into the final design specification.
