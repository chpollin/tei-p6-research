---
type: glossary
term: "Statement about an entity"
created: 2026-09-06
updated: 2026-09-06
---

# Statement about an entity

A statement about an entity attributes a trait, a state, an event or a relationship to a
person, place or organization, rests on a source, can be placed in a time frame and can
conflict with another statement about the same entity. In TEI P5 4.12.0 the Guidelines
describe the information about such entities as statements of this kind.
[[10_markdown/documents/tei-p5-guidelines-nd-4.12.0#^b84]]

## Examples

<!-- examples:begin -->
- [[30_assertions/p5-att-datable-provides-attributes-for-normalization-of-elements-that-contain-dates-times-or-datable-events]] — In TEI P5 4.12.0, the description of att.datable states that the class provides attributes for normalization of elements that contain dates, times, or datable events
  - [[20_distillates/documents/tei-p5-att.datable-4.12.0#^s1]]
- [[30_assertions/p5-att-global-responsibility-indicates-the-agent-responsible-for-something-asserted-by-the-markup]] — In TEI P5 4.12.0, the description of att.global.responsibility states that the class provides attributes indicating the agent responsible for some aspect of the text, the markup or something asserted by the markup
  - [[20_distillates/documents/tei-p5-att.global.responsibility-4.12.0#^s1]]
- [[30_assertions/p5-each-statement-about-a-life-must-be-documentable-and-time-framed]] — In TEI P5 4.12.0, the Guidelines conclude that each statement about the changes of state in a person's life needs to be documentable, put into a time frame and relatable to other statements, because any such statement rests on some source, possibly several and possibly contradictory
  - [[20_distillates/documents/tei-p5-guidelines-nd-4.12.0#^s24]]
- [[30_assertions/p5-entity-information-comprises-statements-about-traits-states-and-events]] — In TEI P5 4.12.0, the Guidelines describe information about people, places, organizations and events as statements about traits, states, events and external resources
  - [[20_distillates/documents/tei-p5-guidelines-nd-4.12.0#^s21]]
- [[30_assertions/p5-generic-description-elements-carry-certainty-and-responsibility]] — In TEI P5 4.12.0, the generic description elements carry cert, resp, evidence and source through att.global.responsibility and att.editLike, so that conflicting sources can yield more than one view of what happened
  - [[20_distillates/documents/tei-p5-guidelines-nd-4.12.0#^s37]]
- [[30_assertions/p5-guidelines-admit-persons-places-and-organizations-as-relationship-participants]] — In TEI P5 4.12.0, the Guidelines chapter names persons, places and organizations as what the participants of a relationship might be
  - [[20_distillates/documents/tei-p5-guidelines-nd-4.12.0#^s38]]
  - [[20_distillates/documents/tei-p5-guidelines-nd-4.12.0#^s39]]
- [[30_assertions/p5-guidelines-present-three-encodings-of-a-nationality-as-the-same-information]] — In TEI P5 4.12.0, the Guidelines present a generic state of type nationality, a nationality element with the same text and an empty nationality element carrying a key and the dating attribute as encodings of the same information
  - [[20_distillates/documents/tei-p5-guidelines-nd-4.12.0#^s33]]
- [[30_assertions/p5-guidelines-use-generic-state-trait-and-event-customized-through-type-for-information-about-a-place]] — In TEI P5 4.12.0, the Guidelines state that the kinds of information worth recording for a place beyond its name and location are likely to be very project-specific, that the generic state, trait and event elements customized through their type attribute should be used instead, and that these are complemented by the predefined elements population, climate and terrain
  - [[20_distillates/documents/tei-p5-guidelines-nd-4.12.0#^s49]]
- [[30_assertions/p5-nested-description-elements-inherit-type-and-responsibility-and-may-date-more-precisely]] — In TEI P5 4.12.0, the Guidelines state that state, trait and other elements of the same class can be nested hierarchically with type values cumulatively inherited, that responsibility is not additive so an element either states it explicitly or inherits it from its nearest ancestor, and that a child element may specify a date more precisely than its parent
  - [[20_distillates/documents/tei-p5-guidelines-nd-4.12.0#^s50]]
- [[30_assertions/p5-person-description-elements-are-datable]] — In TEI P5 4.12.0, the Guidelines state that all the specific and generic elements under discussion are members of att.datable and can therefore be limited in terms of time
  - [[20_distillates/documents/tei-p5-guidelines-nd-4.12.0#^s36]]
- [[30_assertions/p5-relation-describes-a-relationship-amongst-places-events-persons-or-objects]] — In TEI P5 4.12.0, relation describes a relationship or linkage amongst a specified group of places, events, persons, objects or other items
  - [[20_distillates/documents/tei-p5-relation-4.12.0#^s2]]
- [[30_assertions/p5-role-on-a-naming-element-carries-information-about-the-entity-referenced]] — In TEI P5 4.12.0, the role attribute of att.naming may specify further information about the entity referenced by the name, such as the occupation of a person or the status of a place
  - [[20_distillates/documents/tei-p5-att.naming-4.12.0#^s2]]
- [[30_assertions/p5-state-attributes-a-status-or-quality-often-at-a-specific-time-or-for-a-date-range]] — In TEI P5 4.12.0, the English description of state states that the status or quality is attributed often at some specific time or for a specific date range
  - [[20_distillates/documents/tei-p5-state-4.12.0#^s3]]
- [[30_assertions/p5-state-describes-a-status-or-quality-attributed-to-a-person-place-or-organization]] — In TEI P5 4.12.0, the English description of state states that the status or quality the element describes is one attributed to a person, place, or organization
  - [[20_distillates/documents/tei-p5-state-4.12.0#^s2]]
- [[30_assertions/p5-testnames-change-of-place-is-a-sequence-of-dated-residence-states-without-an-event]] — In the TEI P5 4.12.0 test document testnames.xml, a person record holds two successive residence elements, each containing a date with from and to and a placeName, so a change of place is recorded as a sequence of dated states inside the record, which holds no event element
  - [[20_distillates/documents/tei-p5-test-testnames-4.12.0#^s12]]
- [[30_assertions/p5-testnames-places-in-birth-and-death-are-named-without-identification-while-a-nationality-is-identified-by-key]] — In the TEI P5 4.12.0 test document testnames.xml, the place names inside birth and death of one record consist of a settlement and a country carrying neither type nor key, so the places are named without being identified, while the same record identifies a nationality by a key on an empty nationality element
  - [[20_distillates/documents/tei-p5-test-testnames-4.12.0#^s18]]
- [[30_assertions/p5-testnames-relation-to-another-person-is-a-state-with-a-ref-to-a-relationship-and-no-relation-element]] — In the TEI P5 4.12.0 test document testnames.xml, a record expresses a relation to another person as a state whose ref holds a fragment identifier naming a relationship, gives the related person inside a label by a persName that carries only xml:lang and points to no record, and carries no relation element
  - [[20_distillates/documents/tei-p5-test-testnames-4.12.0#^s16]]
<!-- examples:end -->
