import re
from collections import Counter

PT, rules = open("input.txt").read().split("\n\n")
R = dict(re.findall(r"(\w+) -> (\w)\b", rules))
P = Counter(["".join(p) for p in zip(PT[:-1], PT[1:])])

for i in range(40):
    C = Counter()
    for p in P:
        C[p[0] + R[p]] += P[p]
        C[R[p] + p[1]] += P[p]
    P = C

    if i in [9, 39]:
        FNL = Counter()
        for p in P:
            FNL[p[0]] += P[p]
        FNL[PT[-1]] += 1
        print(max(FNL.values()) - min(FNL.values()))
