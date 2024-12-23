from collections import defaultdict
from itertools import combinations
from timeit import timeit

from src.common.python.timing import Timing


class Solution:
    """Solutions to the problems."""

    def __init__(self, antennas: dict[str, list[tuple[int, int]]], size: tuple[int, int]) -> None:
        self.antennas: dict[str, list[tuple[int, int]]] = antennas
        self.size: tuple[int, int] = size

    @classmethod
    def parse_input(cls) -> "Solution":
        """Parse the problem data input to be used.

        Returns:
            Solution:
                Class instance with the parsed input data.
        """
        values: dict[str, list[tuple[int, int]]] = defaultdict(list)

        with open("input.txt", "r") as file:
            lines: list[str] = [line.strip() for line in file.readlines()]
            size: tuple[int, int] = (len(lines), len(lines[0]))

            for x, row in enumerate(lines):
                for y, col in enumerate(row):
                    if col != ".":
                        values[col].append((x, y))

        return cls(size=size, antennas=values)

    def is_in_grid(self, position: tuple[int, int]) -> bool:
        """Check if the given position is within the grid.

        Args:
            position (tuple[int, int]):
                Position to validate.

        Returns:
            bool:
                If position is valid or not.
        """
        return 0 <= position[0] < self.size[0] and 0 <= position[1] < self.size[1]

    def solve(self) -> None:
        """Solve Part 01 and Part 02 of the problem.

        Returns:
            None
        """
        antinodes: set[tuple[int, int]] = set()
        more_antinodes: set[tuple[int, int]] = set()
        for antennas in self.antennas.values():
            for (ax, ay), (bx, by) in combinations(antennas, 2):
                more_antinodes.add((ax, ay))
                more_antinodes.add((bx, by))

                dx: int = bx - ax
                dy: int = by - ay

                new_a: tuple[int, int] = (ax - dx, ay - dy)

                if self.is_in_grid(position=new_a):
                    antinodes.add(new_a)

                while self.is_in_grid(position=new_a):
                    more_antinodes.add(new_a)
                    new_a = (new_a[0] - dx, new_a[1] - dy)

                new_b: tuple[int, int] = (bx + dx, by + dy)
                if self.is_in_grid(position=new_b):
                    antinodes.add(new_b)

                while self.is_in_grid(position=new_b):
                    more_antinodes.add(new_b)
                    new_b = (new_b[0] + dx, new_b[1] + dy)

        print(f"Part 01: {len(antinodes)}")
        print(f"Part 02: {len(more_antinodes)}")


if __name__ == "__main__":
    sol: Solution = Solution.parse_input()

    print(Timing(timeit(sol.solve, number=1)).result(), "\n")
