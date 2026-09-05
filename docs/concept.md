# Grounded Vault

Grounded Vault organizes research claims so that a reader can follow them to
source passages and inspect the checks behind them. It is a Promptotyping
profile for work with explicit evidence obligations.

This document explains the inherited architecture. The operative contracts
for TEI P6 Research are in [knowledge/schema.md](../knowledge/schema.md) and
[knowledge/operations.md](../knowledge/operations.md). Project scope and
current state are defined separately in `knowledge/`.

## 1. Problem

A report may cite a source without showing which passage supports a particular
claim. The reader then has to reconstruct that connection and determine
whether the statement preserves the passage's meaning. This applies to
human-authored and generated research alike.

Grounded Vault makes that connection part of the document structure. A
resolvable citation supplies a checkable path. Source-support review and
human judgment assess what the path establishes.

## 2. Core idea

Source material enters at the bottom of a layered repository. Defined
transformations produce source statements, assertions, and output while
preserving references between adjacent layers. Every load-bearing output
statement cites an assertion or is marked as an authorial posit.

Three checks divide the work. Validation tests structure and anchor
resolution. Machine review tests whether each passage supports its statement.
Human verification determines whether a grounding relation qualifies as
evidence under the project's review role.

Agents can prepare the files and review pairs, but their agreement does not
establish truth. The intended result is an inspectable research record with
dated check outcomes. An unfinished vault can remain useful because the
review state of each artifact is explicit.

## 3. Terminology

A **source** supplies information. Its presence does not establish correctness.
A **source type** determines how the material is represented and how statements
anchor into it.

A **distillate** extracts statements from exactly one source. It preserves
that source's scope and keeps appraisal separate from reported content.
An **assertion** synthesizes one source-supported claim from distillate
statements. This is where different sources and source types can contribute
to the same claim.

**Grounding** is the structural relation connecting a claim to its source
locations. **Evidence** is a grounding relation that has passed human expert
verification. Evidence is therefore relative to a claim rather than an
intrinsic property of a document.

A **posit** records a conclusion supported by the author's reasoning, with an
explicit rationale and open evidence question. It has no verification status
of its own. A **provenance chain** connects output, assertions, distillates,
and source locations without a skipped layer.

The **audit trail** records only checks that actually ran, with dates on the
checked artifacts. The full vocabulary and status rules are defined in the
project schema.

## 4. Layer model

| Layer | Function |
|---|---|
| Sources | Preserve original material |
| Markdown representation | Provide stable source text or data descriptions with anchors |
| Distillates | Extract statements from one source |
| Assertions | Synthesize atomic claims and organize them through topic maps |
| Output | Present the argument with assertion citations and explicit posits |

Each layer mints only its own anchors and references its direct predecessor.
A distillate cites an existing representation block rather than inventing a
source location. Output cites assertions rather than bypassing synthesis.

Unsupported conclusions remain posits. Irreconcilable assertions remain
contested and link to one another in both directions. An output account of
the disagreement cites both sides.

## 5. Source types

Storage rights and the required anchor determine source type. A published
article can be a document when its full text may be stored. Citation-only
admission is the fallback where storage is not permitted or practical.

| Type | Stored material | Grounding anchor |
|---|---|---|
| Document | Immutable Markdown full text converted from the original | Stable passage block |
| Publication | CSL JSON bibliographic record with a persistent identifier, preferably a DOI | Exact quotation and source identifier |
| Data | Data file and schema description | Versioned deterministic computation and its result |
| Image or other carrier | Unelaborated extension point | A region or documented description would need a separate contract |

Document distillation extracts statements against passage blocks.
Publication distillation extracts statements against verbatim quotations.
Quotation identity must be checked at intake while the full text is
available, with the check date recorded. Data distillation names the
computation producing each finding so that validation can reproduce it.

Metadata records the source's identity, creator, date, format, rights, and
confidentiality. Rights determine whether an original or representation may
be stored, versioned, or published. They do not change the checking procedure.
Bibliographic substance remains in the CSL record instead of being copied
into another source record.

A representation is converted once and never edited. A revised source enters
as a new dated or versioned representation, preserving earlier anchors.
The old distillate records its successor and becomes superseded.

### Acquisition channels

Channel records how material arrived. It is independent of source type.
Handover, collection, import, and deep research all retain the same quotation
and support obligations.

The reference deep-research workflow searches a controlled topic, prioritizes
peer-reviewed and official sources, applies the project's exclusions, and
examines full text and counterevidence. Located publications enter a reference
manager and are exported as CSL JSON. Credentials and library identifiers stay
outside the repository.

The generated research report never becomes a source. Its located publications
receive ordinary distillates and checked quotation anchors. The operational
prompt and intake procedure belong in the project operations contract.

## 6. Checking instances and the audit trail

| Check | Question | Authority |
|---|---|---|
| Validation | Does the artifact satisfy its formal contract and do its anchors resolve? | Records deterministic conformance |
| Machine review | Does the cited passage support the statement? | With validation, permits `validated` |
| Verification | Does this grounding hold as evidence? | The designated human expert may establish `verified` |

Validation runs on every change and gates subsequent checks. It tests
frontmatter, anchors, statement IDs, topic-map reachability, quotation checks,
reproducible data results, and output citation mirrors. The same input yields
the same verdict.

Machine review uses a separate context containing only the source location
and bare statement. The producing agent's reasoning stays hidden. Its fixed
verdicts are *fully supports*, *partially supports*, *overreaches*,
*contradicts*, and *not in the text*. Only *fully supports* passes.

Verification is the designated human expert's judgment. Machines prepare the
pairs without acquiring that authority. The project chooses the validator,
reviewer, and pair-extraction mechanisms while retaining these contracts.

Artifacts progress from `grounded` through `validated` to `verified`
only after the corresponding checks. Dates record when those checks ran.
An artifact cannot exceed the status of its supporting anchors or the
authority of its reviewer. Conflicting assertions may instead be `contested`.

## 7. Governance layer and Promptotyping

Promptotyping records a project's requirements, data, decisions, and procedures
so that people and agents can work from shared instructions. Grounded Vault
adds contracts for the research knowledge that the project produces.

The control documents in `knowledge/` govern the numbered content layers.
Specification owns purpose and choices, Schema owns artifact contracts, and
Operations owns procedures. State records holdings and progress, Journal
preserves decisions, and Index connects the reading paths. TEI P6 Research
also has Design for the public workbench contract.

A control document is split only when its sections need different readers or
update rhythms. Decision rationale belongs in the journal rather than being
retold in every content document.

## 8. Dual readability

Humans and agents use the same Markdown files. Topic maps collect assertions,
wikilinks connect related material, and output footnotes lead toward source
passages. The files remain readable outside Obsidian.

Agent adapters such as `AGENTS.md` and `CLAUDE.md` provide short,
harness-specific instructions that route into `knowledge/`. They do not
duplicate the contracts or make the architecture depend on one vendor.

A frontend can render the same artifacts without creating another knowledge
layer. In this project, the generated workbench presents the proposal, model,
materials, and provenance chain under [knowledge/design.md](../knowledge/design.md).

## 9. The output as parameter

The reference output is continuous prose, with one independently checkable
file per chapter. Each load-bearing statement has an inline marker identifying
its assertion support or posit. Frontmatter mirrors the assertion set and
posit count, and validation compares both representations.

Footnotes keep this contract readable in Markdown. An alternative notation
must preserve inline markers, support or posit keywords, and the structured
mirror. A separate data sidecar alone would not preserve human readability.
Genre and style can change without changing these evidence obligations.

Code or data-analysis output requires a separate anchoring design. The
inherited profile does not define that extension. The project's executable
experiments therefore use their own explicit contracts while grounded
research conclusions continue to enter the canonical output chain.

## 10. Repository topology

The inherited template sketch shows the numbered evidence layers and the
supporting folders. Its comments describe the template, not a complete
inventory of this repository.

```
00_sources/         originals per source type, local only where confidentiality
                    requires; unchecked, because this layer holds the original
                    everything above it is checked against
10_markdown/        Markdown representations of full texts and datasets;
                    stable anchors live here
20_distillates/     one distillate per source, one subfolder per source type
30_assertions/      assertion atoms and topic maps (MOC-*)
40_output/          the final output, one file per chapter
glossary/           one term per file: definition, wikilink hub, tag keyword
references/         bibliographic records (CSL JSON)
knowledge/          governance layer (Promptotyping documents)
tools/              validation scripts, one script per task
HOME.md             human entry point
CLAUDE.md           agent action layer (exchangeable block)
```

[ARCHITECTURE.md](../ARCHITECTURE.md) defines the current project topology.
Exact artifact paths and metadata are governed by the schema.

## 11. Instantiation

A project selects its purpose, controlled topics, source types, output genre,
working language, human verification role, and checking mechanisms.
The layer model, source anchors, check contracts, and status progression
remain invariant.

[SETUP.md](../SETUP.md) describes onboarding and the first production cycle
for this repository. Current readiness is recorded in `knowledge/state.md`.

## 12. Lineage

The design draws on source criticism's attention to the source location,
prosopography's distinction between a recorded statement and an asserted fact,
and nanopublications' pairing of assertions with provenance. Schema validation
in scholarly editing and explicit provenance in data management supply related
technical practices.

These connections explain the design's intellectual context. They do not
establish that Grounded Vault is adequate for a research task. That judgment
depends on its applied contracts and review results.
