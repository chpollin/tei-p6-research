---
type: glossary
term: "Entity identification"
created: 2026-09-06
updated: 2026-09-06
---

# Entity identification

Entity identification links a mention in a text, or a record about an entity, to the entity it
stands for or to an external authority, through a coded identifier or a URI. In TEI P5 4.12.0
the attributes `key` and `ref` of `att.canonical` serve this purpose on a name or referring
string.
[[10_markdown/documents/tei-p5-att.canonical-4.12.0#^r1]]

## Examples

<!-- examples:begin -->
- [[30_assertions/p5-att-canonical-associates-a-name-with-canonical-information-about-its-object]] — In TEI P5 4.12.0, att.canonical associates a representation such as a name or title with canonical information about the object being named or referenced
  - [[20_distillates/documents/tei-p5-att.canonical-4.12.0#^s1]]
- [[30_assertions/p5-att-canonical-gives-no-precedence-when-key-and-ref-co-occur]] — In TEI P5 4.12.0, att.canonical provides no semantic basis and suggests no precedence when both key and ref are supplied
  - [[20_distillates/documents/tei-p5-att.canonical-4.12.0#^s10]]
- [[30_assertions/p5-att-naming-describes-nymref-through-the-object-named]] — In TEI P5 4.12.0, att.naming describes nymRef as locating the canonical form of the names associated with the object named by the element bearing it
  - [[20_distillates/documents/tei-p5-att.naming-4.12.0#^s3]]
- [[30_assertions/p5-att-naming-inherits-key-and-ref-and-prefers-a-direct-link]] — In TEI P5 4.12.0, att.naming inherits key and ref from att.canonical as two ways of associating a name with its referent, and ref is to be used wherever a direct link to canonical information about the referent can be supplied
  - [[20_distillates/documents/tei-p5-guidelines-nd-4.12.0#^s3]]
- [[30_assertions/p5-guidelines-detach-the-nymref-association-from-the-entity-named]] — In TEI P5 4.12.0, the Guidelines state that the association nymRef makes with a nym has nothing to do with any individual who might use the name
  - [[20_distillates/documents/tei-p5-guidelines-nd-4.12.0#^s56]]
- [[30_assertions/p5-guidelines-distinguish-resolving-a-name-from-treating-it-as-an-object]] — In TEI P5 4.12.0, the Guidelines distinguish the resolution of a name or referring string to its referent through key or ref from the treatment of names as objects in their own right, for whose canonical or normalized form they use the term nym
  - [[20_distillates/documents/tei-p5-guidelines-nd-4.12.0#^s55]]
- [[30_assertions/p5-guidelines-present-three-encodings-of-a-nationality-as-the-same-information]] — In TEI P5 4.12.0, the Guidelines present a generic state of type nationality, a nationality element with the same text and an empty nationality element carrying a key and the dating attribute as encodings of the same information
  - [[20_distillates/documents/tei-p5-guidelines-nd-4.12.0#^s33]]
- [[30_assertions/p5-key-identifies-the-entity-named-through-an-externally-defined-coded-value]] — In TEI P5 4.12.0, the key attribute of att.canonical provides an externally defined means of identifying the entity or entities being named, using a coded value of some kind
  - [[20_distillates/documents/tei-p5-att.canonical-4.12.0#^s2]]
- [[30_assertions/p5-key-requires-resolution-documentation-for-interchange]] — In TEI P5 4.12.0, the use of key in interchange requires that documentation about how the key is to be resolved be sent to the recipient
  - [[20_distillates/documents/tei-p5-att.canonical-4.12.0#^s8]]
- [[30_assertions/p5-key-serves-cases-where-no-direct-link-is-required]] — In TEI P5 4.12.0, key serves cases where no direct link is required, because a local convention resolves the reference or because the encoder judges that no resolution is necessary
  - [[20_distillates/documents/tei-p5-guidelines-nd-4.12.0#^s4]]
- [[30_assertions/p5-persname-is-synonymous-with-name-of-type-person]] — In TEI P5 4.12.0, the Guidelines hold persName synonymous with name of type person apart from its own type attribute and treat encodings of one name with rs, name or persName under the same ref as equivalent
  - [[20_distillates/documents/tei-p5-guidelines-nd-4.12.0#^s8]]
- [[30_assertions/p5-prosopography-records-refer-to-external-authorities-through-idno]] — In TEI P5 4.12.0, the Guidelines state that a prosopography record of a named entity commonly refers explicitly to other resources such as name authority files, a gazetteer or a printed book, and follow that statement with a specList naming idno with its type attribute
  - [[20_distillates/documents/tei-p5-guidelines-nd-4.12.0#^s25]]
- [[30_assertions/p5-ref-locates-a-definition-or-identity-for-the-entity-named-by-uris]] — In TEI P5 4.12.0, the ref attribute of att.canonical provides an explicit means of locating a full definition or identity for the entity being named by means of one or more URIs
  - [[20_distillates/documents/tei-p5-att.canonical-4.12.0#^s5]]
- [[30_assertions/p5-ref-points-directly-to-xml-elements-or-other-resources]] — In TEI P5 4.12.0, the English remarks on the ref attribute require its value to point directly to one or more XML elements or other resources by means of one or more whitespace-separated URIs
  - [[20_distillates/documents/tei-p5-att.canonical-4.12.0#^s6]]
- [[30_assertions/p5-simultaneous-key-and-ref-are-not-recommended-without-documentation]] — In TEI P5 4.12.0, the English remarks on att.canonical state that the simultaneous use of both key and ref is not recommended unless documentation explaining the use is provided for interchange, probably in an ODD customization
  - [[20_distillates/documents/tei-p5-att.canonical-4.12.0#^s11]]
<!-- examples:end -->
