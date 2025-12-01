import re
from timeit import timeit

from timing import Timing


class Solution:
    def __init__(self, data: str) -> None:
        self.captcha: str = data

    @classmethod
    def parse_input(cls) -> "Solution":
        """Parse the problem data input to be used.

        Returns:
            Solution:
                Class instance with the parsed input data.
        """
        with open("input.txt", "r") as file:
            value: str = file.read().strip()

        return cls(data=value)

    def solve(self, amount: int) -> int:
        """Solve the captcha by finding the digits that are followed by the same digit `amount` times.
        Return the sum of each capture's repeating digit.

        Args:
            amount (int):
                Amount of repeating digits to capture.

        Returns:
            int:
                Sum of each capture's repeating digit.
        """
        # captcha + captcha[:amount] due to being circular.
        return sum(int(val) for val in re.findall(rf"(\d)(?=.{{{amount-1}}}\1)", self.captcha + self.captcha[:amount]))

    def part_01(self) -> None:
        """Solve Part 01 of the problem.

        Returns:
            None
        """
        tlt: int = self.solve(amount=1)
        print(f"Part 01: {tlt}")

    def part_02(self) -> None:
        """Solve Part 02 of the problem.

        Returns:
            None
        """
        tlt: int = self.solve(amount=len(self.captcha) // 2)
        print(f"Part 02: {tlt}")


if __name__ == "__main__":
    sol: Solution = Solution.parse_input()

    print(Timing(timeit(sol.part_01, number=1)).result(), "\n")
    print(Timing(timeit(sol.part_02, number=1)).result(), "\n")
