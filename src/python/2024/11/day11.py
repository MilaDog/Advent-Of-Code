from functools import lru_cache
from timeit import timeit

from src.timing import Timing


class Solution:
    """Solutions to the problems."""

    def __init__(self, data: list[int]) -> None:
        self.stones: list[int] = data

    @classmethod
    def parse_input(cls) -> "Solution":
        """Parse the problem data input to be used.

        Returns:
            Solution:
                Class instance with the parsed input data.
        """
        with open("./inputs/2024/11/input.txt", "r") as file:
            values: list[int] = list(map(int, file.read().strip().split(" ")))

        return cls(data=values)

    @lru_cache(None)
    def mutate(self, stone: int, amount: int, limit: int) -> int:
        """Mutate the given stone the given amount of times, till LIMIT is reached.

        Args:
            stone (int):
                Stone to be mutated.
            amount (int):
                Current iteration.
            limit (int):
                Total number of iterations to perform.

        Returns:
            int:
                Total number of stones after the original stone has been mutated LIMIT
                amount of times.
        """
        if amount == limit:
            return 1

        if stone == 0:
            return self.mutate(1, amount + 1, limit)

        if len(str(stone)) % 2 == 0:
            mid: int = len(str(stone)) // 2
            return self.mutate(int(str(stone)[:mid]), amount + 1, limit) + self.mutate(
                int(str(stone)[mid:]), amount + 1, limit
            )

        return self.mutate(stone * 2024, amount + 1, limit)

    def solve(self, limit: int) -> int:
        """Solve the problem up to the given LIMIT, being the number of iterations of
        mutations that should occur.

        Args:
            limit (int):
                Total number of mutation iterations to perform.

        Returns:
            int:
                Number of stones after LIMIT mutation iterations.
        """
        return sum(self.mutate(stone=stone, amount=0, limit=limit) for stone in self.stones)

    def part_01(self) -> None:
        """Solve Part 01 of the problem.

        Returns:
            None
        """
        tlt: int = self.solve(limit=25)
        print(f"Part 01: {tlt}")

    def part_02(self) -> None:
        """Solve Part 02 of the problem.

        Returns:
            None
        """
        tlt: int = self.solve(limit=75)
        print(f"Part 02: {tlt}")


if __name__ == "__main__":
    sol: Solution = Solution.parse_input()

    print(Timing(timeit(sol.part_01, number=1)).result(), "\n")
    print(Timing(timeit(sol.part_02, number=1)).result(), "\n")
