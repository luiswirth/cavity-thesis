# CLAUDE.md

Guidance for working on this thesis. Layout, build and the results pipeline are
in the README. The wider project, of which this thesis is one component, is
described in the `maxwellgp-project` workspace. General writing and code
guidelines are in the global `~/.claude/CLAUDE.md`, which is authoritative; this
file carries only what is specific to the thesis.

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

## Writing

Concision is the mandate: this is pass/fail, not publication prose. Lean, direct
register, short declarative sentences, everything stated once.

- Voice: impersonal, with the authorial "we" where appropriate.
- Present tense for method and results, past tense for what was actually run.
- Fixed spellings: EPGP, PEC, wavenumber as one word.
- Headings are short noun phrases with no leading article.
- Do not use bold or italic to stress a word. Bold is wanted in one place only:
  marking a term central to this thesis where it is first introduced. Do not
  bold foil or contrast terms mentioned only for context, and do not introduce
  an abbreviation for a term that is never reused.
- Name equations in prose rather than citing them by number. No forward
  references.
- Result numbers appear only in the results chapter. The abstract is the sole
  exception.
- Place a mathematical symbol immediately after the noun it names, never before.
- Define each newly introduced object locally, preferably by naming it in prose
  rather than in a separate note.
- Keep the description of experimental findings separate from interpretation,
  and state any unverified interpretation as explicit conjecture.
- Solver sections contain only solver-specific equations. Do not restate shared
  definitions.
- Typst labels only where cross-referenced; strip orphans.
- Prefer Typst code mode `{...}` over content mode `[...]` where the body is
  mostly commands, so no stray hashes.

Citations are a single final pass, not chased while drafting. Give a specific
locator and verify every one against the source.

## Domain caveat

The reciprocity error and the reference error are not comparable. Reciprocity
sees only the antisymmetric part of the error, so it can be arbitrarily small
while the true error is large. Never infer accuracy from it, and never compare
the two directly.

## Operational

- `./watch.sh` runs continuously and auto-compiles. Never run `./build.sh`
  merely to check that the document compiles.
- The repository is tagged `semester-thesis` at the submitted state and the
  appendix links to that tag. It must not move; a finished V2 gets its own tag.
