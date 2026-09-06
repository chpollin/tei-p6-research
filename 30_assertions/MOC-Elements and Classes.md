---
type: moc
topic: "Elements and Classes"
created: 2026-09-04
updated: 2026-09-06
---

# MOC: Elements and Classes

This map gathers grounded statements about elements, attributes, model classes,
attribute classes, macros, datatypes and their inheritance relations.

## Sources and distillates

<!-- distillates:begin -->
- [[20_distillates/documents/tei-p5-att.canonical-4.12.0]]
- [[20_distillates/documents/tei-p5-att.datable-4.12.0]]
- [[20_distillates/documents/tei-p5-att.editlike-4.12.0]]
- [[20_distillates/documents/tei-p5-att.global.responsibility-4.12.0]]
- [[20_distillates/documents/tei-p5-att.global.source-4.12.0]]
- [[20_distillates/documents/tei-p5-att.naming-4.12.0]]
- [[20_distillates/documents/tei-p5-att.personal-4.12.0]]
- [[20_distillates/documents/tei-p5-guidelines-nd-4.12.0]]
- [[20_distillates/documents/tei-p5-person-4.12.0]]
- [[20_distillates/publications/teic-tei-issue-2739]]
- [[20_distillates/publications/teic-tei-issue-337]]
<!-- distillates:end -->

## Assertions

<!-- assertions:begin -->
- [[30_assertions/p5-att-canonical-associates-a-name-with-canonical-information-about-its-object]] — In TEI P5 4.12.0, att.canonical associates a representation such as a name or title with canonical information about the object being named or referenced
- [[30_assertions/p5-att-canonical-gives-no-precedence-when-key-and-ref-co-occur]] — In TEI P5 4.12.0, att.canonical provides no semantic basis and suggests no precedence when both key and ref are supplied
- [[30_assertions/p5-att-datable-provides-attributes-for-normalization-of-elements-that-contain-dates-times-or-datable-events]] — In TEI P5 4.12.0, the description of att.datable states that the class provides attributes for normalization of elements that contain dates, times, or datable events
- [[30_assertions/p5-att-global-responsibility-indicates-the-agent-responsible-for-something-asserted-by-the-markup]] — In TEI P5 4.12.0, the description of att.global.responsibility states that the class provides attributes indicating the agent responsible for some aspect of the text, the markup or something asserted by the markup
- [[30_assertions/p5-att-naming-describes-nymref-through-the-object-named]] — In TEI P5 4.12.0, att.naming describes nymRef as locating the canonical form of the names associated with the object named by the element bearing it
- [[30_assertions/p5-att-naming-inherits-key-and-ref-and-prefers-a-direct-link]] — In TEI P5 4.12.0, att.naming inherits key and ref from att.canonical as two ways of associating a name with its referent, and ref is to be used wherever a direct link to canonical information about the referent can be supplied
- [[30_assertions/p5-att-personal-provides-common-attributes-for-elements-forming-part-of-a-name]] — In TEI P5 4.12.0, the description of att.personal states that the class provides common attributes for those elements which form part of a name, usually but not necessarily a personal name
- [[30_assertions/p5-evidence-indicates-the-nature-of-the-evidence-supporting-an-intervention-or-interpretation]] — In TEI P5 4.12.0, the description of evidence in att.editLike states that it indicates the nature of the evidence supporting the reliability or accuracy of the intervention or interpretation
- [[30_assertions/p5-key-identifies-the-entity-named-through-an-externally-defined-coded-value]] — In TEI P5 4.12.0, the key attribute of att.canonical provides an externally defined means of identifying the entity or entities being named, using a coded value of some kind
- [[30_assertions/p5-key-remarks-propose-no-particular-syntax-because-its-form-depends-on-project-practice]] — In TEI P5 4.12.0, the English remarks on key propose no particular syntax for the values of the attribute, because its form will depend entirely on practice within a given project
- [[30_assertions/p5-key-requires-resolution-documentation-for-interchange]] — In TEI P5 4.12.0, the use of key in interchange requires that documentation about how the key is to be resolved be sent to the recipient
- [[30_assertions/p5-ref-locates-a-definition-or-identity-for-the-entity-named-by-uris]] — In TEI P5 4.12.0, the ref attribute of att.canonical provides an explicit means of locating a full definition or identity for the entity being named by means of one or more URIs
- [[30_assertions/p5-ref-points-directly-to-xml-elements-or-other-resources]] — In TEI P5 4.12.0, the English remarks on the ref attribute require its value to point directly to one or more XML elements or other resources by means of one or more whitespace-separated URIs
- [[30_assertions/p5-resp-should-point-to-an-element-that-clarifies-the-agents-role-rather-than-to-a-person-or-org]] — In TEI P5 4.12.0, the English remarks on resp in att.global.responsibility recommend pointing resp to a respStmt, an author, an editor or a similar element which clarifies the exact role played by the agent, and advise against pointing it to a person or an org
- [[30_assertions/p5-role-on-a-naming-element-carries-information-about-the-entity-referenced]] — In TEI P5 4.12.0, the role attribute of att.naming may specify further information about the entity referenced by the name, such as the occupation of a person or the status of a place
- [[30_assertions/p5-simultaneous-key-and-ref-are-not-recommended-without-documentation]] — In TEI P5 4.12.0, the English remarks on att.canonical state that the simultaneous use of both key and ref is not recommended unless documentation explaining the use is provided for interchange, probably in an ODD customization
- [[30_assertions/p5-source-specifies-the-source-from-which-some-aspect-of-an-element-is-drawn]] — In TEI P5 4.12.0, the description of source in att.global.source states that it specifies the source from which some aspect of this element is drawn
- [[30_assertions/teic-tei-issue-2739-commenter-states-att-personal-is-a-member-of-att-naming-and-att-naming-of-att-canonical]] — In TEIC/TEI issue 2739, a commenter stated that att.personal is a member of att.naming and that att.naming is a member of att.canonical
- [[30_assertions/teic-tei-issue-337-author-reports-a-wish-to-deprecate-key-held-back-by-its-wide-use]] — In TEIC/TEI issue 337, the issue author reported a wish to deprecate key some day, held back by how widely the attribute was used at the time of writing
<!-- assertions:end -->

## Open questions

- Where does the P5 class system produce semantically motivated reuse, and where does
  it carry forward historically contingent complexity?
