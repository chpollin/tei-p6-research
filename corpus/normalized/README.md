# Normalized corpus records

Normalized records are loss-minimizing, machine-readable derivatives of raw
objects. They make heterogeneous sources queryable without pretending that a
normalized record is the original.

Each record must retain:

- a stable `record_id` and the upstream identifier;
- `source_id` and lock identifier;
- `observed_at`, upstream creation/update times, and source URL;
- raw object SHA-256 and transformation version;
- all source text without summarization when rights allow local storage;
- source order, parent/child relations, labels, event types, and actor identity
  exactly as exposed;
- content authority, instruction trust, and rights status;
- deletion, minimization, redaction, parse error, and unavailable states.

Preferred serializations are UTF-8 JSONL for event streams and JSON for bounded
objects. Records are sorted deterministically by stable identifier. Derived
summaries and embeddings do not belong in this layer.

No normalized dataset has been generated yet.
