import re
from collections import Counter
from timeit import timeit
from typing import Counter as Counter_

from common.python.timing import Timing


class Solution:
    def __init__(self, data: list[str]) -> None:
        self.data: list[str] = data

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

    def part_01(self) -> None:
        """
        Solve Part 01 of the problem.

        Returns:
            None
        """
        tlt: int = 0

        for room in self.data:
            encryption, sector_id, checksum = re.findall(
                r"([a-z-]+?)-(\d+)\[([a-z]{5})]", room
            )[0]

            c: Counter_[str] = Counter()
            for section in encryption.split("-"):
                c.update(section)

            res: str = "".join(
                [ltr for ltr, _ in sorted(c.items(), key=lambda x: (-x[1], x[0]))[:5]]
            )

            if res == checksum:
                tlt += int(sector_id)

        print(f"Part 01: {tlt}")

    def part_02(self) -> None:
        """
        Solve Part 02 of the problem.

        Returns:
            None
        """
        tlt: int = 0

        for room in self.data:
            encryption, sector_id, checksum = re.findall(
                r"([a-z-]+?)-(\d+)\[([a-z]{5})]", room
            )[0]

            key: int = int(sector_id) % 26
            decryption: str = ""

            for ltr in encryption:
                if ltr == "-":
                    decryption += " "

                else:
                    decryption += chr((ord(ltr) - 0x61 + key) % 26 + 0x61)

            if "north" in decryption:
                print(decryption)
                tlt = int(sector_id)
                break

        print(f"Part 02: {tlt}")


if __name__ == "__main__":
    sol: Solution = Solution.parse_input()

    print(Timing(timeit(sol.part_01, number=1)).result(), "\n")
    print(Timing(timeit(sol.part_02, number=1)).result(), "\n")
