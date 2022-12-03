from collections import defaultdict, Counter


def get_input():
    with open("input.txt", "r") as f:
        data = Counter([int(x) for x in f.read().strip().split(",")])
        return data


def solve(data, days):
    for _ in range(days):
        l = defaultdict(int)
        for x, amt in data.items():
            match x:
                case 0:
                    l[6] += amt
                    l[8] += amt
                case _:
                    l[x - 1] += amt
        data = l
    return sum(data.values())


def part1():
    return solve(get_input(), 80)


def part2():
    return solve(get_input(), 256)


print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
