---
type: assertion
topics: ["[[Metadata and Entities]]"]
phenomena: ["[[glossary/mention-of-an-entity]]", "[[glossary/entity-identification]]"]
related: ["[[40_output/12-p6-design]]", "[[30_assertions/p5-placename-abbreviates-typed-name-or-rs-at-the-cost-of-their-distinction]]", "[[30_assertions/p5-rs-contains-a-general-purpose-name-or-referring-string]]"]
status: validated
checked:
  machine-review: 2026-09-06
  validation: 2026-09-06
grounding:
  - "[[20_distillates/documents/tei-p5-guidelines-nd-4.12.0#^s8]]"
created: 2026-09-06
updated: 2026-09-06
---

# In TEI P5 4.12.0, the Guidelines hold persName synonymous with name of type person apart from its own type attribute and treat encodings of one name with rs, name or persName under the same ref as equivalent

## Statement

In TEI P5 4.12.0, the Guidelines state that persName may be used in preference to the general name element whether or not the components of the personal name are marked, that persName is synonymous with name of type person except that its own type attribute allows the personal name itself to be subcategorized, for example as a married, birth, pen, pseudonymous or religious name, and that encodings of one name with rs, with name inside rs, with name and with persName, each carrying the same ref value, are consequently equivalent.

## Support

- [[20_distillates/documents/tei-p5-guidelines-nd-4.12.0#^s8]] — The chapter's own equivalence claim. It establishes the Guidelines' position and establishes nothing about how processors or projects treat the four encodings.

## Related

- [[30_assertions/MOC-Metadata and Entities]]
- [[30_assertions/p5-placename-abbreviates-typed-name-or-rs-at-the-cost-of-their-distinction]]
