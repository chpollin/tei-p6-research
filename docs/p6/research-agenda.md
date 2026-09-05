# P6 research agenda

This independent question map defines the research needed to justify a P6
candidate. Current work and blockers belong in `knowledge/state.md`.

## From text concepts, practice, and P5 to requirements

The model's scope must name the text forms and tasks it intends to cover.
It need not provide an ontology of every subject discussed in a text. P5
supplies the baseline and migration obligations. Textual scholarship,
alternative models, and editorial practice challenge the proposed categories.

The project must establish which P5 distinctions are conceptual, which are
serialization-driven, which arise from compatibility or governance, and which
are merely conventional. It must also distinguish demonstrated friction from
isolated preference and identify successful P5 patterns that a redesign must
preserve.

Resolution requires the pinned ODD model, prose Guidelines, representative
customizations, issue and decision trails, processing evidence, teaching
experience, and real examples. The output distinguishes requirements derived
from grounded findings from proposed project requirements, and gives
counterexamples for both. A conceptual question need not first be framed as a
P5 defect.

## Core-model questions

The core comparison must answer these questions.

- Which primitives for text, structure, annotation, identity, relation, order,
  and constraint are justified by the declared tasks and counterexamples?
- How does a typed ordered graph compare with a primary tree plus references
  and annotations? Do particular cases require regions, events, or other
  primitives, and what would justify treating them as primitive?
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

Compare whether each binding preserves the required distinctions in tools and
real workflows. XML, JSON-LD, RDF, and YAML form the initial contrast set.
Additional syntaxes require a concrete use case.

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

Define that relation independently of a converter or canonical form, using
expected observations and equal/unequal example pairs reviewed in advance.
Only then test whether canonicalization implements it. Distinguish preservation
of all model distinctions, equivalence for a declared task, and byte identity.
They answer different questions.

## Migration questions

The migration study must record coverage, model preservation, lexical changes,
policy or tool dependencies, and reversibility separately. An equivalent result
may still require normalization and editorial policy. The study must cover documents,
ODDs, schemas, processors, identifiers,
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

## Required decision evidence

Each decision needs grounded premises, a reproducible example or prototype,
and a comparison of alternatives and migration consequences. Requirements and
recommendations that express the project's judgment remain explicit posits.
A bounded pilot may justify another experiment while leaving an architecture
recommendation open.

## Next bounded research packages

These packages define work and acceptance criteria. Before delegation, name
the base commit, exclusive write paths, read-only inputs, required checks, and
gaps to report. The integrator owns shared contracts and state.

### A. Text identity requirements

Select a bounded set of text-theoretical, annotation-model, and editorial
practice sources. Record why each can illuminate textual continuity, version,
target, or interpretation. Admit and distill each source separately. Synthesize
only through assertions. Derive a requirement set that distinguishes source
findings from project choices, with an adverse example for each requirement.

Acceptance requires at least two conceptual alternatives to face the same
independently reviewed observations. Explain where each distinguishes text, version,
occurrence, selector, resolved target, and attributed interpretation, and where
it deliberately leaves a question open. Two selectors inside one object model
do not satisfy this comparison. A missing source or unsupported generalization
is reported as a gap.

### B. Real editorial cases

Select three bounded case packages from distinct editorial contexts, together
covering hierarchy, overlap, and customization or contextual interpretation.
Record the selection unit, inclusion and exclusion rules, source versions,
rights, authority, relevant ODD and tool context, and known sampling bias.
State required editorial observations before writing candidate encodings.
Reserve an adverse case for testing after the candidates have been defined.

Acceptance requires reproduction from declared inputs, independent domain
review of the expected distinctions, and explicit coverage gaps. Three
purposefully selected cases support comparison within their scope. They cannot
establish prevalence, general migratability, or universal coverage.
New executable artifact types require a recorded contract before implementation.

### C. One comparative workflow decision

Use annotation review after a text edit as the first decision-sized task.
Compare repair within P5 tooling, compatible evolution, an alternative abstract
model, and retaining or deferring the current behavior. Hold the editorial task
and expected observations fixed. Specify participant roles, procedure, baseline,
and acceptance criteria before measuring correctness, effort, errors, and
interventions. Report migration on the independent axes above.

Acceptance requires technical and domain reviews of the same record, with
costs and unknowns alongside benefits. The recommendation must name evidence
that would reverse it. Its scope may be limited to another bounded prototype.
