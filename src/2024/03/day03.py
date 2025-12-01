import re
from timeit import timeit

from timing import Timing


class Solution:
    """Solutions to the problems."""

    def __init__(self, data: str) -> None:
        self.data: str = data

    @classmethod
    def parse_input(cls) -> "Solution":
        """Parse the problem data input to be used.

        Returns:
            Solution:
                Class instance with the parsed input data.
        """
        with open("input.txt", "r") as file:
            values: str = file.read().strip()

        return cls(data=values)

    def part_01(self) -> None:
        """Solve Part 01 of the problem.

        Returns:
            None
        """
        tlt: int = 0

        for match in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", self.data):
            x: int = int(match[0])
            y: int = int(match[1])

            tlt += x * y

        print(f"Part 01: {tlt}")

    def part_02(self) -> None:
        """Solve Part 02 of the problem.

        Returns:
            None
        """
        tlt: int = 0

        multiply: bool = True
        for do, dont, x, y in re.findall(r"(do)\(\)|(don't)\(\)|mul\((\d{1,3}),(\d{1,3})\)", self.data):
            if do or dont:
                multiply = True if do else False

            elif multiply:
                tlt += int(x) * int(y)

        print(f"Part 02: {tlt}")


if __name__ == "__main__":
    sol: Solution = Solution.parse_input()

    print(Timing(timeit(sol.part_01, number=1)).result(), "\n")
    print(Timing(timeit(sol.part_02, number=1)).result(), "\n")
