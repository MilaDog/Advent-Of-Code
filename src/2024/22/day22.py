from collections import defaultdict
from functools import cache
from itertools import pairwise
from timeit import timeit

from timing import Timing


class Solution:
    """Solutions to the problems."""

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
            values: list[int] = [int(x.strip()) for x in file.readlines()]

        return cls(data=values)

    @cache
    def generate_secret_number(self, number: int) -> int:
        """Convert the given secret number into the next secret number.

        Args:
            number (int):
                Secret number to be converted.

        Returns:
            int:
                New converted secret number.

        """
        number = ((number << 6) ^ number) & 0xFFFFFF
        number = ((number >> 5) ^ number) & 0xFFFFFF
        number = ((number << 11) ^ number) & 0xFFFFFF
        return number

    def solve(self) -> None:
        """Solve Part 01 and Part 02 of the problem.

        Returns:
            None
        """
        tlt1: int = 0
        results: dict[tuple[int, ...], int] = defaultdict(int)

        for number in self.data:
            secret_numbers: list[int] = [number] + [
                number := self.generate_secret_number(number=number) for _ in range(2000)
            ]
            tlt1 += secret_numbers[-1]

            differences: list[int] = [b % 10 - a % 10 for a, b in pairwise(secret_numbers)]

            seen: set[tuple[int, ...]] = set()
            for i in range(len(secret_numbers) - 4):
                section: tuple[int, ...] = tuple(differences[i : i + 4])
                if section not in seen:
                    seen.add(section)
                    results[section] += secret_numbers[i + 4] % 10

        tlt2: int = max(results.values())

        print(f"Part 01: {tlt1}")
        print(f"Part 02: {tlt2}")


if __name__ == "__main__":
    sol: Solution = Solution.parse_input()

    print(Timing(timeit(sol.solve, number=1)).result(), "\n")
