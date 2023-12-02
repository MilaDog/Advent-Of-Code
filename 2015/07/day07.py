# Advent of Code, 2015 Day 07
# MilaDog


from operator import iand, ior, lshift, rshift
from timeit import timeit
from functools import cache

TEST_DATA: str = """123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i"""


@cache
def solve(wire: str):
    if wire.isdigit():
        return int(wire)

    instr = wires[wire]

    if len(instr) == 3:
        match instr[1]:
            case "AND":
                return iand(solve(instr[0]), solve(instr[2]))

            case "OR":
                return ior(solve(instr[0]), solve(instr[2]))

            case "RSHIFT":
                return rshift(solve(instr[0]), solve(instr[2]))

            case "LSHIFT":
                return lshift(solve(instr[0]), solve(instr[2]))

    elif len(instr) == 2:
        return ~solve(instr[1]) & 65535

    else:
        return solve(instr[0])


def main() -> None:
    pa: int = solve("a")
    print(f"Part 1: {pa}")

    wires["b"] = [str(pa)]
    solve.cache_clear()
    print(f"Part 2: {solve('a')}")


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        lines = file.readlines()
    # lines = TEST_DATA.splitlines()

    wires = {
        wire: instr.split(" ")
        for line in lines
        for instr, wire in [line.strip().split(" -> ")]
    }
    print(timeit(main, number=1))
