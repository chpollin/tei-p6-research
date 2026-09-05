# Research-wave-one support review

These files are audit records, never sources or grounding targets. The review
scope is the four new publication distillates and their four assertion pairs.
The P5 assertion also used by the synthesis chapter belongs to the separately
recorded text-identity pilot audit.

`pairs.jsonl` contains unmodified prompts emitted by `tools/review.py`, filtered
to this scope. Each prompt has a SHA-256. `verdicts.jsonl` records an independent
fresh-context judgment bound to that hash. The reviewer sees only the supplied
passage and claim, without the producer's reasoning. The same model family was
used, so independence of context does not imply independence of model errors.

The `*-round1.jsonl` files preserve the first review, including its objection
to the Renear/Wickett assertion heading. The revised heading stays within the
source's distinction about modifying a persistent entity. Later source or
claim changes require new prompts and fresh review; old verdicts do not apply.

Run `py -3 tools/check_wave1_sources.py . --review-only` to check current scope,
unmodified canonical prompts, and passing verdict hashes without local raw data.

Quotation fidelity is checked separately by `tools/check_wave1_sources.py`
against the exact local raw snapshots and bibliography admission manifest.
HTML is decoded once, visible inline text is joined without invented spaces,
block boundaries are separated, and whitespace is folded; JSON ticket fields
remain literal. The checker tests substring identity, not the semantic force
of a passage or the correctness of the human-readable section locator. Those
locators were checked during source reading. No full third-party text is
published in this audit.

These checks do not confer human verification or approve the model assumptions.
