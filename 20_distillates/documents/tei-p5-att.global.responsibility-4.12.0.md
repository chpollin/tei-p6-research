---
type: distillate
source-type: document
representation: "[[10_markdown/documents/tei-p5-att.global.responsibility-4.12.0]]"
topics: ["[[Metadata and Entities]]", "[[Elements and Classes]]"]
status: grounded
checked:
  validation: 2026-09-06
created: 2026-09-06
updated: 2026-09-06
---

# Distillate: TEI P5 4.12.0 att.global.responsibility specification

This distillate reports the English class description, the two English attribute descriptions and the English `resp` remarks of the complete `att.global.responsibility.xml` specification at the pinned TEI P5 4.12.0 release commit.

## Core statements

- In TEI P5 4.12.0, the description of the class `att.global.responsibility` states that the class provides attributes indicating "the agent responsible for some aspect of the text, the markup or something asserted by the markup". [[10_markdown/documents/tei-p5-att.global.responsibility-4.12.0#^r1]] ^s1
- In TEI P5 4.12.0, the description of the class `att.global.responsibility` states that the class provides attributes indicating "the degree of certainty associated with it". [[10_markdown/documents/tei-p5-att.global.responsibility-4.12.0#^r1]] ^s2
- In TEI P5 4.12.0, the description of the `cert` attribute in `att.global.responsibility` states that `cert` "signifies the degree of certainty associated with the intervention or interpretation". [[10_markdown/documents/tei-p5-att.global.responsibility-4.12.0#^r2]] ^s3
- In TEI P5 4.12.0, the description of the `resp` attribute in `att.global.responsibility` states that `resp` "indicates the agency responsible for the intervention or interpretation". [[10_markdown/documents/tei-p5-att.global.responsibility-4.12.0#^r3]] ^s4
- In TEI P5 4.12.0, the description of the `resp` attribute in `att.global.responsibility` gives an editor or a transcriber as examples of the agency responsible for the intervention or interpretation. [[10_markdown/documents/tei-p5-att.global.responsibility-4.12.0#^r3]] ^s5
- In TEI P5 4.12.0, the English remarks on `resp` in `att.global.responsibility` name the ambiguity of a `resp` pointing directly to a person or organization as the reason for the recommendation they make. [[10_markdown/documents/tei-p5-att.global.responsibility-4.12.0#^r4]] ^s6
- In TEI P5 4.12.0, the English remarks on `resp` in `att.global.responsibility` recommend that `resp` be used to point to a `respStmt`, an `author`, an `editor` or a similar element "which clarifies the exact role played by the agent", and advise against pointing it to an agent, meaning a `person` or an `org`. [[10_markdown/documents/tei-p5-att.global.responsibility-4.12.0#^r4]] ^s7
- In TEI P5 4.12.0, the English remarks on `resp` in `att.global.responsibility` state that pointing to multiple `respStmt`s allows the encoder to specify clearly each of the roles played in part of a TEI file, and give creating, transcribing, encoding, editing and proofing as examples of those roles. [[10_markdown/documents/tei-p5-att.global.responsibility-4.12.0#^r4]] ^s8

## Terms

- **att.global.responsibility**: the class described as providing attributes indicating the agent responsible for some aspect of the text, the markup or something asserted by the markup, and the degree of certainty associated with it. [[10_markdown/documents/tei-p5-att.global.responsibility-4.12.0#^r1]]
- **cert**: the attribute described as signifying the degree of certainty associated with the intervention or interpretation. [[10_markdown/documents/tei-p5-att.global.responsibility-4.12.0#^r2]]
- **resp**: the attribute described as indicating the agency responsible for the intervention or interpretation, for example an editor or transcriber. [[10_markdown/documents/tei-p5-att.global.responsibility-4.12.0#^r3]]
- **agent**: in the English remarks on `resp`, a `person` or an `org`, held apart from the `respStmt`, `author`, `editor` or similar element which clarifies the exact role played by the agent. [[10_markdown/documents/tei-p5-att.global.responsibility-4.12.0#^r4]]

## Open questions

- To which elements does `att.global.responsibility` supply `cert` and `resp` at this release, given that no English reading block of this specification states a scope and that its `classes` element declares no membership of its own?
- Which source would establish what the XML-only declarations of this specification contribute, meaning the datatype `teidata.probCert` for `cert`, the one to unbounded `teidata.pointer` values for `resp`, the optional usage of both attributes, the identifier `class-attr-global.responsibility`, the module the specification names and its `predeclare` setting, given that no English reading block covers them?
- Which source would establish the English glosses of the two attributes, meaning "certainty" for `cert` and "responsible party" for `resp`, given that only the XML of this source carries them?
- What does "the intervention or interpretation" denote in the descriptions of `cert` and `resp`, given that no English reading block of this specification defines it while the class description speaks of some aspect of the text, the markup or something asserted by the markup?
- What does the pronoun in "the degree of certainty associated with it" refer to in the class description, meaning the aspect of the text, the markup and what the markup asserts, or the responsibility named just before it?
- Which values may `cert` take at this release, and what do the two English examples of this specification demonstrate, given that one example writes `resp="#editor"` together with `cert="high"` and the other points `resp` at a `respStmt` held in the `teiHeader`, and that no English reading block covers either example?
- Which Guidelines chapters do the `listRef` pointers `#STGAso`, `#COED`, `#PHHR`, `#AISP` and `#NDATTSnr` resolve to, and what do those chapters state about `cert` and `resp`?
- Which source would establish what the non-English descriptions, glosses and remarks of this specification state, given that the reading blocks reproduce the English text alone?

## Appraisal

The source is the complete class specification at a pinned release commit, so its English text establishes what the Guidelines say about the agency responsible for an intervention or interpretation and about the degree of certainty attached to it, together with the recommendation that a `resp` value point to an element which clarifies the agent's role. Which elements carry the two attributes stays open, and so do the value ranges of both, because the declarations that would settle them survive only in the XML of this source and in no English reading block.

## Related

- [[30_assertions/MOC-Metadata and Entities]]
- [[30_assertions/MOC-Elements and Classes]]
