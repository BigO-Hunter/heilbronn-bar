"""Re-derive and cross-check every rung-1 number from the current files.

Run from ~/bigo-campaign/heilbronn-bar:  python3 verify_rung1.py
Exit 0 iff every assertion passes. Requires the Lean clone at ./repo.
"""
import math
import re
from decimal import Decimal, getcontext
from pathlib import Path

getcontext().prec = 40
FINAL_SHA = "6189ae976a538f309232e73ad147c351dc2410f2"

M = math.comb(163, 41)
T = math.comb(M, 3)
K = T * T + 1
DEN = str(100000 * K)

sub = Path("repo/Submission.lean").read_text()
kb = Path("repo/Submission/Bridge/KBound.lean").read_text()
draft = Path("POST_DRAFT.md").read_text()
comment = Path("POST_COMMENT.md").read_text()

doc_digits = "".join(
    r for r in re.findall(r"\d{30,}", sub) if len(r) < 200 and r != str(K)
)
comment_k = comment[comment.index("K = 1386"):comment.index("(232 digits")]

checks = {
    "M is 39 digits": len(str(M)) == 39,
    "T is 116 digits": len(str(T)) == 116,
    "K is 232 digits": len(str(K)) == 232,
    "denominator is 237 digits": len(DEN) == 237,
    "Lean statement carries den twice": sub.count(DEN) == 2,
    "Submission.lean docstring digits == den": doc_digits == DEN,
    "KBound M literal": str(M) in kb,
    "KBound T literal": str(T) in kb,
    "KBound K literal": str(K) in kb,
    "POST_DRAFT bound == 1/den": re.search(r"\*\*Bound:\*\*\s*(1/\d+)", draft).group(1) == "1/" + DEN,
    "POST_DRAFT SHA == final": FINAL_SHA in draft,
    "POST_COMMENT K digits (unwrapped) == K": re.sub(r"\D", "", comment_k) == str(K),
    "eta strictly > 1e-237": Decimal(1) / Decimal(100000 * K) > Decimal(10) ** -237,
}

for name, ok in checks.items():
    print(("PASS  " if ok else "FAIL  ") + name)
eta = Decimal(1) / Decimal(100000 * K)
print(f"\nK  = {K}")
print(f"eta= {eta}")
assert all(checks.values()), "VERIFICATION FAILED"
print("ALL PASS")
