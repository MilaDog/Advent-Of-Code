from collections import Counter
from timeit import timeit

from timing import Timing


class Solution:
    """Solutions to the problems."""

    def __init__(self, codes: list[str]) -> None:
        self.codes: list[str] = codes

    @classmethod
    def parse_input(cls) -> "Solution":
        """Parse the problem codes input to be used.

        Returns:
            Solution:
                Class instance with the parsed input codes.
        """
        with open("input.txt", "r") as file:
            values: list[str] = [code.strip() for code in file.readlines()]

        return cls(codes=values)

    @staticmethod
    def numberpad() -> dict[str, tuple[int, int]]:
        """Mapping for the numberpad.

        Returns:
            dict[str, tuple[int, int]]:
                Numberpad mapping.
        """
        return {val: (i % 3, i // 3) for i, val in enumerate("789456123 0A")}

    @staticmethod
    def keypad() -> dict[str, tuple[int, int]]:
        """Mapping for the directional keypad.

        Returns:
            dict[str, tuple[int, int]]:
                Directional keypad mapping.
        """
        return {val: (i % 3, i // 3) for i, val in enumerate(" ^A<v>")}

    def get_path(
        self, mapping: dict[str, tuple[int, int]], path: str, step_count: int = 1
    ) -> Counter[tuple[int, int, bool]]:
        """Compute the path taken on the keypad/numberpad.

        Args:
            mapping (dict[str, tuple[int, int]]):
                Type of pad being used.
            path (str):
                Path taken to convert into new path.
            step_count (int):
                Increase amount.

        Returns:
            Counter[tuple[int, int, bool]]:
                All paths taken, and whether they crossed an empty block or not.
        """
        start_x, start_y = mapping["A"]
        gap_x, gap_y = mapping[" "]

        movements: Counter[tuple[int, int, bool]] = Counter()

        for action in path:
            x, y = mapping[action]
            new_x, new_y = x - start_x, y - start_y

            # If the path goes through the gap, reverse that path
            entered_gap: bool = (gap_x == x and gap_y == start_y) or (gap_y == y and gap_x == start_x)

            movements[(new_x, new_y, entered_gap)] += step_count
            start_x, start_y = x, y

        return movements

    def solve(self, count: int) -> int:
        """Solve Part 01 and Part 02 of the problem.

        Returns:
            None
        """
        tlt: int = 0
        for code in self.codes:
            res: Counter[tuple[int, int, bool]] = self.get_path(mapping=Solution.numberpad(), path=code)

            for _ in range(count + 1):
                new_res: Counter[tuple[int, int, bool]] = Counter()

                for (x, y, rev), i in res.items():
                    path: str = f"{"<" * -x}{"v" * y}{"^" * -y}{">" * x}"[:: -1 if rev else 1] + "A"
                    new_res.update(self.get_path(mapping=Solution.keypad(), path=path, step_count=i))

                res = new_res

            tlt += int(code[:-1]) * res.total()

        return tlt

    def main(self) -> None:
        """Enter point for the problem.

        Returns:
            None
        """
        print(f"Part 01: {self.solve(count=2)}")
        print(f"Part 02: {self.solve(count=25)}")


if __name__ == "__main__":
    sol: Solution = Solution.parse_input()

    print(Timing(timeit(sol.main, number=1)).result(), "\n")
