import re
from collections import defaultdict
from copy import deepcopy
from timeit import timeit

from src.common.python.timing import Timing


class Solution:
    """Solutions to the problems."""

    def __init__(self, data: tuple[dict[int, list[int]], list[list[int]]]) -> None:
        self.rules: dict[int, list[int]] = data[0]
        self.updates: list[list[int]] = data[1]

    @classmethod
    def parse_input(cls) -> "Solution":
        """Parse the problem data input to be used.

        Returns:
            Solution:
                Class instance with the parsed input data.
        """
        rules: dict[int, list[int]] = defaultdict(list)
        updates: list[list[int]]

        with open("input.txt", "r") as file:
            parts: list[str] = file.read().strip().split("\n\n")

            # Getting the rules
            for rule in parts[0].split("\n"):
                before, after = rule.strip().split("|")
                rules[int(before)].append(int(after))

            # Getting the updates
            updates = [[*map(int, update.strip().split(","))] for update in parts[1].split("\n")]

        return cls(data=(rules, updates))

    @classmethod
    def parse_with_regex(cls) -> "Solution":
        """Because I can."""
        with open("input.txt", "r") as file:
            f = file.read()
            rules = defaultdict(list)
            for a, b in re.findall(r"(\d+)\|(\d+)", f):
                rules[int(a)].append(int(b))

            updates = [list(map(int, line.split(","))) for line in re.findall(r"((?:\d+,)+\d+)", f)]

        return cls(data=(rules, updates))

    def is_valid_update(self, update: list[int]) -> bool:
        """Check if the given update is valid or not. For an update to be valid,
        all IDs in the update have to be in the correct order.
        This is checked against the given update rules.

        Args:
            update (list[int])):
                 Update to check for validity.

        Returns:
            bool:
                If the update is valid or not.

        """
        for i, curr in enumerate(update):
            if rules := self.rules.get(curr):
                for val in rules:
                    # Check that no rule falls BEFORE current value
                    if val in update[:i]:
                        return False

        return True

    def fix_error_update(self, update: list[int]) -> None:
        """Fix a broken update. Fixes by swapping IDs to ensure that the new order of the update is valid.

        Args:
            update (list[int]):
                Update that needs fixing.

        Returns:
            None. Updated in-place.

        """
        for i, curr in enumerate(update):
            if rules := self.rules.get(curr):
                for val in rules:
                    if val in update[:i]:
                        # Swap values
                        replace_index: int = update.index(val)
                        target_index: int = update.index(curr)
                        update[replace_index], update[target_index] = (
                            update[target_index],
                            update[replace_index],
                        )

        if not self.is_valid_update(update):
            self.fix_error_update(update)

    def part_01(self) -> None:
        """Solve Part 01 of the problem.

        Returns:
            None
        """
        tlt: int = 0

        # Go through updates.
        for update in deepcopy(self.updates):
            # Ensure that it is valid
            if self.is_valid_update(update):
                # Get the middle value and add to total
                tlt += update[len(update) // 2]

        print(f"Part 01: {tlt}")

    def part_02(self) -> None:
        """Solve Part 02 of the problem.

        Returns:
            None
        """
        tlt: int = 0

        # Go through updates.
        for update in deepcopy(self.updates):
            # Ensure that it is valid
            if not self.is_valid_update(update):
                # Get the middle value and add to total
                self.fix_error_update(update)
                tlt += update[len(update) // 2]

        print(f"Part 02: {tlt}")

    def solve_both(self) -> None:
        """Solve both problems.

        Returns:
            None
        """
        tlt1: int = 0
        tlt2: int = 0

        # Go through updates.
        for update in deepcopy(self.updates):
            # Ensure that it is valid
            if self.is_valid_update(update):
                # Get the middle value and add to total
                tlt1 += update[len(update) // 2]

            else:
                # Fix
                self.fix_error_update(update)
                # Get the middle value and add to total
                tlt2 += update[len(update) // 2]

        print(f"Part 01: {tlt1}")
        print(f"Part 02: {tlt2}")


if __name__ == "__main__":
    sol: Solution = Solution.parse_with_regex()

    print(Timing(timeit(sol.part_01, number=1)).result(), "\n")
    print(Timing(timeit(sol.part_02, number=1)).result(), "\n")
    print(Timing(timeit(sol.solve_both, number=1)).result(), "\n")
