---
title: Project
project:
  name: "TEI P6 Research"
  repository: "tei-p6-research"
method:
  name: Promptotyping
  url: https://dhcraft.org/Promptotyping/
profile:
  name: Grounded Vault
  url: https://github.com/DigitalHumanitiesCraft/grounded-vault
status: draft
language: en
created: "2026-09-06"
updated: "2026-09-06"
related: [INDEX, specification, data, governance, plan, state, journal]
---

# Project

TEI P6 Research is an independent project that develops and evaluates an
abstract text model for a possible next TEI generation. It asks which
concepts, identities, relations and rules support practical encoding and
interpretation. The investigation covers P5 declarations, ODD customization,
Guidelines prose, processing and documented use, and it examines demonstrated
problems together with the capabilities that a redesign must preserve.
Textual scholarship and alternative models challenge the proposed categories.
Repair within P5, compatible evolution, architectural replacement and
deferral face the same evaluation criteria.

The project is unofficial and has no standing within the TEI Consortium.
Official TEI P6 records are research sources for it, and the proposals
developed here are its own recommendations. The requirements that bind the
work are in [[knowledge/specification]], the material in [[knowledge/data]],
the remaining milestones in [[knowledge/plan]] and the current holdings in
[[knowledge/state]].

## Project proposition

The project develops and evaluates an abstract text model for a possible TEI
P6. Its concepts, identities, relations and rules must support practical
encoding and processing. The model states its scope and makes its choices
traceable to source findings, declared assumptions and reproducible tests.

P5 supplies a normative baseline, successful patterns, demonstrated problems
and migration obligations. Text-theoretical scholarship, alternative models
and documented editorial practice must supply additional requirements and
counterexamples. Reproducing P5 coherently does not by itself establish that
a candidate adequately models text across the declared use contexts.

Repair within P5, compatible evolution, major-version redesign and deliberate
non-change remain comparable options until the evidence narrows them.

## Problem statement

TEI P5 is simultaneously a vocabulary, a customization system, a formal
schema source, a body of prose Guidelines, a governance process, an
implementation ecosystem and a set of community practices. These surfaces
establish different facts. ODD declarations alone do not explain editorial
use, and a discussion record does not establish a released capability. The
source-authority table in [[knowledge/data]] defines these limits. The
research must connect the relevant records without treating their authority
as interchangeable.

## Intended outcome

The programme produces four connected outcomes.

1. A version-bound formal and conceptual atlas of TEI P5.
2. An auditable history of problems, decisions, implementations and releases.
3. Formally specified P6 alternatives with bindings, examples and migration
   behavior.
4. A reasoned recommendation that exposes evidence, counterevidence,
   trade-offs, uncertainty and adoption costs.

The intended integrating text is an independent Proposal for TEI P6. It
combines a P5 model atlas, decision history, grounded requirements and
successful patterns, an abstract model, evaluated alternatives and migration
studies. Executable prototypes test the central claims. Recommendations name
their evidence, counterevidence, costs and open questions, together with the
conditions that would reverse them. P5 reconstruction and migration are
essential baselines, and independent theoretical and editorial sources must
challenge whether the proposed text concepts are adequate for their declared
scope. The deliverables table in [[knowledge/specification]] states locations
and acceptance conditions.

The output genre is an English scholarly synthesis and design specification
for researchers, scholarly editors, standards maintainers, educators and tool
builders. The public workbench opens with the full technical proposal.
Examples branch into comparisons of P5 variants and candidate bindings. Model
presents the formal definition and class relationships, Materials the
acquisition inventory, Knowledge the admitted artifacts and provenance chain,
and About the project documents. These views use one layout and canonical
repository inputs. Publication creates neither evidence nor an official TEI
decision.

## Research questions

The central question is which distinctions among textual objects, their
representations and editorial claims are needed for the declared tasks.
Generality is relative to an explicit range of text forms and practices. The
project does not attempt to model every subject that a text can discuss.
Domain-specific descriptions may connect to other models through explicit
relations. Text identity, carriers, transcription, interpretation and version
continuity remain questions that an element inventory alone cannot settle.

### RQ1. What is the P5 model?

What conceptual entities, element and attribute classes, modules, macros,
datatypes, constraints, content models, customization mechanisms and prose
rules constitute the selected P5 release? Where do the prose model, ODD model
and generated schemas align or diverge?

### RQ2. How did the model develop?

Which structures are inherited from earlier TEI generations, which were added
or revised during P5, and which constraints reflect historical technology,
compatibility, governance or use-case decisions?

### RQ3. Where is friction demonstrated?

Which difficulties are evidenced by repeated issues, workarounds, divergent
customizations, processing complexity, teaching problems, interoperability
failures or migration experience? Which alleged problems are isolated
preferences or remain unsupported?

### RQ4. What already works and must be preserved?

Which P5 capabilities, identifiers, customization patterns, interchange
contracts, community conventions and processing expectations provide durable
value? What would be lost under each redesign option?

### RQ5. What is the official P6 process deciding?

Which goals, agreements, disagreements, prototypes and constraints are
documented by the official TEI P6 process? What remains exploratory? Official
records are reported as such and are never conflated with this independent
project's recommendations.

### RQ6. Which architecture options perform best?

How do incremental P5 repair, compatibility-preserving evolution and a major
P6 redesign compare across the evaluation dimensions in
[[knowledge/specification]]? Which decisions require prototypes or empirical
tests rather than textual argument?

### RQ7. How can change be adopted?

What mappings, compatibility modes, migration tools, version declarations,
validation contracts, governance processes and educational materials would be
required for existing projects and software to adopt a new architecture?

## Research object and temporal scope

The project keeps four states distinct.

| State | Role |
|---|---|
| P5 4.12.0 | immutable normative baseline pinned to an exact release commit |
| P5 development | moving observations pinned to full commits and dates, without normative force |
| historical TEI | earlier releases and records interpreted in their contemporary context |
| official P6 process | current process records and artifacts, whose normativity is left open |

The primary baseline is TEI P5 4.12.0 at commit
`113e933e21f016e2655518321e9d10214b8d9fcb`, recorded in
`sources/locks/tei-p5-4.12.0.yaml`. The alias `current` and a moving branch
name are never used as evidence identities.

Every module in that baseline is in scope for investigation. Module
inventory, source interpretation, formal requirements and executed cases
remain separate coverage measures. Document types, media forms and textual
phenomena are cross-cutting dimensions rather than equivalents of P5 modules
or model classes.

The project studies P5 and official P6 records globally where sources permit.
Corpus completeness is always bounded by the interfaces, dates, languages,
rights and search protocols recorded under `sources/` and defined in
[[knowledge/data]].

## Non-goals

- Declaring the official TEI P6 architecture on behalf of the TEI Consortium.
- Treating every P5 feature or historical layer as a defect.
- Designing from issue frequency alone.
- Copying the whole web or every third-party paper into Git.
- Claiming recovery of deleted, private, overwritten or inaccessible records.
- Equating issue closure, Council discussion, merge and release.
- Replacing human domain verification with agent consensus.
- Producing a final P6 schema before evaluation criteria and evidence paths
  are operational.
