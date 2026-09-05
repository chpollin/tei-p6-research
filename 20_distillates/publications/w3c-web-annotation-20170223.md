---
type: distillate
source-type: publication
reference: w3c-web-annotation-20170223
topics: ["[[Abstract Model]]", "[[Annotation and Overlap]]"]
status: validated
checked:
  quote: 2026-09-05
  validation: 2026-09-05
  machine-review: 2026-09-05
created: 2026-09-05
updated: 2026-09-05
---

# Distillate: Web Annotation Data Model, 2017 Recommendation

This distillate examines one rule for multiple Text Quote Selector matches.

## Core statements

- The W3C 2017 Web Annotation Data Model recommends treating multiple Text Quote Selector matches as matching all the discovered sequences. ^s1
  > "the user agent discovers multiple matching text sequences, then the selection SHOULD be treated as matching all of the matches." (https://www.w3.org/TR/2017/REC-annotation-model-20170223/, section 4.2.4, Text Quote Selector)

## Terms

No additional term definition is extracted in this bounded intake.

## Open questions

- Which intended annotation tasks require one target rather than all matching sequences?
- What normalization and State requirements must a later conformance comparison include?

## Appraisal

The rule challenges the pilot's unique-only selector policy. It does not
establish the correct policy for every editorial task or validate an
interpretation after editing. The citation refers to an independent technical
standard, not TEI policy. Copyright 2017 W3C (MIT, ERCIM, Keio, Beihang);
[document use notice](https://www.w3.org/copyright/document-license-2015/).

## Related

- [[20_distillates/documents/tei-p5-annotation-4.12.0]]
