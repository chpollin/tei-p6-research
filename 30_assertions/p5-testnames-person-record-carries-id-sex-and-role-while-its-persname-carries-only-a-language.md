---
type: assertion
topics: ["[[Metadata and Entities]]"]
phenomena: ["[[glossary/entity-record]]", "[[glossary/mention-of-an-entity]]"]
related: ["[[30_assertions/p5-role-on-a-naming-element-carries-information-about-the-entity-referenced]]", "[[30_assertions/p5-rolename-excludes-the-role-a-person-has-in-a-context]]", "[[30_assertions/p5-person-provides-information-about-an-identifiable-individual]]", "[[30_assertions/p5-testnames-person-name-form-and-place-carry-three-separate-identifying-values]]"]
status: validated
checked:
  machine-review: 2026-09-06
  validation: 2026-09-06
grounding:
  - "[[20_distillates/documents/tei-p5-test-testnames-4.12.0#^s7]]"
created: 2026-09-06
updated: 2026-09-06
---

# In the TEI P5 4.12.0 test document testnames.xml, a person record identifies the person by an xml:id on the person element and carries sex and role there, while its single persName child carries only xml:lang and no identifying attribute

## Statement

In the TEI P5 4.12.0 test document testnames.xml, the person record at block 93 identifies the person by an xml:id on the person element and carries sex and role there as well, while its single persName child carries only xml:lang and no attribute that identifies the person the name stands for.

## Support

- [[20_distillates/documents/tei-p5-test-testnames-4.12.0#^s7]] — A dated observation of one record in the release's own test document at the pinned commit. It establishes that in this record the identifier and the role sit on the record element and that the name form inside the record carries no identification of its own, and it establishes nothing about mentions in running text or about other records of the file.

## Related

- [[30_assertions/MOC-Metadata and Entities]]
- [[30_assertions/p5-role-on-a-naming-element-carries-information-about-the-entity-referenced]]
- [[30_assertions/p5-person-provides-information-about-an-identifiable-individual]]
