---
type: assertion
topics: ["[[Metadata and Entities]]", "[[Abstract Model]]"]
phenomena: ["[[glossary/statement-about-an-entity]]", "[[glossary/responsibility-for-a-statement]]"]
related: ["[[40_output/12-p6-design]]", "[[30_assertions/p5-generic-description-elements-carry-certainty-and-responsibility]]", "[[30_assertions/p5-each-statement-about-a-life-must-be-documentable-and-time-framed]]", "[[30_assertions/p5-guidelines-use-generic-state-trait-and-event-customized-through-type-for-information-about-a-place]]", "[[30_assertions/p5-att-global-responsibility-indicates-the-agent-responsible-for-something-asserted-by-the-markup]]"]
status: validated
checked:
  machine-review: 2026-09-06
  validation: 2026-09-06
grounding:
  - "[[20_distillates/documents/tei-p5-guidelines-nd-4.12.0#^s50]]"
created: 2026-09-06
updated: 2026-09-06
---

# In TEI P5 4.12.0, the Guidelines state that state, trait and other elements of the same class can be nested hierarchically with type values cumulatively inherited, that responsibility is not additive so an element either states it explicitly or inherits it from its nearest ancestor, and that a child element may specify a date more precisely than its parent

## Statement

In TEI P5 4.12.0, the Guidelines state that state, trait and other elements of the same class can be nested hierarchically with type values understood as cumulatively inherited, that responsibility is not an additive property so that an element either states it explicitly or inherits it from its nearest ancestor, and that dating differs again in that a child element may specify a date more precisely than its parent.

## Support

- [[20_distillates/documents/tei-p5-guidelines-nd-4.12.0#^s50]] — The chapter's rule for nested statement elements, stated in its section on places. It establishes three different inheritance behaviours for the type, the responsibility and the date of a statement, and it states nothing about what applies where a child's date falls outside its parent's range or about the documentation of a statement.

## Related

- [[30_assertions/MOC-Metadata and Entities]]
- [[30_assertions/MOC-Abstract Model]]
- [[30_assertions/p5-generic-description-elements-carry-certainty-and-responsibility]]
- [[30_assertions/p5-att-global-responsibility-indicates-the-agent-responsible-for-something-asserted-by-the-markup]]
