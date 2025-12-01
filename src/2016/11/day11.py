import re
from collections import defaultdict
from copy import deepcopy
from dataclasses import dataclass
from timeit import timeit

from timing import Timing


@dataclass
class Equipment:
    iD: str
    type: str
    compatible_with: str


class Solution:
    def __init__(self, data: dict[int, list[Equipment]]) -> None:
        self.data: dict[int, list[Equipment]] = data

    @classmethod
    def parse_input(cls) -> "Solution":
        """Parse the problem data input to be used.

        Returns:
            Solution:
                Class instance with the parsed input data.
        """
        with open("input.txt", "r") as file:
            floors: dict[int, list[Equipment]] = defaultdict(list)

            for i, line in enumerate(file.readlines(), start=1):
                for found_Equipment in re.findall(r"(\w+ generator|\w+-\w+ microchip)", line):
                    parts: list[str] = found_Equipment.split(" ")

                    compatible_with: str = (
                        f"{parts[0][0].upper()}G" if parts[1] == "microchip" else f"{parts[0][0].upper()}M"
                    )

                    item: Equipment = Equipment(
                        iD=f"{parts[0][0]}{parts[1][0]}".upper(),
                        type=parts[1],
                        compatible_with=compatible_with,
                    )
                    floors[i].append(item)

            floors[4] = []

        return cls(data=floors)

    def __all_on_top_floor(self, floors: dict[int, list[Equipment]]) -> bool:
        """Determine if all the equipment are on the top floor.

        Returns:
            bool:
                If all the equipment are on the top floor.
        """
        return all(not floors[x] for x in range(4))

    def part_01(self) -> None:
        """Solve Part 01 of the problem.

        Returns:
            None
        """
        tlt: int = 0

        floors: dict[int, list[Equipment]] = deepcopy(self.data)

        current_item: Equipment | None = None
        current_floor: int = 1
        for item in floors[2]:
            for item2 in floors[1]:
                if item2.iD == item.compatible_with:
                    current_item = item2
                    break

            if current_item:
                break

        assert current_item is not None

        while not self.__all_on_top_floor(floors):
            # Move to next floor
            floors[current_floor].remove(current_item)
            current_floor += 1

            # Determine if can move higher
            if (
                current_item.compatible_with in [x.iD for x in floors[current_floor]]
                and len(floors[current_floor]) == 1
            ):
                # Move both up
                with_item: Equipment = floors[current_floor].pop(0)
                current_floor += 1
                floors[current_floor].append(with_item)

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
