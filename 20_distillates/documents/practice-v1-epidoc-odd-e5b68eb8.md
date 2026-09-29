---
type: distillate
source-type: document
representation: "[[10_markdown/documents/practice-v1-epidoc-odd-e5b68eb8]]"
topics: ["[[ODD and Customization]]", "[[Interoperability and Processing]]"]
status: grounded
checked: {}
created: 2026-09-11
updated: 2026-09-11
---

# Distillate: EpiDoc ODD at e5b68eb8

Five passages of the EpiDoc ODD show its licence comment, a recorded release alignment, its declared TEI source, its module selection, attribute changes and a Schematron constraint.

## Core statements

- The licence comment at the start of `schema/tei-epidoc.xml` permits redistribution and modification under the GNU General Public License version 2 or, at the licensee's option, any later version. [[10_markdown/documents/practice-v1-epidoc-odd-e5b68eb8#^r1]] ^s1
- A `revisionDesc` entry dated 2026-01-26 reads "release 9.8: Aligned schema with TEI v. 4.10.2". [[10_markdown/documents/practice-v1-epidoc-odd-e5b68eb8#^r2]] ^s2
- The `schemaSpec` with `ident="tei-epidoc"` declares `source="https://www.tei-c.org/Vault/P5/4.10.2/xml/tei/odd/p5subset.xml"`. [[10_markdown/documents/practice-v1-epidoc-odd-e5b68eb8#^r3]] ^s3
- The EpiDoc `schemaSpec` references `core`, `tei` and `msdescription` without restriction and fourteen further modules with `except` lists, among them `textstructure`, `transcr`, `namesdates`, `textcrit`, `spoken`, `corpus` and `dictionaries`; it uses no `include` list. [[10_markdown/documents/practice-v1-epidoc-odd-e5b68eb8#^r3]] ^s4
- The EpiDoc ODD changes `gap` with an embedded Schematron rule that reports a gap with both `@quantity` and `@extent`, a gap with `@quantity` but no `@unit`, and a gap inside a `supplied` ancestor whose reason is not `undefined` unless the gap's reason is `ellipsis`. [[10_markdown/documents/practice-v1-epidoc-odd-e5b68eb8#^r4]] ^s5
- The EpiDoc ODD replaces `gap/@reason` with a required attribute whose closed value list is `lost`, `illegible`, `omitted`, `ellipsis` and `undefined`, and deletes `gap/@dur`. [[10_markdown/documents/practice-v1-epidoc-odd-e5b68eb8#^r4]] ^s6
- The EpiDoc ODD changes a class with `ident="att.responsibility"`, replacing its `@cert` with a closed value list of `low` and `high`. [[10_markdown/documents/practice-v1-epidoc-odd-e5b68eb8#^r5]] ^s7

## Terms

No term definition is extracted from these passages.

## Open questions

- Does a class named `att.responsibility` exist in the P5 4.10.2 subset the ODD names, and what does a processor do with a change to a class it cannot find?
- Which RELAX NG schema results from this ODD, and which published schema location supplies that result?
- How do the embedded Schematron reports behave in the tools EpiDoc projects actually use?

## Appraisal

The distilled passages describe ODD declarations. Compiled output and
validation behaviour require execution against a specified toolchain. Statement
s1 reports only the opening licence comment; it is not a determination of the
rights applying to every part of the file. The acquisition manifest records the
separate licence evidence. Review by epigraphers familiar with the Leiden
conventions is pending.

## Related

- [[30_assertions/practice-v1-sampled-odds-name-their-tei-source-differently]]
- [[30_assertions/practice-v1-sampled-odds-select-modules-by-contrasting-mechanisms]]
- [[30_assertions/practice-v1-sampled-schematron-sits-in-odds-and-in-a-service]]
