from functools import reduce
from timeit import timeit

from src.timing import Timing


class Solution:
    """Solutions to the problems."""

    def __init__(self, data: list[str]) -> None:
        self.data: list[str] = data

    @classmethod
    def parse_input(cls) -> "Solution":
        """Parse the problem data input to be used.

        Returns:
            Solution:
                Class instance with the parsed input data.
        """
        with open("./inputs/2025/06/input.txt", "r") as file:
            values: list[str] = [line.strip("\n") for line in file.readlines()]

        return cls(data=values)

    def part_01(self) -> None:
        """Solve Part 01 of the problem."""
        tlt: int = 0

        # want to split on all white spaces, then join with a whitespace, and split again.
        # will remove multiple trailing whitespaces
        # 345  43   5 -> 345 43 5 -> [345, 43, 5]
        values: list[list[str]] = [" ".join(line.strip().split()).split() for line in self.data]

        for vals in zip(*values):
            match vals[-1]:
                case "+":
                    tlt += sum(map(int, vals[:-1]))

                case "*":
                    tlt += reduce(lambda acc, x: acc * x, map(int, vals[:-1]))

                case _:
                    assert f"Unknown match: {vals[-1]}"

        print(f"Part 01: {tlt}")

    def part_02(self) -> None:
        """Solve Part 02 of the problem."""
        tlt: int = 0

        max_len: int = max(len(line) for line in self.data)

        # padding to ensure all are same length
        lines: list[str] = [line.ljust(max_len) for line in self.data]

        # finding boundaries to split on
        boundaries: list[int] = []
        for i in range(max_len):
            if all(line[i] == " " for line in lines):
                if i > 0 and not all(line[i - 1] == " " for line in lines):
                    boundaries.append(i)
        boundaries.append(max_len)

        # splitting on boundaries
        values: list[list[str]] = []
        ptr: int = -1
        for boundary in boundaries:
            values.append([line[ptr + 1 : boundary] for line in lines])
            ptr = boundary

        for cols in values:
            match cols[-1].replace(" ", ""):
                case "+":
                    tlt += sum(map(int, ["".join(v) for v in zip(*cols[:-1])]))

                case "*":
                    tlt += reduce(lambda acc, x: acc * x, map(int, ["".join(v) for v in zip(*cols[:-1])]))

                case _:
                    assert f"Unknown match: {cols[-1]}"

        print(f"Part 02: {tlt}")


if __name__ == "__main__":
    sol: Solution = Solution.parse_input()

    print(Timing(timeit(sol.part_01, number=1)).result(), "\n")
    print(Timing(timeit(sol.part_02, number=1)).result(), "\n")
