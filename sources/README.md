# TEI source control plane

This directory declares what the TEI corpus may acquire and how a run is pinned,
audited, and admitted to the Grounded Vault.

The complete source-family rationale and acquisition tiers are defined in
[`PRIMARY-SOURCES.md`](PRIMARY-SOURCES.md).

```text
registry.yaml                 source families and policy
locks/*.yaml                  immutable or to-be-resolved upstream boundaries
manifests/*.yaml              append-only run records
```

The registry is policy; a lock is the intended upstream identity; a manifest is
evidence of what a particular run actually observed. A lock with
`retrieval_status: not_started` is not proof that the source was fetched.

## Required manifest fields

Every future ingestion manifest must include at least:

```yaml
schema_version: 1
run_id: <stable-id>
source_id: <registry-id>
started_at: <UTC timestamp>
finished_at: <UTC timestamp or null>
status: planned | partial | observable-complete | bounded-complete | failed
scope:
  boundary: <observed-interface-or-sample>
  status_applies_to: <request-or-object-boundary>
adapter:
  name: <name>
  version: <version-or-code-sha>
requests: []
objects: []
counts: {}
gaps: []
rights_exceptions: []
```

`source_id` resolves the lock through the dated registry. A manifest may repeat
`lock_file` for convenience, but the registry mapping remains authoritative.
The manifest status applies only to its declared request and `scope`. Completing
a narrower interface or sample does not change the completion status of the
whole source family.

Counts belong only in manifests produced from observed data. Registry and lock
files do not contain guessed issue, release, meeting, file, or literature counts.

## Source admission

Acquisition is upstream of the canonical evidence chain. A source package enters
the Grounded Vault only after:

1. identity and checksum verification;
2. rights classification;
3. source-type assignment (`document`, `publication`, or `data`);
4. placement of the admitted original according to `00_sources/README.md`;
5. creation of the immutable `10_markdown` representation when applicable.

The corpus layer may automate these steps later, but it may not create a shortcut
from `corpus/` to `20_distillates`, `30_assertions`, or `40_output`.

## Rights and public repositories

Public accessibility does not by itself authorize republication. The registry
therefore separates:

- `rights_status`: whether storage and redistribution have been established;
- `content_authority`: the epistemic role of the source;
- `instruction_trust`: always `none` for acquired content.

Unknown or per-item rights permit metadata, hashes, local retrieval where lawful,
and source links; they do not permit automatically committing full source text.

Validate registry-to-lock identity, manifest source IDs, normalized object
existence, and recorded SHA-256 values with:

```powershell
python -m tools.corpus.validate_control_plane .
```
