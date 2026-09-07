---
title: State
project:
  name: "TEI P6 Research"
  repository: "tei-p6-research"
method:
  name: Promptotyping
  url: https://dhcraft.org/Promptotyping/
status: draft
language: en
created: "2026-09-04"
updated: "2026-09-07"
related: [INDEX, plan, handoff, operations, journal]
---

# State

This file records current holdings, checks and open work. Update it when those
facts change. Stable contracts and historical decisions remain in their own
documents, the milestones in [[knowledge/plan]] and open handoff points in
[[knowledge/handoff]].

## Current checkpoint

| Area | State | Evidence |
|---|---|---|
| English Guidelines reference | bounded source intake complete on 2026-09-07; systematic distillation open | `sources/manifests/2026-09-07-guidelines-4.12.0-admission.yaml` records 888 immutable XML representations, 20 reused and 868 new, including all 24 main chapters and 846 specifications; 883 local XML XIncludes resolve within the intake and 59 graphic references match the pinned Git inventory. The generated coverage maps all 40 published contents entries to sources and confirms their filenames in the recorded release ZIP inventory. Expected HTML pages for `re.xml` and `teidata.key.xml` are absent from that inventory and remain explicit mismatches. Twenty sources in this baseline have existing distillates; no new distillates, assertions, section-level scholarly reviews or human verification were created. Reproduction with `--check` passed. The public HTML/source semantic reconciliation remains open. |
| Local repository | ready | branch `main`; scaffold, collector, workbench and repair commits exist |
| GitHub remote | ready | public `chpollin/tei-p6-research` repository configured as `origin` |
| Knowledge base | restructured and consolidated on 2026-09-06 | every knowledge document lives in `knowledge/` under the Promptotyping convention with `INDEX.md` as hub; the root holds only README, CONTRIBUTING, the two adapters and the licence and citation files after SETUP, HOME and NOTICE were folded into README and the knowledge documents; the method rationale lives in the schema and architecture documents, the RDF export in the bindings document, the selection tables of the topic runs as records under `workbench/selections/`, and the journal carries a fixed entry form; `PLAN.md`, `EXPOSE.md`, `ARCHITECTURE.md`, `contexts/`, `workflows/`, the concept, runbook, corpus-profile, primary-source and completeness documents and `docs/p6/research-agenda.md` were absorbed and deleted; the case-only rename of `knowledge/index.md` to `knowledge/INDEX.md` is recorded in Git |
| P5 4.12.0 identity | resolved | full release commit recorded in `sources/locks/tei-p5-4.12.0.yaml` |
| P5 4.12.0 acquisition | partial | pinned Git tree and official release ZIP are complete; the TEIC/TEI mirror was re-acquired locally on 2026-09-06 (`sources/manifests/2026-09-06-teic-tei-p5-4.12.0-r2.yaml`, tag `P5_Release_4.12.0` resolves to the locked commit); the published-HTML boundary still needs an explicit reconciliation against the ZIP before the family label can return to `observable-complete` |
| Public TEIC Git corpus | observable-complete | all 41 repositories exposed by the organization census are mirrored at full HEAD commits; 25,415 tree entries inventoried |
| TEI-L mailing-list archive | partial | Penn State archive `bounded-complete` for December 2025 to September 2026 on 2026-09-06 (267 messages, metadata only, no sender fields); Wayback coverage of the retired Brown archive measured for all 432 months from 1990 to 2025 (368 captured, 64 missing, each missing month recorded as a gap); the fetch of captured months through the Wayback Machine and the export request to the TEI Consortium remain open |
| TEI website records | partial | the website Git repository is inventoried, but the registered page-snapshot boundary has not yet been acquired |
| GitHub work-item corpus | partial | both stages ran on 2026-09-06 under the authenticated session: the REST snapshot (2,476 issues, 455 pull requests, 19,565 issue comments, 1,258 reviews, 1,259 review comments, 74,981 timeline events) and the GraphQL relations stage (16,003 relations and 674 review threads over all 2,931 items, no gap, 253 rate-limit points); the boundary is complete in substance, while the family label stays `partial` because the recorded REST manifest still names the relations stage as its gap, which the next REST snapshot removes; bodies stay in the private raw store |
| Governance corpus | partial | 206 Council pages and 225 Board targets observed; inaccessible historical links and external working documents remain explicit gaps |
| Historical TEI Archive | partial | 394 index/page responses acquired; 363 linked non-HTML artifacts are in reconciliation |
| Legacy SourceForge | partial | tracker API boundary `observable-complete` on 2026-09-06 under adapter version 2: the 1,349 tickets and 8,880 discussion posts of the 2026-09-05 run reconcile against the tracker-reported counts (774 bugs, 567 feature requests, 8 support requests) in `sources/manifests/2026-09-06-tei-legacy-sourceforge-r4.yaml`; the raw responses of the earlier runs are not in this checkout; release-file and legacy version-control interfaces remain unreconciled |
| Literature corpus | partial | a bounded first reading records four candidates; W3C REC2017, Piez2014 and Renear/Wickett2010 have citation-only admissions; the Renear/Mylonas/Durand author-version full text returned HTTP 403; Zotero/JTEI and full seed census remain open |
| Official P6 process | partial | public `TEIC/timeForP6` history acquired; relevant Council records inventoried; reported `TEIC/p6-sandbox` remains non-public or absent |
| Independent P6 design knowledge | bounded Abstract Text Model 0.1 implemented, human acceptance pending | Ten record kinds with formal constraints and five reference operations. JSON, XML and YAML bindings preserve the same model instance. Two real diary fragments have bounded mappings. Full TEI domain coverage, RDF and whole-document P5 conversion remain open. |
| Grounded knowledge | four bounded chapters; entity runs reviewed | Twenty-three document sources and seven citation-only sources have distillates. Seventy-seven assertions carry passing recorded machine reviews; seventy-one are `validated` and six remain `contested`. Chapter 08 cites sixty-six assertions and records eleven posits. The four output chapters are `grounded`. The full Guidelines intake adds source availability only; comprehensive source interpretation and human verification remain open. |
| Text identity pilot acceptance | awaiting owner review | nine support pairs passed independent fresh-context review on 2026-09-05 after source-context correction; same-model-family limitation remains; human decisions use the five items in `knowledge/experiments.md` |
| Text identity pilot technical gate | passed on 2026-09-05 | 238 tests passed after first-wave integration; 38 synthetic cases reproduced; full-vault and chapter validation had no errors or warnings; source admission, control-plane integrity and current review hashes passed; generated HTML reproduced byte-for-byte |
| Entity extension 0.2 | drafted and implemented, human acceptance pending | section 14 of the text model defines entity, name, denotation, statement and alignment records on the claim pattern; the validator, two reference operations and a deterministic runner pass all fifty-eight independently authored cases and thirty-three canonical checks; four readings the text left open were settled and written back; a one-way RDF export in `tools/models/rdf_binding.py` preserves every record and reference edge under the identifier policy and is documented in `knowledge/text-model-bindings.md` § RDF export; five owner-review items stand in section 14.6 |
| Abstract Text Model 0.1 technical gate | passed on 2026-09-05 | all five reference operations implemented; 68 independently authored cases over 60 models, 38 canonical checks, and two standalone examples pass; deterministic report reproduces; 322 full-suite tests pass; full-vault and chapter 12 validation have no errors or warnings; current source-support audits, four quotation checks, and source control-plane checks pass |
| Abstract Text Model 0.1 review | machine reviews complete; human acceptance open | separate GPT-6 agents authored the implementation and cases; independent ontology and code reviews found no remaining material contract contradiction; positive-only membership, adjacent segments and diagnostic distinctions were clarified; finite synthetic checks do not establish domain adequacy, usability, or P5 migration; five owner-review items are in the model definition |
| Project text and argument review | integrated on 2026-09-05 | three GPT-6 review packages covered the model dossier, pilot argument, and research programme; final readback found no material contradictions in the reviewed model and method texts; these editorial reviews do not establish source support, ontological adequacy, or human acceptance |
| P5 specification atlas | bounded declaration navigation implemented | `corpus/projections/p5-specs-4.12.0.json` inventories 846 specification files, 546 local attributes and 131 local constraints; 57 named-datatype references remain outside declaration lookup; inheritance, Guidelines interpretation and effective ODD compilation remain open |
| First research wave | bounded integration and technical checks complete | four citation-only sources have checked quotations and validated distillates; four validated assertions feed `40_output/06-annotation-and-overlap.md`; eight source-support pairs passed fresh-context review after narrowing one heading; atlas reproduction, quotation checks, chapter and full-vault validation, control-plane checks and 238 tests passed; human verification remains open |
| Proposal for TEI P6 | continuous technical argument integrated | `40_output/12-p6-design.md` links nine grounded premises to thirteen explicit posits and seven comparative examples. Architecture ranking and adoption evidence remain open. |
| Editorial comparison | bounded execution complete | three fragments of one pinned Humboldt diary; two development mappings preserve the declared observations; the frozen candidate refuses the page/foliation holdout and the baseline projection also misses its required prose result; 18 independent synthetic provenance-profile cases pass; CC BY-SA 4.0 attribution and source hashes reconcile; full RNG/ODD conformance and media alignment remain untested |
| Research frontend | implemented and locally checked | The canonical proposal is `docs/index.html`. Model, Materials, Knowledge and About use the same layout and the same local and published routes. No decorative horizontal rules. The model reference derives its ten classes and seventeen reference fields from the existing contract. Published revisions are identified by the Pages deployment log. |
| Integrated release gate | passed locally on 2026-09-07 | 1,377 tests pass; ruff has no findings; full-vault validation has no errors or warnings; the source control plane reconciles. The Guidelines check reproduces 888 immutable source admissions and both coverage projections, including a tested clean checkout without ignored data. The 20 previously admitted baseline representations are byte-identical to HEAD. All five public pages reproduce from their recorded build dates. Desktop browser checks covered the Guidelines contents table and navigation to an expanded XML source passage. Systematic scholarly interpretation, human verification and publication of this working-tree change remain open. |
| Knowledge navigation | implemented; complete Guidelines reference admitted | The actual vault contains 891 source representations, thirty distillates, seventy-seven assertions and four grounded chapters after the 2026-09-07 intake. The generated coverage separates imported sources from existing distillates. Passage links and backreferences follow the immediate-layer chain. Citation-only admissions end at their checked quotation and citation. |
| Materials navigation | implemented | Seventeen primary source families and a separate literature view describe locked holdings and gaps. The Guidelines coverage section maps all 40 published contents entries to the admitted sources and distinguishes import from actual distillate presence. Raw-object acquisition and scholarly completeness retain their separate boundaries. |

## Milestones

The milestones and their exit conditions are defined in [[knowledge/plan]].

| Milestone | Status | Position |
|---|---|---|
| 1. Tools and gates repaired | complete | commit `1cfdb2e` on 2026-09-06 |
| 2. Knowledge base restructured | complete | commit `021b633` on 2026-09-06; every knowledge document lives in `knowledge/` with one function |
| 3. Vault structures | complete | commit `82bce81` on 2026-09-06; topic maps and glossary example lists are generated regions, phenomena are glossary entries, `phenomena` and `related` are validated |
| 4. Foundation closed | in progress | the exhaustive GitHub REST run, the SourceForge reconciliation, the local P5 mirror, the Penn State TEI-L months and the Wayback coverage measurement are done (commits `2a481dc`, `0ac8964`); the GraphQL relations stage ran (commit `810c516`); the Wayback fetch of the Brown archive runs, and the archive and website reconciliation, the export request to the Consortium and the sampling protocol remain open |
| 5. Claim pattern and IRI policy | complete | commit `0419968` on 2026-09-06; section 13 of the text model fixes the claim record, the IRI grammar and the alignment field |
| 6. Entity run and topic cycles | in progress | the first selection-driven vertical cycle ran on the topic Metadata and Entities (commit `0ac8964`): nine sources, nine validated distillates, thirty-five reviewed assertions, chapter 08 grounded; the second run of the topic admitted twelve sources selected by the recorded procedure (commit `02e2df7`), all twelve distillates are validated after three review rounds, thirty-one assertions authored by Fable passed the Opus review in one round, and chapter 08 was rewritten on the enlarged base, two posits became premises and four were narrowed; the next topics follow the order of the posits of chapter 12 |
| 7. Model extended phenomenon by phenomenon | in progress | the entity extension of section 14 is drafted, implemented in `tools/models/entities.py` and checked against fifty-eight independently authored cases on 2026-09-06; the coverage matrix names what stays uncovered; real cases from distinct editions, the RDF binding and the five acceptance items remain open |
| 8. Proposal from assertions | in progress | chapter 12 links nine validated premises to thirteen posits; counter-reader review, option ranking, migration prototype and dated official-P6 comparison remain open |
| 9. Publication | planned | no human verification sample recorded |

## Source inventory

The inventory is generated by `python tools/inventory.py . --write` and is never
edited by hand. Processing follows `new` → `ingested` → `distilled`. Each run
replaces the region between the markers with the actual file state.

<!-- inventory:begin -->
| Source | Type | Channel | Markdown representation | Distillate | Status |
|---|---|---|---|---|---|
| edition humboldt digital: England travel diary H0017682 | document | collection | [[10_markdown/documents/humboldt-h0017682-7d174637]] | [[20_distillates/documents/humboldt-h0017682-7d174637]] | distilled |
| TEI P5 4.12.0 A Gentle Introduction to XML | document | collection | [[10_markdown/documents/tei-p5-guidelines-sg-gentleintroduction-4.12.0]] | — | ingested |
| TEI P5 4.12.0 ab | document | collection | [[10_markdown/documents/tei-p5-ab-4.12.0]] | — | ingested |
| TEI P5 4.12.0 abbr | document | collection | [[10_markdown/documents/tei-p5-abbr-4.12.0]] | — | ingested |
| TEI P5 4.12.0 About These Guidelines | document | collection | [[10_markdown/documents/tei-p5-guidelines-ab-about-4.12.0]] | — | ingested |
| TEI P5 4.12.0 abstract | document | collection | [[10_markdown/documents/tei-p5-abstract-4.12.0]] | — | ingested |
| TEI P5 4.12.0 accMat | document | collection | [[10_markdown/documents/tei-p5-accmat-4.12.0]] | — | ingested |
| TEI P5 4.12.0 acquisition | document | collection | [[10_markdown/documents/tei-p5-acquisition-4.12.0]] | — | ingested |
| TEI P5 4.12.0 activity | document | collection | [[10_markdown/documents/tei-p5-activity-4.12.0]] | — | ingested |
| TEI P5 4.12.0 actor | document | collection | [[10_markdown/documents/tei-p5-actor-4.12.0]] | — | ingested |
| TEI P5 4.12.0 add | document | collection | [[10_markdown/documents/tei-p5-add-4.12.0]] | — | ingested |
| TEI P5 4.12.0 additional | document | collection | [[10_markdown/documents/tei-p5-additional-4.12.0]] | — | ingested |
| TEI P5 4.12.0 additions | document | collection | [[10_markdown/documents/tei-p5-additions-4.12.0]] | — | ingested |
| TEI P5 4.12.0 addName | document | collection | [[10_markdown/documents/tei-p5-addname-4.12.0]] | — | ingested |
| TEI P5 4.12.0 address | document | collection | [[10_markdown/documents/tei-p5-address-4.12.0]] | — | ingested |
| TEI P5 4.12.0 addrLine | document | collection | [[10_markdown/documents/tei-p5-addrline-4.12.0]] | — | ingested |
| TEI P5 4.12.0 addSpan | document | collection | [[10_markdown/documents/tei-p5-addspan-4.12.0]] | — | ingested |
| TEI P5 4.12.0 adminInfo | document | collection | [[10_markdown/documents/tei-p5-admininfo-4.12.0]] | — | ingested |
| TEI P5 4.12.0 affiliation | document | collection | [[10_markdown/documents/tei-p5-affiliation-4.12.0]] | — | ingested |
| TEI P5 4.12.0 age | document | collection | [[10_markdown/documents/tei-p5-age-4.12.0]] | — | ingested |
| TEI P5 4.12.0 alt | document | collection | [[10_markdown/documents/tei-p5-alt-4.12.0]] | — | ingested |
| TEI P5 4.12.0 alternate | document | collection | [[10_markdown/documents/tei-p5-alternate-4.12.0]] | — | ingested |
| TEI P5 4.12.0 altGrp | document | collection | [[10_markdown/documents/tei-p5-altgrp-4.12.0]] | — | ingested |
| TEI P5 4.12.0 altIdent | document | collection | [[10_markdown/documents/tei-p5-altident-4.12.0]] | — | ingested |
| TEI P5 4.12.0 altIdentifier | document | collection | [[10_markdown/documents/tei-p5-altidentifier-4.12.0]] | — | ingested |
| TEI P5 4.12.0 am | document | collection | [[10_markdown/documents/tei-p5-am-4.12.0]] | — | ingested |
| TEI P5 4.12.0 analytic | document | collection | [[10_markdown/documents/tei-p5-analytic-4.12.0]] | — | ingested |
| TEI P5 4.12.0 anchor specification | document | collection | [[10_markdown/documents/tei-p5-anchor-4.12.0]] | [[20_distillates/documents/tei-p5-anchor-4.12.0]] | distilled |
| TEI P5 4.12.0 annotation specification | document | collection | [[10_markdown/documents/tei-p5-annotation-4.12.0]] | [[20_distillates/documents/tei-p5-annotation-4.12.0]] | distilled |
| TEI P5 4.12.0 annotationBlock | document | collection | [[10_markdown/documents/tei-p5-annotationblock-4.12.0]] | — | ingested |
| TEI P5 4.12.0 anyElement | document | collection | [[10_markdown/documents/tei-p5-anyelement-4.12.0]] | — | ingested |
| TEI P5 4.12.0 app | document | collection | [[10_markdown/documents/tei-p5-app-4.12.0]] | — | ingested |
| TEI P5 4.12.0 appInfo | document | collection | [[10_markdown/documents/tei-p5-appinfo-4.12.0]] | — | ingested |
| TEI P5 4.12.0 application | document | collection | [[10_markdown/documents/tei-p5-application-4.12.0]] | — | ingested |
| TEI P5 4.12.0 arc | document | collection | [[10_markdown/documents/tei-p5-arc-4.12.0]] | — | ingested |
| TEI P5 4.12.0 argument | document | collection | [[10_markdown/documents/tei-p5-argument-4.12.0]] | — | ingested |
| TEI P5 4.12.0 att | document | collection | [[10_markdown/documents/tei-p5-att-4.12.0]] | — | ingested |
| TEI P5 4.12.0 att.anchoring | document | collection | [[10_markdown/documents/tei-p5-att.anchoring-4.12.0]] | — | ingested |
| TEI P5 4.12.0 att.ascribed | document | collection | [[10_markdown/documents/tei-p5-att.ascribed-4.12.0]] | — | ingested |
| TEI P5 4.12.0 att.ascribed.directed | document | collection | [[10_markdown/documents/tei-p5-att.ascribed.directed-4.12.0]] | — | ingested |
| TEI P5 4.12.0 att.breaking | document | collection | [[10_markdown/documents/tei-p5-att.breaking-4.12.0]] | — | ingested |
| TEI P5 4.12.0 att.calendarSystem | document | collection | [[10_markdown/documents/tei-p5-att.calendarsystem-4.12.0]] | — | ingested |
| TEI P5 4.12.0 att.canonical specification | document | collection | [[10_markdown/documents/tei-p5-att.canonical-4.12.0]] | [[20_distillates/documents/tei-p5-att.canonical-4.12.0]] | distilled |
| TEI P5 4.12.0 att.citeStructurePart | document | collection | [[10_markdown/documents/tei-p5-att.citestructurepart-4.12.0]] | — | ingested |
| TEI P5 4.12.0 att.citing | document | collection | [[10_markdown/documents/tei-p5-att.citing-4.12.0]] | — | ingested |
| TEI P5 4.12.0 att.cmc | document | collection | [[10_markdown/documents/tei-p5-att.cmc-4.12.0]] | — | ingested |
| TEI P5 4.12.0 att.combinable | document | collection | [[10_markdown/documents/tei-p5-att.combinable-4.12.0]] | — | ingested |
| TEI P5 4.12.0 att.coordinated | document | collection | [[10_markdown/documents/tei-p5-att.coordinated-4.12.0]] | — | ingested |
| TEI P5 4.12.0 att.cReferencing | document | collection | [[10_markdown/documents/tei-p5-att.creferencing-4.12.0]] | — | ingested |
| TEI P5 4.12.0 att.damaged | document | collection | [[10_markdown/documents/tei-p5-att.damaged-4.12.0]] | — | ingested |
| TEI P5 4.12.0 att.datable specification | document | collection | [[10_markdown/documents/tei-p5-att.datable-4.12.0]] | [[20_distillates/documents/tei-p5-att.datable-4.12.0]] | distilled |
| TEI P5 4.12.0 att.datable.custom | document | collection | [[10_markdown/documents/tei-p5-att.datable.custom-4.12.0]] | — | ingested |
| TEI P5 4.12.0 att.datable.iso | document | collection | [[10_markdown/documents/tei-p5-att.datable.iso-4.12.0]] | — | ingested |
| TEI P5 4.12.0 att.datable.w3c | document | collection | [[10_markdown/documents/tei-p5-att.datable.w3c-4.12.0]] | — | ingested |
| TEI P5 4.12.0 att.datcat | document | collection | [[10_markdown/documents/tei-p5-att.datcat-4.12.0]] | — | ingested |
| TEI P5 4.12.0 att.declarable | document | collection | [[10_markdown/documents/tei-p5-att.declarable-4.12.0]] | — | ingested |
| TEI P5 4.12.0 att.declaring | document | collection | [[10_markdown/documents/tei-p5-att.declaring-4.12.0]] | — | ingested |
| TEI P5 4.12.0 att.deprecated | document | collection | [[10_markdown/documents/tei-p5-att.deprecated-4.12.0]] | — | ingested |
| TEI P5 4.12.0 att.dimensions | document | collection | [[10_markdown/documents/tei-p5-att.dimensions-4.12.0]] | — | ingested |
| TEI P5 4.12.0 att.divLike | document | collection | [[10_markdown/documents/tei-p5-att.divlike-4.12.0]] | — | ingested |
| TEI P5 4.12.0 att.docStatus | document | collection | [[10_markdown/documents/tei-p5-att.docstatus-4.12.0]] | — | ingested |
| TEI P5 4.12.0 att.duration | document | collection | [[10_markdown/documents/tei-p5-att.duration-4.12.0]] | — | ingested |
| TEI P5 4.12.0 att.duration.iso | document | collection | [[10_markdown/documents/tei-p5-att.duration.iso-4.12.0]] | — | ingested |
| TEI P5 4.12.0 att.duration.w3c | document | collection | [[10_markdown/documents/tei-p5-att.duration.w3c-4.12.0]] | — | ingested |
| TEI P5 4.12.0 att.edition | document | collection | [[10_markdown/documents/tei-p5-att.edition-4.12.0]] | — | ingested |
| TEI P5 4.12.0 att.editLike specification | document | collection | [[10_markdown/documents/tei-p5-att.editlike-4.12.0]] | [[20_distillates/documents/tei-p5-att.editlike-4.12.0]] | distilled |
| TEI P5 4.12.0 att.enjamb | document | collection | [[10_markdown/documents/tei-p5-att.enjamb-4.12.0]] | — | ingested |
| TEI P5 4.12.0 att.entryLike | document | collection | [[10_markdown/documents/tei-p5-att.entrylike-4.12.0]] | — | ingested |
| TEI P5 4.12.0 att.formula | document | collection | [[10_markdown/documents/tei-p5-att.formula-4.12.0]] | — | ingested |
| TEI P5 4.12.0 att.fragmentable | document | collection | [[10_markdown/documents/tei-p5-att.fragmentable-4.12.0]] | — | ingested |
| TEI P5 4.12.0 att.gaijiProp | document | collection | [[10_markdown/documents/tei-p5-att.gaijiprop-4.12.0]] | — | ingested |
| TEI P5 4.12.0 att.global | document | collection | [[10_markdown/documents/tei-p5-att.global-4.12.0]] | — | ingested |
| TEI P5 4.12.0 att.global.analytic | document | collection | [[10_markdown/documents/tei-p5-att.global.analytic-4.12.0]] | — | ingested |
| TEI P5 4.12.0 att.global.change | document | collection | [[10_markdown/documents/tei-p5-att.global.change-4.12.0]] | — | ingested |
| TEI P5 4.12.0 att.global.facs | document | collection | [[10_markdown/documents/tei-p5-att.global.facs-4.12.0]] | — | ingested |
| TEI P5 4.12.0 att.global.linking | document | collection | [[10_markdown/documents/tei-p5-att.global.linking-4.12.0]] | — | ingested |
| TEI P5 4.12.0 att.global.rendition | document | collection | [[10_markdown/documents/tei-p5-att.global.rendition-4.12.0]] | — | ingested |
| TEI P5 4.12.0 att.global.responsibility specification | document | collection | [[10_markdown/documents/tei-p5-att.global.responsibility-4.12.0]] | [[20_distillates/documents/tei-p5-att.global.responsibility-4.12.0]] | distilled |
| TEI P5 4.12.0 att.global.source specification | document | collection | [[10_markdown/documents/tei-p5-att.global.source-4.12.0]] | [[20_distillates/documents/tei-p5-att.global.source-4.12.0]] | distilled |
| TEI P5 4.12.0 att.handFeatures | document | collection | [[10_markdown/documents/tei-p5-att.handfeatures-4.12.0]] | — | ingested |
| TEI P5 4.12.0 att.identified | document | collection | [[10_markdown/documents/tei-p5-att.identified-4.12.0]] | — | ingested |
| TEI P5 4.12.0 att.indentation | document | collection | [[10_markdown/documents/tei-p5-att.indentation-4.12.0]] | — | ingested |
| TEI P5 4.12.0 att.internetMedia | document | collection | [[10_markdown/documents/tei-p5-att.internetmedia-4.12.0]] | — | ingested |
| TEI P5 4.12.0 att.interpLike | document | collection | [[10_markdown/documents/tei-p5-att.interplike-4.12.0]] | — | ingested |
| TEI P5 4.12.0 att.lexicographic | document | collection | [[10_markdown/documents/tei-p5-att.lexicographic-4.12.0]] | — | ingested |
| TEI P5 4.12.0 att.lexicographic.normalized | document | collection | [[10_markdown/documents/tei-p5-att.lexicographic.normalized-4.12.0]] | — | ingested |
| TEI P5 4.12.0 att.linguistic | document | collection | [[10_markdown/documents/tei-p5-att.linguistic-4.12.0]] | — | ingested |
| TEI P5 4.12.0 att.locatable | document | collection | [[10_markdown/documents/tei-p5-att.locatable-4.12.0]] | — | ingested |
| TEI P5 4.12.0 att.measurement | document | collection | [[10_markdown/documents/tei-p5-att.measurement-4.12.0]] | — | ingested |
| TEI P5 4.12.0 att.media | document | collection | [[10_markdown/documents/tei-p5-att.media-4.12.0]] | — | ingested |
| TEI P5 4.12.0 att.metrical | document | collection | [[10_markdown/documents/tei-p5-att.metrical-4.12.0]] | — | ingested |
| TEI P5 4.12.0 att.milestoneUnit | document | collection | [[10_markdown/documents/tei-p5-att.milestoneunit-4.12.0]] | — | ingested |
| TEI P5 4.12.0 att.msClass | document | collection | [[10_markdown/documents/tei-p5-att.msclass-4.12.0]] | — | ingested |
| TEI P5 4.12.0 att.msExcerpt | document | collection | [[10_markdown/documents/tei-p5-att.msexcerpt-4.12.0]] | — | ingested |
| TEI P5 4.12.0 att.namespaceable | document | collection | [[10_markdown/documents/tei-p5-att.namespaceable-4.12.0]] | — | ingested |
| TEI P5 4.12.0 att.naming specification | document | collection | [[10_markdown/documents/tei-p5-att.naming-4.12.0]] | [[20_distillates/documents/tei-p5-att.naming-4.12.0]] | distilled |
| TEI P5 4.12.0 att.notated | document | collection | [[10_markdown/documents/tei-p5-att.notated-4.12.0]] | — | ingested |
| TEI P5 4.12.0 att.partials | document | collection | [[10_markdown/documents/tei-p5-att.partials-4.12.0]] | — | ingested |
| TEI P5 4.12.0 att.patternReplacement | document | collection | [[10_markdown/documents/tei-p5-att.patternreplacement-4.12.0]] | — | ingested |
| TEI P5 4.12.0 att.performed | document | collection | [[10_markdown/documents/tei-p5-att.performed-4.12.0]] | — | ingested |
| TEI P5 4.12.0 att.personal specification | document | collection | [[10_markdown/documents/tei-p5-att.personal-4.12.0]] | [[20_distillates/documents/tei-p5-att.personal-4.12.0]] | distilled |
| TEI P5 4.12.0 att.placement | document | collection | [[10_markdown/documents/tei-p5-att.placement-4.12.0]] | — | ingested |
| TEI P5 4.12.0 att.pointing | document | collection | [[10_markdown/documents/tei-p5-att.pointing-4.12.0]] | — | ingested |
| TEI P5 4.12.0 att.pointing.group | document | collection | [[10_markdown/documents/tei-p5-att.pointing.group-4.12.0]] | — | ingested |
| TEI P5 4.12.0 att.predicate | document | collection | [[10_markdown/documents/tei-p5-att.predicate-4.12.0]] | — | ingested |
| TEI P5 4.12.0 att.ranging | document | collection | [[10_markdown/documents/tei-p5-att.ranging-4.12.0]] | — | ingested |
| TEI P5 4.12.0 att.rdgPart | document | collection | [[10_markdown/documents/tei-p5-att.rdgpart-4.12.0]] | — | ingested |
| TEI P5 4.12.0 att.repeatable | document | collection | [[10_markdown/documents/tei-p5-att.repeatable-4.12.0]] | — | ingested |
| TEI P5 4.12.0 att.resourced | document | collection | [[10_markdown/documents/tei-p5-att.resourced-4.12.0]] | — | ingested |
| TEI P5 4.12.0 att.scope | document | collection | [[10_markdown/documents/tei-p5-att.scope-4.12.0]] | — | ingested |
| TEI P5 4.12.0 att.scoping | document | collection | [[10_markdown/documents/tei-p5-att.scoping-4.12.0]] | — | ingested |
| TEI P5 4.12.0 att.segLike | document | collection | [[10_markdown/documents/tei-p5-att.seglike-4.12.0]] | — | ingested |
| TEI P5 4.12.0 att.sortable | document | collection | [[10_markdown/documents/tei-p5-att.sortable-4.12.0]] | — | ingested |
| TEI P5 4.12.0 att.spanning | document | collection | [[10_markdown/documents/tei-p5-att.spanning-4.12.0]] | — | ingested |
| TEI P5 4.12.0 att.styleDef | document | collection | [[10_markdown/documents/tei-p5-att.styledef-4.12.0]] | — | ingested |
| TEI P5 4.12.0 att.tableDecoration | document | collection | [[10_markdown/documents/tei-p5-att.tabledecoration-4.12.0]] | — | ingested |
| TEI P5 4.12.0 att.textCritical | document | collection | [[10_markdown/documents/tei-p5-att.textcritical-4.12.0]] | — | ingested |
| TEI P5 4.12.0 att.timed | document | collection | [[10_markdown/documents/tei-p5-att.timed-4.12.0]] | — | ingested |
| TEI P5 4.12.0 att.transcriptional | document | collection | [[10_markdown/documents/tei-p5-att.transcriptional-4.12.0]] | — | ingested |
| TEI P5 4.12.0 att.translatable | document | collection | [[10_markdown/documents/tei-p5-att.translatable-4.12.0]] | — | ingested |
| TEI P5 4.12.0 att.typed | document | collection | [[10_markdown/documents/tei-p5-att.typed-4.12.0]] | — | ingested |
| TEI P5 4.12.0 att.witnessed | document | collection | [[10_markdown/documents/tei-p5-att.witnessed-4.12.0]] | — | ingested |
| TEI P5 4.12.0 att.written | document | collection | [[10_markdown/documents/tei-p5-att.written-4.12.0]] | — | ingested |
| TEI P5 4.12.0 attDef | document | collection | [[10_markdown/documents/tei-p5-attdef-4.12.0]] | — | ingested |
| TEI P5 4.12.0 attList | document | collection | [[10_markdown/documents/tei-p5-attlist-4.12.0]] | — | ingested |
| TEI P5 4.12.0 attRef | document | collection | [[10_markdown/documents/tei-p5-attref-4.12.0]] | — | ingested |
| TEI P5 4.12.0 Attribute Classes | document | collection | [[10_markdown/documents/tei-p5-guidelines-ref-classes-atts-4.12.0]] | — | ingested |
| TEI P5 4.12.0 Attributes | document | collection | [[10_markdown/documents/tei-p5-guidelines-ref-attributes-4.12.0]] | — | ingested |
| TEI P5 4.12.0 author | document | collection | [[10_markdown/documents/tei-p5-author-4.12.0]] | — | ingested |
| TEI P5 4.12.0 authority | document | collection | [[10_markdown/documents/tei-p5-authority-4.12.0]] | — | ingested |
| TEI P5 4.12.0 availability | document | collection | [[10_markdown/documents/tei-p5-availability-4.12.0]] | — | ingested |
| TEI P5 4.12.0 back | document | collection | [[10_markdown/documents/tei-p5-back-4.12.0]] | — | ingested |
| TEI P5 4.12.0 bibl | document | collection | [[10_markdown/documents/tei-p5-bibl-4.12.0]] | — | ingested |
| TEI P5 4.12.0 biblFull | document | collection | [[10_markdown/documents/tei-p5-biblfull-4.12.0]] | — | ingested |
| TEI P5 4.12.0 Bibliography | document | collection | [[10_markdown/documents/tei-p5-guidelines-bib-bibliography-4.12.0]] | — | ingested |
| TEI P5 4.12.0 biblScope | document | collection | [[10_markdown/documents/tei-p5-biblscope-4.12.0]] | — | ingested |
| TEI P5 4.12.0 biblStruct | document | collection | [[10_markdown/documents/tei-p5-biblstruct-4.12.0]] | — | ingested |
| TEI P5 4.12.0 bicond | document | collection | [[10_markdown/documents/tei-p5-bicond-4.12.0]] | — | ingested |
| TEI P5 4.12.0 binary | document | collection | [[10_markdown/documents/tei-p5-binary-4.12.0]] | — | ingested |
| TEI P5 4.12.0 binaryObject | document | collection | [[10_markdown/documents/tei-p5-binaryobject-4.12.0]] | — | ingested |
| TEI P5 4.12.0 binding | document | collection | [[10_markdown/documents/tei-p5-binding-4.12.0]] | — | ingested |
| TEI P5 4.12.0 bindingDesc | document | collection | [[10_markdown/documents/tei-p5-bindingdesc-4.12.0]] | — | ingested |
| TEI P5 4.12.0 birth | document | collection | [[10_markdown/documents/tei-p5-birth-4.12.0]] | — | ingested |
| TEI P5 4.12.0 bloc | document | collection | [[10_markdown/documents/tei-p5-bloc-4.12.0]] | — | ingested |
| TEI P5 4.12.0 body | document | collection | [[10_markdown/documents/tei-p5-body-4.12.0]] | — | ingested |
| TEI P5 4.12.0 broadcast | document | collection | [[10_markdown/documents/tei-p5-broadcast-4.12.0]] | — | ingested |
| TEI P5 4.12.0 byline | document | collection | [[10_markdown/documents/tei-p5-byline-4.12.0]] | — | ingested |
| TEI P5 4.12.0 c | document | collection | [[10_markdown/documents/tei-p5-c-4.12.0]] | — | ingested |
| TEI P5 4.12.0 caesura | document | collection | [[10_markdown/documents/tei-p5-caesura-4.12.0]] | — | ingested |
| TEI P5 4.12.0 calendar | document | collection | [[10_markdown/documents/tei-p5-calendar-4.12.0]] | — | ingested |
| TEI P5 4.12.0 calendarDesc | document | collection | [[10_markdown/documents/tei-p5-calendardesc-4.12.0]] | — | ingested |
| TEI P5 4.12.0 camera | document | collection | [[10_markdown/documents/tei-p5-camera-4.12.0]] | — | ingested |
| TEI P5 4.12.0 caption | document | collection | [[10_markdown/documents/tei-p5-caption-4.12.0]] | — | ingested |
| TEI P5 4.12.0 case | document | collection | [[10_markdown/documents/tei-p5-case-4.12.0]] | — | ingested |
| TEI P5 4.12.0 castGroup | document | collection | [[10_markdown/documents/tei-p5-castgroup-4.12.0]] | — | ingested |
| TEI P5 4.12.0 castItem | document | collection | [[10_markdown/documents/tei-p5-castitem-4.12.0]] | — | ingested |
| TEI P5 4.12.0 castList | document | collection | [[10_markdown/documents/tei-p5-castlist-4.12.0]] | — | ingested |
| TEI P5 4.12.0 catchwords | document | collection | [[10_markdown/documents/tei-p5-catchwords-4.12.0]] | — | ingested |
| TEI P5 4.12.0 catDesc | document | collection | [[10_markdown/documents/tei-p5-catdesc-4.12.0]] | — | ingested |
| TEI P5 4.12.0 category | document | collection | [[10_markdown/documents/tei-p5-category-4.12.0]] | — | ingested |
| TEI P5 4.12.0 catRef | document | collection | [[10_markdown/documents/tei-p5-catref-4.12.0]] | — | ingested |
| TEI P5 4.12.0 cb | document | collection | [[10_markdown/documents/tei-p5-cb-4.12.0]] | — | ingested |
| TEI P5 4.12.0 cell | document | collection | [[10_markdown/documents/tei-p5-cell-4.12.0]] | — | ingested |
| TEI P5 4.12.0 certainty | document | collection | [[10_markdown/documents/tei-p5-certainty-4.12.0]] | — | ingested |
| TEI P5 4.12.0 Certainty, Precision, and Responsibility | document | collection | [[10_markdown/documents/tei-p5-guidelines-ce-certaintyresponsibility-4.12.0]] | — | ingested |
| TEI P5 4.12.0 change | document | collection | [[10_markdown/documents/tei-p5-change-4.12.0]] | — | ingested |
| TEI P5 4.12.0 channel | document | collection | [[10_markdown/documents/tei-p5-channel-4.12.0]] | — | ingested |
| TEI P5 4.12.0 char | document | collection | [[10_markdown/documents/tei-p5-char-4.12.0]] | — | ingested |
| TEI P5 4.12.0 Characters, Glyphs, and Writing Modes | document | collection | [[10_markdown/documents/tei-p5-guidelines-wd-nonstandardcharacters-4.12.0]] | — | ingested |
| TEI P5 4.12.0 charDecl | document | collection | [[10_markdown/documents/tei-p5-chardecl-4.12.0]] | — | ingested |
| TEI P5 4.12.0 choice | document | collection | [[10_markdown/documents/tei-p5-choice-4.12.0]] | — | ingested |
| TEI P5 4.12.0 cit | document | collection | [[10_markdown/documents/tei-p5-cit-4.12.0]] | — | ingested |
| TEI P5 4.12.0 citeData | document | collection | [[10_markdown/documents/tei-p5-citedata-4.12.0]] | — | ingested |
| TEI P5 4.12.0 citedRange | document | collection | [[10_markdown/documents/tei-p5-citedrange-4.12.0]] | — | ingested |
| TEI P5 4.12.0 citeStructure | document | collection | [[10_markdown/documents/tei-p5-citestructure-4.12.0]] | — | ingested |
| TEI P5 4.12.0 cl | document | collection | [[10_markdown/documents/tei-p5-cl-4.12.0]] | — | ingested |
| TEI P5 4.12.0 classCode | document | collection | [[10_markdown/documents/tei-p5-classcode-4.12.0]] | — | ingested |
| TEI P5 4.12.0 classDecl | document | collection | [[10_markdown/documents/tei-p5-classdecl-4.12.0]] | — | ingested |
| TEI P5 4.12.0 classes | document | collection | [[10_markdown/documents/tei-p5-classes-4.12.0]] | — | ingested |
| TEI P5 4.12.0 classRef | document | collection | [[10_markdown/documents/tei-p5-classref-4.12.0]] | — | ingested |
| TEI P5 4.12.0 classSpec | document | collection | [[10_markdown/documents/tei-p5-classspec-4.12.0]] | — | ingested |
| TEI P5 4.12.0 climate | document | collection | [[10_markdown/documents/tei-p5-climate-4.12.0]] | — | ingested |
| TEI P5 4.12.0 closer | document | collection | [[10_markdown/documents/tei-p5-closer-4.12.0]] | — | ingested |
| TEI P5 4.12.0 code | document | collection | [[10_markdown/documents/tei-p5-code-4.12.0]] | — | ingested |
| TEI P5 4.12.0 collation | document | collection | [[10_markdown/documents/tei-p5-collation-4.12.0]] | — | ingested |
| TEI P5 4.12.0 collection | document | collection | [[10_markdown/documents/tei-p5-collection-4.12.0]] | — | ingested |
| TEI P5 4.12.0 colloc | document | collection | [[10_markdown/documents/tei-p5-colloc-4.12.0]] | — | ingested |
| TEI P5 4.12.0 colophon | document | collection | [[10_markdown/documents/tei-p5-colophon-4.12.0]] | — | ingested |
| TEI P5 4.12.0 Colophon | document | collection | [[10_markdown/documents/tei-p5-guidelines-col-colophon-4.12.0]] | — | ingested |
| TEI P5 4.12.0 Computer-mediated Communication | document | collection | [[10_markdown/documents/tei-p5-guidelines-cmc-computermediatedcommunication-4.12.0]] | — | ingested |
| TEI P5 4.12.0 cond | document | collection | [[10_markdown/documents/tei-p5-cond-4.12.0]] | — | ingested |
| TEI P5 4.12.0 condition | document | collection | [[10_markdown/documents/tei-p5-condition-4.12.0]] | — | ingested |
| TEI P5 4.12.0 constitution | document | collection | [[10_markdown/documents/tei-p5-constitution-4.12.0]] | — | ingested |
| TEI P5 4.12.0 constraint | document | collection | [[10_markdown/documents/tei-p5-constraint-4.12.0]] | — | ingested |
| TEI P5 4.12.0 constraintDecl | document | collection | [[10_markdown/documents/tei-p5-constraintdecl-4.12.0]] | — | ingested |
| TEI P5 4.12.0 constraintSpec | document | collection | [[10_markdown/documents/tei-p5-constraintspec-4.12.0]] | — | ingested |
| TEI P5 4.12.0 content | document | collection | [[10_markdown/documents/tei-p5-content-4.12.0]] | — | ingested |
| TEI P5 4.12.0 conversion | document | collection | [[10_markdown/documents/tei-p5-conversion-4.12.0]] | — | ingested |
| TEI P5 4.12.0 corr | document | collection | [[10_markdown/documents/tei-p5-corr-4.12.0]] | — | ingested |
| TEI P5 4.12.0 correction | document | collection | [[10_markdown/documents/tei-p5-correction-4.12.0]] | — | ingested |
| TEI P5 4.12.0 correspAction | document | collection | [[10_markdown/documents/tei-p5-correspaction-4.12.0]] | — | ingested |
| TEI P5 4.12.0 correspContext | document | collection | [[10_markdown/documents/tei-p5-correspcontext-4.12.0]] | — | ingested |
| TEI P5 4.12.0 correspDesc | document | collection | [[10_markdown/documents/tei-p5-correspdesc-4.12.0]] | — | ingested |
| TEI P5 4.12.0 country | document | collection | [[10_markdown/documents/tei-p5-country-4.12.0]] | — | ingested |
| TEI P5 4.12.0 creation | document | collection | [[10_markdown/documents/tei-p5-creation-4.12.0]] | — | ingested |
| TEI P5 4.12.0 cRefPattern | document | collection | [[10_markdown/documents/tei-p5-crefpattern-4.12.0]] | — | ingested |
| TEI P5 4.12.0 Critical Apparatus | document | collection | [[10_markdown/documents/tei-p5-guidelines-tc-criticalapparatus-4.12.0]] | — | ingested |
| TEI P5 4.12.0 custEvent | document | collection | [[10_markdown/documents/tei-p5-custevent-4.12.0]] | — | ingested |
| TEI P5 4.12.0 custodialHist | document | collection | [[10_markdown/documents/tei-p5-custodialhist-4.12.0]] | — | ingested |
| TEI P5 4.12.0 damage | document | collection | [[10_markdown/documents/tei-p5-damage-4.12.0]] | — | ingested |
| TEI P5 4.12.0 damageSpan | document | collection | [[10_markdown/documents/tei-p5-damagespan-4.12.0]] | — | ingested |
| TEI P5 4.12.0 dataFacet | document | collection | [[10_markdown/documents/tei-p5-datafacet-4.12.0]] | — | ingested |
| TEI P5 4.12.0 dataRef | document | collection | [[10_markdown/documents/tei-p5-dataref-4.12.0]] | — | ingested |
| TEI P5 4.12.0 dataSpec | document | collection | [[10_markdown/documents/tei-p5-dataspec-4.12.0]] | — | ingested |
| TEI P5 4.12.0 datatype | document | collection | [[10_markdown/documents/tei-p5-datatype-4.12.0]] | — | ingested |
| TEI P5 4.12.0 Datatypes and Other Macros | document | collection | [[10_markdown/documents/tei-p5-guidelines-ref-macros-4.12.0]] | — | ingested |
| TEI P5 4.12.0 date | document | collection | [[10_markdown/documents/tei-p5-date-4.12.0]] | — | ingested |
| TEI P5 4.12.0 dateline | document | collection | [[10_markdown/documents/tei-p5-dateline-4.12.0]] | — | ingested |
| TEI P5 4.12.0 death | document | collection | [[10_markdown/documents/tei-p5-death-4.12.0]] | — | ingested |
| TEI P5 4.12.0 decoDesc | document | collection | [[10_markdown/documents/tei-p5-decodesc-4.12.0]] | — | ingested |
| TEI P5 4.12.0 decoNote | document | collection | [[10_markdown/documents/tei-p5-deconote-4.12.0]] | — | ingested |
| TEI P5 4.12.0 Dedication | document | collection | [[10_markdown/documents/tei-p5-guidelines-dedication-4.12.0]] | — | ingested |
| TEI P5 4.12.0 def | document | collection | [[10_markdown/documents/tei-p5-def-4.12.0]] | — | ingested |
| TEI P5 4.12.0 default | document | collection | [[10_markdown/documents/tei-p5-default-4.12.0]] | — | ingested |
| TEI P5 4.12.0 Default Text Structure | document | collection | [[10_markdown/documents/tei-p5-guidelines-ds-defaulttextstructure-4.12.0]] | — | ingested |
| TEI P5 4.12.0 defaultVal | document | collection | [[10_markdown/documents/tei-p5-defaultval-4.12.0]] | — | ingested |
| TEI P5 4.12.0 del | document | collection | [[10_markdown/documents/tei-p5-del-4.12.0]] | — | ingested |
| TEI P5 4.12.0 delSpan | document | collection | [[10_markdown/documents/tei-p5-delspan-4.12.0]] | — | ingested |
| TEI P5 4.12.0 Deprecations | document | collection | [[10_markdown/documents/tei-p5-guidelines-deprecations-4.12.0]] | — | ingested |
| TEI P5 4.12.0 depth | document | collection | [[10_markdown/documents/tei-p5-depth-4.12.0]] | — | ingested |
| TEI P5 4.12.0 derivation | document | collection | [[10_markdown/documents/tei-p5-derivation-4.12.0]] | — | ingested |
| TEI P5 4.12.0 desc | document | collection | [[10_markdown/documents/tei-p5-desc-4.12.0]] | — | ingested |
| TEI P5 4.12.0 Dictionaries | document | collection | [[10_markdown/documents/tei-p5-guidelines-di-printdictionaries-4.12.0]] | — | ingested |
| TEI P5 4.12.0 dictScrap | document | collection | [[10_markdown/documents/tei-p5-dictscrap-4.12.0]] | — | ingested |
| TEI P5 4.12.0 dim | document | collection | [[10_markdown/documents/tei-p5-dim-4.12.0]] | — | ingested |
| TEI P5 4.12.0 dimensions | document | collection | [[10_markdown/documents/tei-p5-dimensions-4.12.0]] | — | ingested |
| TEI P5 4.12.0 distinct | document | collection | [[10_markdown/documents/tei-p5-distinct-4.12.0]] | — | ingested |
| TEI P5 4.12.0 distributor | document | collection | [[10_markdown/documents/tei-p5-distributor-4.12.0]] | — | ingested |
| TEI P5 4.12.0 district | document | collection | [[10_markdown/documents/tei-p5-district-4.12.0]] | — | ingested |
| TEI P5 4.12.0 div | document | collection | [[10_markdown/documents/tei-p5-div-4.12.0]] | — | ingested |
| TEI P5 4.12.0 div1 | document | collection | [[10_markdown/documents/tei-p5-div1-4.12.0]] | — | ingested |
| TEI P5 4.12.0 div2 | document | collection | [[10_markdown/documents/tei-p5-div2-4.12.0]] | — | ingested |
| TEI P5 4.12.0 div3 | document | collection | [[10_markdown/documents/tei-p5-div3-4.12.0]] | — | ingested |
| TEI P5 4.12.0 div4 | document | collection | [[10_markdown/documents/tei-p5-div4-4.12.0]] | — | ingested |
| TEI P5 4.12.0 div5 | document | collection | [[10_markdown/documents/tei-p5-div5-4.12.0]] | — | ingested |
| TEI P5 4.12.0 div6 | document | collection | [[10_markdown/documents/tei-p5-div6-4.12.0]] | — | ingested |
| TEI P5 4.12.0 div7 | document | collection | [[10_markdown/documents/tei-p5-div7-4.12.0]] | — | ingested |
| TEI P5 4.12.0 divGen | document | collection | [[10_markdown/documents/tei-p5-divgen-4.12.0]] | — | ingested |
| TEI P5 4.12.0 docAuthor | document | collection | [[10_markdown/documents/tei-p5-docauthor-4.12.0]] | — | ingested |
| TEI P5 4.12.0 docDate | document | collection | [[10_markdown/documents/tei-p5-docdate-4.12.0]] | — | ingested |
| TEI P5 4.12.0 docEdition | document | collection | [[10_markdown/documents/tei-p5-docedition-4.12.0]] | — | ingested |
| TEI P5 4.12.0 docImprint | document | collection | [[10_markdown/documents/tei-p5-docimprint-4.12.0]] | — | ingested |
| TEI P5 4.12.0 docTitle | document | collection | [[10_markdown/documents/tei-p5-doctitle-4.12.0]] | — | ingested |
| TEI P5 4.12.0 Documentation Elements | document | collection | [[10_markdown/documents/tei-p5-guidelines-td-documentationelements-4.12.0]] | — | ingested |
| TEI P5 4.12.0 domain | document | collection | [[10_markdown/documents/tei-p5-domain-4.12.0]] | — | ingested |
| TEI P5 4.12.0 edition | document | collection | [[10_markdown/documents/tei-p5-edition-4.12.0]] | — | ingested |
| TEI P5 4.12.0 editionStmt | document | collection | [[10_markdown/documents/tei-p5-editionstmt-4.12.0]] | — | ingested |
| TEI P5 4.12.0 editor | document | collection | [[10_markdown/documents/tei-p5-editor-4.12.0]] | — | ingested |
| TEI P5 4.12.0 editorialDecl | document | collection | [[10_markdown/documents/tei-p5-editorialdecl-4.12.0]] | — | ingested |
| TEI P5 4.12.0 education | document | collection | [[10_markdown/documents/tei-p5-education-4.12.0]] | — | ingested |
| TEI P5 4.12.0 eg | document | collection | [[10_markdown/documents/tei-p5-eg-4.12.0]] | — | ingested |
| TEI P5 4.12.0 egXML | document | collection | [[10_markdown/documents/tei-p5-egxml-4.12.0]] | — | ingested |
| TEI P5 4.12.0 eLeaf | document | collection | [[10_markdown/documents/tei-p5-eleaf-4.12.0]] | — | ingested |
| TEI P5 4.12.0 elementRef | document | collection | [[10_markdown/documents/tei-p5-elementref-4.12.0]] | — | ingested |
| TEI P5 4.12.0 Elements | document | collection | [[10_markdown/documents/tei-p5-guidelines-ref-elements-4.12.0]] | — | ingested |
| TEI P5 4.12.0 Elements Available in All TEI Documents | document | collection | [[10_markdown/documents/tei-p5-guidelines-co-coreelements-4.12.0]] | — | ingested |
| TEI P5 4.12.0 elementSpec | document | collection | [[10_markdown/documents/tei-p5-elementspec-4.12.0]] | — | ingested |
| TEI P5 4.12.0 ellipsis | document | collection | [[10_markdown/documents/tei-p5-ellipsis-4.12.0]] | — | ingested |
| TEI P5 4.12.0 email | document | collection | [[10_markdown/documents/tei-p5-email-4.12.0]] | — | ingested |
| TEI P5 4.12.0 emph | document | collection | [[10_markdown/documents/tei-p5-emph-4.12.0]] | — | ingested |
| TEI P5 4.12.0 empty | document | collection | [[10_markdown/documents/tei-p5-empty-4.12.0]] | — | ingested |
| TEI P5 4.12.0 encodingDesc | document | collection | [[10_markdown/documents/tei-p5-encodingdesc-4.12.0]] | — | ingested |
| TEI P5 4.12.0 entry | document | collection | [[10_markdown/documents/tei-p5-entry-4.12.0]] | — | ingested |
| TEI P5 4.12.0 entryFree | document | collection | [[10_markdown/documents/tei-p5-entryfree-4.12.0]] | — | ingested |
| TEI P5 4.12.0 epigraph | document | collection | [[10_markdown/documents/tei-p5-epigraph-4.12.0]] | — | ingested |
| TEI P5 4.12.0 epilogue | document | collection | [[10_markdown/documents/tei-p5-epilogue-4.12.0]] | — | ingested |
| TEI P5 4.12.0 equipment | document | collection | [[10_markdown/documents/tei-p5-equipment-4.12.0]] | — | ingested |
| TEI P5 4.12.0 equiv | document | collection | [[10_markdown/documents/tei-p5-equiv-4.12.0]] | — | ingested |
| TEI P5 4.12.0 eTree | document | collection | [[10_markdown/documents/tei-p5-etree-4.12.0]] | — | ingested |
| TEI P5 4.12.0 etym | document | collection | [[10_markdown/documents/tei-p5-etym-4.12.0]] | — | ingested |
| TEI P5 4.12.0 event | document | collection | [[10_markdown/documents/tei-p5-event-4.12.0]] | — | ingested |
| TEI P5 4.12.0 eventName | document | collection | [[10_markdown/documents/tei-p5-eventname-4.12.0]] | — | ingested |
| TEI P5 4.12.0 ex | document | collection | [[10_markdown/documents/tei-p5-ex-4.12.0]] | — | ingested |
| TEI P5 4.12.0 exemplum | document | collection | [[10_markdown/documents/tei-p5-exemplum-4.12.0]] | — | ingested |
| TEI P5 4.12.0 expan | document | collection | [[10_markdown/documents/tei-p5-expan-4.12.0]] | — | ingested |
| TEI P5 4.12.0 explicit | document | collection | [[10_markdown/documents/tei-p5-explicit-4.12.0]] | — | ingested |
| TEI P5 4.12.0 extent | document | collection | [[10_markdown/documents/tei-p5-extent-4.12.0]] | — | ingested |
| TEI P5 4.12.0 f | document | collection | [[10_markdown/documents/tei-p5-f-4.12.0]] | — | ingested |
| TEI P5 4.12.0 facsimile | document | collection | [[10_markdown/documents/tei-p5-facsimile-4.12.0]] | — | ingested |
| TEI P5 4.12.0 factuality | document | collection | [[10_markdown/documents/tei-p5-factuality-4.12.0]] | — | ingested |
| TEI P5 4.12.0 faith | document | collection | [[10_markdown/documents/tei-p5-faith-4.12.0]] | — | ingested |
| TEI P5 4.12.0 fDecl | document | collection | [[10_markdown/documents/tei-p5-fdecl-4.12.0]] | — | ingested |
| TEI P5 4.12.0 fDescr | document | collection | [[10_markdown/documents/tei-p5-fdescr-4.12.0]] | — | ingested |
| TEI P5 4.12.0 Feature Structures | document | collection | [[10_markdown/documents/tei-p5-guidelines-fs-featurestructures-4.12.0]] | — | ingested |
| TEI P5 4.12.0 figDesc | document | collection | [[10_markdown/documents/tei-p5-figdesc-4.12.0]] | — | ingested |
| TEI P5 4.12.0 figure | document | collection | [[10_markdown/documents/tei-p5-figure-4.12.0]] | — | ingested |
| TEI P5 4.12.0 fileDesc | document | collection | [[10_markdown/documents/tei-p5-filedesc-4.12.0]] | — | ingested |
| TEI P5 4.12.0 filiation | document | collection | [[10_markdown/documents/tei-p5-filiation-4.12.0]] | — | ingested |
| TEI P5 4.12.0 finalRubric | document | collection | [[10_markdown/documents/tei-p5-finalrubric-4.12.0]] | — | ingested |
| TEI P5 4.12.0 fLib | document | collection | [[10_markdown/documents/tei-p5-flib-4.12.0]] | — | ingested |
| TEI P5 4.12.0 floatingText | document | collection | [[10_markdown/documents/tei-p5-floatingtext-4.12.0]] | — | ingested |
| TEI P5 4.12.0 floruit | document | collection | [[10_markdown/documents/tei-p5-floruit-4.12.0]] | — | ingested |
| TEI P5 4.12.0 foliation | document | collection | [[10_markdown/documents/tei-p5-foliation-4.12.0]] | — | ingested |
| TEI P5 4.12.0 foreign | document | collection | [[10_markdown/documents/tei-p5-foreign-4.12.0]] | — | ingested |
| TEI P5 4.12.0 forename | document | collection | [[10_markdown/documents/tei-p5-forename-4.12.0]] | — | ingested |
| TEI P5 4.12.0 forest | document | collection | [[10_markdown/documents/tei-p5-forest-4.12.0]] | — | ingested |
| TEI P5 4.12.0 form | document | collection | [[10_markdown/documents/tei-p5-form-4.12.0]] | — | ingested |
| TEI P5 4.12.0 formula | document | collection | [[10_markdown/documents/tei-p5-formula-4.12.0]] | — | ingested |
| TEI P5 4.12.0 front | document | collection | [[10_markdown/documents/tei-p5-front-4.12.0]] | — | ingested |
| TEI P5 4.12.0 fs | document | collection | [[10_markdown/documents/tei-p5-fs-4.12.0]] | — | ingested |
| TEI P5 4.12.0 fsConstraints | document | collection | [[10_markdown/documents/tei-p5-fsconstraints-4.12.0]] | — | ingested |
| TEI P5 4.12.0 fsdDecl | document | collection | [[10_markdown/documents/tei-p5-fsddecl-4.12.0]] | — | ingested |
| TEI P5 4.12.0 fsDecl | document | collection | [[10_markdown/documents/tei-p5-fsdecl-4.12.0]] | — | ingested |
| TEI P5 4.12.0 fsDescr | document | collection | [[10_markdown/documents/tei-p5-fsdescr-4.12.0]] | — | ingested |
| TEI P5 4.12.0 fsdLink | document | collection | [[10_markdown/documents/tei-p5-fsdlink-4.12.0]] | — | ingested |
| TEI P5 4.12.0 funder | document | collection | [[10_markdown/documents/tei-p5-funder-4.12.0]] | — | ingested |
| TEI P5 4.12.0 fvLib | document | collection | [[10_markdown/documents/tei-p5-fvlib-4.12.0]] | — | ingested |
| TEI P5 4.12.0 fw | document | collection | [[10_markdown/documents/tei-p5-fw-4.12.0]] | — | ingested |
| TEI P5 4.12.0 g | document | collection | [[10_markdown/documents/tei-p5-g-4.12.0]] | — | ingested |
| TEI P5 4.12.0 gap | document | collection | [[10_markdown/documents/tei-p5-gap-4.12.0]] | — | ingested |
| TEI P5 4.12.0 gb | document | collection | [[10_markdown/documents/tei-p5-gb-4.12.0]] | — | ingested |
| TEI P5 4.12.0 gen | document | collection | [[10_markdown/documents/tei-p5-gen-4.12.0]] | — | ingested |
| TEI P5 4.12.0 gender | document | collection | [[10_markdown/documents/tei-p5-gender-4.12.0]] | — | ingested |
| TEI P5 4.12.0 genName | document | collection | [[10_markdown/documents/tei-p5-genname-4.12.0]] | — | ingested |
| TEI P5 4.12.0 geo | document | collection | [[10_markdown/documents/tei-p5-geo-4.12.0]] | — | ingested |
| TEI P5 4.12.0 geoDecl | document | collection | [[10_markdown/documents/tei-p5-geodecl-4.12.0]] | — | ingested |
| TEI P5 4.12.0 geogFeat | document | collection | [[10_markdown/documents/tei-p5-geogfeat-4.12.0]] | — | ingested |
| TEI P5 4.12.0 geogName | document | collection | [[10_markdown/documents/tei-p5-geogname-4.12.0]] | — | ingested |
| TEI P5 4.12.0 gi | document | collection | [[10_markdown/documents/tei-p5-gi-4.12.0]] | — | ingested |
| TEI P5 4.12.0 gloss | document | collection | [[10_markdown/documents/tei-p5-gloss-4.12.0]] | — | ingested |
| TEI P5 4.12.0 glyph | document | collection | [[10_markdown/documents/tei-p5-glyph-4.12.0]] | — | ingested |
| TEI P5 4.12.0 gram | document | collection | [[10_markdown/documents/tei-p5-gram-4.12.0]] | — | ingested |
| TEI P5 4.12.0 gramGrp | document | collection | [[10_markdown/documents/tei-p5-gramgrp-4.12.0]] | — | ingested |
| TEI P5 4.12.0 graph | document | collection | [[10_markdown/documents/tei-p5-graph-4.12.0]] | — | ingested |
| TEI P5 4.12.0 graphic | document | collection | [[10_markdown/documents/tei-p5-graphic-4.12.0]] | — | ingested |
| TEI P5 4.12.0 Graphs, Networks, and Trees | document | collection | [[10_markdown/documents/tei-p5-guidelines-gd-graphsnetworkstrees-4.12.0]] | — | ingested |
| TEI P5 4.12.0 group | document | collection | [[10_markdown/documents/tei-p5-group-4.12.0]] | — | ingested |
| TEI P5 4.12.0 Guidelines chapter Names, Dates, People, and Places | document | collection | [[10_markdown/documents/tei-p5-guidelines-nd-4.12.0]] | [[20_distillates/documents/tei-p5-guidelines-nd-4.12.0]] | distilled |
| TEI P5 4.12.0 handDesc | document | collection | [[10_markdown/documents/tei-p5-handdesc-4.12.0]] | — | ingested |
| TEI P5 4.12.0 handNote | document | collection | [[10_markdown/documents/tei-p5-handnote-4.12.0]] | — | ingested |
| TEI P5 4.12.0 handNotes | document | collection | [[10_markdown/documents/tei-p5-handnotes-4.12.0]] | — | ingested |
| TEI P5 4.12.0 handShift | document | collection | [[10_markdown/documents/tei-p5-handshift-4.12.0]] | — | ingested |
| TEI P5 4.12.0 head | document | collection | [[10_markdown/documents/tei-p5-head-4.12.0]] | — | ingested |
| TEI P5 4.12.0 headItem | document | collection | [[10_markdown/documents/tei-p5-headitem-4.12.0]] | — | ingested |
| TEI P5 4.12.0 headLabel | document | collection | [[10_markdown/documents/tei-p5-headlabel-4.12.0]] | — | ingested |
| TEI P5 4.12.0 height | document | collection | [[10_markdown/documents/tei-p5-height-4.12.0]] | — | ingested |
| TEI P5 4.12.0 heraldry | document | collection | [[10_markdown/documents/tei-p5-heraldry-4.12.0]] | — | ingested |
| TEI P5 4.12.0 hi | document | collection | [[10_markdown/documents/tei-p5-hi-4.12.0]] | — | ingested |
| TEI P5 4.12.0 history | document | collection | [[10_markdown/documents/tei-p5-history-4.12.0]] | — | ingested |
| TEI P5 4.12.0 hom | document | collection | [[10_markdown/documents/tei-p5-hom-4.12.0]] | — | ingested |
| TEI P5 4.12.0 hyph | document | collection | [[10_markdown/documents/tei-p5-hyph-4.12.0]] | — | ingested |
| TEI P5 4.12.0 hyphenation | document | collection | [[10_markdown/documents/tei-p5-hyphenation-4.12.0]] | — | ingested |
| TEI P5 4.12.0 ident | document | collection | [[10_markdown/documents/tei-p5-ident-4.12.0]] | — | ingested |
| TEI P5 4.12.0 idno specification | document | collection | [[10_markdown/documents/tei-p5-idno-4.12.0]] | [[20_distillates/documents/tei-p5-idno-4.12.0]] | distilled |
| TEI P5 4.12.0 if | document | collection | [[10_markdown/documents/tei-p5-if-4.12.0]] | — | ingested |
| TEI P5 4.12.0 iff | document | collection | [[10_markdown/documents/tei-p5-iff-4.12.0]] | — | ingested |
| TEI P5 4.12.0 imprimatur | document | collection | [[10_markdown/documents/tei-p5-imprimatur-4.12.0]] | — | ingested |
| TEI P5 4.12.0 imprint | document | collection | [[10_markdown/documents/tei-p5-imprint-4.12.0]] | — | ingested |
| TEI P5 4.12.0 incident | document | collection | [[10_markdown/documents/tei-p5-incident-4.12.0]] | — | ingested |
| TEI P5 4.12.0 incipit | document | collection | [[10_markdown/documents/tei-p5-incipit-4.12.0]] | — | ingested |
| TEI P5 4.12.0 Index | document | collection | [[10_markdown/documents/tei-p5-guidelines-partind-4.12.0]] | — | ingested |
| TEI P5 4.12.0 index | document | collection | [[10_markdown/documents/tei-p5-index-4.12.0]] | — | ingested |
| TEI P5 4.12.0 iNode | document | collection | [[10_markdown/documents/tei-p5-inode-4.12.0]] | — | ingested |
| TEI P5 4.12.0 institution | document | collection | [[10_markdown/documents/tei-p5-institution-4.12.0]] | — | ingested |
| TEI P5 4.12.0 interaction | document | collection | [[10_markdown/documents/tei-p5-interaction-4.12.0]] | — | ingested |
| TEI P5 4.12.0 interleave | document | collection | [[10_markdown/documents/tei-p5-interleave-4.12.0]] | — | ingested |
| TEI P5 4.12.0 interp | document | collection | [[10_markdown/documents/tei-p5-interp-4.12.0]] | — | ingested |
| TEI P5 4.12.0 interpGrp | document | collection | [[10_markdown/documents/tei-p5-interpgrp-4.12.0]] | — | ingested |
| TEI P5 4.12.0 interpretation | document | collection | [[10_markdown/documents/tei-p5-interpretation-4.12.0]] | — | ingested |
| TEI P5 4.12.0 item | document | collection | [[10_markdown/documents/tei-p5-item-4.12.0]] | — | ingested |
| TEI P5 4.12.0 iType | document | collection | [[10_markdown/documents/tei-p5-itype-4.12.0]] | — | ingested |
| TEI P5 4.12.0 join | document | collection | [[10_markdown/documents/tei-p5-join-4.12.0]] | — | ingested |
| TEI P5 4.12.0 joinGrp | document | collection | [[10_markdown/documents/tei-p5-joingrp-4.12.0]] | — | ingested |
| TEI P5 4.12.0 keywords | document | collection | [[10_markdown/documents/tei-p5-keywords-4.12.0]] | — | ingested |
| TEI P5 4.12.0 kinesic | document | collection | [[10_markdown/documents/tei-p5-kinesic-4.12.0]] | — | ingested |
| TEI P5 4.12.0 l | document | collection | [[10_markdown/documents/tei-p5-l-4.12.0]] | — | ingested |
| TEI P5 4.12.0 label | document | collection | [[10_markdown/documents/tei-p5-label-4.12.0]] | — | ingested |
| TEI P5 4.12.0 lacunaEnd | document | collection | [[10_markdown/documents/tei-p5-lacunaend-4.12.0]] | — | ingested |
| TEI P5 4.12.0 lacunaStart | document | collection | [[10_markdown/documents/tei-p5-lacunastart-4.12.0]] | — | ingested |
| TEI P5 4.12.0 lang | document | collection | [[10_markdown/documents/tei-p5-lang-4.12.0]] | — | ingested |
| TEI P5 4.12.0 langKnowledge | document | collection | [[10_markdown/documents/tei-p5-langknowledge-4.12.0]] | — | ingested |
| TEI P5 4.12.0 langKnown | document | collection | [[10_markdown/documents/tei-p5-langknown-4.12.0]] | — | ingested |
| TEI P5 4.12.0 language | document | collection | [[10_markdown/documents/tei-p5-language-4.12.0]] | — | ingested |
| TEI P5 4.12.0 Language Corpora | document | collection | [[10_markdown/documents/tei-p5-guidelines-cc-languagecorpora-4.12.0]] | — | ingested |
| TEI P5 4.12.0 Languages and Character Sets | document | collection | [[10_markdown/documents/tei-p5-guidelines-ch-languagescharactersets-4.12.0]] | — | ingested |
| TEI P5 4.12.0 langUsage | document | collection | [[10_markdown/documents/tei-p5-langusage-4.12.0]] | — | ingested |
| TEI P5 4.12.0 layout | document | collection | [[10_markdown/documents/tei-p5-layout-4.12.0]] | — | ingested |
| TEI P5 4.12.0 layoutDesc | document | collection | [[10_markdown/documents/tei-p5-layoutdesc-4.12.0]] | — | ingested |
| TEI P5 4.12.0 lb | document | collection | [[10_markdown/documents/tei-p5-lb-4.12.0]] | — | ingested |
| TEI P5 4.12.0 lbl | document | collection | [[10_markdown/documents/tei-p5-lbl-4.12.0]] | — | ingested |
| TEI P5 4.12.0 leaf | document | collection | [[10_markdown/documents/tei-p5-leaf-4.12.0]] | — | ingested |
| TEI P5 4.12.0 lem | document | collection | [[10_markdown/documents/tei-p5-lem-4.12.0]] | — | ingested |
| TEI P5 4.12.0 lg | document | collection | [[10_markdown/documents/tei-p5-lg-4.12.0]] | — | ingested |
| TEI P5 4.12.0 licence | document | collection | [[10_markdown/documents/tei-p5-licence-4.12.0]] | — | ingested |
| TEI P5 4.12.0 line | document | collection | [[10_markdown/documents/tei-p5-line-4.12.0]] | — | ingested |
| TEI P5 4.12.0 link | document | collection | [[10_markdown/documents/tei-p5-link-4.12.0]] | — | ingested |
| TEI P5 4.12.0 linkGrp | document | collection | [[10_markdown/documents/tei-p5-linkgrp-4.12.0]] | — | ingested |
| TEI P5 4.12.0 Linking, Segmentation, and Alignment | document | collection | [[10_markdown/documents/tei-p5-guidelines-sa-linkingsegmentationalignment-4.12.0]] | — | ingested |
| TEI P5 4.12.0 list | document | collection | [[10_markdown/documents/tei-p5-list-4.12.0]] | — | ingested |
| TEI P5 4.12.0 listAnnotation | document | collection | [[10_markdown/documents/tei-p5-listannotation-4.12.0]] | — | ingested |
| TEI P5 4.12.0 listApp | document | collection | [[10_markdown/documents/tei-p5-listapp-4.12.0]] | — | ingested |
| TEI P5 4.12.0 listBibl | document | collection | [[10_markdown/documents/tei-p5-listbibl-4.12.0]] | — | ingested |
| TEI P5 4.12.0 listChange | document | collection | [[10_markdown/documents/tei-p5-listchange-4.12.0]] | — | ingested |
| TEI P5 4.12.0 listEvent | document | collection | [[10_markdown/documents/tei-p5-listevent-4.12.0]] | — | ingested |
| TEI P5 4.12.0 listForest | document | collection | [[10_markdown/documents/tei-p5-listforest-4.12.0]] | — | ingested |
| TEI P5 4.12.0 listNym | document | collection | [[10_markdown/documents/tei-p5-listnym-4.12.0]] | — | ingested |
| TEI P5 4.12.0 listObject | document | collection | [[10_markdown/documents/tei-p5-listobject-4.12.0]] | — | ingested |
| TEI P5 4.12.0 listOrg | document | collection | [[10_markdown/documents/tei-p5-listorg-4.12.0]] | — | ingested |
| TEI P5 4.12.0 listPerson | document | collection | [[10_markdown/documents/tei-p5-listperson-4.12.0]] | — | ingested |
| TEI P5 4.12.0 listPlace | document | collection | [[10_markdown/documents/tei-p5-listplace-4.12.0]] | — | ingested |
| TEI P5 4.12.0 listPrefixDef | document | collection | [[10_markdown/documents/tei-p5-listprefixdef-4.12.0]] | — | ingested |
| TEI P5 4.12.0 listRef | document | collection | [[10_markdown/documents/tei-p5-listref-4.12.0]] | — | ingested |
| TEI P5 4.12.0 listRelation | document | collection | [[10_markdown/documents/tei-p5-listrelation-4.12.0]] | — | ingested |
| TEI P5 4.12.0 listTranspose | document | collection | [[10_markdown/documents/tei-p5-listtranspose-4.12.0]] | — | ingested |
| TEI P5 4.12.0 listWit | document | collection | [[10_markdown/documents/tei-p5-listwit-4.12.0]] | — | ingested |
| TEI P5 4.12.0 locale | document | collection | [[10_markdown/documents/tei-p5-locale-4.12.0]] | — | ingested |
| TEI P5 4.12.0 localProp | document | collection | [[10_markdown/documents/tei-p5-localprop-4.12.0]] | — | ingested |
| TEI P5 4.12.0 location | document | collection | [[10_markdown/documents/tei-p5-location-4.12.0]] | — | ingested |
| TEI P5 4.12.0 locus | document | collection | [[10_markdown/documents/tei-p5-locus-4.12.0]] | — | ingested |
| TEI P5 4.12.0 locusGrp | document | collection | [[10_markdown/documents/tei-p5-locusgrp-4.12.0]] | — | ingested |
| TEI P5 4.12.0 m | document | collection | [[10_markdown/documents/tei-p5-m-4.12.0]] | — | ingested |
| TEI P5 4.12.0 macro.abContent | document | collection | [[10_markdown/documents/tei-p5-macro.abcontent-4.12.0]] | — | ingested |
| TEI P5 4.12.0 macro.limitedContent | document | collection | [[10_markdown/documents/tei-p5-macro.limitedcontent-4.12.0]] | — | ingested |
| TEI P5 4.12.0 macro.paraContent | document | collection | [[10_markdown/documents/tei-p5-macro.paracontent-4.12.0]] | — | ingested |
| TEI P5 4.12.0 macro.phraseSeq | document | collection | [[10_markdown/documents/tei-p5-macro.phraseseq-4.12.0]] | — | ingested |
| TEI P5 4.12.0 macro.phraseSeq.limited | document | collection | [[10_markdown/documents/tei-p5-macro.phraseseq.limited-4.12.0]] | — | ingested |
| TEI P5 4.12.0 macro.specialPara | document | collection | [[10_markdown/documents/tei-p5-macro.specialpara-4.12.0]] | — | ingested |
| TEI P5 4.12.0 macro.specialPara.cmc | document | collection | [[10_markdown/documents/tei-p5-macro.specialpara.cmc-4.12.0]] | — | ingested |
| TEI P5 4.12.0 macro.xtext | document | collection | [[10_markdown/documents/tei-p5-macro.xtext-4.12.0]] | — | ingested |
| TEI P5 4.12.0 macroRef | document | collection | [[10_markdown/documents/tei-p5-macroref-4.12.0]] | — | ingested |
| TEI P5 4.12.0 macroSpec | document | collection | [[10_markdown/documents/tei-p5-macrospec-4.12.0]] | — | ingested |
| TEI P5 4.12.0 Manuscript Description | document | collection | [[10_markdown/documents/tei-p5-guidelines-ms-manuscriptdescription-4.12.0]] | — | ingested |
| TEI P5 4.12.0 mapping | document | collection | [[10_markdown/documents/tei-p5-mapping-4.12.0]] | — | ingested |
| TEI P5 4.12.0 material | document | collection | [[10_markdown/documents/tei-p5-material-4.12.0]] | — | ingested |
| TEI P5 4.12.0 measure | document | collection | [[10_markdown/documents/tei-p5-measure-4.12.0]] | — | ingested |
| TEI P5 4.12.0 measureGrp | document | collection | [[10_markdown/documents/tei-p5-measuregrp-4.12.0]] | — | ingested |
| TEI P5 4.12.0 media | document | collection | [[10_markdown/documents/tei-p5-media-4.12.0]] | — | ingested |
| TEI P5 4.12.0 meeting | document | collection | [[10_markdown/documents/tei-p5-meeting-4.12.0]] | — | ingested |
| TEI P5 4.12.0 memberOf | document | collection | [[10_markdown/documents/tei-p5-memberof-4.12.0]] | — | ingested |
| TEI P5 4.12.0 mentioned | document | collection | [[10_markdown/documents/tei-p5-mentioned-4.12.0]] | — | ingested |
| TEI P5 4.12.0 metamark | document | collection | [[10_markdown/documents/tei-p5-metamark-4.12.0]] | — | ingested |
| TEI P5 4.12.0 metDecl | document | collection | [[10_markdown/documents/tei-p5-metdecl-4.12.0]] | — | ingested |
| TEI P5 4.12.0 metSym | document | collection | [[10_markdown/documents/tei-p5-metsym-4.12.0]] | — | ingested |
| TEI P5 4.12.0 milestone | document | collection | [[10_markdown/documents/tei-p5-milestone-4.12.0]] | — | ingested |
| TEI P5 4.12.0 mod | document | collection | [[10_markdown/documents/tei-p5-mod-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model | document | collection | [[10_markdown/documents/tei-p5-model-4.12.0]] | — | ingested |
| TEI P5 4.12.0 Model Classes | document | collection | [[10_markdown/documents/tei-p5-guidelines-ref-classes-model-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.addressLike | document | collection | [[10_markdown/documents/tei-p5-model.addresslike-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.addrPart | document | collection | [[10_markdown/documents/tei-p5-model.addrpart-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.annotationLike | document | collection | [[10_markdown/documents/tei-p5-model.annotationlike-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.annotationPart.body | document | collection | [[10_markdown/documents/tei-p5-model.annotationpart.body-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.applicationLike | document | collection | [[10_markdown/documents/tei-p5-model.applicationlike-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.attributable | document | collection | [[10_markdown/documents/tei-p5-model.attributable-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.availabilityPart | document | collection | [[10_markdown/documents/tei-p5-model.availabilitypart-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.biblLike | document | collection | [[10_markdown/documents/tei-p5-model.bibllike-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.biblPart | document | collection | [[10_markdown/documents/tei-p5-model.biblpart-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.castItemPart | document | collection | [[10_markdown/documents/tei-p5-model.castitempart-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.catDescPart | document | collection | [[10_markdown/documents/tei-p5-model.catdescpart-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.certLike | document | collection | [[10_markdown/documents/tei-p5-model.certlike-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.choicePart | document | collection | [[10_markdown/documents/tei-p5-model.choicepart-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.cmc | document | collection | [[10_markdown/documents/tei-p5-model.cmc-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.common | document | collection | [[10_markdown/documents/tei-p5-model.common-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.contentPart | document | collection | [[10_markdown/documents/tei-p5-model.contentpart-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.correspActionPart | document | collection | [[10_markdown/documents/tei-p5-model.correspactionpart-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.correspContextPart | document | collection | [[10_markdown/documents/tei-p5-model.correspcontextpart-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.correspDescPart | document | collection | [[10_markdown/documents/tei-p5-model.correspdescpart-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.dateLike | document | collection | [[10_markdown/documents/tei-p5-model.datelike-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.descLike | document | collection | [[10_markdown/documents/tei-p5-model.desclike-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.describedResource | document | collection | [[10_markdown/documents/tei-p5-model.describedresource-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.dimLike | document | collection | [[10_markdown/documents/tei-p5-model.dimlike-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.div1Like | document | collection | [[10_markdown/documents/tei-p5-model.div1like-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.div2Like | document | collection | [[10_markdown/documents/tei-p5-model.div2like-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.div3Like | document | collection | [[10_markdown/documents/tei-p5-model.div3like-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.div4Like | document | collection | [[10_markdown/documents/tei-p5-model.div4like-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.div5Like | document | collection | [[10_markdown/documents/tei-p5-model.div5like-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.div6Like | document | collection | [[10_markdown/documents/tei-p5-model.div6like-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.div7Like | document | collection | [[10_markdown/documents/tei-p5-model.div7like-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.divBottom | document | collection | [[10_markdown/documents/tei-p5-model.divbottom-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.divBottomPart | document | collection | [[10_markdown/documents/tei-p5-model.divbottompart-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.divGenLike | document | collection | [[10_markdown/documents/tei-p5-model.divgenlike-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.divLike | document | collection | [[10_markdown/documents/tei-p5-model.divlike-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.divPart | document | collection | [[10_markdown/documents/tei-p5-model.divpart-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.divPart.spoken | document | collection | [[10_markdown/documents/tei-p5-model.divpart.spoken-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.divTop | document | collection | [[10_markdown/documents/tei-p5-model.divtop-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.divTopPart | document | collection | [[10_markdown/documents/tei-p5-model.divtoppart-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.divWrapper | document | collection | [[10_markdown/documents/tei-p5-model.divwrapper-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.editorialDeclPart | document | collection | [[10_markdown/documents/tei-p5-model.editorialdeclpart-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.egLike | document | collection | [[10_markdown/documents/tei-p5-model.eglike-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.emphLike | document | collection | [[10_markdown/documents/tei-p5-model.emphlike-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.encodingDescPart | document | collection | [[10_markdown/documents/tei-p5-model.encodingdescpart-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.entryLike | document | collection | [[10_markdown/documents/tei-p5-model.entrylike-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.entryPart | document | collection | [[10_markdown/documents/tei-p5-model.entrypart-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.entryPart.top | document | collection | [[10_markdown/documents/tei-p5-model.entrypart.top-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.eventLike | document | collection | [[10_markdown/documents/tei-p5-model.eventlike-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.featureVal | document | collection | [[10_markdown/documents/tei-p5-model.featureval-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.featureVal.complex | document | collection | [[10_markdown/documents/tei-p5-model.featureval.complex-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.featureVal.single | document | collection | [[10_markdown/documents/tei-p5-model.featureval.single-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.formPart | document | collection | [[10_markdown/documents/tei-p5-model.formpart-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.frontPart | document | collection | [[10_markdown/documents/tei-p5-model.frontpart-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.frontPart.drama | document | collection | [[10_markdown/documents/tei-p5-model.frontpart.drama-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.fsdDeclPart | document | collection | [[10_markdown/documents/tei-p5-model.fsddeclpart-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.gLike | document | collection | [[10_markdown/documents/tei-p5-model.glike-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.global | document | collection | [[10_markdown/documents/tei-p5-model.global-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.global.edit | document | collection | [[10_markdown/documents/tei-p5-model.global.edit-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.global.meta | document | collection | [[10_markdown/documents/tei-p5-model.global.meta-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.global.spoken | document | collection | [[10_markdown/documents/tei-p5-model.global.spoken-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.gramPart | document | collection | [[10_markdown/documents/tei-p5-model.grampart-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.graphicLike | document | collection | [[10_markdown/documents/tei-p5-model.graphiclike-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.headLike | document | collection | [[10_markdown/documents/tei-p5-model.headlike-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.highlighted | document | collection | [[10_markdown/documents/tei-p5-model.highlighted-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.hiLike | document | collection | [[10_markdown/documents/tei-p5-model.hilike-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.identEquiv | document | collection | [[10_markdown/documents/tei-p5-model.identequiv-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.identSynonyms | document | collection | [[10_markdown/documents/tei-p5-model.identsynonyms-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.imprintPart | document | collection | [[10_markdown/documents/tei-p5-model.imprintpart-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.inter | document | collection | [[10_markdown/documents/tei-p5-model.inter-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.labelLike | document | collection | [[10_markdown/documents/tei-p5-model.labellike-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.lexicalRefinement | document | collection | [[10_markdown/documents/tei-p5-model.lexicalrefinement-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.limitedPhrase | document | collection | [[10_markdown/documents/tei-p5-model.limitedphrase-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.linePart | document | collection | [[10_markdown/documents/tei-p5-model.linepart-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.listLike | document | collection | [[10_markdown/documents/tei-p5-model.listlike-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.lLike | document | collection | [[10_markdown/documents/tei-p5-model.llike-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.lPart | document | collection | [[10_markdown/documents/tei-p5-model.lpart-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.measureLike | document | collection | [[10_markdown/documents/tei-p5-model.measurelike-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.milestoneLike | document | collection | [[10_markdown/documents/tei-p5-model.milestonelike-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.morphLike | document | collection | [[10_markdown/documents/tei-p5-model.morphlike-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.msItemPart | document | collection | [[10_markdown/documents/tei-p5-model.msitempart-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.msQuoteLike | document | collection | [[10_markdown/documents/tei-p5-model.msquotelike-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.nameLike | document | collection | [[10_markdown/documents/tei-p5-model.namelike-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.nameLike.agent | document | collection | [[10_markdown/documents/tei-p5-model.namelike.agent-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.noteLike | document | collection | [[10_markdown/documents/tei-p5-model.notelike-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.objectLike | document | collection | [[10_markdown/documents/tei-p5-model.objectlike-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.oddDecl | document | collection | [[10_markdown/documents/tei-p5-model.odddecl-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.oddRef | document | collection | [[10_markdown/documents/tei-p5-model.oddref-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.offsetLike | document | collection | [[10_markdown/documents/tei-p5-model.offsetlike-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.orgPart | document | collection | [[10_markdown/documents/tei-p5-model.orgpart-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.orgStateLike | document | collection | [[10_markdown/documents/tei-p5-model.orgstatelike-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.paraPart | document | collection | [[10_markdown/documents/tei-p5-model.parapart-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.persNamePart | document | collection | [[10_markdown/documents/tei-p5-model.persnamepart-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.personLike | document | collection | [[10_markdown/documents/tei-p5-model.personlike-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.personPart | document | collection | [[10_markdown/documents/tei-p5-model.personpart-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.persStateLike | document | collection | [[10_markdown/documents/tei-p5-model.persstatelike-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.phrase | document | collection | [[10_markdown/documents/tei-p5-model.phrase-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.phrase.xml | document | collection | [[10_markdown/documents/tei-p5-model.phrase.xml-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.physDescPart | document | collection | [[10_markdown/documents/tei-p5-model.physdescpart-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.placeLike | document | collection | [[10_markdown/documents/tei-p5-model.placelike-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.placeNamePart | document | collection | [[10_markdown/documents/tei-p5-model.placenamepart-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.placeStateLike | document | collection | [[10_markdown/documents/tei-p5-model.placestatelike-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.pLike | document | collection | [[10_markdown/documents/tei-p5-model.plike-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.pLike.front | document | collection | [[10_markdown/documents/tei-p5-model.plike.front-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.pPart.data | document | collection | [[10_markdown/documents/tei-p5-model.ppart.data-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.pPart.edit | document | collection | [[10_markdown/documents/tei-p5-model.ppart.edit-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.pPart.editorial | document | collection | [[10_markdown/documents/tei-p5-model.ppart.editorial-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.pPart.msdesc | document | collection | [[10_markdown/documents/tei-p5-model.ppart.msdesc-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.pPart.transcriptional | document | collection | [[10_markdown/documents/tei-p5-model.ppart.transcriptional-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.profileDescPart | document | collection | [[10_markdown/documents/tei-p5-model.profiledescpart-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.ptrLike | document | collection | [[10_markdown/documents/tei-p5-model.ptrlike-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.ptrLike.form | document | collection | [[10_markdown/documents/tei-p5-model.ptrlike.form-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.publicationStmtPart.agency | document | collection | [[10_markdown/documents/tei-p5-model.publicationstmtpart.agency-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.publicationStmtPart.detail | document | collection | [[10_markdown/documents/tei-p5-model.publicationstmtpart.detail-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.quoteLike | document | collection | [[10_markdown/documents/tei-p5-model.quotelike-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.rdgLike | document | collection | [[10_markdown/documents/tei-p5-model.rdglike-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.rdgPart | document | collection | [[10_markdown/documents/tei-p5-model.rdgpart-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.recordingPart | document | collection | [[10_markdown/documents/tei-p5-model.recordingpart-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.resource | document | collection | [[10_markdown/documents/tei-p5-model.resource-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.respLike | document | collection | [[10_markdown/documents/tei-p5-model.resplike-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.segLike | document | collection | [[10_markdown/documents/tei-p5-model.seglike-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.settingPart | document | collection | [[10_markdown/documents/tei-p5-model.settingpart-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.sourceDescPart | document | collection | [[10_markdown/documents/tei-p5-model.sourcedescpart-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.specDescLike | document | collection | [[10_markdown/documents/tei-p5-model.specdesclike-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.stageLike | document | collection | [[10_markdown/documents/tei-p5-model.stagelike-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.standOffPart | document | collection | [[10_markdown/documents/tei-p5-model.standoffpart-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.teiHeaderPart | document | collection | [[10_markdown/documents/tei-p5-model.teiheaderpart-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.textDescPart | document | collection | [[10_markdown/documents/tei-p5-model.textdescpart-4.12.0]] | — | ingested |
| TEI P5 4.12.0 model.titlepagePart | document | collection | [[10_markdown/documents/tei-p5-model.titlepagepart-4.12.0]] | — | ingested |
| TEI P5 4.12.0 modelGrp | document | collection | [[10_markdown/documents/tei-p5-modelgrp-4.12.0]] | — | ingested |
| TEI P5 4.12.0 modelSequence | document | collection | [[10_markdown/documents/tei-p5-modelsequence-4.12.0]] | — | ingested |
| TEI P5 4.12.0 moduleRef | document | collection | [[10_markdown/documents/tei-p5-moduleref-4.12.0]] | — | ingested |
| TEI P5 4.12.0 moduleSpec | document | collection | [[10_markdown/documents/tei-p5-modulespec-4.12.0]] | — | ingested |
| TEI P5 4.12.0 monogr | document | collection | [[10_markdown/documents/tei-p5-monogr-4.12.0]] | — | ingested |
| TEI P5 4.12.0 mood | document | collection | [[10_markdown/documents/tei-p5-mood-4.12.0]] | — | ingested |
| TEI P5 4.12.0 move | document | collection | [[10_markdown/documents/tei-p5-move-4.12.0]] | — | ingested |
| TEI P5 4.12.0 msContents | document | collection | [[10_markdown/documents/tei-p5-mscontents-4.12.0]] | — | ingested |
| TEI P5 4.12.0 msDesc | document | collection | [[10_markdown/documents/tei-p5-msdesc-4.12.0]] | — | ingested |
| TEI P5 4.12.0 msFrag | document | collection | [[10_markdown/documents/tei-p5-msfrag-4.12.0]] | — | ingested |
| TEI P5 4.12.0 msIdentifier | document | collection | [[10_markdown/documents/tei-p5-msidentifier-4.12.0]] | — | ingested |
| TEI P5 4.12.0 msItem | document | collection | [[10_markdown/documents/tei-p5-msitem-4.12.0]] | — | ingested |
| TEI P5 4.12.0 msItemStruct | document | collection | [[10_markdown/documents/tei-p5-msitemstruct-4.12.0]] | — | ingested |
| TEI P5 4.12.0 msName | document | collection | [[10_markdown/documents/tei-p5-msname-4.12.0]] | — | ingested |
| TEI P5 4.12.0 msPart | document | collection | [[10_markdown/documents/tei-p5-mspart-4.12.0]] | — | ingested |
| TEI P5 4.12.0 musicNotation | document | collection | [[10_markdown/documents/tei-p5-musicnotation-4.12.0]] | — | ingested |
| TEI P5 4.12.0 name specification | document | collection | [[10_markdown/documents/tei-p5-name-4.12.0]] | [[20_distillates/documents/tei-p5-name-4.12.0]] | distilled |
| TEI P5 4.12.0 nameLink | document | collection | [[10_markdown/documents/tei-p5-namelink-4.12.0]] | — | ingested |
| TEI P5 4.12.0 namespace | document | collection | [[10_markdown/documents/tei-p5-namespace-4.12.0]] | — | ingested |
| TEI P5 4.12.0 nationality | document | collection | [[10_markdown/documents/tei-p5-nationality-4.12.0]] | — | ingested |
| TEI P5 4.12.0 node | document | collection | [[10_markdown/documents/tei-p5-node-4.12.0]] | — | ingested |
| TEI P5 4.12.0 Non-hierarchical Structures | document | collection | [[10_markdown/documents/tei-p5-guidelines-nh-non-hierarchical-4.12.0]] | — | ingested |
| TEI P5 4.12.0 normalization | document | collection | [[10_markdown/documents/tei-p5-normalization-4.12.0]] | — | ingested |
| TEI P5 4.12.0 notatedMusic | document | collection | [[10_markdown/documents/tei-p5-notatedmusic-4.12.0]] | — | ingested |
| TEI P5 4.12.0 note | document | collection | [[10_markdown/documents/tei-p5-note-4.12.0]] | — | ingested |
| TEI P5 4.12.0 noteGrp | document | collection | [[10_markdown/documents/tei-p5-notegrp-4.12.0]] | — | ingested |
| TEI P5 4.12.0 notesStmt | document | collection | [[10_markdown/documents/tei-p5-notesstmt-4.12.0]] | — | ingested |
| TEI P5 4.12.0 num | document | collection | [[10_markdown/documents/tei-p5-num-4.12.0]] | — | ingested |
| TEI P5 4.12.0 number | document | collection | [[10_markdown/documents/tei-p5-number-4.12.0]] | — | ingested |
| TEI P5 4.12.0 numeric | document | collection | [[10_markdown/documents/tei-p5-numeric-4.12.0]] | — | ingested |
| TEI P5 4.12.0 nym specification | document | collection | [[10_markdown/documents/tei-p5-nym-4.12.0]] | [[20_distillates/documents/tei-p5-nym-4.12.0]] | distilled |
| TEI P5 4.12.0 object | document | collection | [[10_markdown/documents/tei-p5-object-4.12.0]] | — | ingested |
| TEI P5 4.12.0 objectDesc | document | collection | [[10_markdown/documents/tei-p5-objectdesc-4.12.0]] | — | ingested |
| TEI P5 4.12.0 objectIdentifier | document | collection | [[10_markdown/documents/tei-p5-objectidentifier-4.12.0]] | — | ingested |
| TEI P5 4.12.0 objectName | document | collection | [[10_markdown/documents/tei-p5-objectname-4.12.0]] | — | ingested |
| TEI P5 4.12.0 objectType | document | collection | [[10_markdown/documents/tei-p5-objecttype-4.12.0]] | — | ingested |
| TEI P5 4.12.0 occupation | document | collection | [[10_markdown/documents/tei-p5-occupation-4.12.0]] | — | ingested |
| TEI P5 4.12.0 offset | document | collection | [[10_markdown/documents/tei-p5-offset-4.12.0]] | — | ingested |
| TEI P5 4.12.0 opener | document | collection | [[10_markdown/documents/tei-p5-opener-4.12.0]] | — | ingested |
| TEI P5 4.12.0 oRef | document | collection | [[10_markdown/documents/tei-p5-oref-4.12.0]] | — | ingested |
| TEI P5 4.12.0 org | document | collection | [[10_markdown/documents/tei-p5-org-4.12.0]] | — | ingested |
| TEI P5 4.12.0 orgName | document | collection | [[10_markdown/documents/tei-p5-orgname-4.12.0]] | — | ingested |
| TEI P5 4.12.0 orig | document | collection | [[10_markdown/documents/tei-p5-orig-4.12.0]] | — | ingested |
| TEI P5 4.12.0 origDate | document | collection | [[10_markdown/documents/tei-p5-origdate-4.12.0]] | — | ingested |
| TEI P5 4.12.0 origin | document | collection | [[10_markdown/documents/tei-p5-origin-4.12.0]] | — | ingested |
| TEI P5 4.12.0 origPlace | document | collection | [[10_markdown/documents/tei-p5-origplace-4.12.0]] | — | ingested |
| TEI P5 4.12.0 orth | document | collection | [[10_markdown/documents/tei-p5-orth-4.12.0]] | — | ingested |
| TEI P5 4.12.0 outputRendition | document | collection | [[10_markdown/documents/tei-p5-outputrendition-4.12.0]] | — | ingested |
| TEI P5 4.12.0 p | document | collection | [[10_markdown/documents/tei-p5-p-4.12.0]] | — | ingested |
| TEI P5 4.12.0 param | document | collection | [[10_markdown/documents/tei-p5-param-4.12.0]] | — | ingested |
| TEI P5 4.12.0 paramList | document | collection | [[10_markdown/documents/tei-p5-paramlist-4.12.0]] | — | ingested |
| TEI P5 4.12.0 paramSpec | document | collection | [[10_markdown/documents/tei-p5-paramspec-4.12.0]] | — | ingested |
| TEI P5 4.12.0 particDesc | document | collection | [[10_markdown/documents/tei-p5-particdesc-4.12.0]] | — | ingested |
| TEI P5 4.12.0 path | document | collection | [[10_markdown/documents/tei-p5-path-4.12.0]] | — | ingested |
| TEI P5 4.12.0 pause | document | collection | [[10_markdown/documents/tei-p5-pause-4.12.0]] | — | ingested |
| TEI P5 4.12.0 pb | document | collection | [[10_markdown/documents/tei-p5-pb-4.12.0]] | — | ingested |
| TEI P5 4.12.0 pc | document | collection | [[10_markdown/documents/tei-p5-pc-4.12.0]] | — | ingested |
| TEI P5 4.12.0 per | document | collection | [[10_markdown/documents/tei-p5-per-4.12.0]] | — | ingested |
| TEI P5 4.12.0 performance | document | collection | [[10_markdown/documents/tei-p5-performance-4.12.0]] | — | ingested |
| TEI P5 4.12.0 Performance Texts | document | collection | [[10_markdown/documents/tei-p5-guidelines-dr-performancetexts-4.12.0]] | — | ingested |
| TEI P5 4.12.0 persName specification | document | collection | [[10_markdown/documents/tei-p5-persname-4.12.0]] | [[20_distillates/documents/tei-p5-persname-4.12.0]] | distilled |
| TEI P5 4.12.0 person specification | document | collection | [[10_markdown/documents/tei-p5-person-4.12.0]] | [[20_distillates/documents/tei-p5-person-4.12.0]] | distilled |
| TEI P5 4.12.0 persona | document | collection | [[10_markdown/documents/tei-p5-persona-4.12.0]] | — | ingested |
| TEI P5 4.12.0 personGrp | document | collection | [[10_markdown/documents/tei-p5-persongrp-4.12.0]] | — | ingested |
| TEI P5 4.12.0 persPronouns | document | collection | [[10_markdown/documents/tei-p5-perspronouns-4.12.0]] | — | ingested |
| TEI P5 4.12.0 phr | document | collection | [[10_markdown/documents/tei-p5-phr-4.12.0]] | — | ingested |
| TEI P5 4.12.0 physDesc | document | collection | [[10_markdown/documents/tei-p5-physdesc-4.12.0]] | — | ingested |
| TEI P5 4.12.0 place specification | document | collection | [[10_markdown/documents/tei-p5-place-4.12.0]] | [[20_distillates/documents/tei-p5-place-4.12.0]] | distilled |
| TEI P5 4.12.0 placeName | document | collection | [[10_markdown/documents/tei-p5-placename-4.12.0]] | — | ingested |
| TEI P5 4.12.0 poems | document | collection | [[10_markdown/documents/tei-p5-guidelines-poems-4.12.0]] | — | ingested |
| TEI P5 4.12.0 population | document | collection | [[10_markdown/documents/tei-p5-population-4.12.0]] | — | ingested |
| TEI P5 4.12.0 pos | document | collection | [[10_markdown/documents/tei-p5-pos-4.12.0]] | — | ingested |
| TEI P5 4.12.0 post | document | collection | [[10_markdown/documents/tei-p5-post-4.12.0]] | — | ingested |
| TEI P5 4.12.0 postBox | document | collection | [[10_markdown/documents/tei-p5-postbox-4.12.0]] | — | ingested |
| TEI P5 4.12.0 postCode | document | collection | [[10_markdown/documents/tei-p5-postcode-4.12.0]] | — | ingested |
| TEI P5 4.12.0 postscript | document | collection | [[10_markdown/documents/tei-p5-postscript-4.12.0]] | — | ingested |
| TEI P5 4.12.0 precision | document | collection | [[10_markdown/documents/tei-p5-precision-4.12.0]] | — | ingested |
| TEI P5 4.12.0 pRef | document | collection | [[10_markdown/documents/tei-p5-pref-4.12.0]] | — | ingested |
| TEI P5 4.12.0 Preface and Acknowledgments | document | collection | [[10_markdown/documents/tei-p5-guidelines-fm1-introductorynote-4.12.0]] | — | ingested |
| TEI P5 4.12.0 Prefatory Notes | document | collection | [[10_markdown/documents/tei-p5-guidelines-prefatorynote-4.12.0]] | — | ingested |
| TEI P5 4.12.0 prefixDef | document | collection | [[10_markdown/documents/tei-p5-prefixdef-4.12.0]] | — | ingested |
| TEI P5 4.12.0 preparedness | document | collection | [[10_markdown/documents/tei-p5-preparedness-4.12.0]] | — | ingested |
| TEI P5 4.12.0 principal | document | collection | [[10_markdown/documents/tei-p5-principal-4.12.0]] | — | ingested |
| TEI P5 4.12.0 profileDesc | document | collection | [[10_markdown/documents/tei-p5-profiledesc-4.12.0]] | — | ingested |
| TEI P5 4.12.0 projectDesc | document | collection | [[10_markdown/documents/tei-p5-projectdesc-4.12.0]] | — | ingested |
| TEI P5 4.12.0 prologue | document | collection | [[10_markdown/documents/tei-p5-prologue-4.12.0]] | — | ingested |
| TEI P5 4.12.0 pron | document | collection | [[10_markdown/documents/tei-p5-pron-4.12.0]] | — | ingested |
| TEI P5 4.12.0 provenance | document | collection | [[10_markdown/documents/tei-p5-provenance-4.12.0]] | — | ingested |
| TEI P5 4.12.0 ptr | document | collection | [[10_markdown/documents/tei-p5-ptr-4.12.0]] | — | ingested |
| TEI P5 4.12.0 publicationStmt | document | collection | [[10_markdown/documents/tei-p5-publicationstmt-4.12.0]] | — | ingested |
| TEI P5 4.12.0 publisher | document | collection | [[10_markdown/documents/tei-p5-publisher-4.12.0]] | — | ingested |
| TEI P5 4.12.0 pubPlace | document | collection | [[10_markdown/documents/tei-p5-pubplace-4.12.0]] | — | ingested |
| TEI P5 4.12.0 punctuation | document | collection | [[10_markdown/documents/tei-p5-punctuation-4.12.0]] | — | ingested |
| TEI P5 4.12.0 purpose | document | collection | [[10_markdown/documents/tei-p5-purpose-4.12.0]] | — | ingested |
| TEI P5 4.12.0 q | document | collection | [[10_markdown/documents/tei-p5-q-4.12.0]] | — | ingested |
| TEI P5 4.12.0 quotation | document | collection | [[10_markdown/documents/tei-p5-quotation-4.12.0]] | — | ingested |
| TEI P5 4.12.0 quote | document | collection | [[10_markdown/documents/tei-p5-quote-4.12.0]] | — | ingested |
| TEI P5 4.12.0 rb | document | collection | [[10_markdown/documents/tei-p5-rb-4.12.0]] | — | ingested |
| TEI P5 4.12.0 rdg | document | collection | [[10_markdown/documents/tei-p5-rdg-4.12.0]] | — | ingested |
| TEI P5 4.12.0 rdgGrp | document | collection | [[10_markdown/documents/tei-p5-rdggrp-4.12.0]] | — | ingested |
| TEI P5 4.12.0 re | document | collection | [[10_markdown/documents/tei-p5-re-4.12.0]] | — | ingested |
| TEI P5 4.12.0 recordHist | document | collection | [[10_markdown/documents/tei-p5-recordhist-4.12.0]] | — | ingested |
| TEI P5 4.12.0 recording | document | collection | [[10_markdown/documents/tei-p5-recording-4.12.0]] | — | ingested |
| TEI P5 4.12.0 recordingStmt | document | collection | [[10_markdown/documents/tei-p5-recordingstmt-4.12.0]] | — | ingested |
| TEI P5 4.12.0 redo | document | collection | [[10_markdown/documents/tei-p5-redo-4.12.0]] | — | ingested |
| TEI P5 4.12.0 ref | document | collection | [[10_markdown/documents/tei-p5-ref-4.12.0]] | — | ingested |
| TEI P5 4.12.0 refsDecl | document | collection | [[10_markdown/documents/tei-p5-refsdecl-4.12.0]] | — | ingested |
| TEI P5 4.12.0 refState | document | collection | [[10_markdown/documents/tei-p5-refstate-4.12.0]] | — | ingested |
| TEI P5 4.12.0 reg | document | collection | [[10_markdown/documents/tei-p5-reg-4.12.0]] | — | ingested |
| TEI P5 4.12.0 region | document | collection | [[10_markdown/documents/tei-p5-region-4.12.0]] | — | ingested |
| TEI P5 4.12.0 relatedItem | document | collection | [[10_markdown/documents/tei-p5-relateditem-4.12.0]] | — | ingested |
| TEI P5 4.12.0 relation specification | document | collection | [[10_markdown/documents/tei-p5-relation-4.12.0]] | [[20_distillates/documents/tei-p5-relation-4.12.0]] | distilled |
| TEI P5 4.12.0 Releases of the TEI Guidelines | document | collection | [[10_markdown/documents/tei-p5-guidelines-titlepageverso-4.12.0]] | — | ingested |
| TEI P5 4.12.0 remarks | document | collection | [[10_markdown/documents/tei-p5-remarks-4.12.0]] | — | ingested |
| TEI P5 4.12.0 rendition | document | collection | [[10_markdown/documents/tei-p5-rendition-4.12.0]] | — | ingested |
| TEI P5 4.12.0 repository | document | collection | [[10_markdown/documents/tei-p5-repository-4.12.0]] | — | ingested |
| TEI P5 4.12.0 Representation of Primary Sources | document | collection | [[10_markdown/documents/tei-p5-guidelines-ph-primarysources-4.12.0]] | — | ingested |
| TEI P5 4.12.0 residence | document | collection | [[10_markdown/documents/tei-p5-residence-4.12.0]] | — | ingested |
| TEI P5 4.12.0 resp | document | collection | [[10_markdown/documents/tei-p5-resp-4.12.0]] | — | ingested |
| TEI P5 4.12.0 respons | document | collection | [[10_markdown/documents/tei-p5-respons-4.12.0]] | — | ingested |
| TEI P5 4.12.0 respStmt | document | collection | [[10_markdown/documents/tei-p5-respstmt-4.12.0]] | — | ingested |
| TEI P5 4.12.0 restore | document | collection | [[10_markdown/documents/tei-p5-restore-4.12.0]] | — | ingested |
| TEI P5 4.12.0 retrace | document | collection | [[10_markdown/documents/tei-p5-retrace-4.12.0]] | — | ingested |
| TEI P5 4.12.0 revisionDesc | document | collection | [[10_markdown/documents/tei-p5-revisiondesc-4.12.0]] | — | ingested |
| TEI P5 4.12.0 rhyme | document | collection | [[10_markdown/documents/tei-p5-rhyme-4.12.0]] | — | ingested |
| TEI P5 4.12.0 role | document | collection | [[10_markdown/documents/tei-p5-role-4.12.0]] | — | ingested |
| TEI P5 4.12.0 roleDesc | document | collection | [[10_markdown/documents/tei-p5-roledesc-4.12.0]] | — | ingested |
| TEI P5 4.12.0 roleName | document | collection | [[10_markdown/documents/tei-p5-rolename-4.12.0]] | — | ingested |
| TEI P5 4.12.0 root | document | collection | [[10_markdown/documents/tei-p5-root-4.12.0]] | — | ingested |
| TEI P5 4.12.0 row | document | collection | [[10_markdown/documents/tei-p5-row-4.12.0]] | — | ingested |
| TEI P5 4.12.0 rs specification | document | collection | [[10_markdown/documents/tei-p5-rs-4.12.0]] | [[20_distillates/documents/tei-p5-rs-4.12.0]] | distilled |
| TEI P5 4.12.0 rt | document | collection | [[10_markdown/documents/tei-p5-rt-4.12.0]] | — | ingested |
| TEI P5 4.12.0 rubric | document | collection | [[10_markdown/documents/tei-p5-rubric-4.12.0]] | — | ingested |
| TEI P5 4.12.0 ruby | document | collection | [[10_markdown/documents/tei-p5-ruby-4.12.0]] | — | ingested |
| TEI P5 4.12.0 s | document | collection | [[10_markdown/documents/tei-p5-s-4.12.0]] | — | ingested |
| TEI P5 4.12.0 said | document | collection | [[10_markdown/documents/tei-p5-said-4.12.0]] | — | ingested |
| TEI P5 4.12.0 salute | document | collection | [[10_markdown/documents/tei-p5-salute-4.12.0]] | — | ingested |
| TEI P5 4.12.0 samplingDecl | document | collection | [[10_markdown/documents/tei-p5-samplingdecl-4.12.0]] | — | ingested |
| TEI P5 4.12.0 schemaRef | document | collection | [[10_markdown/documents/tei-p5-schemaref-4.12.0]] | — | ingested |
| TEI P5 4.12.0 schemaSpec | document | collection | [[10_markdown/documents/tei-p5-schemaspec-4.12.0]] | — | ingested |
| TEI P5 4.12.0 scriptDesc | document | collection | [[10_markdown/documents/tei-p5-scriptdesc-4.12.0]] | — | ingested |
| TEI P5 4.12.0 scriptNote | document | collection | [[10_markdown/documents/tei-p5-scriptnote-4.12.0]] | — | ingested |
| TEI P5 4.12.0 scriptStmt | document | collection | [[10_markdown/documents/tei-p5-scriptstmt-4.12.0]] | — | ingested |
| TEI P5 4.12.0 seal | document | collection | [[10_markdown/documents/tei-p5-seal-4.12.0]] | — | ingested |
| TEI P5 4.12.0 sealDesc | document | collection | [[10_markdown/documents/tei-p5-sealdesc-4.12.0]] | — | ingested |
| TEI P5 4.12.0 secFol | document | collection | [[10_markdown/documents/tei-p5-secfol-4.12.0]] | — | ingested |
| TEI P5 4.12.0 secl | document | collection | [[10_markdown/documents/tei-p5-secl-4.12.0]] | — | ingested |
| TEI P5 4.12.0 seg | document | collection | [[10_markdown/documents/tei-p5-seg-4.12.0]] | — | ingested |
| TEI P5 4.12.0 segmentation | document | collection | [[10_markdown/documents/tei-p5-segmentation-4.12.0]] | — | ingested |
| TEI P5 4.12.0 sense | document | collection | [[10_markdown/documents/tei-p5-sense-4.12.0]] | — | ingested |
| TEI P5 4.12.0 sequence | document | collection | [[10_markdown/documents/tei-p5-sequence-4.12.0]] | — | ingested |
| TEI P5 4.12.0 series | document | collection | [[10_markdown/documents/tei-p5-series-4.12.0]] | — | ingested |
| TEI P5 4.12.0 seriesStmt | document | collection | [[10_markdown/documents/tei-p5-seriesstmt-4.12.0]] | — | ingested |
| TEI P5 4.12.0 set | document | collection | [[10_markdown/documents/tei-p5-set-4.12.0]] | — | ingested |
| TEI P5 4.12.0 setting | document | collection | [[10_markdown/documents/tei-p5-setting-4.12.0]] | — | ingested |
| TEI P5 4.12.0 settingDesc | document | collection | [[10_markdown/documents/tei-p5-settingdesc-4.12.0]] | — | ingested |
| TEI P5 4.12.0 settlement | document | collection | [[10_markdown/documents/tei-p5-settlement-4.12.0]] | — | ingested |
| TEI P5 4.12.0 sex | document | collection | [[10_markdown/documents/tei-p5-sex-4.12.0]] | — | ingested |
| TEI P5 4.12.0 shift | document | collection | [[10_markdown/documents/tei-p5-shift-4.12.0]] | — | ingested |
| TEI P5 4.12.0 sic | document | collection | [[10_markdown/documents/tei-p5-sic-4.12.0]] | — | ingested |
| TEI P5 4.12.0 signatures | document | collection | [[10_markdown/documents/tei-p5-signatures-4.12.0]] | — | ingested |
| TEI P5 4.12.0 signed | document | collection | [[10_markdown/documents/tei-p5-signed-4.12.0]] | — | ingested |
| TEI P5 4.12.0 Simple Analytic Mechanisms | document | collection | [[10_markdown/documents/tei-p5-guidelines-ai-analyticmechanisms-4.12.0]] | — | ingested |
| TEI P5 4.12.0 soCalled | document | collection | [[10_markdown/documents/tei-p5-socalled-4.12.0]] | — | ingested |
| TEI P5 4.12.0 socecStatus | document | collection | [[10_markdown/documents/tei-p5-socecstatus-4.12.0]] | — | ingested |
| TEI P5 4.12.0 sound | document | collection | [[10_markdown/documents/tei-p5-sound-4.12.0]] | — | ingested |
| TEI P5 4.12.0 source | document | collection | [[10_markdown/documents/tei-p5-source-4.12.0]] | — | ingested |
| TEI P5 4.12.0 sourceDesc | document | collection | [[10_markdown/documents/tei-p5-sourcedesc-4.12.0]] | — | ingested |
| TEI P5 4.12.0 sourceDoc | document | collection | [[10_markdown/documents/tei-p5-sourcedoc-4.12.0]] | — | ingested |
| TEI P5 4.12.0 sp | document | collection | [[10_markdown/documents/tei-p5-sp-4.12.0]] | — | ingested |
| TEI P5 4.12.0 space | document | collection | [[10_markdown/documents/tei-p5-space-4.12.0]] | — | ingested |
| TEI P5 4.12.0 span specification | document | collection | [[10_markdown/documents/tei-p5-span-4.12.0]] | [[20_distillates/documents/tei-p5-span-4.12.0]] | distilled |
| TEI P5 4.12.0 spanGrp | document | collection | [[10_markdown/documents/tei-p5-spangrp-4.12.0]] | — | ingested |
| TEI P5 4.12.0 speaker | document | collection | [[10_markdown/documents/tei-p5-speaker-4.12.0]] | — | ingested |
| TEI P5 4.12.0 specDesc | document | collection | [[10_markdown/documents/tei-p5-specdesc-4.12.0]] | — | ingested |
| TEI P5 4.12.0 specGrp | document | collection | [[10_markdown/documents/tei-p5-specgrp-4.12.0]] | — | ingested |
| TEI P5 4.12.0 specGrpRef | document | collection | [[10_markdown/documents/tei-p5-specgrpref-4.12.0]] | — | ingested |
| TEI P5 4.12.0 specList | document | collection | [[10_markdown/documents/tei-p5-speclist-4.12.0]] | — | ingested |
| TEI P5 4.12.0 spGrp | document | collection | [[10_markdown/documents/tei-p5-spgrp-4.12.0]] | — | ingested |
| TEI P5 4.12.0 sponsor | document | collection | [[10_markdown/documents/tei-p5-sponsor-4.12.0]] | — | ingested |
| TEI P5 4.12.0 stage | document | collection | [[10_markdown/documents/tei-p5-stage-4.12.0]] | — | ingested |
| TEI P5 4.12.0 stamp | document | collection | [[10_markdown/documents/tei-p5-stamp-4.12.0]] | — | ingested |
| TEI P5 4.12.0 standOff | document | collection | [[10_markdown/documents/tei-p5-standoff-4.12.0]] | — | ingested |
| TEI P5 4.12.0 state specification | document | collection | [[10_markdown/documents/tei-p5-state-4.12.0]] | [[20_distillates/documents/tei-p5-state-4.12.0]] | distilled |
| TEI P5 4.12.0 stdVals | document | collection | [[10_markdown/documents/tei-p5-stdvals-4.12.0]] | — | ingested |
| TEI P5 4.12.0 street | document | collection | [[10_markdown/documents/tei-p5-street-4.12.0]] | — | ingested |
| TEI P5 4.12.0 stress | document | collection | [[10_markdown/documents/tei-p5-stress-4.12.0]] | — | ingested |
| TEI P5 4.12.0 string | document | collection | [[10_markdown/documents/tei-p5-string-4.12.0]] | — | ingested |
| TEI P5 4.12.0 styleDefDecl | document | collection | [[10_markdown/documents/tei-p5-styledefdecl-4.12.0]] | — | ingested |
| TEI P5 4.12.0 subc | document | collection | [[10_markdown/documents/tei-p5-subc-4.12.0]] | — | ingested |
| TEI P5 4.12.0 subst | document | collection | [[10_markdown/documents/tei-p5-subst-4.12.0]] | — | ingested |
| TEI P5 4.12.0 substJoin | document | collection | [[10_markdown/documents/tei-p5-substjoin-4.12.0]] | — | ingested |
| TEI P5 4.12.0 summary | document | collection | [[10_markdown/documents/tei-p5-summary-4.12.0]] | — | ingested |
| TEI P5 4.12.0 superEntry | document | collection | [[10_markdown/documents/tei-p5-superentry-4.12.0]] | — | ingested |
| TEI P5 4.12.0 supplied | document | collection | [[10_markdown/documents/tei-p5-supplied-4.12.0]] | — | ingested |
| TEI P5 4.12.0 support | document | collection | [[10_markdown/documents/tei-p5-support-4.12.0]] | — | ingested |
| TEI P5 4.12.0 supportDesc | document | collection | [[10_markdown/documents/tei-p5-supportdesc-4.12.0]] | — | ingested |
| TEI P5 4.12.0 surface | document | collection | [[10_markdown/documents/tei-p5-surface-4.12.0]] | — | ingested |
| TEI P5 4.12.0 surfaceGrp | document | collection | [[10_markdown/documents/tei-p5-surfacegrp-4.12.0]] | — | ingested |
| TEI P5 4.12.0 surname | document | collection | [[10_markdown/documents/tei-p5-surname-4.12.0]] | — | ingested |
| TEI P5 4.12.0 surplus | document | collection | [[10_markdown/documents/tei-p5-surplus-4.12.0]] | — | ingested |
| TEI P5 4.12.0 surrogates | document | collection | [[10_markdown/documents/tei-p5-surrogates-4.12.0]] | — | ingested |
| TEI P5 4.12.0 syll | document | collection | [[10_markdown/documents/tei-p5-syll-4.12.0]] | — | ingested |
| TEI P5 4.12.0 symbol | document | collection | [[10_markdown/documents/tei-p5-symbol-4.12.0]] | — | ingested |
| TEI P5 4.12.0 table | document | collection | [[10_markdown/documents/tei-p5-table-4.12.0]] | — | ingested |
| TEI P5 4.12.0 Tables, Formulæ, Graphics, and Notated Music | document | collection | [[10_markdown/documents/tei-p5-guidelines-ft-tablesformulaegraphics-4.12.0]] | — | ingested |
| TEI P5 4.12.0 tag | document | collection | [[10_markdown/documents/tei-p5-tag-4.12.0]] | — | ingested |
| TEI P5 4.12.0 tagsDecl | document | collection | [[10_markdown/documents/tei-p5-tagsdecl-4.12.0]] | — | ingested |
| TEI P5 4.12.0 tagUsage | document | collection | [[10_markdown/documents/tei-p5-tagusage-4.12.0]] | — | ingested |
| TEI P5 4.12.0 taxonomy | document | collection | [[10_markdown/documents/tei-p5-taxonomy-4.12.0]] | — | ingested |
| TEI P5 4.12.0 tech | document | collection | [[10_markdown/documents/tei-p5-tech-4.12.0]] | — | ingested |
| TEI P5 4.12.0 TEI | document | collection | [[10_markdown/documents/tei-p5-tei-4.12.0]] | — | ingested |
| TEI P5 4.12.0 teiCorpus | document | collection | [[10_markdown/documents/tei-p5-teicorpus-4.12.0]] | — | ingested |
| TEI P5 4.12.0 teidata.authority | document | collection | [[10_markdown/documents/tei-p5-teidata.authority-4.12.0]] | — | ingested |
| TEI P5 4.12.0 teidata.certainty | document | collection | [[10_markdown/documents/tei-p5-teidata.certainty-4.12.0]] | — | ingested |
| TEI P5 4.12.0 teidata.count | document | collection | [[10_markdown/documents/tei-p5-teidata.count-4.12.0]] | — | ingested |
| TEI P5 4.12.0 teidata.duration.iso | document | collection | [[10_markdown/documents/tei-p5-teidata.duration.iso-4.12.0]] | — | ingested |
| TEI P5 4.12.0 teidata.duration.w3c | document | collection | [[10_markdown/documents/tei-p5-teidata.duration.w3c-4.12.0]] | — | ingested |
| TEI P5 4.12.0 teidata.enumerated | document | collection | [[10_markdown/documents/tei-p5-teidata.enumerated-4.12.0]] | — | ingested |
| TEI P5 4.12.0 teidata.gender | document | collection | [[10_markdown/documents/tei-p5-teidata.gender-4.12.0]] | — | ingested |
| TEI P5 4.12.0 teidata.interval | document | collection | [[10_markdown/documents/tei-p5-teidata.interval-4.12.0]] | — | ingested |
| TEI P5 4.12.0 teidata.key | document | collection | [[10_markdown/documents/tei-p5-teidata.key-4.12.0]] | — | ingested |
| TEI P5 4.12.0 teidata.language | document | collection | [[10_markdown/documents/tei-p5-teidata.language-4.12.0]] | — | ingested |
| TEI P5 4.12.0 teidata.name | document | collection | [[10_markdown/documents/tei-p5-teidata.name-4.12.0]] | — | ingested |
| TEI P5 4.12.0 teidata.namespace | document | collection | [[10_markdown/documents/tei-p5-teidata.namespace-4.12.0]] | — | ingested |
| TEI P5 4.12.0 teidata.namespaceOrName | document | collection | [[10_markdown/documents/tei-p5-teidata.namespaceorname-4.12.0]] | — | ingested |
| TEI P5 4.12.0 teidata.nullOrName | document | collection | [[10_markdown/documents/tei-p5-teidata.nullorname-4.12.0]] | — | ingested |
| TEI P5 4.12.0 teidata.numeric | document | collection | [[10_markdown/documents/tei-p5-teidata.numeric-4.12.0]] | — | ingested |
| TEI P5 4.12.0 teidata.outputMeasurement | document | collection | [[10_markdown/documents/tei-p5-teidata.outputmeasurement-4.12.0]] | — | ingested |
| TEI P5 4.12.0 teidata.pattern | document | collection | [[10_markdown/documents/tei-p5-teidata.pattern-4.12.0]] | — | ingested |
| TEI P5 4.12.0 teidata.point | document | collection | [[10_markdown/documents/tei-p5-teidata.point-4.12.0]] | — | ingested |
| TEI P5 4.12.0 teidata.pointer | document | collection | [[10_markdown/documents/tei-p5-teidata.pointer-4.12.0]] | — | ingested |
| TEI P5 4.12.0 teidata.prefix | document | collection | [[10_markdown/documents/tei-p5-teidata.prefix-4.12.0]] | — | ingested |
| TEI P5 4.12.0 teidata.probability | document | collection | [[10_markdown/documents/tei-p5-teidata.probability-4.12.0]] | — | ingested |
| TEI P5 4.12.0 teidata.probCert | document | collection | [[10_markdown/documents/tei-p5-teidata.probcert-4.12.0]] | — | ingested |
| TEI P5 4.12.0 teidata.replacement | document | collection | [[10_markdown/documents/tei-p5-teidata.replacement-4.12.0]] | — | ingested |
| TEI P5 4.12.0 teidata.sex | document | collection | [[10_markdown/documents/tei-p5-teidata.sex-4.12.0]] | — | ingested |
| TEI P5 4.12.0 teidata.temporal.iso | document | collection | [[10_markdown/documents/tei-p5-teidata.temporal.iso-4.12.0]] | — | ingested |
| TEI P5 4.12.0 teidata.temporal.w3c | document | collection | [[10_markdown/documents/tei-p5-teidata.temporal.w3c-4.12.0]] | — | ingested |
| TEI P5 4.12.0 teidata.temporal.working | document | collection | [[10_markdown/documents/tei-p5-teidata.temporal.working-4.12.0]] | — | ingested |
| TEI P5 4.12.0 teidata.text | document | collection | [[10_markdown/documents/tei-p5-teidata.text-4.12.0]] | — | ingested |
| TEI P5 4.12.0 teidata.truthValue | document | collection | [[10_markdown/documents/tei-p5-teidata.truthvalue-4.12.0]] | — | ingested |
| TEI P5 4.12.0 teidata.unboundedCount | document | collection | [[10_markdown/documents/tei-p5-teidata.unboundedcount-4.12.0]] | — | ingested |
| TEI P5 4.12.0 teidata.version | document | collection | [[10_markdown/documents/tei-p5-teidata.version-4.12.0]] | — | ingested |
| TEI P5 4.12.0 teidata.versionNumber | document | collection | [[10_markdown/documents/tei-p5-teidata.versionnumber-4.12.0]] | — | ingested |
| TEI P5 4.12.0 teidata.word | document | collection | [[10_markdown/documents/tei-p5-teidata.word-4.12.0]] | — | ingested |
| TEI P5 4.12.0 teidata.xmlName | document | collection | [[10_markdown/documents/tei-p5-teidata.xmlname-4.12.0]] | — | ingested |
| TEI P5 4.12.0 teidata.xpath | document | collection | [[10_markdown/documents/tei-p5-teidata.xpath-4.12.0]] | — | ingested |
| TEI P5 4.12.0 teidata.xTruthValue | document | collection | [[10_markdown/documents/tei-p5-teidata.xtruthvalue-4.12.0]] | — | ingested |
| TEI P5 4.12.0 teiHeader | document | collection | [[10_markdown/documents/tei-p5-teiheader-4.12.0]] | — | ingested |
| TEI P5 4.12.0 term | document | collection | [[10_markdown/documents/tei-p5-term-4.12.0]] | — | ingested |
| TEI P5 4.12.0 terrain | document | collection | [[10_markdown/documents/tei-p5-terrain-4.12.0]] | — | ingested |
| TEI P5 4.12.0 test document testnames.xml | document | collection | [[10_markdown/documents/tei-p5-test-testnames-4.12.0]] | [[20_distillates/documents/tei-p5-test-testnames-4.12.0]] | distilled |
| TEI P5 4.12.0 text | document | collection | [[10_markdown/documents/tei-p5-text-4.12.0]] | — | ingested |
| TEI P5 4.12.0 textClass | document | collection | [[10_markdown/documents/tei-p5-textclass-4.12.0]] | — | ingested |
| TEI P5 4.12.0 textDesc | document | collection | [[10_markdown/documents/tei-p5-textdesc-4.12.0]] | — | ingested |
| TEI P5 4.12.0 textLang | document | collection | [[10_markdown/documents/tei-p5-textlang-4.12.0]] | — | ingested |
| TEI P5 4.12.0 textNode | document | collection | [[10_markdown/documents/tei-p5-textnode-4.12.0]] | — | ingested |
| TEI P5 4.12.0 The TEI Guidelines | document | collection | [[10_markdown/documents/tei-p5-guidelines-guidelines-en-4.12.0]] | — | ingested |
| TEI P5 4.12.0 The TEI Header | document | collection | [[10_markdown/documents/tei-p5-guidelines-hd-header-4.12.0]] | — | ingested |
| TEI P5 4.12.0 The TEI Infrastructure | document | collection | [[10_markdown/documents/tei-p5-guidelines-st-infrastructure-4.12.0]] | — | ingested |
| TEI P5 4.12.0 then | document | collection | [[10_markdown/documents/tei-p5-then-4.12.0]] | — | ingested |
| TEI P5 4.12.0 time | document | collection | [[10_markdown/documents/tei-p5-time-4.12.0]] | — | ingested |
| TEI P5 4.12.0 timeline | document | collection | [[10_markdown/documents/tei-p5-timeline-4.12.0]] | — | ingested |
| TEI P5 4.12.0 title | document | collection | [[10_markdown/documents/tei-p5-title-4.12.0]] | — | ingested |
| TEI P5 4.12.0 titlePage | document | collection | [[10_markdown/documents/tei-p5-titlepage-4.12.0]] | — | ingested |
| TEI P5 4.12.0 titlePart | document | collection | [[10_markdown/documents/tei-p5-titlepart-4.12.0]] | — | ingested |
| TEI P5 4.12.0 titleStmt | document | collection | [[10_markdown/documents/tei-p5-titlestmt-4.12.0]] | — | ingested |
| TEI P5 4.12.0 tns | document | collection | [[10_markdown/documents/tei-p5-tns-4.12.0]] | — | ingested |
| TEI P5 4.12.0 trailer | document | collection | [[10_markdown/documents/tei-p5-trailer-4.12.0]] | — | ingested |
| TEI P5 4.12.0 trait | document | collection | [[10_markdown/documents/tei-p5-trait-4.12.0]] | — | ingested |
| TEI P5 4.12.0 transcriptionDesc | document | collection | [[10_markdown/documents/tei-p5-transcriptiondesc-4.12.0]] | — | ingested |
| TEI P5 4.12.0 Transcriptions of Speech | document | collection | [[10_markdown/documents/tei-p5-guidelines-ts-transcriptionsofspeech-4.12.0]] | — | ingested |
| TEI P5 4.12.0 transpose | document | collection | [[10_markdown/documents/tei-p5-transpose-4.12.0]] | — | ingested |
| TEI P5 4.12.0 tree | document | collection | [[10_markdown/documents/tei-p5-tree-4.12.0]] | — | ingested |
| TEI P5 4.12.0 triangle | document | collection | [[10_markdown/documents/tei-p5-triangle-4.12.0]] | — | ingested |
| TEI P5 4.12.0 typeDesc | document | collection | [[10_markdown/documents/tei-p5-typedesc-4.12.0]] | — | ingested |
| TEI P5 4.12.0 typeNote | document | collection | [[10_markdown/documents/tei-p5-typenote-4.12.0]] | — | ingested |
| TEI P5 4.12.0 u | document | collection | [[10_markdown/documents/tei-p5-u-4.12.0]] | — | ingested |
| TEI P5 4.12.0 unclear | document | collection | [[10_markdown/documents/tei-p5-unclear-4.12.0]] | — | ingested |
| TEI P5 4.12.0 undo | document | collection | [[10_markdown/documents/tei-p5-undo-4.12.0]] | — | ingested |
| TEI P5 4.12.0 unicodeProp | document | collection | [[10_markdown/documents/tei-p5-unicodeprop-4.12.0]] | — | ingested |
| TEI P5 4.12.0 unihanProp | document | collection | [[10_markdown/documents/tei-p5-unihanprop-4.12.0]] | — | ingested |
| TEI P5 4.12.0 unit | document | collection | [[10_markdown/documents/tei-p5-unit-4.12.0]] | — | ingested |
| TEI P5 4.12.0 unitDecl | document | collection | [[10_markdown/documents/tei-p5-unitdecl-4.12.0]] | — | ingested |
| TEI P5 4.12.0 unitDef | document | collection | [[10_markdown/documents/tei-p5-unitdef-4.12.0]] | — | ingested |
| TEI P5 4.12.0 usg | document | collection | [[10_markdown/documents/tei-p5-usg-4.12.0]] | — | ingested |
| TEI P5 4.12.0 Using the TEI | document | collection | [[10_markdown/documents/tei-p5-guidelines-use-4.12.0]] | — | ingested |
| TEI P5 4.12.0 val | document | collection | [[10_markdown/documents/tei-p5-val-4.12.0]] | — | ingested |
| TEI P5 4.12.0 valDesc | document | collection | [[10_markdown/documents/tei-p5-valdesc-4.12.0]] | — | ingested |
| TEI P5 4.12.0 valItem | document | collection | [[10_markdown/documents/tei-p5-valitem-4.12.0]] | — | ingested |
| TEI P5 4.12.0 valList | document | collection | [[10_markdown/documents/tei-p5-vallist-4.12.0]] | — | ingested |
| TEI P5 4.12.0 vAlt | document | collection | [[10_markdown/documents/tei-p5-valt-4.12.0]] | — | ingested |
| TEI P5 4.12.0 variantEncoding | document | collection | [[10_markdown/documents/tei-p5-variantencoding-4.12.0]] | — | ingested |
| TEI P5 4.12.0 vColl | document | collection | [[10_markdown/documents/tei-p5-vcoll-4.12.0]] | — | ingested |
| TEI P5 4.12.0 vDefault | document | collection | [[10_markdown/documents/tei-p5-vdefault-4.12.0]] | — | ingested |
| TEI P5 4.12.0 Verse | document | collection | [[10_markdown/documents/tei-p5-guidelines-ve-verse-4.12.0]] | — | ingested |
| TEI P5 4.12.0 view | document | collection | [[10_markdown/documents/tei-p5-view-4.12.0]] | — | ingested |
| TEI P5 4.12.0 vLabel | document | collection | [[10_markdown/documents/tei-p5-vlabel-4.12.0]] | — | ingested |
| TEI P5 4.12.0 vMerge | document | collection | [[10_markdown/documents/tei-p5-vmerge-4.12.0]] | — | ingested |
| TEI P5 4.12.0 vNot | document | collection | [[10_markdown/documents/tei-p5-vnot-4.12.0]] | — | ingested |
| TEI P5 4.12.0 vocal | document | collection | [[10_markdown/documents/tei-p5-vocal-4.12.0]] | — | ingested |
| TEI P5 4.12.0 vRange | document | collection | [[10_markdown/documents/tei-p5-vrange-4.12.0]] | — | ingested |
| TEI P5 4.12.0 w | document | collection | [[10_markdown/documents/tei-p5-w-4.12.0]] | — | ingested |
| TEI P5 4.12.0 watermark | document | collection | [[10_markdown/documents/tei-p5-watermark-4.12.0]] | — | ingested |
| TEI P5 4.12.0 when | document | collection | [[10_markdown/documents/tei-p5-when-4.12.0]] | — | ingested |
| TEI P5 4.12.0 width | document | collection | [[10_markdown/documents/tei-p5-width-4.12.0]] | — | ingested |
| TEI P5 4.12.0 wit | document | collection | [[10_markdown/documents/tei-p5-wit-4.12.0]] | — | ingested |
| TEI P5 4.12.0 witDetail | document | collection | [[10_markdown/documents/tei-p5-witdetail-4.12.0]] | — | ingested |
| TEI P5 4.12.0 witEnd | document | collection | [[10_markdown/documents/tei-p5-witend-4.12.0]] | — | ingested |
| TEI P5 4.12.0 witness | document | collection | [[10_markdown/documents/tei-p5-witness-4.12.0]] | — | ingested |
| TEI P5 4.12.0 witStart | document | collection | [[10_markdown/documents/tei-p5-witstart-4.12.0]] | — | ingested |
| TEI P5 4.12.0 writing | document | collection | [[10_markdown/documents/tei-p5-writing-4.12.0]] | — | ingested |
| TEI P5 4.12.0 xenoData | document | collection | [[10_markdown/documents/tei-p5-xenodata-4.12.0]] | — | ingested |
| TEI P5 4.12.0 xr | document | collection | [[10_markdown/documents/tei-p5-xr-4.12.0]] | — | ingested |
| TEI P5 4.12.0 zone | document | collection | [[10_markdown/documents/tei-p5-zone-4.12.0]] | — | ingested |
| timeForP6 repository README at pinned commit eb924226 | document | collection | [[10_markdown/documents/tei-time-for-p6-readme-2026-07-16]] | [[20_distillates/documents/tei-time-for-p6-readme-2026-07-16]] | distilled |
| <span>should be generalised to support discontinuous spans | publication | import | — | [[20_distillates/publications/tei-sourceforge-fr363]] | distilled |
| att.personal, att.naming, and att.canonical: Error in ODD? | publication | import | — | [[20_distillates/publications/teic-tei-issue-2739]] | distilled |
| Hierarchies within range space: From LMNL to OHCO | publication | import | — | [[20_distillates/publications/piez2014range]] | distilled |
| ogrophy elements should be in att.canonical | publication | import | — | [[20_distillates/publications/teic-tei-issue-1414]] | distilled |
| soft deprecation of @key | publication | import | — | [[20_distillates/publications/teic-tei-issue-337]] | distilled |
| There are No Documents | publication | import | — | [[20_distillates/publications/renear-wickett2010documents]] | distilled |
| Web Annotation Data Model | publication | import | — | [[20_distillates/publications/w3c-web-annotation-20170223]] | distilled |
<!-- inventory:end -->

## Chapter register

One row per chapter of the output. Writing status mirrors the chapter's frontmatter.

| Chapter | File | Status | Notes |
|---|---|---|---|
| P5 Architecture | `40_output/01-p5-architecture.md` | planned | Scope topic: P5 Architecture. |
| Abstract Model | `40_output/02-abstract-model.md` | grounded | Bounded text identity and annotation pilot; four grounded P5 statements and four explicit model posits; human acceptance pending. |
| ODD and Customization | `40_output/03-odd-and-customization.md` | planned | Scope topic: ODD and Customization. |
| Elements and Classes | `40_output/04-elements-and-classes.md` | planned | Scope topic: Elements and Classes. |
| Text and Document Structures | `40_output/05-text-and-document-structures.md` | planned | Scope topic: Text and Document Structures. |
| Annotation and Overlap | `40_output/06-annotation-and-overlap.md` | grounded | First synthesis: five grounded premises and four explicit proposed tests; source-support review and owner review remain distinct. |
| Critical Apparatus | `40_output/07-critical-apparatus.md` | planned | Scope topic: Critical Apparatus. |
| Metadata and Entities | `40_output/08-metadata-and-entities.md` | grounded | Rewritten after the second topic run on sixty-six assertions over twenty-one entity sources, three contested pairs cited on both sides; eleven explicit posits connect the findings to the record kinds of the claim pattern; human verification and encoded practice beyond the release's test document remain open. |
| History and Governance | `40_output/09-history-and-governance.md` | planned | Scope topic: History and Governance. |
| Issues and Decisions | `40_output/10-issues-and-decisions.md` | planned | Scope topic: Issues and Decisions. |
| Interoperability and Processing | `40_output/11-interoperability-and-processing.md` | planned | Scope topic: Interoperability and Processing. |
| P6 Design | `40_output/12-p6-design.md` | grounded | Bounded Abstract Text Model 0.1 proposal with nine grounded premises and thirteen explicit posits. Validated structurally on 2026-09-05. Architecture and adoption verdicts remain open. |

## Open work

<!-- Short, current list; done items are deleted, decisions go to the journal. -->

- Fetch the 368 Wayback-captured months of the Brown TEI-L archive through the
  Wayback Machine and request an export from the TEI Consortium for the 64
  months without capture.
- Take the next REST snapshot of `TEIC/TEI` under the two-stage collector so
  the recorded manifests carry no stage gap and the family can leave `partial`.
- Draw the stratified human verification sample over the two entity runs
  (twenty-one distillates, sixty-six assertions, chapter 08) and record the
  quota.
- Close the evidence gaps the second entity run left open, recorded as open
  questions of the entity topic map: the membership chain from `att.personal`
  to `att.canonical` and the travel of the class remarks stand in XML alone,
  the carriers of `cert`, `resp`, `source` and `evidence` are unnamed by the
  class specifications, no source states a rule for a co-occurring `key` and
  `ref`, and the documentation and relatability requirement is stated for
  changes of state in a person's life only; the deferred sources of the run-2
  selection (`testplace.xml`, `testnym.odd`, the CE chapter and the threads
  on `idno` and on the global responsibility attributes) are the next
  admissions of the topic.
- Reconcile the remaining Archive, SourceForge release-file and legacy
  version-control, external Council, and community-interface gaps.
- Resolve the P5 published-HTML and website-snapshot coverage exceptions before relying on their family-level `observable-complete` labels.
- Reconcile `planned`, `not_started`, and blocked acquisition language with the completion vocabulary.
- Complete three vertical production cycles before topic-scale source admission.
- Review the bounded text identity pilot using its five acceptance questions;
  record a separate accept/revise/defer decision for each item. Synthetic
  success is not proof of ontological adequacy, real-world usability, or P5
  migratability.
- Extend the three-fragment, single-diary comparison in
  `knowledge/experiments.md` with independently selected editions and
  domain reviewers. Test annotation review after actual editing and measure
  preservation, authoring, query, and teaching costs on comparable tasks.
- Review Abstract Text Model 0.1 using the five accept/revise/defer items in
  `knowledge/text-model.md`. Challenge the independently authored
  synthetic requirements with real editorial cases, including negative identity
  claims, noncontiguous structural nodes, and nontextual entities or media.
- Extend and measure the two bounded comparison implementations before ranking
  architectures. Resolve the observed page/foliation limitation through a new
  declared study, preserving the frozen holdout result; add full-document P5
  mappings, preservation/loss reports, and adoption costs.
- Extend the direct-declaration atlas with inherited/effective ODD semantics and
  source-linked prose interpretation before treating it as the formal P5 model.
- Assign the human verification role before any artifact can enter `verified` status.
