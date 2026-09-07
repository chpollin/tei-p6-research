# TEI P6 Research

An independent research repository for developing and evaluating an abstract
text model for a possible next generation of the Text Encoding Initiative
(TEI). It brings source-based analysis of P5 together with model proposals,
executable examples, and tests of their consequences for editions, language
corpora, and documentary catalogues.

The repository supports shared research by people and AI agents. It is
designed for use with a harness such as Claude Code, Codex, or pi, and for
direct reading, inspection, and contribution through Markdown and the web
workbench. Official TEI P6 records are sources for this independent project.
Its proposals are its own research contributions.

[Model proposal](40_output/02-abstract-model.md)
· [Architecture proposal](40_output/12-p6-design.md)
· [Web workbench](https://chpollin.github.io/tei-p6-research/)
· [Research state](knowledge/state.md)
· [Knowledge index](knowledge/INDEX.md)

Version `0.1.0` is the first consolidated research baseline. Its
[version record](knowledge/releases.md) identifies the included results,
model and binding versions, and known limits.

## Research goals

The central question is which objects, identities, relationships, and rules
a text model needs to support encoding, description, and interpretation across
editions, language corpora, and documentary catalogues.

- Understand P5's architecture and encoding practices, including the
  capabilities a successor must preserve and the problems supported by sources.
- Define an abstract model whose concepts and constraints can be explained,
  implemented, and challenged through concrete cases.
- Compare ways of exchanging and processing the same information, including
  their preservation limits and the decisions required to migrate P5 data.
- Evaluate repair within P5, compatible evolution, architectural replacement,
  and deferral under the same requirements and user tasks.

The [research charter](knowledge/project.md) develops these questions.
The [evaluation contract](knowledge/p6-evaluation.md) explains how alternatives
are compared, including customization, tooling, teaching, and governance.
Developed examples are compared in XML, JSON, and RDF. Each view states whether
it is an implemented binding, a proposed representation, or has explicit gaps.

## Central results

| Result | What it provides | Entry point |
|---|---|---|
| Abstract model proposal | A reasoned definition of text identity, fixed versions, selections, structural readings, and attributed claims, including the entity extension. | [Abstract Model](40_output/02-abstract-model.md) |
| Further model design | Proposed distinctions for text, name forms and uses, mentions, open classifications, proposition content and attributed stances. Six complete cases in XML, JSON and RDF. | [Model design](knowledge/model-design.md) · [Examples](knowledge/model-examples.md) |
| Documentary ontology | A small experimental record vocabulary, a generated class hierarchy and a separate external-mapping register. RDF/XML and JSON-LD reproduce the core RDF graph. | [Ontology contract](knowledge/ontology.md) · [Turtle](ontology/core.ttl) · [Class hierarchy](ontology/record-hierarchy.mmd) |
| Real P5/P6 letter case | An admitted HSA letter with its complete text and editorial notes, qualified metadata reports, and matching XML/JSON/RDF records. Compact semantic data and optional preservation data reconstruct one complete graph. | [HSA letter comparison](experiments/hsa_letter_4493/README.md) · [Profile and bindings](knowledge/hsa-profile.md) |
| Executable models and bindings | Validators, examples, and comparison rules for models 0.1 and 0.2. Version 0.1 has JSON/XML/YAML roundtrips; 0.2 has JSON packages and a separate one-way RDF export. | [Model contract](knowledge/text-model.md) · [Bindings](knowledge/text-model-bindings.md) |
| P5 analyses | Source-supported arguments about annotation, overlap, names, entities, and identification that motivate and challenge model decisions. | [Annotation and Overlap](40_output/06-annotation-and-overlap.md) · [Metadata and Entities](40_output/08-metadata-and-entities.md) |
| Editorial experiments | Synthetic counterexamples and bounded studies of edition fragments, catalogue records, and correspondence, with explicit mappings and unresolved cases. | [Experiments](knowledge/experiments.md) · [Identity and Evidence](knowledge/identity-evidence.md) |
| P5 source reference | Version-pinned Guidelines sources with declaration navigation and links to their research interpretation. | [Guidelines coverage](corpus/projections/guidelines-4.12.0.md) · [Knowledge browser](https://chpollin.github.io/tei-p6-research/knowledge.html) |
| Architecture proposal | An argument connecting model choices to customization, exchange, migration, and the comparison of P6 options. | [P6 Design](40_output/12-p6-design.md) |

These results have explicit research and test boundaries. Source availability,
formal validation, and domain acceptance are assessed separately.
Representative P5 migration and a justified architecture recommendation remain
open research requirements. The [current state](knowledge/state.md) records
completed checks, known model limitations, and gaps in the source corpus.

## Work with the repository

### Read, inspect, and contribute

Start with the [model proposal](40_output/02-abstract-model.md) to understand
what is being modeled and why. Read the
[architecture proposal](40_output/12-p6-design.md) for the wider argument.
The [model design](knowledge/model-design.md) collects the proposed extensions
and the distinctions that still require formalization and P5 comparison.

Use the [web workbench](https://chpollin.github.io/tei-p6-research/) to explore
comparative examples and follow claims to their sources. For local work,
browse the Markdown files or open the repository folder as an Obsidian vault.
The [knowledge index](knowledge/INDEX.md) connects research topics, definitions,
and working procedures. Reading the repository requires no AI harness.

Contributions can question a definition, supply a counterexample, examine a
source, or test a mapping. Begin with a concrete encoding or research question and the
relevant evidence or example. [CONTRIBUTING.md](CONTRIBUTING.md) explains
where the resulting work belongs and which checks apply.

### Work with an AI harness

Use the repository root as the harness's working directory. The agent should
read the repository instructions and consult the maintained knowledge before
working on a question.

| Harness | Repository entry point |
|---|---|
| Claude Code | [CLAUDE.md](CLAUDE.md), with research adapters under [.claude/skills/](.claude/skills/) |
| Codex | [AGENTS.md](AGENTS.md) |
| pi or another harness | Explicitly ask the agent to read [AGENTS.md](AGENTS.md) and follow its routes into [knowledge/INDEX.md](knowledge/INDEX.md). |

A starting task can be given directly in the conversation.

> Read AGENTS.md, knowledge/INDEX.md, and knowledge/state.md. Examine how
> the model distinguishes a corrected transcription from a different text.
> Trace the relevant definitions to their source premises and executable
> examples. Identify a counterexample or an unresolved editorial decision.
> Keep source findings and proposed model changes explicit.

For implementation work, name the intended change and the case it must handle.
The agent can inspect sources, revise arguments, implement a bounded model
change, and run the relevant checks. Research findings retain their source
links, while model decisions and experiment results are written back to their
designated repository documents. This allows another agent or a human reader
to continue from inspectable files.

Scientific review and editorial acceptance remain explicit contributions by
the responsible researchers. Generated prose and passing tests establish
neither by themselves.

### Run the examples and checks

Local execution needs Git, Python 3.11 or newer, and `uv`.

```sh
git clone https://github.com/chpollin/tei-p6-research.git
cd tei-p6-research
uv sync
uv run python tools/validate.py .
uv run python tools/check_abstract_text_v01.py --check
uv run python tools/check_entities_v02.py --check
```

These commands validate the repository's research structure and reproduce the
bounded model reports. The [experiment guide](knowledge/experiments.md)
connects each runner to its question, examples, and limitations.
[Operations](knowledge/operations.md#environment) documents setup alternatives,
and [Testing](knowledge/testing.md) defines the checks required after a change.

The admitted Guidelines XML can also be reconstructed from the source
representations in a clone.

```sh
uv run python -m tools.export_guidelines --output ../tei-p5-4.12.0-xml
uv run python -m tools.export_guidelines --output ../tei-p5-4.12.0-xml --check
```

This export preserves the admitted XML bytes and upstream paths. Images and
schemas are outside its scope. [Export and discovery](knowledge/operations.md#export-and-discovery)
describes the source boundary, export behavior, and navigation.

## Licence and provenance

Project-authored text and documentation use [CC BY 4.0](LICENSE), and
project-authored code uses [MIT](LICENSE-CODE).
[CITATION.cff](CITATION.cff) provides citation metadata. Third-party material
retains its own authorship and rights, recorded with its source provenance
under [sources/](sources/) and described in [Data](knowledge/data.md).

Research provenance uses [Grounded Vault](https://github.com/DigitalHumanitiesCraft/grounded-vault),
with [upstream attribution](knowledge/architecture.md#lineage).
