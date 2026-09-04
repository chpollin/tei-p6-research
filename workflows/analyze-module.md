# Workflow: analyze a TEI module

Use this workflow for one named P5 module in one declared release. Start with `contexts/manifests/module.yml`.

## Procedure

1. Fix the module identifier and release or commit before collecting facts.
2. Enter through relevant topic maps and retrieve existing module-level assertions.
3. Establish from pinned declarations: module purpose, elements and classes it defines, dependencies, class memberships, macros and constraints.
4. Select representative elements by modeling role, not merely alphabetically. Use `workflows/analyze-element.md` for details that affect the module conclusion.
5. Map cross-module dependencies explicitly and distinguish mandatory dependency, shared class membership and common co-use.
6. Compare formal declarations with Guidelines prose and documented examples. Record mismatches as questions or grounded contested material, not silent corrections.
7. Trace historical explanations or unresolved design tensions only through dated issues, PRs, governance records and releases.
8. Report: scope; formal inventory; recurring patterns; dependencies; internal variations; historical changes; known tensions; open questions.

## Guardrails

- Do not claim that an inventory is complete unless its extraction scope and pinned source are known.
- Do not turn common usage into normative semantics without an appropriate source.
- Do not infer a module-wide rule from one element.
- Persistent synthesis follows the canonical ingest, distill and assertion operations.

## Done when

The inventory has a declared boundary, representative claims resolve through the canonical chain, cross-module effects are qualified, and every gap is explicit.
