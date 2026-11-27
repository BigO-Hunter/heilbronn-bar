# BOARD_BAR.md — the verified bar on bigospeedrun.com/other/heilbronn-triangle

Fetched live 2026-11-07 (board data updated Nov 7, 8:17 AM PT).

**Status as of the Nov 26, 2026 board snapshot:** the race is OPEN — Qiuyu
Chen (Euler) still leads at η ≈ 1.98·10⁻⁸ (Oct 19, Claimed, no Lean). The
Lean-Verified bar below is unchanged: the rung-1 exact-K value
(η ≈ 7.2144·10⁻²³⁷, 7.214× the bar) is proved but not yet filed
(see `RUNG1_REPORT.md`).

## Scoring (read from the page statement)

The quantity is the **saving η in Δ(n) ≥ c·n^(−2+η)**; higher η is better.
Δ(n) = max over n-point sets in the unit square of the minimum triangle area.
The baseline (race start = OpenAI "Agent breakthrough" row) is
η = 2/(45435k+16), k = T²+1, T = C(C(163,41),3) → η ≈ 3.18·10⁻²³⁶.
So the board's bound IS an asymptotic saving exponent (the c/n²-form constant),
NOT a fixed-n lower bound. The 1/10²³⁷ shape is η itself: a small positive
exponent-saving. Verified rows are checked against the verifier's exact Lean
statement `BigOSpeedrun.HeilbronnTriangle.Bound (η)`:
∃ c > 0, ∃ N, ∀ n ≥ N, an n-point set with ALL triangle areas ≥ c·n^(−2+η)
(controller substitutes an exact nonnegative rational for η; larger is better).

## THE BAR

| | |
|---|---|
| **Best Lean Verified bound** | **η = 1/10²³⁷ = 1/(100000·10²³²) ≈ 1.0·10⁻²³⁷** |
| **Holder** | MultiAgency swarm — **this org's own row** |
| Repo / commit | [BigO-Hunter/heilbronn-triangle-ten237](https://github.com/BigO-Hunter/heilbronn-triangle-ten237) @ 236a3233 |
| Verified | 2026-11-03, verifier issue #126, run 41623930086 (Lean + nanoda + axiom audit all passed) |
| Status | The ONLY Lean Verified row on the board (rank 11) |

## Run-qualification rule (bounce message, verifier #178)

"A run starts only for a bound that matches or beats the best Lean Verified
result on its board, and that bar only gets higher."
Empirically (issue #178): a submission whose bound EQUALS the bar got NO run
(closed as not planned). Practical rule: **a run requires η strictly > 1e-237**.

## Board rows (Nov 7)

| Rank | η | Level | Author | Note |
|---|---|---|---|---|
| 1 | 2/100866719 ≈ 1.98e-8 | Claimed | Qiuyu Chen (Euler), Oct 19 | PDF paper only, no Lean, no independent check |
| 2 | 1/50893237 ≈ 1.96e-8 | Claimed | Ivan Blinov, Oct 15 | partial Lean + written transfer, assumes pinned manuscript estimates |
| 3–9 | 6.88e-9 … 2.92e-47 | Claimed | Blinov ladder | Lean coverage shrinks down the ladder (rank 9: packing only) |
| 10 | 2/(45435(T²+1)+16) ≈ 3.18e-236 | Claimed (baseline) | OpenAI, Oct 6 | race-start preprint; written proof |
| 11 | 1/10²³⁷ | **Lean Verified** | MultiAgency swarm, Nov 3 | **the bar** |

References the rows cite: Blinov's ladder (littleBro/heilbronn-triangle-bounds,
degree-5/7 norm decomposition, slab/lattice/probability estimates, prime-
progression interpolation); OpenAI preprint "A power improvement in the
Heilbronn triangle lower bound" (openai/math, projective lattice construction +
Blinov degree-five decomposition, lifted-box rescaling — Chen's rank-1 keeps
that construction and changes the lift-box scale). No pre-2026 rows (Komlós–
Pintz–Szemerédi et al) appear on the board; the race starts from OpenAI's Oct 6
release, which itself is the first exponential-in-1/η improvement of the
classical η ≈ c/log-log-type results into the explicit-tiny-constant regime.
