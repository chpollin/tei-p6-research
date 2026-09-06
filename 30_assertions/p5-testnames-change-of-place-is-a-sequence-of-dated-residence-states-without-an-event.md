---
type: assertion
topics: ["[[Metadata and Entities]]"]
phenomena: ["[[glossary/statement-about-an-entity]]", "[[glossary/entity-record]]"]
related: ["[[30_assertions/p5-each-statement-about-a-life-must-be-documentable-and-time-framed]]", "[[30_assertions/p5-person-description-elements-are-datable]]", "[[30_assertions/p5-state-attributes-a-status-or-quality-often-at-a-specific-time-or-for-a-date-range]]", "[[30_assertions/p5-entity-information-comprises-statements-about-traits-states-and-events]]"]
status: validated
checked:
  machine-review: 2026-09-06
  validation: 2026-09-06
grounding:
  - "[[20_distillates/documents/tei-p5-test-testnames-4.12.0#^s12]]"
created: 2026-09-06
updated: 2026-09-06
---

# In the TEI P5 4.12.0 test document testnames.xml, a person record holds two successive residence elements, each containing a date with from and to and a placeName, so a change of place is recorded as a sequence of dated states inside the record, which holds no event element

## Statement

In the TEI P5 4.12.0 test document testnames.xml, the record at block 123 holds two successive residence elements, each containing a date with from and to and a placeName, so that a change of place is recorded as a sequence of dated states inside the person record, and the record holds no event element.

## Support

- [[20_distillates/documents/tei-p5-test-testnames-4.12.0#^s12]] — A dated observation of one record in the release's own test document at the pinned commit. It establishes that the time frame of these two states is carried by a date element inside each state rather than by attributes on the state element, and it establishes nothing about responsibility, certainty or source markers, which the statement does not mention.

## Related

- [[30_assertions/MOC-Metadata and Entities]]
- [[30_assertions/p5-each-statement-about-a-life-must-be-documentable-and-time-framed]]
- [[30_assertions/p5-person-description-elements-are-datable]]
