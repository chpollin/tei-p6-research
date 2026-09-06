---
type: distillate
source-type: document
representation: "[[10_markdown/documents/tei-p5-state-4.12.0]]"
topics: ["[[Metadata and Entities]]"]
status: grounded
checked:
  validation: 2026-09-06
created: 2026-09-06
updated: 2026-09-06
---

# Distillate: TEI P5 4.12.0 state specification

This distillate reports the English element description and the English remarks paragraph carried by the complete `state.xml` specification at the pinned TEI P5 4.12.0 release commit.

## Core statements

- In TEI P5 4.12.0, the English description of `state` states that the element contains a description of some status or quality. [[10_markdown/documents/tei-p5-state-4.12.0#^r1]] ^s1
- In TEI P5 4.12.0, the English description of `state` states that the status or quality the element describes is one attributed to a person, place, or organization. [[10_markdown/documents/tei-p5-state-4.12.0#^r1]] ^s2
- In TEI P5 4.12.0, the English description of `state` states that the status or quality is attributed often at some specific time or for a specific date range. [[10_markdown/documents/tei-p5-state-4.12.0#^r1]] ^s3
- In TEI P5 4.12.0, the English remarks for `state` state that where there is confusion between `trait` and `state`, the more general purpose element `state` should be used even for unchanging characteristics. [[10_markdown/documents/tei-p5-state-4.12.0#^r2]] ^s4
- In TEI P5 4.12.0, the English remarks for `state` state that, where a distinction is wished between characteristics that are generally perceived to be time-bound states and those assumed to be fixed traits, `trait` is available for the more static of these. [[10_markdown/documents/tei-p5-state-4.12.0#^r2]] ^s5
- In TEI P5 4.12.0, the English remarks for `state` state that the `state` element encodes characteristics which are sometimes assumed to change, often at specific times or over a date range. [[10_markdown/documents/tei-p5-state-4.12.0#^r2]] ^s6
- In TEI P5 4.12.0, the English remarks for `state` state that the `trait` elements are used to record characteristics, such as eye-colour, which are less subject to change. [[10_markdown/documents/tei-p5-state-4.12.0#^r2]] ^s7
- In TEI P5 4.12.0, the English remarks for `state` state that traits are typically, but not necessarily, independent of the volition or action of the holder. [[10_markdown/documents/tei-p5-state-4.12.0#^r2]] ^s8

## Terms

- **state**: the element described as containing a description of some status or quality attributed to a person, place, or organization, often at some specific time or for a specific date range. [[10_markdown/documents/tei-p5-state-4.12.0#^r1]]
- **trait**: the element the remarks hold available for the more static characteristics, used to record characteristics, such as eye-colour, which are less subject to change. [[10_markdown/documents/tei-p5-state-4.12.0#^r2]]

## Open questions

- Which source establishes through which attributes a `state` records the specific time or date range that its description and its remarks speak of, given that this specification declares the membership `att.datable` in the `classes` element of its XML alone and no English reading block names any attribute of the element?
- Which source establishes what the membership `att.naming` contributes to `state`, meaning whether and how the element itself points at the person, place or organization whose status or quality it describes, given that this specification declares that membership in the XML alone?
- Which source establishes what the remaining declared memberships contribute, meaning `att.global`, `att.cmc`, `att.dimensions`, `att.editLike` and `att.typed`, given that this specification declares them in the XML alone and its English text mentions no attribute?
- Which source states in English what a `state` may contain, given that this specification declares its content model only inside the XML, as any number of `precision` elements followed by an alternation of one or more nested `state` elements, a sequence of `model.headLike`, `model.pLike` and `model.noteLike` or `model.biblLike` members, or any number of `model.labelLike`, `model.noteLike` and `model.biblLike` members?
- Which source explains what a `state` nested inside another `state` records, and what a `precision` inside a `state` records, given that both possibilities follow from the XML content model alone and no English reading block mentions either?
- Which source establishes where a `state` may stand in a document, given that this specification declares only the memberships `model.orgStateLike`, `model.persStateLike` and `model.placeStateLike` in its XML and its English text names no containing element?
- What do the four examples of this specification demonstrate, meaning the English `state` with `ref` and `type="status"` carrying a `label`, the English organization whose two membership states carry `from`, `to` and `notBefore`, the French `state` with `cert`, `type="social"`, `from` and `to`, and the Chinese `state` with `ref` and `type="status"`, given that the reading projection reproduces descriptions and remarks alone and none of the examples carries accompanying English prose?
- Which source establishes what `trait` is and what it may contain, given that this specification names the element in its remarks alone and carries no specification of it?
- Which source establishes whether a `state` must be time-bounded at all, given that the description states the attribution happens often at some specific time or for a specific date range and the remarks state that the encoded characteristics are sometimes assumed to change?
- How do the "status or quality" of the description and the "characteristics" of the remarks relate, and who is the "holder" whose volition or action the remarks name in their closing sentence, given that this specification introduces the three terms without connecting them?
- Which Guidelines sections do the `listRef` pointers `#NDPERSbp` and `#NDPERSEpc` resolve to, and what do the further XML declarations of this specification contribute, meaning `module="namesdates"`, `xml:id="gi-state"`, `ident="state"` and the English gloss "state", given that no English reading block carries them?
- What do the non-English descriptions of this specification state, and how is it to be read that its Spanish and Italian descriptions describe a component of a canonical reference defined by the milestone method rather than a status or quality, given that the reading blocks reproduce the English text alone?

## Appraisal

The English text of this specification settles what a `state` is for and how it is delimited against `trait`, and it does so twice over, once as the description of the element and once as guidance in the remarks. The temporal qualification stays soft in both places, worded as "often" and "sometimes", so the source supports the intention of a time-bounded description while leaving open whether an untimed `state` is defective. Everything that would make that intention executable lives in the XML declarations, meaning the datable attributes, the naming attributes, the recursive content model and the three model classes that decide where the element may stand, and none of it is reachable through the English reading projection. The remarks are the only place in the source where the boundary against `trait` is drawn, and the criterion they use is how far a characteristic is perceived to change.

## Related

- [[30_assertions/MOC-Metadata and Entities]]
