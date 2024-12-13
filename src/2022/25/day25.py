from timeit import timeit

from src.common.python.timing import Timing


class Solution:
    """Solutions to the problems."""

    def __init__(self, data: list[list[str]]) -> None:
        self.snafus: list[list[str]] = data

    @classmethod
    def parse_input(cls) -> "Solution":
        """Parse the problem data input to be used.

        Returns:
            Solution:
                Class instance with the parsed input data.
        """
        with open("input.txt", "r") as file:
            values: list[list[str]] = [list(line.strip()) for line in file.readlines()]

        return cls(data=values)

    def snafu_to_decimal(self, snafu: list[str]) -> int:
        """Convert the given SNAFU value into decimal form.

        Args:
            snafu (list[str]):
                SNAFU to convert.

        Returns:
            int:
                Decimal value of the given SNAFU.
        """
        if snafu:
            *rest, last = snafu
            return self.snafu_to_decimal(rest) * 5 + "=-012".find(last) - 2
        return 0

    def decimal_to_snafu(self, value: int) -> str:
        """Convert the given decimal value into SNAFU.

        Args:
            value (int):
                Decimal value to convert into SNAFU.

        Returns:
            str:
                Converted SNAFU value.
        """
        if value:
            quo, rem = divmod(value + 2, 5)
            return self.decimal_to_snafu(quo) + "=-012"[rem]
        return ""

    def part_01(self) -> None:
        """Solve Part 01 of the problem.

        Returns:
            None
        """
        tlt: int = sum(map(self.snafu_to_decimal, self.snafus))
        res: str = self.decimal_to_snafu(tlt)
        print(f"Method 01:\nPart 01: {res}")

        # Another Method
        print()
        tlt: int = 0
        snafu_map: dict[str, int] = {"=": -2, "-": -1, "1": 1, "2": 2, "0": 0}

        for snafu in self.snafus:
            t: int = 0
            for i, chrr in enumerate(snafu[::-1]):
                t += (5**i) * snafu_map[chrr]

            tlt += t

        res: str = ""

        while tlt:
            quo, rem = divmod(tlt + 2, 5)
            res += "=-012"[rem]
            tlt = quo

        print(f"Method 02: \nPart 01: {res[::-1]}")


if __name__ == "__main__":
    sol: Solution = Solution.parse_input()

    print(Timing(timeit(sol.part_01, number=1)).result(), "\n")
