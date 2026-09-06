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
- [[30_assertions/p5-guidelines-let-an-encoder-regard-a-city-and-its-predecessor-as-one-place]] — In TEI P5 4.12.0, the Guidelines give the modern city of Lyon and the Roman Lugdunum, which overlap significantly without being physically co-extensive, as an example of what an encoder may wish to regard as the same place while supplying both names with the period during which each was current
  - [[20_distillates/documents/tei-p5-guidelines-nd-4.12.0#^s43]]
- [[30_assertions/p5-guidelines-separate-the-entity-record-from-references-to-the-entity]] — In TEI P5 4.12.0, the Guidelines describe org, in a way analogous to place and person, as a unique wrapper for information about an entity distinct from the references to that entity, which a naming element typically encodes
  - [[20_distillates/documents/tei-p5-guidelines-nd-4.12.0#^s40]]
- [[30_assertions/p5-namesdates-represents-the-referent-and-the-name-independently]] — In TEI P5 4.12.0, the Guidelines state that the module provides elements to represent the person, place or organization a name refers to and the name itself independently of its application, so that it can represent a personal name, the person being named and the canonical name being used
  - [[20_distillates/documents/tei-p5-guidelines-nd-4.12.0#^s2]]
- [[30_assertions/p5-person-holds-variant-name-forms-without-prioritization]] — In TEI P5 4.12.0, the Guidelines allow any number of variant name forms within person, each with its language and kind, with no prioritization among them
  - [[20_distillates/documents/tei-p5-guidelines-nd-4.12.0#^s32]]
- [[30_assertions/p5-person-provides-information-about-an-identifiable-individual]] — In TEI P5 4.12.0, person provides information about an identifiable individual
  - [[20_distillates/documents/tei-p5-person-4.12.0#^s1]]
- [[30_assertions/p5-prosopography-records-refer-to-external-authorities-through-idno]] — In TEI P5 4.12.0, the Guidelines state that a prosopography record of a named entity commonly refers explicitly to other resources such as name authority files, a gazetteer or a printed book, and follow that statement with a specList naming idno with its type attribute
  - [[20_distillates/documents/tei-p5-guidelines-nd-4.12.0#^s25]]
- [[30_assertions/p5-rolename-excludes-the-role-a-person-has-in-a-context]] — In TEI P5 4.12.0, the Guidelines reserve roleName for roles that function as part of a name and place information about a person's roles and occupations within person
  - [[20_distillates/documents/tei-p5-guidelines-nd-4.12.0#^s11]]
<!-- examples:end -->
