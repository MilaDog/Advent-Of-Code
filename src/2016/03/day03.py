import re
from copy import deepcopy
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

    def is_valid_triangle(self, triangle: list[int]) -> bool:
        """
        Check whether the triangle is valid or not using the triangle inequality formula.

        Args:
            triangle (list[int]):
                Sides of the triangle.

        Returns:
            bool:
                If the given triangle is valid or not.

        """
        a, b, c = sorted(triangle)
        return a + b > c

    def part_01(self) -> None:
        """
        Solve Part 01 of the problem.

        Returns:
            None
        """
        tlt: int = 0

        for triangle in deepcopy(self.data):
            tlt += self.is_valid_triangle(triangle)

        print(f"Part 01: {tlt}")

    def part_02(self) -> None:
        """
        Solve Part 02 of the problem.

        Returns:
            None
        """
        tlt: int = 0

        for y in range(len(self.data[0])):
            for x in range(0, len(self.data), 3):
                tlt += self.is_valid_triangle(
                    [self.data[x][y], self.data[x + 1][y], self.data[x + 2][y]]
                )

        print(f"Part 02: {tlt}")


if __name__ == "__main__":
    sol: Solution = Solution.parse_input()

    print(Timing(timeit(sol.part_01, number=1)).result(), "\n")
    print(Timing(timeit(sol.part_02, number=1)).result(), "\n")
