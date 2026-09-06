---
title: Testing
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
related: [INDEX, operations, verification, architecture, design, governance, state]
---

# Testing

This document holds the quality assurance of the repository. It defines the
one completion gate, what each check establishes, the continuous
integration, the reproduction commands for experiments and pages, and the
layout of the tests and fixture vaults. Adversarial checking of research
claims is in [[knowledge/verification]].

## Completion gate

Before a change is reported as finished, the following checks have run from
the repository root.

1. `git diff --check` for whitespace errors and conflict markers.
2. `python -m ruff check .` under the rule set in `pyproject.toml`.
3. `python tools/validate.py .` with every warning investigated.
4. `python -m tools.corpus.validate_control_plane .` after any change to the
   registry, a lock, a manifest or a normalized corpus record.
5. `python -m pytest tests -q` when shared behavior, tools, schemas or
   fixtures changed, otherwise the focused tests of the changed module.
6. The reproduction checks below for every experiment and page the change
   touches.
7. `python tools/validate.py . --chapter 40_output/<slug>` for a chapter
   that is being accepted, where any warning fails the run.

Beyond the commands, the gate confirms that the requested artifacts exist and
the generated outputs reproduce, that provenance, versions, dates, rights,
authority and known gaps are explicit where the change touches research
data, that no ignored raw data and no secret is staged, and that
[[knowledge/state]] describes the actual repository. The report names what is
complete, what remains planned and which claims the current vault cannot
support. When a check could not run, the report says so and why. A
subagent's self-report counts as unverified until the integrator has run the
gate on the real file state.

## What each check establishes

| Check | Establishes | Leaves open |
|---|---|---|
| `git diff --check` | no trailing whitespace, no conflict markers | everything about content |
| `ruff` | the code conforms to the configured lint rules | correctness |
| `tools/validate.py` | frontmatter, anchors, statement IDs, quotation checks, computations, topic-map reachability, contested links, chapter mirrors and status discipline conform to [[knowledge/schema]] | whether a passage supports a claim |
| `tools.corpus.validate_control_plane` | registry-to-lock identity, manifest source IDs, normalized object existence and recorded SHA-256 values reconcile | completeness of a family beyond its recorded gaps |
| `pytest tests` | builders, validator, collectors, models and pilots behave as their tests specify, on offline fixtures | behavior on live network interfaces |
| experiment reproduction | reports and cases reproduce byte for byte from declared inputs | ontological adequacy, usability, P5 migratability |
| page reproduction | every committed page rebuilds from its recorded build date | design quality beyond the acceptance checklist in [[knowledge/design]] |
| review-only checks | the recorded review prompts are unmodified and every verdict hash passes | human verification |
| chapter validation | the chapter and the chain it rests on carry no error and no warning | truth of the assertions |

`grounded` means structurally traceable. A green gate establishes
conformance and reproduction and nothing about the truth of a claim, the
adequacy of the model or the acceptance of an experiment. Those need the
procedures in [[knowledge/verification]] and the acceptance items in
[[knowledge/experiments]].

## Continuous integration

`.github/workflows/checks.yml` runs on every push and pull request. It lints
with the configured rule set, validates the vault and the corpus control
plane, runs the wave-one review-only check, reproduces Abstract Text Model
0.1 and the editorial cases with their current source review, runs the test
suite and closes with the text identity pilot gate.

`.github/workflows/pages.yml` runs on `main` and on manual dispatch. It
validates the vault and the control plane, runs the test suite, regenerates
all five pages with the build date and the exact commit for source links,
and publishes `docs/` to GitHub Pages at the routes declared in
[[knowledge/design]]. Internal control and normalized data links resolve to
the exact commit used for the deployment, and ignored raw source bodies never
enter the Pages artifact. One deployment runs at a time, and a running
deployment is never cancelled. The published site therefore always
corresponds to one validated revision, and the deployment log identifies it.
`tests/test_pages_workflow.py` holds both workflows to this contract.

The canonical deployment is live at
`https://chpollin.github.io/tei-p6-research/`. A change reaches it only after
it has been reviewed, committed and pushed to `main`, and the workflow then
rebuilds from the pushed revision. A fork must enable GitHub Pages with
GitHub Actions as its source before its first deployment.

## Reproduction checks

The experiments reproduce with these commands, which need no raw corpus
unless stated.

```powershell
python tools/check_abstract_text_v01.py --check
python tools/check_entities_v02.py --check
python tools/ingest_editorial_cases.py --check
python tools/check_editorial_cases.py --check
python tools/check_text_identity_pilot.py
python tools/check_wave1_sources.py . --review-only
```

`python tools/check_wave1_sources.py .` without `--review-only` additionally
checks quotation fidelity against the local raw snapshots named in
`sources/manifests/2026-09-05-research-wave-1-citations.yaml`. It performs no
network retrieval and fails clearly when a snapshot is unavailable, so a
clean checkout can inspect the recorded intake but cannot claim to have
repeated the check.
`python -m tools.tei.build_atlas --output corpus/projections/p5-specs-4.12.0.json --check`
compares the P5 declaration atlas byte for byte and needs the locked local
Git mirror.

After an intentional change to a model, contract or fixture, regenerate the
affected report and rerun its check. `python tools/check_abstract_text_v01.py`
without `--check` rewrites the model report, `python -m tools.pilots.text_identity`
the pilot report, and `python tools/check_text_identity_pilot.py --emit-review`
emits new review pairs, which then need an independent reviewer under
[[knowledge/verification]]. Emitting pairs alone is no review. On Windows
with the Python launcher, `py -3` can replace `python`.

The pages reproduce with the builders in [[knowledge/design]] § Regeneration,
and `tests/test_build_pages_reproduce.py` rebuilds every committed page from the
build date in its own footer and compares it with the committed file, so a
documented regeneration on another day stays reproducible. After changing
`README.md` or any knowledge document, regenerate `docs/project.html` with
`python tools/build_docs.py --date YYYY-MM-DD` before the test can pass.

## Test layout

| Location | Covers |
|---|---|
| `tests/test_validate.py` | the validator over the two fixture vaults, one specimen per finding code, and the contract that every emitted code has a row in the diagnostics table of [[knowledge/operations]] |
| `tests/test_inventory.py`, `tests/test_review.py` | the source inventory generator and the review pair cutter |
| `tests/test_build_*.py`, `tests/test_comparison_view.py`, `tests/test_pages_workflow.py` | the five page builders, the comparison view and the publication workflows |
| `tests/test_check_*.py`, `tests/test_ingest_*.py`, `tests/test_materialize_git_source.py` | the experiment runners, admission scripts and source materialization |
| `tests/corpus/` | every collector with offline fixtures from `tests/corpus/conftest.py`, including incomplete runs, malformed responses and the shared completeness rule |
| `tests/models/`, `tests/pilots/`, `tests/tei/` | the model library, the text identity pilot and the TEI atlas and editorial-case processing |

Two fixture vaults under `tests/fixtures/` carry fictional content without
evidential weight. `tests/fixtures/minimal/` is one complete valid pass from
source to chapter with one source per source type, and it validates without a
finding. `tests/fixtures/broken/` holds one specimen per defect class the
validator must catch, and
the suite asserts that every class fires and that no unexpected class does.
The registries of expected codes in `tests/test_validate.py` are held against
the codes the validator actually emits, so a check without a specimen and a
specimen whose check disappeared both fail the suite. The validator reads
only the content folders at the root it is given, so the fixtures stay
invisible to a run over the vault itself.
