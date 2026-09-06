# Corpus projections

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
selected primary source is admitted under the existing `00_sources`/`10_markdown`
rules, or the citation-only publication route. The projection itself is not
promoted into evidence. Downstream layers continue to
reference only the layer directly beneath them.

The P5 specification navigation projection has its bounded contract in
`knowledge/experiments.md`. Build it with:

```powershell
py -3 -m tools.tei.build_atlas --output corpus/projections/p5-specs-4.12.0.json
```

Append `--check` for a read-only byte comparison. It requires the locked local
Git mirror. The JSON represents direct declarations and source locators;
inherited semantics and a compiled P5 model remain outside its scope.
