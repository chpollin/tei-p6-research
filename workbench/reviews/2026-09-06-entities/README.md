# Entity-topic support review

These files are audit records, never sources or grounding targets. The review
scope is the nine distillates admitted on 2026-09-06 for the topic Metadata and
Entities, eight P5 4.12.0 specifications (persName, name, rs, person, nym,
att.canonical, att.naming, relation) and the Guidelines chapter on names,
dates, people and places, together with the assertions later built on them.

`pairs.jsonl` holds the unmodified prompts emitted by `tools/review.py emit`
for the source pairs of those distillates, one per core statement, each with
its SHA-256. `verdicts.jsonl` records one independent judgement per pair,
bound to that hash. Every judgement came from a fresh context through
`tools/review.py run`, which calls `claude -p` once per pair, so the reviewer
saw only the supplied passage and claim without the producer's reasoning.
Author and reviewer models differ within one model family. The specification
distillates were authored by Opus and reviewed by Fable, the chapter
distillate was authored by Fable and reviewed by Opus. Independence of
context and of model does not imply independence of the family's errors.

The `*-round1.jsonl` files preserve the first review of the specification
pairs. Its passages carried neither the source title with its release nor the
attribute an attribute-definition block describes, because the pair cutter
showed only the heading path and the block text, and the reviewer therefore
answered "partially supports" to twenty of forty-two statements on exactly that
ground. The nine representations were regenerated under converter version 2,
whose locators name identified elements by their ident, and the cutter now
shows the source title, the heading path and the locator line with the block,
so the second round judges the passage a reader of the representation sees.

`raw-specs.jsonl` and `raw-chapter.jsonl` keep the reviewers' complete
responses. Later source or claim changes require new prompts and fresh review;
old verdicts do not apply.

Run the generic support review check named in `knowledge/testing.md` to verify
that the stored pairs match the current vault and that every verdict binds to
its prompt.
