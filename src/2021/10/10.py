from collections import deque

DATA = [x.strip() for x in open("input.txt", "r").readlines()]

chunks = {")": "(", "]": "[", "}": "{", ">": "<"}
s1 = {")": 3, "]": 57, "}": 1197, ">": 25137}
s2 = {"(": 1, "[": 2, "{": 3, "<": 4}
SCORES = []


def solution():
    tlt = 0
    for line in DATA:
        corrupt = False
        S = deque()
        for c in line:
            if c in chunks.values():
                S.append(c)
            elif not S or S.pop() != chunks[c]:
                tlt += s1[c]
                corrupt = True

        if not corrupt:
            score = 0
            for c in reversed(S):
                score = 5 * score + s2[c]
            SCORES.append(score)
    SCORES.sort()
    return tlt, SCORES[len(SCORES) // 2]


p1, p2 = solution()
print(f"Part 1: {p1}")
print(f"Part 2: {p2}")
