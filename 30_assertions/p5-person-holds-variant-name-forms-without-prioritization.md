---
type: assertion
topics: ["[[Metadata and Entities]]"]
phenomena: ["[[glossary/name-as-an-object]]", "[[glossary/entity-record]]"]
related: ["[[40_output/12-p6-design]]", "[[30_assertions/p5-person-description-elements-are-datable]]"]
status: validated
checked:
  machine-review: 2026-09-06
  validation: 2026-09-06
grounding:
  - "[[20_distillates/documents/tei-p5-guidelines-nd-4.12.0#^s32]]"
created: 2026-09-06
updated: 2026-09-06
---

# In TEI P5 4.12.0, the Guidelines allow any number of variant name forms within person, each with its language and kind, with no prioritization among them

## Statement

In TEI P5 4.12.0, the Guidelines state that persName is repeatable within person, with xml:lang for the language of the name and type for the kind of name. They contrast this with the library practice of accepting the form found in an authority file as the base or neutral form, note that people are often reluctant to accept an overtly foreign form of the name of a local saint or hero as neutral, and conclude that within person any number of variant forms can be given with no prioritization, as in the example of a scholar known by Icelandic, Danish and Latin forms of his name.

## Support

- [[20_distillates/documents/tei-p5-guidelines-nd-4.12.0#^s32]] — The chapter's treatment of name forms inside the record. It establishes that the record carries name forms as repeatable, typed and language-tagged children and that the Guidelines decline a base form, and it establishes nothing about how a form in the record relates to a nym.

## Related

- [[30_assertions/MOC-Metadata and Entities]]
- [[30_assertions/p5-person-description-elements-are-datable]]
