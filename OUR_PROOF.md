# OUR_PROOF.md — what [BigO-Hunter/heilbronn-triangle-lean](https://github.com/BigO-Hunter/heilbronn-triangle-lean) @ 7587116 proves

Submitted 2026-11-07 as verifier issue #178. CLOSED as not planned — no run:
**#178 filed 1/10^237, the same value as the already-verified #126 row.**
It bounced on the bar rule (resubmitting the bar value earns no run), not on
proof quality.

## The theorem (Submission.lean)

```lean
theorem Race.bound :
    BigOSpeedrun.HeilbronnTriangle.Bound ((1 : ℚ) / 10^237)   -- 237-zero literal
```

`Bound (η)` (the verifier's trusted statement, byte-identical, blob
`bff8ba7bc805b881893123eb9b26e348b2bb6ee8`): ∃ c > 0, ∃ N, ∀ n ≥ N, an
n-point set in the closed unit square whose every triangle has area
≥ c·n^(−2+η). So it is **not for a specific n — it is the full "every
sufficiently large n" form**, at the asymptotic saving η = 1/10²³⁷.

## Proof anatomy (247 modules, ~1.6 MB Lean)

1. **Trusted statement** — `Submission/HeilbronnStatement.lean` = verifier's
   `VerifierStatement.lean` byte for byte. Carries OpenAI's frozen
   `OAI.Problem355` definitions: `heilbronnM = C(163,41)`,
   `heilbronnT = C(M,3)`, `heilbronnK = T²+1` (@[irreducible]),
   `heilbronnExponent = 1/(100000·K)`, and the parameterized `Bound`.
2. **OpenAI comparator tree** (243 modules, openai/math @ 1581d4cb, imports
   rewritten only) — proves the subsequence statement at the symbolic exponent
   `1/(100000·K)` (a weakening of the paper's 2/(45435k+16)).
3. **Bridge (new, 3 modules)** — the §8 interpolation to the every-n form:
   - `Cardinality.lean`: two-sided `sampleCard` bounds √2·r^(45435k+16)-type;
     upper constant depends on k only → closes the deletion ratio.
   - `KBound.lean`: `heilbronnM = 606759748397114245242771031375422128400`
     EXACT (factorial route + norm_num; Pascal recursion is kernel-intractable);
     `6T = M(M−1)(M−2)`; `T² ≤ M⁶/36`; hence **`heilbronnK ≤ 10²³²` with K
     never unfolded**; `(1:ℝ)/(100000·10²³²) ≤ heilbronnExponent`.
   - `Assembly.lean`: `bound_stageB` — Bertrand prime choice, `m = ⌈((n+1)/√2)^(1/α)⌉`
     with α = 45435K+16, deletion to exactly n points, c = C′^(−2+η) > 0.
4. **Cast** — ℚ literal 1/10²³⁷ = 1/(100000·10²³²) via norm_num.

Build: Lean v4.34.1, Mathlib d13f23b7 (board pins), 9172 jobs, EXIT=0.
Axioms of `Race.bound`: `[propext, Classical.choice, Quot.sound]` only.
No sorry, no native_decide, no custom axioms.

## Was it ever going to clear the bar?

No — but not because the proof is weak. **The bar was set by our own #126
(three days earlier) at the identical value 1/10²³⁷.** The gap is structural
*process*: the tree proves the saving symbolically at 1/(100000·K), and #178
instantiate it at the crude cap K ≤ 10²³² instead of the exact K. The true
proved saving is ≈ 7.2× larger than what was filed (see GAP_ANALYSIS.md).
