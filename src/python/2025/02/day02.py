import re
from timeit import timeit

from src.timing import Timing


class Solution:
    """Solutions to the problems."""

    def __init__(self, data: list[tuple[int, int]]) -> None:
        self.data: list[tuple[int, int]] = data

    @classmethod
    def parse_input(cls) -> "Solution":
        """Parse the problem data input to be used.

        Returns:
            Solution:
                Class instance with the parsed input data.
        """
        with open("./inputs/2025/02/input.txt", "r") as file:
            values: list[tuple[int, int]] = []

            for line in file.read().strip().split(","):
                a, b = line.strip().split("-")
                values.append((int(a), int(b)))

        return cls(data=values)

    def solve(self) -> None:
        """Solve Part 01 and 02 of the problem.

        Returns:
            None
        """
        tlt1: int = 0
        tlt2: int = 0

        for a, b in self.data:
            for idd in range(a, b + 1):
                if re.search(r"^(\d+)\1$", str(idd)) is not None:
                    tlt1 += idd

                if re.search(r"^(\d+)\1+$", str(idd)) is not None:
                    tlt2 += idd

        print(f"Part 01: {tlt1}")
        print(f"Part 02: {tlt2}")


if __name__ == "__main__":
    sol: Solution = Solution.parse_input()

    print(Timing(timeit(sol.solve, number=1)).result(), "\n")
