---
title: Research Workbench Design
project:
  name: "TEI P6 Research"
  repository: "tei-p6-research"
method:
  name: Promptotyping
  url: https://dhcraft.org/Promptotyping/
status: draft
language: en
created: "2026-09-05"
updated: "2026-09-06"
related: [INDEX, specification, data, schema, operations, testing, state, journal]
---

# Research Workbench Design

This contract defines the public interface, its canonical inputs, and its
publication rules. The workbench is a generated view over the repository.
It cannot ground a research claim or change an artifact's evidence status.
Implementation progress belongs in [[knowledge/state]] and durable decisions
in [[knowledge/journal]].

## Product role and navigation

The workbench helps researchers, editors, educators, and tool builders read
the proposal, inspect its model, compare encodings, and follow claims to their
sources. It is an independent, unofficial research publication.

All pages use the same header, footer, typography, controls, and outer layout.
The primary navigation has five destinations.

| Navigation | Route | Main task |
|---|---|---|
| Proposal | `index.html` | Read the full technical argument and open comparative examples |
| Model | `model.html` | Inspect record classes, relationships, invariants, operations, and the canonical definition |
| Materials | `corpus.html` | Search registered source families and inspect acquisition boundaries and gaps |
| Knowledge | `knowledge.html` | Browse admitted sources, distillates, assertions, and output with provenance links |
| About | `project.html` | Read project scope, method, repository contracts, and current state |

Local preview and GitHub Pages preserve the same routes. Page-local navigation addresses
sections and examples within these views. Raw manifests and control files
belong in contextual technical details, not global navigation.

## Shared visual and writing rules

Use a white background, restrained sans-serif typography, modest headings,
and monospace for code and formal records. Separate content through spacing,
alignment, and heading hierarchy. Do not use decorative horizontal lines,
table separators, card grids, oversized slogans, or promotional introductions.
Diagram edges that express relationships and visible keyboard focus remain
necessary information.

The first viewport presents the page's main work. Proposal begins with the
canonical text. Materials and Knowledge show their search controls and results.
Model begins with its definition and relationship overview. About contains the
longer project explanation without repeating it above every working view.

Use precise English prose with one point per paragraph. Remove repeated
disclaimers, empty transitions, and sentences that only announce the next
sentence. Use no colons or semicolons in running prose. Preserve required
punctuation in code, quotations, URLs, metadata, and formal citation syntax.
Lists serve navigation, independent checks, or ordered actions. Tables compare
the same attributes across records or alternatives.

Keep canonical TEI names, IDs, filenames, and controlled vocabulary unchanged.
Present readable titles before internal identifiers. Explain unfamiliar status
terms where they affect a reader's judgment. The footer identifies the project
as independent and records the build date without becoming a technical index.

## Proposal and comparative examples

The full proposal comes from `40_output/12-p6-design.md`. No second maintained
copy of its prose is permitted. It remains readable without JavaScript, with
a table of contents, stable section links, and source footnotes.

A grounded premise opens the actual assertion and its links down the
provenance chain. A posit opens its rationale and evidence question. Interface
actions do not raise either status. Small editorial excerpts retain attribution
and their own license. Authored examples are labeled as synthetic.

An example opens a comparison workspace to the right of the proposal while
preserving the reading position. Each case has a direct URL and a close action.
At narrow widths it uses the full viewport. The case keeps the phenomenon and
task fixed while the reader selects a documented P5 variant or a supported
binding of the candidate model.

Every binding view must describe the same selected model instance. The
comparison identifies mapping policy, formal requirements, actual validation
results, and unresolved or lost distinctions. A failed mapping remains visible.
An illustrative encoding cannot substitute for a validated converter, and an
unimplemented binding cannot appear as a supported choice.

Type diagrams explain object kinds and cardinalities. Instance diagrams show
the selected package's actual IDs and references. Text-range views display the
same selections as the code and diagram. Diagram position alone must not imply
order, containment, identity, or authority absent from the records.

Coverage navigation may connect P5 modules, document types, media, and
phenomena. These remain separate dimensions. An inventory entry does not
establish model coverage, and a successful case covers only its declared task.

## Model reference

Model renders the canonical definition and the executable contract's record
fields, reference cardinalities, selector types, invariants, and operations.
The class diagram and field tables explain that same contract. They do not
create a second specification.

The reference distinguishes identified records, nested values, and operation
outputs. It also distinguishes the base model from optional profiles and
serialization bindings. Formal validity does not establish the truth of an
annotation or the adequacy of the model for every text form.

## Materials inventory

Acquisition is presented as source families, locked boundaries, selected run
manifests, and declared collections. One row represents one registered family.
Expanded rows expose its named collections and acquisition gaps.

| Level | Visible information |
|---|---|
| Family row | Title, description, collection summary, acquisition state, and observation date |
| Expanded row | Collection names, types, extents, formats, and concise open work |
| Technical detail | Exact IDs, data-product paths, source lock, run manifest, rights, and authority |

Counts retain their units. Unlike collections must not be combined into a
single total or performance indicator. Short gap descriptions may clarify
control-record wording while the complete record remains available for audit.

Materials provides text search, acquisition and material-type filters,
sorting, and keyboard-operable disclosure. It reports an empty result when no
family matches. These controls change the view without modifying source data.

The page reports only what its registry, locks, and manifests establish.
A registered or planned source must not appear acquired. User-facing labels
preserve the bounded completion meanings defined in [[knowledge/data]].
Accessible help explains the applicable release, public interface, sample,
query, or snapshot interval. The inventory does not serve ignored raw bodies
or claim to enumerate every raw file individually.

## Knowledge and provenance

Knowledge inventories actual Vault artifacts and exposes immediate-layer
links and backreferences. It distinguishes acquisition from admission to the
knowledge chain.

```text
00_sources -> 10_markdown -> 20_distillates -> 30_assertions -> 40_output
```

Document admissions lead to stable source passages. Citation-only admissions
lead to the checked quotation and bibliographic record. Ignored originals are
never served. Rights, authority, versions, checks, and known gaps remain
inspectable where they qualify a claim.

Search and projections aid retrieval without becoming grounding targets.
Neither a resolved link nor publication establishes human verification.
Comparison views and model diagrams also remain outside the evidence chain.

## Implementation architecture

The workbench is static and framework-free. All generators use
`tools/sitegen/chrome.py` and `tools/sitegen/assets/workbench.css` for shared
navigation, footer, typography, controls, and outer layout. Page-specific
styles describe content components without redefining that common system.

| Concern | Responsibility |
|---|---|
| Input and view model | Validate declared inputs and prepare presentation labels |
| Rendering | Generate semantic HTML from prepared data without fetching or reinterpreting sources |
| CSS | Define shared layout and component styles in source assets |
| JavaScript | Handle search, selection, disclosure, and accessible state without maintaining research data |

The build embeds CSS and JavaScript into complete HTML pages. Generated files
are never hand-edited. A new client framework, runtime, persistent state, or
manually maintained page requires a recorded architecture decision.

| Generator | Canonical inputs | Generated pages |
|---|---|---|
| `tools/build_home.py` | Proposal, linked knowledge, model definition, and declared examples | `docs/index.html` |
| `tools/build_model_reference.py` | Model definition and formal contracts | `docs/model.html` |
| `tools/build_corpus_overview.py` | Source registry, locks, and selected manifests | `docs/corpus.html` |
| `tools/build_knowledge.py` | Actual Vault artifacts and their provenance metadata | `docs/knowledge.html` |
| `tools/build_docs.py` | README and the knowledge documents | `docs/project.html` |

## Regeneration

After changing `README.md` or any knowledge document consumed by the About
page, and after changing registry, lock, manifest, model or proposal inputs,
run the builders whose declared inputs changed:

```powershell
python tools/build_docs.py --date YYYY-MM-DD
python tools/build_corpus_overview.py --date YYYY-MM-DD
python tools/build_home.py --date YYYY-MM-DD
python tools/build_knowledge.py --date YYYY-MM-DD
python tools/build_model_reference.py --date YYYY-MM-DD
```

Every builder takes its build date as an argument and never reads the system
clock, and it records that date in the page footer. A page regenerated on a
later day therefore still rebuilds from the date it carries, which is what
the reproduction check in [[knowledge/testing]] compares.

## Accessibility and responsive behavior

Use semantic headings, forms, buttons, tables, and disclosure controls.
Every input has a persistent label. Placeholders provide examples. Sort state
is programmatically exposed and result changes are announced. Selected states
and statuses remain understandable without color.

All actions work by keyboard with visible focus. Closing a comparison returns
focus to its origin where available. Respect reduced-motion preferences and
keep text readable at 200 percent zoom. At narrow widths, wide code and tables
use contained scrolling while the main reading surface fits the viewport.
The static proposal and source references remain usable without JavaScript.

## Generation and publication

Builds are deterministic from declared inputs and dates. Checked-in HTML must
match the generators. GitHub Pages publishes the static site for an exact
repository revision. Publication changes neither source rights nor evidence
status.

A new feature requires canonical inputs, a clear provenance boundary, and a
recorded interaction contract. Authentication, collaborative editing,
persistent user state, and editorial decisions remain outside this publication
scope.

## Acceptance checklist

- All five routes use the shared layout and reach their declared content.
- The first viewport presents the page's task without promotional material.
- Holdings and knowledge links reconcile to their canonical records.
- Planned material, bounded mappings, failures, and untested properties remain visible.
- Search, filters, sorting, disclosure, and deep links work together.
- Keyboard, desktop, narrow-screen, and reduced-motion behavior have been checked.
- The full proposal and references remain readable without JavaScript.
- Generated pages reproduce from declared inputs and pass repository checks.
- Source rights, independent status, and verification boundaries are preserved.
