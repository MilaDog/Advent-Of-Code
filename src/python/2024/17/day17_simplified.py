import re
from collections import defaultdict
from timeit import timeit
from typing import Any, Generator

from src.timing import Timing


class Solution:
    """Solutions to the problems."""

    def __init__(self) -> None:
        registers, instructions = Solution.parse_input()
        self.registers: dict[str, int] = registers
        self.instructions: list[int] = instructions

    @staticmethod
    def parse_input() -> tuple[dict[str, int], list[int]]:
        """Parse the problem data input to be used.

        Returns:
            Solution:
                Class instance with the parsed input data.
        """
        with open("./inputs/2024/17/input.txt", "r") as file:
            a, b = file.read().strip().split("\n\n")

            registers: dict[str, int] = defaultdict(int)

            for line in a.strip().split("\n"):
                reg, val = re.findall(r"Register ([ABC]): (\d+)", line)[0]
                registers[reg] = int(val)

            instructions: list[int] = list(map(int, re.findall(r"\d", b)))

        return registers, instructions

    def solve(self) -> Generator[Any, Any, Any]:
        """Simplified solution to Part 01.

        Returns:
            None
        """
        rA: int = self.registers["A"]
        rB: int
        rC: int

        while rA:
            rB = (rA % 8) ^ 1
            rC = rA >> rB
            rB ^= rC + 4
            rA >>= 3
            yield rB % 8

    def part_01(self) -> None:
        """Solve Part 01 of the problem.

        Returns:
            None
        """
        res: str = ",".join(map(str, [*self.solve()]))
        print(f"Part 01: {res}")

    def part_02(self) -> None:
        """Solve Part 02 of the problem.

        Have to break down the program given. From there, reverse engineer your way to the answer.
        Attached that as a separate file.

        Returns:
            None
        """
        potential_A: list[int] = [0]
        next_values: list[int] = []

        for opcode in self.instructions[::-1]:
            for rA in potential_A:
                for bit in range(8):
                    rB = (bit % 8) ^ 1
                    rC = (rA + bit) >> rB
                    rB ^= rC + 4

                    if rB % 8 == opcode:
                        next_values.append((rA + bit) << 3)

            next_values, potential_A = [], next_values

        tlt: int = min([rA >> 3 for rA in potential_A])
        print(f"Part 02: {tlt}")


if __name__ == "__main__":
    sol: Solution = Solution()

    print(Timing(timeit(sol.part_01, number=1)).result(), "\n")
    print(Timing(timeit(sol.part_02, number=1)).result(), "\n")
