def calc_score(x: chr) -> int:
    if "a" <= x <= "z":
        return ord(x) - ord("a") + 1
    else:
        return ord(x) - ord("A") + 27


def solve() -> None:
    backpacks = open("input.txt").read().strip().split("\n")

    # Part 1
    tlt1: int = 0
    for backpack in backpacks:
        middle: int = len(backpack) // 2
        b1, b2 = backpack[:middle], backpack[middle:]

        common_char = next(iter(set(b1) & set(b2)))
        tlt1 += calc_score(common_char)

    print(f"Part 1: {tlt1}")

    # Part 2
    tlt2: int = 0
    for i in range(0, len(backpacks), 3):
        common_char = next(
            iter(set(backpacks[i]) & set(backpacks[i + 1]) & set(backpacks[i + 2]))
        )
        tlt2 += calc_score(common_char)

    print(f"Part 2: {tlt2}")


solve()
