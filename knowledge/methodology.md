---
title: Methodology
project:
  name: "TEI P6 Research"
  repository: "tei-p6-research"
method:
  name: Promptotyping
  url: https://dhcraft.org/Promptotyping/
profile:
  name: Grounded Vault
  url: https://github.com/DigitalHumanitiesCraft/grounded-vault
status: draft
language: en
created: "2026-09-06"
updated: "2026-09-06"
related: [INDEX, schema, operations, verification, testing, architecture]
---

# Methodology

Grounded Vault organizes research claims so that a reader can follow them to
source passages and inspect the checks behind them. It is a Promptotyping
profile for work with explicit evidence obligations. This document explains
why the knowledge of this project is organized that way and what its checks
establish. The operative contracts are in [[knowledge/schema]],
[[knowledge/operations]] and [[knowledge/verification]].

## Problem

A report may cite a source without showing which passage supports a
particular claim. The reader then has to reconstruct that connection and
determine whether the statement preserves the passage's meaning. This applies
to human-authored and generated research alike.

Grounded Vault makes that connection part of the document structure. A
resolvable citation supplies a checkable path. Source-support review and
human judgment assess what the path establishes.

## Core idea

Source material enters at the bottom of a layered repository. Defined
transformations produce source statements, assertions and output while
preserving references between adjacent layers. Every load-bearing output
statement cites an assertion or is marked as an authorial posit.

```text
00_sources -> 10_markdown -> 20_distillates -> 30_assertions -> 40_output
```

Three checks divide the work. Validation tests structure and anchor
resolution. Machine review tests whether each passage supports its statement.
Human verification determines whether a grounding relation qualifies as
evidence under the project's review role. Agents can prepare the files and
review pairs, but their agreement does not establish truth. The intended
result is an inspectable research record with dated check outcomes. An
unfinished vault remains useful because the review state of each artifact is
explicit.

| Check | Question | Authority |
|---|---|---|
| Validation | Does the artifact satisfy its formal contract and do its anchors resolve? | records deterministic conformance |
| Machine review | Does the cited passage support the statement? | with validation, permits `validated` |
| Verification | Does this grounding hold as evidence? | the designated human expert may establish `verified` |

Artifacts progress from `grounded` through `validated` to `verified` only
after the corresponding checks, and dates record when those checks ran. An
artifact cannot exceed the status of its supporting anchors or the authority
of its reviewer. Conflicting assertions may instead be `contested`.

## Why one distillate per source and one claim per assertion

A distillate extracts statements from exactly one source and preserves that
source's scope, keeping appraisal separate from reported content. Cross-source
synthesis happens in assertions, the layer where different sources and source
types can contribute to the same claim. Keeping these steps apart makes a
source-fidelity check possible before any judgment is applied and keeps the
provenance chain free of skipped layers. Irreconcilable assertions remain
contested and link to one another in both directions, so an output account of
the disagreement cites both sides.

Evidence is relative to a claim rather than an intrinsic property of a
document. Grounding is the structural relation, evidence the grounding
relation that passed human verification, and a posit a conclusion supported
by the author's reasoning with an explicit rationale and open evidence
question. The audit trail records only checks that actually ran.

## Dual readability

Humans and agents use the same Markdown files. Topic maps collect assertions,
wikilinks connect related material, and output footnotes lead toward source
passages. The files remain readable outside Obsidian. Agent adapters such as
`AGENTS.md` and `CLAUDE.md` provide short, harness-specific instructions that
route into `knowledge/` without duplicating the contracts or making the
architecture depend on one vendor. The generated workbench renders the same
artifacts under [[knowledge/design]] without creating another knowledge
layer.

## The output as a parameter

The reference output is continuous prose, with one independently checkable
file per chapter. Each load-bearing statement has an inline marker
identifying its assertion support or posit. Frontmatter mirrors the assertion
set and posit count, and validation compares both representations.

Footnotes keep this contract readable in Markdown. An alternative notation
must preserve inline markers, the support or posit keyword and the structured
mirror. A separate data sidecar alone would not preserve human readability.
Genre and style can change without changing these evidence obligations.

Code or data-analysis output requires a separate anchoring design that the
inherited profile does not define. The project's executable experiments
therefore use their own explicit contracts, recorded in
[[knowledge/experiments]], while grounded research conclusions continue to
enter the canonical output chain.

## Instantiation

A project selects its purpose, controlled topics, source types, output genre,
working language, human verification role and checking mechanisms. The layer
model, source anchors, check contracts and status progression remain
invariant. The parameters chosen here are recorded in
[[knowledge/specification]].

The project is maintained as an executable research specification.

| Component | Project realization |
|---|---|
| Intent | understand P5 well enough to compare and test P6 architecture options |
| Inputs | versioned normative, development, governance, historical, scholarly and practice sources |
| Transformations | acquire, normalize, admit, distill, synthesize, review, prototype, evaluate |
| Knowledge objects | representations, distillates, assertions, topic maps, glossary entries, chapters |
| Control objects | registry, locks, run manifests, schemas, state, journal, tests |
| Outputs | P5 model atlas, decision trails, problem taxonomy, P6 options, migration and evaluation dossier |
| Feedback | deterministic validation, adversarial machine review, human verification, prototype results |

The documents in `knowledge/` are part of the control system. They are
revised when the project learns something about its own method or scope.
Research findings themselves enter the canonical Grounded Vault layers.

## Lineage

The design draws on source criticism's attention to the source location,
prosopography's distinction between a recorded statement and an asserted
fact, and nanopublications' pairing of assertions with provenance. Schema
validation in scholarly editing and explicit provenance in data management
supply related technical practices.

These connections explain the design's intellectual context. Whether Grounded
Vault is adequate for a research task depends on its applied contracts and
review results.
