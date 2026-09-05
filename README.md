# TEI P6 Research

Developing and evaluating an abstract text model for a possible TEI P6,
grounded in P5, textual scholarship, and editorial practice.

> This is an independent, unofficial project. It is not a TEI Consortium
> repository. Official TEI P6 records are research sources. Proposals developed
> here are the project's own recommendations.

[Read the proposal](https://chpollin.github.io/tei-p6-research/)
· [Model](https://chpollin.github.io/tei-p6-research/model.html)
· [Materials](https://chpollin.github.io/tei-p6-research/corpus.html)
· [Knowledge](https://chpollin.github.io/tei-p6-research/knowledge.html)
· [Project overview](https://chpollin.github.io/tei-p6-research/project.html)
· [Current research state](knowledge/state.md)

## Research objective

The project asks which concepts, identities, relations, and rules a text model
needs for practical encoding and processing. P5's formal properties, history,
and use provide the baseline. Textual scholarship and editorial cases challenge
the proposed categories. The project compares repair within P5, compatible
evolution, architectural replacement, and deferral, including their migration,
tooling, teaching, interoperability, and governance costs.

The intended result combines a P5 model atlas, decision histories, grounded
requirements, evaluated alternatives, migration evidence, and executable
prototypes in a scholarly proposal.

## Read and inspect

The [Proposal for TEI P6](40_output/12-p6-design.md) presents the argument.
[Abstract Text Model 0.1](docs/p6/abstract-text-model-v0.1.md) defines its
bounded executable candidate and human acceptance questions. The
[editorial case study](docs/p6/editorial-case-study.md) examines source
preservation and mapping limits. These do not establish complete TEI coverage
or general migratability.

The public [materials inventory](https://chpollin.github.io/tei-p6-research/corpus.html)
reports acquisition from pinned control records. The
[knowledge browser](https://chpollin.github.io/tei-p6-research/knowledge.html)
follows admitted sources through assertions to output. Current holdings,
blockers, and checks are recorded in [`knowledge/state.md`](knowledge/state.md).

## Research method

Research claims follow the Grounded Vault chain.

```text
00_sources -> 10_markdown -> 20_distillates -> 30_assertions -> 40_output
```

Each output claim cites an assertion, each assertion cites distillate
statements, and each distillate addresses one source. Collections undergo
controlled admission before entering this chain. Grounding establishes
traceability. Only the designated human expert may assign `verified` status.

## Start here

| Goal | Start here |
|---|---|
| Read the proposal and explore the model | [Research home](https://chpollin.github.io/tei-p6-research/) |
| Browse the available material | [Materials workbench](https://chpollin.github.io/tei-p6-research/corpus.html) |
| Understand the research contract | [`knowledge/specification.md`](knowledge/specification.md) |
| Check what actually exists now | [`knowledge/state.md`](knowledge/state.md) |
| Navigate the research vault | [`HOME.md`](HOME.md) |
| Understand the repository | [`ARCHITECTURE.md`](ARCHITECTURE.md) |
| Set up or publish locally | [`SETUP.md`](SETUP.md) |
| Contribute research or code | [`CONTRIBUTING.md`](CONTRIBUTING.md) |
| Explore provisional P6 design work | [`docs/p6/README.md`](docs/p6/README.md) |

## Citation, rights, and attribution

Project-authored content is licensed under [CC BY 4.0](LICENSE). Third-party
material retains its original rights. Public access does not grant permission
to republish full text. Citation and method attribution are recorded
in [`CITATION.cff`](CITATION.cff) and [`NOTICE.md`](NOTICE.md).
