import hashlib
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

    def part_01(self) -> None:
        """Solve Part 01 of the problem.

        Returns:
            None
        """
        res: str = ""

        tlt: int = -1
        for _ in range(8):
            while True:
                tlt += 1
                hashed: str = hashlib.md5(f"{self.data}{tlt}".encode()).hexdigest()

                if hashed.startswith("00000"):
                    res += hashed[5]
                    break

        print(f"Part 01: {res}")

    def part_02(self) -> None:
        """Solve Part 02 of the problem.

        Returns:
            None
        """
        res: list[str] = ["#"] * 8

        tlt: int = -1
        while "#" in res:
            tlt += 1
            hashed: str = hashlib.md5(f"{self.data}{tlt}".encode()).hexdigest()

            if hashed.startswith("00000"):
                place: str = hashed[5]
                value: str = hashed[6]

                if place.isdigit() and -1 < int(place) < 8:
                    if res[int(place)] == "#":
                        res[int(place)] = value

        print(f"Part 02: {''.join(res)}")


if __name__ == "__main__":
    sol: Solution = Solution.parse_input()

    print(Timing(timeit(sol.part_01, number=1)).result(), "\n")
    print(Timing(timeit(sol.part_02, number=1)).result(), "\n")
