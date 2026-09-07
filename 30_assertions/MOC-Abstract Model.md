---
type: moc
topic: "Abstract Model"
created: 2026-09-04
updated: 2026-09-06
---

# MOC: Abstract Model

This map connects grounded statements about concepts, annotation, and addressing
in the pinned P5 baseline. Independent definitions remain design hypotheses.

## Sources and distillates

<!-- distillates:begin -->
- [[20_distillates/documents/hsa-letter-4493-2026-09-07]]
- [[20_distillates/documents/szd-werke-2026-09-07]]
- [[20_distillates/documents/tei-p5-anchor-4.12.0]]
- [[20_distillates/documents/tei-p5-annotation-4.12.0]]
- [[20_distillates/documents/tei-p5-att.canonical-4.12.0]]
- [[20_distillates/documents/tei-p5-att.global.responsibility-4.12.0]]
- [[20_distillates/documents/tei-p5-guidelines-nd-4.12.0]]
- [[20_distillates/documents/tei-p5-span-4.12.0]]
- [[20_distillates/publications/piez2014range]]
- [[20_distillates/publications/renear-wickett2010documents]]
- [[20_distillates/publications/w3c-web-annotation-20170223]]
<!-- distillates:end -->

## Assertions

<!-- assertions:begin -->
- [[30_assertions/hsa-dateline-retains-short-year]] — Die Datumszeile in Schuchardt-Brief 4493 verwendet eine zweistellige Jahresangabe
- [[30_assertions/hsa-origin-and-sent-dates-have-distinct-contexts]] — Schuchardt-Brief 4493 enthält denselben Datumswert in Entstehungs- und Versandmetadaten
- [[30_assertions/p5-anchor-identifies-a-textual-point]] — In TEI P5 4.12.0, anchor identifies a point within a text
- [[30_assertions/p5-annotation-refers-to-web-annotation-model]] — TEI P5 4.12.0 describes annotation as following the Web Annotation Data Model
- [[30_assertions/p5-att-canonical-gives-no-precedence-when-key-and-ref-co-occur]] — In TEI P5 4.12.0, att.canonical provides no semantic basis and suggests no precedence when both key and ref are supplied
- [[30_assertions/p5-att-global-responsibility-indicates-the-agent-responsible-for-something-asserted-by-the-markup]] — In TEI P5 4.12.0, the description of att.global.responsibility states that the class provides attributes indicating the agent responsible for some aspect of the text, the markup or something asserted by the markup
- [[30_assertions/p5-each-statement-about-a-life-must-be-documentable-and-time-framed]] — In TEI P5 4.12.0, the Guidelines conclude that each statement about the changes of state in a person's life needs to be documentable, put into a time frame and relatable to other statements, because any such statement rests on some source, possibly several and possibly contradictory
- [[30_assertions/p5-generic-description-elements-carry-certainty-and-responsibility]] — In TEI P5 4.12.0, the generic description elements carry cert, resp, evidence and source through att.global.responsibility and att.editLike, so that conflicting sources can yield more than one view of what happened
- [[30_assertions/p5-guidelines-distinguish-names-for-places-from-other-data-about-places-as-they-do-for-people]] — In TEI P5 4.12.0, the Guidelines distinguish the encoding of names for places from the encoding of other data about places in the same way as for people, and present the place elements as a structured record of data about any place that might be named or referenced within a text
- [[30_assertions/p5-guidelines-distinguish-resolving-a-name-from-treating-it-as-an-object]] — In TEI P5 4.12.0, the Guidelines distinguish the resolution of a name or referring string to its referent through key or ref from the treatment of names as objects in their own right, for whose canonical or normalized form they use the term nym
- [[30_assertions/p5-guidelines-group-information-about-a-person-as-distinct-from-references-to-a-person-within-person]] — In TEI P5 4.12.0, the Guidelines group information about a person, as distinct from references to a person such as by name, within a person element
- [[30_assertions/p5-guidelines-separate-the-entity-record-from-references-to-the-entity]] — In TEI P5 4.12.0, the Guidelines describe org, in a way analogous to place and person, as a unique wrapper for information about an entity distinct from the references to that entity, which a naming element typically encodes
- [[30_assertions/p5-namesdates-represents-the-referent-and-the-name-independently]] — In TEI P5 4.12.0, the Guidelines state that the module provides elements to represent the person, place or organization a name refers to and the name itself independently of its application, so that it can represent a personal name, the person being named and the canonical name being used
- [[30_assertions/p5-nested-description-elements-inherit-type-and-responsibility-and-may-date-more-precisely]] — In TEI P5 4.12.0, the Guidelines state that state, trait and other elements of the same class can be nested hierarchically with type values cumulatively inherited, that responsibility is not additive so an element either states it explicitly or inherits it from its nearest ancestor, and that a child element may specify a date more precisely than its parent
- [[30_assertions/p5-span-associates-interpretation-with-text]] — In TEI P5 4.12.0, span associates an interpretative annotation with a span of text
- [[30_assertions/p5-span-from-identifies-start-or-whole-node]] — In TEI P5 4.12.0, span from identifies the starting node or, without to, the entire annotated node
- [[30_assertions/piez-treats-optional-hierarchy-as-object-of-study]] — Piez treats optional hierarchy as an object of study
- [[30_assertions/renear-wickett-distinguish-string-mapping-from-persistent-identity]] — Renear and Wickett describe editing strings as mapping rather than modifying a persistent entity
- [[30_assertions/szd-contributor-and-hand-description-are-distinct]] — SZDMSK.3 erfasst Mitwirkung und Handschriftenangabe in getrennten Feldern
- [[30_assertions/szd-hand-attribution-retains-question-mark]] — Die Handschriftenangabe in SZDMSK.3 enthält ein Fragezeichen
- [[30_assertions/szd-records-have-distinct-shelfmarks]] — Die Zweig-Katalogeinträge SZDMSK.3 und SZDMSK.4 tragen unterschiedliche Signaturen und PIDs
- [[30_assertions/szd-records-share-work-reference]] — Die Zweig-Katalogeinträge SZDMSK.3 und SZDMSK.4 teilen einen Werkverweis
- [[30_assertions/w3c-quote-selection-can-match-multiple-sequences]] — W3C quote selection can match multiple sequences
<!-- assertions:end -->

## Open questions

- Which P5 distinctions support a serialization-independent model of text?
- Which sources establish text identity and version continuity beyond these
  selected element definitions?
- Which real editorial cases challenge immutable versions and region selectors?
- What additional sources are needed to evaluate the full Web Annotation Data
  Model and the range of P5 stand-off mechanisms?
