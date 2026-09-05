# Examples and migration

An experimental design contract for this independent proposal.

Examples specify the tasks used to derive requirements, compare models, and
test P5 migration.

## Example unit

Each case identifies a task, the distinctions that must survive it, and the
P5 and candidate representations under comparison. Claims of a P5 defect need
grounding. A design question may begin as a posit. Encoding complexity alone
does not establish a defect.

Record the editorial distinctions and observable task outcomes that a case
must preserve before producing candidate encodings. Obtain domain review of
these expectations independently of converter output. Synthetic cases isolate
assumptions. Cases taken from practice also require source provenance and a
declared selection protocol.

## Selection and coverage

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

## Comparative case record

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
[version 0.1 binding contract](serialization-bindings-v0.1.md) names the
bounded interchange definitions. RDF, JSON-LD, and any other unimplemented
binding remain open work rather than selectable equivalent outputs.

## P5 variants and model alternatives

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

## Formal description and diagrams

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
case for the one the reader opened.

## Required variants

A complete case contains a minimal example that isolates one rule, a realistic
example that preserves domain complexity, a boundary or adversarial example,
an invalid example with an expected diagnostic, and a migration example from
the pinned P5 baseline. When multiple serializations are in scope, the case also
defines their expected semantic equivalence or declared loss.

Negative cases test the model's constraints and expected diagnostics.

## Initial case families

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

## Before-and-after comparison

Compare the semantic objects in both representations, constraints expressed or lost, amount of
implicit context, required processing knowledge, diagnostic quality,
customization effects, and teaching or authoring consequences.

Useful measurements include element or node count, nesting depth, number of
cross-references, constraint count, transformation steps, unresolved
ambiguities, loss events, validator diagnostics, and implementation effort.
Quantitative measures are interpreted alongside domain review. Fewer nodes do
not automatically mean a better model.

## Equivalence obligations

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

## Migration classes

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
schema is introduced. Use the comparison distinctions in
`serialization-and-conformance.md`. Normalized output or a successful roundtrip
cannot define its own preservation criterion.

## Migration pipeline

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

## Acceptance rule

A design decision is example-ready when its valid behavior, invalid behavior,
migration effect, and serialization effect are all testable. It becomes a
candidate recommendation only after representative examples and disconfirming
cases have been evaluated against grounded P5 knowledge.
