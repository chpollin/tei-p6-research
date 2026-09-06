---
type: distillate
source-type: document
representation: "[[10_markdown/documents/tei-p5-att.canonical-4.12.0]]"
topics: ["[[Metadata and Entities]]", "[[Elements and Classes]]"]
status: validated
checked:
  machine-review: 2026-09-06
  validation: 2026-09-06
created: 2026-09-06
updated: 2026-09-06
---

# Distillate: TEI P5 4.12.0 att.canonical specification

This distillate reports the English descriptions and the English remarks of the complete `att.canonical.xml` specification at the pinned TEI P5 4.12.0 release commit.

## Core statements

- In TEI P5 4.12.0, `att.canonical` provides attributes that can be used to associate a representation such as a name or title with canonical information about the object being named or referenced. [[10_markdown/documents/tei-p5-att.canonical-4.12.0#^r1]] ^s1
- In TEI P5 4.12.0, the `key` attribute of `att.canonical` provides an externally-defined means of identifying the entity or entities being named, using a coded value of some kind. [[10_markdown/documents/tei-p5-att.canonical-4.12.0#^r2]] ^s2
- In TEI P5 4.12.0, the English remarks on `key` state that the value may be a unique identifier from a database, or any other externally-defined string identifying the referent. [[10_markdown/documents/tei-p5-att.canonical-4.12.0#^r3]] ^s3
- In TEI P5 4.12.0, the English remarks on `key` propose no particular syntax for the values of the attribute, because its form will depend entirely on practice within a given project. [[10_markdown/documents/tei-p5-att.canonical-4.12.0#^r3]] ^s4
- In TEI P5 4.12.0, the `ref` attribute of `att.canonical` provides an explicit means of locating a full definition or identity for the entity being named by means of one or more URIs. [[10_markdown/documents/tei-p5-att.canonical-4.12.0#^r4]] ^s5
- In TEI P5 4.12.0, the English remarks on `ref` require the value to point directly to one or more XML elements or other resources by means of one or more URIs, separated by whitespace. [[10_markdown/documents/tei-p5-att.canonical-4.12.0#^r5]] ^s6
- In TEI P5 4.12.0, the English remarks on `ref` state that supplying more than one URI carries the implication that the name identifies several distinct entities. [[10_markdown/documents/tei-p5-att.canonical-4.12.0#^r5]] ^s7
- In TEI P5 4.12.0, the English remarks on `att.canonical` state that `key` is more flexible and general-purpose, and that its use in interchange requires that documentation about how the key is to be resolved be sent to the recipient of the TEI document. [[10_markdown/documents/tei-p5-att.canonical-4.12.0#^r6]] ^s8
- In TEI P5 4.12.0, the English remarks on `att.canonical` state that values of `ref` are resolved using the widely accepted protocols for a URI, and that less documentation, if any, is therefore likely required by the recipient in data interchange. [[10_markdown/documents/tei-p5-att.canonical-4.12.0#^r6]] ^s9
- In TEI P5 4.12.0, the English remarks on `att.canonical` state that these guidelines provide no semantic basis and no suggested precedence when both `key` and `ref` are provided. [[10_markdown/documents/tei-p5-att.canonical-4.12.0#^r7]] ^s10
- In TEI P5 4.12.0, the English remarks on `att.canonical` state that simultaneous use of both `key` and `ref` is not recommended unless documentation explaining the use is provided for interchange, probably in an ODD customization. [[10_markdown/documents/tei-p5-att.canonical-4.12.0#^r7]] ^s11

## Terms

- **att.canonical**: the specification that provides attributes which can be used to associate a representation such as a name or title with canonical information about the object being named or referenced. [[10_markdown/documents/tei-p5-att.canonical-4.12.0#^r1]]
- **key**: the attribute that provides an externally-defined means of identifying the entity or entities being named, using a coded value of some kind. [[10_markdown/documents/tei-p5-att.canonical-4.12.0#^r2]]
- **ref**: the attribute that provides an explicit means of locating a full definition or identity for the entity being named by means of one or more URIs. [[10_markdown/documents/tei-p5-att.canonical-4.12.0#^r4]]

## Open questions

- Which source establishes which elements and which classes are members of `att.canonical` at this release, given that this specification names no member and no English reading block of it carries a membership statement?
- Which source would establish what the XML-only declarations of this specification contribute, meaning the datatype `teidata.text` for `key`, the one to unbounded `teidata.pointer` values for `ref`, the optional usage of both attributes, the identifier `class-attr-canonical`, the module the specification names and its `listRef` pointer, given that no English reading block covers them?
- What would establish which usage the three English examples of this specification demonstrate, meaning the one example under `key`, the one example under `ref` and the contrived example in which a canonical reference to the same organisation is provided in four different ways, given that the prose explaining the last of them lies outside the English reading blocks?
- Within which scope must a `key` value be unique, given that the English remarks say only that the value may be a unique identifier from a database or any other externally-defined string identifying the referent?
- Which source would establish how a processor is expected to behave when `key` and `ref` appear together, given that this specification states no semantic basis and no precedence for that case?
- Which record would establish when the English passage now held as an inert XML comment inside the class remarks, which mentions data interchange and a tag URI as defined in RFC 4151, left the remarks text, given that only the XML of this source carries it?
- Which source would establish what the non-English descriptions and remarks of this specification state, given that the reading blocks reproduce the English text alone?

## Appraisal

The source is the complete class specification at a pinned release commit, so its English text establishes what the Guidelines say about identifying an entity through a coded key or through a URI, and about the documentation each of the two places on a recipient in interchange. It establishes nothing about which elements carry these attributes and nothing about whether a key resolves outside the project that minted it. The declarations preserved in the XML and the prose explaining the examples stay outside the core statements until a reading block or another admitted source carries them.

## Related

- [[30_assertions/MOC-Metadata and Entities]]
- [[30_assertions/MOC-Elements and Classes]]
