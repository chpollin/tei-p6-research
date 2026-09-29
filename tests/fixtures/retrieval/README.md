# Retrieval and selection fixtures

Fictional vault and corpus snapshot for `tests/test_retrieval.py` and
`tests/test_select_sources.py`. Nothing here is a source, carries evidential
weight or describes a real TEI record; identifiers, dates and hashes are
invented, and stream file names only mirror the paths the tools expect.

- A fictional release `9.9.0` admits a class specification in one manifest and
  reuses that admission in a later one, so the predecessor chain is testable.
  A test document of the same release carries an admission authority that
  denies normative force, and a representation with a normative-looking file
  name has no admission at all.
- `knowledge/` holds one project contract and one project proposal.
- The assertions include a validated assertion with and without its
  machine-review date and a reciprocal contested pair.
- `00_sources/`, `corpus/raw/` and the unanchored complete XML hold sentinel
  words that a serialized index must never contain.
- `corpus/normalized/` holds tiny GitHub, relation, SourceForge and TEI-L
  streams. Issue 1505 appears both as an `issue` and as a `work-item-detail`
  record, and a SourceForge ticket shares its title with a GitHub issue without
  any recorded relation. `corpus/projections/` holds a small declaration atlas
  and a one-row Guidelines navigation projection.
