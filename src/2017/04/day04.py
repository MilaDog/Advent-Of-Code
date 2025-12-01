from timeit import timeit

from timing import Timing


class Solution:
    def __init__(self, data: list[list[str]]) -> None:
        self.passphrases: list[list[str]] = data

    @classmethod
    def parse_input(cls) -> "Solution":
        """Parse the problem data input to be used.

        Returns:
            Solution:
                Class instance with the parsed input data.
        """
        with open("input.txt", "r") as file:
            values: list[list[str]] = [line.strip().split(" ") for line in file.readlines()]

        return cls(data=values)

    def part_01(self) -> None:
        """Solve Part 01 of the problem.

        Returns:
            None
        """
        tlt: int = sum(len(set(passphrase)) == len(passphrase) for passphrase in self.passphrases)
        print(f"Part 01: {tlt}")

    def part_02(self) -> None:
        """Solve Part 02 of the problem.

        Returns:
            None
        """
        tlt: int = 0

        for passphrase in self.passphrases:
            sorted_passphrase: list[str] = ["".join(sorted(value)) for value in passphrase]
            tlt += len(set(sorted_passphrase)) == len(sorted_passphrase)

        print(f"Part 02: {tlt}")


if __name__ == "__main__":
    sol: Solution = Solution.parse_input()

    print(Timing(timeit(sol.part_01, number=1)).result(), "\n")
    print(Timing(timeit(sol.part_02, number=1)).result(), "\n")
