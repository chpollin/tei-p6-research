---
type: assertion
topics: ["[[Metadata and Entities]]"]
phenomena: ["[[glossary/mention-of-an-entity]]", "[[glossary/entity-identification]]"]
related: ["[[40_output/12-p6-design]]", "[[30_assertions/p5-placename-abbreviates-typed-name-or-rs-at-the-cost-of-their-distinction]]", "[[30_assertions/p5-rs-contains-a-general-purpose-name-or-referring-string]]"]
status: grounded
checked: {}
grounding:
  - "[[20_distillates/documents/tei-p5-guidelines-nd-4.12.0#^s8]]"
created: 2026-09-06
updated: 2026-09-11
---

# The P5 4.12.0 Guidelines describe persName as synonymous with name of type person, with an exception for its own type attribute

## Statement

In TEI P5 4.12.0, the Guidelines state that `persName` may be used in preference to the general `name` element whether or not the components of the personal name are also marked, that `persName` is synonymous with `name type="person"` except that its own `type` attribute allows further subcategorization of the personal name itself, for example as a `married`, `birth`, `pen`, `pseudo` or `religious` name, and that consequently their four example encodings of one name are equivalent, namely `rs type="person"`, `name` inside `rs type="person"` and `name type="person"`, each carrying the same `ref` value, and `persName` carrying that `ref` value.

## Support

- [[20_distillates/documents/tei-p5-guidelines-nd-4.12.0#^s8]]

## Related

- [[30_assertions/MOC-Metadata and Entities]]
- [[30_assertions/p5-placename-abbreviates-typed-name-or-rs-at-the-cost-of-their-distinction]]
