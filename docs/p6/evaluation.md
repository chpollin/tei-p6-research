# Evaluating P6 options

Status: comparative evaluation contract
Authority: independent project method

This project does not begin with a preferred P6 architecture. It compares
alternatives against the same evidence, examples, and criteria so that
“optimized” always names a visible trade-off rather than a general impression.

## Option space

Every major problem should consider at least four classes of response:

| Option | Question |
|---|---|
| repair within P5 | Can documentation, ODD, constraints, or tooling solve the problem without a new architecture? |
| compatible evolution | Can a new capability preserve the principal P5 contracts and migration path? |
| architectural redesign | Does the problem require a different abstract model or compatibility boundary? |
| defer or reject | Is the problem insufficiently evidenced, out of scope, or more costly to solve than to retain? |

Additional variants may be added, but none may disappear merely because the
team prefers a greenfield design.

## Evaluation record

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
support.

## Evaluation dimensions

The authoritative dimension definitions are in
`knowledge/specification.md`. In compact form they cover conceptual clarity,
expressivity, compositionality, formal precision, customization,
interoperability, validation and processing, compatibility and migration,
learnability and accessibility, and governance and evolution.

Every option is evaluated on all relevant dimensions. “Not applicable” needs a
rationale. A benefit on one dimension never cancels a regression on another;
both remain visible for the decision maker.

## Evidence levels

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
posit even when its factual premises are well supported.

## Adequacy and practical use

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
not establish learnability or usability.

## Comparative scorecard

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

## Decision gates

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
erasing domain requirements.

## Reporting outcomes

An evaluation ends with one of five outcomes: retain current behavior, revise
within P5, develop a compatibility-preserving P6 option, advance an
architectural redesign candidate, or keep the question open. The report states
why, what evidence is missing, what regressions remain, and what new evidence
would change the outcome.
