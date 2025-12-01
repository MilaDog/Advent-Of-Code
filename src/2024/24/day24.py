from collections import defaultdict
from timeit import timeit

from timing import Timing


class Solution:
    """Solutions to the problems."""

    def __init__(self, registers: dict[str, int], instructions: list[tuple[str, ...]]) -> None:
        self.registers: dict[str, int] = registers
        self.instructions: list[tuple[str, ...]] = instructions

    @classmethod
    def parse_input(cls) -> "Solution":
        """Parse the problem data input to be used.

        Returns:
            Solution:
                Class instance with the parsed input data.
        """
        with open("input.txt", "r") as file:
            registers: dict[str, int] = defaultdict(int)
            instructions: list[tuple[str, ...]] = []

            a, b = file.read().split("\n\n")

            for line in a.split("\n"):
                reg, val = line.strip().split(": ")
                registers[reg] = int(val)

            for line in b.split("\n"):
                a, inst, b, _, to = line.strip().split(" ")
                instructions.append((a, b, inst, to))

        return cls(registers=registers, instructions=instructions)

    def part_01(self) -> None:
        """Solve Part 01 of the problem.

        Returns:
            None
        """
        while True:
            repeat: bool = False
            for instruction in self.instructions:
                a, b, instr, c = instruction

                if c not in self.registers and a in self.registers and b in self.registers:
                    match instr:
                        case "OR":
                            self.registers[c] = self.registers[a] | self.registers[b]

                        case "XOR":
                            self.registers[c] = self.registers[a] ^ self.registers[b]

                        case "AND":
                            self.registers[c] = self.registers[a] & self.registers[b]

                        case _:
                            raise Exception("OH NO")

                    repeat = True

            if not repeat:
                break

        tlt: int = 0

        for i, val in enumerate(
            map(self.registers.get, sorted(filter(lambda x: x[0].startswith("z"), self.registers.keys())))
        ):
            tlt += val * 2**i

        print(f"Part 01: {tlt}")

    def part_02(self) -> None:
        """Solve Part 02 of the problem.

        DONE MANUALLY/VISUALLY

        Returns:
            None
        """
        d: dict[str, tuple[str, ...]] = {c: (a, b, instr) for a, b, instr, c in self.instructions}

        def get_path(v, dd=3):
            if v not in d.keys() or v.startswith("z") or dd == 0:
                return v

            a, b, op = d[v]
            return f"({get_path(a, dd - 1)} {op} {get_path(b, dd - 1)})"

        for i in range(1, 46):
            c = "z" + f"{i}".zfill(2)
            a, b, instr = d[c]
            print(f"{c} -> {a} {instr} {b}")
            print(f"{c} -> {get_path(a, dd=1)} {instr} {get_path(b, dd=1)}")
            print(f"{c} -> {get_path(a, dd=2)} {instr} {get_path(b, dd=2)}")
            print(f"{c} -> {get_path(a, dd=3)} {instr} {get_path(b, dd=3)}")
            print()

        tlt: int = 0
        print(f"Part 02: {tlt}")


if __name__ == "__main__":
    sol: Solution = Solution.parse_input()

    print(Timing(timeit(sol.part_01, number=1)).result(), "\n")
    print(Timing(timeit(sol.part_02, number=1)).result(), "\n")
