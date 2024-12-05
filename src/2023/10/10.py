from collections import deque
from dataclasses import dataclass
from enum import Enum
from timeit import timeit

from common.python.timing import Timing


class Directions(Enum):
    NORTH = (-1, 0)
    EAST = (0, 1)
    SOUTH = (1, 0)
    WEST = (0, -1)


class Symbols(Enum):
    PIPE_VERTICAL = "|"
    PIPE_HORIZONTAL = "-"
    BEND_NORTH_EAST = "L"
    BEND_NORTH_WEST = "J"
    BEND_SOUTH_EAST = "F"
    BEND_SOUTH_WEST = "7"
    START = "S"
    EMPTY = "."


class SymbolEntrances(Enum):
    PIPE_VERTICAL = [Directions.NORTH, Directions.SOUTH]
    PIPE_HORIZONTAL = [Directions.EAST, Directions.WEST]
    BEND_NORTH_EAST = [Directions.EAST, Directions.NORTH]
    BEND_NORTH_WEST = [Directions.WEST, Directions.NORTH]
    BEND_SOUTH_EAST = [Directions.EAST, Directions.SOUTH]
    BEND_SOUTH_WEST = [Directions.WEST, Directions.SOUTH]
    START = [Directions.WEST, Directions.SOUTH, Directions.NORTH, Directions.EAST]
    EMPTY = None


DIRECTION_PAIRS: dict[Directions, Directions] = {
    Directions.NORTH: Directions.SOUTH,
    Directions.SOUTH: Directions.NORTH,
    Directions.EAST: Directions.WEST,
    Directions.WEST: Directions.EAST,
}


@dataclass(frozen=True)
class Cell:
    symbol: Symbols
    entrances: SymbolEntrances


class Grid:
    def __init__(self, data: list[list[Cell]]) -> None:
        self.grid: list[list[Cell]] = data
        self.height: int = len(data)
        self.width: int = len(data[0])
        self.starting_point: tuple[int, int, Cell] = self._find_starting_point()
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

        for line in data.splitlines():
            row: list[Cell] = []

            for val in list(line.strip()):
                row.append(
                    Cell(
                        Symbols(val),
                        SymbolEntrances._member_map_.get(Symbols(val).name),
                    )
                )  # type: ignore

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

    def _find_starting_point(self) -> tuple[int, int, Cell]:
        """
        _find_starting_point Find the starting point of the grid

        Returns:
            Cell: Starting point of grid
        """
        for x, row in enumerate(self.grid):
            for y, cell in enumerate(row):
                if cell.symbol == Symbols.START:
                    return (x, y, cell)

        raise Exception("Cannot find a starting point")

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

        Returns:
            list[tuple[int, int]]: Closed loop in the grid
        """
        queue = deque([self.starting_point])
        visited = set()
        loop = []

        while queue:
            curr = queue.popleft()

            # Check if it has been visited
            if curr in visited:
                continue
            visited.add(curr)

            # Unpacking tuple
            x, y, current_cell = curr
            loop.append((x, y))

            if current_cell.entrances.value is not None:
                for direction in current_cell.entrances.value:
                    dx, dy = direction.value[0] + x, direction.value[1] + y

                    if self._is_within_grid_bounds(dx, dy):
                        target_cell: Cell = self.grid[dx][dy]

                        if (
                            target_cell.symbol == Symbols.EMPTY
                            or (dx, dy, target_cell) in visited
                        ):
                            continue

                        # Checking that you can enter the target_cell from current_cell
                        if (
                            DIRECTION_PAIRS.get(direction) is None
                            or target_cell.entrances.value is None
                        ):
                            continue

                        if (
                            DIRECTION_PAIRS.get(direction)
                            in target_cell.entrances.value
                        ):
                            # Choosing initial route
                            if current_cell.symbol == Symbols.START:
                                queue.append((dx, dy, target_cell))
                                break

                            queue.append((dx, dy, target_cell))

        return loop

    def _shoelace_formula(self) -> float:
        """
        _shoelace_formula Calculate the area of the polygon using Shoelace Formula

        Returns:
            float: Area of the polygon
        """
        x, y = zip(*self.loop)
        return (
            abs(sum(x[i] * y[i - 1] - x[i - 1] * y[i] for i in range(len(self.loop))))
            // 2
        )

    def _picks_theorem(self, area: float) -> int:
        """
        _picks_theorem Determine the number of empty cells inside the polygon

        Args:
            area (float): Area of the polygon

        Returns:
            int: Number of empty cells within polygon
        """
        return int(area - len(self.loop) // 2 + 1)

    def solve(self):
        """Solving both Parts of the problem"""
        print("Part 1:", len(self.loop) // 2)

        area: float = self._shoelace_formula()
        print("Part 2:", self._picks_theorem(area))


def main() -> None:
    """Main entry point to solving the problem"""
    grid: Grid = Grid.read_input()
    grid.solve()


if __name__ == "__main__":
    print(Timing(timeit(main, number=1)).milliseconds, "milliseconds")
