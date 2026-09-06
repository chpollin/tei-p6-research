---
type: distillate
source-type: document
representation: "[[10_markdown/documents/tei-p5-att.global.source-4.12.0]]"
topics: ["[[Metadata and Entities]]", "[[Elements and Classes]]"]
status: grounded
checked:
  validation: 2026-09-06
created: 2026-09-06
updated: 2026-09-06
---

# Distillate: TEI P5 4.12.0 att.global.source specification

This distillate reports the English class description, the English description of the `source` attribute and the four English remarks paragraphs of the complete `att.global.source.xml` specification at the pinned TEI P5 4.12.0 release commit.

## Core statements

- In TEI P5 4.12.0, `att.global.source` provides attributes used by elements to point to an external source. [[10_markdown/documents/tei-p5-att.global.source-4.12.0#^r1]] ^s1
- In TEI P5 4.12.0, the description of the `source` attribute in `att.global.source` states that it specifies the source from which some aspect of this element is drawn. [[10_markdown/documents/tei-p5-att.global.source-4.12.0#^r2]] ^s2
- In TEI P5 4.12.0, the English remarks on `source` state that the attribute points to an external source. [[10_markdown/documents/tei-p5-att.global.source-4.12.0#^r3]] ^s3
- In TEI P5 4.12.0, the English remarks on `source` state that when the attribute is used on an element describing a schema component (`classRef`, `dataRef`, `elementRef`, `macroRef`, `moduleRef`, or `schemaSpec`), it identifies the source from which declarations for the components should be obtained. [[10_markdown/documents/tei-p5-att.global.source-4.12.0#^r3]] ^s4
- In TEI P5 4.12.0, the English remarks on `source` state that on other elements the attribute provides a pointer to the bibliographical source from which a quotation or citation is drawn. [[10_markdown/documents/tei-p5-att.global.source-4.12.0#^r4]] ^s5
- In TEI P5 4.12.0, the English remarks on `source` state that in either case the location may be provided using any form of URI, for example an absolute URI, a relative URI, a private scheme URI of the form `tei:x.y.z`, or a private scheme URI that is expanded to an absolute URI as documented in a `prefixDef`. [[10_markdown/documents/tei-p5-att.global.source-4.12.0#^r5]] ^s6
- In TEI P5 4.12.0, the English remarks on `source` state that in the private scheme URI form `tei:x.y.z` the part `x.y.z` indicates the version number, for example `tei:4.3.2` for TEI P5 release 4.3.2 or, as a special case, `tei:current` for whatever is the latest release. [[10_markdown/documents/tei-p5-att.global.source-4.12.0#^r5]] ^s7
- In TEI P5 4.12.0, the English remarks on `source` state that when the attribute is used on elements describing schema components it should have only one value. [[10_markdown/documents/tei-p5-att.global.source-4.12.0#^r6]] ^s8
- In TEI P5 4.12.0, the English remarks on `source` state that when the attribute is used on other elements multiple values are permitted. [[10_markdown/documents/tei-p5-att.global.source-4.12.0#^r6]] ^s9

## Terms

- **att.global.source**: the specification that provides attributes used by elements to point to an external source. [[10_markdown/documents/tei-p5-att.global.source-4.12.0#^r1]]
- **source**: the attribute described as specifying the source from which some aspect of this element is drawn. [[10_markdown/documents/tei-p5-att.global.source-4.12.0#^r2]]
- **element describing a schema component**: `classRef`, `dataRef`, `elementRef`, `macroRef`, `moduleRef` or `schemaSpec`, on which the attribute identifies the source from which declarations for the components should be obtained. [[10_markdown/documents/tei-p5-att.global.source-4.12.0#^r3]]
- **bibliographical source**: on elements other than those describing a schema component, the source from which a quotation or citation is drawn and to which the attribute provides a pointer. [[10_markdown/documents/tei-p5-att.global.source-4.12.0#^r4]]
- **private scheme URI of the form `tei:x.y.z`**: a location form whose `x.y.z` part indicates the version number, with `tei:current` as the special case standing for whatever is the latest release. [[10_markdown/documents/tei-p5-att.global.source-4.12.0#^r5]]

## Open questions

- Which elements carry `source` at this release, and what do the XML-only declarations of this specification contribute, meaning `predeclare="true"`, `type="atts"`, `module="tei"` and the identifier `GBLSRC`, given that no English reading block names a member of the class or covers those declarations?
- Which source would establish the optionality and the value space of `source`, declared in this XML as `usage="opt"` with a `datatype` of one to unbounded `teidata.pointer` values, given that no English reading block states either?
- How does the recommendation that `source` have only one value on an element describing a schema component relate to the Schematron constraint `only_1_ODD_source` that this XML carries, given that the constraint and its report message appear in no English reading block?
- What would establish which usage the four English examples of this specification demonstrate, meaning the two examples that place `source` on `quote` and point it at a `bibl`, the `elementRef` with `source="tei:2.0.1"` and the `schemaSpec` with `source="mycompiledODD.xml"`, given that the example markup and the prose explaining the last two lie outside the English reading blocks?
- Which elements fall under the case the English remarks call other elements, given that the remarks bound the schema-component case by a list of six elements and leave the remaining case unbounded?
- How is a processor expected to treat several `source` values on an element other than one describing a schema component, given that the English remarks permit multiple values there without stating how the values combine or how a relative URI among them is resolved?
- Which record would establish why the list of elements describing a schema component corresponds to the membership named `tei:3.0.0_att.readFrom`, given that only an inert XML comment inside the remarks of this source names that relation?
- Which Guidelines chapters do the `listRef` pointers `#STGAso`, `#COHQQ` and `#TSBAWR` resolve to, and what do those chapters state about this class, given that only the XML of this source carries them?
- Which source would establish what the German and the Japanese descriptions and the Japanese remarks of this specification state and whether they agree with the English text, given that the reading blocks reproduce the English text alone?

## Appraisal

The source is the complete class specification at a pinned release commit, so its English text establishes that one attribute serves two distinct pointing tasks, obtaining declarations for schema components and citing the bibliographical source of a quotation or citation, and that the Guidelines set the value form as any URI including a private scheme with a release-version convention. It establishes nothing about which elements the class reaches and nothing about the datatype behind the value form. Where multiple values are permitted, it leaves open how they combine. The Schematron constraint, the examples and the non-English text stay outside the core statements until a reading block or another admitted source carries them.

## Related

- [[30_assertions/MOC-Metadata and Entities]]
- [[30_assertions/MOC-Elements and Classes]]
