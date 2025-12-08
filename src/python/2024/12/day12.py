from collections import defaultdict, deque
from dataclasses import dataclass
from timeit import timeit

from src.timing import Timing


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
        ]

    @classmethod
    def parse_input(cls) -> "Solution":
        """Parse the problem data input to be used.

        Returns:
            Solution:
                Class instance with the parsed input data.
        """
        with open("./inputs/2024/12/input.txt", "r") as file:
            values: list[list[str]] = [list(line.strip()) for line in file.readlines()]
            grid: Grid = Grid(grid=values, width=len(values), height=len(values[0]))

        return cls(grid=grid)

    def determine_sides(self, section_plots: dict[str, set[tuple[int, int]]]) -> int:
        """Part 02 part to determining the number of sides of the section.

        Args:
            section_plots (dict[str, set[tuple[int, int]]]):
                Plots of section forming the outline of the section.

        Returns:
            int:
                Number of sides.
        """
        sides: int = 0
        for direction, values in section_plots.items():
            if direction in "RL":
                outline: list[tuple[int, int]] = sorted(values, key=lambda v: (v[1], v[0]))

                if len(outline) > 1:
                    for left, right in zip(outline, outline[1:]):
                        if left[0] + 1 == right[0] and left[1] == right[1]:
                            continue
                        sides += 1

                sides += 1

            elif direction in "DU":
                outline: list[tuple[int, int]] = sorted(values, key=lambda v: (v[0], v[1]))

                if len(outline) > 1:
                    for left, right in zip(outline, outline[1:]):
                        if left[1] + 1 == right[1] and left[0] == right[0]:
                            continue
                        sides += 1

                sides += 1

        return sides

    def solve(self) -> None:
        """Solve both parts of the problem.

        Part 01: basic BFS, counting the plots in the section, then determining the perimeter.
        Part 02: Same with the BFS, but keeping track of the plots forming the outline of the section.
        Then, using this, calculating the sides of the section.

        Returns:
            None
        """
        part01: int = 0
        part02: int = 0

        seen: set[tuple[int, int]] = set()

        for x in range(self.grid.width):
            for y in range(self.grid.height):
                q: deque[tuple[int, int]] = deque([(x, y)])

                plots: int = 0
                perimeter: int = 0
                section_plots: dict[str, set[tuple[int, int]]] = defaultdict(set)

                # BFS
                while q:
                    coords: tuple[int, int] = q.popleft()

                    if coords in seen:
                        continue

                    seen.add(coords)
                    plots += 1

                    # NESW offsets
                    for dx, dy in self.directions:
                        if (
                            0 <= coords[0] + dx < self.grid.height
                            and 0 <= coords[1] + dy < self.grid.width
                            and self.grid.grid[coords[0] + dx][coords[1] + dy] == self.grid.grid[coords[0]][coords[1]]
                        ):
                            q.appendleft((coords[0] + dx, coords[1] + dy))

                        else:
                            perimeter += 1

                            # Store plots in section
                            if dy in (-1, 1):
                                section_plots[" RL"[dy]].add(coords)

                            elif dx in (-1, 1):
                                section_plots[" DU"[dx]].add(coords)

                part01 += plots * perimeter

                # Getting the sides
                sides: int = self.determine_sides(section_plots)
                part02 += plots * sides

        print(f"Part 01: {part01}")
        print(f"Part 02: {part02}")


if __name__ == "__main__":
    sol: Solution = Solution.parse_input()

    print(Timing(timeit(sol.solve, number=1)).result(), "\n")
