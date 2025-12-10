from collections import deque
from timeit import timeit

from src.timing import Timing


class Machine:
    """Representation of a machine within the solution."""

    def __init__(self, machine_id: int, target_light_indicator: int, buttons: list[int], target_joltage: list[int]):
        self.machine_id: int = machine_id
        self.target_light_indicator: int = target_light_indicator
        self.buttons: list[int] = buttons
        self.target_joltage: list[int] = target_joltage

    def __str__(self) -> str:
        """String representation of the Machine."""
        return (
            f"Machine[target_light_indicator={self.target_light_indicator}, "
            f"target_joltage={self.target_joltage}, buttons={self.buttons}]"
        )

    def __repr__(self) -> str:
        return str(self)

    def perform_toggles(self) -> int:
        """Perform the toggling of the lights via button presses, returning the minimum number of buttons that need
        to be pressed to turn the lights on into the desired format.

        Returns:
            int: Minimum number of button presses to achieve the target light indicator sequence.
        """
        q: deque[tuple[int, int]] = deque([(0, 0)])
        seen: set[int] = {0}

        while q:
            cnter, light_indicator = q.popleft()

            if light_indicator == self.target_light_indicator:
                return cnter

            for button in self.buttons:
                new_state: int = light_indicator ^ button

                if new_state not in seen:
                    seen.add(new_state)
                    q.append((cnter + 1, new_state))

        return -1

    def perform_joltage_counting(self) -> int:
        """Perform the joltage counting for the machine, to reach the given machine target.

        Returns:
            int: Minimum number of button presses to achieve the target joltage.
        """
        return -1


class Solution:
    """Solutions to the problems."""

    def __init__(self, data: list[Machine]) -> None:
        self.machines: list[Machine] = data

    @classmethod
    def parse_input(cls) -> "Solution":
        """Parse the problem data input to be used.

        Returns:
            Solution:
                Class instance with the parsed input data.
        """
        values: list[Machine] = []

        with open("./inputs/2025/10/input.txt", "r") as file:
            for i, line in enumerate(file.readlines()):
                parts: list[str] = line.strip().split()

                target_light_indicator: int = 0
                for indx, val in enumerate(parts[0][1:-1]):
                    if val == "#":
                        target_light_indicator |= 1 << indx

                buttons: list[int] = []
                for button in parts[1:-1]:
                    button_mask: int = 0
                    for indx in map(int, button[1:-1].split(",")):
                        button_mask |= 1 << indx

                    buttons.append(button_mask)

                joltage: list[int] = list(map(int, parts[-1][1:-1].split(",")))

                values.append(
                    Machine(
                        machine_id=i,
                        target_light_indicator=target_light_indicator,
                        buttons=buttons,
                        target_joltage=joltage,
                    )
                )

        return cls(data=values)

    def part_01(self) -> None:
        """Solve Part 01 of the problem."""
        tlt: int = 0

        for machine in self.machines:
            tlt += machine.perform_toggles()

        print(f"Part 01: {tlt}")

    def part_02(self) -> None:
        """Solve Part 02 of the problem."""
        tlt: int = 0

        for machine in self.machines:
            tlt += machine.perform_joltage_counting()

        print(f"Part 02: {tlt}")


if __name__ == "__main__":
    sol: Solution = Solution.parse_input()

    print(Timing(timeit(sol.part_01, number=1)).result(), "\n")
    print(Timing(timeit(sol.part_02, number=1)).result(), "\n")
