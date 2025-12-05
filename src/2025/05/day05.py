from pathlib import Path
from timeit import timeit

from src.timing import Timing


class Solution:
    """Solutions to the problems."""

    def __init__(self, id_ranges: list[tuple[int, int]], ids: list[int]) -> None:
        self.id_ranges: list[tuple[int, int]] = id_ranges
        self.ids: list[int] = ids

    @classmethod
    def parse_input(cls) -> "Solution":
        """Parse the problem data input to be used.

        Returns:
            Solution:
                Class instance with the parsed input data.
        """
        id_ranges: list[tuple[int, int]] = []
        ids: list[int] = []

        with open(Path(__file__).resolve().parent / "input.txt", "r") as file:
            p1, p2 = file.read().strip().split("\n\n")

            for r in p1.strip().splitlines():
                start, end = r.strip().split("-")
                id_ranges.append((int(start), int(end)))

            ids = [int(i) for i in p2.strip().splitlines()]

        return cls(id_ranges=id_ranges, ids=ids)

    def part_01(self) -> None:
        """Solve Part 01 of the problem."""
        tlt: int = 0

        for id_ in self.ids:
            fresh: bool = False

            for start, end in self.id_ranges:
                if start <= id_ <= end:
                    fresh = True
                    break

            if fresh:
                tlt += 1

        print(f"Part 01: {tlt}")

    def part_02(self) -> None:
        """Solve Part 02 of the problem."""
        tlt: int = 0

        curr: int = -1
        for start, end in sorted(self.id_ranges):
            # Has the range start been considered already. If so, start after it
            if curr >= start:
                start = curr + 1

            # Add unseen values to total
            if start <= end:
                tlt += end - start + 1

            curr = max(curr, end)

        print(f"Part 02: {tlt}")


if __name__ == "__main__":
    sol: Solution = Solution.parse_input()

    print(Timing(timeit(sol.part_01, number=1)).result(), "\n")
    print(Timing(timeit(sol.part_02, number=1)).result(), "\n")
