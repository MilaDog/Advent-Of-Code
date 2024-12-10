from collections import defaultdict, deque
from timeit import timeit

from src.common.python.timing import Timing


class Solution:
    def __init__(self, grid: dict[complex, int], zeroes: set[complex]) -> None:
        self.grid: dict[complex, int] = grid
        self.zeroes: set[complex] = zeroes

    @classmethod
    def parse_input(cls) -> "Solution":
        """
        Parse the problem data input to be used.

        Returns:
            Solution:
                Class instance with the parsed input data.
        """
        with open("input.txt", "r") as file:
            values: dict[complex, int] = defaultdict(int)
            zeroes: set[complex] = set()

            for x, row in enumerate(file.readlines()):
                for y, col in enumerate(row.strip()):
                    values[x + 1j * y] = int(col)

                    if col == "0":
                        zeroes.add(x + 1j * y)

        return cls(grid=values, zeroes=zeroes)

    def part_01(self) -> None:
        """
        Solve Part 01 of the problem.

        Returns:
            None
        """
        tlt: int = 0

        # Simple DFS
        for starting_point in self.zeroes:
            q: deque[complex] = deque([starting_point])
            targets_met: set[complex] = set()

            while q:
                curr = q.popleft()

                if self.grid[curr] == 9:
                    targets_met.add(curr)
                    continue

                for change in (1, -1, -1j, 1j):
                    if n := self.grid.get(curr + change):
                        if n == self.grid[curr] + 1:
                            q.appendleft(curr + change)

            tlt += len(targets_met)

        print(f"Part 01: {tlt}")

    def part_02(self) -> None:
        """
        Solve Part 02 of the problem.

        Returns:
            None
        """
        tlt: int = 0

        # Simple DFS
        for starting_point in self.zeroes:
            q: deque[complex] = deque([starting_point])
            targets_met: int = 0

            while q:
                curr = q.popleft()

                if self.grid[curr] == 9:
                    targets_met += 1
                    continue

                for change in (1, -1, -1j, 1j):
                    if n := self.grid.get(curr + change):
                        if n == self.grid[curr] + 1:
                            q.appendleft(curr + change)

            tlt += targets_met

        print(f"Part 02: {tlt}")


if __name__ == "__main__":
    sol: Solution = Solution.parse_input()

    print(Timing(timeit(sol.part_01, number=1)).result(), "\n")
    print(Timing(timeit(sol.part_02, number=1)).result(), "\n")
