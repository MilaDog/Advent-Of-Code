from collections import deque
from timeit import timeit
from typing import Deque

from src.timing import Timing


class Solution:
    """Solutions to the problems.

    Credit: https://www.reddit.com/r/adventofcode/comments/1pgnmou/2025_day_7_lets_visualize/ for helping with the
    understanding of P2
    """

    def __init__(self, data: dict[complex, str], start: complex, size: tuple[int, int]) -> None:
        self.data: dict[complex, str] = data
        self.start: complex = start
        self.size: tuple[int, int] = size

    @classmethod
    def parse_input(cls) -> "Solution":
        """Parse the problem data input to be used.

        Returns:
            Solution:
                Class instance with the parsed input data.
        """
        data: dict[complex, str] = dict()
        start: complex = 0
        size: tuple[int, int]

        with open("./inputs/2025/07/input.txt", "r") as file:
            lines: list[str] = file.readlines()
            size = (len(lines), len(lines[0]))

            for r, line in enumerate(lines):
                for c, v in enumerate(line.strip()):
                    if v == "S":
                        start = complex(r, c)

                    data[complex(r, c)] = v

        return cls(data=data, start=start, size=size)

    def part_01(self) -> None:
        """Solve Part 01 of the problem."""
        tlt: int = 0

        q: list[complex] = [self.start]
        seen: set[complex] = set()

        while q:
            curr = q.pop()
            seen.add(curr)

            target: complex = curr + 1

            if target not in self.data.keys() or target in seen:
                continue

            match self.data[target]:
                case ".":
                    q.append(target)

                case "^":
                    tlt += 1
                    seen.add(target)
                    q.append(target - 1j)
                    q.append(target + 1j)

                case _:
                    assert f"Unknown symbol at ({target}): {self.data[target]}"

        print(f"Part 01: {tlt}")

    def part_02(self) -> None:
        """Solve Part 02 of the problem."""
        res: list[int] = [0 for _ in range(self.size[1])]
        res[int(self.start.imag)] = 1

        q: Deque[complex] = deque([self.start])
        seen: set[complex] = set()

        while q:
            curr = q.popleft()
            seen.add(curr)

            target: complex = curr + 1

            if target not in self.data.keys() or target in seen:
                continue

            match self.data[target]:
                case ".":
                    q.append(target)

                case "^":
                    seen.add(target)
                    q.append(target - 1j)
                    q.append(target + 1j)

                    res[int((target - 1j).imag)] += res[int(target.imag)]
                    res[int((target + 1j).imag)] += res[int(target.imag)]
                    res[int(target.imag)] = 0

                case _:
                    assert f"Unknown symbol at ({target}): {self.data[target]}"

        print(f"Part 02: {sum(res)}")


if __name__ == "__main__":
    sol: Solution = Solution.parse_input()

    print(Timing(timeit(sol.part_01, number=1)).result(), "\n")
    print(Timing(timeit(sol.part_02, number=1)).result(), "\n")
