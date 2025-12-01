# Advent of Code, Day 02 2023
# MilaDog

from math import prod
from re import findall
from timeit import timeit

DATA_CUBES = {"red": 12, "green": 13, "blue": 14}


def solve(lines: list[str]) -> (int, int):
    """Solve part 1. Returns sum of Game numbers that are valid"""
    valid_games: list[int] = [0]
    valid_games_prod: list[int] = [0]

    for id, data in enumerate(lines, 1):
        cubes_amt = {"red": 0, "blue": 0, "green": 0}
        cubes_amt_part2 = {"red": 0, "blue": 0, "green": 0}
        valid: bool = True

        rounds = findall(r"(?: (\d+) (green|red|blue))", data)

        for amt, colour in rounds:
            cubes_amt[colour] = int(amt)

            # Part 2
            if cubes_amt.get(colour, 0) > cubes_amt_part2.get(colour, 0):
                cubes_amt_part2[colour] = int(amt)

            if any(
                True if cubes_amt.get(colour, 0) > DATA_CUBES.get(colour, 0) else False for colour in DATA_CUBES.keys()
            ):
                valid = False

        # Part 1
        if valid:
            valid_games.append(id)

        # Part 2
        valid_games_prod.append(prod(cubes_amt_part2.values()))

    return (sum(valid_games), sum(valid_games_prod))


def main() -> None:
    """Main function"""
    with open("input.txt") as file:
        lines: list[str] = [x.strip() for x in file.readlines()]

    part1, part2 = solve(lines)
    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")


if __name__ == "__main__":
    print(timeit(main, number=1))
