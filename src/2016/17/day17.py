import hashlib
from collections import deque
from itertools import compress
from timeit import timeit
from typing import Any

from common.python.timing import Timing


class Solution:
    def __init__(self, data: str) -> None:
        self.data: str = data
        self.moves: Any = {
            "U": lambda x, y: (x, y - 1),
            "D": lambda x, y: (x, y + 1),
            "L": lambda x, y: (x - 1, y),
            "R": lambda x, y: (x + 1, y),
        }

    @classmethod
    def parse_input(cls) -> "Solution":
        """
        Parse the problem data input to be used.

        Returns:
            Solution:
                Class instance with the parsed input data.
        """
        with open("input.txt", "r") as file:
            value: str = file.read().strip()

        return cls(data=value)

    def solve(self) -> None:
        """
        Solve both parts.

        Returns:
            None
        """
        # x, y and path
        position: tuple[int, int, list[str]] = (0, 0, [])
        target: tuple[int, int] = (3, 3)
        q: deque[tuple[int, int, list[str]]] = deque([position])

        part01: bool = False
        max_length: int = 0
        while q:
            x: int
            y: int
            processed_directions: list[str]
            x, y, processed_directions = q.popleft()

            hashed: str = hashlib.md5(
                f"{self.data}{''.join(processed_directions).upper()}".encode()
            ).hexdigest()
            doors: list[bool] = [int(x, 16) > 10 for x in hashed[:4]]

            for direction in compress("UDLR", doors):
                dx, dy = self.moves[direction](x, y)

                if (dx, dy) == target:
                    if not part01:
                        print(f"Part 01: {"".join(processed_directions + [direction])}")
                        part01 = True
                    max_length = len(processed_directions + [direction])

                elif 0 <= dx < 4 and 0 <= dy < 4:
                    q.append((dx, dy, processed_directions + [direction]))

                # Not in grid
                continue

        print(f"Part 02: {max_length}")


if __name__ == "__main__":
    sol: Solution = Solution.parse_input()

    print(Timing(timeit(sol.solve, number=1)).result(), "\n")
