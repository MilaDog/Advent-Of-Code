import functools
import hashlib
import re
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
            values: str = file.read().strip()

        return cls(data=values)

    @functools.lru_cache(maxsize=None)
    def get_hash_hex(self, value: str, repeat: int = 1) -> str:
        """Hash the given value and return the hex.

        Args:
            value (str):
                Value to hash.
            repeat (int):
                Number of times to hash the hashed valued.

        Returns:
            str:
                Hashed hex.
        """
        for _ in range(repeat):
            value = hashlib.md5(value.encode()).hexdigest()

        return value

    def solve(self, stretch: bool = False) -> int:
        """Solve the MD5 hash problem.

        Args:
            stretch (bool):
                Whether to hash the hashed keys.

        Returns:
            int:
                Index producing the 64th valid key.
        """
        tlt: int = 0
        index: int = 0

        while True:
            hashed: str = self.get_hash_hex(f"{self.data}{index}", 2017 if stretch else 1)

            if x := re.search(r"(\w)\1{2}", hashed):
                # Check the next 1000 hashes
                check: str = x.group(0)[0] * 5
                for i in range(index + 1, index + 1001):
                    if check in self.get_hash_hex(f"{self.data}{i}", 2017 if stretch else 1):
                        tlt += 1

                        if tlt == 64:
                            return index

                        break

            index += 1

    def part_01(self) -> None:
        """Solve Part 01 of the problem.

        Returns:
            None
        """
        tlt: int = self.solve(stretch=False)
        print(f"Part 01: {tlt}")

    def part_02(self) -> None:
        """Solve Part 02 of the problem.

        Returns:
            None
        """
        tlt: int = self.solve(stretch=True)
        print(f"Part 02: {tlt}")


if __name__ == "__main__":
    sol: Solution = Solution.parse_input()

    print(Timing(timeit(sol.part_01, number=1)).result(), "\n")
    print(Timing(timeit(sol.part_02, number=1)).result(), "\n")
