from dataclasses import dataclass
from itertools import combinations
from timeit import timeit

from common.python.timing import Timing


@dataclass
class Coords:
    x: int
    y: int


@dataclass(frozen=True)
class Cell:
    coords: Coords
    has_galaxy: bool = False


class Image:
    def __init__(self, expanse_amount: int = 2):
        """Read the image data. Constructs a 2D matrix, where each cell contains its coordinates
        and whether or not a galaxy is present"""

        with open("input.txt", "r") as file:
            data = file.read().splitlines()

        self._empty_rows: set[int] = set([i for i, row in enumerate(data) if set(list(row.strip())) == {"."}])
        self._empty_cols: set[int] = set(
            [i for i in range(len(data[0])) if all(set(list(row[i])) == {"."} for row in data)]
        )
        self._galaxies = [self._parse(line.strip(), row) for row, line in enumerate(data)]
        self._expanse_amount = expanse_amount

    @property
    def data(self) -> list[list[Cell]]:
        """Get image data"""
        return self._galaxies

    @property
    def expanse_amount(self) -> int:
        """Get the universe expanse amount for the image"""
        return self._expanse_amount

    def galaxies(self) -> list[Cell]:
        """Return is cells that contain a galaxy"""
        res: list[Cell] = []

        for row in self._galaxies:
            for col in row:
                if col.has_galaxy:
                    res.append(col)

        return res

    def _parse(self, line: str, row: int) -> list[Cell]:
        """Parse an Image line, returning list of all cells"""
        res: list[Cell] = []
        for col, symbol in enumerate(line):
            if symbol == "#":
                res.append(Cell(coords=Coords(row, col), has_galaxy=True))
                continue
            res.append(Cell(coords=Coords(row, col)))
        return res

    def calculate_space_between_galaxies(self, galaxy_a: Cell, galaxy_b: Cell) -> int:
        """Determine the distance between two galaxies using Manhatten Distance"""
        return (
            abs(galaxy_b.coords.x - galaxy_a.coords.x)
            + abs(galaxy_b.coords.y - galaxy_a.coords.y)
            + (self._expanse_amount - 1)
            * (
                len(
                    [
                        x
                        for x in self._empty_rows
                        if min(galaxy_a.coords.x, galaxy_b.coords.x) < x < max(galaxy_a.coords.x, galaxy_b.coords.x)
                    ]
                )
                + len(
                    [
                        y
                        for y in self._empty_cols
                        if min(galaxy_a.coords.y, galaxy_b.coords.y) < y < max(galaxy_a.coords.y, galaxy_b.coords.y)
                    ]
                )
            )
        )


def solve(expanse_amount: int = 2) -> int:
    """Solve the problem"""
    image: Image = Image(expanse_amount=expanse_amount)
    galaxies: list[Cell] = image.galaxies()
    return sum([image.calculate_space_between_galaxies(a, b) for a, b in combinations(galaxies, 2)])


def main() -> None:
    """Entry point for problem"""

    print(f"Part 1: {solve(expanse_amount=2)}")
    print(f"Part 2: {solve(expanse_amount=10**6)}")


if __name__ == "__main__":
    print(Timing(timeit(main, number=1)).milliseconds, "ms")
