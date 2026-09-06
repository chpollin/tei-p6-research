# Selection record, Text and Document Structures run 1

This record holds the selection of run 1 of the topic Text and Document
Structures, made on 2026-09-06 under the selection procedure in
[the plan](../../knowledge/plan.md), which carries the evidence questions of
the run. The tables are records and navigation aids, never sources or
grounding targets, and their counts hold for the manifests, the lock and the
pinned commit named below.

Snapshot of 2026-09-06 over the same manifests, atlas and lock as
[run 2 of Metadata and Entities](2026-09-06-metadata-and-entities-run2.md).

| Family | Declared query | Hits |
|---|---|---|
| atlas, membership | `att.fragmentable` | 6, `ab`, `l`, `p`, `post`, `att.divLike`, `att.segLike` |
| atlas, membership | `att.breaking` | 5, `cb`, `gb`, `lb`, `milestone`, `pb` |
| atlas, membership | `att.divLike` | 10, `div`, `div1` to `div7`, `lg`, `spGrp` |
| atlas, membership | `att.spanning` | 14, among them `pb`, `lb`, `cb`, `gb`, `milestone`, `addSpan`, `delSpan`, `metamark` |
| atlas, membership | `att.placement` | 17, among them `div`, `note`, `head`, `fw`, `figure`, `att.transcriptional` |
| atlas, membership | `att.written` | 29, among them `div`, `p`, `ab`, `head`, `note`, `line`, `zone`, `text` |
| atlas, attribute | `part`, `break`, `facs`, `next`, `prev`, `spanTo`, `place` | 1 each, in `att.fragmentable`, `att.breaking`, `att.global.facs`, `att.global.linking` for both `next` and `prev`, `att.spanning`, `att.placement` |
| atlas, attribute | `target` | 13, among them `att.pointing`, `annotation`, `alt`, `metamark`, `change` |
| atlas, ident | `div`, `p`, `ab`, `seg`, `head`, `note`, `pb`, `lb`, `milestone`, `fw`, `join`, `att.fragmentable`, `att.breaking`, `att.global.linking`, `att.global.facs`, `text`, `body`, `floatingText`, `sourceDoc`, `surface`, `zone`, `line`, `facsimile` | 23, all present; `ab` has the content `macro.abContent`, `facsimile` admits a nested `facsimile` |
| chapters | `NH-Non-hierarchical.xml`, `DS-DefaultTextStructure.xml`, `SA-LinkingSegmentationAlignment.xml`, `PH-PrimarySources.xml`, `CO-CoreElements.xml` | 5 files |
| tests | `P5/Test/testoverlap.xml`, `testfrag.xml`, `testtranscr.xml`, `testtranscr2.xml`, `testtranscr4.xml`, `torture.xml` | 6 files; `testoverlap.xml` holds `p` 9 and `pb` 4 |
| GitHub, B1 | `overlap\|hierarch\|concurrent\|OHCO` | 5 |
| GitHub, B2 | `milestone\|\bpb\b\|\blb\b\|\bcb\b\|\bgb\b\|page ?break\|line ?break\|column ?break\|\bfw\b\|foliation\|att\.breaking\|@break` | 29 |
| GitHub, B3 | `fragmentable\|@part\b\|\bjoin\b\|joinGrp\|discontinu\|@next\|@prev\|aggregat` | 8 |
| GitHub, B4 | `stand-?off\|listAnnotation\|\bannotation\b\|\bspan\b\|spanGrp\|\banchor\b\|att\.spanning\|spanTo\|xpointer\|@target` | 48 |
| GitHub, B5 | `floatingText\|sourceDoc\|\bzone\b\|\bsurface\b\|<line>\|facsimile\|@facs\|embedded transcription\|documentary\|genetic` | 46 |
| GitHub, B6 | `<div>\|<ab>\|<seg>\|<p>\|<head>\|<body>\|<text>\|<group>\|<front>\|<back>\|<note>\|att\.divLike\|content model of div\|\bstructures?\b` | 50 |
| GitHub, label | `Status: Reconsider for P6` | 17, dispositions in run 2 except 1400 and 1508 |
| SourceForge, B1 to B6 | the same expressions on `summary` | 3, 19, 3, 19, 20, 27; every hit maps to a GitHub record of the same title and date |
| TEI-L | `overlap\|hierarch\|structure\|page\|milestone\|stand-?off\|interlinear\|support\|\bdiv\b\|\bp\b\|\bseg\b\|\bnote\b\|facsimile\|zone\|surface\|dictionary-entries\|damage` on `subject` | 8 threads, 55 messages, months 2512 to 2608 |
| literature | lock records; bibliography prefixes `NH-`, `DS-`, `SA-`, `PH-`, `AI-`; title terms `overlap\|hierarch\|structure\|stand-?off\|markup\|OHCO\|document\|milestone\|LMNL\|annotation` | 3 admitted and 1 unavailable lock record; 10, 6, 5, 20 and 7 prefixed entries; 15 title hits |

The selection.

| Source | Family | Exact query or ident | Disposition | Reason |
|---|---|---|---|---|
| `P5/Source/Guidelines/en/NH-Non-hierarchical.xml` | chapter | file at the pinned commit | admit, C | Q1, P5's own account of the problem and of its strategies, boundary marking, fragmentation with reconstitution and stand-off; the chapter names the cases the readings posit asks for and is the counterevidence query for the claim that P5 has only the tree |
| `P5/Source/Guidelines/en/DS-DefaultTextStructure.xml` | chapter | file at the pinned commit | admit | Q2 and Q3, divisions numbered and unnumbered, prose and anonymous blocks, heads, floating texts, front and back |
| `P5/Source/Specs/att.fragmentable.xml` | P5 specification | ident; attribute lookup `part`; declared by `ab`, `l`, `p`, `post`, `att.divLike`, `att.segLike` | admit, C | Q1, the declared way to mark a fragment of a virtual element; `p` is a member at the pinned release, the released effect of issue 399 |
| `P5/Source/Specs/join.xml` | P5 specification | ident; attributes `result`, `scope`; declares `att.pointing`, `model.global.meta` | admit | Q1, the reconstitution of a virtual element from fragments |
| `P5/Source/Specs/att.global.linking.xml` | P5 specification | ident; attributes `corresp`, `synch`, `sameAs`, `copyOf`, `next`, `prev`, `exclude`, `select`; reached by every element through `att.global` | admit | Q1, `next` and `prev` as the aggregation attributes and `exclude` and `select` as alternation |
| `P5/Source/Specs/milestone.xml` | P5 specification | ident; declares `att.breaking`, `att.spanning`, `att.milestoneUnit`, `att.edition`, `model.milestoneLike` | admit | Q1 and Q4, boundary marking by an empty element, with `spanTo` as the bridge to a range |
| `P5/Source/Specs/pb.xml` | P5 specification | ident; declares `att.breaking`, `att.spanning`, `att.edition`, `model.milestoneLike` | admit, C | Q4, the page beginning of the holdout case; `facs` reaches it through `att.global` |
| `P5/Source/Specs/div.xml` | P5 specification | ident; declares `att.divLike`, `att.placement`, `att.written`, `att.declaring`, `model.divLike`; two constraints | admit | Q3, the structural division and its containment constraints; `att.divLike` brings `part` |
| `P5/Source/Specs/note.xml` | P5 specification | ident; declares `att.placement`, `att.anchoring`, `att.pointing`, `att.written`, `model.noteLike` | admit | Q2, where a note stands relative to the text, through `place`, anchoring and `targetEnd`, for the reading projection |
| `P5/Test/testoverlap.xml` | encoded practice | file name; counts `p` 9, `pb` 4 | admit | Q1 and Q4, the release's own test of paragraphs crossed by page beginnings |
| GitHub issue 1505 | work item | B3; created 2016-09-22, closed 2017-05-03, 14 comments, `Type: Bug`, `Status: Go`, `TEI: Guidelines & Documentation`, `TEI: Schema` | admit, C | Q1, the clarification of `next` and `prev` against `join` with `scope`, `result` and `exclude`; its released effect is read in the admitted specifications and in the NH chapter |
| GitHub issue 1400 | work item | label; created 2015-11-10, open, 20 comments, `Type: FeatureRequest`, `Status: Reconsider for P6` | admit | Q3 and Q6, the official process's own reconsideration of numbered divisions |
| `att.spanning.xml`, `att.breaking.xml`, `att.divLike.xml`, `att.placement.xml`, `seg.xml`, `p.xml`, `ab.xml`, `head.xml`, `floatingText.xml`, `text.xml`, `body.xml`, `fw.xml`, `att.global.facs.xml` | P5 specification | ident | defer, budget | Q2, Q3 and Q4 in the next run; `milestone` and `pb` carry the breaking and spanning classes into this run through membership |
| `sourceDoc.xml`, `surface.xml`, `zone.xml`, `line.xml`, `facsimile.xml` with `PH-PrimarySources.xml` | P5 specification and chapter | ident, file | defer, budget | the documentary view and the carrier, a run of their own because PH exceeds the chapter budget beside NH and DS |
| `SA-LinkingSegmentationAlignment.xml`, `CO-CoreElements.xml` | chapter | file | defer, budget | SA holds the aggregation and segmentation prose the specifications point to, CO the milestone prose; both are entered through their specifications in this run |
| `P5/Test/testfrag.xml`, `testtranscr.xml`, `testtranscr2.xml`, `testtranscr4.xml`, `torture.xml` | encoded practice | file name | defer, lead | the file names suggest fragmentation and transcription tests; their counts are taken in the next run |
| GitHub 1856 | work item | B6; created 2019-02-18, closed 2022-10-20, 59 comments | defer, budget, C | Q3, whether `ab` may nest; at the pinned release the content of `ab` is `macro.abContent`, where the outcome is read |
| GitHub 399 (SourceForge feature request 397, `closed-accepted`), 1227, 1750, 2756 | work item | B3 | defer, budget, C for 399 | `part` on `p` and other components, released; `q` as fragmentable still open in 2025 |
| GitHub 2367 with pull request 2633 (merged 2025-01-14), 641 (SourceForge bug 40), 678 (bug 78), 760 (bug 87), 1156 (bug 519), 1529, 269 (feature request 268, `closed-fixed`), 200 (feature request 199), 325 (feature request 324, closed 2025-09-14), 108 (feature request 107), 128, 164, 190, 266, 707, 879, 1660, 1677 | work item | B2 | defer, budget, C for 2367, 760 and 641 | Q4, the typographic line beginning against the topographic line, the consistency of `pb`, `lb`, `cb` and `gb`, foliation and `facs` on `pb`; 1660 declined the renaming of `lb` |
| GitHub 34 (SourceForge feature request 33), 253, 166, 681, 335, 391, 394, 479, 1466, 2551, 435, 452, 701, 1051, 1169, 1939, 2089, 2460, 2711, 1957 with pull request 1983 | work item | B6 | defer, budget, C for 2551 | Q2 and Q3, the placement of notes and heads and the content models of divisions, front and back; `div` is a member of `att.placement` at the pinned release, the released effect of 2551 |
| GitHub 64 (SourceForge feature request 63), 261 (feature request 260, `closed-accepted`), 264 (feature request 261, `closed-later`), 1578, 2607 | work item | B5, B6 | defer, lead | the floating embedded text, from its origin to a report that names an abstract model violation |
| GitHub 258 (SourceForge feature request 257, `closed-accepted`), 259, 98, 113, 204, 213, 278, 456, 515, 541, 1453, 1493, 1508, 1515, 1838, 2148, 2300 with pull request 2360, 2363, pull request 2449, 2476, 2565 with pull request 2654, 2737 | work item | B5 | defer, budget | the documentary run of the topic; the genetic origin of `sourceDoc`, `surface`, `zone` and `line`, the restriction of embedded transcription, the coordinate system and the nesting of `facsimile`; 1508 carries the P6 label |
| GitHub 1691 | work item | B1 | defer, lead | `said` and `q` in the context of overlapping hierarchies, open |
| GitHub 374 (SourceForge feature request 378, `open`), 61 comments, with pull request 2018 (merged 2020-08-17), 51, 168 (feature request 167), 197, 208, 279, 355 (feature request 354), 389, 1049, 1186, 1624, 1626, 1658, pull request 1665, 1666, 1676, 1745, 1779, 1976, 1977, 2048, 2246 with pull request 2662, 2436 with pull request 2555, pull request 2448, 2474, 2530, pull request 2767, 2941 | work item | B4 | defer, another topic's run | Q5, the stand-off and range mechanisms belong to the run of Annotation and Overlap, which starts from 374 and 2018; 1049 and 2767 were declined |
| GitHub 364 (SourceForge feature request 363) | work item | B3, B4 | already admitted | the migrated copy of the feature request admitted in wave one as `tei-sourceforge-fr363` |
| GitHub 503, 1552 | work item | B6 | defer, another topic's run | the content models of `person` and the placement of `listRelation`, for run 2 of Metadata and Entities |
| GitHub 1312 | work item | B6 | defer, another topic's run | conformance wording that singles out `text`, for P5 Architecture |
| TEI-L threads interlinear variation (8 messages, month 2512), tei structure question (7, 2512), different page sizes but one support element (9, 2608) | TEI-L | subject query | defer, prerequisite missing | bodies in the raw store only, no rights review, Penn State months only; leads for Q1, Q3 and Q4 |
| bibliography entries `NH-BIBL-1`, `NH-BIBL-3`, `NH-BIBL-4`, `NH-BIBL-5`, `NH-BIBL-6`, `NH-BIBL-7`, `NH-BIBL-8` | literature | prefix `NH-` | defer, prerequisite missing | the literature the NH chapter cites on overlap, concurrent markup and layered markup; enters through the literature protocol with per-item rights, the review article first |
| GitHub 470, 629 (SourceForge bug 33), 1139, 1876 | work item | B1 | reject, homonym or typography | overlap of attribute classes, and a typo in the multiple-hierarchy examples |
| GitHub 10, 301, 450, 2164, 874, 1222, 1432, 1995, 2241 with pull request 2288 | work item | B2 | reject, outside the topic or tooling and typography | witnesses, dictionaries and geographic features, a stylesheet defect, translations, a typo and release milestones |
| GitHub 1382, 1919 | work item | B3 | reject, typography or outside the topic | markup of a mention and the content of `joinGrp` |
| GitHub 104, 178, 222, 919, 1106, 1118, 1205, 1211, 1367, 1383, 1469, 1620, pull request 1732, 1852, 2145, 2883 | work item | B4 | reject, outside the topic or tooling and typography | `target` on manuscript, bibliographic and apparatus elements, stylesheet defects and example repairs |
| GitHub 177, 729, 741, 758, 1047, 1206, 1363, 1364, 1758, 1767, pull request 2039, 2043, 2414, 2637, 2747 | work item | B5 | reject, outside the topic or tooling and typography | audio facsimile, stylesheet defects, wording, translations, build tooling and example requests |
| GitHub 548, 571, 572, 770, 956, 1108, 1151, 1164, 1207, 1514, 1542, 1641, pull request 1701, 1967, 2147, 2149, pull request 2151, 2719, pull request 2731, 2889 | work item | B6 | reject, outside the topic or tooling and typography | the header, verse and manuscript description, linguistic markup, ODD, stylesheets and example repairs |
| TEI-L threads att.typed and the p element (19 and 2 messages, 2512), nested dictionary-entries (4, 2512), question about the use of damage (2, 2512), describing menu structures in TEI (4, 2601) | TEI-L | subject query | reject, outside the topic | attribute classes, dictionaries, transcription phenomena and a modelling question without structure content |
| bibliography entries with `-eg-` and `-ib` in their identifier under the five prefixes, `SA-BIBL-2`, `PH-BIBL-1`, `AI-BIBL-1` to `AI-BIBL-7` | literature | prefixes and title terms | reject, homonym or outside the topic | example sources and editions the Guidelines cite for illustration, and corpus linguistics |
| lock records `piez2014range`, `w3c-web-annotation-20170223`, `renear-wickett2010documents` | literature | lock | already admitted | wave one; `renear-mylonas-durand-ohco-author1993` stays unavailable |

Run 1 admits twelve sources, two chapters and two threads among them. They
are `NH-Non-hierarchical.xml`, `DS-DefaultTextStructure.xml`,
`att.fragmentable.xml`, `join.xml`, `att.global.linking.xml`,
`milestone.xml`, `pb.xml`, `div.xml`, `note.xml`, `P5/Test/testoverlap.xml`,
GitHub issues 1505 and 1400. The raw snapshots of both threads are present
in the checkout of 2026-09-06.
