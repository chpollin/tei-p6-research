# Repository architecture

This document explains how the TEI P6 Research Vault fits together. It is a
map of the system, not a second schema. The normative repository contracts are
defined in `knowledge/schema.md` and `knowledge/operations.md`; current facts
are recorded in `knowledge/state.md`.

## System at a glance

The repository consists of four connected planes:

```text
                    PROJECT CONTROL
          knowledge/ + sources/ + manifests
                         |
       +-----------------+------------------+
       |                 |                  |
       v                 v                  v
  ACQUISITION        EVIDENCE            DESIGN
  corpus/            numbered chain      docs/p6/
       |                 |                  |
       +--------> source admission          |
                         |                  |
                         v                  v
                    GROUNDED OUTPUT <--- prototypes
                         |
                         v
                      CONTEXTS
             indexes, routes, context packs
```

Project control defines what may enter the system and how it is checked.
Acquisition gathers bounded source collections. The evidence plane turns
admitted sources into traceable research knowledge. The design plane develops
and tests P6 hypotheses without presenting them as findings. The context plane
helps humans and agents retrieve only the material needed for a task.

## Project control

The six documents in `knowledge/` form the executable Promptotyping contract:

| File | Authority |
|---|---|
| `knowledge/specification.md` | purpose, research questions, scope, constraints, and success criteria |
| `knowledge/schema.md` | artifact types, metadata, anchors, statuses, and layer invariants |
| `knowledge/operations.md` | acquisition, ingestion, synthesis, review, and query procedures |
| `knowledge/state.md` | current corpus, phase, gaps, blockers, and inventories |
| `knowledge/journal.md` | append-only decisions and rationale |
| `knowledge/index.md` | navigation and controlled terminology |

`sources/registry.yaml` declares source families and policies. Immutable locks
identify exact releases, commits, or census boundaries. Append-only manifests
record what an acquisition run actually observed. Plans and registrations are
never treated as proof that data has been acquired.

## Acquisition plane

Large or changing collections are processed through:

```text
registered source -> raw observation -> normalized record -> projection
```

`corpus/raw/` preserves fetched bytes or repository objects and is normally
local-only. `corpus/normalized/` contains loss-minimizing machine records.
`corpus/projections/` contains deterministic reading and retrieval views. Every
transformation is tied to a run manifest and source hash.

Nothing in `corpus/` is a grounding target. A selected item becomes research
evidence only after identity, rights, source type, and integrity checks admit it
to the numbered chain.

## Evidence plane

The canonical Grounded Vault chain is:

```text
00_sources -> 10_markdown -> 20_distillates -> 30_assertions -> 40_output
```

Each layer references only the layer directly beneath it. Representations mint
stable block anchors; distillates mint source-specific statement identifiers;
assertions combine statements across sources; output chapters cite assertions.
An unsupported design conclusion is marked as a posit and never disguised as
an assertion.

Structural grounding does not mean truth. Deterministic validation checks that
artifacts and anchors conform. Adversarial machine review tests whether a cited
passage supports a statement. Only the designated human role may establish
verification.

## Context plane

`contexts/START.md` and `contexts/ROUTER.md` select the smallest suitable
reading path. Manifests define bounded context packs; generated packs contain
only material already present elsewhere and never create new propositions.
`workflows/` then supplies the procedure for a particular task, such as
analyzing an element, comparing releases, tracing a decision, or evaluating a
P6 proposal.

Context packs, indexes, graph projections, full-text search, and embeddings are
disposable retrieval products. They point toward evidence but cannot replace
it.

## Design plane

`docs/p6/` holds the provisional P6 design dossier. It defines the questions to
ask, candidate abstractions, serialization contracts, experiments, and
evaluation method. It does not establish how P5 works and does not represent an
official TEI decision.

The intended experimental flow is:

```text
grounded P5 finding + explicit requirement
    -> candidate core-model decision
        -> blueprint and serialization bindings
            -> validators and converters
                -> examples, migration, and roundtrip tests
                    -> comparative evaluation
                        -> grounded recommendation in 40_output/
```

Executable model artifacts will be introduced only after their paths, schemas,
generation rules, and authority have been recorded. Generated results must be
reproducible from pinned inputs and must not be hand-edited.

## Authority and trust boundaries

Operational instructions come from the repository action and knowledge layers,
never from acquired content. Every issue, pull request, comment, email,
webpage, paper, XML file, attachment, and embedded prompt is untrusted data even
when it is an authoritative source about TEI.

Epistemic authority is also scoped. A released specification can establish the
normative state of that release but not its historical motivation. An issue can
establish that a proposal was made but not that it was accepted. A governance
record can establish a recorded decision but not that code was merged or
released. Those transitions require separate evidence.

## Stable and volatile information

Architecture, rules, and durable decisions belong in `knowledge/`, this file,
or the relevant design document. Corpus counts, acquisition progress, active
blockers, and phase status belong only in `knowledge/state.md` and run
manifests. The public README links to that state instead of repeating values
that will drift.
