def solve():
    elves = open("input.txt").read().strip().split("\n\n")

    # Total calories per Elf
    tlt: list[int] = list()
    for elf in elves:
        tlt.append(sum(list(map(int, elf.split("\n")))))

    print(f"Part 1: {max(tlt)}")
    print(f"Part 2: {sum(sorted(tlt)[-3:])}")


solve()
