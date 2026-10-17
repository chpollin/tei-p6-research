---
type: assertion
topics: ["[[Metadata and Entities]]"]
phenomena: ["[[glossary/mention-of-an-entity]]", "[[glossary/entity-identification]]"]
related: ["[[30_assertions/p5-core-elements-state-the-kind-of-referent-only-through-type]]", "[[30_assertions/p5-key-identifies-the-entity-named-through-an-externally-defined-coded-value]]", "[[30_assertions/p5-att-naming-inherits-key-and-ref-and-prefers-a-direct-link]]", "[[30_assertions/p5-testnames-person-name-form-and-place-carry-three-separate-identifying-values]]"]
status: grounded
checked:
  validation: 2026-10-17
grounding:
  - "[[20_distillates/documents/tei-p5-test-testnames-4.12.0#^s6]]"
created: 2026-09-06
updated: 2026-10-17
---

# In the TEI P5 4.12.0 test document testnames.xml, a note states a spouse relation and contains a name with type person and a nonempty key but no ref

## Statement

In the TEI P5 4.12.0 test document testnames.xml, the record at block 84 contains a note that states a spouse relation and contains a name element carrying type="person" and a nonempty key, with no ref attribute.

## Support

- [[20_distillates/documents/tei-p5-test-testnames-4.12.0#^s6]] — A dated observation of one record in the pinned test document. It establishes the markup of this mention. It does not establish the resolution of the key value or the frequency of the pattern in the file or in edited corpora.

## Related

- [[30_assertions/MOC-Metadata and Entities]]
- [[30_assertions/p5-core-elements-state-the-kind-of-referent-only-through-type]]
- [[30_assertions/p5-key-identifies-the-entity-named-through-an-externally-defined-coded-value]]
