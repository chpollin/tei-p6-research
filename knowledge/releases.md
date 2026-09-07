---
title: Research versions
project:
  name: "TEI P6 Research"
  repository: "tei-p6-research"
method:
  name: Promptotyping
  url: https://dhcraft.org/Promptotyping/
status: draft
language: en
created: "2026-09-07"
updated: "2026-09-07"
related: [INDEX, project, architecture, text-model, ontology, hsa-profile, testing, state, handoff, journal]
---

# Research versions

A repository version identifies one reproducible research baseline. Its
annotated Git tag resolves to the complete source tree, documentation,
examples and generated outputs. Version numbers for individual models and
bindings remain separate. A repository tag grants no scholarly acceptance
and makes no claim about an official TEI release.

## v0.1.0 — First consolidated research baseline

Baseline date: 2026-09-07. Repository tag: `v0.1.0`.

The baseline brings together the abstract-model work, the ontology and
the complete HSA letter experiment with the previously prepared P5 structure
study and source-navigation changes. Existing review records retain their
individual provenance and status.

| Included result | Entry point and scope |
|---|---|
| Abstract-model proposal | [Chapter 02](../40_output/02-abstract-model.md) defines and argues the model, with nine source premises and twenty-five explicit posits. |
| Conceptual design | [[knowledge/model-design]] separates text identity, representations, referents, names, mentions, classifications and attributed propositions. |
| Documentary ontology | [[knowledge/ontology]] defines the 21 record classes and 28 properties; the hierarchy and RDF serializations reproduce. External alignments remain comparison candidates. |
| Six illustrative cases | [[knowledge/model-examples]] provides matching XML, JSON and RDF views under its own example contract. |
| Executable candidates | [[knowledge/text-model]] defines model 0.1 and entity extension 0.2; [[knowledge/text-model-bindings]] states their respective exchange limits. |
| Real source cases | [[knowledge/identity-evidence]] examines catalogue identity and source attribution. [[knowledge/hsa-profile]] defines the complete HSA letter mapping and its semantic and preservation components. |
| P5 source basis | The 888-source Guidelines intake, XML export and navigation reproduce. The structure study contributes twelve distillates and twenty-four assertions awaiting source-support review. |
| Human and agent entry points | [README](../README.md), the harness adapters and [[knowledge/INDEX]] route into the same maintained project knowledge. |

### Version boundaries

- Repository `0.1.0` identifies this research baseline.
- Abstract Text Model `0.1` supports its JSON/XML/YAML bindings.
- Entity extension `0.2` has JSON packages and a separate one-way RDF export.
- HSA profile `1` uses compact binding `2`; the reader also accepts
  complete binding-`1` files. The union of `p6.*` and
  `preservation.*` reconstructs the complete case graph.

### Validation and open limits

The baseline incorporates the session's passing full suite of 1,620 tests,
with one platform-dependent skip and ten known RDFLib deprecation warnings.
The final HSA and page reproduction pass covered 102 tests. These results
establish the checked implementation and artifact contracts. The version
closure also checks the tracked source and report dependencies; its current
local or published state belongs in [[knowledge/state]].

The following limits are retained explicitly.

- Revision checks in model 0.2 do not yet protect every unchanged claim
  from an indirect change of its referent or evidence. Concrete counterexamples
  and the next correction are in [[knowledge/handoff]].
- The newer structure and identity/evidence assertions still require
  independent source-support review. No human `verified` status is assigned.
- Representative P5 migration, full HSA-ODD conformance, historical acceptance,
  external ontology alignments and complete ontology reasoning remain open.
- Corpus coverage remains bounded by each source family's recorded scope.
  The unfinished Wayback intake has no completed manifest.

### Resume from this baseline

Read [[knowledge/state]], then the revision-dependency item in
[[knowledge/handoff]]. Its next substantive task is to specify and test
how unchanged claims retain their meaning when referenced records change.
The model proposal and real cases provide the material for that work.

To inspect this baseline without moving a working branch:

```sh
git show v0.1.0
git log -1 --format=fuller v0.1.0
```

Run the scope-specific completion gate in [[knowledge/testing]] when
continuing implementation. Ignored raw stores, credentials, virtual
environments and upstream Git mirrors are outside the version.
