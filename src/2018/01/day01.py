import itertools
from timeit import timeit

from timing import Timing


class Solution:
    def __init__(self, data: list[int]) -> None:
        self.data: list[int] = data

    @classmethod
    def parse_input(cls) -> "Solution":
        """Parse the problem data input to be used.

        Returns:
            Solution:
                Class instance with the parsed input data.
        """
        with open("input.txt", "r") as file:
            values: list[int] = [int(line.strip()) for line in file.readlines()]

        return cls(data=values)

    def part_01(self) -> None:
        """Solve Part 01 of the problem.

        Returns:
            None
        """
        tlt: int = sum(self.data)
        print(f"Part 01: {tlt}")

    def part_02(self) -> None:
        """Solve Part 02 of the problem.

        Returns:
            None
        """
        seen: set[int] = set()

        frequency: int = 0
        for value in itertools.cycle(self.data):
            if frequency in seen:
                break

            seen.add(frequency)
            frequency += value

        print(f"Part 02: {frequency}")


if __name__ == "__main__":
    sol: Solution = Solution.parse_input()

    print(Timing(timeit(sol.part_01, number=1)).result(), "\n")
    print(Timing(timeit(sol.part_02, number=1)).result(), "\n")
