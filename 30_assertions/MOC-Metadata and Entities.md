---
type: moc
topic: "Metadata and Entities"
created: 2026-09-04
updated: 2026-09-06
---

# MOC: Metadata and Entities

This map gathers grounded statements about the teiHeader, metadata, authority data,
persons, places, organizations, events and their reference relations.

## Sources and distillates

<!-- distillates:begin -->
- [[20_distillates/documents/tei-p5-att.canonical-4.12.0]]
- [[20_distillates/documents/tei-p5-att.naming-4.12.0]]
- [[20_distillates/documents/tei-p5-guidelines-nd-4.12.0]]
- [[20_distillates/documents/tei-p5-name-4.12.0]]
- [[20_distillates/documents/tei-p5-nym-4.12.0]]
- [[20_distillates/documents/tei-p5-persname-4.12.0]]
- [[20_distillates/documents/tei-p5-person-4.12.0]]
- [[20_distillates/documents/tei-p5-relation-4.12.0]]
- [[20_distillates/documents/tei-p5-rs-4.12.0]]
<!-- distillates:end -->

## Assertions

<!-- assertions:begin -->
- [[30_assertions/p5-att-canonical-associates-a-name-with-canonical-information-about-its-object]] — In TEI P5 4.12.0, att.canonical associates a representation such as a name or title with canonical information about the object being named or referenced
- [[30_assertions/p5-att-canonical-gives-no-precedence-when-key-and-ref-co-occur]] — In TEI P5 4.12.0, att.canonical provides no semantic basis and suggests no precedence when both key and ref are supplied
- [[30_assertions/p5-att-naming-describes-nymref-through-the-object-named]] — In TEI P5 4.12.0, att.naming describes nymRef as locating the canonical form of the names associated with the object named by the element bearing it
- [[30_assertions/p5-att-naming-inherits-key-and-ref-and-prefers-a-direct-link]] — In TEI P5 4.12.0, att.naming inherits key and ref from att.canonical as two ways of associating a name with its referent, and ref is to be used wherever a direct link to canonical information about the referent can be supplied
- [[30_assertions/p5-core-elements-state-the-kind-of-referent-only-through-type]] — In TEI P5 4.12.0, the core elements mark a text segment as a proper noun or referring string and state the kind of object named only through the type attribute
- [[30_assertions/p5-each-statement-about-a-life-must-be-documentable-and-time-framed]] — In TEI P5 4.12.0, the Guidelines conclude that each statement about the changes of state in a person's life needs to be documentable, put into a time frame and relatable to other statements, because any such statement rests on some source, possibly several and possibly contradictory
- [[30_assertions/p5-entity-information-comprises-statements-about-traits-states-and-events]] — In TEI P5 4.12.0, the Guidelines describe information about people, places, organizations and events as statements about traits, states, events and external resources
- [[30_assertions/p5-generic-description-elements-carry-certainty-and-responsibility]] — In TEI P5 4.12.0, the generic description elements carry cert, resp, evidence and source through att.global.responsibility and att.editLike, so that conflicting sources can yield more than one view of what happened
- [[30_assertions/p5-guidelines-admit-persons-places-and-organizations-as-relationship-participants]] — In TEI P5 4.12.0, the Guidelines chapter names persons, places and organizations as what the participants of a relationship might be
- [[30_assertions/p5-guidelines-detach-the-nymref-association-from-the-entity-named]] — In TEI P5 4.12.0, the Guidelines state that the association nymRef makes with a nym has nothing to do with any individual who might use the name
- [[30_assertions/p5-guidelines-distinguish-resolving-a-name-from-treating-it-as-an-object]] — In TEI P5 4.12.0, the Guidelines distinguish the resolution of a name or referring string to its referent through key or ref from the treatment of names as objects in their own right, for whose canonical or normalized form they use the term nym
- [[30_assertions/p5-guidelines-let-an-encoder-regard-a-city-and-its-predecessor-as-one-place]] — In TEI P5 4.12.0, the Guidelines give the modern city of Lyon and the Roman Lugdunum, which overlap significantly without being physically co-extensive, as an example of what an encoder may wish to regard as the same place while supplying both names with the period during which each was current
- [[30_assertions/p5-guidelines-present-three-encodings-of-a-nationality-as-the-same-information]] — In TEI P5 4.12.0, the Guidelines present a generic state of type nationality, a nationality element with the same text and an empty nationality element carrying a key and the dating attribute as encodings of the same information
- [[30_assertions/p5-guidelines-separate-the-entity-record-from-references-to-the-entity]] — In TEI P5 4.12.0, the Guidelines describe org, in a way analogous to place and person, as a unique wrapper for information about an entity distinct from the references to that entity, which a naming element typically encodes
- [[30_assertions/p5-key-identifies-the-entity-named-through-an-externally-defined-coded-value]] — In TEI P5 4.12.0, the key attribute of att.canonical provides an externally defined means of identifying the entity or entities being named, using a coded value of some kind
- [[30_assertions/p5-key-requires-resolution-documentation-for-interchange]] — In TEI P5 4.12.0, the use of key in interchange requires that documentation about how the key is to be resolved be sent to the recipient
- [[30_assertions/p5-key-serves-cases-where-no-direct-link-is-required]] — In TEI P5 4.12.0, key serves cases where no direct link is required, because a local convention resolves the reference or because the encoder judges that no resolution is necessary
- [[30_assertions/p5-name-component-markup-does-not-cover-every-name]] — In TEI P5 4.12.0, the Guidelines state that their mechanisms for marking personal name components will not cater for every personal name or every processing need, and recommend feature structures where the structure is highly complex or the components particularly ambiguous
- [[30_assertions/p5-namesdates-represents-the-referent-and-the-name-independently]] — In TEI P5 4.12.0, the Guidelines state that the module provides elements to represent the person, place or organization a name refers to and the name itself independently of its application, so that it can represent a personal name, the person being named and the canonical name being used
- [[30_assertions/p5-nym-contains-the-definition-of-a-canonical-name-or-name-component]] — In TEI P5 4.12.0, nym contains the definition for a canonical name or name component of any kind
- [[30_assertions/p5-persname-contains-a-proper-noun-referring-to-a-person]] — In TEI P5 4.12.0, the English description of persName states that the element contains a proper noun or proper-noun phrase referring to a person
- [[30_assertions/p5-persname-is-synonymous-with-name-of-type-person]] — In TEI P5 4.12.0, the Guidelines hold persName synonymous with name of type person apart from its own type attribute and treat encodings of one name with rs, name or persName under the same ref as equivalent
- [[30_assertions/p5-person-description-elements-are-datable]] — In TEI P5 4.12.0, the Guidelines state that all the specific and generic elements under discussion are members of att.datable and can therefore be limited in terms of time
- [[30_assertions/p5-person-holds-variant-name-forms-without-prioritization]] — In TEI P5 4.12.0, the Guidelines allow any number of variant name forms within person, each with its language and kind, with no prioritization among them
- [[30_assertions/p5-person-provides-information-about-an-identifiable-individual]] — In TEI P5 4.12.0, person provides information about an identifiable individual
- [[30_assertions/p5-placename-abbreviates-typed-name-or-rs-at-the-cost-of-their-distinction]] — In TEI P5 4.12.0, the Guidelines state that placeName may be regarded as an abbreviation for name or rs of type place and add in a footnote that strictly a value such as figurative should be given to the periphrastic place names in the placeName version of their example to preserve the distinction that the choice of rs had indicated
- [[30_assertions/p5-prosopography-records-refer-to-external-authorities-through-idno]] — In TEI P5 4.12.0, the Guidelines state that a prosopography record of a named entity commonly refers explicitly to other resources such as name authority files, a gazetteer or a printed book, and follow that statement with a specList naming idno with its type attribute
- [[30_assertions/p5-ref-locates-a-definition-or-identity-for-the-entity-named-by-uris]] — In TEI P5 4.12.0, the ref attribute of att.canonical provides an explicit means of locating a full definition or identity for the entity being named by means of one or more URIs
- [[30_assertions/p5-ref-points-directly-to-xml-elements-or-other-resources]] — In TEI P5 4.12.0, the English remarks on the ref attribute require its value to point directly to one or more XML elements or other resources by means of one or more whitespace-separated URIs
- [[30_assertions/p5-relation-describes-a-relationship-amongst-places-events-persons-or-objects]] — In TEI P5 4.12.0, relation describes a relationship or linkage amongst a specified group of places, events, persons, objects or other items
- [[30_assertions/p5-role-on-a-naming-element-carries-information-about-the-entity-referenced]] — In TEI P5 4.12.0, the role attribute of att.naming may specify further information about the entity referenced by the name, such as the occupation of a person or the status of a place
- [[30_assertions/p5-rolename-excludes-the-role-a-person-has-in-a-context]] — In TEI P5 4.12.0, the Guidelines reserve roleName for roles that function as part of a name and place information about a person's roles and occupations within person
- [[30_assertions/p5-rs-and-name-cannot-mark-the-components-of-a-name]] — In TEI P5 4.12.0, the Guidelines state that rs and name are insufficiently powerful to mark the internal components or structure of names and provide persName, surname, forename, roleName, addName, nameLink and genName for these and related purposes
- [[30_assertions/p5-rs-contains-a-general-purpose-name-or-referring-string]] — In TEI P5 4.12.0, rs contains a general purpose name or referring string
- [[30_assertions/p5-simultaneous-key-and-ref-are-not-recommended-without-documentation]] — In TEI P5 4.12.0, the English remarks on att.canonical state that the simultaneous use of both key and ref is not recommended unless documentation explaining the use is provided for interchange, probably in an ODD customization
<!-- assertions:end -->

## Open questions

- How consistently does P5 separate mentions in the text, entity descriptions,
  identification and external authority references?
