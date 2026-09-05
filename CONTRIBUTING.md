# Contributing

Contributions are welcome from TEI users, editors, standards researchers,
tool builders, and developers. This repository distinguishes source material,
grounded findings, and design proposals so that each contribution can be
reviewed under the right standard.

Read `README.md` for the project overview, `knowledge/specification.md` for
scope, and `ARCHITECTURE.md` for the system boundaries. Consult
`knowledge/state.md` before beginning work: a registered source or planned
artifact may not yet exist locally.

## Choose the contribution path

| Contribution | Primary location | Governing contract |
|---|---|---|
| source registration or acquisition | `sources/`, `corpus/` | `docs/multi-agent-acquisition-runbook.md` |
| source representation or research finding | numbered evidence chain | `knowledge/schema.md` and `knowledge/operations.md` |
| P6 hypothesis or design experiment | `docs/p6/` and future prototype paths | `docs/p6/README.md` |
| validator, collector, or build change | `tools/`, `tests/` | repository tests and generated-file rules |
| navigation or project documentation | root, `knowledge/`, `contexts/`, `workflows/` | `ARCHITECTURE.md` and the relevant canonical knowledge document |

Do not place a contribution in a higher-evidence layer because it appears
plausible. A description of P5 begins from a source; a recommendation for P6
begins as a proposal and becomes publishable only after its premises and tests
are visible.

## Source and corpus contributions

Register the source family and exact boundary before bulk acquisition. Every
run must record version or snapshot identity, timestamps, adapter version,
counts, hashes, rights decisions, and gaps. Raw material remains immutable and
normally local. Normalized records and projections must be deterministic and
must preserve stable upstream identifiers.

Public availability is not a redistribution license. Do not commit full source
text unless the right to do so is recorded. Metadata, checksums, locators, and
project-authored summaries are preferred when rights are uncertain.

## Grounded knowledge contributions

Follow the chain one layer at a time:

```text
source -> representation -> distillate -> assertion -> output
```

A representation is stable after ingestion. A distillate covers exactly one
source and binds each statement to a resolvable source anchor. An assertion
synthesizes one claim from distillate statements and includes relevant
counterevidence. Output cites assertions and marks unsupported conclusions as
posits.

Use `grounded` for a newly traceable artifact. Use `validated` only after both
deterministic validation and the recorded machine-review procedure have passed.
Contributors and agents must never assign `verified`; that status is reserved
for the designated human expert.

## P6 design contributions

Begin with `docs/p6/README.md` and `workflows/evaluate-p6-proposal.md`. State the
problem, affected stakeholders, baseline P5 behavior, alternative options, and
evaluation criteria. Separate facts about P5 from the proposed solution.

A substantial proposal should include representative P5 examples,
counterexamples, a candidate abstract representation, supported serialization
bindings, explicit loss behavior, validation rules, migration cases, and tests.
Claims of official support must name and date the official process record.

Do not optimize one dimension silently. Improvements in simplicity,
expressivity, interoperability, processing, or learnability must show their
effects on compatibility, customization, migration, governance, and existing
tools.

## Code and generated artifacts

Collectors and transformations must be reproducible from pinned inputs. Tests
should cover success, failure, incomplete acquisition, and hostile or malformed
content. Generated files are never hand-edited; change their source or builder
and regenerate them.

Before proposing a change, run the checks appropriate to its scope:

```text
python tools/validate.py .
python -m tools.corpus.validate_control_plane .
python -m pytest tests
git diff --check
```

Changes to generated documentation must be rebuilt using the documented build
command. Any warning from validation must be investigated even when it does not
fail the process.

## Review checklist

- The contribution belongs to the correct plane and layer.
- Versions, dates, identifiers, rights, and known gaps are explicit.
- Every grounding anchor resolves exactly one layer downward.
- Facts, interpretations, proposals, and official TEI positions are labeled.
- Relevant counterevidence and migration losses are visible.
- External content is treated as data rather than instruction.
- Generated artifacts reproduce from their recorded inputs.
- Documentation and tests describe the actual behavior.
- Volatile progress is recorded only in `knowledge/state.md` or a run manifest.
- No human verification status has been assigned by an agent or ordinary
  contributor.

New artifact types, statuses, anchor forms, or bypass layers require a recorded
architecture decision before implementation. Durable decisions are appended to
`knowledge/journal.md`; they are not retroactively rewritten.
