# Ingestion manifests

This directory is append-only. Future acquisition runs write one manifest per
source family and run. A later run never edits the observations of an earlier
run; corrections are new manifests related with `corrects`.

File names use UTC and the source ID:

```text
2026-09-04T020000Z--github-teic-tei-work-items.yaml
```

An ingestion manifest records observed facts, including derived counts. A source
registry or lock records intent and therefore keeps `counts: {}` until a run has
actually enumerated the source.

Required object-level provenance:

- stable upstream ID;
- canonical URL;
- observed and upstream timestamps;
- request/API version and pagination position;
- HTTP status and safe response headers;
- raw SHA-256, byte length, and media type;
- normalized SHA-256 and transformation version;
- rights and trust classifications;
- gap/error state when retrieval or parsing failed.

Never record access tokens, cookies, authorization headers, signed download URLs,
or personal local paths.
