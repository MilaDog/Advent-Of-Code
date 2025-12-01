from collections import deque
from timeit import timeit

from timing import Timing


class Solution:
    def __init__(self, data: int) -> None:
        self.data: int = data

    @classmethod
    def parse_input(cls) -> "Solution":
        """Parse the problem data input to be used.

        Returns:
            Solution:
                Class instance with the parsed input data.
        """
        with open("input.txt", "r") as file:
            values: int = int(file.read().strip())

        return cls(data=values)

    def is_wall(self, coords: tuple[int, int]) -> bool:
        """Determines if the given coordinates represents a wall or not.

        Args:
            coords (tuple[int, int):
                Coordinates to location in grid.

        Returns:
            bool:
                If target coordinates have a wall or not.

        """
        x: int
        y: int
        x, y = coords

        val: int = x * x + 3 * x + 2 * x * y + y + y * y
        val += self.data

        return val.bit_count() % 2 == 1

    def solve(self) -> None:
        """Solve Part 01 and 02 of the problem.

        Returns:
            None
        """
        part01: int = 0
        part02: int = 0

        seen: set[tuple[int, int]] = set()
        target_coords: tuple[int, int] = (31, 39)

        start_coords: tuple[int, int, int] = (1, 1, 0)
        q: deque[tuple[int, int, int]] = deque([start_coords])

        while q:
            x: int
            y: int
            steps: int
            x, y, steps = q.popleft()
            seen.add((x, y))

            # IFF meeting target
            if (x, y) == target_coords:
                part01 = steps

            if steps == 50:
                part02 = len(seen)

            for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                # Either coordinate cannot be negative.
                if (x + dx, y + dy) in seen or x + dx < 0 or y + dy < 0 or self.is_wall((x + dx, y + dy)):
                    continue

                q.append((x + dx, y + dy, steps + 1))

        print(f"Part 01: {part01}")
        print(f"Part 02: {part02}")


if __name__ == "__main__":
    sol: Solution = Solution.parse_input()

    print(Timing(timeit(sol.solve, number=1)).result(), "\n")
