# # Advent of Code, 2015 Day 07
# # MilaDog
#
#
# from operator import iand, ior, lshift, rshift
# from timeit import timeit
# from functools import cache
#
# TEST_DATA: str = """123 -> x
# 456 -> y
# x AND y -> d
# x OR y -> e
# x LSHIFT 2 -> f
# y RSHIFT 2 -> g
# NOT x -> h
# NOT y -> i"""
#
#
# @cache
# def solve(wire: str):
#     if wire.isdigit():
#         return int(wire)
#
#     instr = wires[wire]
#
#     if len(instr) == 3:
#         match instr[1]:
#             case "AND":
#                 return iand(solve(instr[0]), solve(instr[2]))
#
#             case "OR":
#                 return ior(solve(instr[0]), solve(instr[2]))
#
#             case "RSHIFT":
#                 return rshift(solve(instr[0]), solve(instr[2]))
#
#             case "LSHIFT":
#                 return lshift(solve(instr[0]), solve(instr[2]))
#
#     elif len(instr) == 2:
#         return ~solve(instr[1]) & 65535
#
#     else:
#         return solve(instr[0])
#
#
# def main() -> None:
#     pa: int = solve("a")
#     print(f"Part 1: {pa}")
#
#     wires["b"] = [str(pa)]
#     solve.cache_clear()
#     print(f"Part 2: {solve('a')}")
#
#
# if __name__ == "__main__":
#     with open("input.txt", "r") as file:
#         lines = file.readlines()
#     # lines = TEST_DATA.splitlines()
#
#     wires = {
#         wire: instr.split(" ")
#         for line in lines
#         for instr, wire in [line.strip().split(" -> ")]
#     }
#     print(timeit(main, number=1))

from timeit import timeit
from typing import List

from timing import Timing


class Solution:
    def __init__(self, data: List[str]) -> None:
        self.data: List[str] = data

    @classmethod
    def parse_input(cls) -> "Solution":
        """Parse the problem data input to be used.

        Returns:
            Solution:
                Class instance with the parsed input data.
        """
        with open("input.txt", "r") as file:
            values: List[str] = list(file.read().strip())

        return cls(data=values)

    def part_01(self) -> None:
        """Solve Part 01 of the problem.

        Returns:
            None
        """
        tlt: int = 0
        print(f"Part 01: {tlt}")

    def part_02(self) -> None:
        """Solve Part 02 of the problem.

        Returns:
            None
        """
        tlt: int = 0

        print(f"Part 02: {tlt}")


if __name__ == "__main__":
    sol: Solution = Solution.parse_input()

    print(Timing(timeit(sol.part_01, number=1)).result(), "\n")
    print(Timing(timeit(sol.part_02, number=1)).result(), "\n")
