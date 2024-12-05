import re
from timeit import timeit

import numpy as np

from common.python.timing import Timing


class Solution:
    def __init__(self, data: list[str]) -> None:
        self.data: list[str] = data
        self.grid = np.zeros(shape=(6, 50), dtype=bool)

    @classmethod
    def parse_input(cls) -> "Solution":
        """
        Parse the problem data input to be used.

        Returns:
            Solution:
                Class instance with the parsed input data.
        """
        with open("input.txt", "r") as file:
            values: list[str] = [line.strip() for line in file.readlines()]

        return cls(data=values)

    def part_01(self) -> None:
        """
        Solve Part 01 of the problem.

        Returns:
            None
        """
        for line in self.data:
            if "rect" in line:
                # Light up area
                w, h = map(int, re.findall(r"(\d+)", line))
                self.grid[:h, :w] = True

            elif "rotate" in line:
                if "row" in line:
                    # Shift row
                    r, a = map(int, re.findall(r"(\d+)", line))
                    self.grid[r] = np.roll(self.grid[r], a)

                else:
                    # Column shift
                    c, a = map(int, re.findall(r"(\d+)", line))
                    self.grid[:, c] = np.roll(self.grid[:, c], a)

        tlt: int = np.sum(self.grid)
        print(f"Part 01: {tlt}")

    def part_02(self) -> None:
        """
        Solve Part 02 of the problem.

        Returns:
            None
        """
        print("Part 02:\n")
        res: str = "\n".join(
            "".join("\u2593" if val else " " for val in row) for row in self.grid
        )
        print(res)


if __name__ == "__main__":
    sol: Solution = Solution.parse_input()

    print(Timing(timeit(sol.part_01, number=1)).result(), "\n")
    print(Timing(timeit(sol.part_02, number=1)).result(), "\n")
