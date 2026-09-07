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
updated: "2026-09-07"
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
   For Guidelines admissions, distillates, the coverage projection or its
   converter, also run `python -m tools.ingest_guidelines --check`. This checks
   finite source coverage, preserved identities and current processing facts;
   it grants no scholarly status.
   Navigation changes additionally require
   `python -m tools.build_guidelines_navigation --check`. For the Text and
   Document Structures source admission, run
   `python -m tools.ingest_text_structures --check`. Export changes require
   a complete export to a temporary directory followed by its `--check`.
5. `python -m pytest tests -q` when shared behavior, tools, schemas or
   fixtures changed, otherwise the focused tests of the changed module.
6. The reproduction checks below for every experiment and page the change
   touches.
   Ontology changes additionally require `python tools/check_ontology.py --check`
   and `python -m pytest tests/test_check_ontology.py -q`. Changes to the
   illustrative model examples require
   `python -m pytest tests/test_model_design_examples.py -q`.
   HSA case changes require `python tools/build_hsa_case.py --check` and
   `python -m pytest tests/test_build_hsa_case.py tests/test_hsa_bindings.py -q`.
   A full suite already run in step 5 includes these tests; do not repeat them.
   These check the fixed
   snapshot and its declared case binding, including preservation-only fields;
   they do not establish general P5 migration or HSA-ODD conformance.
   The semantic and preservation components, their exact union and both
   binding versions follow [[knowledge/hsa-profile]].
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
| Guidelines navigation reproduction | rule-based topic suggestions and declaration links reproduce from tracked inputs | scholarly classification or source support |
| Guidelines XML export and verification | every admitted XML byte and its original Git path survive a mirror-free export; the export inventory reconciles | images, generated HTML, schemas and scientific interpretation |
| Text structures admission check | the admitted overlap test and its representation reproduce without ignored originals | source-support review of the twelve-source research run |
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

Both workflows install the declared development dependencies from `uv.lock`
and run project commands through `uv run --locked`. RDFLib is pinned for the
ontology and example graph checks. These checks compare explicit graphs and
structural policy; they do not perform OWL reasoning. The RDFLib 7.6 JSON-LD
parser emits an upstream `ConjunctiveGraph` deprecation warning without
changing the compared graph.

`.github/workflows/checks.yml` runs on every push and pull request. It lints
with the configured rule set, validates the vault and the corpus control
plane, runs the wave-one review-only check, reproduces Abstract Text Model
0.1 and the editorial cases with their current source review, runs the test
suite and closes with the text identity pilot gate.

The completion gate and each workflow run the full test suite once.
`tools/check_text_identity_pilot.py` checks only its admitted sources,
bounded source-support review and report reproduction. It starts neither
pytest nor repository-wide validation. Those checks belong to the completion
gate above. The pilot report fingerprints its own contract section; changes
to unrelated experiments do not invalidate it.

Both workflows also reproduce the Guidelines navigation and the Text and
Document Structures admission, then export all 888 admitted Guidelines XML
sources into the runner's temporary directory and verify the result. These
checks need only tracked files and perform no acquisition. The temporary
export remains outside the published Pages artifact. The structure research
review checker is separate: its required independent verdicts remain open,
so it is not a mandatory CI gate and no passing review is implied.

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

The full English Guidelines intake and its coverage projections reproduce
with `python -m tools.ingest_guidelines --check`. It works in a clean checkout
without ignored source files, a raw release ZIP or the Git mirror. The
tracked representations contain the exact XML used for their checks.
`tests/test_ingest_guidelines.py` exercises that clean-checkout path, missing
and modified sources, literal DTD examples versus live declarations,
dependency boundaries, publication-member matching and escaped public
coverage links. Both CI and the Pages build run the intake check.

Navigation, the additional overlap test admission and the XML export use:

```powershell
uv run python -m tools.build_guidelines_navigation --check
uv run python -m tools.ingest_text_structures --check
uv run python -m tools.export_guidelines --output ../tei-p5-4.12.0-xml
uv run python -m tools.export_guidelines --output ../tei-p5-4.12.0-xml --check
```

Choose an export directory whose existing files are either absent or byte
identical. Export preserves the original upstream path layout and rejects
conflicting files, traversal and symlink destinations. Atomic publication
requires a filesystem supporting hardlinks. `tests/test_export_guidelines.py`
checks the complete export without a mirror, repeatability and failure cases.
The navigation builder uses the tracked declaration atlas; its check does
not regenerate that atlas from an unavailable Git mirror.

`python -m tools.check_text_structures` checks source and assertion review
records only after independent verdicts exist. Emitting its review pairs
with `--emit` establishes no source support. An unfinished review remains an
explicit research limitation even when all technical checks pass.

The experiments reproduce with these commands, which need no raw corpus
unless stated.

The text-identity support checker retains the original pilot's four assertions
and three distillates as its review boundary and follows their current
grounding dependencies. Changed dependencies or prompts require a new review.
Chapter 02 has a broader definition and is structurally checked separately.
Passing the pilot audit confers no support review on that expanded chapter.
The pilot checker does not run chapter validation as a side effect.

```powershell
python tools/check_abstract_text_v01.py --check
python tools/check_entities_v02.py --check
python -m tools.ingest_identity_evidence --check
python -m tools.check_identity_evidence --check
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
