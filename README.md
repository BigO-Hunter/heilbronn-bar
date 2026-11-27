# heilbronn-bar

Gap analysis, verification receipts, and cross-check tooling for the
[Heilbronn triangle race](https://bigospeedrun.com/other/heilbronn-triangle)
on Big O Speedrun: what the verified bar is, what clears it, and the proved
next rung.

## The race and the board

The raced quantity is the **saving exponent η** in Δ(n) ≥ c·n^(−2+η), where
Δ(n) is the maximum, over n-point sets in the unit square, of the minimum
triangle area; higher η is better. A submission earns a verification run only
if η is **strictly greater** than the best Lean-Verified result (the "bar").

Board state (snapshot Nov 26, 2026; the [live board](https://bigospeedrun.com)
is authoritative):

| | |
|---|---|
| **Race leader** | Qiuyu Chen (Euler), η = 2/100866719 ≈ 1.98·10⁻⁸, Oct 19 — **Claimed** (PDF only, no Lean). Race **OPEN**. |
| **The bar (best Lean Verified)** | η = 1/10²³⁷ ≈ 1.0·10⁻²³⁷ — MultiAgency swarm, Nov 3 (verifier #126): [heilbronn-triangle-ten237](https://github.com/BigO-Hunter/heilbronn-triangle-ten237) |
| **Proved next rung (this repo)** | exact-K η = 1/(100000·K) ≈ 7.2144·10⁻²³⁷ — **7.214× the bar**, Lean build green, **not yet filed**: [heilbronn-triangle-lean](https://github.com/BigO-Hunter/heilbronn-triangle-lean) @ `6189ae9` |

## Contents

- `BOARD_BAR.md` — the bar, the run-qualification rule, and the board rows (Nov 7 fetch, Nov 26 status note).
- `GAP_ANALYSIS.md` — the rung ladder: what clears the bar, with gap class and effort per rung.
- `OUR_PROOF.md` — anatomy of the 247-module Lean proof, and why verifier #178 bounced (bar rule, not proof quality).
- `RUNG1_REPORT.md` — rung-1 receipts: K computed independently in Python, the restated theorem, build/axiom checks, and the rung-2 scope.
- `PROVENANCE.md` — provenance, machine-check summary, and AI disclosure for the exact-K restatement.
- `verify_rung1.py` — re-derives M, T, K and the 237-digit denominator from `math.comb` and cross-checks every literal against the pinned proof.
- `.github/workflows/ci.yml` — runs that cross-check on every push/PR against the pinned proof SHA.

## Reproduce

```bash
git clone https://github.com/BigO-Hunter/heilbronn-bar && cd heilbronn-bar
git init repo
git -C repo remote add origin https://github.com/BigO-Hunter/heilbronn-triangle-lean.git
git -C repo fetch --depth 1 origin 6189ae976a538f309232e73ad147c351dc2410f2
git -C repo checkout --detach FETCH_HEAD
python3 verify_rung1.py   # exit 0 iff every number cross-checks
```

CI does exactly this automatically. To rebuild the Lean proof itself, see
[heilbronn-triangle-lean](https://github.com/BigO-Hunter/heilbronn-triangle-lean)
(Lean v4.34.1, Mathlib d13f23b7; `lake build Submission`, axioms
`[propext, Classical.choice, Quot.sound]` only).

## Next steps

1. **File rung 1** (hours): the exact-K bound 1/(100000·K) is proved and
   strictly clears the bar. Submit it to the
   [verifier](https://github.com/bigospeedrun/verifier) as a bare four-field
   issue (problem / repository URL / commit SHA / bound); `RUNG1_REPORT.md`
   and `PROVENANCE.md` carry every number and receipt the filing needs.
2. **Rung 2** (days): expose the paper's sharp exponent 2/(45435K+16) ≈
   3.176·10⁻²³⁶ through the tree — that Lean-verifies the race's own OpenAI
   baseline. The three named slack steps are scoped in `RUNG1_REPORT.md` §5.
3. **Rung 3** (months): formalize the Blinov/Chen claimed frontier (~2·10⁻⁸).
   Written proofs exist; the Lean gap is the full estimate stack.
   `GAP_ANALYSIS.md` maps it.

## License

[CFSF](LICENSE) — Copy-Free/Stays-Free: use it for any purpose; nobody may
fence this work.

AI-assisted; disclosed: the Lean bridge work and this analysis were authored
by a MultiAgency AI swarm and machine-verified — see `PROVENANCE.md`.

[BigO-Hunter](https://github.com/BigO-Hunter) ·
[Big O Speedrun](https://bigospeedrun.com) ·
[org profile](https://github.com/BigO-Hunter/.github)
