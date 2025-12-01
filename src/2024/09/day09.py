from collections import defaultdict
from timeit import timeit

from timing import Timing


class Solution:
    """Solve the problems."""

    def __init__(self, data: str) -> None:
        self.disk_map: str = data

    @classmethod
    def parse_input(cls) -> "Solution":
        """Parse the problem data input to be used.

        Returns:
            Solution:
                Class instance with the parsed input data.
        """
        with open("input.txt", "r") as file:
            data: str = file.read().strip()

        return cls(data=data)

    def get_filesystem(self) -> list[int]:
        """Parse the problem input and construct the filesystem from the disk map.

        Returns:
            list[int]:
                Filesystem representation of the diskmap.
        """
        filesystem: list[int] = []

        iD: int = 0
        for i, val in enumerate(self.disk_map):
            if i % 2 == 0:
                filesystem += [iD] * int(val)
                iD += 1
                continue
            filesystem += [-1] * int(val)

        return filesystem

    def get_blocked_filesystem(self) -> dict[int, tuple[int, int]]:
        """Parse the given problem input and get a representation of the filesystem indicating the blocks of files,
        iD -> (start, length).

        Returns:
            dict[int, tuple[int, int]]:
                Blocked filesystem representation.
        """
        filesystem: dict[int, tuple[int, int]] = defaultdict()

        iD: int = 0
        index: int = 0
        for i, val in enumerate(self.disk_map):
            if i % 2 == 0:
                filesystem[iD] = (index, int(val))
                iD += 1
            index += int(val)

        return filesystem

    def get_checksum(self, filesystem: list[int]) -> int:
        """Calculate the checksum of the filesystem.

        Args:
            filesystem (list[int]):
                Filesystem to have the checksum calculated for.

        Returns:
            int:
                Checksum of the filesystem.
        """
        return sum(i * filesystem[i] for i, v in enumerate(filesystem) if v != -1)

    def part_01(self) -> None:
        """Solve Part 01 of the problem.

        Returns:
            None
        """
        checksum: int = 0

        filesystem: list[int] = self.get_filesystem()
        for i, value in enumerate(filesystem):
            if value == -1:
                # Fill empty space with file iD from end of disk
                while filesystem[-1] == -1:
                    filesystem.pop()

                filesystem[i] = filesystem.pop()

            checksum += filesystem[i] * i

        print(f"Part 01: {checksum}")

    def part_02(self) -> None:
        """Solve Part 02 of the problem.

        Very slow method: ~90 seconds

        Returns:
            None
        """
        blocked_filesystem: dict[int, tuple[int, int]] = self.get_blocked_filesystem()
        filesystem: list[int] = self.get_filesystem()

        for iD in range(max(blocked_filesystem), 0, -1):
            start_index: int
            length: int
            start_index, length = blocked_filesystem[iD]

            # Find open space that will fit block (first fit) to the left of the block
            for index in range(start_index):
                if filesystem[index : index + length] == [-1] * length:
                    for j in range(length):
                        filesystem[index + j], filesystem[start_index + j] = (
                            filesystem[start_index + j],
                            filesystem[index + j],
                        )

        checksum: int = self.get_checksum(filesystem)
        print(f"Part 02: {checksum}")


if __name__ == "__main__":
    sol: Solution = Solution.parse_input()

    print(Timing(timeit(sol.part_01, number=1)).result(), "\n")
    print(Timing(timeit(sol.part_02, number=1)).result(), "\n")
