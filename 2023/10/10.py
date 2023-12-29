from collections import deque
from dataclasses import dataclass
from enum import Enum
from timeit import timeit
from typing import Optional

from common.python.timing import Timing


class Directions(Enum):
    NORTH = (-1, 0)
    EAST = (0, 1)
    SOUTH = (1, 0)
    WEST = (0, -1)


class Symbols(Enum):
    PIPE_VERTICAL = ("|", [Directions.NORTH, Directions.SOUTH])
    PIPE_HORIZONTAL = ("-", [Directions.EAST, Directions.WEST])
    BEND_NORTH_EAST = ("L", [Directions.EAST, Directions.NORTH])
    BEND_NORTH_WEST = ("J", [Directions.WEST, Directions.NORTH])
    BEND_SOUTH_EAST = ("F", [Directions.EAST, Directions.SOUTH])
    BEND_SOUTH_WEST = ("7", [Directions.WEST, Directions.SOUTH])
    START = ("S", [Directions.WEST, Directions.SOUTH, Directions.NORTH, Directions.EAST])
    EMPTY = (".", None)


DIRECTION_PAIRS: dict[Directions, Directions] = {
    Directions.NORTH: Directions.SOUTH,
    Directions.SOUTH: Directions.NORTH,
    Directions.EAST: Directions.WEST,
    Directions.WEST: Directions.EAST,
}


@dataclass()
class Cell:
    x: int
    y: int
    symbol: Symbols


class Grid:
    def __init__(self, data: list[list[Cell]]) -> None:
        self.grid: list[list[Cell]] = data
        self.height: int = len(data)
        self.width: int = len(data[0])
        self.starting_point: Optional[Cell] = self._find_starting_point()
        self.loop: list[tuple[int, int]] = self._determine_grid_loop()

    @staticmethod
    def parse_data(data: str) -> list[list[Cell]]:
        """
        parse_data Parse the input data 2D Matrix of cells

        Args:
            data (str): Data to parse

        Returns:
            list[list[Cell]]: Matrix of grid cells
        """
        grid: list = []

        for x, line in enumerate(data.splitlines()):
            row: list[Cell] = []

            for y, val in enumerate(list(line.strip())):
                sym: Symbols = Symbols.EMPTY
                match val:
                    case "-":
                        sym = Symbols.PIPE_HORIZONTAL
                    case "|":
                        sym = Symbols.PIPE_VERTICAL
                    case "S":
                        sym = Symbols.START
                    case "7":
                        sym = Symbols.BEND_SOUTH_WEST
                    case "F":
                        sym = Symbols.BEND_SOUTH_EAST
                    case "J":
                        sym = Symbols.BEND_NORTH_WEST
                    case "L":
                        sym = Symbols.BEND_NORTH_EAST

                row.append(Cell(x, y, sym))

            grid.append(row)

        return grid

    @classmethod
    def read_input(cls):
        """
        read_input Read the input data for the problem
        """
        with open("input.txt", "r") as file:
            data: str = file.read().strip()

        return cls(cls.parse_data(data))

    def _find_starting_point(self) -> Optional[Cell]:
        """
        _find_starting_point Find the starting point of the grid

        Returns:
            Cell: Starting point of grid
        """
        for row in self.grid:
            for cell in row:
                if cell.symbol.value[0] == "S":
                    return cell

        assert "Cannot find a starting point"

    def _is_within_grid_bounds(self, x: int, y: int) -> bool:
        """
        _is_within_grid_bounds Determine if the coordinates are within the grid's bounds

        Args:
            x (int): X Coordinate
            y (int): Y Coordinate

        Returns:
            bool: If coordinates are within the grid's bounds
        """
        return 0 <= x < self.height and 0 <= y < self.width

    def _determine_grid_loop(self) -> list[tuple[int, int]]:
        """
        _determine_grid_loop Determine the loop of the grid
        """
        queue = deque([self.starting_point])
        visited = set()
        loop = []

        while queue:
            current_cell: Optional[Cell] = queue.popleft()

            # Check if it has been visited
            if current_cell in visited or current_cell is None:
                continue

            visited.add(current_cell)
            loop.append((current_cell.x, current_cell.y))

            # Checking that the directions are not none
            if current_cell.symbol.value[1] is None or len(current_cell.symbol.value[1]) == 0:
                continue

            for direction in current_cell.symbol.value[1]:
                dx, dy = direction.value

                if self._is_within_grid_bounds(current_cell.x + dx, current_cell.y + dy):
                    target_cell: Cell = self.grid[current_cell.x + dx][current_cell.y + dy]

                    if target_cell.symbol == Symbols.EMPTY or target_cell in visited:
                        continue

                    # Checking that you can enter the target_cell from current_cell
                    if DIRECTION_PAIRS.get(direction) in target_cell.symbol.value[1]:
                        if current_cell.symbol.value[0] == "S":  # Choosing initial route
                            queue.append(target_cell)
                            break

                        queue.append(target_cell)

        return loop

    def _shoelace_formula(self) -> float:
        """
        _shoelace_formula Calculate the area of the polygon using Shoelace Theorem

        Returns:
            float: Area of the polygon
        """
        x, y = zip(*self.loop)
        return 0.5 * abs(sum(x[i] * y[i - 1] - x[i - 1] * y[i] for i in range(len(self.loop))))

    def _picks_theorem(self, area: float) -> int:
        """
        _picks_theorem Determine the number of empty cells inside the polygon

        Args:
            area (float): Area of the polygon

        Returns:
            int: Number of empty cells within polygon
        """
        return int(area - 0.5 * len(self.loop) + 1)

    def solve(self):
        """Solving both Parts of the problem"""
        self._determine_grid_loop()

        print("Part 1:", len(self.loop) // 2)

        area: float = self._shoelace_formula()
        print("Part 2:", self._picks_theorem(area))


def main() -> None:
    """Main entry point to solving the problem"""
    grid: Grid = Grid.read_input()
    grid.solve()


if __name__ == "__main__":
    print(Timing(timeit(main, number=1)).milliseconds, "milliseconds")
