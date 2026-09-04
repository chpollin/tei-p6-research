# Context layer

This directory controls progressive disclosure for agents. It adds no knowledge layer to the Grounded Vault chain and has no grounding authority.

- `START.md` gives the smallest useful orientation.
- `ROUTER.md` maps a task to one context manifest and one workflow.
- `manifests/` contains declarative read recipes.
- `templates/` defines the shape of a materialized context pack.
- `generated/` is reserved for deterministic pack output and is never edited by hand.

A context pack may quote or summarize canonical artifacts for retrieval, but an answer or production artifact must cite the canonical assertion, distillate or source anchor. If a pack disagrees with a canonical file, the canonical file wins and the stale pack must be rebuilt.
