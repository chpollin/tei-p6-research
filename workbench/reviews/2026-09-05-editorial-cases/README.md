# Editorial case support review

These files are audit records, never sources or grounding targets.

The `*-cutter1.jsonl` files preserve the pairs and verdicts recorded under the
first pair cutter. On 2026-09-06 the cutter began to show the source title,
the heading path and the locator line with each block, so the three source
pairs were re-judged in fresh contexts by a different model
(`claude-fable-5-1`, one `claude -p` call per pair) against the current
prompts; the three assertion pairs keep their earlier verdicts, whose prompts
did not change. `pairs.jsonl` and `verdicts.jsonl` hold the current binding.
