# Editorial case study of one diary and three fragments

This experiment compares two representations of actual editorial XML for
specified inspection tasks and documents a refused migration. The sample does
not represent TEI practice generally. Requirements and interpretations are
project posits. The experimental reports are not Vault grounding sources.
The three source observations enter the canonical chain
through the [diary distillate](../../20_distillates/documents/humboldt-h0017682-7d174637.md)
and its assertions.

## Source and rights

The source is the England travel diary H0017682 in *edition humboldt digital*,
dataset 11.0.1, at repository commit
`7d174637d0b2cf56edaacac3b5e7e283e8ba8245`. All three fragments come from the
same file, `data/travel-journal/H0017682.xml`. The complete XML is retained in the immutable
[Markdown representation](../../10_markdown/documents/humboldt-h0017682-7d174637.md),
alongside exact fragment reading blocks. The source XML SHA-256 is
`89ac55d98d4756cb8ffce59f958d5c6885c8dc22e47e250b1ccd58386e516a54`.

The source is attributed to *edition humboldt digital*, Berlin-Brandenburgische
Akademie der Wissenschaften, 2025. It names editors Dominik Erdmann and Christian
Thomas and contributor Florian Schnee. The source XML, reproduced excerpts,
and adapted source material retain
[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/), as declared in
the [pinned dataset README](https://github.com/telota/edition-humboldt-digital/blob/7d174637d0b2cf56edaacac3b5e7e283e8ba8245/README.md).
Task projections change whitespace and omit specified note text from the main
reading. Those are adaptations, not verbatim transcriptions. The repository's
general authored-content license does not replace the source license.

The [intake](../../experiments/editorial_cases/intake.json) and
[completed manifest](../../sources/manifests/2026-09-05-editorial-cases.yaml)
record exact responses, hashes, dates, fragment locators, and acquisition gaps.
The acquired README, citation record, complete diary XML, and RNG schema form
the declared four-response boundary. Their acquisition does not make the wider
real-world customization family complete. Dataset release identity, the XML
header's edition citation, and acquisition date remain distinct metadata.
XML and RNG parsing succeeded. Full Relax NG validation did not produce a
result within the bounded attempt and remains untested. Embedded Schematron
and effective ODD conformance were not established.

## Question and comparison contract

The task is to inspect textual order, hierarchy, note responsibility, and
selected boundary information without silently erasing a distinction. The
[protocol](../../experiments/editorial_cases/protocol.json) deliberately selects
challenge cases. A source reader authored text and markup expectations before
mapper construction. A separate implementer received only the two development
fragments. The integrator translated the stated expectations into executable
checks. That translation is not independent domain verification.

The baseline retains a parsed XML tree with separate note and line-break
observations. For supported input, the candidate constructs a versioned primary
sequence, an attributed reading, selections, and annotation records under the
`tei-fragment-0.1` metadata binding. Both expose observations for comparison.
This study evaluates these two small implementations, not production P5
software against a complete alternative architecture.

For the development tasks, the declared projection excludes notes from the
main sequence, collapses Unicode whitespace, and trims its ends. It retains
note bodies separately. This is our task policy, not an assertion about the
edition's reading interface or a deficiency of P5 mixed content. Source bytes
remain available separately. Neither representation claims a lexical XML round
trip. Entity spellings, attribute order, quote
styles, and namespace prefix choices are not preserved by the parsed baseline.

## Three cases and their outcomes

| Fragment | Required observation | Parsed-tree baseline | Sequence-and-reading candidate |
|---|---|---|---|
| `case-1-hierarchy` dated heading | Read “Bäder in Derbyshire”. Retain date, highlighting, place metadata, nesting, and distinct equal-extent occurrences. | Preserves the specified observations. | Preserves the same observations through reading nodes and the explicit annotation binding. |
| `case-2-interrupted-heading` heading with nested notes | Read “Reise. 1790. England.” and inspect “6255” and the editorial explanation separately. Retain line break, nesting, responsibility, and reciprocal references. | Preserves the specified observations under the declared projection. | Preserves the same observations under the declared projection and binding. |
| `case-3-holdout-media` paragraph with page break and foliation | Keep prose distinct from “16.” and retain the page/foliation distinction and image-pointer value. | Retains the XML constructs, but its frozen primary-text projection fails the expected prose-only result. No media semantics are established. | Refuses unsupported `pb` and `fw` and returns no package. This is a migration failure with an explicit diagnostic boundary. |

The two development comparisons agree on their specified observations. This
does not identify an expressivity winner. In the first case, the heading, date,
and outer highlighting share an extent but retain separate identities and
parent relationships. In the second, an unknown-hand note containing “6255”
remains separate from its nested editorial explanation marked `resp="#CT #DE"`.
Pointers and responsibility values are retained lexically, without external
resolution, referent verification, or an inferred identity of the unknown hand.

The candidate requires a decoder for the binding's typed metadata. It connects
element records with nodes and selections and validates those connections.
Note nesting and references are encoded inside annotation bodies, not as core
Relation records. Base v0.1 validation treats a body as a string and does not
check its TEI meaning. The chosen main-text projection accommodates the
contiguous-node constraint. It does not demonstrate support for arbitrary
discontinuous source structures.

The separate [JSON, XML, and YAML bindings](serialization-bindings-v0.1.md)
exchange the resulting core model package. Preserving that package across
serializations does not establish preservation during the initial P5 mapping.

The third fragment was evaluated after the mapper and its tests were frozen.
The [freeze record](../../experiments/editorial_cases/mapping-freeze.json)
records their hashes and the disclosure boundary. The mapper author did not
see the fragment during development, but the integrator and source reader did,
and the overall design already knew the problem family. This is an adverse
implementation check, not a statistically independent architecture test.

The report's passing holdout gate means that the unsupported input was refused
explicitly. It does **not** mean the third case migrated successfully. The
baseline's retained XML likewise does not make its task projection correct.
Neither implementation demonstrated image alignment or resolved `#f0018` to an
external image. An unresolved pointer in this experiment is not evidence that
the source edition lacks an image.

## A separate identity experiment

The optional [editorial provenance profile](../../experiments/editorial_cases/profile.json)
tests whether a historical hypothesis can change while the version it concerns
remains fixed. Its independently authored
[identity cases](../../experiments/editorial_cases/identity-cases.json) are
synthetic. They must not be read as reconstructed transmission history for
the diary.

The central example keeps B's version record and its annotations unchanged
while an editor replaces the hypothesis `B derives from A` with `B derives
from C`. A new attributed claim supersedes the old claim. Both remain stored.
Other agents' claims can remain current. The profile checks append-only history
and valid supersession. It does not establish historical truth, supply external
evidence semantics, or make the core's technical `parents` field revisable.
Bare withdrawal, negative claims, and cross-agent supersession remain outside
this profile.

## Reproduce and review

Run from the repository root.

```powershell
py -3 tools/ingest_editorial_cases.py --check
py -3 tools/check_editorial_cases.py --check
py -3 -m pytest tests/models/test_editorial_profile.py tests/tei/test_editorial_cases.py
```

The deterministic [report](../../experiments/editorial_cases/report.json)
contains complete expected/actual comparisons, fingerprints, independent
identity cases, and a separate holdout migration result. Omit `--check` only
when intentionally regenerating it after a reviewed input change. Current
execution dates, aggregate counts, and acceptance state belong in
[`knowledge/state.md`](../../knowledge/state.md).

Human review should decide whether the declared reading projection fits the
task, whether retained metadata supports the required interpretation, and
whether the profile's distinction between technical records and historical
hypotheses is usable. A reviewer should then choose an unselected example
that challenges those decisions. Successful automatic checks establish only
the specified outcomes. They do not establish editor efficiency, learnability,
community preference, general ontology quality, full P5/ODD conformance, or
whole-document migration fidelity.

The next study should add other editions and text forms, independent editorial
requirements, and comparable authoring and correction tasks. A claim that one
architecture is preferable requires preservation and cost evidence beyond
these three fragments. Retaining P5, extending it compatibly, replacing an
architectural component, and deferring an unsupported requirement all remain
open options.
