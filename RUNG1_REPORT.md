# RUNG1_REPORT.md — exact-K restatement: η = 1/(100000·K) ≈ 7.2144e-237

Branch `rung1-exact-k` (fast-forwarded onto `main`) in
[BigO-Hunter/heilbronn-triangle-lean](https://github.com/BigO-Hunter/heilbronn-triangle-lean).
Base: `7587116` (the tree that filed 1/10²³⁷).
Head: **`6189ae9`** (`6189ae976a538f309232e73ad147c351dc2410f2`).

## Commits

| SHA | What |
|---|---|
| `7587116` | base: the tree filed at the crude floor 1/(100000·10²³²) |
| `a15fd64` | restate `KBound`/`Assembly`/`Submission` at the exact K literal |
| `1f36158` | fix `hstep2` orientation in `Assembly.lean`; README refresh; `AxCheck.lean` |
| `6189ae9` | reconcile `PROVENANCE.md` / `BRIDGE_EDITS.md` / Assembly docstring with the exact-K proof (they still advertised the deleted `heilbronnK_le`) |

All three pushed; `main` and `rung1-exact-k` both resolve to `6189ae9`
(verified with `git ls-remote`).

## 1. K, computed exactly (Python `math.comb`, independent of Lean)

```
M = C(163,41)              39 digits  sha256 bf470b9d734eabd6…
T = C(M,3)                116 digits  sha256 f231866b749b444f…
K = T^2 + 1               232 digits  sha256 de3716c1867ceb53…
den = 100000*K            237 digits  sha256 47d1ae1cd6c1f347…
```

T = `372305144512123073415792583918643370553340591825829625179761513295759656
21134724577475162784520018371181237814762800`
K = `138611120630192845449848501984762489503949180120972521287304259199089718
29698657583967280364458651602109006309282023968540550722705409312459754149245
80519625964748753131329280551538059491908934294724322696349160297595005620263
840001`

Every literal in the tree was cross-checked against these: `KBound.lean`
(39/116/232-digit literals) and `Submission.lean` (237-digit denominator,
twice — statement + cast) all match; no stray literals.

## 2. The restated theorem

```lean
theorem Race.bound :
    BigOSpeedrun.HeilbronnTriangle.Bound
      ((1 : ℚ) / 1386111…6384000100000)      -- 237-digit denominator
```

`Submission/Bridge/KBound.lean` now proves `heilbronnT_val` (116-digit T),
`heilbronnK_val` (232-digit K, via `heilbronnK_eq` + cast injectivity — the
`@[irreducible]` K is still never whnf'd, the Assembly kernel-hygiene note is
respected) and `eta_eq_heilbronnExponent` (an EQUALITY, replacing the old
`K ≤ 10²³²` floor; `heilbronnK_le`/`heilbronnT_le`/`heilbronnT_sq_le` are
deleted, with no remaining references). `bound_stageB` is stated AT
`heilbronnExponent`; the ≤-monotonicity step in `Submission.lean` is gone.
`set_option maxRecDepth 20000` (was 4000) covers the 232-digit literal class.
No chunking was needed: the single 232-digit `norm_num` closes in the same
compile pass as the rest of the module.

## 3. Verification receipts

| Check | Result |
|---|---|
| `lake build Submission` | **9172 jobs, EXIT=0** (Assembly alone 65 s; 41 s for the root) |
| re-build after commit | no-op, 7 s → the committed tree IS the built tree |
| `#print axioms Race.bound` | `[propext, Classical.choice, Quot.sound]` |
| same for `bound_stageB`, `heilbronnT_val`, `heilbronnK_val`, `eta_eq_heilbronnExponent` | identical three |
| `sorry` / `native_decide` / custom axioms | none (grep over `Submission/`, `Submission.lean`) |
| trusted statement | `git hash-object Submission/HeilbronnStatement.lean` = `bff8ba7bc805b881893123eb9b26e348b2bb6ee8` — byte-identical, unchanged |
| digit cap | denominator 237 digits < the 238-digit class the form already accepted for 1/10²³⁷ |

**η = 1/(100000·K) = 7.214428362266453e-237**, i.e. **7.2144× 1e-237**.
Strictly greater ⇒ clears the #178 run rule (equality bounces, strictness
does not).

### A defect the interrupted attempt left behind

`a15fd64` was committed but never built: `Assembly.lean`'s calc step
`C'^r·n^r = (C'·n)^r` was discharged by `hstep2`, whose statement runs the
other way (`hstep2.symm` was needed). No `Assembly.olean` had ever existed for
that tree, so nothing verified it. Found by reading the committed diff before
rebuilding, fixed in `1f36158`. Lesson: a commit is not a build.

## 4. Filing package

`PROVENANCE.md` carries the provenance, machine check and AI disclosure.
Every number a bare four-field verifier body needs (problem / repository
URL / commit SHA / bound) is in this report: bound = 1/(100000·K), SHA =
`6189ae9`. **Not yet filed on the board — filing is the next action
(README, "Next steps").**

## 5. RUNG-2 scope: what 2/(45435K+16) needs

Rung 2 is worth 4.4019× over rung 1 (**3.175714e-236**, = 31.757× the bar) and
lands exactly on the board's own OpenAI baseline row (3.18e-236) — a real
scientific statement: the race's baseline becomes machine-checked. The tree
already produces `α = 45435K+16` (our `Bridge/Cardinality.lean` proves the
SHARP upper bound `sampleCard ≤ √(cubeTauConst K)·r^(45435K+16)`), so the gap
is not new mathematics — it is three named slack steps in the frozen port:

1. **`OAI/…/ExponentScaling.lean::exponent_scaling`** — the elementary site.
   From `n ≤ r^(100000k)` and `r²/64 ≤ n²a` the argument supports
   `η = 2/(100000k)`; the proof drops a factor (`hrscale : r ≤ r²/64`) and
   claims only `1/(100000k)`. Local, ~10 lines, constant-bearing.
2. **The crude upper bound `n ≤ r^(100000k)`** (`SampleUpper.lean`, plus 28
   `100000` sites across 7 files) where the sharp `45435k+16` scaled bound is
   needed — that sharp bound exists on OUR side of the fence
   (`Bridge/Cardinality.lean:233`), not in the port.
3. **The statement layer itself**: `Main`, `ParameterSampling`,
   `ParameterConclusion`, `FinalScalingBridge`, `FinalSampling` are all stated
   at the frozen def `heilbronnExponent`, so η′ needs either a parallel
   instance at η′ or parameterizing those theorems over η plus side conditions
   (`0 < η`, `η ≤ 1/200000` — both hold at η′, trivially). The final ℚ literal
   is cheap now: `2/(45435K+16)` has a 236-digit denominator and
   `2/(45435K+16) ≥ 1/(100000K)` is symbolic (`200000K ≥ 45435K+16 ⇔ K ≥ 1`),
   so no new big-number work.

Cost class: **days, statement-layer refactor**, and it breaks the "OpenAI
modules import-rewritten only" provenance claim unless the sharp chain is
added as new bridge modules instead. Rung 1 avoided both costs by changing
only the constant.
