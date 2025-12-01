from collections import deque
from math import prod

DR = [-1, 0, 1, 0]
DC = [0, 1, 0, -1]


def get_input():
    with open("input.txt", "r") as f:
        data = [list(map(int, line.strip())) for line in f.readlines()]
        return data


def get_neighbours(data, i, j):
    n = (data[j - 1][i], j - 1) if j > 0 else None
    e = (data[j][i + 1], j) if i < len(data[0]) - 1 else None
    s = (data[j + 1][i], j + 1) if j < len(data) - 1 else None
    w = (data[j][i - 1], j) if i > 0 else None
    return [n, e, s, w]


def is_valid(i, neighbours):
    valid = all(i < n[0] for n in neighbours if n is not None)
    return valid


def part1(data):
    low_points = []

    for j in range(len(data)):
        for i in range(len(data[0])):
            neighbours = get_neighbours(data, i, j)
            if is_valid(data[j][i], neighbours):
                low_points.append(data[j][i])

    return sum([x + 1 for x in low_points])


def part2(data):
    sizes = []
    SEEN = set()

    for j in range(len(data)):
        for i in range(len(data[0])):
            if (j, i) not in SEEN and data[j][i] != 9:
                size = 0
                Q = deque()
                Q.append((j, i))

                while Q:
                    (j, i) = Q.popleft()
                    if (j, i) in SEEN:
                        continue

                    SEEN.add((j, i))
                    size += 1
                    for d in range(4):
                        jj = j + DR[d]
                        ii = i + DC[d]
                        if 0 <= ii < len(data[0]) and 0 <= jj < len(data) and data[jj][ii] != 9:
                            Q.append((jj, ii))

                sizes.append(size)
    sizes.sort(reverse=True)
    return prod(sizes[:3])


print(f"Part 1: {part1(get_input())}")
print(f"Part 2: {part2(get_input())}")
