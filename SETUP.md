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
- pytest for the test suite
- GitHub CLI when authenticated GitHub acquisition or repository administration
  is required

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

The canonical deployment is live at
`https://chpollin.github.io/tei-p6-research/`. Changes reach it only after they
are reviewed, committed, and pushed to `main`; the workflow then rebuilds from
the pushed revision. A fork must enable GitHub Pages with GitHub Actions as its
source before its first deployment.

## 10. Completion gate

Before handing off a change:

```powershell
git diff --check
python tools/validate.py .
python -m pytest tests
```

Also verify that generated files reproduce, no ignored raw data or secret is
staged, source rights and gaps are explicit, and `knowledge/state.md` describes
the actual repository rather than intended future work. Run
`python -m tools.corpus.validate_control_plane .` whenever registry, lock,
manifest, or normalized-corpus controls change.
