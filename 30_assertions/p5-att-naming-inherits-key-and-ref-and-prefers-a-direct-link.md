---
type: assertion
topics: ["[[Metadata and Entities]]", "[[Elements and Classes]]"]
phenomena: ["[[glossary/entity-identification]]", "[[glossary/mention-of-an-entity]]"]
related: ["[[40_output/12-p6-design]]", "[[30_assertions/p5-key-serves-cases-where-no-direct-link-is-required]]", "[[30_assertions/p5-att-canonical-gives-no-precedence-when-key-and-ref-co-occur]]", "[[30_assertions/teic-tei-issue-2739-commenter-states-att-personal-is-a-member-of-att-naming-and-att-naming-of-att-canonical]]", "[[30_assertions/p5-att-personal-provides-common-attributes-for-elements-forming-part-of-a-name]]"]
status: validated
checked:
  machine-review: 2026-09-06
  validation: 2026-09-06
grounding:
  - "[[20_distillates/documents/tei-p5-guidelines-nd-4.12.0#^s3]]"
created: 2026-09-06
updated: 2026-09-06
---

# In TEI P5 4.12.0, att.naming inherits key and ref from att.canonical as two ways of associating a name with its referent, and ref is to be used wherever a direct link to canonical information about the referent can be supplied

## Statement

In TEI P5 4.12.0, the Guidelines state that att.naming is a subclass of att.canonical, from which it inherits key and ref as two different ways of associating any sort of name with its referent, and that att.naming adds a simple role attribute for minimal information about the person named and a nymRef attribute for associating the name itself with a base or canonical form. They state that ref should be used wherever it is possible to supply a direct link such as a URI to the location of canonical information about the referent, which requires that a person element with that identifier exist somewhere, possibly in another document, and that more than one URI may be supplied where the name refers to more than one person.

## Support

- [[20_distillates/documents/tei-p5-guidelines-nd-4.12.0#^s3]] — The chapter's account of the class relation and its recommendation. The subclass relation is declared in the class XML, which no reading block of the class specification reproduces, so this statement is the only anchorable evidence for it.

## Related

- [[30_assertions/MOC-Metadata and Entities]]
- [[30_assertions/MOC-Elements and Classes]]
- [[30_assertions/p5-key-serves-cases-where-no-direct-link-is-required]]
