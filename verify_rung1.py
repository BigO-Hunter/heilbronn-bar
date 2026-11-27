"""Re-derive and cross-check every rung-1 number from the pinned proof.

Run from anywhere:  python3 verify_rung1.py
Exit 0 iff every assertion passes. Requires the pinned Lean proof cloned at
./repo next to this script (see README "Reproduce"; CI fetches it automatically).
"""
import math
import re
from decimal import Decimal, getcontext
from pathlib import Path

getcontext().prec = 40
ROOT = Path(__file__).resolve().parent
FINAL_SHA = "6189ae976a538f309232e73ad147c351dc2410f2"

M = math.comb(163, 41)
T = math.comb(M, 3)
K = T * T + 1
DEN = str(100000 * K)

sub = (ROOT / "repo/Submission.lean").read_text()
kb = (ROOT / "repo/Submission/Bridge/KBound.lean").read_text()
report = (ROOT / "RUNG1_REPORT.md").read_text()
provenance = (ROOT / "PROVENANCE.md").read_text()

doc_digits = "".join(
    r for r in re.findall(r"\d{30,}", sub) if len(r) < 200 and r != str(K)
)
comment_k = provenance[provenance.index("K = 1386"):provenance.index("(232 digits")]

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
    "RUNG1_REPORT carries final SHA": FINAL_SHA in report,
    "PROVENANCE K digits (unwrapped) == K": re.sub(r"\D", "", comment_k) == str(K),
    "eta strictly > 1e-237": Decimal(1) / Decimal(100000 * K) > Decimal(10) ** -237,
}

for name, ok in checks.items():
    print(("PASS  " if ok else "FAIL  ") + name)
eta = Decimal(1) / Decimal(100000 * K)
print(f"\nK  = {K}")
print(f"eta= {eta}")
assert all(checks.values()), "VERIFICATION FAILED"
print("ALL PASS")
