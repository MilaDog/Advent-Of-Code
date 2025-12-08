from collections import defaultdict
from dataclasses import dataclass
from timeit import timeit

from src.timing import Timing


@dataclass
class Input:
    """Data for the problem."""

    grid: dict[complex, str]
    movements: list[str]
    size: tuple[int, int]


class Solution:
    """Solutions to the problems."""

    def __init__(self) -> None:
        self.directions: dict[str, complex] = {"^": -1, "v": 1, "<": -1j, ">": 1j}

    @staticmethod
    def parse_input(part02: bool = False) -> "Input":
        """Parse the problem data input to be used.

        Returns:
            dict[complex, str]:
                Input data.
        """
        with open("./inputs/2024/15/input.txt", "r") as file:
            g, m = file.read().strip().split("\n\n")

            if part02:
                g = g.replace("#", "##").replace(".", "..").replace("O", "[]").replace("@", "@.")

            grid_rows: list[str] = g.strip().split("\n")

            # Movements
            movements: list[str] = []
            for line in m:
                movements += list(line.strip())

            # Grid
            grid: dict[complex, str] = defaultdict(str)
            width: int = len(grid_rows)
            height: int = len(grid_rows[0])

            for x, row in enumerate(grid_rows):
                for y, col in enumerate(row.strip()):
                    grid[x + 1j * y] = col

        return Input(movements=movements, grid=grid, size=(width, height))

    def get_starting_position(self, grid: dict[complex, str]) -> complex:
        """Get the starting position within the grid.

        Returns:
            complex:
                Starting position.
        """
        for k, v in grid.items():
            if v == "@":
                return k

        assert False, "No starting point found within the grid."

    def push_box(self, grid: dict[complex, str], position: complex, direction: complex) -> complex:
        """Push the box in the given direction, moving any other boxes in its path as well.

        Args:
            grid (dict[complex, str]):
                Grid to go through.
            position (complex):
                Current position to start moving from.
            direction (complex):
                Direction to push the box(es) in.

        Returns:
            complex:
                New character position after moving the box(es).
        """
        line: list[tuple[complex, str]] = [(position, grid[position])]

        tmp: complex = position + direction
        while True:
            line.append((tmp, grid[tmp]))

            tmp += direction
            if grid[tmp] in ".#":
                line.append((tmp, grid[tmp]))
                break

        if line[-1][1] == ".":
            for pos, val in line[::-1]:
                grid[pos] = grid[pos - direction]
            grid[position] = "."
            return position + direction

        # No movement
        return position

    def push_box_p2(self, grid: dict[complex, str], position: complex, direction: complex) -> complex:
        """Push the box in the given direction, moving any other boxes in its path as well.

        Args:
            grid (dict[complex, str]):
                Grid to go through.
            position (complex):
                Current position to start moving from.
            direction (complex):
                Direction to push the box(es) in.

        Returns:
            complex:
                New character position after moving the box(es).
        """
        original_position: complex = position

        # DFS to get the boxes to move
        rows: list[set[complex]] = []
        current_row: set[complex] = {position}

        while current_row:
            next_row: set[complex] = set()
            rows.append(current_row)

            for pos in current_row:
                match grid[pos + direction]:
                    case "#":
                        # Cannot move the boxes
                        return original_position

                    case "[":
                        next_row.add(pos + direction)
                        next_row.add(pos + direction + 1j)

                    case "]":
                        next_row.add(pos + direction)
                        next_row.add(pos + direction - 1j)

            current_row = next_row
            position += direction

        # Moving the boxes
        for row in rows[::-1]:
            for pos in row:
                grid[pos + direction], grid[pos] = grid[pos], grid[pos + direction]

        return original_position + direction

    def display_grid(self, grid: dict[complex, str], size: tuple[int, int]) -> None:
        """Display the grid.

        Args:
            grid (dict[complex, str]):
                Grid to display.
            size (tuple[int, int]):
                Size of the grid.

        Returns:
            None
        """
        for x in range(size[0]):
            row: list[str] = [grid[x + 1j * y] for y in range(size[1])]
            print("".join(row))

    def sum_gps_coordinates(self, grid: dict[complex, str], size: tuple[int, int]) -> int:
        """Determine the sum of all the coordinates of the boxes within the grid.

        Args:
            grid (dict[complex, str]):
                Grid to get the sum of all box coordinates for.
            size (tuple[int, int]):
                Size of the grid.

        Returns:
            int:
                SUm of all box coordinates.
        """
        tlt: int = 0

        width: int
        height: int
        width, height = size

        for x in range(1, width - 1):
            for y in range(1, height - 1):
                if grid[x + 1j * y] in "O[":
                    tlt += 100 * x + y

        return tlt

    def part_01(self) -> None:
        """Solve Part 01 of the problem.

        Returns:
            None
        """
        inpt: Input = Solution.parse_input()
        current: complex = self.get_starting_position(grid=inpt.grid)

        for movement in inpt.movements:
            direction: complex = self.directions[movement]

            match inpt.grid[current + direction]:
                case ".":
                    inpt.grid[current + direction], inpt.grid[current] = (
                        inpt.grid[current],
                        inpt.grid[current + direction],
                    )
                    current += direction

                case "#":
                    pass

                case "O":
                    current = self.push_box(grid=inpt.grid, position=current, direction=direction)

        # self.display_grid(grid=inpt.grid, size=inpt.size)
        tlt: int = self.sum_gps_coordinates(grid=inpt.grid, size=inpt.size)
        print(f"Part 01: {tlt}")

    def part_02(self) -> None:
        """Solve Part 02 of the problem.

        Returns:
            None
        """
        inpt: Input = Solution.parse_input(part02=True)
        current: complex = self.get_starting_position(grid=inpt.grid)

        for movement in inpt.movements:
            direction: complex = self.directions[movement]

            match inpt.grid[current + direction]:
                case ".":
                    inpt.grid[current + direction], inpt.grid[current] = (
                        inpt.grid[current],
                        inpt.grid[current + direction],
                    )
                    current += direction

                case "#":
                    pass

                case "[" | "]":
                    if movement in "<>":
                        current = self.push_box(grid=inpt.grid, position=current, direction=direction)

                    else:
                        current = self.push_box_p2(grid=inpt.grid, position=current, direction=direction)

        # self.display_grid(grid=inpt.grid, size=inpt.size)
        tlt: int = self.sum_gps_coordinates(grid=inpt.grid, size=inpt.size)
        print(f"Part 02: {tlt}")


if __name__ == "__main__":
    sol: Solution = Solution()

    print(Timing(timeit(sol.part_01, number=1)).result(), "\n")
    print(Timing(timeit(sol.part_02, number=1)).result(), "\n")
