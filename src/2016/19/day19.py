from timeit import timeit

from timing import Timing


class Solution:
    def __init__(self, data: int) -> None:
        self.number_elves: int = data

    @classmethod
    def parse_input(cls) -> "Solution":
        """Parse the problem data input to be used.

        Returns:
            Solution:
                Class instance with the parsed input data.
        """
        with open("input.txt", "r") as file:
            value: int = int(file.read().strip())

        return cls(data=value)

    def part_01(self) -> None:
        """Solve Part 01 of the problem.

        https://www.youtube.com/watch?v=uCsD3ZGzMgE

        Returns:
            None
        """
        tlt: int = int(str(bin(self.number_elves))[3:] + "1", 2)

        print(f"Part 01: {tlt}")

    def part_02(self) -> None:
        """Solve Part 02 of the problem.

        Returns:
            None
        """
        tlt: int = 0

        print(f"Part 02: {tlt}")


if __name__ == "__main__":
    sol: Solution = Solution.parse_input()

    print(Timing(timeit(sol.part_01, number=1)).result(), "\n")
    print(Timing(timeit(sol.part_02, number=1)).result(), "\n")
