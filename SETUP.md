# Project setup

This guide prepares a local environment for TEI P6 Research and lists the
build, publication and acquisition commands. The rules behind the commands
live in `knowledge/`, and `knowledge/INDEX.md` is the entry point.

## 1. Read the project documents

Before changing content or running acquisition:

1. read `README.md` for the public overview;
2. read `knowledge/INDEX.md`, `knowledge/project.md` and
   `knowledge/specification.md`;
3. read `knowledge/state.md` for the actual data and milestone status;
4. use `AGENTS.md` for Codex or `CLAUDE.md` for Claude Code;
5. read `knowledge/design.md` for research-frontend, About or publication
   work.

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

Verify the checkout:

```powershell
python tools/validate.py .
python -m pytest tests
```

Warnings such as `W-EMPTY` and `W-NO-OUTPUT` describe missing production
artifacts. Investigate and report them rather than hiding them. Their current
applicability belongs in `knowledge/state.md`.

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

The GitHub collectors need `gh auth login` or `GITHUB_TOKEN` and stop with a
`rate-limit-stop` gap while quota remains. Tokens stay in the GitHub
credential store or environment. They never enter files, commands recorded in
manifests, logs or briefs.

## 5. Understand storage boundaries

Normal Git contains code, contracts, registries, locks, manifests, checksums,
small rights-cleared fixtures, and curated knowledge artifacts. Git mirrors,
raw API and web responses, third-party PDFs and attachments, mailing-list
archives, unreviewed discussion text, caches, credentials and temporary files
remain ignored and local. Do not use `git add -f` to bypass these boundaries.
The complete rights and redistribution rule, including how a reviewed original
is admitted to versioning, is in `knowledge/data.md`.

## 6. Acquire or admit material

The collectors are described in `knowledge/operations.md` § Acquire and the
source families, identity and completion vocabulary in `knowledge/data.md`.
`knowledge/state.md` records which families are actually ready. Production
collection starts only after the relevant offline fixtures and integration
checks pass, and source registration or a local cache alone never establishes
acquisition.

Each collector writes one normalized object and one run manifest and prints
one status line. Exit code 0 means `observable-complete`, exit code 2 means a
recorded gap and `partial`. Replace `YYYY-MM-DD`, `<id>` and the URLs with the
values of the run.

```powershell
python -m tools.corpus.git_snapshot --repo-url <url> --source-id <id> --ref HEAD --normalized-output corpus/normalized/git/<id>.json --manifest-output sources/manifests/YYYY-MM-DD-<id>.yaml
python -m tools.corpus.github_snapshot --owner TEIC --repository TEI --source-id github-teic-tei-work-items --normalized-output corpus/normalized/github/teic-tei-work-items.jsonl --manifest-output sources/manifests/YYYY-MM-DD-github-teic-tei-work-items.yaml
python -m tools.corpus.github_org_census --organization TEIC --source-id teic-github-organization --normalized-output corpus/normalized/github/teic-repositories.jsonl --manifest-output sources/manifests/YYYY-MM-DD-teic-github-organization.yaml
python -m tools.corpus.github_org_git_snapshot --census corpus/normalized/github/teic-repositories.jsonl --normalized-root corpus/normalized/git --manifest-root sources/manifests/repos --manifest-output sources/manifests/YYYY-MM-DD-teic-public-git-repositories.yaml
python -m tools.corpus.web_census --source-id <id> --root-url <url> --allow-prefix <prefix> --depth 2 --max-pages 500 --normalized-output corpus/normalized/web/<id>.jsonl --manifest-output sources/manifests/YYYY-MM-DD-<id>.yaml
python -m tools.corpus.sourceforge_snapshot --tracker bugs=https://sourceforge.net/rest/p/tei/bugs --tracker feature-requests=https://sourceforge.net/rest/p/tei/feature-requests --tracker support-requests=https://sourceforge.net/rest/p/tei/support-requests --workers 8 --delay-seconds 0.2 --normalized-output corpus/normalized/sourceforge/tei-legacy-trackers.jsonl --manifest-output sources/manifests/YYYY-MM-DD-tei-legacy-sourceforge.yaml
python -m tools.corpus.asset_snapshot --source-id <id> --url <asset url> --normalized-output corpus/normalized/assets/<name>.json --manifest-output sources/manifests/YYYY-MM-DD-<name>.yaml
python -m tools.corpus.zip_inventory --source-id <id> --archive corpus/raw/sha256/<aa>/<rest> --normalized-output corpus/normalized/assets/<name>-members.json --manifest-output sources/manifests/YYYY-MM-DD-<name>-members.yaml
```

After a run, validate the control plane:

```powershell
python -m tools.corpus.validate_control_plane .
```

Admission of a selected source into the knowledge chain follows
`knowledge/operations.md` § Ingest.

## 7. Run a vertical research cycle

Before topic-scale distillation, take one rights-cleared source through the
canonical chain. `knowledge/operations.md` holds the complete procedure and,
under § Analyze, the procedures for an element, a module, a release
comparison, an issue or decision and a P6 proposal. Never create a shortcut
from the acquisition corpus to a higher evidence layer.

Run after representation and distillate changes:

```powershell
python tools/inventory.py . --write
python tools/validate.py .
```

For one chapter acceptance:

```powershell
python tools/validate.py . --chapter 40_output/CHAPTER-SLUG.md
```

## 8. Reproduce the experiments

The bounded text identity and annotation pilot:

```powershell
python tools/check_text_identity_pilot.py
```

The combined gate checks source integrity, chapter provenance, current
independent-review coverage, experiment reproduction and the full test suite.
Human acceptance uses the items in `knowledge/experiments.md`. After an
intentional experiment or contract change, regenerate the report with
`python -m tools.pilots.text_identity`. Changed research claims require fresh
review via `python tools/check_text_identity_pilot.py --emit-review` and an
independent reviewer under `knowledge/verification.md`.

Abstract Text Model 0.1, whose independent case gate needs no raw corpus:

```powershell
python tools/check_abstract_text_v01.py --check
python tools/check_abstract_text_v01.py --validate experiments/abstract_text_v01/examples/competing-readings.json
python -m pytest tests/models tests/test_check_abstract_text_v01.py
```

The first command checks frozen expectations, all declared rule and operation
coverage, nonmutation, canonical reproduction, standalone examples and exact
report reproduction, and it fails if the report is missing or stale. After
reviewing an intentional model, contract or fixture change, regenerate with
`python tools/check_abstract_text_v01.py` and rerun `--check`. Input
fingerprints normalize checkout line endings, and strings inside model
instances remain exact. The validation command prints machine-readable
diagnostics and resolutions. The definitions and the separate human
acceptance questions are in `knowledge/text-model.md`.

The editorial cases:

```powershell
python tools/ingest_editorial_cases.py --check
python tools/check_editorial_cases.py --check
```

The first research wave provides three read-only reproduction checks:

```powershell
python -m tools.tei.build_atlas --output corpus/projections/p5-specs-4.12.0.json --check
python tools/check_wave1_sources.py .
python tools/check_wave1_sources.py . --review-only
```

The atlas check requires the locked local TEI Git mirror. Omit `--check` to
regenerate the projection after an intentional generator or control-input
change. The quotation check requires the local raw snapshots named in
`sources/manifests/2026-09-05-research-wave-1-citations.yaml`. It performs no
network retrieval and fails clearly when a snapshot is unavailable, so a clean
checkout without ignored raw data can inspect the recorded intake but cannot
claim to have rerun quotation fidelity. `--review-only` needs no ignored
originals. It checks the canonical source-support prompts recorded in
`workbench/reviews/2026-09-05-wave1/pairs.jsonl`, their exact dependency
coverage and their passing verdict hashes. CI runs this check separately from
the local raw-source quotation check. None of these commands assigns research
status. On Windows with the Python launcher, `py -3` can replace `python`.

## 9. Regenerate the site

After changing `README.md` or any knowledge document consumed by the About
page, and after changing registry, lock, manifest, model or proposal inputs:

```powershell
python tools/build_docs.py --date YYYY-MM-DD
python tools/build_corpus_overview.py --date YYYY-MM-DD
python tools/build_home.py --date YYYY-MM-DD
python tools/build_knowledge.py --date YYYY-MM-DD
python tools/build_model_reference.py --date YYYY-MM-DD
```

Never hand-edit generated HTML. The home builder writes `docs/index.html`, the
project builder `docs/project.html`, and the Knowledge and Model builders
`docs/knowledge.html` and `docs/model.html`. These paths are identical locally
and on GitHub Pages. The home generator reads the complete canonical proposal
in `40_output/12-p6-design.md`, its source links, model definitions and
examples. The builders and their declared inputs are listed in
`knowledge/architecture.md`.

## 10. Publish the research workbench

`.github/workflows/pages.yml` validates and regenerates the static site on
`main` and publishes the proposal home at the GitHub Pages root, the
materials overview at `corpus.html`, the project documents at
`project.html`, the formal model reference at `model.html` and the knowledge
browser at `knowledge.html`. Internal control and normalized data links
resolve to the exact GitHub commit used for the deployment, and ignored raw
source bodies are never included in the Pages artifact.

The canonical deployment is live at
`https://chpollin.github.io/tei-p6-research/`. Changes reach it only after
they are reviewed, committed and pushed to `main`; the workflow then rebuilds
from the pushed revision. A fork must enable GitHub Pages with GitHub Actions
as its source before its first deployment.

## 11. Completion gate

The one completion gate for every change, what each check establishes and
the layout of the tests are in `knowledge/testing.md`.
