from collections import Counter
from timeit import timeit

from common.python.timing import Timing


class Solution:
    def __init__(self, data: list[str]) -> None:
        self.data: list[str] = data

    @classmethod
    def parse_input(cls) -> "Solution":
        """
        Parse the problem data input to be used.

        Returns:
            Solution:
                Class instance with the parsed input data.
        """
        with open("input.txt", "r") as file:
            values: list[str] = [line.strip() for line in file.readlines()]

        return cls(data=values)

    def part_01(self) -> None:
        """
        Solve Part 01 of the problem.

        Returns:
            None
        """
        res: str = ""
        for message in zip(*self.data):
            c: Counter[str] = Counter(message)
            res += c.most_common(1)[0][0]

        print(f"Part 01: {res}")

    def part_02(self) -> None:
        """
        Solve Part 02 of the problem.

        Returns:
            None
        """
        res: str = ""
        for message in zip(*self.data):
            c: Counter[str] = Counter(message)
            res += sorted(c.items(), key=lambda x: x[1])[0][0]

        print(f"Part 02: {res}")


if __name__ == "__main__":
    sol: Solution = Solution.parse_input()

    print(Timing(timeit(sol.part_01, number=1)).result(), "\n")
    print(Timing(timeit(sol.part_02, number=1)).result(), "\n")
