# TEI P6 Research

An independent research vault that studies TEI P5 and the official TEI P6
process to develop evidence-grounded options for a possible next-generation
architecture.

> This is an independent, unofficial project without standing in the TEI
> Consortium. Official TEI P6 records are research sources here, and the
> proposals developed here are the project's own recommendations.

[Read the proposal](https://chpollin.github.io/tei-p6-research/)
· [Model](https://chpollin.github.io/tei-p6-research/model.html)
· [Materials](https://chpollin.github.io/tei-p6-research/corpus.html)
· [Knowledge](https://chpollin.github.io/tei-p6-research/knowledge.html)
· [About](https://chpollin.github.io/tei-p6-research/project.html)
· [Current research state](knowledge/state.md)

## Objective

The project asks which concepts, identities, relations and rules a text model
needs for practical encoding and processing. P5's formal properties, history
and use provide the baseline, and textual scholarship and editorial cases
challenge the proposed categories. Repair within P5, compatible evolution,
architectural replacement and deferral are compared under the same
dimensions, including their migration, tooling, teaching, interoperability
and governance costs. The charter with the research questions is
[`knowledge/project.md`](knowledge/project.md).

## Method

Research claims follow the Grounded Vault chain.

```text
00_sources -> 10_markdown -> 20_distillates -> 30_assertions -> 40_output
```

Each output claim cites an assertion, each assertion cites distillate
statements, and each distillate addresses one source. Collections undergo
controlled admission before entering this chain. Grounding establishes
traceability, machine review tests source support, and only the designated
human expert assigns `verified`. The rationale is in
[`knowledge/schema.md`](knowledge/schema.md).

## Where to start

The [English Guidelines coverage](corpus/projections/guidelines-4.12.0.md)
maps the complete pinned source intake to the published contents and the
actual distillates. Imported sources are available for citation; systematic
interpretation and human verification have their own recorded scope.

| Goal | Start here |
|---|---|
| Read the proposal and explore the model | [Research home](https://chpollin.github.io/tei-p6-research/) |
| Browse the acquired material | [Materials](https://chpollin.github.io/tei-p6-research/corpus.html) |
| Find any document, term or folder | [`knowledge/INDEX.md`](knowledge/INDEX.md) |
| Understand the charter and scope | [`knowledge/project.md`](knowledge/project.md) |
| Check what actually exists now | [`knowledge/state.md`](knowledge/state.md) |
| Understand the repository structure | [`knowledge/architecture.md`](knowledge/architecture.md) |
| Read the model definition | [`knowledge/text-model.md`](knowledge/text-model.md) |
| Read the proposal source | [`40_output/12-p6-design.md`](40_output/12-p6-design.md) |
| Set up a local environment and run the checks | [Quick start](#quick-start) and [`knowledge/operations.md`](knowledge/operations.md) |
| Acquire a source, regenerate the site or publish | [`knowledge/operations.md`](knowledge/operations.md), [`knowledge/design.md`](knowledge/design.md) and [`knowledge/testing.md`](knowledge/testing.md) |
| Contribute research or code | [`CONTRIBUTING.md`](CONTRIBUTING.md) |
| Enter the research topics in Obsidian | [`knowledge/INDEX.md`](knowledge/INDEX.md#topic-maps) |

## Quick start

```powershell
uv sync
python tools/validate.py .
python -m pytest tests
```

`uv sync` installs the dependencies. Without `uv` use
`python -m pip install pyyaml pytest ruff`. The environment, the collectors
and the research procedures are in
[`knowledge/operations.md`](knowledge/operations.md), the regeneration of the
public site in [`knowledge/design.md`](knowledge/design.md), and the one
completion gate that closes a change in
[`knowledge/testing.md`](knowledge/testing.md).

## Licence and attribution

Project-authored text, documentation and content are licensed under
[CC BY 4.0](LICENSE). Project-authored code under `tools/`, `tests/`,
`.github/` and the site assets is licensed under [MIT](LICENSE-CODE).
Citation metadata is in [`CITATION.cff`](CITATION.cff) and
[`codemeta.json`](codemeta.json).

The vault architecture was instantiated from
[DigitalHumanitiesCraft/grounded-vault](https://github.com/DigitalHumanitiesCraft/grounded-vault)
at commit `e19231735832f486735f94250d2771441372667e`, licensed under
CC BY 4.0. The original architecture, validation tools, tests, documentation
and Claude-oriented skills remain attributable to Christopher Pollin /
Digital Humanities Craft OG.

TEI Guidelines, schemas, source files, repository discussions, scholarly
publications and other third-party materials retain their own authorship and
applicable rights. Public access grants no permission to republish full text,
and inclusion in a source registry implies no permission to redistribute full
content. Per-source rights and provenance are recorded under `sources/` and
governed by [`knowledge/data.md`](knowledge/data.md).
