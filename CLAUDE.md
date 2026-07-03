# CLAUDE.md

Guidance for working on this thesis. Source is Typst under `src/`; build with
`./build.sh`.

## Writing style

- Avoid parentheses in running prose. Prefer commas, em-dashes, or restructuring.
  Keep parentheses only for acronym definitions, cross-references, and mathematics.
- Keep citations lowkey. Prefer a trailing `#cite` at the end of the sentence or
  clause, which the author-date style already sets in parentheses. Do not set them
  off as comma-delimited notes ("..., as shown in X") or build a sentence around
  them ("We refer to X for..."). Narrative "prose" form is fine only where the
  author is a natural part of the sentence.
- Place a mathematical symbol immediately after the noun it names, never before.
- Define each newly introduced object locally, preferably by naming it in prose
  rather than in a separate note.
- Keep the description of experimental findings separate from interpretation.
  State any unverified interpretation as explicit conjecture.

## References

- Give a specific locator (section, equation, or page) and verify every one
  against the source. Never invent or guess a citation.

## Layout

- Do not place manual page breaks in the body chapters; let content reflow.
  Chapter breaks are handled by the templates in `setup.typ`.

## Build

- Build with `./build.sh` (Typst). The body font is New Computer Modern Sans.

## Review workflow

- Mark new or changed content with the `hl`, `hlx`, and `hlb` helpers in
  `src/setup-math.typ`, then set `review: false` for a clean version.
- Working context (feedback briefing, claims audit) lives in `.v2/`.
