import re
from itertools import combinations
from timeit import timeit

from common.python.timing import Timing


class Solution:
    def __init__(self, data: list[list[int]]) -> None:
        self.data: list[list[int]] = data

    @classmethod
    def parse_input(cls) -> "Solution":
        """
        Parse the problem data input to be used.

        Returns:
            Solution:
                Class instance with the parsed input data.
        """
        with open("input.txt", "r") as file:
            values: list[list[int]] = [
                list(map(int, re.findall(r"(\d+)", line))) for line in file.readlines()
            ]

        return cls(data=values)

    def part_01(self) -> None:
        """
        Solve Part 01 of the problem.

        Returns:
            None
        """
        tlt: int = sum(max(line) - min(line) for line in self.data)
        print(f"Part 01: {tlt}")

    def part_02(self) -> None:
        """
        Solve Part 02 of the problem.

        Returns:
            None
        """
        tlt: int = 0

        for line in self.data:
            for comb in combinations(line, 2):
                x, y = max(comb), min(comb)
                if x % y == 0:
                    tlt += x // y
                    break

        print(f"Part 02: {tlt}")


if __name__ == "__main__":
    sol: Solution = Solution.parse_input()

    print(Timing(timeit(sol.part_01, number=1)).result(), "\n")
    print(Timing(timeit(sol.part_02, number=1)).result(), "\n")
