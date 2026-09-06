# TEI source control plane

This directory declares what the TEI corpus may acquire and how a run is
pinned, audited and admitted to the Grounded Vault.

```text
registry.yaml                 source families and policy
locks/*.yaml                  immutable or to-be-resolved upstream boundaries
manifests/*.yaml              append-only run records
```

The registry is policy, a lock is the intended upstream identity, and a
manifest is evidence of what a particular run actually observed. A lock with
`retrieval_status: not_started` proves nothing about whether the source was fetched.

The source families, the identity syntax, the rights rule and the completion
vocabulary are defined in `knowledge/data.md`. The required manifest fields,
the collectors and the admission procedure are in `knowledge/operations.md`.
Validate registry-to-lock identity, manifest source IDs, normalized object
existence and recorded SHA-256 values with
`python -m tools.corpus.validate_control_plane .`.
