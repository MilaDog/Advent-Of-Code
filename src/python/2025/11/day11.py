from functools import cache
from timeit import timeit

from src.timing import Timing


class Solution:
    """Solutions to the problems."""

    def __init__(self, data: dict[str, list[str]]) -> None:
        self.data: dict[str, list[str]] = data

    @classmethod
    def parse_input(cls) -> "Solution":
        """Parse the problem data input to be used.

        Returns:
            Solution:
                Class instance with the parsed input data.
        """
        values: dict[str, list[str]] = dict()
        with open("./inputs/2025/11/input.txt", "r") as file:
            for line in file.readlines():
                x, y = line.strip().split(":")
                values[x.strip()] = [z.strip() for z in y.strip().split(" ")]

        return cls(data=values)

    @cache
    def part_01(self, start: str) -> int:
        """Solve Part 01 of the problem."""
        if start == "out":
            return 1
        return sum(self.part_01(start=x) for x in self.data[start])

    @cache
    def part_02(self, start: str, seen_dac: bool, seen_fft: bool) -> int:
        """Solve Part 02 of the problem."""
        if start == "out":
            return seen_dac and seen_fft
        return sum(
            self.part_02(start=value, seen_dac=(seen_dac or value == "dac"), seen_fft=(seen_fft or value == "fft"))
            for value in self.data[start]
        )

    def solve(self) -> None:
        """Solve Part 01 and 02 of the problem."""
        print(f"Part 01: {self.part_01(start='you')}")
        print(f"Part 02: {self.part_02(start='svr', seen_dac=False, seen_fft=False)}")


if __name__ == "__main__":
    sol: Solution = Solution.parse_input()

    print(Timing(timeit(sol.solve, number=1)).result(), "\n")
