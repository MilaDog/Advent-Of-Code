from timeit import timeit

from timing import Timing


class Assembunny:
    def __init__(self, *, c_start: int = 0) -> None:
        self.registers: dict[str, int] = {x: 0 for x in "abcd"}
        self.registers["c"] = c_start
        self.index: int = 0

    def copy(self, instruction: str) -> None:
        frm, to = instruction.strip().split(" ")
        self.registers[to] = int(frm) if frm.isdigit() else self.registers[frm]
        self.index += 1

    def increment(self, instruction: str) -> None:
        self.registers[instruction.strip()] += 1
        self.index += 1

    def decrement(self, instruction: str) -> None:
        self.registers[instruction.strip()] -= 1
        self.index += 1

    def jump_not_zero(self, instruction: str) -> None:
        reg, amt = instruction.strip().split(" ")
        value: int = int(reg) if reg.isdigit() else self.registers[reg]

        self.index += 1 if value == 0 else int(amt)

    def get(self, register: str) -> int:
        if register in self.registers:
            return self.registers[register]
        return -1

    def parse(self, instruction: str) -> None:
        match instruction[:3]:
            case "cpy":
                self.copy(instruction[4:])

            case "inc":
                self.increment(instruction[4:])

            case "dec":
                self.decrement(instruction[4:])

            case "jnz":
                self.jump_not_zero(instruction[4:])

            case _:
                assert False, "INVALID INSTRUCTION"


class Solution:
    def __init__(self, data: list[str]) -> None:
        self.data: list[str] = data

    @classmethod
    def parse_input(cls) -> "Solution":
        """Parse the problem data input to be used.

        Returns:
            Solution:
                Class instance with the parsed input data.
        """
        with open("input.txt", "r") as file:
            values: list[str] = file.read().splitlines()

        return cls(data=values)

    def part_01(self) -> None:
        """Solve Part 01 of the problem.

        Returns:
            None
        """
        asm: Assembunny = Assembunny()

        while True:
            try:
                asm.parse(self.data[asm.index].strip())

            except IndexError:
                break

        print(f"Part 01: {asm.get('a')}")

    def part_02(self) -> None:
        """Solve Part 02 of the problem.

        Returns:
            None
        """
        asm: Assembunny = Assembunny(c_start=1)

        while True:
            try:
                asm.parse(self.data[asm.index].strip())

            except IndexError:
                break

        print(f"Part 02: {asm.get('a')}")


if __name__ == "__main__":
    sol: Solution = Solution.parse_input()

    print(Timing(timeit(sol.part_01, number=1)).result(), "\n")
    print(Timing(timeit(sol.part_02, number=1)).result(), "\n")
