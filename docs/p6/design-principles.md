# P6 design principles

Status: candidate evaluation principles
Authority: independent project hypothesis, not an official TEI position

These principles define the qualities against which candidate P6 architectures
will be tested. They do not prescribe a final syntax or prove that a major
redesign is preferable to compatible P5 evolution.

## Evidence before architecture

A change must identify the P5 behavior it preserves, repairs, replaces, or
removes. Reported pain, successful practice, historical rationale,
counterexamples, and migration consequences must be examined before a design is
preferred. Complexity or age alone is not evidence of a defect.

## Model before serialization

Concepts, identity, containment, order, text, relations, and constraints should
be defined independently of XML, JSON, RDF, or another concrete syntax. Each
serialization is a binding with an explicit mapping contract. The abstract
model must not merely rename the data structures of one preferred syntax.

## Preserve ordered textual structure

Text encoding requires order, mixed textual and structural content, addressable
regions, and relationships across regions. These are first-class semantic
requirements rather than artifacts to reconstruct from one serialization.

## Support trees and graphs explicitly

Document containment is valuable but not sufficient for overlap, stand-off
annotation, correspondence, alignment, and other non-hierarchical relations. A
candidate should represent both ordered hierarchies and graph relations without
forcing one to masquerade as the other.

## Make context and constraints visible

Whether a construct is permitted or meaningful may depend on its containing
structure, blueprint, or declared processing contract. Context-sensitive rules
should be explicit, inspectable, and testable rather than hidden in prose or
processor convention.

## Keep customization compositional

Projects must be able to select, restrict, combine, and extend reusable model
parts. Composition should have deterministic conflict rules, predictable
inheritance, and diagnostics that explain which blueprint or customization
introduced a constraint.

## Distinguish identity from labels and locations

Objects, concepts, versions, and source regions need stable identifiers that do
not depend on a filename, namespace prefix, display label, or current URL.
Serializations may use different local identifiers while preserving the same
declared identity.

## Define interoperability as a contract

Interoperability is not established by producing multiple file formats. A
binding must specify which concepts and invariants it preserves, how ordering
and identity are represented, what information it normalizes or loses, and how
equivalence is tested.

## Prefer progressive complexity

Evaluate complexity with named authoring and processing tasks. For an
introductory task, record the concepts the author must understand, declarations
they must supply, steps needed to diagnose an error, and dependencies a
receiving tool must obtain. Generated or inherited declarations reduce effort
only when their effective values remain inspectable and reproducible.

Add an advanced feature to the same example, such as a second annotation of a
paragraph, and record what changes in the document, explanation, and processor.
Reduced markup is useful only when it preserves necessary distinctions and
does not move unexplained complexity into tools or implicit conventions.

## Treat migration as part of the design

Every architectural decision is evaluated against existing P5 documents,
customizations, schemas, processors, teaching material, and institutional
workflows. Ambiguous, lossy, and unsupported migrations must be reported, not
hidden behind a nominal converter.

## Make conformance executable

Normative requirements should have machine-checkable identifiers, defined
scope, expected diagnostics, and positive and negative fixtures wherever
possible. Prose remains necessary for meaning and rationale, but hidden
processor behavior is not a conformance mechanism.

## Design for evolution and governance

The model needs explicit rules for versioning, extension, deprecation,
compatibility, and ownership of identifiers. Technical modularity must be
matched by a governance process capable of reviewing and maintaining modules,
bindings, blueprints, and test suites over time.

## Evaluation rule

No principle wins automatically. A candidate that improves conceptual clarity
may harm migration; a highly generic model may become difficult to teach; a
lossless binding may be costly to process. Every recommendation must state its
benefits, regressions, affected stakeholders, uncertainty, and rejected
alternatives under the shared evaluation framework.
