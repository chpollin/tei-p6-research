---
type: assertion
topics: ["[[Metadata and Entities]]", "[[Elements and Classes]]"]
phenomena: ["[[glossary/entity-identification]]", "[[glossary/mention-of-an-entity]]"]
related: ["[[40_output/12-p6-design]]", "[[30_assertions/p5-key-serves-cases-where-no-direct-link-is-required]]", "[[30_assertions/p5-att-canonical-gives-no-precedence-when-key-and-ref-co-occur]]", "[[30_assertions/teic-tei-issue-2739-commenter-states-att-personal-is-a-member-of-att-naming-and-att-naming-of-att-canonical]]", "[[30_assertions/p5-att-personal-provides-common-attributes-for-elements-forming-part-of-a-name]]"]
status: grounded
checked: {}
grounding:
  - "[[20_distillates/documents/tei-p5-guidelines-nd-4.12.0#^s3]]"
created: 2026-09-06
updated: 2026-09-11
---

# The P5 4.12.0 Guidelines describe att.naming as inheriting key and ref and recommend ref wherever a direct link can be supplied

## Statement

In TEI P5 4.12.0, the Guidelines state that att.naming is a subclass of att.canonical, from which it inherits key and ref as two different ways of associating any sort of name with its referent, and that att.naming also provides a simple role attribute for cases where all that is required is some minimal information about the person name, for example their occupation or status, and a nymRef attribute that allows the name itself to be associated with a base or canonical form. They state that ref should be used wherever it is possible to supply a direct link such as a URI to indicate the location of canonical information about the referent, that their example encoding with ref="#DPB1" requires that there exist somewhere a person element with the identifier DPB1, which might alternatively be provided by some other document referred to by means of a URI, and that more than one URI may be supplied if the name refers to more than one person.

## Support

- [[20_distillates/documents/tei-p5-guidelines-nd-4.12.0#^s3]] — The chapter's account of the class relation, its recommendation for ref and its example encoding. The requirement of a person element is stated for that example encoding.

## Related

- [[30_assertions/MOC-Metadata and Entities]]
- [[30_assertions/MOC-Elements and Classes]]
- [[30_assertions/p5-key-serves-cases-where-no-direct-link-is-required]]
