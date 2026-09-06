# Project setup

This repository contains TEI P6 Research and its Grounded Vault evidence
system. This guide prepares a local environment; it is not a
template-substitution workflow.

## 1. Read the project contract

Before changing content or running acquisition:

1. read `README.md` for the public overview;
2. read `knowledge/index.md` and `knowledge/specification.md`;
3. read `knowledge/state.md` for the actual data and phase status;
4. use `AGENTS.md` for Codex or `CLAUDE.md` for Claude Code;
5. route a content task through `contexts/START.md` and
   `contexts/ROUTER.md`.

For research-frontend, About, or publication work, also read
`knowledge/design.md`.

Do not assume that a source named in `sources/registry.yaml` has already been
downloaded. A completed run manifest and matching local artifacts establish
that state.

## 2. Install local dependencies

Requirements:

- Git
- Python 3.11 or newer
- PyYAML
- pytest for the test suite and ruff for the linter
- GitHub CLI when authenticated GitHub acquisition or repository administration
  is required

With `uv`:

```powershell
uv sync
```

Without `uv`:

```powershell
python -m pip install pyyaml pytest ruff
```

Verify the scaffold:

```powershell
python tools/validate.py .
python -m pytest tests
```

Warnings such as `W-EMPTY` and `W-NO-OUTPUT` describe missing production
artifacts. Investigate and report them rather than hiding them; their current
applicability belongs in `knowledge/state.md`, not this setup guide.

## 3. Open as an Obsidian vault

Open the repository root as the vault. The committed `.obsidian/` configuration
uses core features only. Personal workspace state, caches, and installed
community plugins remain uncommitted.

Start at `HOME.md`. The repository continues to work as plain Markdown without
Obsidian.

## 4. Use GitHub and authenticated acquisition

The canonical public remote is
`https://github.com/chpollin/tei-p6-research`. A normal clone already configures
it as `origin`; verify the checkout with:

```powershell
git remote get-url origin
gh auth status
```

Run `gh auth login` only when authentication is absent and the task requires
GitHub API access or repository administration:

```powershell
gh auth login
```

Full GitHub corpus acquisition also requires authenticated read access. Tokens
stay in the GitHub credential store or environment; they never enter files,
commands recorded in manifests, logs, or context packs.

## 5. Understand storage boundaries

Normal Git contains code, contracts, registries, locks, manifests, checksums,
small rights-cleared fixtures, and curated knowledge artifacts.

The following remain ignored and local by default:

- Git mirrors and checkouts;
- raw API and web responses;
- third-party PDFs and attachments;
- mailing-list archives;
- unreviewed user-generated discussion text;
- caches, credentials, and temporary files.

Do not use `git add -f` to bypass these boundaries. If a reviewed original is
approved for versioning, the integrator adds a narrow per-file exception to
`.gitignore` so the policy change is visible in review. Rights-cleared material
is admitted explicitly according to `sources/README.md`,
`corpus/COMPLETENESS.md`, and `knowledge/operations.md`.

## 6. Acquire or admit material

Follow `docs/multi-agent-acquisition-runbook.md` for collector work and the
Acquire and Ingest sections of `knowledge/operations.md` for source admission.
Those documents own the fetch, identity, rights, reconciliation, and provenance
requirements; `knowledge/state.md` records which families are actually ready.

Production collection starts only after the relevant offline fixtures and
integration checks pass. Source registration or a local cache alone never
establishes acquisition.

## 7. Run a vertical research cycle

Before topic-scale distillation, take one rights-cleared source through the
canonical chain. Use `knowledge/operations.md` for the complete procedure and
`workflows/` for TEI-specific analysis routes; do not create a shortcut from
the acquisition corpus to a higher evidence layer.

Run after representation and distillate changes:

```powershell
python tools/inventory.py . --write
python tools/validate.py .
```

For one chapter acceptance:

```powershell
python tools/validate.py . --chapter 40_output/CHAPTER-SLUG.md
```

For the bounded text identity and annotation pilot:

```powershell
python tools/check_text_identity_pilot.py
```

On Windows with the Python launcher, `py -3` can replace `python`. The combined
gate checks source integrity, chapter provenance, current independent-review
coverage, experiment reproduction, and the full test suite. Human acceptance
uses `docs/p6/text-identity-pilot.md`; passing code does not approve an ontology.
After an intentional experiment or contract change, regenerate its report with
`python -m tools.pilots.text_identity`. Changed research claims require fresh
review via `python tools/check_text_identity_pilot.py --emit-review` and an
independent reviewer; generating pairs alone is not review.

For Abstract Text Model 0.1, the independent case gate needs no raw corpus:

```powershell
py -3 tools/check_abstract_text_v01.py --check
py -3 tools/check_abstract_text_v01.py --validate experiments/abstract_text_v01/examples/competing-readings.json
py -3 -m pytest tests/models tests/test_check_abstract_text_v01.py
```

The first command checks frozen expectations, all declared rule and operation
coverage, nonmutation, canonical reproduction, standalone examples, and exact
report reproduction. It fails if the report is missing or stale. After reviewing
an intentional model, contract, or fixture change, regenerate with
`py -3 tools/check_abstract_text_v01.py` and rerun `--check`. Input fingerprints
normalize checkout line endings; strings inside model instances remain exact.
The validation command prints machine-readable diagnostics and resolutions.
Use `docs/p6/abstract-text-model-v0.1.md` for the definitions and separate human
acceptance questions. A passing gate does not establish real P5 migration or
practical adequacy.

## 8. Regenerate documentation

The first research wave also provides two read-only reproduction checks:

```powershell
py -3 -m tools.tei.build_atlas --output corpus/projections/p5-specs-4.12.0.json --check
py -3 tools/check_wave1_sources.py .
py -3 tools/check_wave1_sources.py . --review-only
```

The atlas check requires the locked local TEI Git mirror. Omit `--check` to
regenerate the projection after an intentional generator or control-input
change. The quotation check requires the four local raw snapshots named in
`sources/manifests/2026-09-05-research-wave-1-citations.yaml`; it performs no
network retrieval and fails clearly when a snapshot is unavailable. A clean
checkout without ignored raw data can inspect the recorded intake but cannot
claim to have rerun quotation fidelity. Neither command assigns research status.

`--review-only` needs no ignored originals. It checks the current eight canonical
source-support prompts, exact dependency coverage, and their passing verdict
hashes. CI runs this check separately from the local raw-source quotation check.

After changing `README.md`, `docs/concept.md`, or knowledge documents consumed
by the site builder:

```powershell
python tools/build_docs.py --date YYYY-MM-DD
python tools/build_corpus_overview.py --date YYYY-MM-DD
python tools/build_home.py --date YYYY-MM-DD
python tools/build_knowledge.py --date YYYY-MM-DD
python tools/build_model_reference.py --date YYYY-MM-DD
```

Never hand-edit generated HTML. The home builder writes `docs/index.html`; the
project builder writes `docs/project.html`. Knowledge and Model builders write
`docs/knowledge.html` and `docs/model.html`. These paths are identical locally
and on GitHub Pages.
The home generator reads the complete canonical proposal in
`40_output/12-p6-design.md`, its source links, model definitions and examples.

## 9. Publish the research workbench

`.github/workflows/pages.yml` validates and regenerates the static site on
`main`, publishes the proposal home at the GitHub Pages root, the materials
overview at `corpus.html`, and the full project documentation at `project.html`.
The formal model reference is `model.html`; `knowledge.html` inventories the
actual Vault artifacts and exposes their precise provenance links.
Internal control and normalized
data links resolve to the exact GitHub commit used for the deployment; ignored
raw source bodies are never included in the Pages artifact.

The canonical deployment is live at
`https://chpollin.github.io/tei-p6-research/`. Changes reach it only after they
are reviewed, committed, and pushed to `main`; the workflow then rebuilds from
the pushed revision. A fork must enable GitHub Pages with GitHub Actions as its
source before its first deployment.

## 10. Completion gate

Before handing off a change:

```powershell
git diff --check
python -m ruff check .
python tools/validate.py .
python -m pytest tests
```

Also verify that generated files reproduce, no ignored raw data or secret is
staged, source rights and gaps are explicit, and `knowledge/state.md` describes
the actual repository rather than intended future work. Run
`python -m tools.corpus.validate_control_plane .` whenever registry, lock,
manifest, or normalized-corpus controls change.
