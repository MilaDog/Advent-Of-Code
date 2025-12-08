import heapq as hq
import itertools
from collections import defaultdict
from timeit import timeit

from src.timing import Timing


class Solution:
    """Solutions to the problems."""

    def __init__(self, data: dict[complex, str], size: tuple[int, int]) -> None:
        self.grid: dict[complex, str] = data
        self.size: tuple[int, int] = size
        self.directions: list[complex] = [-1, 1, -1j, 1j]

    @classmethod
    def parse_input(cls) -> "Solution":
        """Parse the problem data input to be used.

        Returns:
            Solution:
                Class instance with the parsed input data.
        """
        with open("./inputs/2024/16/input.txt", "r") as file:
            lines: list[str] = file.readlines()
            size: tuple[int, int] = (len(lines), len(lines[0].strip()))

            values: dict[complex, str] = {
                (x + 1j * y): val for x, row in enumerate(lines) for y, val in enumerate(row.strip())
            }

        return cls(data=values, size=size)

    def solve(self) -> None:
        """Solve Part 01 and 02 of the problem.

        Returns:
            None
        """
        start: complex = next(k for k, v in self.grid.items() if v == "S")
        end: complex = next(k for k, v in self.grid.items() if v == "E")

        # Due to using a priority queue and complex numbers, there is not way to
        # determine which item to take next if a bunch share the same complex value.
        # Need another tie-breaker.
        cnter = itertools.count()

        pq: list[tuple[int, int, complex, complex, list[complex]]] = [(0, next(cnter), start, 1j, [start])]
        visited: dict[tuple[complex, complex], float] = defaultdict(lambda: 1e9)  # each position and their score
        best: float = 1e9
        seen_tiles: list[complex] = []  # visited tiles

        while pq:
            score, _, position, direction, path = hq.heappop(pq)

            # Ignore if score is more than what is stored, since we want the
            # smallest cost
            if visited[(position, direction)] < score:
                continue
            visited[(position, direction)] = score

            if position == end and score <= best:
                best = score
                seen_tiles += path

            # Go through the different directions
            for offset in self.directions:
                if self.grid.get(position + offset, "#") == "#":
                    continue

                cost: int = 1001 if direction != offset else 1
                hq.heappush(pq, (score + cost, next(cnter), position + offset, offset, path + [position + offset]))

        print(f"Part 01: {best}")
        print(f"Part 02: {len(set(seen_tiles))}")


if __name__ == "__main__":
    sol: Solution = Solution.parse_input()

    print(Timing(timeit(sol.solve, number=1)).result(), "\n")
