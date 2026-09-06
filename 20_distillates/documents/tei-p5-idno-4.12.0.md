---
type: distillate
source-type: document
representation: "[[10_markdown/documents/tei-p5-idno-4.12.0]]"
topics: ["[[Metadata and Entities]]"]
status: grounded
checked:
  validation: 2026-09-06
created: 2026-09-06
updated: 2026-09-06
---

# Distillate: TEI P5 4.12.0 idno specification

This distillate reports the English description, the English descriptions of the `type` attribute and of its documented values, and the English remarks of the complete `idno.xml` specification at the pinned TEI P5 4.12.0 release commit.

## Core statements

- In TEI P5 4.12.0, the English description of `idno` states that the element supplies any form of identifier used to identify some object in a standardized way. [[10_markdown/documents/tei-p5-idno-4.12.0#^r1]] ^s1
- In TEI P5 4.12.0, the English description of `idno` names a bibliographic item, a person, a title and an organization as examples of the object identified, with the enumeration left open by "etc.". [[10_markdown/documents/tei-p5-idno-4.12.0#^r1]] ^s2
- In TEI P5 4.12.0, the English description of the `type` attribute of `idno` states that the attribute categorizes the identifier. [[10_markdown/documents/tei-p5-idno-4.12.0#^r2]] ^s3
- In TEI P5 4.12.0, the English description of the `type` attribute of `idno` names an ISBN and a Social Security number as examples of the category, with the enumeration left open by "etc.". [[10_markdown/documents/tei-p5-idno-4.12.0#^r2]] ^s4
- In TEI P5 4.12.0, the English description of the value `ISBN` of `type` on `idno` states that an International Standard Book Number is a 13-digit or, if assigned prior to 2007, 10-digit identifying number assigned by the publishing industry to a published book or similar item, registered with the International ISBN Agency. [[10_markdown/documents/tei-p5-idno-4.12.0#^r3]] ^s5
- In TEI P5 4.12.0, the English description of the value `ISSN` of `type` on `idno` states that an International Standard Serial Number is an eight-digit number to uniquely identify a serial publication. [[10_markdown/documents/tei-p5-idno-4.12.0#^r4]] ^s6
- In TEI P5 4.12.0, the English description of the value `DOI` of `type` on `idno` states that a Digital Object Identifier is a unique string of letters and numbers assigned to an electronic document. [[10_markdown/documents/tei-p5-idno-4.12.0#^r5]] ^s7
- In TEI P5 4.12.0, the English description of the value `URI` of `type` on `idno` states that a Uniform Resource Identifier is a string of characters to uniquely identify a resource, following the syntax of RFC 3986. [[10_markdown/documents/tei-p5-idno-4.12.0#^r6]] ^s8
- In TEI P5 4.12.0, the English description of the value `VIAF` of `type` on `idno` states that it is a data number in the "Virtual Internet Authority File" assigned to link different names in catalogs around the world for the same entity. [[10_markdown/documents/tei-p5-idno-4.12.0#^r7]] ^s9
- In TEI P5 4.12.0, the English description of the value `ESTC` of `type` on `idno` states that an English Short-Title Catalogue number is an identifying number assigned to a document in English printed in the British Isles or North America before 1801. [[10_markdown/documents/tei-p5-idno-4.12.0#^r8]] ^s10
- In TEI P5 4.12.0, the English description of the value `OCLC` of `type` on `idno` states that it is the OCLC control number (record number) for the union catalog record in WorldCat, a union catalog for member libraries in the Online Computer Library Center global cooperative. [[10_markdown/documents/tei-p5-idno-4.12.0#^r9]] ^s11
- In TEI P5 4.12.0, the English remarks on `idno` state that the element should be used for labels which identify an object or concept in a formal cataloguing system such as a database or an RDF store, or in a distributed system such as the World Wide Web. [[10_markdown/documents/tei-p5-idno-4.12.0#^r10]] ^s12
- In TEI P5 4.12.0, the English remarks on `idno` state that some suggested values for `type` on `idno` are `ISBN`, `ISSN`, `DOI` and `URI`. [[10_markdown/documents/tei-p5-idno-4.12.0#^r10]] ^s13

## Terms

- **idno**: the element whose English description supplies any form of identifier used to identify some object in a standardized way. [[10_markdown/documents/tei-p5-idno-4.12.0#^r1]]
- **type**: the attribute of `idno` whose English description categorizes the identifier. [[10_markdown/documents/tei-p5-idno-4.12.0#^r2]]
- **ISBN**: the value of `type` on `idno` whose English description expands it as "International Standard Book Number". [[10_markdown/documents/tei-p5-idno-4.12.0#^r3]]
- **ISSN**: the value of `type` on `idno` whose English description expands it as "International Standard Serial Number". [[10_markdown/documents/tei-p5-idno-4.12.0#^r4]]
- **DOI**: the value of `type` on `idno` whose English description expands it as "Digital Object Identifier". [[10_markdown/documents/tei-p5-idno-4.12.0#^r5]]
- **URI**: the value of `type` on `idno` whose English description expands it as "Uniform Resource Identifier". [[10_markdown/documents/tei-p5-idno-4.12.0#^r6]]
- **VIAF**: the value of `type` on `idno` whose English description names a data number in the "Virtual Internet Authority File". [[10_markdown/documents/tei-p5-idno-4.12.0#^r7]]
- **ESTC**: the value of `type` on `idno` whose English description expands it as "English Short-Title Catalogue number". [[10_markdown/documents/tei-p5-idno-4.12.0#^r8]]
- **OCLC**: the value of `type` on `idno` whose English description names the OCLC control number for the union catalog record in WorldCat. [[10_markdown/documents/tei-p5-idno-4.12.0#^r9]]

## Open questions

- Which source establishes where an `idno` may stand in a record and which attributes reach it, given that only the XML declares the memberships in `att.global`, `att.cmc`, `att.datable`, `att.sortable`, `att.typed`, `model.msItemPart`, `model.nameLike`, `model.personPart` and `model.publicationStmtPart.detail`, the module `header`, the identifier `gi-idno` and the four `listRef` pointers, and no English reading block states any of them?
- Which source establishes what an identifier value inside `idno` may consist of, given that only the XML declares the content model as an unbounded alternation of a text node, `model.gLike` and a nested `idno`, and no English reading block covers it?
- Which source establishes whether a value of `type` outside the seven documented ones is permitted, given that only the XML declares `type` as optional with the datatype `teidata.enumerated` and its value list as `type="semi"`, while the English remarks call four of the values suggested?
- Which representation would anchor the usage the examples demonstrate, in which `idno` carries the types `LT`, `Wing`, `oldCat` and `OTA` beside the documented values and one identifier includes a non-Unicode character referenced as `#sym`, given that the examples and the paragraph explaining them lie outside the English reading blocks?
- In which scope do the uniqueness claims hold that the English descriptions make for `ISSN`, `DOI` and `URI`, given that they state only that the number uniquely identifies a serial publication, that the string assigned to an electronic document is unique, and that the string uniquely identifies a resource?
- Which source establishes how a consumer resolves an `idno` value to the object it identifies, given that the English remarks state only that the element should be used for labels which identify an object or concept in a formal cataloguing system or in a distributed system?
- Which source would establish what the English gloss "identifier" and the non-English glosses, descriptions and remarks of this specification state, given that the reading blocks reproduce the English description, the English attribute and value descriptions and the English remarks alone?

## Appraisal

The source is the complete element specification at a pinned release commit, so its English text establishes what the Guidelines say about carrying a standardized identifier, about the kinds of object such an identifier may name, and about seven identifier schemes documented as values of `type` together with the value form each of them takes. It establishes nothing about where `idno` may occur in a record, because every membership and the module stay in the XML, and nothing about how a stated identifier is resolved to its object. The two levels the source keeps apart, the categorization of an identifier through `type` and the description of the scheme behind each documented value, are separately anchorable and should stay separate until the assertion layer joins them.

## Related

- [[30_assertions/MOC-Metadata and Entities]]
