import re
from collections import defaultdict


def get_input():
    with open("input.txt") as f:
        data = [list(map(int, re.findall(r"\d+", line))) for line in f]
        return data


def sign(n):
    return (1 if n > 0 else -1) if n else 0


def part1(data):
    vlines = defaultdict(int)

    for line in data:
        x1, x2 = line[0], line[2]
        y1, y2 = line[1], line[-1]

        if (x1 == x2) or (y1 == y2):
            for x in range(min(x1, x2), max(x1, x2) + 1):
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    vlines[(x, y)] += 1

    return len([x for x in vlines.values() if x > 1])


def part2(data):
    dlines = defaultdict(int)

    for x1, y1, x2, y2 in data:
        dx, dy = sign(x2 - x1), sign(y2 - y1)
        x, y = x1, y1

        while x != x2 or y != y2:
            dlines[(x, y)] += 1
            x += dx
            y += dy
        dlines[(x2, y2)] += 1

    return len([x for x in dlines.values() if x > 1])


print(f"Part 1: {part1(get_input())}")
print(f"Part 2: {part2(get_input())}")
