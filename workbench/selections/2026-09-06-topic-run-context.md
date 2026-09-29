# Topic-run context of 2026-09-06

Am 2026-09-11 verlustfrei aus `knowledge/plan.md` übernommen. Die folgenden Fragen und Auswahlbegründungen dokumentieren die damalige Planung. Die ursprünglichen Auswahlrecords bleiben unverändert. Der aktuelle Bearbeitungsstand steht in `knowledge/state.md`, die gültige Auswahlprozedur in `knowledge/operations.md` unter Select.

### Run 2 of Metadata and Entities

The entity run left three gaps in [[knowledge/state]]. Class membership
stands only in XML, no admitted source is encoded practice, and no source
states what applies when a local key and a URI are both available. The
second run of the topic closes them. Its questions come from the posits of
`40_output/08-metadata-and-entities.md` and from Open work.

| Question | Kind | Origin |
|---|---|---|
| Q1. Which class specifications carry `key`, `ref`, `nymRef` and `role` to the naming elements, through which chain, and do their remarks travel with the attributes? | coverage | posits boundary and inheritance; Open work |
| Q2. Which encoded practice at the pinned release places the kind of referent or a role on a mention, and identifies mentions by `key`, by `ref` or by both? | coverage | posits mention and alignment; Open work |
| Q3. Where do the sources state the separation of record and reference for person and place records, and how do records point outward? | coverage | posit separation |
| Q4. What purpose does the specification of `idno` state, and does encoded practice carry external references through it? | coverage | posit idnoread |
| Q5. Which sources state the time frame, documentation and relatability requirement for traits, states, places and organizations? | coverage | posit extension |
| Q6. Do the sources give the act of identifying an agent, a date, a certainty or a source pointer? | problem claim, identification names no agent, date or certainty | posit denotation |
| Q7. Do the records themselves carry identification, or only their names? | problem claim, the record links outward through `idno` and the mention through `key` and `ref` | posits separation and alignment |
| Q8. What applies when a local key and a URI are both available? | problem claim, no precedence when `key` and `ref` co-occur | Open work; assertion `p5-att-canonical-gives-no-precedence-when-key-and-ref-co-occur` |

The streams queried on 2026-09-06, the declared query of every family with
its hit count and the disposition of every hit stand in the
[selection record](../workbench/selections/2026-09-06-metadata-and-entities-run2.md).

Run 2 admits twelve sources, no chapter among them and three threads. They
are `att.personal.xml`, `att.global.responsibility.xml`, `att.global.source.xml`,
`att.editLike.xml`, `att.datable.xml`, `idno.xml`, `place.xml`, `state.xml`,
`P5/Test/testnames.xml`, GitHub issues 337, 2739 and 1414. The raw snapshots
of the three threads are present in the checkout of 2026-09-06; the raw
responses of the SourceForge originals are not, which is why the GitHub
records are the admitted manifestations.

The run was executed on 2026-09-06 through admission, distillation, three
rounds of source review, assertion building with a fresh-context review and
the rewrite of chapter 08; [[knowledge/state]] holds its counts and
[[knowledge/journal]] its outcomes, and the questions it left open stand in
the entity topic map. The human verification sample over both entity runs
remains an operator decision.

### Run 1 of Text and Document Structures

The second topic is Text and Document Structures. At selection time, in the order of the posits
of chapter 12, the first open evidence questions that no admitted source
addresses are those of the projection posit, the objects posit and the
readings posit, and all three ask how P5 encodes structure, the reading of
a main text apart from its notes, distinct roles over the same characters and
a containment model for crossing or noncontiguous structures. The selection
posit, whose question the topic Annotation and Overlap serves, comes later in
that order and already rests on three admitted specifications, three
admitted publications and the grounded chapter
`40_output/06-annotation-and-overlap.md`. At that selection boundary the structure topic had no admitted
P5 specification, its map held two diary assertions, and the single
recorded failure of the candidate, the refused page and foliation holdout in
[[knowledge/experiments]], is a structure phenomenon. Overlap is the bridge
between the two topics, and the run admits P5's own chapter on it; the
stand-off mechanisms are deferred to the annotation run.

| Question | Kind | Origin |
|---|---|---|
| Q1. Which cases require noncontiguous nodes, shared occurrences or another containment model, and how does P5 itself account for structures that cross the tree? | problem claim, a forest of contiguous extents is the first account of structure while P5 has only the tree and its workarounds | posit readings; map question on coupled concepts |
| Q2. Which constructs place a note or an embedded text relative to the main text, so that a reading projection can be checked against them? | coverage | posit projection |
| Q3. Which structural elements keep distinct roles over the same characters, and which content models decide what may contain what? | coverage | posit objects; map question |
| Q4. How does P5 record a page beginning, a folio number and a facsimile pointer, and what does it say about their alignment? | problem claim, the page and foliation distinction is spread over constructs the candidate refused | posit evaluation; Open work |
| Q5. Which mechanisms serve stand-off and range annotation, and which of them belong to the annotation topic? | coverage, a boundary question | posit selection; map question of Annotation and Overlap |
| Q6. Which of the official process's own reconsiderations for P6 concern structure? | coverage | label query |

The streams queried on 2026-09-06, the declared query of every family with
its hit count and the disposition of every hit stand in the
[selection record](../workbench/selections/2026-09-06-text-and-document-structures-run1.md).

Run 1 admits twelve sources, two chapters and two threads among them. They
are `NH-Non-hierarchical.xml`, `DS-DefaultTextStructure.xml`,
`att.fragmentable.xml`, `join.xml`, `att.global.linking.xml`,
`milestone.xml`, `pb.xml`, `div.xml`, `note.xml`, `P5/Test/testoverlap.xml`,
GitHub issues 1505 and 1400. The raw snapshots of both threads are present
in the checkout of 2026-09-06.

The subsequent intake and processing state is recorded in [[knowledge/state]].
The section audit and prepared source-support pairs are in
`workbench/reviews/2026-09-07-text-structures-run1/`. A chapter draft in that
directory remains outside `40_output/` until the underlying assertions pass
the review required by [[knowledge/verification]].

