# Context router

Choose the narrowest route that answers the task. A manifest is a read recipe, not a source.

| Intent | Manifest | Workflow | Expand when |
|---|---|---|---|
| Understand one TEI element | `contexts/manifests/element.yml` | `workflows/analyze-element.md` | Content model, class inheritance, examples or history are load-bearing |
| Understand one TEI module | `contexts/manifests/module.yml` | `workflows/analyze-module.md` | Cross-module dependencies or representative elements need checking |
| Explain an issue, PR or design decision | `contexts/manifests/issue-decision.yml` | `workflows/trace-issue-decision.md` | Claimed outcome requires merge, release or normative confirmation |
| Compare two P5 releases | `contexts/manifests/release-comparison.yml` | `workflows/compare-releases.md` | A syntactic diff may imply a semantic or compatibility claim |
| Assess a P6 design proposal | `contexts/manifests/p6-evaluation.yml` | `workflows/evaluate-p6-proposal.md` | The proposal depends on a claimed P5 defect, user need or migration cost |
| General question from the vault | no special manifest | `knowledge/operations.md` § Query | An exact quotation or source-level distinction matters |
| Add, distill or synthesize sources | no context shortcut | matching section of `knowledge/operations.md` | Always follow the complete canonical operation |

If a task spans routes, complete the most evidence-sensitive route first and record the handoff points. Do not load every manifest by default.
