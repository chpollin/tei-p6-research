---
type: distillate
source-type: document
representation: "[[10_markdown/documents/tei-p5-test-testnames-4.12.0]]"
topics: ["[[Metadata and Entities]]"]
status: grounded
checked:
  validation: 2026-09-06
created: 2026-09-06
updated: 2026-09-06
---

# Distillate: TEI P5 4.12.0 test document testnames.xml

This distillate reports how the release's own test document for names and dates encodes person records, name forms, nym records, places, dates and relations at the pinned TEI P5 4.12.0 release commit, with every statement anchored to the single encoded record or body unit that exhibits the pattern.

## Core statements

- In the TEI P5 4.12.0 test document testnames.xml, the `title` of the file description at block 1 reads "The title", a generic phrase standing where a name for the document would stand. [[10_markdown/documents/tei-p5-test-testnames-4.12.0#^b1]] ^s1
- In the TEI P5 4.12.0 test document testnames.xml, the `nym` record at block 4 carries an `xml:id` and no other attribute and holds four `form` children whose only attribute is `xml:lang`, three of those tags being private-use extensions of the fourth, so the four written forms of one name are distinguished by language tag alone. [[10_markdown/documents/tei-p5-test-testnames-4.12.0#^b4]] ^s2
- In the TEI P5 4.12.0 test document testnames.xml, the residence of the record at block 19 names a place by a `placeName` holding a `settlement`, two `region` elements and a `country` in that order, where the `settlement` and both `region` elements carry a `type` naming the kind of unit while only the `country` carries a `key`. [[10_markdown/documents/tei-p5-test-testnames-4.12.0#^b19]] ^s3
- In the TEI P5 4.12.0 test document testnames.xml, the `country` element in the residence of the record at block 30 carries the one-letter `key` value `D` while its text content gives the country name in English, so the country is identified by a code and named by the element text independently of it. [[10_markdown/documents/tei-p5-test-testnames-4.12.0#^b30]] ^s4
- In the TEI P5 4.12.0 test document testnames.xml, the person record at block 34 carries `rend="nolist"` on the `person` element beside `xml:id`, `sex` and `role`, so an instruction about the presentation of the record is attached to the record element, while the `persName` it contains carries only `xml:lang`. [[10_markdown/documents/tei-p5-test-testnames-4.12.0#^b34]] ^s5
- In the TEI P5 4.12.0 test document testnames.xml, the record at block 84 states a relation to another person inside a `note`, marking that other person with a `name` element that carries `type="person"` and a `key` holding an identifier while carrying no `ref`, so the kind of referent is given by `type` and the identification of the referent by `key`. [[10_markdown/documents/tei-p5-test-testnames-4.12.0#^b84]] ^s6
- In the TEI P5 4.12.0 test document testnames.xml, the person record at block 93 identifies the person by an `xml:id` on the `person` element and carries `sex` and `role` there as well, while its single `persName` child carries only `xml:lang` and no attribute that identifies the person the name stands for. [[10_markdown/documents/tei-p5-test-testnames-4.12.0#^b93]] ^s7
- In the TEI P5 4.12.0 test document testnames.xml, the record at block 101 carries two `persName` children with the same `xml:lang` value and no further attribute, one of them written in inverted order with a comma, so neither form is marked as preferred and the markup states nothing about how the two forms relate. [[10_markdown/documents/tei-p5-test-testnames-4.12.0#^b101]] ^s8
- In the TEI P5 4.12.0 test document testnames.xml, the record at block 108 gives a bibliographic reference as a `bibl` in which a `ref` carries a `target` holding a bare token rather than a URI, with the volume and page numbers standing as plain text beside the `ref`. [[10_markdown/documents/tei-p5-test-testnames-4.12.0#^b108]] ^s9
- In the TEI P5 4.12.0 test document testnames.xml, the `role` attribute of the person record at block 110 holds five whitespace-separated tokens, so one record carries several role values at once on the record element. [[10_markdown/documents/tei-p5-test-testnames-4.12.0#^b110]] ^s10
- In the TEI P5 4.12.0 test document testnames.xml, the record at block 120 dates the birth by a `notBefore` and `notAfter` pair twenty years apart whose element content marks the year as approximate, and dates the death by the same attribute pair with two identical values, so a range and a point in time are expressed through one mechanism. [[10_markdown/documents/tei-p5-test-testnames-4.12.0#^b120]] ^s11
- In the TEI P5 4.12.0 test document testnames.xml, the record at block 123 holds two successive `residence` elements, each containing a `date` with `from` and `to` and a `placeName`, so a change of place is recorded as a sequence of dated states inside the person record, and the record holds no `event` element. [[10_markdown/documents/tei-p5-test-testnames-4.12.0#^b123]] ^s12
- In the TEI P5 4.12.0 test document testnames.xml, the `occupation` element of the record at block 131 holds no text of its own but a single `foreign` child carrying `xml:lang`, so the occupation is stated by a language-marked term, while the `occupation` element itself carries no attribute. [[10_markdown/documents/tei-p5-test-testnames-4.12.0#^b131]] ^s13
- In the TEI P5 4.12.0 test document testnames.xml, the record at block 132 carries only an `xml:id` on the `person` element, gives the name form its own `key` beside `type="full"`, and identifies the birthplace by a `key` on `placeName` whose value repeats the text of that element, so the person, the name form and the place carry three separate identifying values. [[10_markdown/documents/tei-p5-test-testnames-4.12.0#^b132]] ^s14
- In the TEI P5 4.12.0 test document testnames.xml, the record at block 133 states sex by an empty `sex` element with a `value` attribute instead of an attribute on `person`, and states a social status by a `socecStatus` element that carries a `key` together with `notBefore` and `notAfter` and repeats the status as text with a nested `date`. [[10_markdown/documents/tei-p5-test-testnames-4.12.0#^b133]] ^s15
- In the TEI P5 4.12.0 test document testnames.xml, the record at block 134 expresses a relation to another person as a `state` whose `ref` holds a fragment identifier naming a relationship, with the related person given inside a `label` by a `persName` that carries only `xml:lang` and points to no record, and the record carries no `relation` element. [[10_markdown/documents/tei-p5-test-testnames-4.12.0#^b134]] ^s16
- In the TEI P5 4.12.0 test document testnames.xml, the record at block 135 dates birth and death by a `when` attribute on empty `birth` and `death` elements and states the person's age as a bare number in an `age` element that carries no attribute relating that number to either date. [[10_markdown/documents/tei-p5-test-testnames-4.12.0#^b135]] ^s17
- In the TEI P5 4.12.0 test document testnames.xml, the place names inside `birth` and `death` of the record at block 137 consist of a `settlement` and a `country` element carrying neither `type` nor `key`, so those places are named without being identified, while the same record identifies a nationality by a `key` on an empty `nationality` element. [[10_markdown/documents/tei-p5-test-testnames-4.12.0#^b137]] ^s18
- In the TEI P5 4.12.0 test document testnames.xml, the person record at block 143 carries neither `xml:id` nor `role`, splits the name into a `forename` and a `surname` inside a `persName` where none of the three elements carries an attribute, and holds a `birth` element that is present and empty, so nothing in the record identifies the person apart from the name components. [[10_markdown/documents/tei-p5-test-testnames-4.12.0#^b143]] ^s19
- In the TEI P5 4.12.0 test document testnames.xml, the paragraph at the location `/TEI[1]/text[1]/body[1]/p[1]`, recorded as block 152, is empty, so this location carries no running text in which a name could be marked. [[10_markdown/documents/tei-p5-test-testnames-4.12.0#^b152]] ^s20

## Terms

No term definition is extracted. The source is an encoded test file whose blocks carry markup and data, and no block states the meaning of an element, an attribute or one of the token values it uses.

## Open questions

- The `key` values in the blocks read here differ in kind, a country code on `country`, a two-letter code on `nationality`, a name form on `persName`, a place name repeated on `placeName` and a person identifier on `name`. Which of these are meant to resolve against an external authority and which only inside the file?
- Nothing in the records declares the vocabulary of the `role` tokens, the `sex` values or the `type` values on `settlement` and `region`. Where would a consumer of this document find that vocabulary?
- Some person records identify the person by `xml:id` while others carry no identifier at all. Does the document treat the identifier as optional for a person record, or do the several lists serve different tests?
- The relation at block 134 points by `ref` to a fragment identifier, and no block read here declares the target of that pointer. Where is the relationship type meant to be declared?
- The file holds `nym` records, yet the person records attach no `nymRef` to any name form. Does the document exercise the link from a name form to its nym at all?
- The `notBefore` and `notAfter` pair carries an approximation in one record and two identical values in another. Which reading does the document intend where the two values agree?
- The text content of the `socecStatus` element at block 133 contains an unbalanced brace. Is that a transcription defect carried over from the source data or deliberate test input?

## Appraisal

This source is the release's own test document at the pinned commit, so it establishes how a file the project maintains actually encodes person records, name forms, places, dates and relations, and which attribute carries the identifier at each of those points. It cannot establish what the Guidelines recommend, how often these patterns occur in edited corpora, or whether a construct absent from it was left out deliberately, because a test file is written to exercise a schema and its content therefore does not sample encoding practice.

## Related

- [[30_assertions/MOC-Metadata and Entities]]
