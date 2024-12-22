from collections import defaultdict
from functools import cache
from itertools import pairwise
from timeit import timeit
from typing import Generator

from src.common.python.timing import Timing


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
    def __generate_secret_number(self, number: int) -> int:
        """Convert the given secret number into the next secret number.

        Args:
            number (int):
                Secret number to be converted.

        Returns:
            int:
                New converted secret number.

        """
        number = ((number << 6) ^ number) % 16777216
        number = ((number >> 5) ^ number) % 16777216
        number = ((number << 11) ^ number) % 16777216
        return number

    def get_secret_numbers(self, number: int) -> Generator[int, None, None]:
        """Generate the needed secret numbers.

        Args:
            number (int):
                Initial secret number.

        Returns:
            int:
                Created secret number.
        """
        for _ in range(2000):
            number = self.__generate_secret_number(number=number)
            yield number

    def get_number_last_digit(self, numbers: list[int]) -> list[int]:
        """Get the singles unit of the secret numbers, for each generated secret number.

        Args:
            numbers (list[int]):
                List of all secret numbers.

        Returns:
            list[int]:
                Single's unit of all secret numbers.
        """
        return [number % 10 for number in numbers]

    def get_differences(self, values: list[int]) -> tuple[int, ...]:
        """Get the price differences between selling values.

        Args:
            values (list[int]):
                All selling values.

        Returns:
            list[int]:
                Price difference between these values.
        """
        return tuple(b - a for a, b in pairwise(values))

    def solve(self) -> None:
        """Solve Part 01 and Part 02 of the problem.

        Returns:
            None
        """
        tlt1: int = 0

        results: dict[tuple[int, ...], int] = defaultdict(int)
        for number in self.data:
            secret_numbers: list[int] = [*self.get_secret_numbers(number=number)]
            tlt1 += secret_numbers[-1]

            last_digits: list[int] = self.get_number_last_digit(numbers=secret_numbers)

            seen: set[tuple[int, ...]] = set()
            for i in range(len(last_digits) - 4):
                values: list[int] = last_digits[i : i + 5]
                differences: tuple[int, ...] = self.get_differences(values=values)

                if differences not in seen:
                    seen.add(differences)
                    results[differences] += values[-1]

        tlt2: int = max(results.values())

        print(f"Part 01: {tlt1}")
        print(f"Part 02: {tlt2}")


if __name__ == "__main__":
    sol: Solution = Solution.parse_input()

    print(Timing(timeit(sol.solve, number=1)).result(), "\n")
