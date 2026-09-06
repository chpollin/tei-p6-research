# Second entity-run support review

These files are audit records, never sources or grounding targets. The review
scope is the twelve sources admitted for the second run of the topic Metadata
and Entities on 2026-09-06, eight P5 4.12.0 specifications (att.personal,
att.global.responsibility, att.global.source, att.editLike, att.datable, idno,
place, state), the release's test document testnames.xml, and three GitHub
threads admitted as citation-only sources whose quotations the quotation check
reconciles against the raw snapshots, together with the assertions later built
on them.

`pairs.jsonl` holds the unmodified prompts emitted by `tools/review.py emit`,
one per core statement, each with its SHA-256. `verdicts.jsonl` records one
independent judgement per pair, bound to that hash, from a fresh context through
`tools/review.py run`, which calls `claude -p` once per pair, so the reviewer saw
only the supplied passage and claim. Every distillate of this run was authored
by Opus and reviewed by Fable. Independence of context and of model does not
imply independence of the family's errors. `raw-*.jsonl` keep the reviewers'
complete responses. Later source or claim changes require new prompts and fresh
review; old verdicts do not apply.
