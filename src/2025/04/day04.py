import os
from pathlib import Path
from timeit import timeit

from src.timing import Timing


class Solution:
    """Solutions to the problems."""

    def __init__(self, data: list[list[str]]) -> None:
        self.data: list[list[str]] = data
        self.rows: int = len(self.data)
        self.cols: int = len(self.data[0])

    @classmethod
    def parse_input(cls) -> "Solution":
        """Parse the problem data input to be used.

        Returns:
            Solution:
                Class instance with the parsed input data.
        """
        with open(os.path.join(Path(__file__).resolve().parent, "input.txt"), "r") as file:
            values: list[list[str]] = [list(line.strip()) for line in file.readlines()]

        return cls(data=values)

    def original(self) -> None:
        """Solve Part 01 and 02 of the problem.

        Returns:
            None
        """
        tlt1: int = 0
        tlt2: int = 0

        solving_first: bool = True
        while True:
            changed: bool = False
            for r in range(self.rows):
                for c in range(self.cols):
                    cnt: int = 0

                    for dr in [-1, 0, 1]:
                        for dc in [-1, 0, 1]:
                            if 0 <= r + dr < self.rows and 0 <= c + dc < self.cols:
                                cnt += self.data[r + dr][c + dc] == "@"

                    if cnt < 5 and self.data[r][c] == "@":
                        tlt1 += 1

                        changed = True
                        if not solving_first:
                            tlt2 += 1
                            self.data[r][c] = "."

            if solving_first:
                print(f"Part 01: {tlt1}")
                solving_first = False

            if not changed:
                break

        print(f"Part 02: {tlt2}")


if __name__ == "__main__":
    sol: Solution = Solution.parse_input()

    # Original
    print(Timing(timeit(sol.original, number=1)).result(), "\n")
