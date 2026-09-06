# Second entity-run support review

These files are audit records, never sources or grounding targets. The review
scope is the twelve sources admitted for the second run of the topic Metadata
and Entities on 2026-09-06, eight P5 4.12.0 specifications (att.personal,
att.global.responsibility, att.global.source, att.editLike, att.datable, idno,
place, state), the release's test document testnames.xml, and three GitHub
threads (issues 337, 2739 and 1414) admitted as citation-only sources whose
quotations the quotation check reconciles against the raw snapshots, together
with the thirty-one assertions built on the run, which `tests/test_entity_review_audit.py`
lists by name.

`pairs.jsonl` holds the unmodified prompts emitted by `tools/review.py emit`,
one per core statement and one per assertion anchor, each with its SHA-256.
`verdicts.jsonl` records one independent judgement per pair, bound to that
hash, from a fresh context through `tools/review.py run`, which calls
`claude -p` once per pair, so the reviewer saw only the supplied passage and
claim. `raw-sources.jsonl` and `raw-assertions.jsonl` keep the reviewers'
complete responses behind the recorded verdicts.

The source review ran in three rounds. In the first round every specification
pair passed, one test-document pair overreached, and about half of the judged
thread pairs failed because a quotation capped at fifteen words could not carry
the frame of its statement; the pairs of issue 2739 and the last twelve pairs
of issue 337 received no verdict in that round because the review calls failed.
In the second round the thread distillates carried quotations of at most one
sentence and statements narrowed to what the quotation shows, and every pair
passed. The third round followed because the assertions built on the threads
name the issue they come from while the assertion review sees the distillate
statement alone, so every thread statement was prefixed with its issue and the
changed pairs were judged again; one fragment of issue 337 that could not be
lengthened across a hard line break was removed instead. Unchanged pairs kept
their earlier verdicts, which `tools/review.py run --only-missing` verified by
prompt hash. `pairs-round1.jsonl`, `verdicts-round1.jsonl`,
`raw-sources-round1.jsonl` and the `*-round2.jsonl` files keep the earlier
rounds inspectable.

Every distillate of this run was authored by Opus and reviewed by Fable; the
assertions were authored by Fable and reviewed by Opus, all thirty-one passing
in the first round. Independence of context and of model does not imply
independence of the family's errors. Later source or claim changes require new
prompts and fresh review; old verdicts do not apply.
