---
type: glossary
term: "Mention of an entity"
created: 2026-09-06
updated: 2026-09-06
---

# Mention of an entity

A mention of an entity is a segment of a text that refers to a person, place or organization,
as a proper noun or as a referring string, so that the reference is marked where it occurs.
In TEI P5 4.12.0 the core module marks such a segment as a proper noun or a referring string
and states the kind of object referred to only through a `type` value.
[[10_markdown/documents/tei-p5-guidelines-nd-4.12.0#^b2]]

## Examples

<!-- examples:begin -->
- [[30_assertions/p5-att-naming-inherits-key-and-ref-and-prefers-a-direct-link]] — In TEI P5 4.12.0, att.naming inherits key and ref from att.canonical as two ways of associating a name with its referent, and ref is to be used wherever a direct link to canonical information about the referent can be supplied
  - [[20_distillates/documents/tei-p5-guidelines-nd-4.12.0#^s3]]
- [[30_assertions/p5-att-personal-provides-common-attributes-for-elements-forming-part-of-a-name]] — In TEI P5 4.12.0, the description of att.personal states that the class provides common attributes for those elements which form part of a name, usually but not necessarily a personal name
  - [[20_distillates/documents/tei-p5-att.personal-4.12.0#^s1]]
- [[30_assertions/p5-core-elements-state-the-kind-of-referent-only-through-type]] — In TEI P5 4.12.0, the core elements mark a text segment as a proper noun or referring string and state the kind of object named only through the type attribute
  - [[20_distillates/documents/tei-p5-guidelines-nd-4.12.0#^s1]]
- [[30_assertions/p5-guidelines-distinguish-names-for-places-from-other-data-about-places-as-they-do-for-people]] — In TEI P5 4.12.0, the Guidelines distinguish the encoding of names for places from the encoding of other data about places in the same way as for people, and present the place elements as a structured record of data about any place that might be named or referenced within a text
  - [[20_distillates/documents/tei-p5-guidelines-nd-4.12.0#^s42]]
- [[30_assertions/p5-guidelines-group-information-about-a-person-as-distinct-from-references-to-a-person-within-person]] — In TEI P5 4.12.0, the Guidelines group information about a person, as distinct from references to a person such as by name, within a person element
  - [[20_distillates/documents/tei-p5-guidelines-nd-4.12.0#^s26]]
- [[30_assertions/p5-guidelines-separate-the-entity-record-from-references-to-the-entity]] — In TEI P5 4.12.0, the Guidelines describe org, in a way analogous to place and person, as a unique wrapper for information about an entity distinct from the references to that entity, which a naming element typically encodes
  - [[20_distillates/documents/tei-p5-guidelines-nd-4.12.0#^s40]]
- [[30_assertions/p5-namesdates-represents-the-referent-and-the-name-independently]] — In TEI P5 4.12.0, the Guidelines state that the module provides elements to represent the person, place or organization a name refers to and the name itself independently of its application, so that it can represent a personal name, the person being named and the canonical name being used
  - [[20_distillates/documents/tei-p5-guidelines-nd-4.12.0#^s2]]
- [[30_assertions/p5-persname-contains-a-proper-noun-referring-to-a-person]] — In TEI P5 4.12.0, the English description of persName states that the element contains a proper noun or proper-noun phrase referring to a person
  - [[20_distillates/documents/tei-p5-persname-4.12.0#^s1]]
- [[30_assertions/p5-persname-is-synonymous-with-name-of-type-person]] — In TEI P5 4.12.0, the Guidelines hold persName synonymous with name of type person apart from its own type attribute and treat encodings of one name with rs, name or persName under the same ref as equivalent
  - [[20_distillates/documents/tei-p5-guidelines-nd-4.12.0#^s8]]
- [[30_assertions/p5-placename-abbreviates-typed-name-or-rs-at-the-cost-of-their-distinction]] — In TEI P5 4.12.0, the Guidelines state that placeName may be regarded as an abbreviation for name or rs of type place and add in a footnote that strictly a value such as figurative should be given to the periphrastic place names in the placeName version of their example to preserve the distinction that the choice of rs had indicated
  - [[20_distillates/documents/tei-p5-guidelines-nd-4.12.0#^s18]]
- [[30_assertions/p5-role-on-a-naming-element-carries-information-about-the-entity-referenced]] — In TEI P5 4.12.0, the role attribute of att.naming may specify further information about the entity referenced by the name, such as the occupation of a person or the status of a place
  - [[20_distillates/documents/tei-p5-att.naming-4.12.0#^s2]]
- [[30_assertions/p5-rolename-excludes-the-role-a-person-has-in-a-context]] — In TEI P5 4.12.0, the Guidelines reserve roleName for roles that function as part of a name and place information about a person's roles and occupations within person
  - [[20_distillates/documents/tei-p5-guidelines-nd-4.12.0#^s11]]
- [[30_assertions/p5-rs-and-name-cannot-mark-the-components-of-a-name]] — In TEI P5 4.12.0, the Guidelines state that rs and name are insufficiently powerful to mark the internal components or structure of names and provide persName, surname, forename, roleName, addName, nameLink and genName for these and related purposes
  - [[20_distillates/documents/tei-p5-guidelines-nd-4.12.0#^s7]]
- [[30_assertions/p5-rs-contains-a-general-purpose-name-or-referring-string]] — In TEI P5 4.12.0, rs contains a general purpose name or referring string
  - [[20_distillates/documents/tei-p5-rs-4.12.0#^s1]]
- [[30_assertions/p5-testnames-name-of-type-person-in-a-note-carries-a-key-and-no-ref]] — In the TEI P5 4.12.0 test document testnames.xml, a record states a relation to another person inside a note and marks that other person with a name element that carries type person and a key holding an identifier and no ref, so the kind of referent is given by type and the identification of the referent by key
  - [[20_distillates/documents/tei-p5-test-testnames-4.12.0#^s6]]
- [[30_assertions/p5-testnames-person-record-carries-id-sex-and-role-while-its-persname-carries-only-a-language]] — In the TEI P5 4.12.0 test document testnames.xml, a person record identifies the person by an xml:id on the person element and carries sex and role there, while its single persName child carries only xml:lang and no identifying attribute
  - [[20_distillates/documents/tei-p5-test-testnames-4.12.0#^s7]]
- [[30_assertions/p5-testnames-places-in-birth-and-death-are-named-without-identification-while-a-nationality-is-identified-by-key]] — In the TEI P5 4.12.0 test document testnames.xml, the place names inside birth and death of one record consist of a settlement and a country carrying neither type nor key, so the places are named without being identified, while the same record identifies a nationality by a key on an empty nationality element
  - [[20_distillates/documents/tei-p5-test-testnames-4.12.0#^s18]]
- [[30_assertions/p5-testnames-relation-to-another-person-is-a-state-with-a-ref-to-a-relationship-and-no-relation-element]] — In the TEI P5 4.12.0 test document testnames.xml, a record expresses a relation to another person as a state whose ref holds a fragment identifier naming a relationship, gives the related person inside a label by a persName that carries only xml:lang and points to no record, and carries no relation element
  - [[20_distillates/documents/tei-p5-test-testnames-4.12.0#^s16]]
- [[30_assertions/teic-tei-issue-2739-commenter-states-att-personal-is-a-member-of-att-naming-and-att-naming-of-att-canonical]] — In TEIC/TEI issue 2739, a commenter stated that att.personal is a member of att.naming and that att.naming is a member of att.canonical
  - [[20_distillates/publications/teic-tei-issue-2739#^s4]]
<!-- examples:end -->
