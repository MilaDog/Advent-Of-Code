import re
from collections import defaultdict
from timeit import timeit
from typing import List, Tuple, Dict

from common.python.timing import Timing


class Solution:
    def __init__(self, data: List[Tuple[str, List[int]]]) -> None:
        self.data: List[Tuple[str, List[int]]] = data

    @classmethod
    def parse_input(cls) -> "Solution":
        """
        Parse the problem data input to be used.

        Returns:
            Solution:
                Class instance with the parsed input data.
        """
        instructions: List[Tuple[str, List[int]]] = []

        with open("input.txt", "r") as file:
            for line in file.readlines():
                instruction: str = re.findall("turn on|turn off|toggle", line)[0]
                positions: List[int] = list(map(int, re.findall(r"\d{1,3}", line)))

                instructions.append((instruction, positions))

        return cls(data=instructions)

    def part_01(self) -> None:
        """
        Solve Part 01 of the problem.

        Returns:
            None
        """
        coords: Dict[Tuple[int, int], bool] = defaultdict()

        for action in self.data:
            instruction: str = action[0]
            start_x, start_y, end_x, end_y = action[1]

            for x in range(start_x, end_x + 1):
                for y in range(start_y, end_y + 1):
                    pos: Tuple[int, int] = (x, y)

                    match instruction:
                        case "turn on":
                            coords[pos] = True

                        case "turn off":
                            coords[pos] = False

                        case "toggle":
                            if coords.get(pos):
                                coords[pos] = not coords[pos]

                            else:
                                coords[pos] = True

        tlt: int = sum(coords.values())
        print(f"Part 01: {tlt}")

    def part_02(self) -> None:
        """
        Solve Part 02 of the problem.

        Returns:
            None
        """
        brightness: Dict[Tuple[int, int], int] = defaultdict()

        for action in self.data:
            instruction: str = action[0]
            start_x, start_y, end_x, end_y = action[1]

            for x in range(start_x, end_x + 1):
                for y in range(start_y, end_y + 1):
                    pos: Tuple[int, int] = (x, y)

                    if not brightness.get(pos):
                        brightness[pos] = 0

                    match instruction:
                        case "turn on":
                            brightness[pos] += 1

                        case "turn off":
                            if brightness[pos] < 1:
                                continue

                            brightness[pos] -= 1

                        case "toggle":
                            brightness[pos] += 2

        tlt: int = sum(brightness.values())

        print(f"Part 02: {tlt}")


if __name__ == "__main__":
    sol: Solution = Solution.parse_input()

    print(Timing(timeit(sol.part_01, number=1)).result(), "\n")
    print(Timing(timeit(sol.part_02, number=1)).result(), "\n")
