---
type: distillate
source-type: publication
reference: teic-tei-issue-1414
topics: ["[[Metadata and Entities]]"]
status: validated
checked:
  machine-review: 2026-09-06
  validation: 2026-09-06
  quote: 2026-09-06
created: 2026-09-06
updated: 2026-09-06
---

# Distillate: TEIC/TEI GitHub issue 1414

This distillate extracts what one thread of the TEIC/TEI issue tracker proposes
about pointing from an entity record to an external description of the same
entity, and what its comments and its closure record about that proposal.

## Core statements

- In TEIC/TEI issue 1414, the issue author writes that an entry in a placeography, personography, bibliography or whatever should be able to refer, using `ref` or `key`, to some other data structure that has further information about the same entity. ^s1
  > "An entry in a placeography, personography, bibliography, or whatever should be able to refer (using `@ref` or `@key`) to some other data structure that has further information about the same entity." (https://github.com/TEIC/TEI/issues/1414, issue body, opening paragraph, 2015-12-15)
- In TEIC/TEI issue 1414, the issue author writes of developing some local convention like using `ref` of a `<placeName>` child of `<place>`. ^s2
  > "is to develop some local convention like using `@ref` of a `<placeName>` child of `<place>`" (https://github.com/TEIC/TEI/issues/1414, issue body, second paragraph, 2015-12-15)
- In TEIC/TEI issue 1414, the issue author writes that they think the best way to do this is by allowing `ref`, and `key` for the web-impaired, on `<person>` and `<place>`. ^s3
  > "I think the best way to do this is by allowing `@ref` (and `@key` for the web-impaired) on `<person>` and `<place>`" (https://github.com/TEIC/TEI/issues/1414, issue body, closing paragraph, 2015-12-15)
- In TEIC/TEI issue 1414, a commenter writes a plus one and states that linking personographies to external authorities is not as elegant as it could be. ^s4
  > "+1 linking personographies to external authorities isn't as elegant as it could be." (https://github.com/TEIC/TEI/issues/1414, comment 1, 2015-12-16)
- In TEIC/TEI issue 1414, a commenter writes that they would have used the corresponding attribute on `place` or `person` and private uri schemes. ^s5
  > "I would have used the corresponding attribute on place or person and private uri schemes." (https://github.com/TEIC/TEI/issues/1414, comment 2, 2015-12-16)
- In TEIC/TEI issue 1414, a commenter writes that a schema or grammar for link sequences would be needed, especially where more than one private URI of the same scheme is present. ^s6
  > "you'd need a schema/grammar for link sequences, especially if you have more than one private URI of the same scheme there." (https://github.com/TEIC/TEI/issues/1414, comment 3, 2015-12-16)
- In TEIC/TEI issue 1414, a commenter records that `@ref` can already hold several URIs separated by white-space. ^s7
  > "I just realised that `@ref` can hold multiple URIs separated by white-space" (https://github.com/TEIC/TEI/issues/1414, comment 5, 2015-12-16)
- In TEIC/TEI issue 1414, a commenter reports using an `<idno>` of type uri as a child of a structured `<place>` or `<person>`. ^s8
  > "We're using `<idno type="uri">http://lccn.loc.gov/n80051862</uri>` as a child of (structured) `<place>`, `<person>` etc." (https://github.com/TEIC/TEI/issues/1414, comment 6, 2015-12-16)
- In TEIC/TEI issue 1414, a commenter writes that it allows multiple links to be represented in a more precise and scaleable way than does simply providing multiple URI values for a single attribute. ^s9
  > "it allows you to represent multiple links in a more precise and scaleable way than does simply providing multiple URI values for a single attribute." (https://github.com/TEIC/TEI/issues/1414, comment 7, 2015-12-16)
- In TEIC/TEI issue 1414, a commenter reports that the Council sub-group thinks conceptually that the requirement for a single TEI Guidelines endorsed mechanism for this purpose is a Go and no longer needs discussion. ^s10
  > "Council sub-group thinks conceptually the requirement for a single TEI Guidelines endorsed mechanism for this purpose is a "Go" (no longer "needs discussion")." (https://github.com/TEIC/TEI/issues/1414, comment 8, 2016-04-25)
- In TEIC/TEI issue 1414, a commenter writes that the details of implementation do require discussion. ^s11
  > "The details of implementation do require discussion." (https://github.com/TEIC/TEI/issues/1414, comment 8, 2016-04-25)
- In TEIC/TEI issue 1414, a comment records a leaning towards permitting `<idno>` as a direct, probably first, child of `<person>` and `<place>`. ^s12
  > "We lean towards permitting `<idno>` as a direct (probably 1st) child of `<person>`, `<place>`" (https://github.com/TEIC/TEI/issues/1414, comment 8, 2016-04-25)
- In TEIC/TEI issue 1414, a comment notes that the content of some of those elements has positions where `<idno>` cannot stand. ^s13
  > "there are places in the content of some of those elements that `<idno>` cannot go" (https://github.com/TEIC/TEI/issues/1414, comment 10, 2016-04-25)
- In TEIC/TEI issue 1414, a commenter summarizes the discussion and names as the short-term solution adding `<idno>` as a first child for ogrophy elements. ^s14
  > "To summarize the discussion: short-term solution is to add `<idno>` as a first child for ogrophy elements" (https://github.com/TEIC/TEI/issues/1414, comment 12, 2016-09-26)
- In TEIC/TEI issue 1414, a comment of 2019-05-07 states that `person`, `place`, `org` and `bibl` allow `idno` at that time and that `event` and `nym` do not. ^s15
  > "`person`, `place`, `org` and `bibl` all allow for `idno`. Missing from `event` and `nym`" (https://github.com/TEIC/TEI/issues/1414, comment 13, 2019-05-07)
- In TEIC/TEI issue 1414, a comment of 2019-07-10 asks whether the issue can be closed and reports that `idno` had been added to `event` and `nym` on 7 May. ^s16
  > "can we close this? You added idno to event and nym on May 7" (https://github.com/TEIC/TEI/issues/1414, comment 15, 2019-07-10)
- In TEIC/TEI issue 1414, a commenter writes that they think it can be closed unless a passage about this use of `idno` should be added into GL. ^s17
  > "I think we can close it, unless we think a passage about this use of `idno` should be added into GL?" (https://github.com/TEIC/TEI/issues/1414, comment 16, 2019-07-15)

## Terms

No additional term definition is extracted in this bounded intake.

## Open questions

- Did `@ref` and `@key` ever reach the record elements, which is the mechanism the issue proposed and which no comment in the thread reports as carried out?
- Where was the class framing of the record title settled, given that no body in the snapshot names an attribute class?
- Which governance record decided the mechanism, and which commit and release gave it effect, neither of which the thread names?
- Was the passage about this use of `idno` added to the Guidelines, which the closing comment leaves open?
- What applies when a local key and an external URI are both available for the same record, which the thread does not address?
- Which positions in the content models of the record elements remained closed to `<idno>` after the reported additions?

## Appraisal

The thread establishes what participants and one Council sub-group stated
between 2015 and 2019 about pointing from an entity record to an external
description of the same entity. It establishes neither a governance decision
nor a released effect. The membership of the record elements in `att.canonical`
and their content models at the pinned release are read in the admitted class
and element blobs at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The line of the discussion moves from the proposed attributes to a child
element. The reported additions of `idno` to `event` and `nym` are participant
reports inside the thread and carry no release state.

The recorded outcome comes from the work-item record of the admission run
`sources/manifests/2026-09-06-entities-run2-citations.yaml`. The issue is
closed with the reason `completed` on 2019-07-15, it carries the labels
`Type: FeatureRequest`, `Status: Go` and `TEI: Schema` and the milestone
`Guidelines 3.6.0`, and the snapshot names no pull request. Closure records
closure alone. The label `Status: Go` records a disposition of the discussion,
and acceptance or a released effect would need a governance record and a
release.

Full discussion prose stays in local raw storage because repository licensing
does not license participant discussion text. Participant logins and names are
absent from this distillate under the same rule, so positions are attributed by
role and comment position. The spelling of the quotations follows the raw
snapshot, including the misspelling of the element name in the summarizing
comment.

## Related

- [[20_distillates/documents/tei-p5-idno-4.12.0]]
- [[20_distillates/documents/tei-p5-att.canonical-4.12.0]]
- [[20_distillates/documents/tei-p5-person-4.12.0]]
- [[20_distillates/documents/tei-p5-place-4.12.0]]
- [[30_assertions/p5-guidelines-separate-the-entity-record-from-references-to-the-entity]]
