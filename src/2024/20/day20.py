from collections import defaultdict, deque
from timeit import timeit

from timing import Timing


class Solution:
    """Solutions to the problems."""

    def __init__(self, grid: dict[complex, str]) -> None:
        self.grid: dict[complex, str] = grid
        self.directions: list[complex] = [1, -1, 1j, -1j]

    @classmethod
    def parse_input(cls) -> "Solution":
        """Parse the problem data input to be used.

        Returns:
            Solution:
                Class instance with the parsed input data.
        """
        with open("input.txt", "r") as file:
            grid: dict[complex, str] = defaultdict(str)

            for x, row in enumerate(file.readlines()):
                for y, col in enumerate(row.strip()):
                    grid[x + 1j * y] = col

        return cls(grid=grid)

    def solve(self) -> None:
        """Solve Part 01 and Part 02 of the problem.

        Returns:
            None
        """
        start: complex = next(k for k, v in self.grid.items() if v == "S")
        end: complex = next(k for k, v in self.grid.items() if v == "E")

        # Simple DFS to start off
        q: deque[tuple[complex, int]] = deque([(start, 0)])
        visited: dict[complex, int] = {start: 0}

        # Getting the path from START to END, with the score of following that path
        while q:
            position, score = q.popleft()

            if position == end:
                continue

            neighbours: dict[complex, int] = {
                new_position: score + 1
                for offset in self.directions
                if self.grid[new_position := position + offset] != "#" and new_position not in visited
            }
            q.extendleft(neighbours.items())
            visited |= neighbours

        tlt1: int = 0
        tlt2: int = 0

        # For each position, determine the time saved when applying a cheat.
        # Go from the current position and cheat to every other position, excluding itself.
        # Calculate the distance and if within cheat range AND score is above 100,
        # count it.
        for i, (position_1, score_1) in enumerate(visited.items()):
            for position_2, score_2 in list(visited.items())[i + 1 :]:
                distance_change: complex = position_2 - position_1
                dist: int = int(abs(distance_change.real)) + int(abs(distance_change.imag))

                if dist <= 20 and score_2 - score_1 - dist >= 100:
                    tlt2 += 1
                    tlt1 += dist == 2

        print(f"Part 01: {tlt1}")
        print(f"Part 02: {tlt2}")


if __name__ == "__main__":
    sol: Solution = Solution.parse_input()

    print(Timing(timeit(sol.solve, number=1)).result(), "\n")
