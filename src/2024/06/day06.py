from timeit import timeit

from src.common.python.timing import Timing


class Solution:
    def __init__(
        self, data: dict[tuple[int, int], str], initial_position: tuple[int, int]
    ) -> None:
        self.data: dict[tuple[int, int], str] = data
        self.position: tuple[int, int] = initial_position

    @classmethod
    def parse_input(cls) -> "Solution":
        """
        Parse the problem data input to be used.

        Returns:
            Solution:
                Class instance with the parsed input data.
        """
        start: tuple[int, int] = (0, 0)
        with open("input.txt", "r") as file:
            values: dict[tuple[int, int], str] = dict()

            for x, row in enumerate(file.readlines()):
                for y, col in enumerate(row):
                    values[(x, y)] = col

                    if col == "^":
                        start = (x, y)

        return cls(data=values, initial_position=start)

    def part_01(self) -> None:
        """
        Solve Part 01 of the problem.

        Returns:
            None
        """
        # NESW -> 0123
        direction: int = 0
        factors: list[tuple[int, int]] = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        self.data[self.position] = "X"

        while True:
            # Move
            direction %= 4
            dx, dy = factors[direction]

            new_position: tuple[int, int] = (
                self.position[0] + dx,
                self.position[1] + dy,
            )

            # Check if in bounds
            if new_position not in self.data:
                break

            # Check if hit object
            if self.data[new_position] == "#":
                direction += 1
                continue

            # Mark area
            self.position = new_position

            if self.data[self.position] == ".":
                self.data[self.position] = "X"

        tlt: int = sum(v == "X" for v in self.data.values())

        print(f"Part 01: {tlt}")

    def part_02(self) -> None:
        """
        Solve Part 02 of the problem. 1784

        Returns:
            None
        """
        tlt: int = 0

        print(f"Part 02: {tlt}")


if __name__ == "__main__":
    sol: Solution = Solution.parse_input()

    print(Timing(timeit(sol.part_01, number=1)).result(), "\n")
    print(Timing(timeit(sol.part_02, number=1)).result(), "\n")
