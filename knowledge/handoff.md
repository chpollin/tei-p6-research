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
- Source: background run `python -m tools.corpus.listserv_snapshot wayback-fetch` over all 368 captured months, started from this session at about 15:00 local time
- Target: `corpus/normalized/mail/tei-l-wayback.jsonl` and `sources/manifests/2026-09-06-tei-l-wayback.yaml`, then the TEI-L rows of [[knowledge/state]] and the lock `sources/locks/tei-l-archive.yaml`
- Context: the run writes its manifest only at the end; a bounded test of one month showed index-only rows for messages without an individual Wayback capture, so expect `messages_index_only` close to `messages_missing`
- Next action: when the manifest exists, add it to the lock, update the state rows, run the control-plane check and commit
