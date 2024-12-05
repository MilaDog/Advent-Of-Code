def solve() -> None:
    lines = open("input.txt").read().splitlines()

    tlt1: int = 0
    tlt2: int = 0
    for line in lines:
        a1, a2, b1, b2 = map(int, line.strip().replace(",", "-").split("-"))  # why not?

        # Part 1
        if a1 <= b1 <= b2 <= a2 or b1 <= a1 <= a2 <= b2:
            tlt1 += 1

        # Part 2
        if a1 <= b1 <= a2 or a1 <= b2 <= a2 or b1 <= a1 <= b2 or b1 <= a2 <= b2:
            tlt2 += 1

    print(f"Part 1: {tlt1}")
    print(f"Part 2: {tlt2}")


solve()
