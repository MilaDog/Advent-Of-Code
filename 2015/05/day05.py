from operator import truediv
import re
from itertools import count

with open("input.txt") as f:
    ps = [x.strip() for x in f.readlines()]


def part1():
    cnt = 0

    for val in ps:
        if re.search(r"([aeiou].*){3,}", val):
            if re.search(r"(.)\1", val):
                if not re.search(r"ab|cd|pq|xy", val):
                    cnt += 1
    return cnt


def part2():
    cnt = 0

    for val in ps:
        if re.search(r"(..).*\1", val):
            if re.search(r"(.).\1", val):
                cnt += 1
    return cnt


print("Part 1:", part1())
print("Part 2:", part2())
