---
title: Handoff
project:
  name: "TEI P6 Research"
  repository: "tei-p6-research"
method:
  name: Promptotyping
  url: https://dhcraft.org/Promptotyping/
status: draft
language: en
created: "2026-09-06"
updated: "2026-09-06"
related: [INDEX, state, plan]
---

# Handoff

## Wayback fetch of the Brown TEI-L archive in progress

- Received: 2026-09-06
- Source: background run started from the session of 2026-09-06 at 14:38 local time over all 368 captured months, with `--delay-seconds 0.5`; the exact command was `python -m tools.corpus.listserv_snapshot wayback-fetch --coverage-input corpus/normalized/mail/tei-l-wayback-coverage.jsonl --delay-seconds 0.5 --normalized-output corpus/normalized/mail/tei-l-wayback.jsonl --manifest-output sources/manifests/2026-09-06-tei-l-wayback.yaml`
- Target: `corpus/normalized/mail/tei-l-wayback.jsonl` and `sources/manifests/2026-09-06-tei-l-wayback.yaml`, then the TEI-L rows of [[knowledge/state]] and the lock `sources/locks/tei-l-archive.yaml`
- Context: the run writes its normalized output and manifest only at the end and has no resume support, so a run interrupted by the end of the session leaves the fetched pages in the content-addressed raw store without a manifest and a re-run fetches every page again; a bounded test of one month showed index-only rows for messages without an individual Wayback capture, so expect `messages_index_only` close to `messages_missing`; the fetch was still running when the session of 2026-09-06 closed (about 1,400 raw pages stored by 20:00)
- Next action: if the manifest exists, add it to the lock, update the state rows, run the control-plane check and commit; if it does not, give `wayback-fetch` a resume that skips months whose index and message pages are already in the raw store, test it, and re-run the command
