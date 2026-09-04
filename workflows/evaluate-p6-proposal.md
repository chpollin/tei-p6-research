# Workflow: evaluate a P6 proposal

Use this workflow to assess a future-model proposal against grounded P5 behavior. Start with `contexts/manifests/p6-evaluation.yml`.

## Inputs

- The proposal, named as a local author posit or an attributed external proposal.
- Explicit evaluation criteria, such as conceptual coherence, expressivity, interoperability, migration cost, implementability or governance feasibility.
- The P5 release used as baseline.

## Procedure

1. Rewrite the proposal into separable design decisions without changing its intent.
2. For each decision, list the P5 behavior it intends to preserve, replace or remove. Ground those baseline descriptions in the canonical chain.
3. Test the alleged P5 problem against representative modules and counterexamples. Historical growth or complexity alone does not establish a defect.
4. Evaluate each decision against the declared criteria. Keep facts, inferences and preferences visibly separate.
5. Model migration explicitly: source P5 constructs; target representation; reversible and lossy cases; customization impact; validation and tooling consequences.
6. Seek disconfirming cases, especially overlapping structures, manuscript description, critical apparatus, dictionaries, spoken data and project-specific ODD customizations where relevant.
7. Trace any claim of community agreement, planned P6 work or official direction through `workflows/trace-issue-decision.md` with an `as_of` date.
8. Report: proposal; grounded P5 baseline; benefits by criterion; costs and regressions; migration matrix; counterexamples; unknowns; recommendation.

## Grounding discipline

The proposal and recommendation are posits unless the output is reporting an attributed source's proposal. Do not encode a preferred design as a TEI assertion. Claims about existing P5 behavior may become assertions only through the normal source, distillate and assertion chain.

## Done when

Every stated P5 limitation is grounded, major counterexamples and migration losses are visible, official-future claims are dated, and the final recommendation is clearly marked as a reasoned posit rather than established TEI fact.
