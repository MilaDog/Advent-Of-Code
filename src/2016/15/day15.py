import re
from timeit import timeit

from common.python.timing import Timing


class Disk:
    def __init__(self, iD: int, positions: int, current_position: int) -> None:
        self.iD: int = iD
        self.positions: int = positions
        self.current_position: int = current_position

    @classmethod
    def parse(cls, line: str) -> "Disk":
        """
        Parse the string to get the details of the Disk.

        Args:
            line (str):
                Disk line to parse.

        Returns:
            Disk:
                Class with the details of the Disk.
        """
        iD: int
        positions: int
        current_position: int
        iD, positions, _, current_position = map(int, re.findall(r"(\d+)", line))

        return cls(iD=iD, positions=positions, current_position=current_position)


class Solution:
    def __init__(self, data: list[Disk]) -> None:
        self.disks: list[Disk] = data

    @classmethod
    def parse_input(cls) -> "Solution":
        """
        Parse the problem data input to be used.

        Returns:
            Solution:
                Class instance with the parsed input data.
        """
        with open("input.txt", "r") as file:
            values: list[Disk] = [Disk.parse(line) for line in file.readlines()]

        return cls(data=values)

    def crt(self, time: int, position: int, total_positions: int) -> bool:
        """
        Using Chinese Remainder Theorem to solve when the best time to drop the capsule is.
        Valid if result is equal to 0, indicating level 0.

        So, a MOD m => X, where a -> (time + position), m -> number of positions, X -> target level 0.

        Args:
            time (int):
                Time when the capsule is dropped.
            position (int):
                Current position of the disk.
            total_positions (int):
                Number of positions that the disk can go to.

        Returns:
            bool:
                If, when dropped, disk is on level 0, thus passing through disk.
        """
        return (time + position) % total_positions == 0

    def solve(self, part02: bool = False) -> int:
        """
        Solve the given part. Find time when all disk will be on level 0.

        Args:
            part02 (bool):
                Whether to solve part 02.

        Returns:
            int:
                Time at which to drop the capsule to win.
        """
        disks: list[Disk] = self.disks if part02 else self.disks[:-1]
        tlt: int = 0

        while True:
            # Adding offset `i` since you only pass one disk at a time.
            # So, when you reach the first disk, all disks moved 1 tick.
            # Then the second disk, every other disk besides the first disk moves 1 tick
            # and so on.
            disks_moved: list[bool] = [
                self.crt(
                    time=tlt + i,
                    position=disk.current_position,
                    total_positions=disk.positions,
                )
                for i, disk in enumerate(disks, 1)
            ]

            # With the given time, find if all disks will be on level 0 to allow the capsule to pass through.
            if all(disks_moved):
                return tlt

            tlt += 1

    def part_01(self) -> None:
        """
        Solve Part 01 of the problem.

        Returns:
            None
        """
        tlt: int = self.solve()
        print(f"Part 01: {tlt}")

    def part_02(self) -> None:
        """
        Solve Part 02 of the problem.

        Returns:
            None
        """
        tlt: int = self.solve(part02=True)
        print(f"Part 02: {tlt}")


if __name__ == "__main__":
    sol: Solution = Solution.parse_input()

    print(Timing(timeit(sol.part_01, number=1)).result(), "\n")
    print(Timing(timeit(sol.part_02, number=1)).result(), "\n")
