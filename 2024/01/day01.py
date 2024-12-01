import re
from collections import Counter
from timeit import timeit
from typing import Counter as Counter_
from typing import List
from typing import Tuple

from common.python.timing import Timing


class Solution:
    def __init__(self, data: Tuple[List[int], List[int]]) -> None:
        self.data: Tuple[List[int], List[int]] = data

    @classmethod
    def parse_input(cls) -> "Solution":
        """
        Parse the problem data input to be used.

        Returns:
            Solution:
                Class instance with the parsed input data.
        """
        with open("input.txt", "r") as file:
            values_left: List[int] = []
            values_right: List[int] = []

            for line in file.readlines():
                left: int
                right: int

                left, right = re.findall(r"\d+", line)
                values_left.append(int(left))
                values_right.append(int(right))

        return cls(data=(sorted(values_left), sorted(values_right)))

    def part_01(self) -> None:
        """
        Solve Part 01 of the problem.

        Returns:
            None
        """
        tlt: int = 0

        for left, right in zip(*self.data):
            tlt += abs(left - right)

        print(f"Part 01: {tlt}")

    def part_02(self) -> None:
        """
        Solve Part 02 of the problem.

        Returns:
            None
        """
        tlt: int = 0

        count: Counter_[int] = Counter(self.data[1])
        for val in self.data[0]:
            tlt += val * count.get(val, 0)

        print(f"Part 02: {tlt}")


if __name__ == "__main__":
    sol: Solution = Solution.parse_input()

    print(Timing(timeit(sol.part_01, number=1)).result(), "\n")
    print(Timing(timeit(sol.part_02, number=1)).result(), "\n")
