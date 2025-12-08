from timeit import timeit

from src.timing import Timing


class Solution:
    """Solutions to the problems."""

    def __init__(self, keys: list[list[int]], locks: list[list[int]]) -> None:
        self.keys: list[list[int]] = keys
        self.locks: list[list[int]] = locks

    @classmethod
    def parse_input(cls) -> "Solution":
        """Parse the problem data input to be used.

        Returns:
            Solution:
                Class instance with the parsed input data.
        """
        with open("./inputs/2024/25/input.txt", "r") as file:
            keys: list[list[int]] = []
            locks: list[list[int]] = []

            for grid in file.read().strip().split("\n\n"):
                values: list[list[str]] = [list(line.strip()) for line in grid.split("\n")]

                if values[0][0] == "#":
                    locks.append([line.count("#") for line in zip(*values)])
                else:
                    keys.append([line.count("#") for line in zip(*values)])

        return cls(keys=keys, locks=locks)

    def part_01(self) -> None:
        """Solve Part 01 of the problem.

        Returns:
            None
        """
        tlt: int = 0

        for lock in self.locks:
            for key in self.keys:
                tlt += all(sum(heights) <= 7 for heights in zip(key, lock))

        print(f"Part 01: {tlt}")


if __name__ == "__main__":
    sol: Solution = Solution.parse_input()

    print(Timing(timeit(sol.part_01, number=1)).result(), "\n")
