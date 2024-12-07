from math import floor, log10
from timeit import timeit

from src.common.python.timing import Timing


class Solution:
    def __init__(self, data: list[list[int]]) -> None:
        self.data: list[list[int]] = data

    @classmethod
    def parse_input(cls) -> "Solution":
        """
        Parse the problem data input to be used.

        Returns:
            Solution:
                Class instance with the parsed input data.
        """
        with open("input.txt", "r") as file:
            values: list[list[int]] = [
                list(map(int, line.strip().replace(":", "").split(" ")))
                for line in file.readlines()
            ]

        return cls(data=values)

    def concat_digits(self, x: int, y: int) -> int:
        """
        Joins to integers together. Just another method as opposed to string concatenation.
        Eg: (x,y) => (23, 34) -> 2334

        Args:
            x (int):
                First integer.
            y (int):
                Second integer.

        Returns:
            int:
                Two integers joined together.
        """
        cnt: int = floor(log10(y)) + 1
        return x * 10**cnt + y

    def calculate_total(self, part02: bool = False) -> int:
        """
        Calculate the totals for valid equations.

        Args:
            part02 (bool):
                If solving for Part 02.

        Returns:
            int:
                Sum of all valid equation results.
        """
        tlt: int = 0

        for result, *parts in self.data:
            possible_results: list[int] = [parts.pop(0)]

            while parts:
                current: int = parts.pop(0)
                tmp: list[int] = []

                for p in possible_results:
                    if (r := current + p) <= result:
                        tmp.append(r)

                    if (r := current * p) <= result:
                        tmp.append(r)

                    if (r := self.concat_digits(p, current)) <= result and part02:
                        tmp.append(r)

                possible_results = tmp

            if result in possible_results:
                tlt += result

        return tlt

    def part_01(self) -> None:
        """
        Solve Part 01 of the problem.

        Returns:
            None
        """
        tlt: int = self.calculate_total()
        print(f"Part 01: {tlt}")

    def part_02(self) -> None:
        """
        Solve Part 02 of the problem.

        Returns:
            None
        """
        tlt: int = self.calculate_total(part02=True)
        print(f"Part 02: {tlt}")


if __name__ == "__main__":
    sol: Solution = Solution.parse_input()
    print(Timing(timeit(sol.part_01, number=1)).result(), "\n")
    print(Timing(timeit(sol.part_02, number=1)).result(), "\n")
