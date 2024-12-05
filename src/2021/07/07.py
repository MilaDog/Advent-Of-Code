def get_input():
    with open("input.txt") as f:
        pos = list(map(int, f.read().strip().split(",")))
        return pos


def cost(a, b):
    n = abs(a - b)
    return n * (n + 1) // 2


def part1(data):
    data.sort()
    med = data[len(data) // 2]
    fnl = [abs(x - med) for x in data]

    return sum(fnl)


def part2(data):
    fnl = []
    for pos in range(min(data), max(data) + 1):
        fnl.append(sum(cost(x, pos) for x in data))
    return min(fnl)


print(f"Part 1: {part1(get_input())}")
print(f"Part 2: {part2(get_input())}")
