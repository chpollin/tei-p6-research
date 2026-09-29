---
type: distillate
source-type: document
representation: "[[10_markdown/documents/practice-v1-dracor-odd-c2f9e814]]"
topics: ["[[ODD and Customization]]", "[[Interoperability and Processing]]"]
status: grounded
checked: {}
created: 2026-09-11
updated: 2026-09-11
---

# Distillate: DraCor ODD at c2f9e814

Four selected passages of the DraCor project's ODD show its declared TEI source, its module selection, deleted attribute classes, one added Schematron constraint and one added element.

## Core statements

- The `schemaSpec` with `ident="dracor"` declares `source="tei:4.12.0"` and `start="TEI teiCorpus dracorCorpus"`. [[10_markdown/documents/practice-v1-dracor-odd-c2f9e814#^r1]] ^s1
- The DraCor `schemaSpec` has twelve `moduleRef` declarations: `header`, `core`, `tei`, `linking`, `drama`, `verse`, `namesdates` and `analysis` without `include` or `except`, `textstructure` restricted with `except="div1 div2 div3 div4 div5 div6 div7"`, and `include` lists for `corpus` (`particDesc`), `figures` (`figure figDesc table row cell`) and `transcr` (`addSpan damageSpan delSpan ellipsis space`). [[10_markdown/documents/practice-v1-dracor-odd-c2f9e814#^r1]] ^s2
- The DraCor ODD deletes the attribute classes `att.datable.custom`, `att.datable.iso`, `att.written`, `att.transcriptional`, `att.editLike`, `att.declaring` and `att.declarable` with `mode="delete"`. [[10_markdown/documents/practice-v1-dracor-odd-c2f9e814#^r2]] ^s3
- A Schematron constraint added by the DraCor ODD, in a rule on the TEI root with `role="warning"`, asserts that the root has `@type='dracor'` or the document has an `xml-model` processing instruction, and that such an instruction references `https://dracor.org/schema.rng`. [[10_markdown/documents/practice-v1-dracor-odd-c2f9e814#^r3]] ^s4
- The DraCor ODD adds the element `dracorCorpus` with `mode="add"`, described as the root element of a `corpus.xml` descriptor document, with exactly one `teiHeader` as its content. [[10_markdown/documents/practice-v1-dracor-odd-c2f9e814#^r4]] ^s5

## Terms

No term definition is extracted from these passages.

## Open questions

- Which effective schema results when this ODD is compiled with a specified toolchain, and does it match the RELAX NG schema served at `https://dracor.org/schema.rng` on a given date?
- Does `source="tei:4.12.0"` resolve to the TEI P5 4.12.0 release in every processor the project uses?
- Which constraints with `role="warning"` does a corpus workflow treat as blocking?

## Appraisal

Only selected passages are distilled. The statements describe declarations;
compiled schemas and validation results require execution against a specified
toolchain. The acquisition manifest records version and rights evidence. Review
by drama-encoding experts is pending.

## Related

- [[30_assertions/practice-v1-sampled-odds-name-their-tei-source-differently]]
- [[30_assertions/practice-v1-sampled-odds-select-modules-by-contrasting-mechanisms]]
- [[30_assertions/practice-v1-sampled-schematron-sits-in-odds-and-in-a-service]]
