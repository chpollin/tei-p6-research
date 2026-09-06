---
type: assertion
topics: ["[[Metadata and Entities]]"]
phenomena: ["[[glossary/entity-record]]", "[[glossary/entity-identification]]", "[[glossary/name-as-an-object]]"]
related: ["[[30_assertions/p5-key-identifies-the-entity-named-through-an-externally-defined-coded-value]]", "[[30_assertions/p5-person-holds-variant-name-forms-without-prioritization]]", "[[30_assertions/p5-testnames-name-of-type-person-in-a-note-carries-a-key-and-no-ref]]", "[[30_assertions/p5-testnames-person-record-carries-id-sex-and-role-while-its-persname-carries-only-a-language]]"]
status: validated
checked:
  machine-review: 2026-09-06
  validation: 2026-09-06
grounding:
  - "[[20_distillates/documents/tei-p5-test-testnames-4.12.0#^s14]]"
created: 2026-09-06
updated: 2026-09-06
---

# In the TEI P5 4.12.0 test document testnames.xml, a person record carries only an xml:id on the person element, gives its name form a key of its own beside a type value, and identifies the birthplace by a key on placeName that repeats the element text, so the person, the name form and the place carry three separate identifying values

## Statement

In the TEI P5 4.12.0 test document testnames.xml, the record at block 132 carries only an xml:id on the person element, gives the name form its own key beside type="full", and identifies the birthplace by a key on placeName whose value repeats the text of that element, so that the person, the name form and the place carry three separate identifying values.

## Support

- [[20_distillates/documents/tei-p5-test-testnames-4.12.0#^s14]] — A dated observation of one record in the release's own test document at the pinned commit. It establishes that in this record identification attaches to the record, to a name form inside the record and to a place name inside a statement, each by its own value, and it establishes nothing about what any of the three values resolves against.

## Related

- [[30_assertions/MOC-Metadata and Entities]]
- [[30_assertions/p5-key-identifies-the-entity-named-through-an-externally-defined-coded-value]]
- [[30_assertions/p5-person-holds-variant-name-forms-without-prioritization]]
