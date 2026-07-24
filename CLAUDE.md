# CLAUDE.md

Guidance for working on this thesis. Layout, build and the results pipeline are
in the README. The wider project, of which this thesis is one component, is
described in the `maxwellgp-project` workspace.

The thesis was submitted 2026-07-01. The only remaining work is the V2 revision
requested by Kurz, and it is low priority; the paper takes precedence.

## V2

`.v2/KURZ_REVIEW.md` is the authority on the revision. It carries every one of
Kurz's annotations verbatim, the triage, and the fix for each, plus his
governing instruction not to invest excessive time. Read it before touching
anything V2-related.

All items there are checked off, but that pass was LLM-driven and awaits Luis's
own read-through and hand corrections. The prose is not yet where it should be.

Do not run new experiments for V2. Where a comment asks for a result that would
prove an interpretive claim, soften the claim to a conjecture instead. Items
tagged `[PAPER]` in that file are out of scope here and have been migrated to a
`SIAM_Journal` issue.

## Writing style

Concision is the mandate: this is pass/fail, not publication prose.

- Voice: impersonal, with the authorial "we" where appropriate.
- Lean, direct register. Short declarative sentences. State everything once.
- Plain technical language. Avoid essayistic wording.
- Present tense for method and results, past tense for what was actually run.
- US spelling, Oxford `-ize`/`-ization`.
- Fixed spellings: EPGP, PEC, wavenumber as one word.
- Headings and titles are short noun phrases with no leading article.
- Captions are minimal. The prose describes the figure; reference it there.
- No emphasis by bold or italic in prose.
- Block equations for load-bearing statements, inline math for incidental
  quantities. No trailing punctuation in display math.
- Name equations in prose rather than citing them by number. No forward
  references.
- Typst labels only where cross-referenced; strip orphans.
- Solver sections contain only solver-specific equations. Do not restate shared
  definitions.
- Result numbers appear only in the results chapter. The abstract is the sole
  exception.
- Place a mathematical symbol immediately after the noun it names, never before.
- Define each newly introduced object locally, preferably by naming it in prose
  rather than in a separate note.
- Keep the description of experimental findings separate from interpretation,
  and state any unverified interpretation as explicit conjecture.

Avoid AI-giveaway style: no em-dashes for asides, use commas, colons,
parentheses or separate sentences; do not overuse semicolons; avoid "not just X
but Y" constructions, rule-of-three padding, and hedging filler.

## Typst source

- ASCII source only. Dashes via `--` and `---`, never unicode glyphs.
- Prefer code mode `{...}` over content mode `[...]` where the body is mostly
  commands. No stray hashes.
- Break lines semantically, one unit of meaning per line. Never wrap to a
  column, never reflow.

## References

Give a specific locator (section, equation, or page) and verify every one
against the source. Never invent or guess a citation. Citations are a single
final pass, not chased while drafting.

## Domain caveat

The reciprocity error and the reference error are not comparable. Reciprocity
sees only the antisymmetric part of the error, so it can be arbitrarily small
while the true error is large. Never infer accuracy from it, and never compare
the two directly.

## Operational

- `./watch.sh` runs continuously and auto-compiles. Never run `./build.sh`
  merely to check that the document compiles.
- Never push a thesis that does not compile; a GitHub Action deploys on push.
- Luis reviews figures himself. Do not render images to inspect them.
- The repository is tagged `semester-thesis` at the submitted state, and the
  appendix links to that tag.
