from timeit import timeit

from src.common.python.timing import Timing


class Solution:
    """Solutions to the problems."""

    def __init__(self, keys: list[list[list[str]]], locks: list[list[list[str]]]) -> None:
        self.keys: list[list[list[str]]] = keys
        self.locks: list[list[list[str]]] = locks

    @classmethod
    def parse_input(cls) -> "Solution":
        """Parse the problem data input to be used.

        Returns:
            Solution:
                Class instance with the parsed input data.
        """
        with open("input.txt", "r") as file:
            keys: list[list[list[str]]] = []
            locks: list[list[list[str]]] = []

            for grid in file.read().strip().split("\n\n"):
                values: list[list[str]] = [list(line.strip()) for line in grid.split("\n")]

                if values[0][0] == "#":
                    locks.append(values)
                else:
                    keys.append(values)

        return cls(keys=keys, locks=locks)

    def is_valid(self, key: list[list[str]], lock: list[list[str]]) -> bool:
        """Check if the given key fits the given lock.

        Args:
            key (list[list[str]]):
                Key to check.
            lock (list[list[str]]):
                Lock to check.

        Returns:
            bool:
                Whether the key fits or not.
        """
        width: int = len(key)
        height: int = len(key[0])

        for x in range(width):
            for y in range(height):
                if key[x][y] == "#" and lock[x][y] == "#":
                    return False

        return True

    def part_01(self) -> None:
        """Solve Part 01 of the problem.

        Returns:
            None
        """
        tlt: int = 0

        for lock in self.locks:
            for key in self.keys:
                tlt += self.is_valid(key=key, lock=lock)

        print(f"Part 01: {tlt}")


if __name__ == "__main__":
    sol: Solution = Solution.parse_input()

    print(Timing(timeit(sol.part_01, number=1)).result(), "\n")
