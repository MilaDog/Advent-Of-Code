from collections import defaultdict
from timeit import timeit

from timing import Timing


class Solution:
    """Solutions to the problems."""

    def __init__(self, data: dict[tuple[int, int], str]) -> None:
        self.data: dict[tuple[int, int], str] = data

    @classmethod
    def parse_input(cls) -> "Solution":
        """Parse the problem data input to be used.

        Returns:
            Solution:
                Class instance with the parsed input data.
        """
        values: dict[tuple[int, int], str] = defaultdict()
        with open("input.txt", "r") as file:
            for x, r in enumerate(file.readlines()):
                for y, c in enumerate(r.strip()):
                    values[(x, y)] = c

        return cls(data=values)

    def part_01(self) -> None:
        """Solve Part 01 of the problem.

        Returns:
            None
        """
        tlt: int = 0

        # Extracting all the 'X's to start searching from
        for x, y in [k for k, v in self.data.items() if v == "X"]:
            # Horizontal looking
            if f"{self.data.get((x, y+1), 'y')}{self.data.get((x, y+2), 'y')}{self.data.get((x, y+3), 'y')}" == "MAS":
                tlt += 1

            if f"{self.data.get((x, y-1), 'y')}{self.data.get((x, y-2), 'y')}{self.data.get((x, y-3), 'y')}" == "MAS":
                tlt += 1

            # Vertical looking
            if f"{self.data.get((x+1, y), 'y')}{self.data.get((x+2, y), 'y')}{self.data.get((x+3, y), 'y')}" == "MAS":
                tlt += 1

            if f"{self.data.get((x-1, y), 'y')}{self.data.get((x-2, y), 'y')}{self.data.get((x-3, y), 'y')}" == "MAS":
                tlt += 1

            # Diagonal looking
            for dx, dy in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
                if (
                    f"{self.data.get((x+dx, y+dy), 'y')}{self.data.get((x+(dx*2), y+(dy*2)), 'y')
                }{self.data.get((x+(dx*3), y+(dy*3)), 'y')}"
                    == "MAS"
                ):
                    tlt += 1

        print(f"Part 01: {tlt}")

    def part_02(self) -> None:
        """Solve Part 02 of the problem.

        Returns:
            None
        """
        tlt: int = 0

        # Extracting all the 'X's to start searching from
        for x, y in [k for k, v in self.data.items() if v == "A"]:
            # Diagonal looking
            diag1: str = f"{self.data.get((x+1, y+1), 'y')}{self.data.get((x, y), 'y')}{self.data.get((x-1, y-1), 'y')}"
            diag2: str = (
                f"{self.data.get((x-1, y+1), 'y')}{self.data.get((x, y), 'y')}" f"{self.data.get((x+1, y-1), 'y')}"
            )

            if (diag1 == "MAS" or diag1[::-1] == "MAS") and (diag2 == "MAS" or diag2[::-1] == "MAS"):
                tlt += 1

        print(f"Part 02: {tlt}")


if __name__ == "__main__":
    sol: Solution = Solution.parse_input()

    print(Timing(timeit(sol.part_01, number=1)).result(), "\n")
    print(Timing(timeit(sol.part_02, number=1)).result(), "\n")
