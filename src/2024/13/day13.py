import re
from dataclasses import dataclass
from timeit import timeit

from timing import Timing


@dataclass
class ClawMachine:
    """Claw Machine details."""

    button_a: tuple[int, int]
    button_b: tuple[int, int]
    target: tuple[int, int]
    button_a_cost: int = 3
    button_b_cost: int = 1


class Solution:
    """Solutions to the problems."""

    def __init__(self, claw_machines: list[ClawMachine]) -> None:
        self.claw_machines: list[ClawMachine] = claw_machines

    @classmethod
    def parse_input(cls) -> "Solution":
        """Parse the problem data input to be used.

        Returns:
            Solution:
                Class instance with the parsed input data.
        """
        with open("input.txt", "r") as file:
            values: list[ClawMachine] = []

            for claw_machine in file.read().split("\n\n"):
                ax, ay, bx, by, tx, ty = list(map(int, re.findall(r"\d+", claw_machine)))
                values.append(ClawMachine(button_a=(ax, ay), button_b=(bx, by), target=(tx, ty)))

        return cls(claw_machines=values)

    def can_win(self, claw_machine: ClawMachine, part02: bool = False) -> int:
        """Determine whether the Claw Machine can be solved.

        Math:
            With ButtonA -> a, ButtonB -> b, Target -> t, x/y changes being ax/ay for (a, b, t) respectively,
            and unknown amount pushes A and B,

            Aax + Bbx = tx
            Aay + Bby = ty

            Therefore, solving for A and equalling them gives:
            (tx - Bbx)/ax = (ty - Bby) / ay

            Solving B:
            ay*tx - B*ay*bx = ax*ty - B*ax*by
            B*ax*by - B*ay*bx = ax*ty - ay*tx
            B(ax*by - ay*bx) = ax*ty - ay*tx
            B = (ax*ty - ay*tx) / (ax*by - ay*bx)

            Thus, solve B, then A.
            If results are integer values, no decimals, then can win.

            Return A*ButtonACost + B*ButtonBCost

        Args:
            claw_machine (ClawMachine):
                Claw machine to see if you can try and win it.

            part02 (bool):
                Default False. Whether solving for Part 02 of the problem.

        Returns:
            int:
                Number of tokens needed to win the claw machine. 0 if unwinnable.
        """
        ax, ay = claw_machine.button_a
        bx, by = claw_machine.button_b
        tx, ty = claw_machine.target
        tx += 1e13 * part02
        ty += 1e13 * part02

        B: float = (ax * ty - ay * tx) / (ax * by - ay * bx)
        A: float = (tx - B * bx) / ax

        if not B.is_integer() or not A.is_integer():
            return 0

        return int(A * claw_machine.button_a_cost + B * claw_machine.button_b_cost)

    def part_01(self) -> None:
        """Solve Part 01 of the problem.

        Returns:
            None
        """
        tlt: int = sum(self.can_win(claw_machine=claw_machine) for claw_machine in self.claw_machines)
        print(f"Part 01: {tlt}")

    def part_02(self) -> None:
        """Solve Part 02 of the problem.

        Returns:
            None
        """
        tlt: int = sum(self.can_win(claw_machine=claw_machine, part02=True) for claw_machine in self.claw_machines)
        print(f"Part 02: {tlt}")


if __name__ == "__main__":
    sol: Solution = Solution.parse_input()

    print(Timing(timeit(sol.part_01, number=1)).result(), "\n")
    print(Timing(timeit(sol.part_02, number=1)).result(), "\n")
