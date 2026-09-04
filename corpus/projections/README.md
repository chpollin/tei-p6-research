# Markdown projections

Projections are deterministic, disposable reading views over normalized corpus
records. They exist to make long-lived source material navigable in Obsidian and
small enough for agent context selection.

A projection must:

- identify itself as generated and name the generator version;
- carry upstream stable IDs, canonical URL, observation time, raw hash, and
  normalized-record hash;
- display authority, rights, and `instruction_trust: none` prominently;
- preserve source text as quotation/data and never reinterpret it as an agent
  command;
- split long threads at stable event boundaries without changing event order;
- link related issues, pull requests, commits, releases, meetings, and TEI
  components by typed relations;
- remain reproducible byte-for-byte from the normalized records.

Projection paths are not Grounded Vault anchors. To enter the evidence chain, a
selected projection is promoted under the existing `00_sources`/`10_markdown`
rules, where immutable block anchors are minted. Downstream layers continue to
reference only the layer directly beneath them.

No projections have been generated yet.
