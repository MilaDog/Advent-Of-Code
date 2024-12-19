from functools import cache
from timeit import timeit

from src.common.python.timing import Timing


class Solution:
    """Solutions to the problems."""

    def __init__(self, patterns: list[str], towels: list[str]) -> None:
        self.patterns: list[str] = patterns
        self.towels: list[str] = towels

    @classmethod
    def parse_input(cls) -> "Solution":
        """Parse the problem data input to be used.

        Returns:
            Solution:
                Class instance with the parsed input data.
        """
        with open("input.txt", "r") as file:
            p1, p2 = file.read().strip().split("\n\n")

            patterns: list[str] = [w.strip() for w in p1.strip().split(", ")]
            towels: list[str] = [t.strip() for t in p2.strip().splitlines()]

        return cls(patterns=patterns, towels=towels)

    @cache
    def can_make(self, target: str):
        """Recursive function that checks if the given towel, `target`, can be made with the given towel patterns.
        Returns the amount of different ways that the towel can be created with the patterns.

        Args:
            target (str):
                Target towel to create.

        Returns:
            int:
                Number of ways to create the towel.
        """
        if not target:
            return 1

        count: int = 0
        for pattern in self.patterns:
            if target.startswith(pattern):
                count += self.can_make(target[len(pattern) :])

        return count

    def solve(self) -> None:
        """Solve Part 01 and Part 02 of the problem.

        Returns:
            None
        """
        can_make_towels: list[int] = [self.can_make(target=towel) for towel in self.towels]

        tlt1: int = sum(map(bool, can_make_towels))
        print(f"Part 01: {tlt1}")

        tlt2: int = sum(can_make_towels)
        print(f"Part 01: {tlt2}")


if __name__ == "__main__":
    sol: Solution = Solution.parse_input()

    print(Timing(timeit(sol.solve, number=1)).result(), "\n")
