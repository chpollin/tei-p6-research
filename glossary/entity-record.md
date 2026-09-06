---
type: glossary
term: "Entity record"
created: 2026-09-06
updated: 2026-09-06
---

# Entity record

An entity record gathers the information known about a person, place or organization in one
place, independent of the way the entity is named or referred to in a text. In TEI P5 4.12.0
the elements `person`, `place` and `org` serve as such records.
[[10_markdown/documents/tei-p5-guidelines-nd-4.12.0#^b133]]

## Examples

<!-- examples:begin -->
- [[30_assertions/p5-guidelines-distinguish-names-for-places-from-other-data-about-places-as-they-do-for-people]] — In TEI P5 4.12.0, the Guidelines distinguish the encoding of names for places from the encoding of other data about places in the same way as for people, and present the place elements as a structured record of data about any place that might be named or referenced within a text
  - [[20_distillates/documents/tei-p5-guidelines-nd-4.12.0#^s42]]
- [[30_assertions/p5-guidelines-group-information-about-a-person-as-distinct-from-references-to-a-person-within-person]] — In TEI P5 4.12.0, the Guidelines group information about a person, as distinct from references to a person such as by name, within a person element
  - [[20_distillates/documents/tei-p5-guidelines-nd-4.12.0#^s26]]
- [[30_assertions/p5-guidelines-let-an-encoder-regard-a-city-and-its-predecessor-as-one-place]] — In TEI P5 4.12.0, the Guidelines give the modern city of Lyon and the Roman Lugdunum, which overlap significantly without being physically co-extensive, as an example of what an encoder may wish to regard as the same place while supplying both names with the period during which each was current
  - [[20_distillates/documents/tei-p5-guidelines-nd-4.12.0#^s43]]
- [[30_assertions/p5-guidelines-separate-the-entity-record-from-references-to-the-entity]] — In TEI P5 4.12.0, the Guidelines describe org, in a way analogous to place and person, as a unique wrapper for information about an entity distinct from the references to that entity, which a naming element typically encodes
  - [[20_distillates/documents/tei-p5-guidelines-nd-4.12.0#^s40]]
- [[30_assertions/p5-guidelines-use-generic-state-trait-and-event-customized-through-type-for-information-about-a-place]] — In TEI P5 4.12.0, the Guidelines state that the kinds of information worth recording for a place beyond its name and location are likely to be very project-specific, that the generic state, trait and event elements customized through their type attribute should be used instead, and that these are complemented by the predefined elements population, climate and terrain
  - [[20_distillates/documents/tei-p5-guidelines-nd-4.12.0#^s49]]
- [[30_assertions/p5-idno-serves-labels-that-identify-an-object-or-concept-in-a-cataloguing-system-or-a-distributed-system]] — In TEI P5 4.12.0, the English remarks on idno state that the element should be used for labels which identify an object or concept in a formal cataloguing system such as a database or an RDF store, or in a distributed system such as the World Wide Web
  - [[20_distillates/documents/tei-p5-idno-4.12.0#^s12]]
- [[30_assertions/p5-idno-supplies-any-form-of-identifier-used-to-identify-some-object-in-a-standardized-way]] — In TEI P5 4.12.0, the English description of idno states that the element supplies any form of identifier used to identify some object in a standardized way
  - [[20_distillates/documents/tei-p5-idno-4.12.0#^s1]]
- [[30_assertions/p5-namesdates-represents-the-referent-and-the-name-independently]] — In TEI P5 4.12.0, the Guidelines state that the module provides elements to represent the person, place or organization a name refers to and the name itself independently of its application, so that it can represent a personal name, the person being named and the canonical name being used
  - [[20_distillates/documents/tei-p5-guidelines-nd-4.12.0#^s2]]
- [[30_assertions/p5-person-holds-variant-name-forms-without-prioritization]] — In TEI P5 4.12.0, the Guidelines allow any number of variant name forms within person, each with its language and kind, with no prioritization among them
  - [[20_distillates/documents/tei-p5-guidelines-nd-4.12.0#^s32]]
- [[30_assertions/p5-person-provides-information-about-an-identifiable-individual]] — In TEI P5 4.12.0, person provides information about an identifiable individual
  - [[20_distillates/documents/tei-p5-person-4.12.0#^s1]]
- [[30_assertions/p5-place-contains-data-about-a-geographic-location]] — In TEI P5 4.12.0, place contains data about a geographic location
  - [[20_distillates/documents/tei-p5-place-4.12.0#^s1]]
- [[30_assertions/p5-prosopography-records-refer-to-external-authorities-through-idno]] — In TEI P5 4.12.0, the Guidelines state that a prosopography record of a named entity commonly refers explicitly to other resources such as name authority files, a gazetteer or a printed book, and follow that statement with a specList naming idno with its type attribute
  - [[20_distillates/documents/tei-p5-guidelines-nd-4.12.0#^s25]]
- [[30_assertions/p5-rolename-excludes-the-role-a-person-has-in-a-context]] — In TEI P5 4.12.0, the Guidelines reserve roleName for roles that function as part of a name and place information about a person's roles and occupations within person
  - [[20_distillates/documents/tei-p5-guidelines-nd-4.12.0#^s11]]
- [[30_assertions/p5-testnames-change-of-place-is-a-sequence-of-dated-residence-states-without-an-event]] — In the TEI P5 4.12.0 test document testnames.xml, a person record holds two successive residence elements, each containing a date with from and to and a placeName, so a change of place is recorded as a sequence of dated states inside the record, which holds no event element
  - [[20_distillates/documents/tei-p5-test-testnames-4.12.0#^s12]]
- [[30_assertions/p5-testnames-person-name-form-and-place-carry-three-separate-identifying-values]] — In the TEI P5 4.12.0 test document testnames.xml, a person record carries only an xml:id on the person element, gives its name form a key of its own beside a type value, and identifies the birthplace by a key on placeName that repeats the element text, so the person, the name form and the place carry three separate identifying values
  - [[20_distillates/documents/tei-p5-test-testnames-4.12.0#^s14]]
- [[30_assertions/p5-testnames-person-record-carries-id-sex-and-role-while-its-persname-carries-only-a-language]] — In the TEI P5 4.12.0 test document testnames.xml, a person record identifies the person by an xml:id on the person element and carries sex and role there, while its single persName child carries only xml:lang and no identifying attribute
  - [[20_distillates/documents/tei-p5-test-testnames-4.12.0#^s7]]
- [[30_assertions/teic-tei-issue-1414-author-proposes-ref-and-key-on-person-and-place]] — In TEIC/TEI issue 1414, the issue author wrote that they thought the best way was to allow ref, and key for the web-impaired, on person and place
  - [[20_distillates/publications/teic-tei-issue-1414#^s3]]
- [[30_assertions/teic-tei-issue-1414-author-proposes-that-a-record-entry-refer-through-ref-or-key-to-further-information-about-the-same-entity]] — In TEIC/TEI issue 1414, the issue author wrote that an entry in a placeography, personography, bibliography or whatever should be able to refer, using ref or key, to some other data structure that has further information about the same entity
  - [[20_distillates/publications/teic-tei-issue-1414#^s1]]
- [[30_assertions/teic-tei-issue-1414-comment-of-2019-reports-that-person-place-org-and-bibl-allow-idno-while-event-and-nym-do-not]] — In TEIC/TEI issue 1414, a comment of 2019-05-07 stated that person, place, org and bibl allowed idno at that time and that event and nym did not
  - [[20_distillates/publications/teic-tei-issue-1414#^s15]]
- [[30_assertions/teic-tei-issue-1414-commenter-summarizes-idno-as-a-first-child-of-the-record-elements-as-the-short-term-solution]] — In TEIC/TEI issue 1414, a commenter summarized the discussion and named adding idno as a first child of the ogrophy elements as the short-term solution
  - [[20_distillates/publications/teic-tei-issue-1414#^s14]]
<!-- examples:end -->
