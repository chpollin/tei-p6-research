# Operational completeness

The corpus never uses *complete* to mean “everything that ever existed.” It
means that a declared, testable boundary was exhausted at a stated observation
time.

The strongest permitted corpus-wide statement is:

> Complete for the objects publicly observable through the registered sources
> and interfaces at the snapshot time, subject to the recorded exclusions and
> failures.

Deleted, private, embargoed, access-controlled, or historically overwritten
content cannot be presumed recoverable. An unavailable object remains a gap in
the manifest; it is not silently omitted.

## Completion states

Every ingestion run and source family uses one of these states:

- `planned`: scope declared, no retrieval attempted;
- `partial`: retrieval began but at least one declared boundary or check is
  unfinished;
- `observable-complete`: every currently observable object inside the boundary
  was enumerated, retrieved or explicitly marked unavailable, and reconciled;
- `bounded-complete`: a finite search or bibliography protocol was exhausted;
- `not-completable`: the source does not expose a finite or auditable boundary.

No planned count is a coverage result. Counts are written only by an ingestion
run and must cite its manifest.

## Family-specific definitions

### TEI P5 4.12.0 normative baseline

`observable-complete` requires all of the following:

1. the published revision `113e933e2` has been resolved to one full Git object
   ID and verified against the declared release/tag;
2. every tracked file at that commit has an inventory entry and content hash;
3. the Guidelines source, component specifications, release notes, generated
   schemas, and published documentation artifacts declared by the lock are
   represented or explicitly marked unavailable;
4. release, Vault, and repository manifestations are related without treating
   byte-different formats as duplicates;
5. every admitted object carries source, version, trust, and rights metadata.

### GitHub issues and pull requests

For repository `TEIC/TEI` at time `T`, `observable-complete` means:

1. the issue endpoint was paginated to exhaustion with state `all`;
2. issue-shaped pull requests were identified and not double-counted;
3. every observable issue has its detail record, comments, and timeline events;
4. every observable pull request has its detail record, issue comments, reviews,
   review comments, commits, and declared relation metadata;
5. labels, milestones, releases, redirects/transfers, pagination, and API errors
   were recorded;
6. a second enumeration reconciled identifiers and API-reported child counts;
7. missing, minimized, deleted, or inaccessible objects are gaps, not absences.

The API exposes current representations, not necessarily every historical edit.
Periodic snapshots create a local observation history from the first successful
run onward.

### Council minutes

For a declared date interval, `observable-complete` requires:

1. every meeting link reachable from the official Council meeting index was
   enumerated;
2. the official page and, where present, its source in `TEIC/Documentation` were
   modeled as separate manifestations of the same meeting;
3. attachments and referenced working papers were inventoried;
4. unreachable or rights-restricted items were retained as explicit gaps;
5. the discovered meeting-date set was reconciled against the index at the end
   of the run.

### P5 releases

At time `T`, `observable-complete` requires every P5 release listed by the
official release index to have a version record, publication date when supplied,
release/tag/revision identifiers when supplied, release notes, artifact
inventory, hashes for retrieved artifacts, and explicit missing-artifact status.

The alias `current` is never used as an immutable identifier.

### Literature

“All TEI literature” has no finite boundary and is `not-completable`. A
literature snapshot may be `bounded-complete` only when it names:

- its seed bibliographies, journals, indexes, and exact queries;
- language, date, document-type, and relevance boundaries;
- the observation date and pagination/result limits;
- a disposition for every discovered record: included, duplicate, excluded with
  reason, unavailable, or pending review.

The first bounded seeds are the bibliography of the locked Guidelines release
and the Journal of the Text Encoding Initiative. Neither seed is treated as the
whole field.

## Reconciliation invariants

- Stable upstream IDs, not titles or URLs, define identity.
- Raw bytes are addressed by SHA-256.
- A changed source body creates a new observed version; it does not overwrite
  history.
- Exact hashes may deduplicate byte-identical manifestations. Fuzzy similarity
  may propose a relation but may never merge records automatically.
- SourceForge-to-GitHub migrations, web-to-repository minutes, and XML/HTML/PDF
  renditions remain distinct records connected by typed relations.
- Every projection can be traced to normalized record hashes, raw hashes, the
  transformation version, and the lock used for the run.
