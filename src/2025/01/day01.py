from timeit import timeit

from src.timing import Timing


class Solution:
    """Solutions to the problems."""

    def __init__(self, data: list[tuple[str, int]]) -> None:
        self.data: list[tuple[str, int]] = data

    @classmethod
    def parse_input(cls) -> "Solution":
        """Parse the problem data input to be used.

        Returns:
            Solution:
                Class instance with the parsed input data.
        """
        with open("input.txt", "r") as file:
            values: list[tuple[str, int]] = [(line[0], int(line[1:])) for line in file.readlines()]

        return cls(data=values)

    def part_01(self) -> None:
        """Solve Part 01 of the problem.

        Returns:
            None
        """
        tlt: int = 0

        pointing: int = 50

        for action, amount in self.data:
            if action == "L":
                pointing -= amount
            else:
                pointing += amount

            pointing %= 100

            if pointing == 0:
                tlt += 1

        print(f"Part 01: {tlt}")

    def part_02(self) -> None:
        """Solve Part 02 of the problem.

        Returns:
            None
        """
        tlt: int = 0

        pointing: int = 50

        for action, amount in self.data:
            for _ in range(amount):
                if action == "L":
                    pointing = (pointing + 99) % 100
                else:
                    pointing = (pointing + 1) % 100

                if pointing == 0:
                    tlt += 1

        print(f"Part 02: {tlt}")


if __name__ == "__main__":
    sol: Solution = Solution.parse_input()

    print(Timing(timeit(sol.part_01, number=1)).result(), "\n")
    print(Timing(timeit(sol.part_02, number=1)).result(), "\n")
