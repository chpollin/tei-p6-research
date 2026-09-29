---
type: distillate
source-type: document
representation: "[[10_markdown/documents/practice-v1-cmif-odd-d171133e]]"
topics: ["[[ODD and Customization]]", "[[Metadata and Entities]]"]
status: grounded
checked: {}
created: 2026-09-11
updated: 2026-09-11
---

# Distillate: CMIF ODD at d171133e

Six passages of the Correspondence Metadata Interchange Format ODD, version 1.1, show its schema specification, module selection, one replaced attribute class, three element changes and a recorded restriction.

## Core statements

- The `schemaSpec` with `ident="cmi-customization"` declares `start="TEI"` and `status="stable"` and carries no `source` attribute. [[10_markdown/documents/practice-v1-cmif-odd-d171133e#^r1]] ^s1
- The CMIF `schemaSpec` has five `moduleRef` declarations: `tei` without restriction and `textstructure`, `core`, `header` and `namesdates` with `include` lists; the `header` list includes `correspDesc`, `correspAction` and `correspContext`, and the `namesdates` list is `persName orgName placeName`. [[10_markdown/documents/practice-v1-cmif-odd-d171133e#^r1]] ^s2
- The CMIF ODD replaces `att.editLike` with a class whose optional `@evidence` has a closed value list containing only `conjecture`. [[10_markdown/documents/practice-v1-cmif-odd-d171133e#^r2]] ^s3
- The CMIF ODD changes `correspAction` to a content of one or more members of `model.correspActionPart` and makes `@type` required with a replaced closed value list of `sent` and `received`. [[10_markdown/documents/practice-v1-cmif-odd-d171133e#^r3]] ^s4
- The CMIF ODD replaces `idno` with a declaration described as providing the URL of the CMI file, with `teidata.pointer` content and an added required `@type` whose closed value list is `url`. [[10_markdown/documents/practice-v1-cmif-odd-d171133e#^r4]] ^s5
- The CMIF ODD changes `persName` by replacing its class memberships with `model.nameLike.agent`, `att.canonical`, `att.editLike` and `att.global.responsibility`, limiting its content to text, deleting `@key` and changing `@ref` to recommended usage. [[10_markdown/documents/practice-v1-cmif-odd-d171133e#^r5]] ^s6
- A CMIF revision entry dated 2025-02-26 describes restricting `@evidence` to `conjecture` and `@cert` to `low`. [[10_markdown/documents/practice-v1-cmif-odd-d171133e#^r6]] ^s7

## Terms

No term definition is extracted from these passages.

## Open questions

- Against which TEI P5 release is this ODD compiled when no `source` attribute names one?
- Does the RELAX NG schema published in the same repository reflect every restriction of this ODD revision?
- Which additional checks, if any, are required beyond a schema generated from this ODD?

## Appraisal

The statements describe declarations in the sampled ODD. This project compiled
no schema and validated no CMIF file. Version and rights evidence for the
acquisition are recorded in its manifest. Review by correspondence-edition
experts is pending.

## Related

- [[30_assertions/practice-v1-sampled-odds-name-their-tei-source-differently]]
- [[30_assertions/practice-v1-sampled-odds-select-modules-by-contrasting-mechanisms]]
- [[30_assertions/practice-v1-cmif-evidence-restriction-appears-in-a-real-file]]
