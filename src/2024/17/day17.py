import enum
import re
from collections import defaultdict
from copy import deepcopy
from timeit import timeit

from src.common.python.timing import Timing


class OPCodes(enum.Enum):
    """Operation Codes for the Debugger."""

    ADV = 0
    BXL = 1
    BST = 2
    JNZ = 3
    BXC = 4
    OUT = 5
    BDV = 6
    CDV = 7


class Debugger:
    """Problem debugger."""

    def __init__(self, registers: dict[str, int]) -> None:
        self.registers: dict[str, int] = registers
        self.index: int = 0

    def debug(self, instructions: list[int]) -> list[int]:
        """Execute the given instructions, returning the output after debugging has finished.

        Args:
            instructions (list[int]):
                Instruction set to debug.

        Returns:
            list[int]:
                Resulting output from the debugger.
        """
        res: list[int] = []
        while 0 <= self.index < len(instructions):
            match OPCodes(instructions[self.index]):
                case OPCodes.ADV:
                    self.__adv(operand=instructions[self.index + 1])

                case OPCodes.BXL:
                    self.__bxl(operand=instructions[self.index + 1])

                case OPCodes.BST:
                    self.__bst(operand=instructions[self.index + 1])

                case OPCodes.JNZ:
                    self.__jnz(operand=instructions[self.index + 1])

                case OPCodes.BXC:
                    self.__bxc()

                case OPCodes.OUT:
                    res.append(self.__out(operand=instructions[self.index + 1]))

                case OPCodes.BDV:
                    self.__bdv(operand=instructions[self.index + 1])

                case OPCodes.CDV:
                    self.__cdv(operand=instructions[self.index + 1])

        return res

    # Utility
    def __get_combo_operand_value(self, operand: int) -> int:
        """Get the combo value based on the given operand.

        Args:
            operand (int):
                Operand used to get the combo value for.

        Returns:
            int:
                Got combo value.

        """
        if 0 <= operand <= 3:
            return operand

        if operand < 7:
            return self.registers["ABC"[operand - 4]]

        raise ValueError

    # Operations
    def __adv(self, operand: int) -> None:
        """Divide register A by the combo value of the given operand, assigned back to register A.
        Truncates decimals.

        Args:
            operand (int):
                Operand used to divide against.

        Returns:
            None

        """
        self.registers["A"] >>= self.__get_combo_operand_value(operand=operand)
        self.index += 2

    def __bdv(self, operand: int) -> None:
        """Divide register A by the combo value of the given operand, assigned back to register B.
        Truncates decimals.

        Args:
            operand (int):
                Operand used to divide against.

        Returns:
            None

        """
        self.registers["B"] = self.registers["A"] >> self.__get_combo_operand_value(operand=operand)
        self.index += 2

    def __cdv(self, operand: int) -> None:
        """Divide register A by the combo value of the given operand, assigned back to register C.
        Truncates decimals.

        Args:
            operand (int):
                Operand used to divide against.

        Returns:
            None

        """
        self.registers["C"] = self.registers["A"] >> self.__get_combo_operand_value(operand=operand)
        self.index += 2

    def __bxl(self, operand: int) -> None:
        """Get the bitwise XOR of register B and the literal operand, assigning result to register B.

        Args:
            operand (int):
                Operand used for operation.

        Returns:
            None

        """
        self.registers["B"] ^= operand
        self.index += 2

    def __bst(self, operand: int) -> None:
        """Calculate the value of the combo operand modulo 8, assigning result to register B.

        Args:
            operand (int):
                Operand used for operation.

        Returns:
            None

        """
        self.registers["B"] = self.__get_combo_operand_value(operand=operand) % 8
        self.index += 2

    def __jnz(self, operand: int) -> None:
        """Increase the current index by the given literal operand if the value in register A is not 0.

        Args:
            operand (int):
                Operand used for operation.

        Returns:
            None

        """
        if self.registers["A"] != 0:
            self.index = operand

        else:
            self.index += 2

    def __bxc(self) -> None:
        """Calculate the bitwise XOR of registers B and C, assigning the result to register B.

        Returns:
            None

        """
        self.registers["B"] ^= self.registers["C"]
        self.index += 2

    def __out(self, operand: int) -> int:
        """Get the value of the combo operand modulo 8.

        Args:
            operand (int):
                Operand used to divide against.

        Returns:
            None

        """
        self.index += 2
        return self.__get_combo_operand_value(operand=operand) % 8


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
        with open("input.txt", "r") as file:
            a, b = file.read().strip().split("\n\n")

            registers: dict[str, int] = defaultdict(int)

            for line in a.strip().split("\n"):
                reg, val = re.findall(r"Register ([ABC]): (\d+)", line)[0]
                registers[reg] = int(val)

            instructions: list[int] = list(map(int, re.findall(r"\d", b)))

        return registers, instructions

    def part_01(self) -> None:
        """Solve Part 01 of the problem.

        Returns:
            None
        """
        debugger: Debugger = Debugger(registers=deepcopy(self.registers))
        res: str = ",".join(map(str, debugger.debug(instructions=self.instructions)))
        print(f"Part 01: {res}")

    def part_02(self) -> None:
        """Solve Part 02 of the problem.

        Returns:
            None
        """
        tlt: int = 0

        print(f"Part 02: {tlt}")


if __name__ == "__main__":
    sol: Solution = Solution()

    print(Timing(timeit(sol.part_01, number=1)).result(), "\n")
    print(Timing(timeit(sol.part_02, number=1)).result(), "\n")
