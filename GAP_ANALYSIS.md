# GAP_ANALYSIS.md — what clears the bar, and which gap class each rung is

Bar: η_verified = 1/10²³⁷ (ours, #126). A run needs η strictly > 1e-237.

## Rung 0 — why #178 bounced (process, not math)

#178 re-filed the bar value from a rebuilt tree. Equal value ⇒ no run.
Zero math gap; pure resubmission error. Lesson holds: verified rows set the
bar — and our own verified row was the thing we failed to beat.

## Rung 1 — ALREADY PROVED, NOT YET FILED: η = 1/(100000·K_exact) ≈ 7.214e-237

The tree's top statement is the every-n form at the **symbolic** exponent
`heilbronnExponent = 1/(100000·K)`. #178/#126 filed the crude floor
1/(100000·10²³²) using `heilbronnK ≤ 10²³²`. But `KBound.lean` already
computes M exactly, and the exact K is:

- M = C(163,41) = 606759748397114245242771031375422128400 (39 digits; matches
  the Lean literal — verified in Python with math.comb)
- T = C(M,3) = M(M−1)(M−2)/6 = 37230514451212307341579258391864337055334
  059182582962517976151329575965621134724577475162784520018371181237814762800
  (116 digits; matches math.comb(M,3))
- **K = T²+1 = 1386111206301928454498485019847624895039491801209725212873
  04259199089718296986575839672803644586516021090063092820239685405507227054
  09312459754149245805196259647487531313292805515380594919089342947243226963
  49160297595005620263840001** (232 digits)
- **File: η = 1/(100000·K) = 1/1386111…000100000** (237-digit denominator,
  numerator 1 ⇒ automatically reduced) ≈ **7.2144·10⁻²³⁷**
- **7.214× strictly better than the bar.** Denominator digit count 237 < 238,
  same size class the form already accepted for 1/10²³⁷.

Lean work: replace the literal `10^232` in KBound/bound_stageB/Race.bound by
the exact K literal; prove `(K_literal : ℕ) = heilbronnK` via the existing
factorial route (`heilbronnM_val` + `heilbronnT_mul_six` + `heilbronnK_eq`),
then norm_num on the 232-digit equality. Must respect the kernel-hygiene rule
documented in Assembly.lean (never whnf the @[irreducible] K; ℝ-side rewrites
only). Effort: hours. **Gap class: prover-gap (trivial) — zero new math.**

## Rung 2 — the paper exponent: η = 2/(45435·K+16) ≈ 3.176e-236 (31.8× over bar)

At true K this equals the board's OpenAI baseline row (≈3.18e-236 — exact
match, Python-verified). Filing it would make **the board's own baseline
Lean Verified** — a strong scientific statement. But the 243-module tree's
top theorem is stated at the weakened 1/(100000·K) form; recovering 2/(45435K+16)
means exposing the sharp constant through the tree (or re-deriving its top).
Depth unknown until scoped. **Gap class: prover-gap in the math (published
paper proves it), formalization-effort unknown — needs a scoping pass.**

## Rung 3 — the claimed frontier: Blinov 1.96e-8 (1/50893237), Chen 1.98e-8

~2.8·10²²⁸ × beyond rung 1. Board proof-scope rows say it outright: Blinov's
Lean covers only the degree-5/7 norm decomposition, interpolation descent,
finite packing, tag separation, finite fresh-digit probability; the interface
instantiation, Smith-divisor identification, slab, lattice, orbit, deletion,
prime-progression and the full theorem are WRITTEN proofs assuming a pinned
manuscript's estimates. Chen: no Lean at all (PDF only, no independent check).
So the math is published-claimed, not new — but formalizing it is a
project the size of (or larger than) the entire current 247-module tree,
repeated per estimate stack. **Gap class: formalization-gap (large,
months-scale), not math-gap.** If any written step is wrong, formalization is
where that surfaces — that is the value and the risk.

## Summary table

| Rung | η | vs bar | Class | Effort |
|---|---|---|---|---|
| 0. #178 (filed) | 1e-237 | = bar, bounced | process error | — |
| 1. exact-K filing | 1/(100000·K) ≈ 7.214e-237 | **7.2× better** | prover-gap, trivial | hours |
| 2. paper exponent | 2/(45435K+16) ≈ 3.176e-236 | 31.8× | prover-gap, scope unknown | days? |
| 3. Blinov/Chen | ~2e-8 | ~2.8e228× | formalization-gap, large | months |
