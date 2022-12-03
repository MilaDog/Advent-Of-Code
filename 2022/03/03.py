from timeit import timeit


def calc_score(x: chr) -> int:
    if 'a' <= x <= 'z':
        return ord(x) - ord('a') + 1
    else:
        return ord(x) - ord('A') + 27


def solve():
    backpacks = open("input.txt").readlines()

    tlt1: int = 0
    tlt2: int = 0
    for backpack in backpacks:
        backpack.strip()
        b1, b2 = backpack[:len(backpack) // 2], backpack[len(backpack) // 2:]

        for x in b1:
            if x in b2:
                tlt1 += calc_score(x)
                break

    for i in range(0, len(backpacks), 3):
        for x in backpacks[i].strip():
            if x in backpacks[i + 1] and x in backpacks[i + 2]:
                tlt2 += calc_score(x)
                break

    print(f"Part 1: {tlt1}")
    print(f"Part 2: {tlt2}")


solve()
