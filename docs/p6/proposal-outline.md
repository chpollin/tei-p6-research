# Abstract Text Model: proposal structure and coverage method

An outline for this project's independent proposal.

The proposal should explain which textual distinctions and practices the model
can represent, why its categories are justified, and how those categories help
people encode, exchange, interpret, and maintain textual resources. Its coverage
ambition comes from systematic study of P5, its documented discussions, and
relevant literature. Each coverage claim must name the sources and cases that
support it. Unresolved requirements remain visible.

The canonical argument lives in `40_output/12-p6-design.md` and cites
assertions directly. This outline organizes that argument and supplies no
grounding of its own.

## Proposed argument

| Part | Question the reader should be able to answer | Required foundation |
|---|---|---|
| 1. Purpose, audience, and coverage | What does the proposed model aim to describe, for whom, and under what limits? | Declared source/search boundaries, stakeholder tasks, explicit exclusions and unresolved coverage. |
| 2. P5 baseline | Which distinctions and successful capabilities must be understood and preserved? | Pinned ODD declarations interpreted with Guidelines prose, examples, and relevant customizations. |
| 3. Problems and competing accounts of text | Which needs are demonstrated, which are contested, and which are project choices? | Source-grounded discussion histories and literature, including counterevidence and already implemented repairs. |
| 4. Requirements | What must a candidate express or enable, and why? | Each requirement linked to findings or labeled as a project posit, with expected observations and counterexamples. |
| 5. Abstract model and alternatives | What objects, identities, relations, order, constraints, and interpretation boundaries are proposed? | At least two conceptual alternatives compared against the same requirements, with justified core and extension choices. |
| 6. Formalization and examples | How can someone construct and check an instance? | Explicit semantics, positive and adverse fixtures, diagnostic behavior, and declared undecidable or untested properties. |
| 7. Serialization and migration | What survives exchange and conversion, and what requires policy or is lost? | Independently specified comparison relations, P5 mappings, binding contracts, and separate preservation and dependency reports. |
| 8. Practical use and adoption | Can intended users perform their tasks, and what would adoption cost? | Comparable workflows, domain review, tool and teaching implications, and governance responsibilities. |
| 9. Recommendation and open decisions | What should be advanced, retained, revised, or deferred? | Benefits and costs, alternatives, remaining gaps, and explicit conditions that would reverse each recommendation. |

## Coverage through every P5 module

The scope of the investigation is all modules of the pinned P5 baseline. This
is a commitment to examine their representational requirements, not a claim
that the current candidate covers them. Modules organize the source inventory.
The conceptual model must justify its own categories independently of that
organization.

Case selection distinguishes three dimensions.

| Dimension | Proposed examples | What a case must explain |
|---|---|---|
| Document or text type | Letter, charter, dictionary entry, poem | Which domain roles, structures, and acts matter to the task? |
| Transmission or media form | Manuscript, print, digital file, recorded speech | Which carrier, layout, temporal, or version distinctions must be retained? |
| Phenomenon | Dating, correction, uncertainty, attribution, overlap | Which distinction occurs across types and media, and what varies by context? |

These are working classification examples, not established correspondences
between P5 modules and ontological classes. A manuscript letter and a poem can
exercise a common proposed correction requirement while needing different
domain descriptions. Module, document type, medium, phenomenon, element, and
model entity must therefore remain separately identifiable.

Each module investigation produces a declaration inventory, source
interpretation, requirements, and case evaluation. The inventory locates
elements, attributes, classes, macros, datatypes, constraints, and references
at the pinned release. Interpretation connects these declarations to
Guidelines prose, customizations, and observed use, including conflicts and
unknowns. Requirements name the task, necessary distinctions, and proposed
core, profile, or external model support. Cases test those requirements through
P5 alternatives, candidate instances, migration observations, and domain
review. Direct declarations, effective rules, and executed cases are counted
separately.

Issues and literature feed the interpretation and requirement stages. A
reported difficulty must be checked against its version and the current
baseline. Scholarly disagreements remain visible. The steps are research
obligations, not new Vault artifact statuses. Source acquisition completeness,
grounding and verification, specification coverage, and executed case coverage
are separate measures.

The eventual coverage account needs a declared denominator and dispositions
for missing, excluded, or unresolved entries. Passing one phenomenon case
does not complete a module, and processing every declaration does not establish
coverage of all textual practices. A prototype that models character sequences
and attributed readings must retain that boundary while this investigation
tests whether additional primitives or connected domain models are required.

## Technical reading and comparison

The canonical synthesis is a continuous technical text with numbered sections.
An example link opens the corresponding comparative specification without
replacing the argument. Its record separates the phenomenon and task, P5
variants, the candidate model, supported serializations, formal constraints,
and results. Closing a comparison returns to the originating paragraph.

The same instance must underlie its XML, JSON, or other supported binding views.
A proposed binding with no decoder and checked contract is identified as a
proposal. Type diagrams show object kinds and relation cardinalities. Instance
diagrams show the actual IDs in the case. Diagrams, highlighted text, and code
must refer to those same records. They are explanations of the declared model,
not additional evidence for its adequacy.

The [example and migration contract](examples-and-migration.md) defines the
comparison obligations. The
[version 0.1 binding contract](serialization-bindings-v0.1.md) defines the
bounded interchange rules. A model roundtrip, P5 migration preservation,
formal conformance, and editorial acceptance remain separate questions.

## Relation to the output chapters

P5 Architecture, Elements and Classes, and ODD and Customization establish the
baseline. Text and Document Structures, Annotation and Overlap, Critical
Apparatus, and Metadata and Entities develop the required distinctions. History
and Governance and Issues and Decisions establish the dated problem and
decision context. Abstract Model develops the conceptual alternatives.
Interoperability and Processing evaluates their executable consequences. P6
Design brings those arguments together without treating their recommendations
as externally established facts.

Reading entry points are the [text identity pilot](../../40_output/02-abstract-model.md)
and [selection, hierarchy, and identity](../../40_output/06-annotation-and-overlap.md).
Their grounding stays with assertions. These links provide navigation only.

The bounded [P6 Design proposal](../../40_output/12-p6-design.md) assembles the
first model argument, and [Abstract Text Model 0.1](abstract-text-model-v0.1.md)
defines its executable scope. These provide an initial contribution to parts
4–6 and a provisional recommendation, with a conceptual alternative and
explicit mapping questions. They do not complete the real-case, migration, or
adoption evidence required by the full outline.

## Acceptance of the synthesis

- Every factual premise has the canonical provenance chain and the required checks.
- Every proposed requirement and design choice is identifiable as the project's judgment.
- A reader can follow a requirement to its source context, example, alternatives, formal description, and evaluation.
- Every pinned P5 module has a visible inventory disposition. Interpretation and model coverage are reported separately from declaration counts.
- Document types, media, and cross-cutting phenomena are not silently equated with modules or proposed model classes.
- Historical complaints are checked against the declared current baseline.
- Formal conformance, conceptual adequacy, and practical usefulness have separate evidence.
- Preservation, losses, costs, uncertainties, and reversal conditions accompany recommendations.
- Supported serialization views derive from the same model instance and name the comparison relation their checks actually test.
- The title and text consistently distinguish the independent proposal from official TEI decisions.

Execution packages are specified in [research-wave-1.md](research-wave-1.md)
and [research-agenda.md](research-agenda.md). Progress belongs in `knowledge/state.md`.
