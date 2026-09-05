---
title: Schema
project:
  name: "TEI P6 Research"
  repository: "tei-p6-research"
method:
  name: Promptotyping
  url: https://dhcraft.org/Promptotyping/
profile:
  name: Grounded Vault
  url: https://github.com/DigitalHumanitiesCraft/grounded-vault
status: draft
language: en
created: "2026-09-04"
updated: "2026-09-05"
related: [index, specification, design, operations, state]
---

# Schema

This schema defines artifact types, frontmatter, section skeletons, anchor
forms, and status rules. Every content file follows these contracts.
[[knowledge/operations]] defines how the files are produced and checked.

## Layer model

| Layer | Folder | Content | Anchor it carries |
|---|---|---|---|
| Sources | `00_sources/` | originals, local only | none |
| Markdown representation | `10_markdown/` | archived full texts, datasets with schema | block IDs, file plus schema |
| Distillates | `20_distillates/` | one distillate per source | grounding anchors into its source, statement IDs |
| Assertions | `30_assertions/` | atomic cross-source statements, topic maps | grounding anchors into distillate statements |
| Output | `40_output/` | one file per chapter | footnote anchors into assertions, posits marked |

Generate the source inventory in [[knowledge/state]] with
`python tools/inventory.py . --write`. It lists every representation and
distillate from actual files and must not be maintained by hand.

A source is the unchanged original. Its Markdown representation is converted
once and given stable block IDs. A distillate extracts statements from exactly
one source. An assertion synthesizes one claim from the topic's distillates
and cites at least one supporting statement. A chapter is the output unit.
Its factual premises cite assertions and its own conclusions are explicit posits.

Anchors are minted only at their own layer. Representations mint block IDs
and distillates mint statement IDs. Higher layers reference existing anchors
in their direct predecessor. Chapters cite assertions, assertions cite
distillate statements, and document distillates cite representation blocks.

Anchor resolution establishes structural traceability. It does not establish
that the passage supports the claim. Source-support review and human
verification remain separate checks under [[knowledge/operations]].

## Controlled vocabularies

| Field | Allowed values or constraint |
|---|---|
| `type` | `representation`, `distillate`, `assertion`, `moc`, `glossary`, `chapter` |
| `source-type` | `document`, `publication`, `data` |
| `channel` | `handover`, `collection`, `import`, `deep-research` |
| `status` | `grounded`, `validated`, `verified`, plus `contested` for assertions and `superseded` for distillates |
| `topics` | Each value names an existing `MOC-*.md` topic map in `30_assertions/` |

The value `representation` is the machine-side abbreviation. Prose uses
“Markdown representation.”

## Audit trail

Status records checks that actually ran. Every check writes its date into
the checked artifact's `checked` map.

```yaml
status: validated
checked:
  validation: 2026-07-11
  machine-review: 2026-07-11
```

`validated` requires `checked.validation` and `checked.machine-review`.
`verified` additionally requires `checked.verification`. Every entry has an
ISO date. A new artifact enters as `grounded` without requiring a check entry.

An artifact's status is the minimum status of its anchors.
Assertions use their `grounding` field and chapters their `assertions` mirror
for this comparison. An unreviewed anchor keeps the dependent artifact at
`grounded`. The separate states `contested` and `superseded` have no ladder
rank, so their dependents also remain `grounded`.

Publication distillates record the intake quotation check as `checked.quote`
because the full text may be unavailable later. No check may assign a status
above its authority in [[knowledge/operations]].

## Source metadata

Every representation carries Dublin-Core-compatible source metadata.
Licensing and confidentiality are properties of the individual source.

```yaml
metadata:
  title: ""            # dc:title
  creator: ""          # dc:creator; role and institution, no third-party personal names
  date: ""             # dc:date of the source, ISO 8601
  format: ""           # dc:format of the original (pdf, pptx, csv, …)
  identifier: ""       # dc:identifier (DOI, URL, archival signature) where one exists
  license: ""          # dc:rights; SPDX identifier or short clause
  confidential: false  # true keeps original and full text local
```

## Source types

Choose the source type by storage rights and the required anchor.

| Source type | Representation and anchor |
|---|---|
| `document` | Stored full text in a Markdown representation, anchored by block references |
| `publication` | Bibliographic record, anchored by an exact quotation and source identifier |
| `data` | Data file and schema description, anchored by a deterministic computation |

An aggregate finding may have no corresponding passage. Its computation
therefore supplies the anchor.

Publication status does not determine source type. Prefer `document` when
the full text may be stored, including an open-access article with suitable
rights, because its anchors resolve inside the vault.

## Bibliographic records

`references/` holds the bibliographic records of the citable-only sources as CSL JSON, normally exported from the reference manager. A small curated primary-metadata import follows the recorded intake procedure in [[knowledge/operations]]. Each file is a JSON array of records, and each record carries an `id` alongside its bibliographic fields.

```json
[
  {
    "id": "author2024keyword",
    "type": "article-journal",
    "title": "",
    "author": [{ "family": "", "given": "" }],
    "issued": { "date-parts": [[2024]] },
    "container-title": "",
    "URL": ""
  }
]
```

The `reference` field of a publication distillate names one such `id`, and validation raises `E-ANCHOR` when no record in `references/` carries it. The folder is needed only while the source type `publication` is active.

## Document types

Each type carries its frontmatter as a code block, followed by the section skeleton where one is fixed. Fields not marked optional are required. Wikilink values are quoted, block IDs unquoted, as Obsidian requires for YAML.

### 1. Markdown representation (source-type: document)

Store exactly one immutable representation per admitted document source in
`10_markdown/documents/`. A revised source enters as a new file with a
date-suffixed slug. Existing anchors continue to address the older file.

```yaml
---
type: representation
source-type: document
source: "[[00_sources/<filename>]]"
converter: ""            # e.g. Docling, MarkItDown
channel: handover        # handover | collection | import | deep-research
metadata: { … }          # see Source metadata
created: 2026-01-01
updated: 2026-01-01
---
```

Use the original H1 above the converted full text. Each anchor-relevant
paragraph ends with a block ID.

```markdown
The board approves centrally operated services. ^a1b2
```

Block IDs are short, stable, unique per file, and minted only here.

### 2. Markdown representation (source-type: data)

A dataset plus its schema description. The data file (CSV, XML, …) lives in `10_markdown/data/` next to a Markdown file of the same slug that carries the frontmatter and describes the schema.

```yaml
---
type: representation
source-type: data
source: "[[00_sources/<filename>]]"    # omit when the data file is the original
data: "[[10_markdown/data/<file.csv>]]"
channel: handover
metadata: { … }
created: 2026-01-01
updated: 2026-01-01
---
```

The body describes columns, units, encodings and known limitations. The anchor of this type is a computation, defined in the distillate.

### 3. Distillate

Store one distillate per source in `20_distillates/<source-type>s/`,
using the representation's slug where one exists. Its core statements
reproduce that source alone. Cross-source synthesis belongs in assertions
and source appraisal in the optional Appraisal section.

```yaml
---
type: distillate
source-type: document        # document | publication | data
representation: "[[10_markdown/documents/<slug>]]"   # document and data types
reference: ""                # publication type: CSL JSON id from references/
topics: ["[[<Topic>]]"]
status: grounded             # grounded | validated | verified | superseded
checked: {}
superseded-by: ""            # optional, wikilink to the successor distillate
created: 2026-01-01
updated: 2026-01-01
---
```

```markdown
# Distillate: <source short title>

<Lead: one sentence naming the source and its contribution to the vault.>

## Core statements

- <statement> [[10_markdown/documents/<slug>#^a1b2]] ^s1
- <statement> [[10_markdown/documents/<slug>#^c3d4]] ^s2

## Terms

- **<term>**: <meaning as set by the source> [[10_markdown/documents/<slug>#^e5f6]]

## Open questions

- <unclarity of the source>

## Appraisal

<optional; what this source is worth, in prose>

## Related

- [[20_distillates/…]] / [[30_assertions/…]]
```

Each core statement has exactly one source anchor and ends with a statement
ID such as `^s1`. Assertions cite these IDs. The source type determines the
anchor form.

- For a document, use a block reference into its representation.
- For a publication, use a verbatim quotation and citation. Check exact
  quotation identity at intake and record `checked.quote`.

  ```markdown
  - <statement in own words> ^s1
    > "<verbatim quotation>" (<identifier>, p. <n>)
  ```

- For data, name a reproducible computation on an indented line. Its
  deterministic script lives in `tools/analysis/`.

  ```markdown
  - <statement, e.g. an aggregate or finding> ^s1
    - computation: `python tools/analysis/<script>.py` → `<stated result>`
  ```

  The script reads the data file of the Markdown representation, takes no arguments, and prints the stated result and nothing else to standard output. Validation re-runs it from the vault root and compares that output character for character with the stated result, so a formatting difference is a defect.

The optional **Appraisal** evaluates the source's venue, review, method,
relevance, and limitations where applicable. It expresses the project's
judgment and carries no grounding obligation. It cannot mint anchors or
statement IDs. Validation raises `E-STATEMENT` for any ID outside Core
statements. An appraisal used in output becomes a posit footnote.

**Open questions** contains questions rather than findings and mints no IDs.
A source-supported finding belongs in Core statements with its own anchor
and ID. Unresolved perspectives may remain as questions until sources can
support a statement.

### 4. Assertion

A single source-supported statement synthesized from the distillates of a topic and grounded in at least one distillate statement. One file per assertion in `30_assertions/`. This is the layer where source types converge.

```yaml
---
type: assertion
topics: ["[[<Topic>]]"]
status: grounded             # grounded | validated | verified | contested
checked: {}
grounding:
  - "[[20_distillates/documents/<slug>#^s1]]"
  - "[[20_distillates/publications/<slug>#^s2]]"
contested-with: []           # wikilinks; required on both sides when status is contested
created: 2026-01-01
updated: 2026-01-01
---
```

```markdown
# <The assertion as one sentence>

## Statement

<The assertion spelled out, one short paragraph.>

## Support

- [[20_distillates/documents/<slug>#^s1]] — <what this anchor contributes>
- [[20_distillates/publications/<slug>#^s2]] — <what this anchor contributes>

## Related

- [[30_assertions/…]]
```

A conclusion without source support enters output as a posit. Irreconcilable
assertions are both marked `contested` and linked reciprocally in
`contested-with`.

An assertion reports a source-supported claim and carries a check status.
A posit records the author's judgment, with no status of its own. It does not
mature into an assertion. If later sources support a claim, write a new
assertion and remove the replaced posit. The open evidence question remains
a research task. A chapter's `posits` count records its authorial conclusions.

Source support can conceal a shift in what the statement is about.
Two recurring forms require explicit attribution or additional evidence.

**Self-report.** A source's claim about its own priority, reach, or achievement
supports an attributed report of that claim. Asserting the achievement itself
requires an independent source. Preserve this attribution in the distillate
and assertion.

**State report.** A source that shows an object in one state at one time
supports that dated observation. Preserve the state and date in the
distillate and assertion, or cite a source that establishes the wider period
being claimed. A restoration records the restored state, an inventory its
dated contents, and a plan an intention.

### 5. Topic map (MOC)

One file per topic of the controlled topic set, named `MOC-<Topic>.md` in `30_assertions/`. The set of these files is the topic vocabulary.

```yaml
---
type: moc
topic: "<Topic>"
created: 2026-01-01
updated: 2026-01-01
---
```

```markdown
# MOC: <Topic>

<Lead: one sentence on what this topic covers.>

- [[30_assertions/<slug>]] — <half-sentence of orientation>

## Open questions

- <question the vault cannot currently answer from its sources>
```

The body lists every assertion of the topic as a wikilink with a half-sentence of orientation. Every assertion must be reachable from at least one topic map, and the validator raises `E-ORPHAN` on one that is not.

### 6. Glossary entry

One term per file in `glossary/`, serving as definition, wikilink hub and tag keyword.

```yaml
---
type: glossary
term: "<term>"
created: 2026-01-01
updated: 2026-01-01
---
```

```markdown
# <Term>

<Definition in one or two sentences.> [[10_markdown/documents/<slug>#^a1b2]]
```

The body gives the definition in one or two sentences with a grounding anchor where the definition comes from a source. The glossary holds one document per central technical term of the content and is used as the need arises.

### 7. Chapter

Store one chapter per file in `40_output/`, using continuous prose in the
project's working language and style. Every factual premise cites an assertion
and every own conclusion is marked as a posit. The chapter is independently
checkable and acceptable as an output unit. In an article it may correspond
to a section.

```yaml
---
type: chapter
status: grounded             # grounded | validated | verified
checked: {}
assertions: ["[[30_assertions/<slug>]]"]   # structured mirror of exactly the Grounded-in assertions; posit-linked ones stay out
posits: 0                                  # count of posit footnotes
created: 2026-01-01
updated: 2026-01-01
---
```

Every load-bearing sentence has a footnote marker. Each footnote begins with
one of the two keywords shown below. Other openings do not satisfy the contract.

```markdown
Water use fell by a third after metering was introduced.[^1] The board should
therefore extend metering to all sites.[^2]

[^1]: Grounded in [[30_assertions/metering-reduces-use]].
[^2]: Posit: follows from [^1] only if consumption patterns are comparable
      across sites. Open evidence question: site-level baseline data.
```

Validation compares the footnotes with the `assertions` mirror and `posits`
count. An alternative notation must preserve the marker, keyword, and mirror.

A chapter discussing contested claims cites both sides of each pair.
Citing one without any counterpart raises `W-CONTESTED`.

## Meta documents

The seven documents in `knowledge/` carry the Promptotyping header (as at the top of this file) instead of a content `type`. They are meta-knowledge about the vault and are exempt from the content schema. `knowledge/design.md` governs the research workbench but creates no artifact type, status, or grounding target. A knowledge document is split only when its sections develop divergent update rhythms or divergent readers.

## Naming

File names are speaking slugs, ASCII-lowercase with hyphens, derived from genre and subject (`report-water-metering-2026-03`). Markdown representation and distillate of the same source share the same slug. Date suffixes distinguish version rows.
