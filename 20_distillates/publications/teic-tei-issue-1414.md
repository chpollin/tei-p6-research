---
type: distillate
source-type: publication
reference: teic-tei-issue-1414
topics: ["[[Metadata and Entities]]"]
status: grounded
checked:
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

- The issue proposes that an entry in a placeography, personography or bibliography be able to point at another data structure holding further information about the same entity. ^s1
  > "should be able to refer (using `@ref` or `@key`) to some other data structure" (https://github.com/TEIC/TEI/issues/1414, issue body, opening paragraph, 2015-12-15)
- The issue states that reaching such a structure requires a local convention, for instance `@ref` on a `<placeName>` child of `<place>`. ^s2
  > "is to develop some local convention like using `@ref` of a `<placeName>` child" (https://github.com/TEIC/TEI/issues/1414, issue body, second paragraph, 2015-12-15)
- The issue names allowing `@ref` and `@key` on the record elements `<person>` and `<place>` as the way it considers best. ^s3
  > "is by allowing `@ref` (and `@key` for the web-impaired) on `<person>` and `<place>`" (https://github.com/TEIC/TEI/issues/1414, issue body, closing paragraph, 2015-12-15)
- A commenter supports the request and states that the existing linking of personographies to external authorities is less elegant than it could be. ^s4
  > "linking personographies to external authorities isn't as elegant as it could be" (https://github.com/TEIC/TEI/issues/1414, comment 1, 2015-12-16)
- A commenter reports that they would have used the corresponding attribute on `place` or `person` together with private URI schemes. ^s5
  > "used the corresponding attribute on place or person and private uri schemes" (https://github.com/TEIC/TEI/issues/1414, comment 2, 2015-12-16)
- A commenter objects that this route needs a schema or grammar for link sequences as soon as more than one private URI of the same scheme occurs. ^s6
  > "you'd need a schema/grammar for link sequences, especially if you have more than one" (https://github.com/TEIC/TEI/issues/1414, comment 3, 2015-12-16)
- A commenter records that `@ref` can already hold several URIs separated by white-space. ^s7
  > "I just realised that `@ref` can hold multiple URIs separated by white-space" (https://github.com/TEIC/TEI/issues/1414, comment 5, 2015-12-16)
- A commenter reports the practice of holding the external identifier in an `<idno>` of type uri inside the structured record element. ^s8
  > "We're using `<idno type="uri">http://lccn.loc.gov/n80051862</uri>` as a child of (structured)" (https://github.com/TEIC/TEI/issues/1414, comment 6, 2015-12-16)
- A commenter calls that route more precise and scalable than supplying several URI values in a single attribute. ^s9
  > "a more precise and scaleable way than does simply providing multiple URI values" (https://github.com/TEIC/TEI/issues/1414, comment 7, 2015-12-16)
- A comment attributes to a Council sub-group the position that a single TEI Guidelines endorsed mechanism for this purpose is required. ^s10
  > "Council sub-group thinks conceptually the requirement for a single TEI Guidelines endorsed" (https://github.com/TEIC/TEI/issues/1414, comment 8, 2016-04-25)
- The same comment states that the implementation of that mechanism remains to be discussed. ^s11
  > "The details of implementation do require discussion." (https://github.com/TEIC/TEI/issues/1414, comment 8, 2016-04-25)
- The same comment records a leaning towards permitting `<idno>` as a direct, probably first, child of `<person>` and `<place>`. ^s12
  > "We lean towards permitting `<idno>` as a direct (probably 1st) child of `<person>`, `<place>`" (https://github.com/TEIC/TEI/issues/1414, comment 8, 2016-04-25)
- A comment notes that the content of some of those elements has positions where `<idno>` cannot stand. ^s13
  > "there are places in the content of some of those elements that `<idno>` cannot go" (https://github.com/TEIC/TEI/issues/1414, comment 10, 2016-04-25)
- A comment summarizes the discussion and names adding `<idno>` as a first child of the record elements the short-term solution. ^s14
  > "short-term solution is to add `<idno>` as a first child for ogrophy elements" (https://github.com/TEIC/TEI/issues/1414, comment 12, 2016-09-26)
- A comment of 2019-05-07 states that `person`, `place`, `org` and `bibl` allow `idno` at that time and that `event` and `nym` do not. ^s15
  > "`person`, `place`, `org` and `bibl` all allow for `idno`. Missing from `event` and `nym`" (https://github.com/TEIC/TEI/issues/1414, comment 13, 2019-05-07)
- A comment of 2019-07-10 asks whether the issue can be closed and reports that `idno` had been added to `event` and `nym` on 7 May. ^s16
  > "can we close this? You added idno to event and nym on May 7" (https://github.com/TEIC/TEI/issues/1414, comment 15, 2019-07-10)
- The last recorded comment holds that the issue can be closed and raises whether a passage about this use of `idno` should be added to the Guidelines. ^s17
  > "I think we can close it, unless we think a passage about this use" (https://github.com/TEIC/TEI/issues/1414, comment 16, 2019-07-15)

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
