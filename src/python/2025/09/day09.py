import itertools as itr
from timeit import timeit
from typing import Any

from shapely import Polygon

from src.timing import Timing

type Point = tuple[int, int]


class Solution:
    """Solutions to the problems."""

    def __init__(self, data: list[Point]) -> None:
        self.data: list[Point] = data

    @classmethod
    def parse_input(cls) -> "Solution":
        """Parse the problem data input to be used.

        Returns:
            Solution:
                Class instance with the parsed input data.
        """
        values: list[Point] = []

        with open("./inputs/2025/09/input.txt", "r") as file:
            for line in file.readlines():
                x, y = line.strip().split(",")
                values.append((int(x), int(y)))

        return cls(data=values)

    def calculate_area(self, point1: Point, point2: Point) -> float:
        """Calculate the area of the rectangle formed from the two points.

        Args:
            point1 (Point): Point 1 (corner).
            point2 (Point): Point 2 (corner).

        Returns:
            float: Area of the determined rectangle.
        """
        x1, y1 = point1
        x2, y2 = point2

        return (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)

    def calculate_rectangle(self, point1: Point, point2: Point) -> Polygon:
        """Calculate a rectangle with the given two points.

        Args:
            point1 (Point): Point 1.
            point2 (Point): Point 2.

        Returns:
            Polygon: Constructed polygon.
        """
        x1, y1 = point1
        x2, y2 = point2

        return Polygon([(x1, y1), (x2, y1), (x2, y2), (x1, y2)])

    def solve_shapely(self) -> None:
        """Solve Part 01 and 02 of the problem."""
        print("Shapely Approach")
        combos: list[Any] = list(itr.combinations(self.data, 2))

        tlt: float = max(self.calculate_area(point1=point1, point2=point2) for point1, point2 in combos)
        print(f"Part 01: {tlt}")

        polygon: Polygon = Polygon(self.data)
        tlt = max(
            self.calculate_area(point1=point1, point2=point2)
            for point1, point2 in combos
            if polygon.contains(self.calculate_rectangle(point1=point1, point2=point2))
        )
        print(f"Part 02: {tlt}")

    def solve(self) -> None:
        """Solve Part 01 and 02 of the problem with a vanilla approach."""
        tlt1 = tlt2 = 0

        for (x, y), (u, v) in itr.combinations(self.data, 2):
            x, u = sorted((x, u))
            y, v = sorted((y, v))

            area: float = self.calculate_area(point1=(x, y), point2=(u, v))
            tlt1 = max(tlt1, area)

            for (p, q), (r, s) in itr.pairwise(self.data + [self.data[0]]):
                p, r = sorted((p, r))
                q, s = sorted((q, s))
                if all((x < r, u > p, y < s, v > q)):
                    break

            else:
                tlt2 = max(tlt2, area)

        print("Vanilla Approach")
        print(f"Part 01: {tlt1}")
        print(f"Part 02: {tlt2}")


if __name__ == "__main__":
    sol: Solution = Solution.parse_input()

    # Vanilla approach
    print(Timing(timeit(sol.solve, number=1)).result(), "\n")

    # Using Shapely
    print(Timing(timeit(sol.solve_shapely, number=1)).result(), "\n")
