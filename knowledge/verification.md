---
title: Verification
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
related: [INDEX, operations, schema, testing, governance, state, journal]
---

# Verification

This document holds the adversarial checking of the project's own claims.
Validation in [[knowledge/operations]] establishes deterministic
conformance. Everything beyond that, the machine review of source support,
its independence, the human verification, the premise rule for proposals
and the counterevidence search, is defined here. Together with validation,
machine review permits `validated`. Only human verification permits
`verified`.

## Machine review

Machine review judges source support for each passage and statement pair.
Its fixed verdicts are **fully supports**, **partially supports**,
**overreaches**, **contradicts** and **not in the text**. Only *fully
supports* passes. Together with validation, this permits `validated` status
and no higher.

Anti-anchoring is mandatory. The reviewer sees the source location and the
bare statement, without the producing agent's reasoning, its Support prose or
its anchors. A document pair contains the anchored block and heading path, a
publication pair the quotation, a data pair the computation and its result.
Each is paired only with the statement being judged. `tools/review.py` cuts
these pairs deterministically and builds one prompt per pair from the
skeleton below.

> You are an adversarial reviewer. Below are a source passage and a statement
> that claims to be supported by it. Your task is to refute the statement.
> Judge only whether this passage supports this statement. Answer with exactly
> one verdict: fully supports | partially supports | overreaches | contradicts
> | not in the text. Then give one sentence of justification.
>
> PASSAGE: {source location, with its heading path}
> STATEMENT: {statement}

The reviewer must add a line when the statement displaces the passage's
subject. For a self-report, *fully supports* applies when the statement
attributes the claim to the source, while asserting the claimed achievement
itself is *overreaches*. For a state report, the statement must retain the
state and date shown by the source, while extending that observation into an
unqualified property of the object is *overreaches*. Examples include
restored objects, dated inventories and plans. The assertion review prompt
in [[knowledge/operations]] applies the same verdicts to an assertion and the
distillate statement it claims as support.

Record `checked.machine-review: <date>` on a document only when every one of
its pairs came back *fully supports*. A failed verdict requires rework.
Narrow the assertion or replace the unsupported anchor with one that carries
the claim, then review the changed pair again. Record systematic failure
patterns in [[knowledge/journal]].

## Review protocol and audit records

A review runs in a fresh context. The prompts are emitted unmodified by
`tools/review.py` or by the pilot runner, each prompt carries its SHA-256,
and every verdict is bound to that hash together with reviewer attribution,
the verdict from the fixed vocabulary and one sentence of reasoning. The
audit records of one run live under `workbench/reviews/<run-id>/` as
`pairs.jsonl` and `verdicts.jsonl` with a README that names the scope. They
are records and never sources or grounding targets.

A changed passage, a changed claim or a reused verdict invalidates the
review. `check_review_records` in `tools/review.py` holds the stored pairs
against the pairs the vault cuts today and the verdicts against both. An
acceptance runner rejects changed prompts, incomplete coverage, duplicate or
unknown verdicts, missing reasoning and any verdict other than *fully
supports*. Earlier rounds, including non-passing ones, stay in the run
directory as `*-round1.jsonl` so that a correction remains inspectable.
Completing the prompt context with mechanically recovered source identity,
locator or XML ancestor labels is legitimate, because it changes neither the
immutable representation nor the claim. A changed claim needs new prompts
and a fresh review, and old verdicts do not apply to it.

`python tools/check_wave1_sources.py . --review-only` and
`python tools/check_text_identity_pilot.py` check the current scope, the
unmodified canonical prompts and the passing verdict hashes of the recorded
runs without local raw data.

## Independence

A review is independent when three conditions hold. The reviewer comes from
a different model family than the producer, it works in a fresh context, and
it has no access to the author's rationale. A review that meets the second
and third condition with the same model family is recorded as a limitation
in the run's README and in [[knowledge/state]], because independence of
context does not imply independence of model errors. [[knowledge/governance]]
assigns adversarial reading to Fable, and where the producer was Fable the
reviewer comes from another family.

## Human verification

The human verification role named in [[knowledge/specification]], the
project owner or an explicitly designated TEI domain expert, judges whether
grounding holds as evidence. Only this role may establish `verified`. Machine
checks prepare the material without replacing that judgment.

Verification runs as a stratified sample per chapter. The strata are the
assertions the chapter cites, grouped by source type and by topic, and the
quota per stratum is recorded in [[knowledge/journal]] before the sample is
drawn. The role verifies the prepared pairs of the sample passage by passage
and records `checked.verification: <date>` by or on behalf of the verifying
role. A failed pair returns its assertion to rework and voids the sample of
its stratum. Human acceptance of an experiment, recorded through the items in
[[knowledge/experiments]], is a separate decision from the verification of a
grounding relation.

## Premises of a proposal

A premise of the Proposal for TEI P6, and of any design requirement, rests on
`validated` assertions. A `grounded` assertion may be cited while a chapter
is being written, but the chapter cannot reach `validated` and no design
requirement can be derived from the assertion until it has passed machine
review. A recommendation remains a posit even when its premises are
verified.

## Counterevidence search

Before an assertion supports a design requirement, a counterevidence search
runs and is recorded. The search names the topic map, the sources or queries
consulted and the result. A source that contradicts the assertion produces a
second assertion, both marked `contested` and linked reciprocally through
`contested-with`. A search without a finding is recorded with its date under
the open questions of the topic map, so that a later reader can see what was
looked for. A requirement that rests on an assertion without a recorded
counterevidence search enters output as a posit.

## Status discipline

`grounded` → (validation and machine review passed) → `validated` →
(verification passed) → `verified`. Assertion building or review may set
`contested` when sources conflict, and only verification resolves it. An
artifact's status is the minimum of its anchors' states, and no check may
assign a status above its authority.
