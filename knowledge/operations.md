---
title: Operations
project:
  name: "TEI P6 Research"
  repository: "tei-p6-research"
method:
  name: Promptotyping
  url: https://dhcraft.org/Promptotyping/
status: draft
language: en
created: "2026-09-04"
updated: "2026-09-05"
related: [schema, state, journal]
---

# Operations

These procedures produce and check the artifacts defined in
[[knowledge/schema]]. Record processing state in [[knowledge/state]] and
durable decisions in [[knowledge/journal]].

## Acquire

Acquisition channel and source type are independent. Record the channel in
the representation's `channel` field without changing its checking obligations.

| Channel | Action |
|---|---|
| `handover` or `collection` | Place the original in `00_sources/` |
| `import` | Export the reference library as CSL JSON into `references/`, one file per batch |
| `deep-research` | Run the prompt below, capture every located publication in the reference manager, and export CSL JSON |

For a small curated import, CSL records may be transcribed from consulted
primary metadata. Record this choice in the journal and identify the exact
snapshots and bibliographic checks in the intake manifest. Apply the same
quotation and support checks. The CSL record remains the publication root.
An agent's report or reading memo never replaces the located source.

### Deep research prompt skeleton

> Research the topic **{topic from the controlled topic set}** for the project **{project}**.
> Search broadly, then prioritize: peer-reviewed and official sources first;
> exclude: {project exclusion list}. Evaluate candidates at full text.
> Counter-check adversarially: for each candidate finding, search for sources
> that contradict it. Deliver a list of publications with full bibliographic
> data and, per publication, the two or three passages that matter for the
> topic, quoted verbatim. Do not deliver synthesis; the vault synthesizes.

## Ingest

For an archivable document, first convert the original to Markdown while
preserving its headings, lists, tables, and paragraph boundaries. Then stamp
each anchor-relevant paragraph with a block ID. The resulting representation
is immutable.

Choose the converter by source structure and record it in `converter`.

| Source structure | Conversion |
|---|---|
| Short, simple text | Agent conversion |
| Standard office or PDF document | MarkItDown or pandoc |
| Complex layout or scanned document | Docling |
| Image requiring OCR | Unelaborated extension point |

| Source type | Required artifact |
|---|---|
| `document` | Markdown in `10_markdown/documents/`, with converter, original H1, and metadata |
| `data` | Data file in `10_markdown/data/` and a schema description with the same slug and metadata |
| `publication` | CSL JSON in `references/`, with no Markdown representation |

Run `python tools/inventory.py . --write` to regenerate the source inventory
in [[knowledge/state]] from the files.

## Distill

Produce one distillate per source through three steps.

1. Extract core statements with the canonical prompt, one statement per
   anchor, without evaluation or cross-source merging.
2. Apply the section skeleton, statement IDs, and anchor syntax in
   [[knowledge/schema]] through deterministic formatting.
3. Compare every statement with its source anchor. For publications, check
   the quotation while the full text is available and record `checked.quote`.

Reformulate or discard statements that fail fidelity checking and repeat the
check until every retained statement passes. Write any optional Appraisal
afterwards so that judgments cannot influence the extraction. Appraisal
remains outside the source-fidelity check.

### Canonical extraction prompt skeleton

> Extract the core statements of the source **{source short title}**, and of this
> source alone. Work only from the text given below.
> One statement per anchor. Each statement stands on its own, is understandable
> without its neighbours, and stays within the literal sense of the source.
> Do not evaluate, do not interpret, do not infer, and do not merge this source
> with any other; the vault synthesizes at a later layer.
> No statement without a nameable source location. Where you cannot name one,
> drop the statement.
> Deliver per statement the statement itself and its source location, in the form
> the source type requires: for a document the block it was taken from, for a
> publication the verbatim quotation with page, for data the computation that
> yields the stated result.
>
> SOURCE: {Markdown representation, quotation set, or data schema description}

Set the new distillate to `grounded` and run
`python tools/inventory.py . --write` again.

## Build assertions

Work by topic, with one file per assertion.

1. Enter through the topic map and read every distillate registered there.
2. Group statements about the same matter across sources and source types.
3. Formulate one atomic assertion per group, supported jointly by that group.
   An atomic statement cannot be split without losing its point.
4. List the supporting statement IDs in `grounding`, one per supporting
   source, and explain each anchor's contribution in Support.
5. For irreconcilable statements, write two assertions, mark both `contested`,
   and link them reciprocally through `contested-with`.
6. Reserve unsupported conclusions and distillate appraisals for output posits.
   They cannot ground assertions.
7. Register each assertion in its topic map with a short orientation and
   record unresolved questions under Open questions.

Machine-review every assertion against each supporting statement. Only
*fully supports* passes. Narrow a failed assertion or replace its unsupported
anchor with one that carries the claim, then review the changed pair again.

### Assertion review prompt skeleton

> You are an adversarial reviewer. Below are a distillate statement and an
> assertion that claims to be supported by it. Your task is to refute the
> assertion. Judge only whether this statement supports this assertion; whether
> the assertion is true is out of scope. Answer with exactly one verdict: fully supports
> | partially supports | overreaches | contradicts | not in the text. Then give
> one sentence of justification, and where the verdict is not *fully supports*,
> name the part of the assertion that the statement does not carry.
>
> STATEMENT: {distillate statement, without its own grounding anchor}
> ASSERTION: {assertion as one sentence}

## Write chapters

Use the working language and style sheet in [[knowledge/specification]].
Every load-bearing sentence receives a `Grounded in [[assertion]]` footnote
or, for an own conclusion, a
`Posit: <rationale>. Open evidence question: <question>` footnote. Mirror the
referenced assertions and posit count in frontmatter and update the chapter
register in [[knowledge/state]].

A synthesis of a topic uses the same chapter contract. Enter through its map.
Ground agreement in the relevant assertions and disagreement in both sides of
a contested pair. Citing only one side triggers `W-CONTESTED`. A research gap
drawn from the map's open questions enters as a posit with its evidence
question. A synthesis chapter remains an ordinary chapter even when it later
informs another chapter.

## Query

Enter through topic maps and follow assertions to distillate statements.
Consult source passages where exact wording matters. Cite assertions by
wikilink. Record unanswered questions in the topic map.

## Check

The three check contracts are fixed. Their implementation mechanisms are
project choices recorded in [[knowledge/specification]].

### Contract: validation

Validation checks formal conformance against [[knowledge/schema]]. It is
deterministic and runs on every change. A failing file cannot proceed to
another check. Validation alone does not promote status. Record
`checked.validation: <date>` on each file that passes.

Run `python tools/validate.py .` to check frontmatter, anchors, statement IDs,
quotation identity where source text is available, computation declarations,
topic-map reachability, reciprocal contested links, chapter mirrors and
footnote keywords, and status discipline. Data computations are rerun and
their results compared by default. `--no-computations` omits that step for a
faster, narrower check.

Use `python tools/validate.py . --chapter 40_output/<slug>` to check a chapter
and the assertions, distillates, and representations it grounds in. The scope
walk follows only immediate-layer anchors. Other branches and vault-wide
warnings are excluded, and the closing output names the excluded checks.
Any warning or error within chapter scope fails the run.

| Diagnostic | Condition |
|---|---|
| `E-ANCHOR` | An anchor or frontmatter target in `source`, `data`, `representation`, `superseded-by`, or `contested-with` does not resolve |
| `E-LAYER` | An anchor skips its direct predecessor layer |
| `E-GROUNDING` | An artifact with a grounding obligation has empty grounding |
| `E-DUPLICATE` | A block or statement ID occurs more than once within a file |
| `E-STATUS` | A required check is missing or an entry in `checked` lacks a date |
| `E-LADDER` | An artifact's status exceeds that of an anchor it rests on |
| `W-PLACEHOLDER` | An unreplaced double-brace placeholder remains in the vault |
| `W-EMPTY` | No document exists in the production chain from `10_markdown` to `40_output` |
| `W-STALE` | `updated` is later than the most recent recorded check date. Artifacts without check dates do not trigger it |
| `W-DUPLICATE-GROUNDING` | Two assertions have equal grounding sets or one set contains the other |
| `W-ALIAS` | A chapter footnote alias differs from its assertion's H1 and may omit a qualifying clause |
| `E-FRONTMATTER` | Frontmatter is unreadable or not a map, carries an unknown type, misses a required field, holds an illegal value, gives a list-valued field another type, or leaves a declared metadata field out |
| `E-SOURCE` | A second representation or a second distillate names a source another one already holds |
| `E-STATEMENT` | A core statement has no statement ID, has no source anchor or more than one, or mints an ID outside the Core statements section |
| `E-QUOTE` | A publication distillate records no intake quotation check (`checked.quote`) |
| `E-COMPUTATION` | A data computation names other than one script, passes an argument, lies outside `tools/analysis/`, is missing, fails, or yields another result than the stated one |
| `E-TOPIC` | A `topics` value names no topic map of the controlled topic set |
| `E-ORPHAN` | An assertion is reachable from no topic map |
| `E-CONTESTED` | A contested assertion names no counterpart, or a contested relation is one-sided |
| `E-FOOTNOTE` | A chapter footnote is used without definition, defined without use, defined twice, or opens with neither `Grounded in` nor `Posit:` |
| `E-MIRROR` | A chapter's `assertions` mirror or `posits` count disagrees with its footnotes |
| `E-SCOPE` | `--chapter` names no chapter document |
| `W-NAME` | A file name is no ASCII-lowercase hyphen slug; `MOC-<Topic>.md` is the schema's exception |
| `W-UNANCHORED` | A chapter paragraph carries no footnote marker |
| `W-NO-OUTPUT` | The vault holds no chapter, so the footnote contract has no subject |

Every warning must be investigated. Warnings identify either a check with no
subject or a condition the schema does not classify as an error. They are
printed and counted. Vault-wide warnings preserve a successful exit code for
work in progress. Chapter warnings fail the run because it judges readiness
for acceptance.

### Contract: machine review

Machine review judges source support for each passage and statement pair.
Its fixed verdicts are **fully supports**, **partially supports**,
**overreaches**, **contradicts**, and **not in the text**. Only *fully supports*
passes. Together with validation, this permits `validated` status and no higher.

Anti-anchoring is mandatory. The reviewer sees the source location and bare
statement, without the producing agent's reasoning. A reviewer from a different
model family is recommended to reduce correlated errors.

A document pair contains the anchored block and heading path. A publication
pair contains the quotation. A data pair contains the computation and its
result. Each is paired only with the statement being judged.

Record `checked.machine-review: <date>`. Failed verdicts require rework.
Record systematic failure patterns in the journal.

  > You are an adversarial reviewer. Below are a source passage and a statement
  > that claims to be supported by it. Your task is to refute the statement.
  > Judge only whether this passage supports this statement. Answer with exactly
  > one verdict: fully supports | partially supports | overreaches | contradicts
  > | not in the text. Then give one sentence of justification.
  >
  > PASSAGE: {source location, with its heading path}
  > STATEMENT: {statement}

The reviewer must add a line when the statement displaces the passage's subject.
For a self-report, *fully supports* applies when the statement attributes the
claim to the source. Asserting the claimed achievement itself is *overreaches*.
For a state report, the statement must retain the state and date shown by the
source. Extending that observation into an unqualified property of the object
is *overreaches*. Examples include restored objects, dated inventories, and plans.

### Contract: verification

The human verification role named in [[knowledge/specification]] judges
whether grounding holds as evidence. Only this role may establish `verified`.
Machine checks prepare the material without replacing that judgment.

Verification proceeds passage by passage over the prepared pairs. Sampling is
permitted where the machine-review pass rate justifies it, with the sampling
rule recorded in the journal. Record `checked.verification: <date>` by or on
behalf of the verifying role.

### Status discipline

`grounded` → (validation and machine review passed) → `validated` →
(expert passed) → `verified`. Assertion building or review may set
`contested` when sources conflict. Only verification resolves it.
An artifact's status is the minimum of its anchors' states.
