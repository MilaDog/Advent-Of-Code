from copy import deepcopy
from timeit import timeit

from src.timing import Timing


class Solution:
    """Solutions to the problems."""

    def __init__(
        self,
        data: dict[tuple[int, int], str],
        initial_position: tuple[int, int],
        size: tuple[int, int],
    ) -> None:
        self.data: dict[tuple[int, int], str] = data
        self.position: tuple[int, int] = initial_position
        self.height: int = size[0]
        self.width: int = size[1]
        self.factors: list[tuple[int, int]] = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    @classmethod
    def parse_input(cls) -> "Solution":
        """Parse the problem data input to be used.

        Returns:
            Solution:
                Class instance with the parsed input data.
        """
        start: tuple[int, int] = (0, 0)
        with open("./inputs/2024/06/input.txt", "r") as file:
            values: dict[tuple[int, int], str] = dict()
            lines: list[str] = file.readlines()

            height: int = len(lines)
            width: int = len(lines[0])

            for x, row in enumerate(lines):
                for y, col in enumerate(row):
                    values[(x, y)] = col

                    if col == "^":
                        start = (x, y)

        return cls(data=values, initial_position=start, size=(height, width))

    def part_01(self) -> None:
        """Solve Part 01 of the problem.

        Returns:
            None
        """
        # NESW -> 0123
        direction: int = 0

        grid: dict[tuple[int, int], str] = deepcopy(self.data)
        position: tuple[int, int] = deepcopy(self.position)
        grid[position] = "X"

        while True:
            # Move
            direction %= 4
            dx, dy = self.factors[direction]

            new_position: tuple[int, int] = (
                position[0] + dx,
                position[1] + dy,
            )

            # Check if in bounds
            if new_position not in grid:
                break

            # Check if hit object
            if grid[new_position] == "#":
                direction += 1
                continue

            # Mark area
            position = new_position

            if grid[position] == ".":
                grid[position] = "X"

        tlt: int = sum(v == "X" for v in grid.values())

        print(f"Part 01: {tlt}")

    def part_02(self) -> None:
        """Solve Part 02 of the problem.

        Returns:
            None
        """
        tlt: int = 0

        # Augh, have to brute force it
        for row in range(self.height):
            for col in range(self.width):
                pos_row: int = self.position[0]
                pos_col: int = self.position[1]
                direction: int = 0

                SEEN: set[tuple[int, int, int]] = set()

                # Iterating grid to determine if cycle can be made
                while True:
                    if (pos_row, pos_col, direction) in SEEN:
                        tlt += 1
                        break

                    SEEN.add((pos_row, pos_col, direction))
                    change: tuple[int, int] = self.factors[direction]

                    dx: int = pos_row + change[0]
                    dy: int = pos_col + change[1]

                    # Outside grid
                    if (dx, dy) not in self.data:
                        break

                    if self.data[(dx, dy)] == "#" or dx == row and dy == col:
                        direction = (direction + 1) % 4

                    else:
                        pos_row, pos_col = dx, dy

        print(f"Part 02: {tlt}")


if __name__ == "__main__":
    sol: Solution = Solution.parse_input()

    print(Timing(timeit(sol.part_01, number=1)).result(), "\n")
    print(Timing(timeit(sol.part_02, number=1)).result(), "\n")
