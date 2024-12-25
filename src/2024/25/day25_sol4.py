from timeit import timeit

from src.common.python.timing import Timing


class Solution:
    """Solutions to the problems."""

    def __init__(self, keys: list[set[complex]], locks: list[set[complex]]) -> None:
        self.keys: list[set[complex]] = keys
        self.locks: list[set[complex]] = locks

    @classmethod
    def parse_input(cls) -> "Solution":
        """Parse the problem data input to be used.

        Returns:
            Solution:
                Class instance with the parsed input data.
        """

        def get_coords(g: list[str], key: str = "#") -> set[complex]:
            res: set[complex] = set()
            for x, row in enumerate(g):
                for y, col in enumerate(row.strip()):
                    if col == key:
                        res.add(x + 1j * y)

            return res

        with open("input.txt", "r") as file:
            keys: list[set[complex]] = []
            locks: list[set[complex]] = []

            for grid in file.read().strip().split("\n\n"):
                lines: list[str] = [line.strip() for line in grid.split("\n")]

                if lines[0][0] == "#":
                    locks.append(get_coords(g=lines, key="."))
                else:
                    keys.append(get_coords(g=lines))

        return cls(keys=keys, locks=locks)

    def part_01(self) -> None:
        """Solve Part 01 of the problem.

        Returns:
            None
        """
        tlt: int = 0

        for lock in self.locks:
            for key in self.keys:
                tlt += not key - lock

        print(f"Part 01: {tlt}")


if __name__ == "__main__":
    sol: Solution = Solution.parse_input()

    print(Timing(timeit(sol.part_01, number=1)).result(), "\n")
