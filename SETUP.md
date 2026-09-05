# Project setup

This repository is already instantiated as the TEI P6 Research Vault. This
guide prepares a local environment; it is not a template-substitution workflow.

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
- pytest for the test suite
- GitHub CLI for repository creation and authenticated API acquisition

With `uv`:

```powershell
uv sync
```

Without `uv`:

```powershell
python -m pip install pyyaml pytest
```

Verify the scaffold:

```powershell
python tools/validate.py .
python -m pytest tests
```

`W-EMPTY` and `W-NO-OUTPUT` describe the present empty production chain. They
are expected until the first complete vertical pilot, but remain findings to
report rather than warnings to hide.

## 3. Open as an Obsidian vault

Open the repository root as the vault. The committed `.obsidian/` configuration
uses core features only. Personal workspace state, caches, and installed
community plugins remain uncommitted.

Start at `HOME.md`. The repository continues to work as plain Markdown without
Obsidian.

## 4. Configure GitHub

The canonical public remote is
`https://github.com/chpollin/tei-p6-research`. Authenticate interactively:

```powershell
gh auth login
gh auth status
```

If the checkout does not yet have `origin`, configure it and push:

```powershell
git remote add origin https://github.com/chpollin/tei-p6-research.git
git push -u origin main
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

## 6. Build collectors before collecting production data

Follow `docs/multi-agent-acquisition-runbook.md`. The first work wave builds and
tests three independent collector families:

1. TEI Git, release, Vault, and baseline materialization;
2. GitHub issues, PRs, comments, reviews, timelines, and relations;
3. governance, history, Zotero, JTEI, and bounded literature discovery.

Each collector needs:

- content-addressed immutable raw storage;
- request and cursor journaling;
- resume and bounded retry;
- exact source/version/API identity;
- offline replay fixtures;
- normalization schemas;
- count and pagination reconciliation;
- explicit rights and gap states.

Production crawls run only after the collector's fixture tests and integration
gate pass.

## 7. Run the first vertical production cycle

Before bulk distillation, carry one rights-cleared source through every layer:

1. **Acquire:** register and retrieve the exact source version.
2. **Admit:** place the allowed original in `00_sources/` or its citation record
   in `references/`.
3. **Represent:** create the immutable anchored file in `10_markdown/`.
4. **Distill:** create source-faithful atomic statements in `20_distillates/`.
5. **Assert:** synthesize one cross-source-ready claim in `30_assertions/` and
   register it in the relevant MOC.
6. **Write:** create one grounded paragraph in `40_output/`.
7. **Check:** run validation and adversarial source-support review.

Run after representation and distillate changes:

```powershell
python tools/inventory.py . --write
python tools/validate.py .
```

For one chapter acceptance:

```powershell
python tools/validate.py . --chapter 40_output/CHAPTER-SLUG.md
```

The first three planned pilots are a normative P5 architecture claim, a
Council-to-release decision trail, and an official-P6-process observation kept
separate from an independent proposal.

## 8. Regenerate documentation

After changing `README.md`, `docs/concept.md`, or knowledge documents consumed
by the site builder:

```powershell
python tools/build_docs.py --date YYYY-MM-DD
python tools/build_corpus_overview.py --date YYYY-MM-DD
```

Never hand-edit `docs/index.html` or `docs/corpus.html`.

## 9. Publish the research workbench

`.github/workflows/pages.yml` validates and regenerates the static site on
`main`, publishes the materials overview at the GitHub Pages root, and keeps the
full project documentation at `project.html`. Internal control and normalized
data links resolve to the exact GitHub commit used for the deployment; ignored
raw source bodies are never included in the Pages artifact.

Before the first publication, configure the GitHub remote, settle repository
visibility, and enable GitHub Pages with GitHub Actions as its source.

## 10. Completion gate

Before handing off a change:

```powershell
git diff --check
python tools/validate.py .
python -m pytest tests
```

Also verify that generated files reproduce, no ignored raw data or secret is
staged, source rights and gaps are explicit, and `knowledge/state.md` describes
the actual repository rather than intended future work.
