from timeit import timeit

from src.common.python.timing import Timing


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

    def execute_instructions(self, a_value: int = 0) -> int:
        """
        Execute the computer program instructions. Return the result in register `b` when done.

        Args:
            a_value (int):
                Starting value of register `a`.

        Returns:
            int:
                Value in register `b`.
        """
        registers: dict[str, int] = {"a": a_value, "b": 0}
        i: int = 0

        while 0 <= i < len(self.data):
            instruction: str = self.data[i].replace(",", "")

            match instruction[:3]:
                case "inc":
                    registers[instruction[4:]] += 1
                    i += 1

                case "tpl":
                    registers[instruction[4:]] *= 3
                    i += 1

                case "hlf":
                    registers[instruction[4:]] //= 2
                    i += 1

                case "jmp":
                    i += int(instruction[4:])

                case "jio":
                    vals: list[str] = instruction[4:].split(" ")
                    i += int(vals[1]) if registers[vals[0]] == 1 else 1

                case "jie":
                    vals: list[str] = instruction[4:].split(" ")
                    i += int(vals[1]) if registers[vals[0]] % 2 == 0 else 1

                case _:
                    assert False, f"INVALID INSTRUCTIONS {instruction}"

        return registers["b"]

    def part_01(self) -> None:
        """
        Solve Part 01 of the problem.

        Returns:
            None
        """
        tlt: int = self.execute_instructions()
        print(f"Part 01: {tlt}")

    def part_02(self) -> None:
        """
        Solve Part 02 of the problem.

        Returns:
            None
        """
        tlt: int = self.execute_instructions(a_value=1)
        print(f"Part 02: {tlt}")


if __name__ == "__main__":
    sol: Solution = Solution.parse_input()

    print(Timing(timeit(sol.part_01, number=1)).result(), "\n")
    print(Timing(timeit(sol.part_02, number=1)).result(), "\n")
