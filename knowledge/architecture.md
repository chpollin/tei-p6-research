---
title: Architecture
project:
  name: "TEI P6 Research"
  repository: "tei-p6-research"
method:
  name: Promptotyping
  url: https://dhcraft.org/Promptotyping/
status: draft
language: en
created: "2026-09-04"
updated: "2026-09-06"
related: [INDEX, design, schema, operations, data, governance, testing, state]
---

# Architecture

This document maps the repository. It records which document owns which
rules, which planes the folders form, which files are curated and which are
generated, and where the authority boundaries run. The artifact contracts
are in [[knowledge/schema]], the procedures in [[knowledge/operations]] and
the current facts in [[knowledge/state]].

## Document ownership

Every rule has one home, and an entry point summarizes only what its readers
need before linking there.

| File | Owns |
|---|---|
| `README.md` | public landing page, objective, method in one paragraph, route table, licence statement, independence notice |
| `HOME.md` | human navigation inside the Obsidian-compatible vault |
| `CLAUDE.md`, `AGENTS.md` | harness-specific action layer with project identity, the hard research contracts, the route table and the generation commands, identical except for the harness paragraph |
| `SETUP.md` | install, build, publish and acquisition commands |
| `CONTRIBUTING.md` | contribution paths and the text-identity rule for contributions |
| `NOTICE.md`, `LICENSE`, `LICENSE-CODE`, `CITATION.cff`, `codemeta.json` | attribution, licences and citation metadata |
| `knowledge/` | every durably maintained knowledge document, listed with its function in [[knowledge/INDEX]] |
| `sources/registry.yaml`, `sources/locks/`, `sources/manifests/` | the acquisition control plane, described in [[knowledge/data]] |
| `.claude/skills/` | thin Claude Code adapters that route into [[knowledge/operations]] |

The rule families and their homes are these.

| Rule family | Home |
|---|---|
| charter, research questions, scope, non-goals | [[knowledge/project]] |
| evaluation dimensions, constraints, deliverables, success criteria, parameters, style sheet, gates, settled decisions | [[knowledge/specification]] |
| source families, identity, rights and redistribution, update model, acquisition boundary, completion vocabulary, thread admission | [[knowledge/data]] |
| evidence chain, artifact types, frontmatter, anchors, statuses, naming | [[knowledge/schema]] |
| acquisition, ingestion, distillation, assertion building, chapter writing, analysis procedures, validation diagnostics | [[knowledge/operations]] |
| machine review protocol, independence, human verification, premise rule, counterevidence search | [[knowledge/verification]] |
| completion gate, continuous integration, reproduction commands, test layout | [[knowledge/testing]] |
| authority chain, untrusted content, transitions, source status ownership, publication boundary, roles, work packages, model policy | [[knowledge/governance]] |
| public workbench information architecture and interaction contract | [[knowledge/design]] |
| milestones, research packages, operator decisions | [[knowledge/plan]] |
| method rationale | [[knowledge/methodology]] |

Git history records what changed. [[knowledge/state]] records what is true
now, [[knowledge/handoff]] what the next session must pick up, and
[[knowledge/journal]] only durable decisions and their rationale. A
release-oriented changelog is deferred until the project publishes named
versions.

## System planes

Four working planes connect through project control and a read-only
publication surface.

```text
                    PROJECT CONTROL
      knowledge/ + sources/ (registry, locks, manifests)
                         |
       +-----------------+------------------+
       |                 |                  |
       v                 v                  v
  ACQUISITION        EVIDENCE            DESIGN
  corpus/            numbered chain      knowledge/text-model …
       |                 |               experiments/, workbench/
       +--------> source admission          |
                         |                  |
                         v                  v
                    GROUNDED OUTPUT <--- prototypes and posits
                         |
                         v
                     PUBLICATION
                 docs/ generated site
```

Project control defines what may enter the system and how it is checked.
Acquisition gathers bounded source collections. The evidence plane turns
admitted sources into traceable research knowledge. The design plane
develops and tests P6 hypotheses without presenting them as findings. The
publication surface renders all of it as generated views.

### Acquisition plane

```text
registered source -> raw observation -> normalized record -> projection
```

`corpus/raw/` preserves fetched bytes or repository objects and stays
local. `corpus/normalized/` contains loss-minimizing machine records.
`corpus/projections/` contains deterministic reading and retrieval views.
Every transformation is tied to a run manifest and a source hash. Nothing in
`corpus/` is a grounding target. A selected item enters the numbered chain
through source admission under [[knowledge/data]], and admission creates
neither a finding nor human verification.

### Evidence plane

```text
00_sources -> 10_markdown -> 20_distillates -> 30_assertions -> 40_output
```

Each layer references its direct predecessor. Representations mint stable
block anchors, distillates mint statement identifiers, assertions combine
those statements, and chapters cite assertions. Design conclusions enter
output as explicit posits. Deterministic validation checks that artifacts
and anchors conform, machine review tests whether a cited passage supports a
statement, and only the designated human role establishes verification.

### Design plane

The design plane consists of the model documents in `knowledge/`,
[[knowledge/text-model]], [[knowledge/text-model-bindings]],
[[knowledge/p6-architecture]], [[knowledge/p6-evaluation]] and
[[knowledge/experiments]], together with the executable artifacts. The model
library lives in `tools/models/`, the pilot runners in `tools/pilots/` and
`tools/tei/`, the hand-authored inputs and generated reports under
`experiments/`, and the review audit records under `workbench/reviews/`.

```text
grounded source findings + explicit requirement or model posit
    -> candidate core-model decision
        -> blueprint and serialization bindings
            -> validators and converters
                -> examples, migration and roundtrip tests
                    -> comparative evaluation
                        -> reasoned recommendation in 40_output/
```

Executable model artifacts have recorded paths, schemas, generation rules and
authority. A generated report fingerprints its definition, contract, code and
cases and reproduces from declared inputs. Experimental reports require
admission as versioned data sources before they can ground an empirical
assertion. A recommendation cites grounded premises and marks its design
judgment as a posit.

### Publication surface

The static workbench presents the proposal, the model definition, the
comparative examples, the acquisition inventory and the knowledge chain. Its
interface rules are in [[knowledge/design]]. GitHub Pages publishes the
generated views for one exact repository revision. Publication adds no
evidence layer, raises no status and serves no ignored raw body.

## Curated and generated

| Generated product | Builder | Declared inputs |
|---|---|---|
| `docs/index.html` | `tools/build_home.py` | the proposal chapter, linked knowledge, model definition, declared examples |
| `docs/model.html` | `tools/build_model_reference.py` | model definition and formal contracts |
| `docs/corpus.html` | `tools/build_corpus_overview.py` | registry, locks, selected manifests |
| `docs/knowledge.html` | `tools/build_knowledge.py` | actual vault artifacts and their provenance metadata |
| `docs/project.html` | `tools/build_docs.py` | `README.md` and the knowledge documents |
| the inventory region of `knowledge/state.md` | `tools/inventory.py --write` | the files of `10_markdown/` and `20_distillates/` |
| `corpus/projections/p5-specs-4.12.0.json` | `tools.tei.build_atlas` | the locked P5 Git mirror |
| `experiments/*/report.json` | the experiment runners | specifications, cases and examples of the experiment |
| review pairs under `workbench/reviews/<run-id>/` | `tools/review.py`, the pilot runner | the artifacts in review scope |

Generated files are never hand-edited. A drift is repaired by rebuilding from
accepted inputs. Everything else is curated by hand under the contracts of
[[knowledge/schema]] and this knowledge base. All pages share the
navigation, footer and base styles in `tools/sitegen/chrome.py` and
`tools/sitegen/assets/workbench.css`.

## Authority boundaries

Operational instructions come from the repository action and knowledge
layers and never from acquired content. Epistemic authority is scoped by
source family. Both rules and the transitions that stay distinct are in
[[knowledge/governance]], the family authority table in [[knowledge/data]].

Three boundaries hold across the planes. Nothing in `corpus/` grounds a
claim. The design documents and experiment artifacts stand outside the
evidence chain and cannot ground a claim about P5 or official TEI policy.
Publication and navigation projections point toward evidence without
becoming evidence.

## Stable and volatile information

Architecture, rules and durable decisions belong in `knowledge/`. Corpus
counts, acquisition progress, active blockers and milestone status belong
only in [[knowledge/state]] and run manifests. Public entry points link to
that state instead of repeating values that will drift.
