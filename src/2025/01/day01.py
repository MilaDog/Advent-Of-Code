import os
from pathlib import Path
from timeit import timeit

from src.timing import Timing


class Solution:
    """Solutions to the problems."""

    def __init__(self, data: list[tuple[str, int]]) -> None:
        self.data: list[tuple[str, int]] = data

    @classmethod
    def parse_input(cls) -> "Solution":
        """Parse the problem data input to be used.

        Returns:
            Solution:
                Class instance with the parsed input data.
        """
        with open(os.path.join(Path(__file__).resolve().parent, "input.txt"), "r") as file:
            values: list[tuple[str, int]] = [(line[0], int(line[1:])) for line in file.readlines()]

        return cls(data=values)

    def solve(self) -> None:
        """Solve Part 01 and 02 of the problem.

        Returns:
            None
        """
        tlt1: int = 0
        tlt2: int = 0

        pointing: int = 50

        for action, amount in self.data:
            for _ in range(amount):
                if action == "L":
                    pointing = (pointing + 99) % 100
                else:
                    pointing = (pointing + 1) % 100

                if pointing == 0:
                    tlt2 += 1

            if pointing == 0:
                tlt1 += 1

        print(f"Part 01: {tlt1}")
        print(f"Part 02: {tlt2}")


if __name__ == "__main__":
    sol: Solution = Solution.parse_input()

    print(Timing(timeit(sol.solve, number=1)).result(), "\n")
