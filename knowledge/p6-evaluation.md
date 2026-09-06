---
title: P6 Evaluation
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
related: [specification, p6-architecture, text-model, experiments, plan, state]
---

# P6 Evaluation

This document holds the qualities against which candidate P6 architectures
are tested, the method for comparing alternatives without assuming the
answer, the structure of the independent proposal's argument and the
acceptance criteria for its synthesis. All of it is an independent project
hypothesis. It does not prescribe a final syntax or prove that a major
redesign is preferable to compatible P5 evolution. The authoritative
evaluation dimensions and decision gates remain in [[knowledge/specification]].

## Statement roles

Statements about the design use four roles.

- **Requirement:** a capability a candidate is evaluated against. Distinguish
  requirements derived from grounded findings from explicit project choices;
  a project decision records a commitment, not external evidence of need.
- **Hypothesis:** a proposed design choice that must be tested against
  alternatives.
- **Contract:** an operational rule for a prototype or evaluation.
- **Question:** an unresolved issue assigned to evidence gathering, formal
  analysis, prototyping, or governance.

None of these roles establishes a fact about P5 or the official P6 process.
When a design document relies on such a fact, the final research output must
cite the relevant assertion in `30_assertions/`.

## Design principles as evaluation criteria

These principles define the qualities against which candidate P6 architectures
will be tested. They do not prescribe a final syntax or prove that a major
redesign is preferable to compatible P5 evolution.

### Evidence before architecture

A change must identify the P5 behavior it preserves, repairs, replaces, or
removes. Reported pain, successful practice, historical rationale,
counterexamples, and migration consequences must be examined before a design is
preferred. Complexity or age alone is not evidence of a defect. The
[option space](#option-space) and the [decision gates](#decision-gates) apply
this principle.

### Model before serialization

Concepts, identity, containment, order, text, relations, and constraints should
be defined independently of XML, JSON, RDF, or another concrete syntax. Each
serialization is a binding with an explicit mapping contract. The abstract
model must not merely rename the data structures of one preferred syntax.
The rule that one instance underlies every binding view in
[technical reading and comparison](#technical-reading-and-comparison) applies
this principle.

### Preserve ordered textual structure

Text encoding requires order, mixed textual and structural content, addressable
regions, and relationships across regions. These are first-class semantic
requirements rather than artifacts to reconstruct from one serialization.

### Support trees and graphs explicitly

Document containment is valuable but not sufficient for overlap, stand-off
annotation, correspondence, alignment, and other non-hierarchical relations. A
candidate should represent both ordered hierarchies and graph relations without
forcing one to masquerade as the other.

### Make context and constraints visible

Whether a construct is permitted or meaningful may depend on its containing
structure, blueprint, or declared processing contract. Context-sensitive rules
should be explicit, inspectable, and testable rather than hidden in prose or
processor convention.

### Keep customization compositional

Projects must be able to select, restrict, combine, and extend reusable model
parts. Composition should have deterministic conflict rules, predictable
inheritance, and diagnostics that explain which blueprint or customization
introduced a constraint. The customization operations and composition rules
of the [[knowledge/p6-architecture|P6 architecture]] elaborate this principle.

### Distinguish identity from labels and locations

Objects, concepts, versions, and source regions need stable identifiers that do
not depend on a filename, namespace prefix, display label, or current URL.
Serializations may use different local identifiers while preserving the same
declared identity.

### Define interoperability as a contract

Interoperability is not established by producing multiple file formats. A
binding must specify which concepts and invariants it preserves, how ordering
and identity are represented, what information it normalizes or loses, and how
equivalence is tested. The binding rule in
[technical reading and comparison](#technical-reading-and-comparison) and the
ninth [acceptance criterion](#acceptance-of-the-synthesis) apply this
principle.

### Prefer progressive complexity

Evaluate complexity with named authoring and processing tasks. For an
introductory task, record the concepts the author must understand, declarations
they must supply, steps needed to diagnose an error, and dependencies a
receiving tool must obtain. Generated or inherited declarations reduce effort
only when their effective values remain inspectable and reproducible.

Add an advanced feature to the same example, such as a second annotation of a
paragraph, and record what changes in the document, explanation, and processor.
Reduced markup is useful only when it preserves necessary distinctions and
does not move unexplained complexity into tools or implicit conventions.
[Adequacy and practical use](#adequacy-and-practical-use) applies this
principle.

### Treat migration as part of the design

Every architectural decision is evaluated against existing P5 documents,
customizations, schemas, processors, teaching material, and institutional
workflows. Ambiguous, lossy, and unsupported migrations must be reported, not
hidden behind a nominal converter. The [evaluation record](#evaluation-record)
and the [decision gates](#decision-gates) apply this principle.

### Make conformance executable

Normative requirements should have machine-checkable identifiers, defined
scope, expected diagnostics, and positive and negative fixtures wherever
possible. Prose remains necessary for meaning and rationale, but hidden
processor behavior is not a conformance mechanism. The example and prototype
results among the [evidence levels](#evidence-levels) apply this principle.

### Design for evolution and governance

The model needs explicit rules for versioning, extension, deprecation,
compatibility, and ownership of identifiers. Technical modularity must be
matched by a governance process capable of reviewing and maintaining modules,
bindings, blueprints, and test suites over time. The
[evaluation record](#evaluation-record) applies this principle in its effects
on validators, processors, APIs, teaching, and governance.

### Evaluation rule

No principle wins automatically. A candidate that improves conceptual clarity
may harm migration; a highly generic model may become difficult to teach; a
lossless binding may be costly to process. Every recommendation must state its
benefits, regressions, affected stakeholders, uncertainty, and rejected
alternatives under the shared evaluation framework. The
[evaluation dimensions](#evaluation-dimensions) and
[reporting outcomes](#reporting-outcomes) apply this rule.

## Comparative evaluation

This project does not begin with a preferred P6 architecture. It compares
alternatives against the same evidence, examples, and criteria so that
“optimized” always names a visible trade-off rather than a general impression.

### Option space

Every major problem should consider at least four classes of response:

| Option | Question |
|---|---|
| repair within P5 | Can documentation, ODD, constraints, or tooling solve the problem without a new architecture? |
| compatible evolution | Can a new capability preserve the principal P5 contracts and migration path? |
| architectural redesign | Does the problem require a different abstract model or compatibility boundary? |
| defer or reject | Is the problem insufficiently evidenced, out of scope, or more costly to solve than to retain? |

Additional variants may be added, but none may disappear merely because the
team prefers a greenfield design. This applies
[evidence before architecture](#evidence-before-architecture).

### Evaluation record

The unit of comparison is a design decision, not an entire imagined standard.
Each record identifies:

- the grounded P5 baseline and affected constructs;
- stakeholders, use cases, and the selection scope they cover;
- the demonstrated problem or explicitly proposed requirement, and relevant
  counterevidence;
- candidate options, including preservation of current behavior;
- assumptions and unresolved dependencies;
- expected benefits and regressions by criterion;
- required prototypes, examples, and measurements;
- migration outcomes for existing documents and customizations;
- effects on validators, processors, APIs, teaching, and governance;
- recommendation, confidence, and conditions that would reverse it.

Recommendations are project posits unless they report and attribute an external
proposal. Facts about P5 or the official P6 process require their own grounded
support. The record applies
[treat migration as part of the design](#treat-migration-as-part-of-the-design)
and [design for evolution and governance](#design-for-evolution-and-governance).

### Evaluation dimensions

The authoritative dimension definitions are in [[knowledge/specification]].
In compact form they cover conceptual clarity, expressivity, compositionality,
formal precision, customization, interoperability, validation and processing,
compatibility and migration, learnability and accessibility, and governance
and evolution.

Every option is evaluated on all relevant dimensions. “Not applicable” needs a
rationale. A benefit on one dimension never cancels a regression on another;
both remain visible for the decision maker. This is the
[evaluation rule](#evaluation-rule) applied per dimension.

### Evidence levels

An evaluation distinguishes four levels of support:

| Level | Meaning |
|---|---|
| assertion | grounded account of P5, use, history, or an attributed proposal |
| example result | reproducible behavior on a declared case and version |
| prototype result | measured behavior of an implementation under stated conditions |
| judgment | reasoned interpretation or preference, explicitly marked as such |

Counts of issues, elements, or lines of markup are descriptive measurements,
not automatic quality scores. Qualitative judgments name the reviewer,
procedure, and uncertainty where possible.

These levels describe support for evaluation, not additional Vault artifact
types or statuses. A prototype report is an experiment output; to support a
persistent factual assertion, its versioned observations must enter the
canonical source-to-assertion chain. A design recommendation remains a reasoned
posit even when its factual premises are well supported. Example and prototype
results are where [make conformance executable](#make-conformance-executable)
takes effect.

### Adequacy and practical use

Evaluate three separate questions: whether the declared rules are consistent
and executable; whether the model preserves the distinctions required by the
chosen cases; and whether people can use it to complete the intended tasks.
Passing instance validation answers only part of the first question. A bounded
search that finds no contradiction must state its bounds; it is not a general
proof of consistency or satisfiability.

Define the expected editorial observations before implementing an encoding or
converter. Include pairs that must count as equivalent and pairs that must
remain distinct. Have those expectations reviewed independently of the
implementation so that the converter does not define its own correctness.

A practical-use comparison names the task, participant role and relevant
experience, baseline tools, procedure, and acceptance criteria in advance.
For example, ask an editor to inspect and revise an annotation after a text
change, then observe correctness, time, errors, help requests, and interventions
under each candidate. Keep task and starting information comparable. Small
exploratory trials can expose problems; report their sample and limits instead
of generalizing to all TEI users. Lower node counts or shorter markup alone do
not establish learnability or usability. This applies
[prefer progressive complexity](#prefer-progressive-complexity).

### Comparative scorecard

A scorecard should record observations before any aggregate score. Suggested
fields are:

```yaml
decision_id: p6-decision-...
baseline: tei-p5-4.12.0
problem_assertions: []
stakeholders: []
use_cases: []
options: []
dimensions: {}
example_results: []
prototype_results: []
migration_results: []
counterevidence: []
unknowns: []
recommendation: null
confidence: null
reversal_conditions: []
```

This is a planning shape, not an approved artifact schema. A formal schema is
introduced only through the repository's architecture-decision process.

### Decision gates

A proposal cannot pass directly from an attractive example to a design
recommendation. Its baseline behavior must be established; the problem must be
supported or the proposed requirement explicitly justified; alternatives must
be comparable; cases selected for the declared scope and adverse cases must
run; migration consequences must be measured where claimed; and official-process
claims must be dated and attributed. An exploratory experiment may leave these
questions open, but must limit its conclusion accordingly. A selector experiment
within one object model cannot justify choosing that model over another.

The project may conclude that different blueprints need different solutions.
Uniformity is preferred only when it improves the shared contract without
erasing domain requirements. The gates apply
[evidence before architecture](#evidence-before-architecture) and
[treat migration as part of the design](#treat-migration-as-part-of-the-design).

### Reporting outcomes

An evaluation ends with one of five outcomes: retain current behavior, revise
within P5, develop a compatibility-preserving P6 option, advance an
architectural redesign candidate, or keep the question open. The report states
why, what evidence is missing, what regressions remain, and what new evidence
would change the outcome, as the [evaluation rule](#evaluation-rule) requires.

## Structure of the proposal argument

The proposal should explain which textual distinctions and practices the model
can represent, why its categories are justified, and how those categories help
people encode, exchange, interpret, and maintain textual resources. Its coverage
ambition comes from systematic study of P5, its documented discussions, and
relevant literature. Each coverage claim must name the sources and cases that
support it. Unresolved requirements remain visible.

The canonical argument lives in `40_output/12-p6-design.md` and cites
assertions directly. This structure organizes that argument and supplies no
grounding of its own.

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

The bounded [P6 Design proposal](../40_output/12-p6-design.md) assembles the
first model argument, and the [[knowledge/text-model|Abstract Text Model 0.1]]
defines its executable scope. These provide an initial contribution to parts
4–6 and a provisional recommendation, with a conceptual alternative and
explicit mapping questions. They do not complete the real-case, migration, or
adoption evidence required by the full structure. The coverage method behind
part 1 and the mapping of the argument to the output chapters are in the
[[knowledge/p6-architecture|P6 architecture]].

### Technical reading and comparison

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
not additional evidence for its adequacy. These rules apply
[model before serialization](#model-before-serialization) and
[define interoperability as a contract](#define-interoperability-as-a-contract).

The example and migration contract of the
[[knowledge/p6-architecture|P6 architecture]] defines the comparison
obligations. The [[knowledge/text-model-bindings|version 0.1 binding contract]]
defines the bounded interchange rules. A model roundtrip, P5 migration
preservation, formal conformance, and editorial acceptance remain separate
questions.

### Acceptance of the synthesis

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

Research packages and open questions are in [[knowledge/plan]]. Progress
belongs in [[knowledge/state]].
