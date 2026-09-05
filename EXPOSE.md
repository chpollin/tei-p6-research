# Exposé: TEI P6 Research

TEI P6 Research is an independent project developing and evaluating an abstract
text model for a possible next TEI generation. It asks which concepts,
identities, relations, and rules support practical encoding and interpretation.
The investigation covers P5 declarations, ODD customization, Guidelines prose,
processing, and documented use. It examines both demonstrated problems and
capabilities that a redesign must preserve. Textual scholarship and alternative
models challenge the proposed categories. Repair within P5, compatible
evolution, architectural replacement, and deferral face the same evaluation
criteria.

The planned evidence base combines pinned P5 Guidelines and ODD sources, generated
schemas, release history, Git commits, GitHub issues and pull requests, Council
and Board records, official P6 process documents, relevant scholarship, and a
documented sample of real customizations and toolchains. Each source family has
an explicit authority, version boundary, rights status, and completeness
definition. Issue closure is not treated as acceptance, governance discussion
is not treated as implementation, and merged code is not treated as a released
normative effect without separate evidence for each transition.

Research knowledge follows the Grounded Vault chain.

```text
00_sources -> 10_markdown -> 20_distillates -> 30_assertions -> 40_output
```

Factual claims trace to source locations through assertions and distillates.
Experimental results also require admission before they can ground assertions.
Model interpretations and recommendations remain explicit posits. Deterministic
validation checks structure and provenance, machine review tests source
support, and human expert review establishes verification.

One hypothesis is a serialization-independent semantic core with reusable
profiles and explicit constraints. XML and additional bindings will be selected
for concrete exchange tasks. A canonical comparison representation is an
experimental option whose adequacy must be tested alongside alternatives.
Preservation criteria are specified before converters are evaluated. A
successful roundtrip alone cannot establish that a migration retained the
editorial distinctions required by its task.

Cases are selected across P5 modules and textual practices, with document
type, medium, and phenomenon recorded separately. Each combines a P5 baseline,
candidate P6 representation,
supported serializations, valid and invalid fixtures, migration behavior, and
an explicit loss report. Cases require an explicit selection and rights
protocol. Synthetic examples isolate assumptions. Real editorial cases test
their practical adequacy without claiming statistical representativeness.

The intended publication joins a formal P5 atlas, decision history, grounded
requirements, comparative evaluation, and executable migration studies.
Recommendations must explain their evidence, costs, remaining gaps, and the
conditions that would reverse them. The
[research state](knowledge/state.md) distinguishes completed work from these
research obligations.
