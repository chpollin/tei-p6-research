---
type: distillate
source-type: publication
reference: teic-tei-issue-337
topics: ["[[Metadata and Entities]]"]
status: grounded
checked:
  validation: 2026-09-06
  quote: 2026-09-06
created: 2026-09-06
updated: 2026-09-06
---

# Distillate: TEIC/TEI issue 337, soft deprecation of @key

This distillate reports the proposal, the discussion and the recorded outcome of the TEIC/TEI issue thread on a soft deprecation of `key`, as observed in the locked GitHub REST snapshot of 2026-09-06 with the issue page and the single comment page of twenty-one comments.

## Core statements

- The issue author attributes the proposal to a discussion at a TEI Council meeting of November 2011. ^s1
  > "Per discussion at TEI Council meeting in Paris in November 2011" (https://github.com/TEIC/TEI/issues/337, issue description, 2011-11-13)
- The issue author reports an agreement that all uses of `key` can be handled by `ref`. ^s2
  > "we agreed that uses of `@key` can all be handled by `@ref`" (https://github.com/TEIC/TEI/issues/337, issue description, 2011-11-13)
- The issue gives a URN as the value form of the replacing `ref` attribute. ^s3
  > "using ref="urn:&lt;NID&gt;:&lt;NSS&gt;"" (https://github.com/TEIC/TEI/issues/337, issue description, 2011-11-13)
- The issue author reports a wish to deprecate `key` some day, held back by how widely the attribute is used at the time of writing. ^s4
  > "deprecate `@key` some day but that it's too widely used today to do so" (https://github.com/TEIC/TEI/issues/337, issue description, 2011-11-13)
- The issue announces an interim measure that changes the Guidelines so that readers are told to switch to `ref`. ^s5
  > "modify the Guidelines to make the point that people should switch to `@ref`" (https://github.com/TEIC/TEI/issues/337, issue description, 2011-11-13)
- A commenter offers an alternative to the URN with a non-registered NID that the issue proposes. ^s6
  > "As an alternative to using a URN with a non-registered NID" (https://github.com/TEIC/TEI/issues/337, comment 3 of 21, 2011-11-13)
- The same commenter states that deciding between the two value forms needs someone with a better understanding of the matter. ^s7
  > "Need to find someone who better understands these things to know which is better" (https://github.com/TEIC/TEI/issues/337, comment 3 of 21, 2011-11-13)
- A commenter relays a report that a URI with a non-registered scheme was judged slightly less abusive. ^s8
  > "a URI with a non-registered scheme was slightly less abusive" (https://github.com/TEIC/TEI/issues/337, comment 7 of 21, 2011-11-20)
- A commenter relays an emailed opinion that asks why an http URL is not used, so that people who need to find out what the referent is can do so. ^s9
  > "not an http URL, so people who need to find out what the thing" (https://github.com/TEIC/TEI/issues/337, comment 9 of 21, 2011-12-04)
- The same relayed opinion names a PURL for the case where permanence is the concern. ^s10
  > "you are concerned about permanence, why not make it a PURL?" (https://github.com/TEIC/TEI/issues/337, comment 9 of 21, 2011-12-04)
- A commenter suggests folding the ticket into a proposed subcommittee. ^s11
  > "I suggest that this get folded into the subcommittee" (https://github.com/TEIC/TEI/issues/337, comment 10 of 21, 2011-12-08)
- A commenter agrees with the soft deprecation of `key` that the issue proposes. ^s12
  > "I agree with the original ticket, for soft deprecation of `@key`" (https://github.com/TEIC/TEI/issues/337, comment 11 of 21, 2012-04-13)
- The same commenter records uncertainty between recommending URIs and URNs together with a leaning towards unregulated URIs. ^s13
  > "recommending URIs vs URNs but lean towards unregulated URIs" (https://github.com/TEIC/TEI/issues/337, comment 11 of 21, 2012-04-13)
- A commenter records that one participant would choose between URI and URN and carry the ticket out. ^s14
  > "will choose URI or URN and carry out this ticket now" (https://github.com/TEIC/TEI/issues/337, comment 12 of 21, 2012-04-16)
- The same commenter states that a value whose scheme is not internal is to be left as `key`. ^s15
  > "should be left as key because it's not an internal scheme" (https://github.com/TEIC/TEI/issues/337, comment 12 of 21, 2012-04-16)
- A commenter reports that the bar for registering a URI scheme is fairly high. ^s16
  > "the bar for registration is fairly high" (https://github.com/TEIC/TEI/issues/337, comment 13 of 21, 2012-05-20)
- The same commenter judges that most uses of `key` would not satisfy the stated requirements. ^s17
  > "most uses of `@key` would not satisfy these" (https://github.com/TEIC/TEI/issues/337, comment 13 of 21, 2012-05-20)
- The same commenter reports that RFC 2141 never advanced beyond being a proposed standard. ^s18
  > "RFC 2141 never advanced beyond being a proposed standard" (https://github.com/TEIC/TEI/issues/337, comment 13 of 21, 2012-05-20)
- The same commenter identifies the URI scheme described in RFC 4151 as exactly what is needed. ^s19
  > "URI scheme (as described in RFC 4151) -- appears to be exactly what we need" (https://github.com/TEIC/TEI/issues/337, comment 13 of 21, 2012-05-20)
- The same commenter announces changing all uses of `key` in Guidelines examples to one format. ^s20
  > "change all uses of `@key` in examples in the Guidelines to use this format" (https://github.com/TEIC/TEI/issues/337, comment 13 of 21, 2012-05-20)
- That announced change excludes examples which already refer to a particular external vocabulary. ^s21
  > "which already refer to a particular external vocabulary" (https://github.com/TEIC/TEI/issues/337, comment 13 of 21, 2012-05-20)
- The same commenter states that the use of tag URIs does not prohibit any user of the TEI. ^s22
  > "use of tag URIs does not prohibit any user of the TEI" (https://github.com/TEIC/TEI/issues/337, comment 13 of 21, 2012-05-20)
- A commenter reports the change implemented at a named repository revision. ^s23
  > "Implemented at revision 10374." (https://github.com/TEIC/TEI/issues/337, comment 14 of 21, 2012-05-20)
- A commenter states that the result looks fine and that they are closing the ticket. ^s24
  > "This looks fine to me, so I am closing the ticket" (https://github.com/TEIC/TEI/issues/337, comment 19 of 21, 2012-06-17)
- The migrated thread records a status change from open to closed. ^s25
  > "**status**: open --> closed" (https://github.com/TEIC/TEI/issues/337, comment 20 of 21, 2012-06-17)
- The last comment reports, with reference to a Council working paper, that text was added to `<remarks>`. ^s26
  > "Per http://www.tei-c.org/Activities/Council/Working/tcw27.xml, added text to `<remarks>`" (https://github.com/TEIC/TEI/issues/337, comment 21 of 21, 2013-06-21)

## Terms

No additional term definition is extracted in this citation-only intake. The thread uses "soft deprecation" in its title and in one comment without stating what the term covers.

## Open questions

- Which record establishes the reported November 2011 agreement as a governance decision, given that the thread carries a participant report of a meeting?
- Which release first carried the announced Guidelines change and the added `<remarks>` text, given that the thread names repository revisions only?
- What applies when `key` and `ref` are both present on one element, given that the thread proposes a switch from the one to the other and states no precedence for the case in which both are given?
- Which of the discussed value forms do the Guidelines finally recommend, given that the thread weighs a URN, an unregistered URI scheme, an http URL, a PURL and a tag URI, and records no decision by any body?
- What is the status of `key` at the pinned release after this thread, given that the thread's own closure establishes nothing about that status?
- How far does the announced exclusion of values that already point at an external vocabulary reach, given that the thread names one example of such a value?

## Appraisal

The source establishes a participant proposal, the arguments raised against its value form, and the reported implementation and closure of a work item. It establishes no acceptance by a TEI body and no released effect. The snapshot records the thread as `closed` with the labels `Type: FeatureRequest`, `sf-automigrated` and `Status: Go`, and those labels are repository metadata at the observation date. The recorded GitHub closing timestamp of 2015-10-02 falls on the same day as the migration comment and the `updated_at` value of every comment record, while the thread's own closing statement is dated 2012-06-17, so the two dates stay apart in any citation of this thread. Two comments of the migrated thread record assignment and status transitions, and the reported email of an outside expert reaches the thread through a participant who quotes it. The entity spellings and the nested quotation marks inside the quotations are preserved from the original API fields. Full discussion prose remains in local raw storage because repository licensing does not license participant discussion text, and participant identities are deliberately absent from this distillate.

## Related

- [[20_distillates/documents/tei-p5-att.canonical-4.12.0]]
- [[20_distillates/documents/tei-p5-guidelines-nd-4.12.0]]
