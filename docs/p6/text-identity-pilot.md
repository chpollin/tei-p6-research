# Text identity and annotation pilot

Authority: independent modeling experiment, not an official TEI P6 specification.
Contract version: 1. Working language: English.

## Question and bounded scope

What must distinguish a text, a text version, a region, and an annotation so
that annotations remain auditable when text changes? This pilot compares two
region selectors on finite Unicode strings. It does not define text in general,
infer authorial intention, implement collaborative editing, or demonstrate
real-world P5 migration. All example instances are explicitly synthetic.

The evidence branch reports only what selected specification files in TEI P5
4.12.0 say. The experiment branch proposes independent semantics. Similar names
do not establish equivalence between P5 constructs and pilot objects.

The admitted P5 statements motivate questions about identifying a target,
addressing it, and associating an interpretation with it. They do not establish
that P5 is defective or that immutable string versions are necessary. The
pilot chooses editing as a test situation and proposes version identity as one
answer. P5 `anchor` identifies a point; empty regions are excluded here, so the
experiment does not yet provide a counterpart for that distinction.

## Candidate definitions

- **Text:** an identified editorial grouping of versions. The criterion for
  treating those versions as one text is an assumption outside this prototype;
  it is not inferred from equal character content.
- **Text version:** an identified immutable Unicode string associated with one
  text, carrying a SHA-256 of its UTF-8 bytes and optionally one parent version
  of that same text. A parent relation must be acyclic.
- **Region:** an identified target specification containing a version reference
  and a selector. The selector describes a target; resolution returns an
  interval in that version. Distinct region records may resolve to the same
  interval without becoming the same record.
- **Annotation:** an identified record carrying an interpretation body and a
  reference to one region. Different annotations may overlap or disagree; the
  prototype checks their structure, not the consistency of their interpretations.

These are definitions under test, not findings about the nature of text. The
pilot's positions count Unicode code points, not bytes, UTF-16 units, or grapheme
clusters. Strings are not normalized implicitly. End positions are exclusive.
Empty regions and discontinuous regions are outside this first experiment.
IDs are unique within an experiment instance. The text/version relationship is
an explicit editorial assignment, not a conclusion the validator can infer.
One text per version, at most one parent, and one region per annotation are
experimental limits, not claims about all textual traditions or editing tasks.

Immutability is a contract on versions and on the nonmutating operations in this
prototype. Hash checks detect disagreement between a supplied string and its
declared hash. They cannot detect a historical rewrite if somebody replaces
both string and hash; that requires a trusted persistent version history, which
this pilot does not implement.

## Two selector alternatives within one object model

Both alternatives retain the four candidate object definitions. They compare
target resolution, not competing ontologies of text or complete architectures.

**A — Version-bound position:** the selector supplies `start` and `end`, plus
an exact quote used as an integrity check against that range.

**B — Version-bound quotation:** the selector supplies a nonempty exact quote,
optionally qualified by immediately adjacent prefix and suffix. Resolution
must yield exactly one matching range; zero and multiple matches are explicit
failures. Context is literal and case-sensitive.

Both alternatives require version identity. B is not presumed superior:
repeated quotations can be ambiguous, and edits can destroy its context. A is
simple and deterministic on a fixed version but cannot reuse positions safely
on an edited version. A separate reanchoring operation searches an explicitly
chosen destination version and returns candidates or absence/ambiguity. It
does not mutate the original annotation or claim that a surviving quotation
retains the same interpretation.
An `absent` result means no match for the retained selector, including its
context requirements; it does not necessarily mean the quotation was deleted.

## Formal experiment contract

Inputs are `experiments/text_identity/spec.json` and `cases.json`. The runner
is `python -m tools.pilots.text_identity`; `--check` compares its deterministic
report with the checked-in `report.json` and fails on drift. The ordinary run
regenerates that report. The runner must fail if any case differs from its
declared expected diagnostics or resolution. All report inputs, including the
implementation and contract, are identified by SHA-256; wall-clock times and
machine-specific absolute paths are excluded from generated output.

Required constraints include unique IDs, resolvable references, text/version
ownership, hash fidelity, acyclic version ancestry, selector type and bounds,
exact-quote fidelity, and explicit quotation ambiguity. Malformed objects must
produce diagnostics rather than uncaught exceptions. Diagnostic codes and case
IDs provide stable links between the contract, fixtures, and tests.

Required cases include valid fixed-version annotation; insertion before a
region; edit within a region; deletion; repeated quotation; disambiguation by
context; overlapping annotations; Unicode positions and normalization
differences; invalid bounds; broken references; duplicate identity; changed
version content; a version-parent cycle; and an unchanged quotation at unchanged
positions in a changed interpretative context. Counterexamples must test the
assumptions of both alternatives, not merely the implementation's happy path.

## Acceptance procedure

Start with the [pilot chapter](../../40_output/02-abstract-model.md), then the
four definitions above and the cases below. The machine-readable
[report](../../experiments/text_identity/report.json) gives actual results by
case ID; [cases.json](../../experiments/text_identity/cases.json) supplies the
hand-authored expected outcomes independently of report generation.

| Case to inspect | Input or change | Expected behavior to assess |
|---|---|---|
| `reanchor-insertion` | `The red fox.` becomes `Now: The red fox.` | The old `red` target remains `[4,7)` in v1; `[9,12)` in v2 is proposed with `accepted: false`. |
| `reanchor-repeated` | The new version contains `red red` | Both `[0,3)` and `[4,7)` are candidates; neither is chosen. |
| `reanchor-deletion` | `red` disappears in `The fox.` | No new target is proposed; the old annotation remains auditable. |
| `normalization-quotation` | A composed quote is searched in decomposed Unicode text | Literal matching fails explicitly; no hidden normalization occurs. |
| `reanchor-context-loss` | The quote survives but its required adjacent context changes | `absent` reports failure of the retained selector, not deletion of the quote. |
| `surviving-quote-changed-interpretation-position` and `surviving-quote-changed-interpretation-quotation` | `The red fox.` becomes `The red car.`; an old annotation interprets `red` as fur color | Both selectors resolve `red` at `[4,7)`; reanchoring proposes that interval with `accepted: false`. Matching cannot establish that the old interpretation fits. |

These are normative expectations of the experiment, not observations of real
editorial practice. A reviewer can reject an expectation even when the code
implements it correctly.

Read the paired cases as a comparison of explicit commitments: position
selection checks a supplied interval; quotation selection must distinguish
matches. Neither operation evaluates the annotation's interpretation. The
fur-color example stipulates an editorial reason to reject reuse; that reason
is not a semantic judgment performed by the runner. These cases test a boundary
of both selectors and do not establish a general winner.

Run the technical gate from the repository root:

```powershell
py -3 tools/check_text_identity_pilot.py
```

On systems with Python on PATH, use `python` instead of `py -3`. This command
validates the full vault and pilot chapter, rechecks source admission integrity,
checks current review-pair coverage and hashes, checks the source control plane,
reproduces the model report, and runs the complete test suite. It does not
modify research statuses or approve the model. The normal CI check runs it too.

| Machine check | What it establishes | What it does not establish |
|---|---|---|
| Source bytes, commit, license records and representation regeneration | The admitted passages reproduce the declared source snapshot | Whether the source is correct or the sample is representative |
| Layer, anchor, status and chapter checks | The claimed provenance chain is structurally well formed | Whether every natural-language conclusion follows |
| Independent support review, prompt hashes and dependency coverage | Recorded judgments refer to the current source/claim pairs | Human expert verification or philosophical agreement |
| Type, reference, ownership, hash, bounds and cycle constraints | An instance satisfies the pilot's executable rules | A proof of a universally adequate ontology |
| Adversarial fixtures, type-strict expected results and report regeneration | Implementation behavior matches the declared finite examples | Real-world usability, complete P5 migration or all possible cases |

Technical acceptance requires the full vault validator, chapter-scoped
validator, source-control validator, independent support-pair review, pilot
checks, full test suite, reproducible generated pages, and `git diff --check`.
A green report establishes agreement with these finite contracts; it is not
a proof of universal expressivity, philosophical correctness, or usability.

The human reviewer then records **accept**, **revise**, or **defer** for each:

1. Are the four candidate definitions intelligible, and are their identity
   assumptions acceptable for this bounded experiment?
2. Do the admitted passages support the chapter's P5 statements without
   silently extending their authority to the pilot's semantics?
3. Are the examples and expected outcomes sensible? Inspect insertion, repeated
   quotation, normalization, deletion, context loss, and the surviving quotation
   with changed interpretation, including failures.
4. Are both alternatives represented fairly, and is the reanchoring proposal
   clearly distinct from an accepted interpretation?
5. Is the evidence sufficient to justify a next experiment? Name a real editorial
   task, the expected outcome, and an observation that would require revising
   one of the candidate definitions.

Acceptance means this pilot is an adequate basis for further research. It does
not approve a final P6 model or confer `verified` on research artifacts. The
reviewer should return a decision and reasons for each of the five items. Full
acceptance requires all five to be accepted; mixed decisions remain a partial
review with named revisions or missing evidence in `knowledge/state.md`.
Accepting the experiment does not choose selector A or B.

## Evidence and audit entry points

- [Pilot chapter](../../40_output/02-abstract-model.md) separates grounded P5 statements and model posits.
- [Source admission manifest](../../sources/manifests/2026-09-05-text-identity-pilot-admission.yaml) records exact source, rights, hashes and scope.
- [Support-review audit](../../experiments/text_identity/review/README.md) describes review inputs, verdicts and limitations.
- [Experiment specification](../../experiments/text_identity/spec.json) defines object fields and diagnostic codes.
- [Generated report](../../experiments/text_identity/report.json) exposes actual case outcomes and input hashes.

Current completion and human-review state belong only in `knowledge/state.md`.
