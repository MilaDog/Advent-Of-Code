from timeit import timeit

from timing import Timing


class Solution:
    def __init__(self, data: str) -> None:
        self.data: str = data

    @classmethod
    def parse_input(cls) -> "Solution":
        """Parse the problem data input to be used.

        Returns:
            Solution:
                Class instance with the parsed input data.
        """
        with open("input.txt", "r") as file:
            value: str = file.read().strip()

        return cls(data=value)

    def transform(self, value: str) -> str:
        """Transform the data into desired form.
        With the given value, make copy and reverse. Replace all 1s with 0s and 0s with 1s.
        Return original value and transformed values joined with `0`.

        Args:
            value (str):
                Value to transform.

        Returns:
            str:
                Transformed value.
        """
        translate_table: dict[int, int] = str.maketrans("10", "01")

        modified: str = value[::-1].translate(translate_table)
        return value + "0" + modified

    def calculate_checksum(self, value: str) -> str:
        """Determine the checksum for the given value.
        If calculated checksum's length is even, calculate again with the newly calculated value.
        Else, return.

        Args:
            value (str):
                Value to have checksum calculated from.

        Returns:
            str:
                Determined checksum.
        """
        checksum: list[str] = []

        for a, b in zip(value[::2], value[1::2]):  # faster than using regex to get the pairs
            checksum.append(str(int(a == b)))

        if len(checksum) % 2 == 0:
            return self.calculate_checksum("".join(checksum))
        return "".join(checksum)

    def part_01(self) -> None:
        """Solve Part 01 of the problem.

        Returns:
            None
        """
        initial_state: str = self.data
        length = 272

        while len(initial_state) < length:
            initial_state = self.transform(initial_state)

        res: str = self.calculate_checksum(initial_state[:length])
        print(f"Part 01: {res}")

    def part_02(self) -> None:
        """Solve Part 02 of the problem.

        Returns:
            None
        """
        initial_state: str = self.data
        length = 35651584

        while len(initial_state) < length:
            initial_state = self.transform(initial_state)

        res: str = self.calculate_checksum(initial_state[:length])
        print(f"Part 02: {res}")


if __name__ == "__main__":
    sol: Solution = Solution.parse_input()

    print(Timing(timeit(sol.part_01, number=1)).result(), "\n")
    print(Timing(timeit(sol.part_02, number=1)).result(), "\n")
