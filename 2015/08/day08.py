# Advent of Code, 2015 Day 07
# MilaDog

from ast import literal_eval
from timeit import timeit


def solve(lines: list[str]) -> None:
    """Calculate the difference between the number of characters between the raw string and normal string.
    Return sum of all the differences"""

    res: list[int] = []
    tlt: int = 0

    for line in lines:
        line = line.strip()
        lngth_normal = len(literal_eval(line))
        lngth_raw = len(line)

        # Part 1
        res.append(lngth_raw - lngth_normal)

        # Part 2
        tlt += line.count("\\") + line.count('"') + 2

    print(f"Part 1: {sum(res)}")
    print(f"Part 2: {tlt}")


def main() -> None:
    with open("input.txt", "r") as file:
        lines: list[str] = file.readlines()

    solve(lines)


if __name__ == "__main__":
    print(timeit(main, number=1))
