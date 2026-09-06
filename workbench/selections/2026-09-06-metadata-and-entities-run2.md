# Selection record, Metadata and Entities run 2

This record holds the selection of run 2 of the topic Metadata and Entities,
made on 2026-09-06 under the selection procedure in
[the plan](../../knowledge/plan.md), which carries the evidence questions of
the run and the state it reached. The tables are records and navigation
aids, never sources or grounding targets, and their counts hold for the
manifests, the lock and the pinned commit named below.

Snapshot of 2026-09-06. The atlas is the projection of commit
`113e933e21f016e2655518321e9d10214b8d9fcb`, the GitHub stream is the run
`sources/manifests/2026-09-06-github-teic-tei-work-items.yaml`, the
SourceForge stream the run `sources/manifests/2026-09-06-tei-legacy-sourceforge-r4.yaml`,
the TEI-L stream the run `sources/manifests/2026-09-06-tei-l-psu.yaml`, and
the literature seeds the lock `sources/locks/literature.yaml` with the
pinned bibliography.

| Family | Declared query | Hits |
|---|---|---|
| atlas, membership | `classes_declared` names `att.naming` | 31 records, among them `att.personal`, `rs`, `geogName`, `country`, `settlement`, `region`, `district`, `bloc`, `state`, `trait`, `event`, `birth`, `death`, `author`, `editor` |
| atlas, membership | `att.canonical` | 31 records, among them `att.naming`, `relation`, `faith`, `object`, `date`, `title`, `bibl`, `author`, `term` |
| atlas, membership | `att.datable` | 74 records, among them `place`, `org`, `person`, `state`, `trait`, `event`, `idno`, `persName`, `placeName`, `name` |
| atlas, membership | `att.editLike` | 53 records, among them `persName`, `name`, `placeName`, `orgName`, `place`, `org`, `person`, `state`, `trait`, `event` |
| atlas, attribute | records declaring `key` | 10, `att.canonical` and nine ODD reference elements |
| atlas, attribute | `ref` | 3, `att.canonical`, `dataRef`, `g` |
| atlas, attribute | `nymRef` | 1, `att.naming` |
| atlas, attribute | `role` | 7, `att.naming`, `person`, `org`, `personGrp`, `persona`, `address`, `att.tableDecoration` |
| atlas, attribute | `cert`, `resp`, `evidence`, `source` | 2, 2, 2, 1; `cert` and `resp` in `att.global.responsibility`, `evidence` in `att.editLike`, `source` in `att.global.source`, all three classes reached through `att.global` |
| atlas, ident | `att.personal`, `att.global.responsibility`, `att.editLike`, `att.global.source`, `att.datable`, `att.datable.w3c`, `idno`, `place`, `org`, `trait`, `state`, `event`, `placeName`, `orgName` | 14, all present; `persName`, `placeName`, `orgName`, `name` and the name components declare `att.personal` and reach `att.naming` and `att.canonical` through it |
| chapters | `CE-CertaintyResponsibility.xml`, `HD-Header.xml`, `CO-CoreElements.xml` | 3 files |
| tests | `P5/Test/testnames.xml`, `names-demo-en.xml`, `testplace.xml`, `testnym.odd` | 4 files |
| GitHub, A1 | `att\.canonical\|att\.naming\|nymRef` | 19 |
| GitHub, A2 | `persName\|placeName\|orgName\|\brs\b\|geogName\|roleName\|surname\|forename\|addName\|genName\|nameLink\|<name>\|name element\|@type on name` | 24 |
| GitHub, A3 | `\bkey\b\|@ref\b` | 20 |
| GitHub, A4 | `prosopograph\|personograph\|listPerson\|listPlace\|listOrg\|<person>\|<place>\|<org>\|\bpersona\b\|personGrp\|\bidno\b\|linked data\|authority file\|\bURIs?\b` | 62 |
| GitHub, A5 | `\btrait\b\|\bstate\b\|\bevent\b\|\brelation\b\|listRelation\|\bnym\b\|listNym\|@cert\|@resp\|@evidence\|@source\|att\.datable\|att\.editLike\|att\.global\.responsibility\|responsibility` | 88 |
| GitHub, label | `Status: Reconsider for P6` | 17 |
| SourceForge, A1 to A5 | the same expressions on `summary` | 10, 12, 9, 34, 50; every hit maps to a GitHub record of the same title and date except support request 4 |
| TEI-L | `persName\|persongrp\|surname\|placeName\|orgName\|\bname\b\|\bidno\b\|traits of places\|authority\|prosopograph\|linked\|author` on `subject` | 9 threads, 38 messages, months 2512 to 2608 |
| literature | lock records; bibliography prefix `ND-`; title terms `name\|prosopograph\|onomast\|authority\|person\|place\|linked data\|entity\|identif` | 4 lock records, none on the topic; 1 entry with the prefix; 3 title hits |

The selection. A SourceForge original is named in the row of its GitHub
record with its status.

| Source | Family | Exact query or ident | Disposition | Reason |
|---|---|---|---|---|
| `P5/Source/Specs/att.personal.xml` | P5 specification | ident `att.personal`; declares `att.naming`; declared by `persName`, `placeName`, `orgName`, `name`, `objectName`, `surname`, `forename`, `addName`, `genName`, `roleName` | admit | Q1, the class through which the naming elements reach `att.naming` and `att.canonical`; `persName` and `placeName` declare neither class directly |
| `P5/Source/Specs/att.global.responsibility.xml` | P5 specification | ident; attribute lookup `cert`, `resp`; reached through `att.global` | admit, C | Q6, `cert` and `resp` are global at the pinned release, so every naming element carries them; this is the counterevidence query for the claim that identification names no agent or certainty |
| `P5/Source/Specs/att.global.source.xml` | P5 specification | ident; attribute lookup `source`; reached through `att.global` | admit, C | Q6, a source pointer is global at the pinned release |
| `P5/Source/Specs/att.editLike.xml` | P5 specification | ident; attributes `evidence`, `instant`; declared by the naming elements and the records | admit | Q5 and Q6, the class that carries `evidence` and `instant` to names and records |
| `P5/Source/Specs/att.datable.xml` | P5 specification | ident; attribute `period`; pulls `att.datable.w3c`, `att.datable.iso`, `att.datable.custom`; declared by `place`, `org`, `state`, `trait`, `event`, `idno` | admit, C | Q5, the time frame for statements about places and organizations; `place` and `org` are members at the pinned release, which answers the reading that the requirement holds for them |
| `P5/Source/Specs/idno.xml` | P5 specification | ident; declares `model.personPart`, `model.nameLike`, `att.datable`, `att.typed`, `att.sortable` | admit | Q4 and Q7, the specification's own statement of purpose and its availability inside `person` |
| `P5/Source/Specs/place.xml` | P5 specification | ident; declares `att.datable`, `att.editLike`, `att.sortable`, `att.typed`, `model.placeLike` | admit | Q3, the place record's description and remarks |
| `P5/Source/Specs/state.xml` | P5 specification | ident; declares `att.naming`, `att.datable`, `att.editLike`, `model.persStateLike`, `model.orgStateLike`, `model.placeStateLike` | admit | Q5 and Q7, a statement element that is itself a member of `att.naming`, so `key`, `ref` and `role` recur inside statements about persons, organizations and places |
| `P5/Test/testnames.xml` | encoded practice | file name; counts at the pinned commit `persName` 165, `placeName` 139, `person` 137, `key` 144, `role` 117, `ref` 11, `nym` 11 | admit | Q2, the release's own test document identifies mentions by `key`, places roles on mentions and uses nyms; rights follow the release with the per-file review recorded in the manifest |
| GitHub issue 337 (SourceForge feature request 336, `closed`) | work item | A3; created 2011-11-13, closed 2015-10-02, 21 comments, `Type: FeatureRequest`, `Status: Go`, `sf-automigrated` | admit, C | Q8, the thread that proposed a soft deprecation of `key` in favour of `ref`; `key` is still declared on `att.canonical` at the pinned release, so the released effect is at most the remarks text the chapter grounds in, which the thread has to establish |
| GitHub issue 2739 | work item | A1; created 2025-08-04, closed 2025-08-06, 4 comments | admit | Q1, reports an ODD error in the chain `att.personal`, `att.naming`, `att.canonical` before the pinned release; its outcome is checked against the admitted class blobs |
| GitHub issue 1414 | work item | A1; created 2015-12-15, closed 2019-07-15, 16 comments, `Type: FeatureRequest`, `Status: Go`, `TEI: Schema` | admit, C | Q7, the proposal to put the record elements themselves into `att.canonical`; at the pinned release `object` is a member and `person`, `place` and `org` are not, so the trail from proposal to released effect tests the claim that records link outward through `idno` only |
| `org.xml`, `trait.xml`, `event.xml`, `placeName.xml`, `orgName.xml`, `att.datable.w3c.xml` | P5 specification | ident | defer, budget | Q3 and Q5 in the next run; `place` and `state` stand for the record and the statement kinds in this run |
| `P5/Test/testplace.xml` (`placeName` 70, `place` 34, `ref` 12, `key` 9, `cert` 2, `resp` 2), `names-demo-en.xml` (`role` 117, `key` 1), `testnym.odd` (`nym` 15, `nymRef` 3) | encoded practice | file name and counts | defer, budget | `testplace.xml` in the next run for Q3 and Q6, records with `cert` and `resp`; `testnym.odd` for the nym question |
| `CE-CertaintyResponsibility.xml`, `HD-Header.xml`, `CO-CoreElements.xml` | chapter | file | defer, budget | CE for Q6 in the next run; HD and CO exceed the chapter budget beside CE and are entered through their specifications first |
| GitHub 290 (SourceForge feature request 289, `open-accepted`) | work item | A1; closed 2016-09-26, 12 comments, `Status: Blocked` | defer, budget, C | Q7, the proposal to give the trait and state elements `att.canonical`; at the pinned release `trait` and `state` are members of `att.naming`, so the effect exists and its trail is the next run's |
| GitHub 338 (SourceForge feature request 337, `closed-accepted`), 462 (feature request 462, `closed-fixed`), 158, 219, 698, 1424, 1442, 1480, 1481, 1685, 2071, pull request 2630 | work item | A4 | defer, budget, C for 338 | Q4, `idno` as the external reference of a record; the specification is admitted first and the threads follow |
| GitHub 444 (SourceForge feature request 443, `closed-fixed`), 536 (feature request 536), 465, 490, 509 (feature request 509, `closed-fixed`), 166, 191, 196, 240, 560, 681, 766, 1003, 1204, 1242, pull request 1352, 1368, 1631, 1668, 2158 | work item | A5, A2 | defer, budget, C for 444, 536 and 509 | Q6, the threads that made `resp`, `cert` and `source` global and allowed `cert` on `rs`; the admitted classes carry the released state, the trails follow |
| GitHub 367 (SourceForge feature request 366, `open`) | work item | label; closed 2025-09-14, 27 comments, `Status: Reconsider for P6` | defer, budget | Q3, the official process's own reconsideration of the content models of `org`, `place` and `person`; first thread of the next run |
| GitHub 843 (SourceForge bug 168), 1041, 1248, 1340, 518, 519, 1310, 616, 1723, 1756, 2382, pull request 2427, 2466, pull request 2483, 2499, 2523, 2524, 2699, 2827, pull request 2882 | work item | A5, A2, A4 | defer, budget, C for 843 | Q5, `trait`, `state` and `event` and their datability; the thread on state against trait is the counterevidence query for the extension of the requirement |
| GitHub 504 (SourceForge feature request 504, `closed-wont-fix`), 467, 495, 567, 640, 1183, 1262, 1314, 1552 | work item | A5 | defer, budget, C for 504 | the relation participants; the declined proposal to replace `active` and `passive` by `from` and `to` is the counterevidence query for the contested participant pair |
| GitHub 2451 with pull request 2881, 2389 with pull request 2952, 88, 210, 298, 299, 513, 608, 909, 1042, 1241, 1244, 1410, 1689, 1986, 1992, 2045, 2257, 2432, 2887 | work item | A5, A2 | defer, budget, C for 2451 | the class scope of `att.datable` and `att.editLike`; 2881 merged on 2026-05-04 gives `place` and `org` the class at the pinned release, 2952 merged on 2026-08-18 after the release, so `rs` is datable on the development branch only |
| GitHub 58 (SourceForge feature request 57), 125 (feature request 124), 1035 (bug 391, `closed-accepted`), 238 (feature request 245, `closed-accepted`), 623 (bug 27, `closed-accepted`), 781, 1531, 1684, 1695 | work item | A2, A1 | defer, budget, C for 1035 and 623 | Q1 and Q2, `role` and `type` on mentions, and the deliberate exclusion of `nameLink` from `key` and `ref` |
| GitHub 129, 130, 131, 146, 187, 206, 246, 625, 1521, 1525, 1659, 1775, 1821, 2392 with pull request 2655, 2687 | work item | A1, A3 | defer, budget | the growth of `att.canonical` and `att.naming` beyond names, to `author`, `title`, `editor`, `term`, `faith`, `actor`, `publisher`, `bibl`, `material` and `date`; which representations carry identification |
| GitHub 2, 69, 73, 183, 321, 322, 498, 627, 635, 638, 794, 1128, 1772, pull request 1974, 2011, 2016, 2180, 2296, 2475, 2595, 2651, 2745, 2890 with pull request 2891 | work item | A4 | defer, budget | the record elements, their lists and their roles; 2 is the origin of the module for the history topic, 2745 and 498 are leads on the identity of a person against a persona |
| GitHub 535 (SourceForge feature request 535, `closed-fixed`), 474, 1334 | work item | A3 | defer, lead | the Guidelines' own move of examples from `key` to `ref` |
| GitHub 696 (SourceForge bug 110, `closed-fixed`), 2150 | work item | A1, A5 | defer, lead | the description of `nymRef` and the definition of `listNym` as standardized, the latter open |
| GitHub 1400, 1508 | work item | label | defer, another topic's run | structure, see run 1 of Text and Document Structures below |
| GitHub 2843, 2893, 2894, 2957 | work item | label | defer, another topic's run | the class system and attribute naming for P6, for Elements and Classes and P6 Design |
| GitHub 1175, 1744, 1923, 2000, 2013, 2090, 2146, 2373, 2744, 2875 | work item | label | defer, another topic's run | ODD, apparatus, header and documentation topics |
| TEI-L threads persName or personGrp (8 messages, month 2607), surname (4, 2607), traits of places, persons, etc. in a linked fashion (1, 2512) | TEI-L | subject query | defer, prerequisite missing | bodies in the raw store only, no rights review, Penn State months only; the traits thread is a lead for Q6 |
| bibliography entry `github-mix-mix` | literature | title terms | defer, prerequisite missing | a project personography, a lead for encoded practice that needs the sampling protocol |
| GitHub 2738 | work item | A1 | reject, typography | a typo |
| GitHub 405, 485, 609, 1597, 1623, 1656, 1692, 1842, 2297 | work item | A2 | reject, outside the topic or example repair | whitespace, content models of other elements, schema tooling, example quality |
| GitHub 867, 903, 953, 1606, 1724, pull request 1742, pull request 1817, 2062, 2726, 2850, pull request 2852 | work item | A3 | reject, homonym | `key` of ODD references and datatypes |
| GitHub 68, 116, 217, 310, 339, 344, 348, 376, 385, 440, 1088, 1294, pull request 1443, 1989, 2198, 2345 | work item | A4 | reject, outside the topic | bibliographic and manuscript identifiers |
| GitHub 847, 959, 1232, 1446, 1592 | work item | A4 | reject, homonym | URI as namespace or stylesheet matter |
| GitHub 316, 424, 432, 745, 782, 883, 950, 961, 963, 1111, 1127, 1463, 1593, 1604, 1649, 1916, 2588, 2591, pull request 2692 | work item | A5 | reject, homonym | `state`, `source`, `relation`, `event` and `nym` in other senses, and the technical limit on nym parts |
| SourceForge support request 4 | ticket | A4 | reject, outside the topic | a support question of 2004 without a proposal |
| TEI-L threads idno for TEI (9 and 3 messages, 2602), author for AI-generated texts (7, 3 and 1, 2605), different shares of authorship (2, 2608) | TEI-L | subject query | reject, outside the topic | header identifiers and statements of responsibility |
| bibliography entries `ND-eg-99`, `fr-ex-Corneille_Place-Royale`, `DS-eg-05` | literature | prefix and title terms | reject, homonym | example sources of the Guidelines without a claim about the topic |
| lock records | literature | lock | no hit | the four records of wave one concern annotation and identity; the Journal of the TEI and Zotero seeds remain the recorded gap |

Run 2 admits twelve sources, no chapter among them and three threads. They
are `att.personal.xml`, `att.global.responsibility.xml`, `att.global.source.xml`,
`att.editLike.xml`, `att.datable.xml`, `idno.xml`, `place.xml`, `state.xml`,
`P5/Test/testnames.xml`, GitHub issues 337, 2739 and 1414. The raw snapshots
of the three threads are present in the checkout of 2026-09-06; the raw
responses of the SourceForge originals are not, which is why the GitHub
records are the admitted manifestations.
