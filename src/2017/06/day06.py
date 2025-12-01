import re
from collections import defaultdict
from copy import deepcopy
from itertools import cycle, islice
from timeit import timeit

from timing import Timing


class Solution:
    def __init__(self, data: list[int]) -> None:
        self.banks: list[int] = data

    @classmethod
    def parse_input(cls) -> "Solution":
        """Parse the problem data input to be used.

        Returns:
            Solution:
                Class instance with the parsed input data.
        """
        with open("input.txt", "r") as file:
            values: list[int] = [int(x) for x in re.findall(r"(\d+)", file.read().strip())]

        return cls(data=values)

    def solve(self) -> None:
        """Solve Part 01 and 02 of the problem.

        Returns:
            None
        """
        banks: list[int] = deepcopy(self.banks)
        seen: dict[tuple[int, ...], int] = defaultdict(int)

        while tuple(banks) not in seen:
            seen[tuple(banks)] = len(seen)

            i: int
            val: int
            i, val = max(enumerate(banks), key=lambda k: (k[1], -k[0]))
            banks[i] = 0

            for j in islice(cycle(range(len(banks))), i + 1, i + val + 1):
                banks[j] += 1

        print(f"Part 01: {len(seen)}")
        print(f"Part 02: {len(seen) - seen[tuple(banks)]}")


if __name__ == "__main__":
    sol: Solution = Solution.parse_input()

    print(Timing(timeit(sol.solve, number=1)).result(), "\n")
