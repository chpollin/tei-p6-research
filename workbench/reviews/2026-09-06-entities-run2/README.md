# Second entity-run support review

These files are audit records, never sources or grounding targets. The review
scope is the twelve sources admitted for the second run of the topic Metadata
and Entities on 2026-09-06, eight P5 4.12.0 specifications (att.personal,
att.global.responsibility, att.global.source, att.editLike, att.datable, idno,
place, state), the release's test document testnames.xml, and three GitHub
threads (issues 337, 2739 and 1414) admitted as citation-only sources whose
quotations the quotation check reconciles against the raw snapshots, together
with the assertions later built on them.

`pairs.jsonl` holds the unmodified prompts emitted by `tools/review.py emit`,
one per core statement, each with its SHA-256. `verdicts.jsonl` records one
independent judgement per pair, bound to that hash, from a fresh context through
`tools/review.py run`, which calls `claude -p` once per pair, so the reviewer saw
only the supplied passage and claim. `raw-sources.jsonl` keeps the reviewers'
complete responses behind the recorded source verdicts.

The source review ran in two rounds. In the first round every specification
pair passed, one test-document pair overreached, and about half of the judged
thread pairs failed because a quotation capped at fifteen words could not carry
the frame of its statement; the pairs of issue 2739 and the last twelve pairs
of issue 337 received no verdict in that round because the review calls failed.
The thread distillates were reformulated with quotations of at most one sentence
and statements narrowed to what the quotation shows, every changed pair was
judged again in a fresh context, and the unchanged pairs kept their first-round
verdicts, which `tools/review.py run --only-missing` verified by prompt hash.
`pairs-round1.jsonl`, `verdicts-round1.jsonl` and `raw-sources-round1.jsonl`
keep the first round inspectable. Every distillate of this run was authored by
Opus and reviewed by Fable. Independence of context and of model does not imply
independence of the family's errors. Later source or claim changes require new
prompts and fresh review; old verdicts do not apply.
