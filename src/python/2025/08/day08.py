import math
from itertools import combinations
from timeit import timeit

from src.timing import Timing

type JunctionBox = tuple[int, ...]


class Solution:
    """Solutions to the problems."""

    def __init__(self, data: list[JunctionBox]) -> None:
        self.data: list[JunctionBox] = data

    @classmethod
    def parse_input(cls) -> "Solution":
        """Parse the problem data input to be used.

        Returns:
            Solution:
                Class instance with the parsed input data.
        """
        with open("./inputs/2025/08/input.txt", "r") as file:
            values: list[JunctionBox] = [tuple(map(int, line.strip().split(","))) for line in file.readlines()]

        return cls(data=values)

    def solve(self) -> None:
        """Solve Part 01 and 02 of the problem."""
        circuits: dict[JunctionBox, set[JunctionBox]] = {box: {box} for box in self.data}
        pairs: list[tuple[JunctionBox, JunctionBox]] = sorted(combinations(circuits, 2), key=lambda x: math.dist(*x))

        for i, (box1, box2) in enumerate(pairs):
            # Get the circuit each box belongs to
            cir1: JunctionBox = ()
            cir2: JunctionBox = ()

            for c in circuits:
                if box1 in circuits[c]:
                    cir1 = c

                if box2 in circuits[c]:
                    cir2 = c

            # different circuits, then join them
            if cir1 != cir2:
                circuits[cir1] |= circuits[cir2]
                del circuits[cir2]

            if i + 1 == 1000:
                n = sorted(len(circuits[b]) for b in circuits)
                print(f"Part 01: {n[-3] * n[-2] * n[-1]}")

            if len(circuits) == 1:
                print(f"Part 02: {box1[0] * box2[0]}")
                break


if __name__ == "__main__":
    sol: Solution = Solution.parse_input()

    print(Timing(timeit(sol.solve, number=1)).result(), "\n")
