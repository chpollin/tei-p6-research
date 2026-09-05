---
title: Research Workbench Design
project:
  name: "TEI P6 Research Vault"
  repository: "tei-p6-research"
method:
  name: Promptotyping
  url: https://dhcraft.org/Promptotyping/
status: draft
language: en
created: "2026-09-05"
updated: "2026-09-05"
related: [index, specification, schema, operations, state, journal]
---

# Research Workbench Design

This document is the stable product and interface contract for the public
research workbench. It records what the interface is for, how the underlying
holdings are presented, where explanatory and technical content belongs, and
which interaction, accessibility, provenance, generation, and publication
rules implementations must preserve.

It is control meta-knowledge, not a source or evidence layer. It cannot ground
a research claim, create a new completion status, or replace the canonical
`00_sources -> 10_markdown -> 20_distillates -> 30_assertions -> 40_output`
chain. Current implementation facts and blockers belong in [[knowledge/state]];
changes of rationale are appended to [[knowledge/journal]].

## Product role

The workbench is the public working surface over the TEI P6 Research Vault. Its
first task is to let a reader inspect which primary materials have actually
been acquired, how they are organized, and where bounded acquisition gaps
remain. Later surfaces may support evidence tracing, comparison, proposal
evaluation, and migration experiments when their canonical inputs are ready.

The workbench is:

- an exploratory research tool, not a promotional dashboard;
- an interface over registered and pinned holdings, not an evidence layer;
- independent and unofficial, not an interface of the TEI Consortium or the
  official TEI P6 process;
- static-first and reproducible, with GitHub Pages as the intended public host.

It must not imply that all relevant material has been collected, that grounded
claims have been human-verified, or that an independent proposal is an official
TEI decision.

## Primary users and tasks

The initial users are researchers, TEI editors and maintainers, educators, and
tool builders. The first interface must help them:

1. see which source families and material collections are present;
2. find a source by title, description, material type, or known term;
3. distinguish acquired, partly acquired, and planned material;
4. inspect the concrete subcollections held for a source family;
5. reach provenance and control records when technical verification is needed.

The default view serves these tasks directly. It does not require the reader to
understand the vault schema, source-lock syntax, run manifests, or internal IDs.

## Information architecture

Acquisition is presented through this hierarchy:

```text
source family
  -> source lock: identity, scope, version, rights, completion target
  -> run manifest: one acquisition run and its declared data products
  -> material collection: a concrete inventory, snapshot, mirror, or record set
  -> files or records
```

One row in the materials table represents one registered source family. Its
expanded detail lists the material collections declared by the selected run
manifest. Counts from unlike collections are not added into a single headline
number. Projections and catalogs aid navigation but remain outside grounding.

| Interface level | Primary content | Secondary content |
|---|---|---|
| Materials table | source title, short description, material summary, acquisition state, observation date | family type and concise gap |
| Expanded row | named material collections, collection type, extent, format | exact data-product path or manifest reference |
| Technical detail | stable IDs, source lock, run manifest, rights and authority fields | raw control records |
| About | project purpose, method, completion semantics, evidence boundary, independent status | links to fuller project documentation |

Raw YAML or Markdown control files are not global navigation and do not belong
in the main footer. They may be exposed in a clearly labelled technical detail
for readers who need to audit the generated view.

## Working-surface principles

The materials page is a working surface. Its first viewport should contain the
page title, the controls needed to explore the holdings, and the beginning of
the results.

- Use a plain white background, restrained typography, clear rules, and a
  compact tabular rhythm.
- Prefer human-readable source titles and short descriptions. Internal IDs are
  secondary.
- Do not place an explanatory hero, methodological essay, release stamp, or
  generated-at line above the work.
- Do not use KPI cards or aggregate counts that combine heterogeneous material
  units or turn bounded acquisition states into project-performance metrics.
- Keep status language concise and explain its exact bounded meaning through
  accessible help or About.
- Translate terse control-record gaps into short user-facing work items. Keep
  the full technical wording in the underlying control record.
- Use progressive disclosure for provenance, rights, identifiers, and file
  paths.
- Show only facts reproducible from current registry, lock, and manifest files.
  A registered or planned source must never appear as acquired by implication.

## Materials-table contract

The initial table provides:

- full-text search across source titles, descriptions, material labels, and
  concise gap descriptions;
- filters for acquisition state and material type;
- sorting by source, materials, acquisition state, and date;
- one expandable row per source family;
- a useful empty state when no row matches;
- keyboard-operable disclosure and controls.

Sorting and filtering change only the view. They do not mutate source records
or create a new research artifact. The page must remain useful as generated
static HTML without a server-side application or a JavaScript framework.

## Header, About, and footer

The initial header contains the project identity and two destinations:
`Materials` and `About`. More navigation is added only when another working
surface exists and has a distinct user task.

About owns the explanatory layer: project purpose, relationship to TEI P6,
method, evidence and completion semantics, data organization, and publication
context. The working page should communicate its function through labels,
controls, columns, and row details instead of repeating that explanation.

The footer is quiet. It identifies the project as independent and unofficial
and may link to About. It is not an index of raw registry, completeness, or
manifest files.

## Language and status semantics

The public interface language is English. Canonical TEI names, stable IDs, file
names, and control vocabulary remain unchanged inside technical details.

User-facing status labels must preserve the completion vocabulary defined in
`corpus/COMPLETENESS.md`. A short label such as `Acquired` is acceptable only
when adjacent accessible help makes clear that completeness is bounded by the
locked public interface, query, sample, release, or observation interval. No
interface may claim global completeness.

## Accessibility and responsive behavior

- Use semantic headings, forms, buttons, tables, and disclosure controls.
- Give every input a persistent label; placeholders are examples, not labels.
- Expose sort state programmatically and announce result-count changes.
- Keep focus indicators visible and make every action keyboard-operable.
- Do not encode acquisition state by color alone.
- Preserve readable type and spacing at 200 percent zoom.
- On narrow screens, preserve table meaning through controlled horizontal
  scrolling or an equivalently structured compact view.

## Provenance, generation, and publication

The public page is generated from `sources/registry.yaml`, source locks, and the
run manifests selected by those locks. It must not publish raw source bodies.
Generation must be deterministic from pinned inputs, and checked-in generated
HTML must match the generator. Generated pages are never edited by hand.

GitHub Pages publishes the checked-in static site for an exact repository
revision. Publication does not raise the evidential status of any material or
claim. Links to technical control records remain audit affordances, not primary
navigation.

## Scope gates

The current scope is the materials inventory. A later feature enters the public
workbench only when its canonical inputs exist, its provenance path is clear,
and its interaction contract has been recorded. Candidate later features are:

- browsing material objects and normalized representations;
- following a claim through assertions and distillates to source passages;
- comparing releases, modules, elements, and implementation consequences;
- evaluating P6 options and migration experiments against explicit criteria.

Authentication, collaborative editing, persistent user state, and editorial
decision making are outside the current static-first scope.

## Acceptance checklist

A workbench change is ready when:

- the main task is evident from the first viewport;
- visible holdings reconcile to locked, completed manifests;
- planned or partial material remains visibly qualified;
- source titles and material descriptions carry the main information load;
- search, filters, sorting, disclosure, and keyboard use work together;
- explanatory content is in About and technical controls use progressive
  disclosure;
- the generated page reproduces from pinned inputs and passes repository checks;
- the interface preserves the independent, unofficial, and bounded-completeness
  distinctions.
