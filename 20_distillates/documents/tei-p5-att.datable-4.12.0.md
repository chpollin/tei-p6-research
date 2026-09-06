---
type: distillate
source-type: document
representation: "[[10_markdown/documents/tei-p5-att.datable-4.12.0]]"
topics: ["[[Metadata and Entities]]", "[[Elements and Classes]]"]
status: grounded
checked:
  validation: 2026-09-06
created: 2026-09-06
updated: 2026-09-06
---

# Distillate: TEI P5 4.12.0 att.datable specification

This distillate reports the English class description, the English description of the one attribute this class defines and the English remarks in the complete `att.datable.xml` specification at the pinned TEI P5 4.12.0 release commit.

## Core statements

- In TEI P5 4.12.0, the description of the attribute class `att.datable` states that the class provides attributes for normalization of elements that contain dates, times, or datable events. [[10_markdown/documents/tei-p5-att.datable-4.12.0#^r1]] ^s1
- In TEI P5 4.12.0, the description of the `period` attribute in `att.datable` states that it supplies pointers to one or more definitions of named periods of time within which the datable item is understood to have occurred. [[10_markdown/documents/tei-p5-att.datable-4.12.0#^r2]] ^s2
- In TEI P5 4.12.0, the description of the `period` attribute in `att.datable` names `category`, `date` and `event` as the typical definitions of named periods of time that its pointers address. [[10_markdown/documents/tei-p5-att.datable-4.12.0#^r2]] ^s3
- In TEI P5 4.12.0, the English remarks on `att.datable` call the class a "superclass" that provides attributes which can be used to provide normalized values of temporal information. [[10_markdown/documents/tei-p5-att.datable-4.12.0#^r3]] ^s4
- In TEI P5 4.12.0, the English remarks on `att.datable` state that by default the attributes from the `att.datable.w3c` class are provided. [[10_markdown/documents/tei-p5-att.datable-4.12.0#^r3]] ^s5
- In TEI P5 4.12.0, the English remarks on `att.datable` state that if the module for names & dates is loaded, this class also provides attributes from the `att.datable.iso` and `att.datable.custom` classes. [[10_markdown/documents/tei-p5-att.datable-4.12.0#^r3]] ^s6
- In TEI P5 4.12.0, the English remarks on `att.datable` state that in general the possible values of attributes restricted to the W3C datatypes form a subset of those values available via the ISO 8601 standard. [[10_markdown/documents/tei-p5-att.datable-4.12.0#^r3]] ^s7
- In TEI P5 4.12.0, the English remarks on `att.datable` state that the greater expressiveness of the ISO datatypes may not be needed, and that there exists much greater software support for the W3C datatypes. [[10_markdown/documents/tei-p5-att.datable-4.12.0#^r3]] ^s8

## Terms

- **att.datable**: the attribute class described as providing attributes for normalization of elements that contain dates, times, or datable events. [[10_markdown/documents/tei-p5-att.datable-4.12.0#^r1]]
- **period**: the attribute described as supplying pointers to one or more definitions of named periods of time within which the datable item is understood to have occurred. [[10_markdown/documents/tei-p5-att.datable-4.12.0#^r2]]
- **superclass**: the word the English remarks use for `att.datable` as a provider of attributes for normalized values of temporal information. [[10_markdown/documents/tei-p5-att.datable-4.12.0#^r3]]

## Open questions

- Which source establishes the class memberships that only the XML of this specification declares, meaning the `memberOf` declarations for `att.datable.custom`, `att.datable.iso` and `att.datable.w3c`, given that no English reading block states a membership?
- Which source would establish the optionality and the value space of `period`, declared in this XML as `usage="opt"` with one to unbounded `teidata.pointer` values and covered by no English reading block?
- Which source would establish what the further XML-only declarations of this specification contribute, meaning the identifier `DATABLE`, the class type `atts`, the module `tei`, the version dates recorded on descriptions and remarks and the `listRef` pointers `#CONADA` and `#NDDATE`?
- Which source would establish which attributes actually carry the normalized temporal values, for instance a `calendar` attribute, given that this specification defines `period` as its only attribute and that no English reading block names any attribute of the three classes it draws on?
- Which normalized values may such an attribute take, given that the English text names the W3C datatypes and the ISO 8601 standard without naming a single value form?
- Which module is "the module for names & dates" that the English remarks make the condition for the additional attributes, given that no reading block names a module identifier?
- Which elements are members of `att.datable` at this release, given that this specification names no member element?
- Which source would establish the claim about software support, given that the English remarks assert much greater support for the W3C datatypes without naming an observation or a body of software?
- Which source would establish what the non-English descriptions and remarks of this specification state, given that the reading blocks reproduce the English text alone?

## Appraisal

The source is the complete class specification at a pinned release commit, so its English text establishes how the Guidelines position one dating superclass, meaning that it normalizes temporal information, that the W3C attributes come by default, and that the ISO and custom attributes depend on loading the module for names and dates. The English text names no attribute of those three classes and states no value form, so everything an encoder would write into a normalized date stays outside this source. The comparison of the W3C and ISO datatypes is stated as a general tendency together with an unsourced claim about software support, so it records a position of the Guidelines and leaves the underlying facts to be established elsewhere. The declarations preserved in the XML stay outside the core statements until a reading block or another admitted source carries them.

## Related

- [[30_assertions/MOC-Metadata and Entities]]
- [[30_assertions/MOC-Elements and Classes]]
