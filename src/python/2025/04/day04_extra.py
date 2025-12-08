from copy import deepcopy
from timeit import timeit

from src.timing import Timing


class Solution:
    """Solutions to the problems."""

    def __init__(self, data: set[complex]) -> None:
        self.data: set[complex] = data
        self.offsets: set[complex] = {(-1 - 1j), (-1 + 0j), (-1 + 1j), -1j, 1j, (1 - 1j), (1 + 0j), (1 + 1j)}

    @classmethod
    def parse_input(cls) -> "Solution":
        """Parse the problem data input to be used.

        Returns:
            Solution:
                Class instance with the parsed input data.
        """
        values: set[complex] = set()

        with open("./inputs/2025/04/input.txt", "r") as file:
            for r, line in enumerate(file.readlines()):
                for c, paper in enumerate(line.strip()):
                    if paper == "@":
                        values.add(complex(r, c))

        return cls(data=values)

    def solve(self) -> None:
        """Solve Part 01 and 02 of the problem, making use of complex numbers to store the positions of all the
        papers in the area.

        Returns:
            None
        """
        papers: set[complex] = deepcopy(self.data)

        tlt1: int = 0
        tlt2: int = 0

        solving_first: bool = True

        while True:
            changed: bool = False
            for paper in list(papers):
                cnt: int = sum((paper + offset) in papers for offset in self.offsets)

                if cnt < 4:
                    tlt1 += 1

                    changed = True
                    if not solving_first:
                        tlt2 += 1
                        papers.remove(paper)

            if solving_first:
                solving_first = False
                print(f"Part 01: {tlt1}")

            if not changed:
                break

        print(f"Part 02: {tlt2}")


if __name__ == "__main__":
    sol: Solution = Solution.parse_input()

    # Original
    print(Timing(timeit(sol.solve, number=1)).result(), "\n")
