# Repository architecture

This map records data flow and document ownership. The repository contracts
are defined in `knowledge/schema.md` and `knowledge/operations.md`.
Current facts are recorded in `knowledge/state.md`.

## Entry points and document ownership

| Entry point | Single responsibility |
|---|---|
| `README.md` | concise public landing page and route to the live workbench |
| `HOME.md` | human navigation inside the Obsidian-compatible vault |
| `AGENTS.md` / `CLAUDE.md` | thin tool-specific action layers that route into `knowledge/` |
| `SETUP.md` | local installation, generation, validation, and publication commands |
| `CONTRIBUTING.md` | contribution paths and review expectations |
| `PLAN.md` | stable phase sequence and exit gates, never current progress |
| `ARCHITECTURE.md` | system planes, data flow, authority, and document ownership |
| `EXPOSE.md` | one-page narrative description for scholarly communication |
| `knowledge/` | canonical project contract, rules, current state, and decisions |

Rules have one canonical definition. Entry points summarize only what their
readers need and link to that definition. Generated HTML pages in `docs/` are
products of their builders, not additional documentation sources.

Git history records what changed. `knowledge/state.md` records what is true
now, and `knowledge/journal.md` records only durable decisions and their
rationale. A release-oriented changelog will be introduced only when the
project starts publishing named versions.

## System at a glance

Four working planes connect through project controls and a read-only
publication surface.

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

## Publication surface

The static workbench presents the canonical proposal, model definition,
comparative examples, acquisition inventory, and knowledge chain. Its materials
page uses the registry, locks, and selected manifests. Its project page uses
the public overview and knowledge documents. GitHub Pages publishes the
generated views for one exact repository revision.

Publication does not add an evidence layer or raise any artifact's status. The
site excludes ignored raw source bodies and links acquisition records and
canonical knowledge for inspection. Interface rules live in
`knowledge/design.md`. Deployment state lives in `knowledge/state.md`.

## Project control

The seven documents in `knowledge/` define the Promptotyping contract.

| File | Authority |
|---|---|
| `knowledge/specification.md` | purpose, research questions, scope, constraints, and success criteria |
| `knowledge/design.md` | public research-workbench information architecture and interface contract |
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

Large or changing collections follow the acquisition chain.

```text
registered source -> raw observation -> normalized record -> projection
```

`corpus/raw/` preserves fetched bytes or repository objects and is normally
local-only. `corpus/normalized/` contains loss-minimizing machine records.
`corpus/projections/` contains deterministic reading and retrieval views. Every
transformation is tied to a run manifest and source hash.

Nothing in `corpus/` is a grounding target. A selected item enters the numbered
research chain after identity, rights, source type, and integrity checks.
Admission creates neither a research finding nor human verification.

## Evidence plane

Admitted sources enter the Grounded Vault chain.

```text
00_sources -> 10_markdown -> 20_distillates -> 30_assertions -> 40_output
```

Each layer references its direct predecessor. Representations mint stable
block anchors. Distillates mint source-specific statement identifiers.
Assertions combine those statements, and output chapters cite assertions.
Design conclusions enter output as explicit posits.

Structural grounding does not mean truth. Deterministic validation checks that
artifacts and anchors conform. Adversarial machine review tests whether a cited
passage supports a statement. Only the designated human role may establish
verification.

## Context plane

`contexts/START.md` and `contexts/ROUTER.md` select the smallest suitable
reading path. Manifests define bounded context packs. Generated packs contain
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

Design experiments connect requirements to comparative recommendations.

```text
grounded source findings + explicit requirement or model posit
    -> candidate core-model decision
        -> blueprint and serialization bindings
            -> validators and converters
                -> examples, migration, and roundtrip tests
                    -> comparative evaluation
                        -> reasoned recommendation in 40_output/
```

Experimental reports require admission as versioned data sources before they
can ground empirical assertions. A recommendation cites grounded premises and
marks its design judgment as a posit.

Executable model artifacts require recorded paths, schemas, generation rules,
and authority. The v0.1 contract uses `experiments/abstract_text_v01/spec.json`
and independently authored cases and examples, with the reference library in
`tools/models/` and the runner in `tools/check_abstract_text_v01.py`. Its generated
report fingerprints the definition, contract, code, and cases. Generated
results must reproduce from declared inputs and must not be hand-edited.
The full definition and exclusions are in
`docs/p6/abstract-text-model-v0.1.md`.

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
