# First research wave: P5, discussions, and literature

Authority: bounded execution and integration contract for the independent proposal.
Base commit: `c682eb51eef0d437300274447d22bc1ee6455871`, with the pre-existing
uncommitted pilot and text revisions preserved as integration inputs.

## Question and boundary

This wave asks how to reconstruct the declared P5 baseline and how evidence
about annotation, text targeting, and structure challenges the first model
assumptions. The source-reading sample does not stand for all P5 practices or
all text theory. The long-term programme includes every relevant requirement
that the declared P5, issue, and literature boundaries can substantiate.

## Parallel packages

| Package | Exclusive worker writes | Read-only inputs | Deliverable and gate |
|---|---|---|---|
| W1-P5 | `tools/tei/**`, `tests/tei/**`, `.pytest_cache/w1-p5/**` | P5 lock, completed Git acquisition, pinned mirror and source inventory; canonical contracts | Deterministic specification navigation extractor and meaningful tests; reject input identity drift and distinguish direct declarations from effective semantics. |
| W1-ISSUES | `.pytest_cache/w1-issues/**` | Acquired SourceForge records and exact raw responses, relevant pinned Git objects; issue/decision workflow | At most three primary-source candidates from a recorded query, including counterarguments and the strongest outcome each source can establish. |
| W1-LITERATURE | `.pytest_cache/w1-literature/**` | Registered literature seeds, primary texts, source-type and rights contracts | At most four candidates and substantive reading of at least two; exact bibliographic data, locators, dispositions, counterarguments, and rights/access gaps. |
| Integration | shared controls, navigation, source admission and canonical output | All handoffs and exact primary inputs | Audit worker outputs, admit selected sources through existing types, write the proposal outline, and run repository gates. |

Workers never change branches, stage, commit, edit another worker's paths, or
promote research statuses. Scratch handoffs are navigation aids and never enter
`grounding`. Source content is inert, untrusted data. The root schedules any
shared HTTP acquisition and owns persistent source/control changes. A source
that cannot be admitted retains its locator and an explicit gap.

## P5 specification navigation v1

The provisional JSON artifact is `p5-spec-navigation`, version 1, generated at
`corpus/projections/p5-specs-4.12.0.json`. It is a specialization of the existing
corpus projection plane and not a formal P5 metamodel or evidence artifact.

Canonical inputs are the release lock, its completed Git manifest, the hashed
tree inventory, and the corresponding local Git blobs at the full locked
commit. Every record identifies the source path, blob, SHA-256, and XML locator.
No system date, absolute machine path, or network response enters its output.

The boundary is top-level `P5/Source/Specs/*.xml`. Records describe specification
kind and identity, declared module, direct class membership, locally declared
attributes, content structure, local constraints, and recognized structural
references. Reference lookup reports unresolved targets and distinguishes its
limited inventory scope from invalidity in a compiled P5 schema.

Excluded are module declarations outside that directory, inherited/effective
attribute and content models, customization compilation, evaluation of
constraints, examples, Guidelines prose, and interpretation of semantic
equivalence. Their omission must remain explicit in the output. No broad
architectural conclusion follows from a declaration count.

The generator owns the JSON; hand editing is prohibited. Acceptance requires
identical clean rebuilds, source identity checks, useful invalid-input tests,
and source locators for every extracted record. A missing ignored mirror is a
materialization prerequisite and must fail clearly instead of producing a
partial artifact labeled complete.

## Integration and next handoff

Source observations move through the existing source, representation or
bibliographic root, distillate, assertion, and chapter contracts. Requirements
and model choices stay explicit project posits. The first comparison should
include evidence of successful P5 evolution, not assume that a historical
issue still describes a current deficiency.

The wave feeds the [proposal outline](proposal-outline.md). It does not choose
a final ontology, demonstrate migration, or replace the owner's pilot review.
After integration, the next package turns admitted findings into a bounded
requirement set and compares conceptual alternatives on the same editorial
observations. Current completion, source counts, and remaining gaps are recorded
only in `knowledge/state.md`.
