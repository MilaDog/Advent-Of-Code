from __future__ import annotations

import re
from collections import Counter
from timeit import timeit

from src.timing import Timing


class Solution:
    """Solve the problems."""

    def __init__(self, data: tuple[list[int], list[int]]) -> None:
        self.data: tuple[list[int], list[int]] = data

    @classmethod
    def parse_input(cls) -> "Solution":
        """Parse the problem data input to be used.

        Returns:
            Solution:
                Class instance with the parsed input data.
        """
        with open("./inputs/2024/01/input.txt", "r") as file:
            values_left: list[int] = []
            values_right: list[int] = []

            for line in file.readlines():
                vals: list[str] = re.findall(r"\d+", line)
                values_left.append(int(vals[0]))
                values_right.append(int(vals[1]))

        return cls(data=(sorted(values_left), sorted(values_right)))

    def part_01(self) -> None:
        """Solve Part 01 of the problem.

        Returns:
            None
        """
        tlt: int = 0

        for left, right in zip(*self.data):
            tlt += abs(left - right)

        print(f"Part 01: {tlt}")

    def part_02(self) -> None:
        """Solve Part 02 of the problem.

        Returns:
            None
        """
        tlt: int = 0

        count: Counter[int] = Counter(self.data[1])
        for val in self.data[0]:
            tlt += val * count.get(val, 0)

        print(f"Part 02: {tlt}")


if __name__ == "__main__":
    sol: Solution = Solution.parse_input()

    print(Timing(timeit(sol.part_01, number=1)).result(), "\n")
    print(Timing(timeit(sol.part_02, number=1)).result(), "\n")
