---
type: assertion
topics: ["[[Metadata and Entities]]", "[[Abstract Model]]"]
phenomena: ["[[glossary/statement-about-an-entity]]"]
related: ["[[40_output/12-p6-design]]", "[[30_assertions/p5-each-statement-about-a-life-must-be-documentable-and-time-framed]]"]
status: validated
checked:
  machine-review: 2026-09-06
  validation: 2026-09-06
grounding:
  - "[[20_distillates/documents/tei-p5-guidelines-nd-4.12.0#^s37]]"
created: 2026-09-06
updated: 2026-09-06
---

# In TEI P5 4.12.0, the generic description elements carry cert, resp, evidence and source through att.global.responsibility and att.editLike, so that conflicting sources can yield more than one view of what happened

## Statement

In TEI P5 4.12.0, the Guidelines state that the generic elements are members of att.global.responsibility and att.editLike, which make available cert for the degree of certainty, resp for the agency responsible, evidence for the nature of the evidence used and source as a pointer to the resource from which the information derives, so that in the case of multiple and conflicting sources more than one view of what happened can be provided, as in the example of two event elements of type birth with different places, dates, responsible agents and certainty values.

## Support

- [[20_distillates/documents/tei-p5-guidelines-nd-4.12.0#^s37]] — The attribution attributes as the chapter presents them and the coexistence of conflicting statements in its example. The class specifications are not among the sources, and the statement says nothing about withdrawing a statement or about relating two conflicting ones to each other.

## Related

- [[30_assertions/MOC-Metadata and Entities]]
- [[30_assertions/MOC-Abstract Model]]
- [[30_assertions/p5-each-statement-about-a-life-must-be-documentable-and-time-framed]]
