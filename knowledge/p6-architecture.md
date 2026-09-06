---
title: P6 Architecture
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
related: [text-model, text-model-bindings, p6-evaluation, experiments, design, plan, state]
---

# P6 Architecture

This document holds the candidate architecture around the
[[knowledge/text-model|text model]]. It states how shared models can be
selected, constrained and extended, how identifiers, releases, compatibility
and decisions evolve, and how examples and migration make P5 and candidate
comparisons executable. Everything here is an independent project proposal.
It does not represent TEI Consortium policy or an official TEI decision.

## Candidate architecture

The design work asks how a next-generation TEI model could be made
conceptually clearer, formally testable, serialization-independent,
customizable, and migratable without presuming that a complete redesign is
the correct answer.

```text
P5 + text theory + editorial practice
          |
          v
requirements and counterexamples
          |
          v
serialization-independent core model
          |
          +--> blueprint/customization
          |          |
          |          v
          +--> normative serialization bindings
                         |
                         v
              validators and converters
                         |
                         v
        examples + migration + roundtrip tests
                         |
                         v
              comparative evaluation
```

This flow sketches one candidate: a semantic core with customization rules,
normative bindings, invariants, conformance levels, diagnostic behavior, and an
executable test suite. The need for each component, its boundary, and competing
arrangements remain questions for comparative evaluation. Neither this diagram
nor a successful selector pilot settles the architecture.

## Blueprints and customization

Customization is central to TEI rather than an optional post-processing step.
A P6 architecture must allow communities and projects to create narrower,
clearer contracts while retaining an intelligible relationship to shared
concepts and to one another. This candidate design contract elaborates the
principle
[keep customization compositional](p6-evaluation.md#keep-customization-compositional).

### Candidate layers

```text
metamodel
    -> shared domain model
        -> blueprint
            -> project customization
                -> instance declaration
```

The metamodel defines the available modeling mechanisms. A shared domain model
defines concepts and their intended semantics. A blueprint selects and
organizes a coherent contract for a domain or document family. A project
customization restricts or extends a declared blueprint. An instance names the
exact model, blueprint, customization, and binding versions against which it
claims conformance. The four modeling levels of the text model's wider sketch
name the same stack without the project customization step
([text model, section 11](text-model.md#four-modeling-levels)).

### Blueprint responsibilities

A blueprint may select concepts, properties, relations, hierarchies, content
patterns, and constraints. It may define required entry points, default
processing expectations, permitted extension points, and supported binding
profiles. It should be usable without importing unrelated domain complexity.

A blueprint is not merely a list of elements. It is a versioned behavioral
contract that states what its instances mean, which invariants apply, and what
other systems may rely on.

### Customization operations

The candidate algebra distinguishes explicit operations:

| Operation | Effect |
|---|---|
| select | include a shared concept or rule without changing it |
| restrict | narrow cardinality, values, content, or permitted relations |
| extend | add a locally identified concept, property, relation, or constraint |
| specialize | derive a more specific concept while preserving its declared parent relation |
| bind | associate a concept with a controlled vocabulary, datatype, or external authority |
| alias | provide a local label without changing canonical identity |
| deprecate | discourage a construct under an explicit replacement and version policy |
| compose | combine compatible blueprints or customization modules under conflict rules |

Whether a particular operation is allowed depends on the invariant being
modified. Core invariants may be non-overridable; blueprint rules may declare
controlled variation points; local additions must use stable identities and
must not impersonate shared concepts.

### Composition and conflict

Composition must be deterministic. The result records its inputs, order or
precedence where relevant, resolved conflicts, unresolved conflicts, and the
origin of every effective rule. Two incompatible cardinalities or content
requirements cannot silently collapse into whichever one a processor happens
to load last.

Deterministic composition establishes which rules apply; it does not establish
that any instance can satisfy them. Distinguish dependency validity, resolved
rule conflicts, and satisfiability. For each supported constraint language,
state which checks are decidable, which use bounded examples, and which remain
unresolved. Diagnostics identify the contributing rules and must not report an
unresolved satisfiability question as a proven valid composition.

For example, requiring exactly one value while intersecting the disjoint
allowed sets `{x}` and `{y}` admits no valid instance. A defined merge order
does not resolve this problem unless its policy explicitly changes a rule.

### Context-sensitive rules

The same concept may have different permitted structures in different declared
contexts. Such variation should be modeled as a scoped constraint with a stable
identity. Scope may refer to a named hierarchy, containing concept, relation,
blueprint, or processing mode.

Context sensitivity must not alter the core meaning of a concept invisibly. If
the semantics differ, the model should consider distinct concepts or an
explicit specialization rather than relying only on position.

### Interoperability contract

Every customization publishes its base, version dependencies, selected
concepts, restrictions, extensions, aliases, binding profiles, and conformance
claim. These declarations support comparison of shared declarations and
detected conflicts. A common vocabulary alone does not guarantee that
instances satisfy both customizations or that processors interpret them alike.

Interoperability may occur at several levels: common core, common blueprint,
exact customization, or explicit projection. Exchange claims must name the
level instead of using “TEI conformant” as an undifferentiated label.

### Validation and generation

A valid customization must pass metamodel validation, dependency resolution,
composition checks, invariant checks, and binding-generation checks. Generated
schemas and documentation are derived artifacts and retain links to the model
objects and constraints from which they were produced.

An instance validator should report the model stack it used and the origin of
each failing rule. Reproducibility requires immutable version identifiers or
content hashes for every dependency.

### Open design choices

The project has not decided whether blueprints should use inheritance,
declarative set operations, transformations, package composition, or a hybrid.
Nor has it decided how closely their behavior should correspond to existing ODD
customizations. These choices require extraction of real P5 customization
patterns, conflict examples, generated-schema comparison, and migration tests.

## Versioning and governance

A formal model remains interoperable only if its identifiers, changes,
bindings, and compatibility claims can be governed over time. This candidate
policy model defines the policy questions that P6 candidates must answer; it
does not assign authority on behalf of the TEI Consortium. It elaborates the
principle
[design for evolution and governance](p6-evaluation.md#design-for-evolution-and-governance).

### Governed objects

Governance applies independently to the metamodel, shared domain concepts,
blueprints, constraints, serialization bindings, migration rules, diagnostic
codes, examples, and conformance tests. A release identifies a coherent set of
compatible versions rather than assuming that all components always change
together.

Distinguish the persistent identifier of a governed object from the immutable
identifier of a particular definition. An instance's dependency context must
make the applicable definition recoverable. Governed definitions name their
owner, dependencies, change history, and replacement relations where applicable.

A wording change counts as editorial only when interpretation, validation, and
processing consequences remain unchanged. A semantic change requires an
explicit decision whether it revises the same concept or introduces a distinct
concept, with relations to earlier definitions and consequences for existing
data. A content hash identifies a definition's bytes, not the correctness of
that semantic decision.

### Change classes

| Change | Compatibility question |
|---|---|
| editorial | Does meaning, validation, or processing remain unchanged? |
| additive | Can existing conformant instances and processors ignore or adopt the addition safely? |
| restrictive | Which previously valid instances become invalid? |
| semantic | Does an existing identifier acquire a different meaning or processing expectation? |
| structural | Does containment, order, relation, or serialization mapping change? |
| removal | What replacement and migration path exists? |
| binding-only | Does the abstract model remain stable while a serialization representation changes? |

Versioning policy must define compatibility for documents, models,
customizations, validators, converters, and processors separately. One version
number cannot make all of those guarantees implicit.

### Compatibility declarations

A release should publish machine-readable compatibility statements describing
which earlier model and binding versions it accepts, which it can migrate,
which require a compatibility mode, and which are unsupported. Compatibility
may be syntactic, model-level, semantic, processing-level, or ecosystem-level;
the declaration names the kind.

Backward compatibility is a design variable rather than an automatic absolute.
An incompatible change may be justified, but its affected constructs, evidence,
migration, diagnostics, and adoption costs must be explicit.

### Deprecation lifecycle

Deprecation is a staged contract: proposal, decision, warning period,
replacement availability, migration support, and possible removal. The policy
must state which stage changes validation behavior and how long identifiers and
documentation remain resolvable.

A deprecated construct retains its historical meaning. Reusing the identifier
for a different concept would corrupt versioned interpretation and should be
prohibited.

### Decision record

A material change should connect:

```text
grounded problem or requirement
    -> alternatives and counterevidence
        -> prototype and migration results
            -> governance decision
                -> merged implementation
                    -> released package
```

These states are independently observable. Discussion does not imply decision;
decision does not imply implementation; implementation does not imply release.
A release manifest points to the evidence for each transition.

### Conformance-suite governance

Normative tests are governed artifacts. Each test names the model, blueprint,
binding, and requirement it exercises. Adding or changing a test may change
effective conformance even if prose is untouched, so test-suite versions and
their relation to releases must be explicit.

Disputed tests require a review path and may not be silently weakened to make an
implementation pass. Errata distinguish a mistaken test from a changed
requirement.

### Extension governance

Local and community extensions need collision-resistant identifiers and
declared ownership. A pathway may promote a widely used extension into a shared
domain model, but promotion requires semantic review, migration guidance, and a
mapping from the earlier identifier. Central adoption must not erase the origin
or silently redefine deployed data.

### Adoption and transition

A candidate release needs more than schemas: documentation, teaching examples,
reference validators, converters, compatibility guidance, implementation
reports, and a transition window. Governance should make it possible for P5 and
P6 ecosystems to coexist while projects evaluate migration.

The research project evaluates such policies comparatively. Its recommendation
remains a reasoned posit. If an official body adopts a policy, that separate
event may be reported through grounded process records; adoption neither makes
the research reasoning a source fact nor supplies human verification of it.

## Examples and migration

Examples specify the tasks used to derive requirements, compare models, and
test P5 migration. This experimental design contract elaborates the principle
[treat migration as part of the design](p6-evaluation.md#treat-migration-as-part-of-the-design).

### Example unit

Each case identifies a task, the distinctions that must survive it, and the
P5 and candidate representations under comparison. Claims of a P5 defect need
grounding. A design question may begin as a posit. Encoding complexity alone
does not establish a defect.

Record the editorial distinctions and observable task outcomes that a case
must preserve before producing candidate encodings. Obtain domain review of
these expectations independently of converter output. Synthetic cases isolate
assumptions. Cases taken from practice also require source provenance and a
declared selection protocol.

### Selection and coverage

The inventory scope is every module of the pinned P5 baseline. It provides a
finite starting point for locating declarations and their dependencies, not a
finished taxonomy of textual phenomena. Read effective constraints, Guidelines
prose, examples, and project customizations before deriving a requirement from
a declaration. Issues and literature can introduce requirements or challenge
the interpretation, but do not themselves prove current P5 behavior.

A case records module and specification references separately from document
or text type, transmission or media form, and phenomenon. For example, letter,
manuscript, and uncertain correction describe different dimensions of a
proposed case. None is interchangeable with a model entity. Several modules
may contribute to one case, and one phenomenon may recur across many document
types. Coverage must remain attributable to the named task and observations.

Before selecting real cases, record the target use contexts, sampling unit,
inclusion and exclusion rules, selection rationale, rights disposition, and
known biases. Include the project's P5/ODD context, language or writing system
where relevant, and the editorial task. Report coverage of this bounded sample.
Purposefully selected examples cannot establish community-wide prevalence.

Reserve at least one adverse case for evaluation after the candidate mappings
are defined. If access or rights prevent its use, record the gap rather than
substituting a convenient success case without explanation. The case-family
list below is a coverage guide, not a completed sampling protocol.

### Comparative case record

A case is an authored comparison contract with generated views and results.
Its canonical inputs must be distinguished from displays derived from them.
The existing experiment directories retain their own versioned artifact
contracts. These information requirements do not create another
evidence layer or require those directories to be reorganized.

| Part | Required information |
|---|---|
| Phenomenon and task | Stable case ID, intended observation or operation, case role, scope, and exclusions |
| Source context | P5 release, module and specification locators, customization, canonical grounding, provenance, and rights |
| P5 alternatives | One or more variants, each with a stable ID, rationale, full relevant input context, processor assumptions, and separately reported validity and preservation checks |
| Candidate instance | Exact model version and records, mapping policy, profiles and processor dependencies, unresolved objects and references |
| Formal description | Object meanings and identities, relation domains and ranges, cardinalities, order, invariants, operations, and expected valid and invalid behavior |
| Serializations | Binding version, generated syntax, supported domain, parser and decoder results, comparison relation, and unsupported formats |
| Evaluation | Required observations, discrepancies, losses, unknowns, manual decisions, and reverse-mapping tests for each alternative |

P6 XML denotes a binding of this independent candidate. Only bindings with a
declared contract may be presented as supported. The
[[knowledge/text-model-bindings|version 0.1 binding contract]] names the
bounded interchange definitions. RDF, JSON-LD, and any other unimplemented
binding remain open work rather than selectable equivalent outputs.

### P5 variants and model alternatives

Use one P5 variant when only one is justified by the declared source and task.
Add alternatives where their different assumptions help test the requirement.
Never invent a fixed number of variants to make the interface look complete.
For overlapping ranges, an anchor-and-span formulation is a candidate baseline
to examine. Its source context, endpoint policy, and customization checks must
be made explicit. Other formulations require their own supported semantics.

P5 syntax variants and competing abstract models are different comparison
axes. Rearranging a P5 encoding does not automatically produce another model.
Changing the candidate from JSON to XML does not produce another model either.
Keep the task and required observations fixed while varying one declared axis,
then report the dependencies introduced by that variation.

### Formal description and diagrams

The formal description names the complete rules needed for the example,
including conditions not visible in the diagram. A type diagram identifies
object kinds and directed relationships with cardinalities. An instance
diagram contains the actual IDs and references in the selected package.
Neither a diagram edge nor a spatial arrangement may imply identity,
containment, ordering, or authority absent from the formal records.

For selection examples, display the source sequence with its declared position
unit and selected extents. For time or surface examples, use a corresponding
temporal or spatial view only after its coordinate semantics are defined.
An entity-relationship diagram by itself cannot demonstrate interval overlap,
text order, or image alignment.

The technical frontend presents the comparison beside the proposal and gives
it a direct URL. P5 variants and candidate serializations are independently
selectable. Code, text highlights, and instance diagrams refer to the same
selected records. Missing source support, a failed mapping, or an unimplemented
binding must remain visible. Changing the view must not substitute a success
case for the one the reader opened. The interface contract that carries these
requirements is [[knowledge/design]].

### Required variants

A complete case contains a minimal example that isolates one rule, a realistic
example that preserves domain complexity, a boundary or adversarial example,
an invalid example with an expected diagnostic, and a migration example from
the pinned P5 baseline. When multiple serializations are in scope, the case also
defines their expected semantic equivalence or declared loss.

Negative cases test the model's constraints and expected diagnostics.

### Initial case families

These are task families for case selection, not an exhaustive list of modules,
document types, or implemented model capabilities.

| Family | Capability under test |
|---|---|
| mixed content | ordered alternation of text and inline structures |
| overlap | spans and concurrent hierarchies without false nesting |
| context-sensitive content | rules whose meaning or validity depends on structural context |
| stand-off annotation | stable references, ranges, and external annotation layers |
| linking and identity | local and global identifiers, pointers, and relation typing |
| bibliography | structured, unstructured, and partially known descriptions |
| critical apparatus | readings, witnesses, lemmas, variation, and location |
| manuscript description | deep structures, uncertain values, and reusable entities |
| linguistic annotation | tokenization, segmentation, alternatives, and alignment |
| facsimile alignment | text regions, surfaces, coordinates, and media references |
| correspondence | communicative roles, dates, places, attachments, and response relationships |
| documentary acts | issuers, witnesses, attestation, formulaic structure, copies, and carrier relations |
| dictionaries and encyclopedic entries | headwords, senses or topics, grammatical descriptions, attestations, and cross-references |
| transcription and revision | deletion, addition, substitution, uncertain readings, hands, and successive states |
| verse and performance | metrical and syntactic divisions, speakers, stage instructions, and concurrent events |
| spoken and recorded text | utterances, turn taking, pauses, temporal alignment, and recording context |

Initial pilots must cover hierarchy, overlap or stand-off annotation, and
context-sensitive customization before drawing conclusions across these
structural patterns.

### Before-and-after comparison

Compare the semantic objects in both representations, constraints expressed or lost, amount of
implicit context, required processing knowledge, diagnostic quality,
customization effects, and teaching or authoring consequences.

Useful measurements include element or node count, nesting depth, number of
cross-references, constraint count, transformation steps, unresolved
ambiguities, loss events, validator diagnostics, and implementation effort.
Quantitative measures are interpreted alongside domain review. Fewer nodes do
not automatically mean a better model.

### Equivalence obligations

For a supported binding with encoder E and decoder D, check
`equivalent(M, D(E(M)))` for valid model instances M under the named model
version's comparison relation. A passing model roundtrip shows that the binding
preserves those defined distinctions for the tested domain. It does not show
that every arbitrary source file can be decoded, that input formatting is
reconstructed, or that the model preserves an editor's intended meaning.

P5 migration therefore needs independently authored observations of both the
source and decoded target. Exact identity, task equivalence, lexical identity,
and practical adequacy are different tests. Report them separately, including
which have not run. An unsupported mapping can produce a correct refusal and
still count as a failed migration. Successful diagnostics must not inflate the
number of preserved cases.

### Migration classes

Report migration on separate axes. A mapping can preserve the required model
while changing lexical details or requiring a human policy decision. One
exclusive label would hide those combinations.

| Axis | Required distinction |
|---|---|
| coverage | all in-scope constructs mapped, only a named subset mapped, or unsupported |
| model preservation | all required distinctions preserved, a named task-equivalence preserved, or explicit losses/unknowns |
| lexical change | none, or an enumerated set of normalizations and other changes |
| dependency | deterministic from declared inputs, policy-dependent, externally enriched, or unresolved, with combined dependencies recorded |
| reversibility | reconstructable under a named comparison relation and package context, not reconstructable, or untested |

Migration reports identify the source object, target object, applied rule,
confidence or determinism, warnings, information loss, manual intervention, and
reverse-mapping behavior.

Each axis needs a decision rule and case-level evidence before a machine-readable
schema is introduced. Use the comparison distinctions of the serialization and
conformance contract in the
[text model, section 12](text-model.md#12-serialization-and-conformance).
Normalized output or a successful roundtrip cannot define its own preservation
criterion.

### Migration pipeline

```text
P5 document + P5 customization + baseline version
    -> P5 validation and feature inventory
        -> normalized P5 interpretation
            -> explicit migration rules
                -> candidate P6 model
                    -> P6 blueprint validation
                        -> selected serialization
                            -> semantic and loss report
```

The source customization is part of the migration input. Validating only
against TEI All can miss project-specific restrictions and extensions that
determine the intended meaning.

### Acceptance rule

A design decision is example-ready when its valid behavior, invalid behavior,
migration effect, and serialization effect are all testable. It becomes a
candidate recommendation only after representative examples and disconfirming
cases have been evaluated against grounded P5 knowledge.

## Relation to the output chapters

The coverage method of the investigation, every module of the pinned P5
baseline with document type, media form and phenomenon kept as separate case
dimensions and coverage reported separately for inventory, interpretation,
requirements and executed cases, is stated in section 1 of the
[P6 Design chapter](../40_output/12-p6-design.md).

P5 Architecture, Elements and Classes, and ODD and Customization establish the
baseline. Text and Document Structures, Annotation and Overlap, Critical
Apparatus, and Metadata and Entities develop the required distinctions. History
and Governance and Issues and Decisions establish the dated problem and
decision context. Abstract Model develops the conceptual alternatives.
Interoperability and Processing evaluates their executable consequences. P6
Design brings those arguments together without treating their recommendations
as externally established facts.

Reading entry points are the [text identity pilot](../40_output/02-abstract-model.md)
and [selection, hierarchy, and identity](../40_output/06-annotation-and-overlap.md).
Their grounding stays with assertions. These links provide navigation only.
The nine-part structure that these chapters serve is in the
[[knowledge/p6-evaluation|P6 evaluation]].
