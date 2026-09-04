# Exposé: TEI P6 Research Vault

The TEI Guidelines are not only an XML vocabulary. TEI P5 combines a conceptual
model, modular declarations, ODD customization, generated schemas, prose
guidance, processing infrastructure, governance decisions, and accumulated
community practice. These layers have evolved over many years and do not always
make the same distinctions visible. A serious proposal for TEI P6 must
therefore begin by reconstructing how P5 actually works, why it developed in
that way, where its complexity creates demonstrated problems, and which of its
capabilities remain essential.

The TEI P6 Research Vault is an independent, provenance-complete research
environment for that task. Its guiding question is: **Which architecture for a
next TEI generation is best supported by the formal properties, development
history, and real-world use of P5?** The project does not assume that a complete
rewrite is necessary. Repair within P5, compatibility-preserving evolution,
architectural redesign, and deliberate non-change are evaluated as competing
options under the same criteria.

The evidence base combines the pinned P5 Guidelines and ODD sources, generated
schemas, release history, Git commits, GitHub issues and pull requests, Council
and Board records, official P6 process documents, relevant scholarship, and a
documented sample of real customizations and toolchains. Each source family has
an explicit authority, version boundary, rights status, and completeness
definition. Issue closure is not treated as acceptance, governance discussion
is not treated as implementation, and merged code is not treated as a released
normative effect without separate evidence for each transition.

Research knowledge is produced through the Grounded Vault chain:

```text
00_sources -> 10_markdown -> 20_distillates -> 30_assertions -> 40_output
```

This makes every important statement traceable to an exact source location or
reproducible computation. Large source collections are acquired and normalized
outside the evidence chain before controlled admission. Deterministic
validation checks structure and provenance, adversarial machine review tests
whether cited passages support their statements, and human expert review alone
may establish verification.

The P6 design programme investigates a serialization-independent semantic core
with reusable blueprints, project customizations, explicit constraints, and
normative bindings for XML, JSON-LD, RDF, YAML, and other justified formats.
Every binding must declare what it preserves, normalizes, loses, projects, or
cannot represent. Formal schemas and validators are combined with semantic
roundtrip tests through a canonical intermediate representation.

Concrete P5/P6 comparisons are part of the method rather than decorative
examples. Candidate designs are tested on mixed content, overlap, stand-off
annotation, context-sensitive structures, linking, bibliography, the critical
apparatus, manuscript description, linguistic annotation, and facsimile
alignment. Each case combines a P5 baseline, candidate P6 representation,
supported serializations, valid and invalid fixtures, migration behavior, and
an explicit loss report.

The expected result is not merely a new schema. It is a reviewable design
dossier: a formal atlas of P5, a history of decisions and demonstrated
frictions, a comparative evaluation of P6 options, an executable conformance
and migration framework, and a design specification whose recommendations are
linked to evidence, counterevidence, tests, trade-offs, and open questions. The
repository is thus both a research archive and an engineering environment for
reasoning about the future of text encoding without confusing an attractive
proposal with an established fact.
