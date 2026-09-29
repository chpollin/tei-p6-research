---
type: distillate
source-type: document
representation: "[[10_markdown/documents/practice-v1-isicily-isic000156-262784ad]]"
topics: ["[[Interoperability and Processing]]", "[[ODD and Customization]]"]
status: grounded
checked: {}
created: 2026-09-11
updated: 2026-09-11
---

# Distillate: I.Sicily inscription ISic000156 at 262784ad

Six passages of one edited I.Sicily EpiDoc file show its schema associations, licence, dating, header inclusions, revision status and primary edition markup.

## Core statements

- The file `inscriptions/ISic000156.xml` carries two `xml-model` processing instructions, one for RELAX NG at `https://epidoc.stoa.org/schema/latest/tei-epidoc.rng` and one for Schematron at the relative path `../schematron/ircyr-checking.sch`. [[10_markdown/documents/practice-v1-isicily-isic000156-262784ad#^r1]] ^s1
- The file's `licence` element states a Creative Commons Attribution 4.0 licence with the target `http://creativecommons.org/licenses/by/4.0/`. [[10_markdown/documents/practice-v1-isicily-isic000156-262784ad#^r2]] ^s2
- The file's `origDate` carries `datingMethod="#julian"`, `notBefore-custom="0001"`, `notAfter-custom="0250"` and `cert="low"` around the text "Imperial". [[10_markdown/documents/practice-v1-isicily-isic000156-262784ad#^r3]] ^s3
- The file's `encodingDesc` contains the paragraph "Encoded following the latest EpiDoc guidelines" and two `xi:include` elements with fallback paragraphs, referencing `../alists/ISicily-taxonomies.xml` and `../alists/charDecl.xml`. [[10_markdown/documents/practice-v1-isicily-isic000156-262784ad#^r4]] ^s4
- The file's `revisionDesc` has `status="edited"`. [[10_markdown/documents/practice-v1-isicily-isic000156-262784ad#^r5]] ^s5
- The primary Latin edition `div` encodes abbreviations with `expan`, `abbr` and `ex`, lost text with `supplied reason="lost"`, an ivy-leaf glyph with `g ref="#ivy-leaf"`, and a `gap` with `reason="lost"`, `extent="unknown"` and `unit="character"`. [[10_markdown/documents/practice-v1-isicily-isic000156-262784ad#^r6]] ^s6

## Terms

No term definition is extracted from these passages.

## Open questions

- Is the file valid against the RELAX NG schema served at the referenced `latest` location on a stated date, and against the project Schematron?
- How does a processor that does not resolve the two XIncludes treat the fallback paragraphs?
- Which schema declares the `notBefore-custom` and `notAfter-custom` attributes the file uses?

## Appraisal

The passages describe one inscription record; no representativeness of the
corpus is claimed. The schema references alone establish no validation result
or equivalence with another schema. No validation was executed. Review by
epigraphers is pending. Selection and context comparisons are recorded in the
acquisition manifest.

## Related

- [[30_assertions/practice-v1-sampled-inputs-associate-schemas-differently]]
- [[30_assertions/practice-v1-epidoc-latest-guidance-and-isicily-reference]]
