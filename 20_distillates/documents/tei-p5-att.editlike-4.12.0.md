---
type: distillate
source-type: document
representation: "[[10_markdown/documents/tei-p5-att.editlike-4.12.0]]"
topics: ["[[Metadata and Entities]]", "[[Elements and Classes]]"]
status: validated
checked:
  machine-review: 2026-09-06
  validation: 2026-09-06
created: 2026-09-06
updated: 2026-09-06
---

# Distillate: TEI P5 4.12.0 att.editLike specification

This distillate reports the English class description, the two English attribute descriptions, the three English value descriptions and the two English remarks paragraphs of the complete `att.editLike.xml` specification at the pinned TEI P5 4.12.0 release commit.

## Core statements

- In TEI P5 4.12.0, the description of the attribute class `att.editLike` states that it "provides attributes describing the nature of an encoded scholarly intervention or interpretation of any kind." [[10_markdown/documents/tei-p5-att.editlike-4.12.0#^r1]] ^s1
- In TEI P5 4.12.0, the description of the `evidence` attribute in `att.editLike` states that it "indicates the nature of the evidence supporting the reliability or accuracy of the intervention or interpretation." [[10_markdown/documents/tei-p5-att.editlike-4.12.0#^r2]] ^s2
- In TEI P5 4.12.0, the description of the `evidence` value `internal` states that "there is internal evidence to support the intervention." [[10_markdown/documents/tei-p5-att.editlike-4.12.0#^r3]] ^s3
- In TEI P5 4.12.0, the description of the `evidence` value `external` states that "there is external evidence to support the intervention." [[10_markdown/documents/tei-p5-att.editlike-4.12.0#^r4]] ^s4
- In TEI P5 4.12.0, the description of the `evidence` value `conjecture` states that the intervention or interpretation has been made by the editor, cataloguer, or scholar "on the basis of their expertise." [[10_markdown/documents/tei-p5-att.editlike-4.12.0#^r5]] ^s5
- In TEI P5 4.12.0, the description of the `instant` attribute in `att.editLike` states that it "indicates whether this is an instant revision or not." [[10_markdown/documents/tei-p5-att.editlike-4.12.0#^r6]] ^s6
- In TEI P5 4.12.0, the English remarks on `att.editLike` state that the members of this attribute class are typically used to represent any kind of editorial intervention in a text, for example a correction or interpretation. [[10_markdown/documents/tei-p5-att.editlike-4.12.0#^r7]] ^s7
- In TEI P5 4.12.0, the English remarks on `att.editLike` state that the members of this attribute class are typically used to date or localize manuscripts etc. [[10_markdown/documents/tei-p5-att.editlike-4.12.0#^r7]] ^s8
- In TEI P5 4.12.0, the English remarks on `att.editLike` state that each pointer on the source, if present, corresponding to a witness or witness group should reference a bibliographic citation such as a `witness`, `msDesc`, or `bibl` element, or another external bibliographic citation, documenting the source concerned. [[10_markdown/documents/tei-p5-att.editlike-4.12.0#^r8]] ^s9

## Terms

- **att.editLike**: the attribute class described as providing attributes describing the nature of an encoded scholarly intervention or interpretation of any kind. [[10_markdown/documents/tei-p5-att.editlike-4.12.0#^r1]]
- **evidence**: the attribute described as indicating the nature of the evidence supporting the reliability or accuracy of the intervention or interpretation. [[10_markdown/documents/tei-p5-att.editlike-4.12.0#^r2]]
- **internal**: the `evidence` value described as there being internal evidence to support the intervention. [[10_markdown/documents/tei-p5-att.editlike-4.12.0#^r3]]
- **external**: the `evidence` value described as there being external evidence to support the intervention. [[10_markdown/documents/tei-p5-att.editlike-4.12.0#^r4]]
- **conjecture**: the `evidence` value described as an intervention or interpretation made by the editor, cataloguer, or scholar on the basis of their expertise. [[10_markdown/documents/tei-p5-att.editlike-4.12.0#^r5]]
- **instant**: the attribute described as indicating whether this is an instant revision or not. [[10_markdown/documents/tei-p5-att.editlike-4.12.0#^r6]]

## Open questions

- Which source would establish which elements and which classes are members of `att.editLike`, given that the English remarks speak of the members of this attribute class while the specification names no member and no English reading block carries a membership statement?
- Which source would establish what the XML-only declarations of `evidence` contribute, meaning the optional usage, the datatype `teidata.enumerated` with `maxOccurs="unbounded"` and the value list declared as `type="semi"`, given that no English reading block covers them?
- Whether an `evidence` value other than `internal`, `external` and `conjecture` is admissible and whether several values may be given at once, given that only the XML of this source declares the list type and the occurrence bound?
- Which source would establish what the XML-only declarations of `instant` contribute, meaning the datatype `teidata.xTruthValue` and the default value `false`, given that no English reading block covers them?
- What the word "this" refers to in the description of `instant`, and what makes a revision an "instant revision", given that no English reading block of this source explains the term?
- Where the source pointer named in the second English remarks paragraph is declared and what a value of it may point to, given that the English reading blocks of this specification describe `evidence` and `instant` alone?
- Which uses of the class lie outside those the English remarks call typical, given that the remarks qualify correction, interpretation, dating and localization with "typically" and close the list with "etc."?
- Which Guidelines chapters do the `listRef` pointers `#COED`, `#msdates`, `#NDPERSE` and `#PHCO` resolve to, and what do those chapters state about this class, given that only the XML of this source carries them?
- Which source would establish what the non-English descriptions and remarks of this specification state, given that the reading blocks reproduce the English text alone?

## Appraisal

The source is the complete class specification at a pinned release commit, so its English text establishes how the Guidelines describe an encoded scholarly intervention, the nature of the evidence behind it and the three named kinds of that evidence. It establishes nothing about which elements carry the attributes, because the specification declares no membership and the only English sentence about members says what members are typically used for. The remarks reach beyond the two attributes declared here by regulating pointers on a source attribute that this specification does not define, so the declaration of that attribute and the Guidelines chapters named in `listRef` remain to be established from other admitted sources.

## Related

- [[30_assertions/MOC-Metadata and Entities]]
- [[30_assertions/MOC-Elements and Classes]]
