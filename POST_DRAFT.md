# POST_DRAFT.md — rung-1 verifier submission issue BODY (BARE FOUR-FIELD FORM)

Per the #173 parser lesson: NOTHING else in the body. All human context goes
in a follow-up comment (see POST_COMMENT.md). Fill SHA after final commit.

---

**Problem:** heilbronn-triangle

**Repository URL:** https://github.com/darkhipo/heilbronn-triangle-lean

**Commit SHA:** 1f3615880e417a78f1c6b43d27476a50b77ed084

**Bound:** 1/138611120630192845449848501984762489503949180120972521287304259199089718296986575839672803644586516021090063092820239685405507227054093124597541492458051962596474875313132928055153805949190893429472432269634916029759500562026384000100000

---

Notes (NOT part of the body):
- Bound = 1/(100000·K), K = heilbronnT²+1 = T²+1, T = C(C(163,41),3) — the
  exact 232-digit K; denominator is 237 digits (one reduced fraction,
  numerator 1). Digit class: 237 < 238 (the cap the form accepted for the
  previous 1/10^237 filing), so format-accepted.
- η ≈ 7.2144283622664535e-237 — strictly greater than the current Lean
  Verified bar 1/10^237 = 1.0e-237 (ratio ≈ 7.214×), so the run rule
  (strictly > bar; #178 lesson: equality bounces) is satisfied.
- Statement is `BigOSpeedrun.HeilbronnTriangle.Bound ((1:ℚ)/<den literal>)`
  — byte-identical trusted statement, blob bff8ba7bc805b881893123eb9b26e348b2bb6ee8.
