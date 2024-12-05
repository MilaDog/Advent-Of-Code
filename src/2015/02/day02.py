from timeit import timeit
from typing import List

from common.python.timing import Timing


class Solution:
    def __init__(self, data: List[List[int]]) -> None:
        self.data: List[List[int]] = data

    @classmethod
    def parse_input(cls) -> "Solution":
        """
        Parse the problem data input to be used.

        Returns:
            Solution:
                Class instance with the parsed input data.
        """
        values: List[List[int]] = []
        with open("input.txt", "r") as file:
            for line in file.readlines():
                dims: List[int] = list(map(int, line.strip().split("x")))
                values.append(dims)

        return cls(data=values)

    def part_01(self) -> None:
        """
        Solve Part 01 of the problem.

        Returns:
            None
        """
        tlt: int = 0
        for l, w, h in self.data:
            # Formula: 2*l*w + 2*w*h + 2*h*l
            min_value: int = min(l * w, w * h, h * l)
            tlt += (2 * l * w) + (2 * w * h) + (2 * h * l) + min_value

        print(f"Part 01: {tlt}")

    def part_02(self) -> None:
        """
        Solve Part 02 of the problem.

        Returns:
            None
        """
        tlt: int = 0

        m1: int
        m2: int
        for l, w, h in self.data:
            m1, m2 = sorted([l, w, h])[:2]
            tlt += (l * w * h) + (2 * m1) + (2 * m2)

        print(f"Part 02: {tlt}")


if __name__ == "__main__":
    sol: Solution = Solution.parse_input()

    print(Timing(timeit(sol.part_01, number=1)).result(), "\n")
    print(Timing(timeit(sol.part_02, number=1)).result(), "\n")
