# TEI corpus workspace

`corpus/` is the acquisition workspace of the vault. It prepares repeatable
source packages for admission to the evidence chain and never bypasses it.

```text
raw -> normalized -> projections
```

- `raw/` materializes byte-preserving responses, archives or Git objects. It
  is local, ignored and never hand-edited.
- `normalized/` holds loss-minimizing machine records derived from raw
  objects, with source identifiers, order, timestamps, relationships and a
  pointer to the raw hash.
- `projections/` holds deterministic reading and retrieval views.

Nothing in `corpus/` may be cited by a distillate, assertion or chapter. Each
transformation is recorded by an append-only manifest under
`sources/manifests/`. The source families, the version semantics, the trust
boundary and the completion vocabulary are defined in `knowledge/data.md`, the
collectors in `knowledge/operations.md`.
