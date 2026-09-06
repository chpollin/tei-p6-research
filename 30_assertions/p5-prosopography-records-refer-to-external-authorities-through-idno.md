---
type: assertion
topics: ["[[Metadata and Entities]]"]
phenomena: ["[[glossary/entity-record]]", "[[glossary/entity-identification]]"]
related: ["[[40_output/12-p6-design]]", "[[30_assertions/p5-ref-locates-a-definition-or-identity-for-the-entity-named-by-uris]]", "[[30_assertions/p5-idno-supplies-any-form-of-identifier-used-to-identify-some-object-in-a-standardized-way]]", "[[30_assertions/teic-tei-issue-1414-commenter-summarizes-idno-as-a-first-child-of-the-record-elements-as-the-short-term-solution]]"]
status: validated
checked:
  machine-review: 2026-09-06
  validation: 2026-09-06
grounding:
  - "[[20_distillates/documents/tei-p5-guidelines-nd-4.12.0#^s25]]"
created: 2026-09-06
updated: 2026-09-06
---

# In TEI P5 4.12.0, the Guidelines state that a prosopography record of a named entity commonly refers explicitly to other resources such as name authority files, a gazetteer or a printed book, and follow that statement with a specList naming idno with its type attribute

## Statement

In TEI P5 4.12.0, the Guidelines state that when developing a prosopography record of a named entity it is a common practice to refer explicitly to other resources, naming the Library of Congress Name Authority File, the Virtual International Authority File, a gazetteer of places like Pleiades and a printed book as examples, and follow that statement with a specList naming idno with its type attribute.

## Support

- [[20_distillates/documents/tei-p5-guidelines-nd-4.12.0#^s25]] — The link from the record to an external authority as the chapter describes it, as distinct from the link a name in a text makes through key or ref. The statement places the specList for idno after the practice it describes and states no purpose for the element in prose, so the use of idno for these references rests on that juxtaposition.

## Related

- [[30_assertions/MOC-Metadata and Entities]]
- [[30_assertions/p5-ref-locates-a-definition-or-identity-for-the-entity-named-by-uris]]
