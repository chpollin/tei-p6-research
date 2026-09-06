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
- [[30_assertions/p5-core-elements-state-the-kind-of-referent-only-through-type]] — In TEI P5 4.12.0, the core elements mark a text segment as a proper noun or referring string and state the kind of object named only through the type attribute
  - [[20_distillates/documents/tei-p5-guidelines-nd-4.12.0#^s1]]
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
<!-- examples:end -->
