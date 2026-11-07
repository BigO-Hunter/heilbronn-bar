# PLAN.md — verdict + recommended action (DRAFT, nothing public)

## Verdict

**(a) improve-our-bound — RECOMMENDED, rung 1.** The bounce cost us nothing
but a listing; the fix is cheap and restarts the ladder under our own name.
The tree already proves more than we filed; file the true value.

## The plan (rung 1: exact-K submission)

1. **Branch** from darkhipo/heilbronn-triangle-lean @ 7587116.
2. **KBound-exact.lean** (edit of KBound.lean):
   - keep `heilbronnM_val` as-is;
   - add `heilbronnT_val : (heilbronnT : ℝ) = T_literal` — reuse
     `heilbronnT_mul_six`, then `norm_num` the 39→116-digit division (T =
     M(M−1)(M−2)/6; Python-verified literal in GAP_ANALYSIS.md);
   - add `heilbronnK_val : (heilbronnK : ℝ) = K_literal` via `heilbronnK_eq`
     + `heilbronnT_val`, norm_num on the 232-digit square (replaces the
     ≤-vs-10²³² hnum step with an equality — same norm_num class);
   - replace `eta_le_heilbronnExponent` with the equality form
     `(1:ℝ)/(100000·K_literal) = heilbronnExponent`.
   - RESPECT the Assembly kernel-hygiene note: no Nat.pow_pos/nlinarith/
     exact_mod_cast over K-headed ℕ expressions; keep K opaque except through
     `heilbronnK_eq` + the M-literal route; keep `set_option maxRecDepth 4000`.
3. **Assembly.lean / Submission.lean**: restate `bound_stageB` at
   `(1:ℝ)/(100000·K_literal)`; `Race.bound : Bound ((1:ℚ)/<237-digit literal>)`.
4. **Verify locally**: `lake exe cache get && lake build Submission` (warm ~7
   min on 12 cores, budget 320-min deadline); `#print axioms Race.bound` must
   stay `[propext, Classical.choice, Quot.sound]`; no sorry/native_decide.
5. **File** new verifier issue (bound field = 1/<den literal>, one reduced
   fraction; denominator 237 digits < the accepted 238-digit class; cite #178
   bounce + #126 row in the description).

Expected: Lean Verified row at η ≈ 7.214e-237, rank unchanged (still 11th —
all claimed rows above are far stronger) but the bar moves up 7.2× under a
strictly stronger verified statement.

## Pre-position (rung 2, when the bar opens again)

- **Scoping pass** (1 session): grep the 243-module tree for where the paper's
  2/(45435k+16) form was normalized to 1/(100000·K); decide if the sharp form
  can be exposed at the top or needs re-derivation through the deletion/
  cardinality layer. If exposed: file 2/(45435·K+16) ≈ 3.176e-236 = the
  OpenAI baseline value, Lean-verified — makes the race's own baseline a
  machine-checked row. That is a real scientific contribution and the natural
  next bar-move.
- **Statement sketch** (rung 3 pre-position, do NOT start): formalizing
  Blinov's ladder requires the pinned manuscript's slab/lattice/probability
  estimates; each is a Mathlib-scale effort. Register as a long-horizon
  feature; revisit only after rung 2.

## Explicit pass

- Re-filing 1e-237 in any form: never — equal value cannot run (measured).
- Chen's rank-1 (1.98e-8): out of reach without the full formalization
  program; the paper has no Lean and no independent check.

## Risks

- norm_num equality on 232-digit literals is new (the existing proof only did
  a ≤ against 10²³²); if it times out, fall back to proving `T_literal · 6 =
  M·(M−1)·(M−2)` in ℕ with `heilbronnT_mul_six` + push_cast, then one
  `decide`-free ring/norm_num chain — measured classes from the smoke notes
  say 237-digit rationals cost ≤0.8 s warm.
- Digit cap: denominator 237 digits fits the accepted class; if the verifier
  still balks, the 2/(45435K+16) form (236-digit denominator, 31.8× better)
  is the fallback filing.
- nanoda re-check runs on every verified submission; keep the tree
  self-contained (no network, no native_decide) as before.
