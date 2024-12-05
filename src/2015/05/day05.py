import re
from timeit import timeit
from typing import List

from common.python.timing import Timing


class Solution:
    def __init__(self, data: List[str]) -> None:
        self.data: List[str] = data

    @classmethod
    def parse_input(cls) -> "Solution":
        """
        Parse the problem data input to be used.

        Returns:
            Solution:
                Class instance with the parsed input data.
        """
        with open("input.txt", "r") as file:
            values: List[str] = list(file.readlines())

        return cls(data=values)

    def part_01(self) -> None:
        """
        Solve Part 01 of the problem.

        Returns:
            None
        """
        tlt: int = 0

        for val in self.data:
            if re.search(r"([aeiou].*){3,}", val):
                if re.search(r"(.)\1", val):
                    if not re.search(r"ab|cd|pq|xy", val):
                        tlt += 1

        print(f"Part 01: {tlt}")

    def part_02(self) -> None:
        """
        Solve Part 02 of the problem.

        Returns:
            None
        """
        tlt: int = 0
        for val in self.data:
            if re.search(r"(..).*\1", val):
                if re.search(r"(.).\1", val):
                    tlt += 1

        print(f"Part 02: {tlt}")


if __name__ == "__main__":
    sol: Solution = Solution.parse_input()

    print(Timing(timeit(sol.part_01, number=1)).result(), "\n")
    print(Timing(timeit(sol.part_02, number=1)).result(), "\n")
