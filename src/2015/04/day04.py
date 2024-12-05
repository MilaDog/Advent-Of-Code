from hashlib import md5
from itertools import count
from timeit import timeit

from common.python.timing import Timing


class Solution:
    def __init__(self, data: str) -> None:
        self.data: str = data

    @classmethod
    def parse_input(cls) -> "Solution":
        """
        Parse the problem data input to be used.

        Returns:
            Solution:
                Class instance with the parsed input data.
        """
        with open("input.txt", "r") as file:
            value: str = file.read().strip()

        return cls(data=value)

    def decrypt(self, check: str) -> int:
        """
        Solve the hash and return the found value. Returns -1 if value cannot be found.

        Args:
            check (str):
                How many leading `0` to account for.

        Returns:
            int:
                Determined value.
        """
        for x in count(1):
            c = md5((self.data + str(x)).encode()).hexdigest()
            if c[:5] == check or c[:6] == check:
                return x

        return -1

    def part_01(self) -> None:
        """
        Solve Part 01 of the problem.

        Returns:
            None
        """
        tlt: int = self.decrypt(check="00000")
        print(f"Part 01: {tlt}")

    def part_02(self) -> None:
        """
        Solve Part 02 of the problem.

        Returns:
            None
        """
        tlt: int = self.decrypt(check="000000")
        print(f"Part 02: {tlt}")


if __name__ == "__main__":
    sol: Solution = Solution.parse_input()

    print(Timing(timeit(sol.part_01, number=1)).result(), "\n")
    print(Timing(timeit(sol.part_02, number=1)).result(), "\n")
