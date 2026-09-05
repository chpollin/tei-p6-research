# TEI analysis workflows

These workflows specialize the operations already defined in `knowledge/operations.md`; they do not replace them or introduce new artifact types. Use `contexts/ROUTER.md` to select one.

For persistent knowledge, every workflow must enter the standard Grounded Vault chain. A chat answer may report what the present vault does and does not support, but it must point to canonical anchors. Scratch findings do not belong in `contexts/` or `workflows/`.

Shared completion checks:

1. Separate source observation, cross-source assertion and author posit.
2. Preserve release, repository, date and source-state qualifiers.
3. Follow every load-bearing claim to the canonical layer below it.
4. Record unsupported questions in the relevant topic map when editing the vault is in scope.
5. Run the checks required by `knowledge/operations.md` and the applicable
   repository adapter (`AGENTS.md` or `CLAUDE.md`).
