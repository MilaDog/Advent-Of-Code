from timeit import timeit

from common.python.timing import Timing


class Solution:
    def __init__(self, data: list[int]) -> None:
        self.data: list[int] = data

    @classmethod
    def parse_input(cls) -> "Solution":
        """
        Parse the problem data input to be used.

        Returns:
            Solution:
                Class instance with the parsed input data.
        """
        with open("input.txt", "r") as file:
            values: list[int] = [int(line.strip()) for line in file.readlines()]

        return cls(data=values)

    def part_01(self) -> None:
        """
        Solve Part 01 of the problem.

        Returns:
            None
        """
        tlt: int = sum(self.data)
        print(f"Part 01: {tlt}")

    def part_02(self) -> None:
        """
        Solve Part 02 of the problem.

        Returns:
            None
        """
        seen: set[int] = set()

        index: int = 0
        frequency: int = 0
        while frequency not in seen:
            seen.add(frequency)
            frequency += self.data[index]
            index = (index + 1) % len(self.data)

        print(f"Part 02: {frequency}")


if __name__ == "__main__":
    sol: Solution = Solution.parse_input()

    print(Timing(timeit(sol.part_01, number=1)).result(), "\n")
    print(Timing(timeit(sol.part_02, number=1)).result(), "\n")
