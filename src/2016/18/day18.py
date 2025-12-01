from timeit import timeit

import regex

from timing import Timing


class Solution:
    def __init__(self, data: list[str]) -> None:
        self.tiles: list[str] = data

    @classmethod
    def parse_input(cls) -> "Solution":
        """Parse the problem data input to be used.

        Returns:
            Solution:
                Class instance with the parsed input data.
        """
        with open("input.txt", "r") as file:
            values: list[str] = list(file.read().strip())

        return cls(data=values)

    def determine_new_tile_type(self, determining_tiles: str) -> str:
        """Determine the type of tile in the new row based on tiles in the previous row to the left, center and right.

        Args:
            determining_tiles (str):
                Tiles to determine the new tile type.

        Returns:
            str:
                Determined tile type.
        """
        if determining_tiles in ("^^.", ".^^", "^..", "..^"):
            return "^"
        return "."

    def create_grid(self, rows: int) -> int:
        """Create the grid with the given amount of rows and return the amount of safe spots within the grid.

        Args:
            rows (int):
                Number of rows to have in the grid.

        Returns:
            int:
                Number of safe spots.
        """
        grid: list[str] = ["".join(self.tiles)]
        for _ in range(rows - 1):
            new_role: list[str] = [
                self.determine_new_tile_type(tiles)
                for tiles in regex.findall(r"([.^]{3})", f".{grid[-1]}.", overlapped=True)
            ]
            grid.append("".join(new_role))

        return sum([tile.count(".") for tile in grid])

    def part_01(self) -> None:
        """Solve Part 01 of the problem.

        Returns:
            None
        """
        print(f"Part 01: {self.create_grid(rows=40)}")

    def part_02(self) -> None:
        """Solve Part 02 of the problem.

        Returns:
            None
        """
        print(f"Part 02: {self.create_grid(rows=400000)}")


if __name__ == "__main__":
    sol: Solution = Solution.parse_input()

    print(Timing(timeit(sol.part_01, number=1)).result(), "\n")
    print(Timing(timeit(sol.part_02, number=1)).result(), "\n")
