---
type: assertion
topics: ["[[Metadata and Entities]]"]
phenomena: ["[[glossary/mention-of-an-entity]]", "[[glossary/entity-identification]]", "[[glossary/statement-about-an-entity]]"]
related: ["[[30_assertions/p5-guidelines-present-three-encodings-of-a-nationality-as-the-same-information]]", "[[30_assertions/p5-testnames-name-of-type-person-in-a-note-carries-a-key-and-no-ref]]", "[[30_assertions/p5-key-serves-cases-where-no-direct-link-is-required]]"]
status: validated
checked:
  machine-review: 2026-09-06
  validation: 2026-09-06
grounding:
  - "[[20_distillates/documents/tei-p5-test-testnames-4.12.0#^s18]]"
created: 2026-09-06
updated: 2026-09-06
---

# In the TEI P5 4.12.0 test document testnames.xml, the place names inside birth and death of one record consist of a settlement and a country carrying neither type nor key, so the places are named without being identified, while the same record identifies a nationality by a key on an empty nationality element

## Statement

In the TEI P5 4.12.0 test document testnames.xml, the place names inside birth and death of the record at block 137 consist of a settlement and a country element carrying neither type nor key, so those places are named without being identified, while the same record identifies a nationality by a key on an empty nationality element.

## Support

- [[20_distillates/documents/tei-p5-test-testnames-4.12.0#^s18]] — A dated observation of one record in the release's own test document at the pinned commit. It establishes that a name inside a statement may stand without any identification and that a statement element may carry a key in place of text, and it establishes nothing about what the nationality key resolves against.

## Related

- [[30_assertions/MOC-Metadata and Entities]]
- [[30_assertions/p5-guidelines-present-three-encodings-of-a-nationality-as-the-same-information]]
- [[30_assertions/p5-key-serves-cases-where-no-direct-link-is-required]]
