# Portable Obsidian configuration

The repository root is the Obsidian vault. This directory commits only portable settings and requires no community plugins.

Per-device workspace state, caches and installed plugin code are ignored locally. Keep the Grounded Vault Markdown portable. Use the existing wikilinks and block references, and do not make canonical knowledge depend on Dataview, Bases, Canvas or another plugin-specific index. `README.md` is the human entry point and `knowledge/INDEX.md` the hub of the knowledge base, whose topic-map section enters the research content. Agents enter through `CLAUDE.md` or `AGENTS.md`, which route into the same hub.

The ignored-path list keeps the source pools, the build machinery and the locally retained upstream Grounded Vault instance under `paper/` out of routine Obsidian search. It does not change their Git status and does not make source material trusted.
