from copy import deepcopy
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

    def solve(self, data: list[int], part02: bool = False) -> int:
        tlt: int = 0
        pos: int = 0

        while True:
            if not 0 <= pos < len(data):
                break

            val: int = data[pos]

            if part02:
                data[pos] += -1 if val >= 3 else 1
            else:
                data[pos] += 1

            pos += val
            tlt += 1

        return tlt

    def part_01(self) -> None:
        """Solve Part 01 of the problem.

        Returns:
            None
        """
        tlt: int = self.solve(data=deepcopy(self.data))
        print(f"Part 01: {tlt}")

    def part_02(self) -> None:
        """Solve Part 02 of the problem.

        Returns:
            None
        """
        tlt: int = self.solve(data=deepcopy(self.data), part02=True)
        print(f"Part 02: {tlt}")


if __name__ == "__main__":
    sol: Solution = Solution.parse_input()

    print(Timing(timeit(sol.part_01, number=1)).result(), "\n")
    print(Timing(timeit(sol.part_02, number=1)).result(), "\n")
