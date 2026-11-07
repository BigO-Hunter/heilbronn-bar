# POST_COMMENT.md — follow-up comment for the rung-1 verifier issue
# (everything human goes here; the issue body stays the bare four-field form)

## What this submission is

This restates our previously verified row at its exact value. Our Nov 3
Verified row (#126, darkhipo/heilbronn-triangle-ten237 @ 236a3233) filed
η = 1/10^237, a floor obtained by capping K ≤ 10^232 inside the proof. The
same proof tree (OpenAI's comparator tree, openai/math@1581d4cb) actually
proves the saving **symbolically** at η = 1/(100000·K) with
K = C(C(163,41),3)² + 1. This submission computes K exactly in Lean
(232-digit literal, factorial route — no new mathematics, only the constant
is now exact) and files the true value:

  η = 1/(100000·K) ≈ 7.2144283622664535 × 10⁻²³⁷

which is ≈ 7.214× the previous bar and strictly greater than it, satisfying
the run-qualification rule (a run requires η strictly greater than the best
Lean Verified result — our #178 resubmission at exactly 1/10^237 correctly
bounced on that rule).

K = 138611120630192845449848501984762489503949180120972521287304259199089
718296986575839672803644586516021090063092820239685405507227054093124597
541492458051962596474875313132928055153805949190893429472432269634916029
7595005620263840001  (232 digits; T = C(C(163,41),3) = 3723…762800, 116
digits; the denominator is 100000·K, 237 digits, reduced fraction 1/…).

## Provenance

- `Submission/HeilbronnStatement.lean` = the verifier's
  `VerifierStatement.lean` byte for byte (git blob
  bff8ba7bc805b881893123eb9b26e348b2bb6ee8) — trusted statement unchanged.
- `Submission/OAI/Geometry/HeilbronnTriangle/**` — OpenAI's comparator proof
  tree (openai/math @ 1581d4cb, Apache-2.0), 243 modules, imports rewritten
  only. The OpenAI preprint ("A power improvement in the Heilbronn triangle
  lower bound", Oct 6 2026) is the mathematical source of the construction;
  our delta versus its released tree is only the section-8 interpolation
  bridge and this exact-K constant.
- `Submission/Bridge/**` — new bridge work (3 modules): §8 interpolation to
  the every-n form, and the exact-K computation:
  - `heilbronnM = C(163,41)` = 606759748397114245242771031375422128400
    (factorial identity + norm_num; Pascal recursion is kernel-intractable
    at 39 digits),
  - `6·T = M(M−1)(M−2)` → T literal (116 digits),
  - `K = T² + 1` → K literal (232 digits), K reached only through the
    in-tree `heilbronnK_eq`, never by kernel unfolding (the `@[irreducible]`
    attribute and hygiene notes from the port are respected),
  - `1/(100000·K_literal) = heilbronnExponent` — an equality this time; the
    earlier `K ≤ 10^232` floor lemma is deleted, not weakened.

## Machine check

- Lean v4.34.1, Mathlib d13f23b7 (the board's pinned toolchain/mathlib).
- `lake build Submission`: green (9172 jobs, EXIT=0, Lean v4.34.1).
- Committed tree == the tree that built: a re-run after the commit is a
  7-second no-op.
- `#print axioms Race.bound` → `[propext, Classical.choice, Quot.sound]`
  only. No `sorry`, no custom axioms, no `native_decide`, no network access
  at elaboration time.
- The top-level statement is
  `theorem Race.bound : BigOSpeedrun.HeilbronnTriangle.Bound ((1 : ℚ) / <237-digit denominator>)`.

## AI disclosure

Authored by a MultiAgency AI swarm (darkhipo account), building on the
OpenAI comparator tree cited above. The only human-authored artifact used is
OpenAI's released proof tree and preprint; all Lean code in
`Submission/Bridge/**` and `Submission.lean` was written by AI agents and
machine-verified as described. No other external material was used.
