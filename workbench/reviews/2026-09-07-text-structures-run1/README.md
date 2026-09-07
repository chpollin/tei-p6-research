# Text and Document Structures, run 1

This directory records source extraction and the subsequently required review of the twelve sources selected on 2026-09-06. The producer is GPT-6 Astra. The extraction is authored work, and no independent source-support verdict is claimed here. The root integrator arranges fresh-context review and records its model-family limitation separately.

## Scope

The source identities are the nine P5 4.12.0 Guidelines files, the pinned testoverlap document, and two citation-only GitHub threads. The 2026-09-07 intake reuses immutable representations. Full discussion bodies remain private. The section audit is a navigation and coverage record and cannot ground research claims.

The chapter audit below records all headed sections examined. Extracted means that source-specific statements were retained; it does not mean that every possible claim was extracted. Unselected illustrative details are excluded from the present claim set. Source dependencies referenced through XInclude, specification references and bibliography pointers remain separate sources and are not silently folded into chapter statements. No effective ODD compilation or independent implementation measurement was performed.

## NH section audit

All locators below refer to `P5/Source/Guidelines/en/NH-Non-hierarchical.xml` in `tei-p5-guidelines-nh-non-hierarchical-4.12.0`. The complete chapter has 49 source blocks. All blocks were read, including the worked XML and qualifications.

| Section and XML location | Disposition and retained contribution | Exclusions or open limits |
|---|---|---|
| Non-hierarchical Structures, `/div[1]`, b1–b5 | Extracted, conflict types, trade-offs, four methods and bounded example views, s1–s4 | Literary interpretation of the quoted poems excluded; sources cited by the chapter remain separate. |
| Multiple Encodings of the Same Information, `/div[1]/div[1]`, b6–b11 | Extracted, separate views, conformance, maintenance costs and the note about indirect linking through identical content, s5–s7 | Repeated poem encodings examined as examples, with no new implementation-performance claim. |
| Boundary Marking with Empty Elements, `/div[1]/div[2]`, b12–b26 | Extracted, boundary semantics, typographical versus metrical lines, custom delimiters, namespaces, explicit pairing and validation limits, s8–s16 | b24 contains the wording `fast cars` despite the preceding `trains` example; no corrected reading is substituted. Figure interpretation remains limited to its accompanying prose and encoded example. The context-dependent conformance sentence b18 is not promoted as a standalone claim. |
| Fragmentation and Reconstitution of Virtual Elements, `/div[1]/div[3]`, b27–b39 | Extracted, partial elements, inflated counts, misleading sentence labels, chaining, part ambiguity, explicit join and hierarchy reconstitution, s17–s24 | The context-dependent conformance sentence b38 is not promoted alone. No reconstruction algorithm was executed. |
| Stand-off Markup, `/div[1]/div[4]`, b40–b45 | Extracted, linked layers, offsets, discontinuity, read-only annotation, dependencies and conditional extension scope, s25–s29 | XInclude examples remain inert. Off-the-shelf processing and reported advantages are not independently measured. |
| Non-XML-based Approaches, `/div[1]/div[5]`, b46–b49 | Extracted, named alternatives and the chapter's limits of treatment, s30–s31 | The cited proposals require separate admissions before their technical merits can be established. |

## DS section audit

All locators below refer to `P5/Source/Guidelines/en/DS-DefaultTextStructure.xml` in `tei-p5-guidelines-ds-defaulttextstructure-4.12.0`. The complete chapter has 115 source blocks. All were examined, including the illustrative XML. Includes and specification groups identify separate dependencies.

| Section and XML location | Disposition and retained contribution | Exclusions or open limits |
|---|---|---|
| Default Text Structure, `/div[1]`, b1–b13 | Extracted, resource types, shared metadata, nesting, corpora, module dependency and encoder choice, s1–s8 | Included TEI, text, body and group specifications require their own distillates. |
| Divisions of the Body, `/div[1]/div[1]`, b14–b16 | Extracted, neutral division type and numbered/unnumbered alternatives, s9 | Genre examples illustrate terminology and are not separate corpus observations. |
| Un-numbered Divisions, `/div[1]/div[1]/div[1]`, b17–b20 | Extracted, att.typed relationship, s10; nested example examined | div specification is extracted separately. |
| Numbered Divisions, `/div[1]/div[1]/div[2]`, b21–b25 | Extracted, level restriction, s11; example and include group examined | Historical XML comments about div0 are excluded from normative claims. |
| Numbered or Un-numbered?, `/div[1]/div[1]/div[3]`, b26–b32 | Extracted, depth trade-off, reference labels and customization alternatives, s12–s14 | Repeated prohibition of mixing is consolidated with s9. The customization mechanism itself requires the MD chapter. |
| Partial and Composite Divisions, `/div[1]/div[1]/div[4]`, b33–b39 | Extracted, incomplete samples, the chapter's part-value wording and independent composite stories, s15–s18 | The part explanation is retained verbatim in meaning and flagged for comparison with att.fragmentable. |
| Elements Common to All Divisions, `/div[1]/div[2]`, b40–b42 | Examined, opening/closing heterogeneity and named classes | Extraction follows in the substantive child sections; effective class population remains open. |
| Headings and Trailers, `/div[1]/div[2]/div[1]`, b43–b49 | Extracted, multiple heads, parent context, encoder choice and trailer position, s19–s22 | The newspaper example supplies illustrative markup without empirical frequency claims. |
| Openers and Closers, `/div[1]/div[2]/div[2]`, b50–b54 | Extracted, provenance and grouping, s23–s24 | Name/date detail belongs to separately referenced chapters. |
| Arguments, Epigraphs, and Postscripts, `/div[1]/div[2]/div[3]`, b55–b59 | Extracted, alternative argument encodings, source grouping and postscript placement, s25–s27 | Literary content of examples excluded. |
| Content of Textual Divisions, `/div[1]/div[2]/div[4]`, b60–b63 | Extracted, module dependency and permission to mix low-level elements, s28–s29 | Includes are recorded dependencies; no full effective content model is claimed. |
| Grouped and Floating Texts, `/div[1]/div[3]`, b64–b65 | Extracted, collection versus interruption, s30 | Child sections supply examples and qualifications. |
| Grouped Texts, `/div[1]/div[3]/div[1]`, b66–b77 | Extracted, nesting, editorial alternatives and short extracts, s31–s33 | Extended anthology examples examined; no judgment that one editorial segmentation is uniquely correct. |
| Floating Texts, `/div[1]/div[3]/div[2]`, b78–b85 | Extracted, tessellation qualification, placement, alternative framing and quote distinction, s34–s38 | Example narrative interpretations remain those stipulated by the chapter. |
| Virtual Divisions, `/div[1]/div[4]`, b86–b89 | Extracted, application responsibility for generated divisions, s39 | No generation software executed; separate divGen declaration remains a dependency. |
| Front Matter, `/div[1]/div[5]`, b90–b96 | Extracted, text/header distinction, omission policy and link targets, s40–s42 | The list of suggested subdivision labels is examined but excluded from the structure claim set. Examples are illustrative; generated contents repeat the virtual-division mechanism. |
| Title Pages, `/div[1]/div[6]`, b97–b106 | Extracted, descriptive limits, non-textual content and rendition alternatives, s43–s45 | Full typographic module design and included title-page specifications remain open dependencies. |
| Back Matter, `/div[1]/div[7]`, b107–b113 | Extracted, claimed front/back content equivalence and identified page targets, s46–s47 | Suggested subdivision labels and the letter/corrigenda examples were examined but not separately distilled. Formal front/back equivalence needs specification comparison. |
| Module for Default Text Structure, `/div[1]/div[8]`, b114–b115 | Extracted, textstructure identity and dependency on module selection, s48 | Specification group references are not an executed schema. |

## Specification unit audit

Each source below is `P5/Source/Specs/<ident>.xml`, identified by its same-slug representation. All English descriptions and remarks, local declaration units and English examples were examined. Translations are excluded from this English extraction. The multilingual milestone example was also examined. Datatype and class references are declarations and carry no inferred effective semantics.

| Source and XML units | Extracted | Excluded or open |
|---|---|---|
| att.fragmentable, `/classSpec[1]/desc[1]`, `/attList[1]/attDef[1]` | Fragmentation, part description, default, complete closed value meanings and reconstitution qualification, b1/b3/b6–b8 | Referenced enumerated datatype b5 is noted but not expanded. Japanese descriptions and remarks excluded. |
| join, `/elementSpec[1]/desc[1]`, `/classes[1]`, `/content[1]`, `/constraintSpec[1]`, `/attList[1]/attDef[1..2]`, `/exemplum[1]`, `/exemplum[6]` | Discontiguity, target cardinality, result, scope alternatives/default, both English examples and local content, b3/b11–b13/b21/b29–b31/b36 | Class references, datatypes and listRef examined as dependencies; translations and translated examples excluded. No virtual-aggregate implementation tested. |
| att.global.linking, `/classSpec[1]/desc[1]`, `/attList[1]/attDef[1..8]` | All eight English attribute descriptions; copyOf, next, prev and select remarks; corresp non-substitutability example | English corresp translation example b25 and pointer datatypes examined but omitted from core claims. ListRef remains a dependency. Translations excluded. |
| milestone, `/elementSpec[1]/desc[1]`, `/classes[1]`, `/content[1]`, `/exemplum[1]`, `/remarks[1]` | Boundary, empty content, n, unnumbered and order qualifications | Multilingual example b14 combines distinct units and editions; examined as an example without a separate claim. Class/list references remain dependencies. Translations excluded. |
| pb, `/elementSpec[1]/desc[1]`, `/classes[1]`, `/content[1]`, `/exemplum[1]`, `/exemplum[3]`, `/remarks[1]` | Page beginning, empty content, edition variation, facs and specialized attributes | Class/list references remain dependencies. Translations excluded; no media alignment inferred from a pointer. |
| div, `/elementSpec[1]/desc[1]`, `/classes[1]`, `/content[1]`, `/constraintSpec[1..2]`, `/exemplum[1]` | Division, selected explicit memberships, content outline, both Schematron conditions and nested English example | Full referenced class expansion remains open. Non-English examples excluded. |
| note, `/elementSpec[1]/desc[1]`, `/classes[1]`, `/content[1]`, `/exemplum[1]`, `/exemplum[6]` | Note, local declarations, embedded translator note, responsibility resolution, numbering and omission | macro.specialPara and attribute-class semantics remain dependencies. Other-language examples excluded. |

## Additional selected sources

| Source and unit | Disposition and retained contribution | Exclusions or open limits |
|---|---|---|
| `P5/Test/testoverlap.xml`, `/TEI[1]/teiHeader[1]`, b1–b4 | Examined, placeholder title and empty metadata paragraphs | Excluded from structural claims. |
| `P5/Test/testoverlap.xml`, `/TEI[1]/text[1]/body[1]/div[1]`, b5–b12 | Extracted page beginnings outside and inside paragraphs, s1–s4; all six body paragraphs examined | The source has six body paragraphs and three header paragraphs. The selection record's nine-paragraph count is a whole-document count. No processor or historical pagination accuracy is established. Literary prose is not independently interpreted. |
| TEIC/TEI issue 1400, description and comment 4, 2015-11-10; issue labels at 2026-09-06 | Extracted three admitted short quotations, removal proposal, editing claim and dated P6 label | Claims are confined to the quotations. Full thread argument and provenance of release effects remain open. |
| TEIC/TEI issue 1505, comment 2, 2016-09-26; comment 14, 2017-05-03 | Extracted same-type target statement and attributed implementation report | No inference from closure to adoption; a released effect requires separate evidence. |

The five admitted quotations match the two local raw sources and distillates under `tools/check_wave1_sources.py` on 2026-09-07. Only `checked.quote` records this check. Source-support review remains separate. Each thread stays below 25 quoted words across its core statements.

## Prepared pairs and validation

Canonical per-source batches were emitted with `tools/review.py emit` and a path prefix without the `.md` extension. The two chapter batches contain 31 and 48 pairs. The seven specification batches contain 55 pairs, the test instance four, and the two threads five. The initial assertion batch contains 25 pairs for 24 assertions. The integrator owns the final enriched source batch and fresh-context verdicts.

The first full validator run found only missing quote check dates and integration-owned orphan/generated-region updates. After the quotation check, the two quote dates were recorded. The integrator regenerates topic maps and the source inventory before the final validation. No machine-review, human verification or successful full-vault validation date is self-assigned by the producer.

## Producer checks

The canonical cutter was run against the complete current vault on 2026-09-07 and returned no problems. The owned scope supplies 143 source pairs and 25 assertion pairs. The full validator still requires integration-owned topic-map and inventory regeneration. The producer's `git diff --check` passed.

## Produced research files

- `20_distillates/documents/tei-p5-att.fragmentable-4.12.0.md`
- `20_distillates/documents/tei-p5-join-4.12.0.md`
- `20_distillates/documents/tei-p5-att.global.linking-4.12.0.md`
- `20_distillates/documents/tei-p5-milestone-4.12.0.md`
- `20_distillates/documents/tei-p5-pb-4.12.0.md`
- `20_distillates/documents/tei-p5-div-4.12.0.md`
- `20_distillates/documents/tei-p5-note-4.12.0.md`
- `20_distillates/documents/tei-p5-guidelines-nh-non-hierarchical-4.12.0.md`
- `20_distillates/documents/tei-p5-guidelines-ds-defaulttextstructure-4.12.0.md`
- `20_distillates/documents/tei-p5-test-testoverlap-4.12.0.md`
- `20_distillates/publications/teic-tei-issue-1400.md`
- `20_distillates/publications/teic-tei-issue-1505.md`
- `30_assertions/structure-p5-has-several-nonhierarchical-methods.md`
- `30_assertions/structure-p5-join-combines-virtual-elements.md`
- `30_assertions/structure-p5-boundary-range-validation.md`
- `30_assertions/structure-p5-part-reconstitution-ambiguity.md`
- `30_assertions/structure-p5-part-positions-fragments.md`
- `30_assertions/structure-p5-part-locates-omissions-in-ds.md`
- `30_assertions/structure-p5-floatingtext-interrupts-resumable-text.md`
- `30_assertions/structure-p5-floatingtext-does-not-imply-external-origin.md`
- `30_assertions/structure-p5-div-in-line-needs-floatingtext.md`
- `30_assertions/structure-p5-div-in-paragraph-needs-floatingtext.md`
- `30_assertions/structure-p5-pb-associates-page-image.md`
- `30_assertions/structure-p5-pb-number-and-sequence.md`
- `30_assertions/structure-p5-test-page-marker-inside-paragraph.md`
- `30_assertions/structure-p5-next-same-type-recommendation.md`
- `30_assertions/structure-p5-prev-same-type-recommendation.md`
- `30_assertions/structure-p5-multiple-encoding-maintenance-cost.md`
- `30_assertions/structure-p5-composite-stories-have-flexible-order.md`
- `30_assertions/structure-p5-division-type-is-independent-of-depth.md`
- `30_assertions/structure-p5-note-responsibility-code-needs-definition.md`
- `30_assertions/structure-p5-note-number-omission-is-conditional.md`
- `30_assertions/structure-p6-numbered-divisions-reconsideration-label.md`
- `30_assertions/structure-issue1505-recommendation-self-report.md`
- `30_assertions/structure-p5-stand-off-discontinuous-annotation.md`
- `30_assertions/structure-p5-divgen-processing-is-application-defined.md`

## Chapter integration outline

The authored text waits in `chapter-draft.md` with draft status. It was removed from `40_output` because the synthesis-role contract in `knowledge/governance.md` permits composition only from validated assertions. The source-support review is pending. Passing a chapter-scoped structural check does not satisfy that prerequisite. No completed chapter is recorded by this working draft.

The bounded chapter can first establish the alternatives already documented by P5, then explain interrupted texts and virtual aggregation, then compare page beginnings with the pinned test instance. The part-value disagreement and the distinction between a same-type recommendation and a participant's implementation report should remain explicit. Reading projection policy, migration fidelity and the ranking of architectures require output posits or further evidence. The dated P6 label is a process observation only.

## Research interpretation boundaries

The chapter and class explanations of part require a paired comparison. The sources are allowed to disagree. The NH chapter supplies explicit P5 capabilities as counterevidence to any unrestricted assertion that P5 represents only one hierarchy. The image association documented for pb does not establish image alignment. The run supplies no architecture ranking or measured usability claim.
