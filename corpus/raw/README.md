# Raw materializations

This directory is intentionally ignored except for its documentation. A fetcher
may materialize HTTP response bodies, response headers, archives, Git bundles,
or API pages here without changing the committed vault.

Rules:

- preserve response bytes before parsing;
- record SHA-256, byte length, media type, canonical URL, retrieval time, status,
  redirect chain, request parameters, pagination cursor, and response headers in
  the run manifest;
- never store credentials, authorization headers, cookies, or signed URLs;
- never edit a raw object in place;
- use a content-addressed path such as `sha256/ab/<remaining-digest>`;
- do not commit or redistribute a raw object until its rights status explicitly
  permits that action.

The original admitted to `00_sources/` is governed by the existing vault method.
This cache is not a substitute for that original and cannot be grounded into
directly.
