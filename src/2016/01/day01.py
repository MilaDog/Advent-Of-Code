from timeit import timeit

from timing import Timing


class Solution:
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
            values: list[tuple[str, int]] = [(action[0], int(action[1:])) for action in file.read().split(", ")]

        return cls(data=values)

    def move(self, position: tuple[int, int], direction: int, distance: int) -> tuple[int, int]:
        """Move the bunny in the given direction by the given distance.

        Args:
            position (tuple[int, int]):
                Current position of the bunny.
            direction (int):
                Facing direction of the bunny.
            distance (int):
                How much to move the bunny by.

        Returns:
            tuple[int, int]:
                New bunny position.
        """
        FACTORS: list[tuple[int, int]] = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        return position[0] + (FACTORS[direction][0] * distance), position[1] + (FACTORS[direction][1] * distance)

    def part_01(self) -> None:
        """Solve Part 01 of the problem.

        Returns:
            None
        """
        start: tuple[int, int] = (0, 0)
        facing: int = 0

        # Direction: NESW -> 0123
        for direction, distance in self.data:
            facing = (facing + 1) % 4 if direction == "R" else (facing - 1) % 4
            start = self.move(start, facing, distance)

        tlt: int = abs(start[0]) + abs(start[1])
        print(f"Part 01: {tlt}")

    def part_02(self) -> None:
        """Solve Part 02 of the problem.

        Returns:
            None
        """
        start: tuple[int, int] = (0, 0)
        facing: int = 0
        seen: set[tuple[int, int]] = set()

        # Direction: NESW -> 0123
        for direction, distance in self.data:
            facing = (facing + 1) % 4 if direction == "R" else (facing - 1) % 4

            for _ in range(distance):
                start = self.move(start, facing, 1)

                if start in seen:
                    tlt: int = abs(start[0]) + abs(start[1])
                    print(f"Part 02: {tlt}")
                    return

                seen.add(start)

        print("NOPE")


if __name__ == "__main__":
    sol: Solution = Solution.parse_input()

    print(Timing(timeit(sol.part_01, number=1)).result(), "\n")
    print(Timing(timeit(sol.part_02, number=1)).result(), "\n")
