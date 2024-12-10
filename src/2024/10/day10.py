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
                    pos: complex = x + 1j * y
                    values[pos] = int(col)

                    if col == "0":
                        zeroes.add(pos)

        return cls(grid=values, zeroes=zeroes)

    def solve(self) -> None:
        """
        Solves both parts of the problem.

        Returns:
            None
        """
        p1: int = 0
        p2: int = 0

        # Simple DFS
        for starting_point in self.zeroes:
            q: deque[complex] = deque([starting_point])
            targets_met: set[complex] = set()
            unique_paths: int = 0

            while q:
                curr = q.popleft()

                if self.grid[curr] == 9:
                    unique_paths += 1
                    targets_met.add(curr)
                    continue

                for change in (1, -1, -1j, 1j):
                    if self.grid.get(curr + change, -1) == self.grid[curr] + 1:
                        q.appendleft(curr + change)

            p1 += len(targets_met)
            p2 += unique_paths

        print(f"Part 01: {p1}")
        print(f"Part 02: {p2}")


if __name__ == "__main__":
    sol: Solution = Solution.parse_input()

    print(Timing(timeit(sol.solve, number=1)).result(), "\n")
