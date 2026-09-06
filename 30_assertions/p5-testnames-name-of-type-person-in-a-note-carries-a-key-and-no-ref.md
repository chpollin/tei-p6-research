---
type: assertion
topics: ["[[Metadata and Entities]]"]
phenomena: ["[[glossary/mention-of-an-entity]]", "[[glossary/entity-identification]]"]
related: ["[[30_assertions/p5-core-elements-state-the-kind-of-referent-only-through-type]]", "[[30_assertions/p5-key-identifies-the-entity-named-through-an-externally-defined-coded-value]]", "[[30_assertions/p5-att-naming-inherits-key-and-ref-and-prefers-a-direct-link]]", "[[30_assertions/p5-testnames-person-name-form-and-place-carry-three-separate-identifying-values]]"]
status: validated
checked:
  machine-review: 2026-09-06
  validation: 2026-09-06
grounding:
  - "[[20_distillates/documents/tei-p5-test-testnames-4.12.0#^s6]]"
created: 2026-09-06
updated: 2026-09-06
---

# In the TEI P5 4.12.0 test document testnames.xml, a record states a relation to another person inside a note and marks that other person with a name element that carries type person and a key holding an identifier and no ref, so the kind of referent is given by type and the identification of the referent by key

## Statement

In the TEI P5 4.12.0 test document testnames.xml, the record at block 84 states a relation to another person inside a note and marks that other person with a name element that carries type="person" and a key holding an identifier while carrying no ref, so that the kind of referent is given by type and the identification of the referent by key.

## Support

- [[20_distillates/documents/tei-p5-test-testnames-4.12.0#^s6]] — A dated observation of one record in the release's own test document at the pinned commit. It establishes the pattern for this one mention, a core name element with a type value and a key and without a ref, and it establishes nothing about how often the file or any edited corpus identifies a mention by key rather than by ref.

## Related

- [[30_assertions/MOC-Metadata and Entities]]
- [[30_assertions/p5-core-elements-state-the-kind-of-referent-only-through-type]]
- [[30_assertions/p5-key-identifies-the-entity-named-through-an-externally-defined-coded-value]]
