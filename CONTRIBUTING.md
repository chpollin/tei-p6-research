# Contributing

Read `README.md` for the project overview, `knowledge/project.md` for the
charter, `knowledge/architecture.md` for the repository structure and
`knowledge/state.md` before beginning work. A registered source or planned
artifact may not yet exist locally.

## Choose the contribution path

| Contribution | Primary location | Governing document |
|---|---|---|
| source registration or acquisition | `sources/`, `corpus/` | `knowledge/data.md` and `knowledge/operations.md` § Acquire |
| source representation or research finding | numbered evidence chain | `knowledge/schema.md` and `knowledge/operations.md` |
| P6 hypothesis or design experiment | `knowledge/text-model.md`, `knowledge/p6-architecture.md`, `knowledge/experiments.md` and explicitly contracted experiment paths | `knowledge/p6-evaluation.md` and `knowledge/operations.md` § Analyze |
| validator, collector or build change | `tools/`, `tests/` | `knowledge/testing.md` |
| navigation or project documentation | root files and `knowledge/` | `knowledge/INDEX.md` and `knowledge/architecture.md` |

A description of P5 requires source support. A P6 recommendation is a project
judgment whose premises, alternatives and tests must be available for review.
A question about text identity or interpretation need not begin with a claimed
P5 defect. Name its theoretical or practical motivation, distinguish sourced
requirements from project assumptions, and specify a case that could refute
the proposal. Define a pilot through a bounded question and explicit
exclusions. Claims of official support must name and date the official
process record.

## Rules that bind every contribution

The authority chain, the treatment of acquired content as untrusted data, the
rights and publication boundary, the roles and the shape of a delegated work
package are in `knowledge/governance.md`. The statuses `grounded`,
`validated` and `verified`, the review that permits each of them and the rule
that no contributor or agent assigns `verified` are in
`knowledge/verification.md`. The style of every text is the style sheet in
`knowledge/specification.md`.

Editorial and argument review can improve definitions, examples, scope and
clarity. It is separate from the recorded source-support procedure. If a
review changes a core statement or its grounding, rerun the required checks.
Unchanged source claims acquire no new authority from a prose review.

## Before proposing a change

Run the completion gate in `knowledge/testing.md` for the scope of the change,
regenerate changed generated files with their documented builder, and record
volatile progress only in `knowledge/state.md` or a run manifest. A new
artifact type, status, anchor form or bypass layer requires a recorded
architecture decision before implementation, and durable decisions are
appended to `knowledge/journal.md` without rewriting earlier entries.
