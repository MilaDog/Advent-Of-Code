from collections import Counter
from timeit import timeit
from typing import List, Counter as Counter_, Tuple

from common.python.timing import Timing


class Solution:
    def __init__(self, data: List[str]) -> None:
        self.data: List[str] = data

    @classmethod
    def parse_input(cls) -> "Solution":
        """
        Parse the problem data input to be used.

        Returns:
            Solution:
                Class instance with the parsed input data.
        """
        with open("input.txt", "r") as file:
            values: List[str] = list(file.read().strip())

        return cls(data=values)

    def __update_position(self, position: Tuple[int, int], direction: str) -> Tuple[int, int]:
        """
        Update the person's current position according to the given direction.

        Args:
            position (Tuple[int, int]):
                Current person's position.
            direction (str):
                Direction to update the position in.

        Returns:
            Tuple[int, int]:
                The updated position.

        """
        x: int
        y: int
        x, y = position

        match direction:
            case "^":
                return x, y + 1

            case ">":
                return x + 1, y

            case "v":
                return x, y - 1

            case "<":
                return x - 1, y

        raise Exception("Invalid direction given.")

    def part_01(self) -> None:
        """
        Solve Part 01 of the problem.

        Returns:
            None
        """
        pos: Tuple[int, int] = (0, 0)
        cnter: Counter_[Tuple[int, int]] = Counter([pos])

        # ^>v<
        for dir in self.data:
            pos = self.__update_position(position=pos, direction=dir)
            cnter.update([pos])

        tlt: int = len(cnter.values())
        print(f"Part 01: {tlt}")

    def part_02(self) -> None:
        """
        Solve Part 02 of the problem.

        Returns:
            None
        """
        santa: Tuple[int, int] = (0, 0)
        robo: Tuple[int, int] = (0, 0)
        cnter: Counter_[Tuple[int, int]] = Counter([santa])

        # ^>v<
        for i, dir in enumerate(self.data):
            pos: Tuple[int, int] = self.__update_position(position=santa if i % 2 == 0 else robo, direction=dir)
            cnter.update([pos])

            if i % 2 == 0:
                santa = pos
            else:
                robo = pos

        tlt: int = len(cnter.values())
        print(f"Part 02: {tlt}")


if __name__ == "__main__":
    sol: Solution = Solution.parse_input()

    print(Timing(timeit(sol.part_01, number=1)).result(), "\n")
    print(Timing(timeit(sol.part_02, number=1)).result(), "\n")
