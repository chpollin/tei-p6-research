# Workflow: compare P5 releases

Use this workflow for two explicitly pinned P5 releases or commits. Start with `contexts/manifests/release-comparison.yml`.

## Procedure

1. Record both version identifiers, source locations and checksums or commit SHAs. Refuse a floating `latest` comparison.
2. Bound the comparison: whole release, module, element, class, schema behavior, Guidelines prose or issue set.
3. Compare like with like using deterministic tools where possible. Keep raw file or XML differences separate from interpreted model changes.
4. Classify each observed change: documentation-only; declaration; membership/inheritance; content model; attribute/datatype; constraint; deprecation; example; processing/tooling; unknown.
5. Validate a minimal before/after example when claiming changed document validity or migration behavior.
6. Use release notes and traced decisions for rationale. A commit diff establishes what changed, not why.
7. State compatibility effects separately: accepted documents, generated schemas, query or transformation behavior, customization impact and information loss. Mark untested effects as posits.
8. Produce a change table with one row per atomic difference and direct anchors for both sides, followed by unchanged assumptions and open questions.

## Done when

Both sides are reproducibly pinned, every semantic claim is narrower than its evidence, rationale is sourced independently from the diff, and claimed compatibility effects are tested or explicitly provisional.
