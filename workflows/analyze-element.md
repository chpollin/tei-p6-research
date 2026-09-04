# Workflow: analyze a TEI element

Use this workflow for one exact TEI element in one declared P5 release. Start with `contexts/manifests/element.yml`.

## Inputs

- Exact expanded element name, including namespace where ambiguity is possible.
- P5 release or commit. Use the vault's active pinned release when the user does not request another one.
- Requested facets, or the default facets below.

## Procedure

1. Enter through the matching topic map and collect existing assertions. Follow only relevant grounding chains.
2. Establish the element's formal identity from the pinned ODD or generated schema: owning module, classes, inherited attributes, content model, datatype or constraints, and documented availability.
3. Establish its prose semantics separately from its formal declaration. Do not infer intended meaning solely from element or class names.
4. Inspect examples only for the behavior they demonstrate. An example does not prove exhaustiveness or preferred practice unless the prose says so.
5. Trace deprecation, replacement or historical rationale through `workflows/trace-issue-decision.md` when such a claim matters.
6. Test relevant boundary cases against the pinned schema when validation behavior is part of the question. Record the exact schema and command.
7. Report under these headings: identity; semantic purpose; formal model; interactions; representative patterns; version scope; open questions.

## Grounding discipline

- A generated declaration proves the declaration in that pinned build, not its rationale.
- Guidelines prose may explain intention but does not replace the executable content model when validation behavior is claimed.
- GitHub discussions establish attributed proposals. Require merged and released evidence before saying TEI changed.
- If persistent notes are requested, acquire and ingest any missing source, distill it, then synthesize atomic assertions. Do not write directly from raw `corpus/` material into `30_assertions/`.

## Done when

Every requested facet is either grounded with release-specific support or named as an open question; the element is not generalized beyond the inspected release or customization; required validation has run.
