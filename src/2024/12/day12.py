from collections import defaultdict, deque
from dataclasses import dataclass
from timeit import timeit

from src.common.python.timing import Timing


@dataclass
class Grid:
    """Grid for the problem."""

    grid: list[list[str]]
    width: int
    height: int


class Solution:
    """Solutions to the problems."""

    def __init__(self, grid: Grid) -> None:
        self.grid: Grid = grid
        self.directions: list[tuple[int, int]] = [
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0),
        ]  # NESW

    @classmethod
    def parse_input(cls) -> "Solution":
        """Parse the problem data input to be used.

        Returns:
            Solution:
                Class instance with the parsed input data.
        """
        with open("input.txt", "r") as file:
            values: list[list[str]] = [list(line.strip()) for line in file.readlines()]
            grid: Grid = Grid(grid=values, width=len(values), height=len(values[0]))

        return cls(grid=grid)

    def part_01(self) -> None:
        """Solve Part 01 of the problem.

        Returns:
            None
        """
        tlt: int = 0

        seen: set[tuple[int, int]] = set()

        for x in range(self.grid.width):
            for y in range(self.grid.height):
                q: deque[tuple[int, int]] = deque([(x, y)])

                plots: int = 0
                perimeter: int = 0

                # BFS
                while q:
                    coords: tuple[int, int] = q.popleft()

                    if coords in seen:
                        continue

                    seen.add(coords)
                    plots += 1

                    for dx, dy in self.directions:
                        if (
                            0 <= coords[0] + dx < self.grid.height
                            and 0 <= coords[1] + dy < self.grid.width
                        ):
                            if (
                                self.grid.grid[coords[0] + dx][coords[1] + dy]
                                != self.grid.grid[coords[0]][coords[1]]
                            ):
                                perimeter += 1

                            else:
                                q.appendleft((coords[0] + dx, coords[1] + dy))

                        else:
                            perimeter += 1

                tlt += plots * perimeter

        print(f"Part 01: {tlt}")

    def part_02(self) -> None:
        """Solve Part 02 of the problem.

        Returns:
            None
        """
        tlt: int = 0

        seen: set[tuple[int, int]] = set()

        for x in range(self.grid.width):
            for y in range(self.grid.height):
                if (x, y) in seen:
                    continue

                q: deque[tuple[int, int]] = deque([(x, y)])

                plots: int = 0
                section_plots: dict[str, set[tuple[int, int]]] = defaultdict(set)

                # BFS
                while q:
                    coords: tuple[int, int] = q.popleft()

                    if coords in seen:
                        continue

                    seen.add(coords)
                    plots += 1

                    for dx, dy in self.directions:
                        if (
                            0 <= coords[0] + dx < self.grid.height
                            and 0 <= coords[1] + dy < self.grid.width
                        ):
                            if (
                                self.grid.grid[coords[0] + dx][coords[1] + dy]
                                == self.grid.grid[coords[0]][coords[1]]
                            ):
                                q.appendleft((coords[0] + dx, coords[1] + dy))

                            else:
                                if dy == 1:
                                    section_plots["R"].add(coords)

                                elif dx == 1:
                                    section_plots["D"].add(coords)

                                elif dy == -1:
                                    section_plots["L"].add(coords)

                                elif dx == -1:
                                    section_plots["U"].add(coords)

                        else:
                            if dy == 1:
                                section_plots["R"].add(coords)

                            elif dx == 1:
                                section_plots["D"].add(coords)

                            elif dy == -1:
                                section_plots["L"].add(coords)

                            elif dx == -1:
                                section_plots["U"].add(coords)

                # Getting the sides
                sides: int = 0

                for direction, values in section_plots.items():
                    if direction in "RL":
                        outline: list[tuple[int, int]] = sorted(
                            values, key=lambda v: (v[1], v[0])
                        )
                        # print(outline)

                        if len(outline) > 1:
                            # print(list(zip(outline, outline[1:])))
                            for left, right in zip(outline, outline[1:]):
                                if left[0] + 1 == right[0] and left[1] == right[1]:
                                    continue
                                sides += 1

                        sides += 1

                    elif direction in "DU":
                        outline: list[tuple[int, int]] = sorted(
                            values, key=lambda v: (v[0], v[1])
                        )

                        if len(outline) > 1:
                            for left, right in zip(outline, outline[1:]):
                                if left[1] + 1 == right[1] and left[0] == right[0]:
                                    continue
                                sides += 1

                        sides += 1

                tlt += plots * sides

        print(f"Part 02: {tlt}")


if __name__ == "__main__":
    sol: Solution = Solution.parse_input()

    print(Timing(timeit(sol.part_01, number=1)).result(), "\n")
    print(Timing(timeit(sol.part_02, number=1)).result(), "\n")
