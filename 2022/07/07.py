from collections import defaultdict


def solve():
    actions = open("input.txt").read().strip().splitlines()

    FT = defaultdict(int)
    cDir = []

    for x in actions:
        match x.strip().replace("$", "").split():
            case ["cd", "/"]:
                cDir.clear()
                cDir.append("/")

            case ["cd", ".."]:
                cDir.pop()

            case ["cd", folder]:
                cDir.append(folder)

            case [sz, file] if sz.isdigit():
                for i in range(1, len(cDir) + 1):
                    FT["/".join(cDir[:i])] += int(sz)

    # Part 2
    needed_free_amount = FT["/"] - 40000000

    print(f"Part 1: {sum([v for v in FT.values() if v <= 100000])}")
    print(f"Part 2: {min([v for v in FT.values() if v >= needed_free_amount])}")


solve()
