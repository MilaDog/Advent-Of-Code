import os
from pathlib import Path
from timeit import timeit

from src.timing import Timing


class Solution:
    """Solutions to the problems."""

    def __init__(self, data: list[list[str]]) -> None:
        self.data: list[list[str]] = data

    @classmethod
    def parse_input(cls) -> "Solution":
        """Parse the problem data input to be used.

        Returns:
            Solution:
                Class instance with the parsed input data.
        """
        with open(os.path.join(Path(__file__).resolve().parent, "input.txt"), "r") as file:
            values: list[list[str]] = [list(line.strip()) for line in file.readlines()]

        return cls(data=values)

    def part_01_old(self) -> None:
        """Old version making use of a two-pointer method to determine the largest number in the given code.

        Returns:
            None
        """
        tlt: int = 0

        for line in self.data:
            ptr1: int = 0

            lngth: int = len(line)
            largest: int = 0

            while ptr1 <= lngth - 2:
                ptr2: int = ptr1 + 1

                while ptr2 <= lngth - 1:
                    val: int = int(line[ptr1] + line[ptr2])

                    if val > largest:
                        largest = val

                    ptr2 += 1

                ptr1 += 1

            tlt += largest

        print(f"Part 01 [OLD]: {tlt}")

    def get_largest_k_digits(self, values: list[str], k: int) -> str:
        """Greedy algorithm that considers the largest following digit to consider. Takes that digit, ignoring the
        rest, constructing a final number being that of the largest possible number of given length `k`.

        Args:
            values (list[str]): Digits in number to consider.
            k (int): Number of digits to consider.

        Returns:
            str: Greedily found largest number.
        """
        lngth: int = len(values)

        res: list[str] = []
        ptr: int = 0

        for i in range(k):
            needed_digits: int = k - i - 1
            look_ahead_end: int = lngth - needed_digits

            max_digit: str = max(values[ptr:look_ahead_end])
            max_index: int = values.index(max_digit, ptr)

            res.append(max_digit)
            ptr = max_index + 1

        return "".join(res)

    def part_01(self) -> None:
        """Solve Part 01 of the problem.

        Returns:
            None
        """
        tlt: int = 0

        for line in self.data:
            tlt += int(self.get_largest_k_digits(values=line, k=2))
        print(f"Part 01: {tlt}")

    def part_02(self) -> None:
        """Solve Part 02 of the problem.

        Returns:
            None
        """
        tlt: int = 0

        for line in self.data:
            tlt += int(self.get_largest_k_digits(values=line, k=12))

        print(f"Part 02: {tlt}")


if __name__ == "__main__":
    sol: Solution = Solution.parse_input()

    print(Timing(timeit(sol.part_01_old, number=1)).result(), "\n")
    print(Timing(timeit(sol.part_01, number=1)).result(), "\n")
    print(Timing(timeit(sol.part_02, number=1)).result(), "\n")
