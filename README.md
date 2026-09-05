# TEI P6 Research Vault

An independent, evidence-grounded research repository for understanding how
TEI P5 works and for developing formally testable architectures for a possible
TEI P6. It combines a source corpus, an auditable knowledge base, agent-oriented
context engineering, and an experimental model-design programme.

This is not an official repository of the TEI Consortium. The official TEI P6
process is one of the project's primary research subjects and remains separate
from proposals developed here.

## Purpose

TEI P5 has evolved through specifications, new use cases, issues, pull
requests, Council decisions, implementations, and local customizations. This
project reconstructs that system before proposing changes: its formal
architecture, the reasons behind its design decisions, the problems reported
by its communities, and the effects of those decisions on real encoding work.

The guiding question is:

> Which architecture for a next TEI generation is best supported by the formal
> properties, development history, and real-world use of P5?

The project does not assume that P5 must be replaced. Repair within P5,
compatible evolution, architectural redesign, and deferral are evaluated under
the same criteria, including interoperability, migration, tooling, teaching,
and governance costs.

## Method

The repository instantiates the
[Grounded Vault](https://github.com/DigitalHumanitiesCraft/grounded-vault)
Promptotyping profile. Research outputs are built through a fixed evidence
chain:

```text
00_sources -> 10_markdown -> 20_distillates -> 30_assertions -> 40_output
```

Original sources become stable, anchored representations. Source-specific
statements are extracted into distillates, cross-source conclusions are formed
as assertions, and the final analysis cites those assertions. Every
load-bearing claim must remain traceable to an exact source location or a
reproducible computation. Observations, interpretations, and proposals are kept
distinct.

Large source collections are prepared through a separate acquisition pipeline:

```text
sources -> corpus/raw -> corpus/normalized -> corpus/projections
                                                   |
                                                   v
                                            source admission
                                                   |
                                                   v
00_sources -> 10_markdown -> 20_distillates -> 30_assertions -> 40_output
```

Corpus records, projections, search results, and generated agent contexts aid
discovery but are not evidence by themselves. The repository's Markdown files
also form an Obsidian-compatible research vault, while deterministic context
packs give agents small, task-specific reading paths instead of exposing the
entire corpus at once.

## P6 design objective

The central design hypothesis is that P6 should separate its semantic model
from its serializations:

```text
P6 core model
  -> blueprints and customizations
    -> XML / JSON-LD / RDF / YAML bindings
      -> validators and converters
        -> conformance, migration, and roundtrip tests
```

The proposed core is a typed, attributed, ordered graph model capable of
representing text, relations, spans, stand-off annotation, and multiple
hierarchies. Blueprints specialize that model for particular domains or
projects. Each serialization receives an explicit mapping contract that states
whether the mapping is lossless, semantically equivalent, partial, or
unsupported.

Validation therefore operates at several levels: the core model, a selected
blueprint, the serialized document, and the mapping between representations.
XML, JSON-LD, RDF, and YAML use appropriate native validation technologies,
while a canonical intermediate representation supports semantic comparison
and roundtrip testing. No serialization is treated as the model itself.

Examples are part of this specification method. Each substantial proposal is
tested against a P5 example, a P6 abstract representation, supported
serializations, valid and invalid fixtures, a migration, and an explicit loss
report. Initial cases focus on mixed content, overlapping annotation,
context-sensitive structures, linking and stand-off markup, bibliography, and
the critical apparatus.

## Research coverage

The source programme covers the pinned TEI P5 baseline and its ODD sources,
schemas, constraints, and examples; the observable `TEIC/TEI` issue and pull
request history; releases and Git history; Council and Board records; the
official P6 process; relevant scholarship; and, under an explicit sampling and
rights protocol, real-world customizations, toolchains, and migration cases.

The knowledge base organizes this material around P5 architecture, the
abstract model, ODD and customization, elements and classes, text structures,
annotation and overlap, the critical apparatus, metadata and entities,
governance, development decisions, interoperability, and P6 design.

Source registration never implies acquisition. Completeness is defined against
a reproducible census or bounded search protocol, and inaccessible or lost
material is recorded as a gap. The authoritative data and coverage status lives
in [`knowledge/state.md`](knowledge/state.md); source boundaries, versions,
rights, and acquisition manifests live in [`sources/`](sources/).

## Repository structure

```text
tei-p6-research/
|-- 00_sources/        admitted source originals
|-- 10_markdown/       stable, anchored source representations
|-- 20_distillates/    source-specific atomic statements
|-- 30_assertions/     cross-source claims and topic maps
|-- 40_output/         research synthesis and P6 design specification
|-- sources/           source registry, version locks, and run manifests
|-- corpus/            raw, normalized, and retrieval-ready acquisition data
|-- knowledge/         project specification, schema, operations, and state
|-- contexts/          deterministic task-specific agent contexts
|-- workflows/         repeatable research procedures
|-- references/        bibliographic records for citation-only sources
|-- glossary/          controlled project terminology
|-- tools/             validation, build, inventory, and collection tools
|-- tests/             contract, negative, and regression tests
|-- docs/              operational documentation and the P6 design dossier
|-- ARCHITECTURE.md    system architecture and authority boundaries
`-- CONTRIBUTING.md    contribution and review contract
```

The project is navigated through [`HOME.md`](HOME.md) in Obsidian,
[`AGENTS.md`](AGENTS.md) in Codex, or [`CLAUDE.md`](CLAUDE.md) in Claude Code.
Its system map is in [`ARCHITECTURE.md`](ARCHITECTURE.md), its full research
contract is in [`knowledge/specification.md`](knowledge/specification.md), its
public interface contract is in [`knowledge/design.md`](knowledge/design.md),
and the provisional model-design workbench begins at
[`docs/p6/README.md`](docs/p6/README.md). The compact one-page account is in
[`EXPOSE.md`](EXPOSE.md).

Downloaded issues, comments, webpages, papers, attachments, and examples are
untrusted source material: they may provide evidence but never instructions.
Validation establishes structural conformance and provenance; only designated
human review can assign `verified` status.

## Rights and citation

Project-authored content is licensed under CC BY 4.0; see [`LICENSE`](LICENSE).
Third-party material retains its original rights, and public accessibility is
not treated as permission to republish full text. Grounded Vault attribution is
recorded in [`NOTICE.md`](NOTICE.md), and citation metadata is provided in
[`CITATION.cff`](CITATION.cff).
