---
type: glossary
term: "Responsibility for a statement"
created: 2026-09-06
updated: 2026-09-06
---

# Responsibility for a statement

Responsibility for a statement names the agent who stands behind something the markup
asserts, together with the certainty the agent attaches to it, the kind of evidence behind it
and the source it is drawn from, so that statements by different agents about the same matter
can stand side by side. In TEI P5 4.12.0 the classes `att.global.responsibility`,
`att.editLike` and `att.global.source` provide `resp`, `cert`, `evidence` and `source` for this.
[[10_markdown/documents/tei-p5-att.global.responsibility-4.12.0#^r1]]

## Examples

<!-- examples:begin -->
- [[30_assertions/p5-att-global-responsibility-indicates-the-agent-responsible-for-something-asserted-by-the-markup]] — In TEI P5 4.12.0, the description of att.global.responsibility states that the class provides attributes indicating the agent responsible for some aspect of the text, the markup or something asserted by the markup
  - [[20_distillates/documents/tei-p5-att.global.responsibility-4.12.0#^s1]]
- [[30_assertions/p5-evidence-indicates-the-nature-of-the-evidence-supporting-an-intervention-or-interpretation]] — In TEI P5 4.12.0, the description of evidence in att.editLike states that it indicates the nature of the evidence supporting the reliability or accuracy of the intervention or interpretation
  - [[20_distillates/documents/tei-p5-att.editlike-4.12.0#^s2]]
- [[30_assertions/p5-nested-description-elements-inherit-type-and-responsibility-and-may-date-more-precisely]] — In TEI P5 4.12.0, the Guidelines state that state, trait and other elements of the same class can be nested hierarchically with type values cumulatively inherited, that responsibility is not additive so an element either states it explicitly or inherits it from its nearest ancestor, and that a child element may specify a date more precisely than its parent
  - [[20_distillates/documents/tei-p5-guidelines-nd-4.12.0#^s50]]
- [[30_assertions/p5-resp-should-point-to-an-element-that-clarifies-the-agents-role-rather-than-to-a-person-or-org]] — In TEI P5 4.12.0, the English remarks on resp in att.global.responsibility recommend pointing resp to a respStmt, an author, an editor or a similar element which clarifies the exact role played by the agent, and advise against pointing it to a person or an org
  - [[20_distillates/documents/tei-p5-att.global.responsibility-4.12.0#^s7]]
- [[30_assertions/p5-source-specifies-the-source-from-which-some-aspect-of-an-element-is-drawn]] — In TEI P5 4.12.0, the description of source in att.global.source states that it specifies the source from which some aspect of this element is drawn
  - [[20_distillates/documents/tei-p5-att.global.source-4.12.0#^s2]]
<!-- examples:end -->
