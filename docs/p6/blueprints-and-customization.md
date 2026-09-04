# Blueprints and customization

Status: candidate design contract
Authority: independent project proposal

Customization is central to TEI rather than an optional post-processing step.
A P6 architecture must allow communities and projects to create narrower,
clearer contracts while retaining an intelligible relationship to shared
concepts and to one another.

## Candidate layers

```text
metamodel
    -> shared domain model
        -> blueprint
            -> project customization
                -> instance declaration
```

The metamodel defines the available modeling mechanisms. A shared domain model
defines concepts and their intended semantics. A blueprint selects and
organizes a coherent contract for a domain or document family. A project
customization restricts or extends a declared blueprint. An instance names the
exact model, blueprint, customization, and binding versions against which it
claims conformance.

## Blueprint responsibilities

A blueprint may select concepts, properties, relations, hierarchies, content
patterns, and constraints. It may define required entry points, default
processing expectations, permitted extension points, and supported binding
profiles. It should be usable without importing unrelated domain complexity.

A blueprint is not merely a list of elements. It is a versioned behavioral
contract that states what its instances mean, which invariants apply, and what
other systems may rely on.

## Customization operations

The candidate algebra distinguishes explicit operations:

| Operation | Effect |
|---|---|
| select | include a shared concept or rule without changing it |
| restrict | narrow cardinality, values, content, or permitted relations |
| extend | add a locally identified concept, property, relation, or constraint |
| specialize | derive a more specific concept while preserving its declared parent relation |
| bind | associate a concept with a controlled vocabulary, datatype, or external authority |
| alias | provide a local label without changing canonical identity |
| deprecate | discourage a construct under an explicit replacement and version policy |
| compose | combine compatible blueprints or customization modules under conflict rules |

Whether a particular operation is allowed depends on the invariant being
modified. Core invariants may be non-overridable; blueprint rules may declare
controlled variation points; local additions must use stable identities and
must not impersonate shared concepts.

## Composition and conflict

Composition must be deterministic. The result records its inputs, order or
precedence where relevant, resolved conflicts, unresolved conflicts, and the
origin of every effective rule. Two incompatible cardinalities or content
requirements cannot silently collapse into whichever one a processor happens
to load last.

A composed model is valid only if all mandatory core invariants hold and every
conflict has a defined resolution. Diagnostics should identify the contributing
blueprints and exact rules, not only the invalid instance location.

## Context-sensitive rules

The same concept may have different permitted structures in different declared
contexts. Such variation should be modeled as a scoped constraint with a stable
identity. Scope may refer to a named hierarchy, containing concept, relation,
blueprint, or processing mode.

Context sensitivity must not alter the core meaning of a concept invisibly. If
the semantics differ, the model should consider distinct concepts or an
explicit specialization rather than relying only on position.

## Interoperability contract

Every customization publishes a machine-readable declaration of its base,
version dependencies, selected concepts, restrictions, extensions, aliases,
binding profiles, and conformance class. This declaration enables two projects
to compute their shared subset and identify incompatible or unknown extensions.

Interoperability may occur at several levels: common core, common blueprint,
exact customization, or explicit projection. Exchange claims must name the
level instead of using “TEI conformant” as an undifferentiated label.

## Validation and generation

A valid customization must pass metamodel validation, dependency resolution,
composition checks, invariant checks, and binding-generation checks. Generated
schemas and documentation are derived artifacts and retain links to the model
objects and constraints from which they were produced.

An instance validator should report the model stack it used and the origin of
each failing rule. Reproducibility requires immutable version identifiers or
content hashes for every dependency.

## Open design choices

The project has not decided whether blueprints should use inheritance,
declarative set operations, transformations, package composition, or a hybrid.
Nor has it decided how closely their behavior should correspond to existing ODD
customizations. These choices require extraction of real P5 customization
patterns, conflict examples, generated-schema comparison, and migration tests.
