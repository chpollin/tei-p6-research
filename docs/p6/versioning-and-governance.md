# Versioning and governance

Status: candidate policy model
Authority: independent project proposal, not TEI Consortium policy

A formal model remains interoperable only if its identifiers, changes,
bindings, and compatibility claims can be governed over time. This document
defines the policy questions that P6 candidates must answer; it does not assign
authority on behalf of the TEI Consortium.

## Governed objects

Governance applies independently to the metamodel, shared domain concepts,
blueprints, constraints, serialization bindings, migration rules, diagnostic
codes, examples, and conformance tests. A release identifies a coherent set of
compatible versions rather than assuming that all components always change
together.

Distinguish the persistent identifier of a governed object from the immutable
identifier of a particular definition. An instance's dependency context must
make the applicable definition recoverable. Governed definitions name their
owner, dependencies, change history, and replacement relations where applicable.

A wording change counts as editorial only when interpretation, validation, and
processing consequences remain unchanged. A semantic change requires an
explicit decision whether it revises the same concept or introduces a distinct
concept, with relations to earlier definitions and consequences for existing
data. A content hash identifies a definition's bytes, not the correctness of
that semantic decision.

## Change classes

| Change | Compatibility question |
|---|---|
| editorial | Does meaning, validation, or processing remain unchanged? |
| additive | Can existing conformant instances and processors ignore or adopt the addition safely? |
| restrictive | Which previously valid instances become invalid? |
| semantic | Does an existing identifier acquire a different meaning or processing expectation? |
| structural | Does containment, order, relation, or serialization mapping change? |
| removal | What replacement and migration path exists? |
| binding-only | Does the abstract model remain stable while a serialization representation changes? |

Versioning policy must define compatibility for documents, models,
customizations, validators, converters, and processors separately. One version
number cannot make all of those guarantees implicit.

## Compatibility declarations

A release should publish machine-readable compatibility statements describing
which earlier model and binding versions it accepts, which it can migrate,
which require a compatibility mode, and which are unsupported. Compatibility
may be syntactic, model-level, semantic, processing-level, or ecosystem-level;
the declaration names the kind.

Backward compatibility is a design variable rather than an automatic absolute.
An incompatible change may be justified, but its affected constructs, evidence,
migration, diagnostics, and adoption costs must be explicit.

## Deprecation lifecycle

Deprecation is a staged contract: proposal, decision, warning period,
replacement availability, migration support, and possible removal. The policy
must state which stage changes validation behavior and how long identifiers and
documentation remain resolvable.

A deprecated construct retains its historical meaning. Reusing the identifier
for a different concept would corrupt versioned interpretation and should be
prohibited.

## Decision record

A material change should connect:

```text
grounded problem or requirement
    -> alternatives and counterevidence
        -> prototype and migration results
            -> governance decision
                -> merged implementation
                    -> released package
```

These states are independently observable. Discussion does not imply decision;
decision does not imply implementation; implementation does not imply release.
A release manifest points to the evidence for each transition.

## Conformance-suite governance

Normative tests are governed artifacts. Each test names the model, blueprint,
binding, and requirement it exercises. Adding or changing a test may change
effective conformance even if prose is untouched, so test-suite versions and
their relation to releases must be explicit.

Disputed tests require a review path and may not be silently weakened to make an
implementation pass. Errata distinguish a mistaken test from a changed
requirement.

## Extension governance

Local and community extensions need collision-resistant identifiers and
declared ownership. A pathway may promote a widely used extension into a shared
domain model, but promotion requires semantic review, migration guidance, and a
mapping from the earlier identifier. Central adoption must not erase the origin
or silently redefine deployed data.

## Adoption and transition

A candidate release needs more than schemas: documentation, teaching examples,
reference validators, converters, compatibility guidance, implementation
reports, and a transition window. Governance should make it possible for P5 and
P6 ecosystems to coexist while projects evaluate migration.

The research project evaluates such policies comparatively. Its recommendation
remains a reasoned posit. If an official body adopts a policy, that separate
event may be reported through grounded process records; adoption neither makes
the research reasoning a source fact nor supplies human verification of it.
