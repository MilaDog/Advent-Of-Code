from timeit import timeit

from common.python.timing import Timing


class Solution:
    def __init__(self, data: list[str]) -> None:
        self.data: list[str] = data
        self.factors: list[tuple[int, int]] = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        self.__values: list[list[int]] = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.__values2: list[list[str]] = [
            [".", ".", "1", ".", "."],
            [".", "2", "3", "4", "."],
            ["5", "6", "7", "8", "9"],
            [".", "A", "B", "C", "."],
            [".", ".", "D", ".", "."],
        ]

    @classmethod
    def parse_input(cls) -> "Solution":
        """
        Parse the problem data input to be used.

        Returns:
            Solution:
                Class instance with the parsed input data.
        """
        with open("input.txt", "r") as file:
            values: list[str] = [line.strip() for line in file.readlines()]

        return cls(data=values)

    def move(
        self, position: tuple[int, int], direction: int, *, part_2: bool = False
    ) -> tuple[int, int]:
        """
        Move to a new position.

        Args:
            position (tuple[int, int]):
                Current position.
            direction (int):
                Direction to move in.
            part_2 (bool):
                Whether to solve for part 2

        Returns:
            tuple[int, int]:
                New position.
        """

        if not part_2:
            dx: int = position[0] + self.factors[direction][0]
            dy: int = position[1] + self.factors[direction][1]

            if dx < 0 or dy < 0:
                return max(position[0], dx), max(position[1], dy)
            elif dx > 2 or dy > 2:
                return min(position[0], dx), min(position[1], dy)
            return dx, dy

        # Part 2
        dx: int = position[0] + self.factors[direction][0]
        dy: int = position[1] + self.factors[direction][1]

        if dx < 0 or dy < 0:
            return max(position[0], dx), max(position[1], dy)
        elif dx > 4 or dy > 4:
            return min(position[0], dx), min(position[1], dy)

        if self.__values2[dx][dy] == ".":
            return position

        return dx, dy

    def get_value(self, position: tuple[int, int], *, part_2: bool = False) -> str:
        """
        Get the corresponding digit on the number pad for the given position.

        Args:
            position (tuple[int, int]):
                Position on the number pad, relative to the center '5'.
            part_2 (bool):
                Whether to solve for part 2

        Returns:
            str:
                Target digit.

        """
        if not part_2:
            return str(self.__values[position[0]][position[1]])
        return self.__values2[position[0]][position[1]]

    def part_01(self) -> None:
        """
        Solve Part 01 of the problem.

        Returns:
            None
        """
        start: tuple[int, int] = (1, 1)
        res: str = ""

        for line in self.data:
            for action in line:
                direction: int = "URDL".index(action)
                start = self.move(start, direction)

            res += self.get_value(start)

        print(f"Part 01: {res}")

    def part_02(self) -> None:
        """
        Solve Part 02 of the problem.

        Returns:
            None
        """
        start: tuple[int, int] = (2, 0)
        res: str = ""

        for line in self.data:
            for action in line:
                direction: int = "URDL".index(action)
                start = self.move(start, direction, part_2=True)

            res += self.get_value(start, part_2=True)

        print(f"Part 02: {res}")


if __name__ == "__main__":
    sol: Solution = Solution.parse_input()

    print(Timing(timeit(sol.part_01, number=1)).result(), "\n")
    print(Timing(timeit(sol.part_02, number=1)).result(), "\n")
