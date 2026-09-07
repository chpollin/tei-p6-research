---
title: Experiments
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
related: [text-model, model-design, model-examples, ontology, text-model-bindings, p6-architecture, testing, verification, state]
---

# Experiments

Executable schemas, converters, fixtures, and reports require explicit
artifact contracts before dedicated directories are created. Those contracts
must state canonical inputs, generated outputs, authority, versioning,
validation, and whether an artifact is hand-authored or derived. Experiment
reports are not Vault grounding sources.
The documentary ontology and its syntax/hierarchy checks have a separate
contract in [[knowledge/ontology]]. The six illustrative instance cases have
cross-view tests under [[knowledge/model-examples]]; those tests establish the
specified record correspondence and selected counterexamples, without adding
P5 migration coverage or an ontology-to-instance binding.

This document holds the contracts of the text identity pilot, the editorial
case study of one diary, and the P5 specification navigation projection. The
contract of Abstract Text Model 0.1, with its requirement and test ledger,
its run commands and its human acceptance items, is in
[[knowledge/text-model]]. Current completion and human-review state belong
only in [[knowledge/state]].

The illustrative sentence and the historical, cultural and fictional place
cases in [[knowledge/model-examples]] apply [[knowledge/model-design]] as
design walkthroughs. They specify
distinctions to challenge with future experiments and are not executed fixtures
or observations about named people's lives. Their source leads and conceptual
diagrams add no cases to the existing experiment reports.

## Reproduction

Each contract below carries the run commands of its own experiment. This
section collects the reproduction checks whose contracts live outside this
document and the rules that hold for all of them. None of these commands
assigns research status. On Windows with the Python launcher, `py -3` can
replace `python`.

Abstract Text Model 0.1, whose independent case gate needs no raw corpus,
reproduces with these commands.

```powershell
python tools/check_abstract_text_v01.py --check
python tools/check_entities_v02.py --check
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
acceptance questions are in [[knowledge/text-model]].

The first research wave provides three read-only reproduction checks.

```powershell
python -m tools.tei.build_atlas --output corpus/projections/p5-specs-4.12.0.json --check
python tools/check_wave1_sources.py .
python tools/check_wave1_sources.py . --review-only
```

Run 2 of Metadata and Entities admits nine document sources and three
citation-only threads.

```powershell
python -m tools.ingest_git_blobs . --run entities-run2 --check
python tools/check_wave1_sources.py . --manifest sources/manifests/2026-09-06-entities-run2-citations.yaml --references references/entities-run2.json
```

`--run` selects an admission run and defaults to the first entity run. The
citation check reconciles the six raw thread snapshots and reports the threads
as pending until their distillates exist.

The atlas check requires the locked local TEI Git mirror. Omit `--check` to
regenerate the projection after an intentional generator or control-input
change. The quotation check requires the local raw snapshots named in
`sources/manifests/2026-09-05-research-wave-1-citations.yaml`. It performs no
network retrieval and fails clearly when a snapshot is unavailable, so a clean
checkout without ignored raw data can inspect the recorded intake but cannot
claim to have rerun quotation fidelity. `--review-only` needs no ignored
originals. It checks the canonical source-support prompts recorded in
`workbench/reviews/2026-09-05-wave1/pairs.jsonl`, their exact dependency
coverage and their passing verdict hashes. Continuous integration runs this
check separately from the local raw-source quotation check.

After an intentional experiment or contract change, regenerate the text
identity report with `python -m tools.pilots.text_identity`. Changed research
claims require fresh review pairs from
`python tools/check_text_identity_pilot.py --emit-review` and an independent
reviewer under [[knowledge/verification]].

## Text identity and annotation pilot

The pilot is an independent modeling experiment at contract version 1. It is
not an official TEI P6 specification. The working language is English.

### Question and bounded scope

What must distinguish a text, a text version, a region, and an annotation so
that annotations remain auditable when text changes? This pilot compares two
region selectors on finite Unicode strings. It does not define text in general,
infer authorial intention, implement collaborative editing, or demonstrate
real-world P5 migration. All example instances are explicitly synthetic.

The evidence branch reports only what selected specification files in TEI P5
4.12.0 say. The experiment branch proposes independent semantics. Similar names
do not establish equivalence between P5 constructs and pilot objects. The
[model proposal](../40_output/02-abstract-model.md) now incorporates these
source findings into the broader 0.1 and 0.2 definition. The initial pilot
defined here retains its own narrower contract, including the exclusion of
empty regions and textual points. Its support audit covers only the original
four assertions and three distillates, regardless of later chapter growth.

### Candidate definitions

- **Text:** an identified editorial grouping of versions. The criterion for
  treating those versions as one text is an assumption outside this prototype;
  it is not inferred from equal character content.
- **Text version:** an identified immutable Unicode string associated with one
  text, carrying a SHA-256 of its UTF-8 bytes and optionally one parent version
  of that same text. A parent relation must be acyclic.
- **Region:** an identified target specification containing a version reference
  and a selector. The selector describes a target; resolution returns an
  interval in that version. Distinct region records may resolve to the same
  interval without becoming the same record.
- **Annotation:** an identified record carrying an interpretation body and a
  reference to one region. Different annotations may overlap or disagree; the
  prototype checks their structure, not the consistency of their interpretations.

The pilot's positions count Unicode code points, not bytes, UTF-16 units, or
grapheme clusters. Strings are not normalized implicitly. End positions are
exclusive. Empty regions and discontinuous regions are outside this first
experiment. IDs are unique within an experiment instance. The text/version
relationship is an explicit editorial assignment, not a conclusion the
validator can infer. One text per version, at most one parent, and one region
per annotation are experimental limits, not claims about all textual
traditions or editing tasks.

Immutability is a contract on versions and on the nonmutating operations in this
prototype. Hash checks detect disagreement between a supplied string and its
declared hash. They cannot detect a historical rewrite if somebody replaces
both string and hash; that requires a trusted persistent version history, which
this pilot does not implement.

### Two selector alternatives within one object model

Both alternatives retain the four candidate object definitions. They compare
target resolution, not competing ontologies of text or complete architectures.

**A — Version-bound position:** the selector supplies `start` and `end`, plus
an exact quote used as an integrity check against that range.

**B — Version-bound quotation:** the selector supplies a nonempty exact quote,
optionally qualified by immediately adjacent prefix and suffix. Resolution
must yield exactly one matching range; zero and multiple matches are explicit
failures. Context is literal and case-sensitive.

Both alternatives require version identity. B is not presumed superior:
repeated quotations can be ambiguous, and edits can destroy its context. A is
simple and deterministic on a fixed version but cannot reuse positions safely
on an edited version. A separate reanchoring operation searches an explicitly
chosen destination version and returns candidates or absence/ambiguity. It
does not mutate the original annotation or claim that a surviving quotation
retains the same interpretation.
An `absent` result means no match for the retained selector, including its
context requirements; it does not necessarily mean the quotation was deleted.

### Formal experiment contract

Inputs are `experiments/text_identity/spec.json` and `cases.json`. The runner
is `python -m tools.pilots.text_identity`; `--check` compares its deterministic
report with the checked-in `report.json` and fails on drift. The ordinary run
regenerates that report. The runner must fail if any case differs from its
declared expected diagnostics or resolution. All report inputs, including the
implementation and contract, are identified by SHA-256; wall-clock times and
machine-specific absolute paths are excluded from generated output.

The documentation fingerprint covers only this second-level section, from
`Text identity and annotation pilot` to the next second-level heading.
Its line endings are normalized; unrelated experiment descriptions do not
invalidate this report. A missing or duplicated section heading fails the
check. The report names this scope explicitly in `input_scopes`.

Required constraints include unique IDs, resolvable references, text/version
ownership, hash fidelity, acyclic version ancestry, selector type and bounds,
exact-quote fidelity, and explicit quotation ambiguity. Malformed objects must
produce diagnostics rather than uncaught exceptions. Diagnostic codes and case
IDs provide stable links between the contract, fixtures, and tests.

Required cases include valid fixed-version annotation; insertion before a
region; edit within a region; deletion; repeated quotation; disambiguation by
context; overlapping annotations; Unicode positions and normalization
differences; invalid bounds; broken references; duplicate identity; changed
version content; a version-parent cycle; and an unchanged quotation at unchanged
positions in a changed interpretative context. Counterexamples must test the
assumptions of both alternatives, not merely the implementation's happy path.

### Acceptance procedure

Start with the four pilot definitions above and the cases below. The
[model proposal](../40_output/02-abstract-model.md) provides the broader
conceptual context and has a separate acceptance scope. The machine-readable
[report](../experiments/text_identity/report.json) gives actual results by
case ID; [cases.json](../experiments/text_identity/cases.json) supplies the
hand-authored expected outcomes independently of report generation.

| Case to inspect | Input or change | Expected behavior to assess |
|---|---|---|
| `reanchor-insertion` | `The red fox.` becomes `Now: The red fox.` | The old `red` target remains `[4,7)` in v1; `[9,12)` in v2 is proposed with `accepted: false`. |
| `reanchor-repeated` | The new version contains `red red` | Both `[0,3)` and `[4,7)` are candidates; neither is chosen. |
| `reanchor-deletion` | `red` disappears in `The fox.` | No new target is proposed; the old annotation remains auditable. |
| `normalization-quotation` | A composed quote is searched in decomposed Unicode text | Literal matching fails explicitly; no hidden normalization occurs. |
| `reanchor-context-loss` | The quote survives but its required adjacent context changes | `absent` reports failure of the retained selector, not deletion of the quote. |
| `surviving-quote-changed-interpretation-position` and `surviving-quote-changed-interpretation-quotation` | `The red fox.` becomes `The red car.`; an old annotation interprets `red` as fur color | Both selectors resolve `red` at `[4,7)`; reanchoring proposes that interval with `accepted: false`. Matching cannot establish that the old interpretation fits. |

These are normative expectations of the experiment, not observations of real
editorial practice. A reviewer can reject an expectation even when the code
implements it correctly.

Read the paired cases as a comparison of explicit commitments: position
selection checks a supplied interval; quotation selection must distinguish
matches. Neither operation evaluates the annotation's interpretation. The
fur-color example stipulates an editorial reason to reject reuse; that reason
is not a semantic judgment performed by the runner. These cases test a boundary
of both selectors and do not establish a general winner.

Run the technical gate from the repository root:

```powershell
py -3 tools/check_text_identity_pilot.py
```

On systems with Python on PATH, use `python` instead of `py -3`. This command
validates the full vault and pilot chapter, rechecks source admission integrity,
checks current review-pair coverage and hashes, checks the source control plane,
reproduces the model report, and runs the complete test suite. It does not
modify research statuses or approve the model. The normal CI check runs it too.

| Machine check | What it establishes | What it does not establish |
|---|---|---|
| Source bytes, commit, license records and representation regeneration | The admitted passages reproduce the declared source snapshot | Whether the source is correct or the sample is representative |
| Layer, anchor, status and chapter checks | The claimed provenance chain is structurally well formed | Whether every natural-language conclusion follows |
| Independent support review, prompt hashes and dependency coverage | Recorded judgments refer to the current source/claim pairs | Human expert verification or philosophical agreement |
| Type, reference, ownership, hash, bounds and cycle constraints | An instance satisfies the pilot's executable rules | A proof of a universally adequate ontology |
| Adversarial fixtures, type-strict expected results and report regeneration | Implementation behavior matches the declared finite examples | Real-world usability, complete P5 migration or all possible cases |

Technical acceptance requires the full vault validator, chapter-scoped
validator, source-control validator, independent support-pair review, pilot
checks, full test suite, reproducible generated pages, and `git diff --check`.
A green report establishes agreement with these finite contracts; it is not
a proof of universal expressivity, philosophical correctness, or usability.

The human reviewer then records **accept**, **revise**, or **defer** for each:

1. Are the four candidate definitions intelligible, and are their identity
   assumptions acceptable for this bounded experiment?
2. Do the admitted passages support the chapter's P5 statements without
   silently extending their authority to the pilot's semantics?
3. Are the examples and expected outcomes sensible? Inspect insertion, repeated
   quotation, normalization, deletion, context loss, and the surviving quotation
   with changed interpretation, including failures.
4. Are both alternatives represented fairly, and is the reanchoring proposal
   clearly distinct from an accepted interpretation?
5. Is the evidence sufficient to justify a next experiment? Name a real editorial
   task, the expected outcome, and an observation that would require revising
   one of the candidate definitions.

Acceptance means this pilot is an adequate basis for further research. It does
not approve a final P6 model or confer `verified` on research artifacts. The
reviewer should return a decision and reasons for each of the five items. Full
acceptance requires all five to be accepted; mixed decisions remain a partial
review with named revisions or missing evidence in [[knowledge/state]].
Accepting the experiment does not choose selector A or B.

### Evidence and audit entry points

- [Model proposal](../40_output/02-abstract-model.md) separates grounded premises and model posits, with a broader scope than this pilot audit.
- [Source admission manifest](../sources/manifests/2026-09-05-text-identity-pilot-admission.yaml) records exact source, rights, hashes and scope.
- [Support-review audit](../workbench/reviews/2026-09-05-text-identity/README.md) describes review inputs, verdicts and limitations.
- [Experiment specification](../experiments/text_identity/spec.json) defines object fields and diagnostic codes.
- [Generated report](../experiments/text_identity/report.json) exposes actual case outcomes and input hashes.

## Editorial case study of one diary and three fragments

This experiment compares two representations of actual editorial XML for
specified inspection tasks and documents a refused migration. The sample does
not represent TEI practice generally. Requirements and interpretations are
project posits. The experimental reports are not Vault grounding sources.
The three source observations enter the canonical chain
through the [diary distillate](../20_distillates/documents/humboldt-h0017682-7d174637.md)
and its assertions.

### Source and rights

The source is the England travel diary H0017682 in *edition humboldt digital*,
dataset 11.0.1, at repository commit
`7d174637d0b2cf56edaacac3b5e7e283e8ba8245`. All three fragments come from the
same file, `data/travel-journal/H0017682.xml`. The complete XML is retained in the immutable
[Markdown representation](../10_markdown/documents/humboldt-h0017682-7d174637.md),
alongside exact fragment reading blocks. The source XML SHA-256 is
`89ac55d98d4756cb8ffce59f958d5c6885c8dc22e47e250b1ccd58386e516a54`.

The source is attributed to *edition humboldt digital*, Berlin-Brandenburgische
Akademie der Wissenschaften, 2025. Its XML names two editors and one
contributor. The attribution with their names is research data and is
recorded in the `attribution` field of the
[report](../experiments/editorial_cases/report.json) and in the rights record
of the [completed manifest](../sources/manifests/2026-09-05-editorial-cases.yaml).
The source XML, reproduced excerpts, and adapted source material retain
[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/), as declared in
the [pinned dataset README](https://github.com/telota/edition-humboldt-digital/blob/7d174637d0b2cf56edaacac3b5e7e283e8ba8245/README.md).
Task projections change whitespace and omit specified note text from the main
reading. Those are adaptations, not verbatim transcriptions. The repository's
general authored-content license does not replace the source license.

The [intake](../experiments/editorial_cases/intake.json) and
[completed manifest](../sources/manifests/2026-09-05-editorial-cases.yaml)
record exact responses, hashes, dates, fragment locators, and acquisition gaps.
The acquired README, citation record, complete diary XML, and RNG schema form
the declared four-response boundary. Their acquisition does not make the wider
real-world customization family complete. Dataset release identity, the XML
header's edition citation, and acquisition date remain distinct metadata.
XML and RNG parsing succeeded. Full Relax NG validation did not produce a
result within the bounded attempt and remains untested. Embedded Schematron
and effective ODD conformance were not established.

### Question and comparison contract

The task is to inspect textual order, hierarchy, note responsibility, and
selected boundary information without silently erasing a distinction. The
[protocol](../experiments/editorial_cases/protocol.json) deliberately selects
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

### Three cases and their outcomes

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

The separate [[knowledge/text-model-bindings|JSON, XML, and YAML bindings]]
exchange the resulting core model package. Preserving that package across
serializations does not establish preservation during the initial P5 mapping.

The third fragment was evaluated after the mapper and its tests were frozen.
The [freeze record](../experiments/editorial_cases/mapping-freeze.json)
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

### A separate identity experiment

The optional [editorial provenance profile](../experiments/editorial_cases/profile.json)
tests whether a historical hypothesis can change while the version it concerns
remains fixed. Its independently authored
[identity cases](../experiments/editorial_cases/identity-cases.json) are
synthetic. They must not be read as reconstructed transmission history for
the diary.

The central example keeps B's version record and its annotations unchanged
while an editor replaces the hypothesis `B derives from A` with `B derives
from C`. A new attributed claim supersedes the old claim. Both remain stored.
Other agents' claims can remain current. The profile checks append-only history
and valid supersession. It does not establish historical truth, supply external
evidence semantics, or make the core's technical `parents` field revisable.
Bare withdrawal, negative claims, and cross-agent supersession remain outside
this profile. The profile's rules are defined in section 4 of the
[[knowledge/text-model|text model]].

### Reproduce and review

Run from the repository root.

```powershell
py -3 tools/ingest_editorial_cases.py --check
py -3 tools/check_editorial_cases.py --check
py -3 -m pytest tests/models/test_editorial_profile.py tests/tei/test_editorial_cases.py
```

The deterministic [report](../experiments/editorial_cases/report.json)
contains complete expected/actual comparisons, fingerprints, independent
identity cases, and a separate holdout migration result. Omit `--check` only
when intentionally regenerating it after a reviewed input change. Current
execution dates, aggregate counts, and acceptance state belong in
[[knowledge/state]].

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

## P5 specification navigation

The provisional JSON artifact is `p5-spec-navigation`, version 1, generated at
`corpus/projections/p5-specs-4.12.0.json`. It is a specialization of the existing
corpus projection plane and not a formal P5 metamodel or evidence artifact.

Canonical inputs are the release lock, its completed Git manifest, the hashed
tree inventory, and the corresponding local Git blobs at the full locked
commit. Every record identifies the source path, blob, SHA-256, and XML locator.
No system date, absolute machine path, or network response enters its output.

The boundary is top-level `P5/Source/Specs/*.xml`. Records describe specification
kind and identity, declared module, direct class membership, locally declared
attributes, content structure, local constraints, and recognized structural
references. Reference lookup reports unresolved targets and distinguishes its
limited inventory scope from invalidity in a compiled P5 schema.

Excluded are module declarations outside that directory, inherited/effective
attribute and content models, customization compilation, evaluation of
constraints, examples, Guidelines prose, and interpretation of semantic
equivalence. Their omission must remain explicit in the output. No broad
architectural conclusion follows from a declaration count.

The generator owns the JSON; hand editing is prohibited. Acceptance requires
identical clean rebuilds, source identity checks, useful invalid-input tests,
and source locators for every extracted record. A missing ignored mirror is a
materialization prerequisite and must fail clearly instead of producing a
partial artifact labeled complete.

Build the projection with `py -3 -m tools.tei.build_atlas --output
corpus/projections/p5-specs-4.12.0.json` and append `--check` for a read-only
byte comparison. Both require the locked local Git mirror.

## Identität und Quellenbezug an Katalog und Korrespondenz

Der Nutzer benannte Stefan Zweig Digital und das Hugo Schuchardt Archiv als
reale Prüfumgebungen und delegierte die Beantwortung der fachlichen Fragen.
Die Auswahl umfasst zwei Einträge des Zweig-Werkkatalogs und drei Kontexte
des Schuchardt-Briefs 4493. Das Protokoll unter
`experiments/identity_evidence/protocol.json` hält Auswahl, Anforderungen und
Grenzen fest. Beide Quelldokumente wurden vor der Implementierung eingesehen.
Es gibt keinen verdeckten Prüffall und keinen unabhängigen Quellenleser.

Die Aufnahme unter `sources/manifests/2026-09-07-identity-evidence.yaml`
fixiert zwei vollständige XML-Antworten mit Prüfsummen und fünf exakten
Byteintervallen. Die Repräsentationen enthalten die unveränderten Originale.
Beide XML-Header erklären CC BY-NC 4.0. Die vollständigen Header bleiben als
Attribution erhalten; die Projektlizenzen ersetzen diese Quellenlizenz nicht.
Bilddaten, Personenregister, weitere Briefe und ODDs gehören nicht zur Aufnahme.

Die fachlichen Arbeitsentscheidungen und der Profilvertrag stehen in
[[knowledge/identity-evidence]]. Der Versuch erhält zwei materielle
Katalogobjekte mit gemeinsamer berichteter Werkzuordnung, die unsichere
Handschriftzuschreibung und die gesonderte Mitwirkungsangabe. Datumszeile,
Entstehungsmetadaten und Korrespondenzmetadaten erhalten eigene Belegstellen.
Die Importverantwortung bezeichnet die Übernahme durch den Agenten und
behauptet keine persönliche Urheberschaft am ursprünglichen Katalogbefund.

`tools/check_identity_evidence.py` erzeugt aus den festgelegten Ausschnitten
ein Dossier auf Modell 0.2 und prüfbare Ansichten der Quellenberichte. Vier
synthetische Fälle führen die Arbeitsentscheidungen für korrigierte und
normalisierte Transkriptionen, gleiche Zeichen in getrennten Versionen und
die fehlende automatische Gruppierung von Entwurf und Ausfertigung aus.
Sie dokumentieren gewählte Modellpolitik und keine Überlieferungsbefunde
über die aufgenommenen Quellen. Im dritten Fall beweist eine unveränderte
Versionsanzahl keine Identität der Textzeugen; sie zeigt das Ausbleiben
einer automatischen Zusammenlegung im konstruierten Beispiel.

Ein absichtlich unzutreffender Aussageinhalt bleibt bei exaktem Quellenzitat
formal gültig. Dieser Gegenfall begrenzt den Anspruch des Validators.
Weitere Tests verändern Quellenhash, Ausschnitt, Belegwortlaut,
Verantwortlichkeit und Revisionsgeschichte. Eine synthetische Bewertung
durch einen zweiten Agenten lässt die Quellenzuschreibung unverändert.

Die wissenschaftlichen Befunde gehen separat durch zwei Destillate und sechs
Assertions. Sie behalten `grounded`, bis unabhängige Quellenprüfung und die
erforderliche formale Prüfung eine höhere Stufe tragen. Die vorbereiteten
Prüfpaare liegen unter `workbench/reviews/2026-09-07-identity-evidence/`.
Das Experiment selbst steht außerhalb dieser Grounding-Kette.

```powershell
python -m tools.ingest_identity_evidence --check
python -m tools.check_identity_evidence --check
python -m pytest tests/models/test_identity_evidence.py -q
```

Diese Reproduktion benötigt keinen Netzwerkzugriff und keine ignorierten
Originaldateien. Umfang, aktuelle Resultate und offene Prüfstände stehen in
[[knowledge/state]]. Vollständige Editionsmigration, historische
Handidentifizierung, tatsächlicher Versandtag und allgemeine Werkontologie
bleiben außerhalb des belegten Ergebnisses.

## Ein vollständiger HSA-Brief als P5/P6-Fall

Der [HSA-Fall 4493](../experiments/hsa_letter_4493/README.md) wendet die
dokumentarische Ontologie auf den bereits aufgenommenen Brief an. Sein
in [[knowledge/hsa-profile]] gepflegtes Profil beschreibt die vollständige Zeichenprojektion des Briefs,
separate editorische Notes, ausgewählte Metadaten und Personenverweise.
Die Quellenfassung wird aus der unveränderlichen Repräsentation reproduziert.
Die Übernahme erfordert keinen erneuten Netzwerkabruf.

Der Generator `tools/build_hsa_case.py` besitzt die XML-/JSON-/RDF-Instanzen,
die rekonstruierte P5-Quelle, das ergänzende Fallvokabular, den
Abdeckungsbericht und das Instanzdiagramm. `p6.*` enthält die semantischen
Records; `preservation.*` ergänzt die Erhaltungsdaten. Ihre Vereinigung
rekonstruiert den vollständigen Fallgraphen. Die handgeschriebene Fall-README
erklärt die Abgrenzung und fachliche Bewertung. Die XML-/JSON-Bindings dieses
Falls und die Ontologie-Serialisierungen sind unterschiedliche Verträge.

Die Prüfung unterscheidet exakte Dateierhaltung, die erklärte Übernahme von
P5-Strukturen und die Interpretation ausgewählter Angaben als Propositionen.
Quellenhash, XPath, Verantwortlichkeit und `report`-Haltung machen die
Übernahme nachprüfbar. Die Herkunft des beschriebenen Trägers begründet keine
automatische Zuschreibung eines Schreibereignisses. Leere Empfangsangaben,
unklare Hervorhebungen und unterschiedliche Identifikatoren werden erhalten.

```powershell
python tools/build_hsa_case.py --check
python -m pytest tests/test_build_hsa_case.py -q
```

HSA-ODD-Validierung, Quellenregisterauflösung, Faksimileprüfung und eine
allgemeine Rückkonvertierung bleiben außerhalb des Fallvertrags. Die
aufgenommenen Quellen behalten ihren bisherigen Prüfstatus. Der Fall und sein
technischer Bericht sind Entwurfsartefakte außerhalb der Grounding-Kette.
Tatsächlich ausgeführte Prüfungen stehen in [[knowledge/state]].
