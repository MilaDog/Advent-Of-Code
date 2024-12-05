import re
from collections import deque

TOWER, ACTIONS = open("input.txt").read().split('\n\n')
TOWER = TOWER.replace('[', '').replace(']', '').replace('    ', 'x').replace(' ', '')


def part1():
    towers = [deque() for _ in range(9)]
    for t in TOWER.splitlines()[:-1][::-1]:
        for i, p in enumerate(list(t)):
            if p != 'x':
                towers[i].append(p)

    for action in ACTIONS.splitlines():
        amt, f, t = map(int, re.findall(r"\d+", action))
        for _ in range(amt):
            got = towers[f - 1].pop()
            towers[t - 1].append(got)

    print("Part 1:", "".join(x.pop() for x in towers))


def part2():
    towers = [deque() for _ in range(9)]
    for t in TOWER.splitlines()[:-1][::-1]:
        for i, p in enumerate(list(t)):
            if p != 'x':
                towers[i].append(p)

    for action in ACTIONS.splitlines():
        amt, f, t = map(int, re.findall(r"\d+", action))
        got = []
        for _ in range(amt):
            got.append(towers[f - 1].pop())

        for v in got[::-1]:
            towers[t - 1].append(v)

    print("Part 2:", "".join(x.pop() for x in towers))


part1()
part2()
