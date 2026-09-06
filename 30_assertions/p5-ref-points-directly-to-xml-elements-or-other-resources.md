---
type: assertion
topics: ["[[Metadata and Entities]]", "[[Elements and Classes]]"]
phenomena: ["[[glossary/entity-identification]]"]
related: ["[[40_output/12-p6-design]]", "[[30_assertions/p5-ref-locates-a-definition-or-identity-for-the-entity-named-by-uris]]", "[[30_assertions/p5-prosopography-records-refer-to-external-authorities-through-idno]]"]
status: validated
checked:
  machine-review: 2026-09-06
  validation: 2026-09-06
grounding:
  - "[[20_distillates/documents/tei-p5-att.canonical-4.12.0#^s6]]"
created: 2026-09-06
updated: 2026-09-06
---

# In TEI P5 4.12.0, the English remarks on the ref attribute require its value to point directly to one or more XML elements or other resources by means of one or more whitespace-separated URIs

## Statement

In TEI P5 4.12.0, the English remarks on the ref attribute require the value of the attribute to point directly to one or more XML elements or other resources by means of one or more URIs, separated by whitespace.

## Support

- [[20_distillates/documents/tei-p5-att.canonical-4.12.0#^s6]] — The English remarks on the value. They establish that a target may be an element inside a TEI document or a resource outside it and that several targets are written as one whitespace-separated value, and they state nothing about schema-level enforcement.

## Related

- [[30_assertions/MOC-Metadata and Entities]]
- [[30_assertions/MOC-Elements and Classes]]
- [[30_assertions/p5-ref-locates-a-definition-or-identity-for-the-entity-named-by-uris]]
