from timeit import timeit

from common.python.timing import Timing


class Solution:
    def __init__(self, data: list[list[int]]) -> None:
        self.data: list[list[int]] = data

    @classmethod
    def parse_input(cls) -> "Solution":
        """
        Parse the problem data input to be used.

        Returns:
            Solution:
                Class instance with the parsed input data.
        """
        with open("input.txt", "r") as file:
            values: list[list[int]] = [
                list(map(int, line.split(" "))) for line in file.readlines()
            ]

        return cls(data=values)

    def check_if_safe(self, report: list[int]) -> bool:
        """
        Check if the given report is valid. Ensures that the following are met:
        1) Report has levels either all increasing or decreasing
        2) Adjacent levels differ at least by one and at most by three.

        Args:
            report (list[int]):
                Report to check.

        Returns:
            bool:
                If the report is valid or not.

        """
        # Check increasing/decreasing state
        if all([report[i - 1] < report[i] for i in range(1, len(report))]) or all(
            [report[i - 1] > report[i] for i in range(1, len(report))]
        ):
            # Check if adjacent numbers differ min 1 max 3
            if all(
                [
                    1 <= abs(report[i - 1] - report[i]) <= 3
                    for i in range(1, len(report))
                ]
            ):
                return True

        return False

    def can_fix_report(self, report: list[int]) -> bool:
        """
        Attempts to fix the given report by removing a single level at a time to see if that makes it valid.

        Args:
            report (list[int]):
                Report to try and fix.

        Returns:
            bool:
                If the given report can be fixed.
        """
        for i in range(len(report)):
            if self.check_if_safe(report[:i] + report[i + 1 :]):
                return True

        return False

    def part_01(self) -> None:
        """
        Solve Part 01 of the problem.

        Returns:
            None
        """
        tlt: int = 0

        for report in self.data:
            # Check increasing/decreasing state
            if all([report[i - 1] < report[i] for i in range(1, len(report))]) or all(
                [report[i - 1] > report[i] for i in range(1, len(report))]
            ):
                # Check if adjacent numbers differ min 1 max 3
                if all(
                    [
                        1 <= abs(report[i - 1] - report[i]) <= 3
                        for i in range(1, len(report))
                    ]
                ):
                    tlt += 1

        print(f"Part 01: {tlt}")

    def part_02(self) -> None:
        """
        Solve Part 02 of the problem.

        Returns:
            None
        """
        tlt: int = 0

        for report in self.data:
            tlt += self.can_fix_report(report)

        print(f"Part 02: {tlt}")


if __name__ == "__main__":
    sol: Solution = Solution.parse_input()

    print(Timing(timeit(sol.part_01, number=1)).result(), "\n")
    print(Timing(timeit(sol.part_02, number=1)).result(), "\n")
