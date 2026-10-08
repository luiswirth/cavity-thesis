# AGENTS.md

Guidance for working on this thesis. Layout, build and the results pipeline are
in the README.

The thesis was submitted 2026-07-01 and revised once, as the V2 that Kurz asked
for. It is finished. The review that shaped V2 is in
`../../project/refs/kurz/thesis-review/`.

## Writing

Keep it concise: the thesis is pass/fail, not a publication. Plain, direct
language, short declarative sentences, everything stated once.

- Voice: impersonal, with the authorial "we" where appropriate.
- Present tense for method and results, past tense for what was actually run.
- Fixed spellings: EPGP, PEC, wavenumber as one word, curl-curl hyphenated.
- An en dash joins two things that keep their separate identities, as in
  Ehrenpreis--Palamodov and accuracy--runtime. A compound modifier takes a
  hyphen.
- Headings are short noun phrases with no leading article.
- Bold marks a technical keyword where it is first introduced. Italic stresses a
  word only where the stress is needed. A canonical, informative abbreviation may
  be introduced without being reused.
- Name equations in prose rather than citing them by number. No forward
  references.
- Result numbers appear only in the results chapter, the abstract, and the
  conclusion summary.
- Place a mathematical symbol immediately after the noun it names, never before.
- Define each newly introduced object locally, preferably by naming it in prose
  rather than in a separate note.
- Keep the description of experimental findings separate from interpretation,
  and state any unverified interpretation as explicit conjecture.
- Solver sections contain only solver-specific equations. Do not restate shared
  definitions.
- Typst labels only where cross-referenced. Remove unused ones.
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
- The repository is tagged `semester-thesis` at the submitted state and `v2` at
  the revision. The appendix links to `semester-thesis`. Neither tag moves.
