---
type: distillate
source-type: document
representation: "[[10_markdown/documents/tei-p5-att.personal-4.12.0]]"
topics: ["[[Metadata and Entities]]", "[[Elements and Classes]]"]
status: grounded
checked:
  validation: 2026-09-06
created: 2026-09-06
updated: 2026-09-06
---

# Distillate: TEI P5 4.12.0 att.personal specification

This distillate reports the English class description together with the English attribute and value descriptions of the complete `att.personal.xml` specification at the pinned TEI P5 4.12.0 release commit.

## Core statements

- In TEI P5 4.12.0, the description of the attribute class `att.personal` states that the class provides "common attributes for those elements which form part of a name usually, but not necessarily, a personal name." [[10_markdown/documents/tei-p5-att.personal-4.12.0#^r1]] ^s1
- In TEI P5 4.12.0, the description of `att.personal` qualifies the name whose part those elements form as "usually, but not necessarily, a personal name." [[10_markdown/documents/tei-p5-att.personal-4.12.0#^r1]] ^s2
- In TEI P5 4.12.0, the description of the `full` attribute in `att.personal` states that it indicates whether the name component is given in full, as an abbreviation or simply as an initial. [[10_markdown/documents/tei-p5-att.personal-4.12.0#^r2]] ^s3
- In TEI P5 4.12.0, the description of the value `yes` of the `full` attribute states that the name component is spelled out in full. [[10_markdown/documents/tei-p5-att.personal-4.12.0#^r3]] ^s4
- In TEI P5 4.12.0, the description of the value `abb` of the `full` attribute states that the name component is given in an abbreviated form. [[10_markdown/documents/tei-p5-att.personal-4.12.0#^r4]] ^s5
- In TEI P5 4.12.0, the description of the value `init` of the `full` attribute states that the name component is indicated only by one initial. [[10_markdown/documents/tei-p5-att.personal-4.12.0#^r5]] ^s6
- In TEI P5 4.12.0, the description of the `sort` attribute in `att.personal` states that it specifies the sort order of the name component in relation to others within the name. [[10_markdown/documents/tei-p5-att.personal-4.12.0#^r6]] ^s7

## Terms

- **att.personal**: the attribute class described as providing common attributes for those elements which form part of a name usually, but not necessarily, a personal name. [[10_markdown/documents/tei-p5-att.personal-4.12.0#^r1]]
- **full**: the attribute described as indicating whether the name component is given in full, as an abbreviation or simply as an initial. [[10_markdown/documents/tei-p5-att.personal-4.12.0#^r2]]
- **sort**: the attribute described as specifying the sort order of the name component in relation to others within the name. [[10_markdown/documents/tei-p5-att.personal-4.12.0#^r6]]

## Open questions

- Which source would establish the effect of the `memberOf key="att.naming"` declaration, which this specification carries in the `classes` element of its XML and in no English reading block, and which therefore leaves the route from a name-part element to `att.naming` unstated in the English text?
- Which source would establish whether the attributes of `att.canonical` reach an element that carries `att.personal`, given that this specification mentions `att.canonical` nowhere and declares its own membership only in the XML?
- Which source would establish which elements are members of `att.personal`, given that this specification names no member element and its English description identifies the carrying elements only by the function of forming part of a name?
- Which source would establish that `full` and `sort` are the complete set of attributes this class provides, given that only the `attList` element of the XML enumerates them and no English reading block states how many attributes there are?
- Which source would establish the optionality, the datatypes and the default of the two attributes, declared in this XML as `usage="opt"` with `teidata.enumerated` and the default value `yes` for `full` and as `usage="opt"` with `teidata.count` for `sort`, and covered by no English reading block?
- Which source would establish that the value list of `full` is closed and holds exactly `yes`, `abb` and `init`, given that only the `valList type="closed"` element of the XML declares this?
- Which source would establish what the class-level XML declarations of this specification contribute, meaning `module="tei"`, `type="atts"` and `ident="att.personal"`, and which Guidelines chapter the `listRef` pointer `#NDPER` resolves to?
- What do the English glosses of this specification contribute, meaning the class gloss "attributes for components of names usually, but not necessarily, personal names", the gloss "sort" on the `sort` attribute and the value glosses "yes", "abbreviated" and "initial letter", given that the reading blocks reproduce descriptions and remarks alone?
- Which source would establish what the non-English glosses and descriptions of this specification state, given that the reading blocks reproduce the English text alone?
- What counts as a "name component", and which elements realize one, given that the English text of this specification uses the term in every description without defining it?
- How is a `sort` value to be read, meaning from which end of the name the order is counted and whether the values of the components of one name must be contiguous, given that the English text states only that the attribute specifies the sort order of the name component in relation to others within the name?
- Which source carries remarks on `att.personal`, given that this specification holds no remarks element and its English text consists of the class description, the two attribute descriptions and the three value descriptions?

## Appraisal

The source is the complete class specification at a pinned release commit, so its English text establishes what the Guidelines say about the two attributes a name part may carry, the form in which that part is given and its position in the sort order of the name. The membership that makes this class the route from a name-part element to `att.naming` lives in the XML alone, so no English reading block of this source can carry it, and the elements at the other end of that route are named nowhere in the specification. Everything the specification fixes about optionality, datatypes, the default value and the closed value list stays outside the core statements until a reading block or another admitted source carries it.

## Related

- [[30_assertions/MOC-Metadata and Entities]]
- [[30_assertions/MOC-Elements and Classes]]
