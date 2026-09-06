---
type: assertion
topics: ["[[Metadata and Entities]]"]
phenomena: ["[[glossary/statement-about-an-entity]]", "[[glossary/mention-of-an-entity]]"]
related: ["[[30_assertions/p5-relation-describes-a-relationship-amongst-places-events-persons-or-objects]]", "[[30_assertions/p5-guidelines-admit-persons-places-and-organizations-as-relationship-participants]]", "[[30_assertions/p5-state-describes-a-status-or-quality-attributed-to-a-person-place-or-organization]]"]
status: validated
checked:
  machine-review: 2026-09-06
  validation: 2026-09-06
grounding:
  - "[[20_distillates/documents/tei-p5-test-testnames-4.12.0#^s16]]"
created: 2026-09-06
updated: 2026-09-06
---

# In the TEI P5 4.12.0 test document testnames.xml, a record expresses a relation to another person as a state whose ref holds a fragment identifier naming a relationship, gives the related person inside a label by a persName that carries only xml:lang and points to no record, and carries no relation element

## Statement

In the TEI P5 4.12.0 test document testnames.xml, the record at block 134 expresses a relation to another person as a state whose ref holds a fragment identifier naming a relationship, with the related person given inside a label by a persName that carries only xml:lang and points to no record, and the record carries no relation element.

## Support

- [[20_distillates/documents/tei-p5-test-testnames-4.12.0#^s16]] — A dated observation of one record in the release's own test document at the pinned commit. It establishes that in this record a relationship is carried by a statement element whose ref names the kind of relationship and whose related party is a name without identification, and it establishes nothing about what the fragment identifier resolves to or about the use of relation elsewhere in the file.

## Related

- [[30_assertions/MOC-Metadata and Entities]]
- [[30_assertions/p5-relation-describes-a-relationship-amongst-places-events-persons-or-objects]]
- [[30_assertions/p5-guidelines-admit-persons-places-and-organizations-as-relationship-participants]]
