# Changelog

Material changes to the TEI P6 Research Vault are recorded here. Architectural
rationale remains in the append-only `knowledge/journal.md`; Git preserves the
complete file history.

## 2026-09-04

### Project baseline

- Instantiated the Grounded Vault as the independent TEI P6 Research Vault.
- Added the five-layer provenance chain, validator, tests, CI, Obsidian
  configuration, twelve topic MOCs, and Codex/Claude action layers.
- Added TEI-specific source registries, locks, corpus boundaries, context
  manifests, and analysis workflows.
- Pinned TEI P5 4.12.0 to full commit
  `113e933e21f016e2655518321e9d10214b8d9fcb`.

### Acquisition contract

- Added the staged multi-agent acquisition runbook.
- Separated the official TEI P6 process from independent P6 proposals.
- Separated the official Council meeting index from the incomplete
  `TEIC/Documentation` working-document repository.
- Defined observable and bounded completeness, raw-data quarantine, rights
  gates, resumable acquisition, and reconciliation requirements.

### Promptotyping project scaffold

- Reframed `knowledge/` as the executable Promptotyping document of the project.
- Expanded the project specification with seven research questions, a
  source-authority model, comparative P6 evaluation dimensions, deliverables,
  success criteria, and decision gates.
- Rebuilt `README.md`, `HOME.md`, `AGENTS.md`, `CLAUDE.md`, and `SETUP.md` as
  consistent project-specific entry points.
- Adapted the generated project page to the TEI P6 project and added the
  specification, state, and journal sections.
- Removed obsolete routes into the upstream template's example research
  instance.

### P6 design knowledge

- Added a repository-wide architecture map and contribution contract.
- Added the provisional P6 design dossier covering design principles, the
  candidate core model, blueprints and customization, serialization and
  conformance, executable examples and migration, comparative evaluation,
  versioning and governance, and the research agenda.
- Connected human and agent navigation to the dossier while preserving the
  distinction between provisional design knowledge and grounded evidence.

### Primary-source acquisition

- Defined the finite, auditable meaning of “all primary sources” and registered
  normative, governance, historical, implementation, community, and practice
  source families.
- Added tested collectors for Git mirrors, the TEIC GitHub organization census,
  GitHub work items, bounded web indexes, SourceForge trackers, and large release
  assets.
- Began content-addressed acquisition of P5 4.12.0, every public TEIC Git
  repository, P5 release history, Council and Board records, the TEI Archive,
  official P6 records, tooling, customizations, and legacy trackers.
