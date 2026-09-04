# Primary-source census

This document defines the primary-source universe for the TEI P6 Research
Vault. It distinguishes normative specifications, development records,
governance records, implementation artifacts, historical records, and observed
practice. It does not claim that every source is already acquired; actual state
is recorded in `knowledge/state.md`, source locks, and run manifests.

## Meaning of “all primary sources”

There is no globally finite set of every TEI-related primary source. Private
mail, deleted records, closed project documentation, inaccessible Slack history,
and unknown local customizations cannot be exhaustively recovered. The project
therefore uses a bounded claim:

> All publicly observable primary-source objects exposed by the registered
> official interfaces and repositories during the declared census interval,
> plus every result admitted through a documented real-world sampling protocol,
> with inaccessible and historically lost material recorded as gaps.

Primary means that a source directly records a specification, artifact, event,
decision, implementation, report, or encoding practice being studied. It does
not mean that every primary source is normative or reliable for every claim.

## A. Normative and publication sources

| Family | Primary objects | Boundary | Authority |
|---|---|---|---|
| P5 4.12.0 release | ODD source, prose Guidelines, specifications, exemplars, schemas, release notes, license, published HTML/PDF and release artifacts | exact release tag and full commit | normative for the named release |
| P5 release history | every P5 version exposed by the official release page, Vault, GitHub releases, and Zenodo | official indexes at census time | publication history |
| Earlier Guidelines | P1, P2, P3, P4, DTDs, ODD where available, migration material, and rendered editions | official TEI Archive index | historical normative/publication record for its period |
| Official customizations | TEI All, Lite, Tite, simplePrint, jTEI, Bare, Corpus, MS, Drama, Speech, ODD, SVG, MathML, XInclude and other exemplars in the pinned release | pinned release tree and official customization index | normative or official exemplar within its declared scope |

The principal origins are the
[TEIC/TEI repository](https://github.com/TEIC/TEI), the
[current P5 Guidelines](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/),
the [P5 release index](https://www.tei-c.org/guidelines/p5/), and the
[TEI Archive](https://www.tei-c.org/Vault/).

## B. Development and decision sources

| Family | Primary objects | Boundary | Authority |
|---|---|---|---|
| TEIC/TEI Git history | commits, tags, branches, diffs, file history, and release ancestry | complete observable Git object graph at pinned observations | implementation history |
| TEIC repository census | every public repository exposed by the official GitHub organization | paginated organization API at census time | discovery and publication-infrastructure record |
| TEIC public Git repositories | complete Git object graphs and pinned HEAD trees for every repository in that census | all 41 public repositories observed on 2026-09-04 | mixed development, implementation, event, and infrastructure evidence; classified per repository |
| TEIC/TEI GitHub work items | issues, PRs, comments, reviews, review comments, timelines, commits, changed files, labels, milestones, releases, and relations | authenticated API pagination to exhaustion with start/end reconciliation | proposal, report, discussion, and implementation trail |
| Legacy SourceForge | bug, feature-request, and support trackers; file releases; CVS/SVN material where exposed; migration relations to GitHub | public SourceForge project interfaces | historical development record |
| Council minutes | agendas, minutes, attachments, reports, decisions, and referenced working documents | every meeting linked from the official Council index through the census date | primary technical-governance record |
| Council working documents | repository documents and separately linked papers | complete public `TEIC/Documentation` Git tree plus official links | primary process record, not a complete minutes mirror |
| Board records | meeting minutes, agendas, AGM slides, procedural documents, and published policy decisions | every object linked from the official Board page through the census date | primary strategic-governance record |
| Official P6 process | P6-specific Council records, accessible artifacts, and official presentation repositories | official Council index plus registered public repositories | primary process/development record, not a normative release |

Issue closure does not establish acceptance. Council or Board discussion does
not establish implementation. A merge does not establish released normative
effect. The corpus preserves those transitions as independently evidenced
events.

## C. Reference implementation and tooling sources

| Family | Primary objects | Boundary | Authority |
|---|---|---|---|
| TEI Stylesheets | source, tests, releases, issues, PRs, and transformation profiles | public `TEIC/Stylesheets` repository and its work items | reference ecosystem implementation, not the normative model |
| Roma | RomaJS and relevant predecessor repositories, source, configuration, tests, releases, issues, and PRs | registered TEIC repositories | observed customization-tool behavior |
| TEIGarage and converters | TEIGarage, EGE services, converters, validators, and exposed API contracts | relevant public TEIC repositories | observed processing and conversion behavior |
| Website and infrastructure | TEI website source, publication configuration, redirects, and policies needed to interpret official manifestations | public TEIC website/infrastructure repositories | publication and operational record |

Tool behavior can establish what an implementation does at a version. It does
not override the released Guidelines or prove that every TEI processor behaves
the same way.

## D. Historical design sources

The historical TEI Archive contains the primary records needed to understand
why earlier modeling decisions exist: the Poughkeepsie Principles; Advisory
Board material; Analysis and Interpretation, Metalanguage and Syntax, Text
Documentation, Text Representation, Steering, Technical Review, and editorial
committee documents; working papers and proposals; concluded workgroup
records; earlier Guidelines; migration guidance; and unnumbered reports.

The Archive itself warns that its historical holdings were assembled from
multiple servers and personal collections and are not complete. This family can
be observable-complete for the official Archive index while remaining
historically incomplete.

## E. Community and practice sources

| Family | Primary objects | Boundary | Authority |
|---|---|---|---|
| TEI-L | publicly archived messages and threads | LISTSERV archive within a declared date and query boundary | primary record of community questions and practice, not consensus |
| SIGs and workgroups | charters, minutes, reports, proposals, schemas, repositories, wiki pages, and list archives | official active/dormant SIG and concluded-workgroup indexes | primary community/process record |
| Annual meetings | programmes, AGM material, abstracts, slides, reports, and published proceedings | official meeting indexes and archives | primary event and attributed proposal record |
| Registered projects | project documentation, schemas, examples, and processing code | explicit sample selected under a published protocol | observed practice within the sample |
| Real-world ODDs | customization source, generated schemas, documentation, tests, release history, and compatibility declarations | reproducible repository and registry census plus purposive domain sample | observed customization practice within the sample |

TEI-L and SIG material is user-generated content. Rights, privacy, and
redistribution are reviewed per collection. Raw text defaults to local-only;
public repository output may use metadata, locators, hashes, and checked short
quotations until rights are established.

## Secondary and interpretive sources

Journal articles, books, dissertations, tutorials, retrospective essays, and
research reports are essential to the project but are normally secondary
sources. They are collected through the separate bounded literature protocol.
An article may contain primary empirical material, but its role must be declared
for the specific claim rather than inferred from publication venue.

## Acquisition tiers

The census uses three priorities without changing source authority:

1. **Core:** pinned P5 release and Git history, TEIC/TEI work items, Council and
   Board records, official P6 records, and P5 release history.
2. **Interpretive infrastructure:** TEI Archive, SourceForge, Stylesheets,
   Roma/TEIGarage, website sources, and official customizations.
3. **Observed practice:** TEI-L, SIG/workgroup outputs, annual meetings, and a
   rights-aware sample of projects and ODD customizations.

Core sources are required for any architecture-level conclusion. Later tiers
are required before claims about historical motivation, processing cost,
community need, or real-world migration can be generalized.

## Completion rule

A family is complete only under the tests in `corpus/COMPLETENESS.md`. Each run
records the exact time interval, interface, pagination, object counts, hashes,
rights exceptions, and inaccessible objects. If an interface cannot expose a
finite census, the result is `bounded-complete` or `not-completable`, never
silently described as complete.
