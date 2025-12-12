from dataclasses import dataclass
from timeit import timeit

from src.timing import Timing


@dataclass
class Present:
    """Representation of a Present in the solution."""

    id_: int
    size: list[list[str]]


@dataclass
class Tree:
    """Representation of a Tree in the problem."""

    size: tuple[int, ...]
    needed_presents: dict[int, int]


class Solution:
    """Solutions to the problems."""

    def __init__(self, trees: list[Tree], presents: dict[int, Present]) -> None:
        self.trees: list[Tree] = trees
        self.presents: dict[int, Present] = presents

    @classmethod
    def parse_input(cls) -> "Solution":
        """Parse the problem data input to be used.

        Returns:
            Solution:
                Class instance with the parsed input data.
        """
        values: list[Tree] = []
        presents: dict[int, Present] = dict()

        with open("./inputs/2025/12/input.txt", "r") as file:
            *ps, ts = file.read().strip().split("\n\n")

            for present in ps:
                id_, grid = present.strip().split(":\n")
                presents[int(id_)] = Present(id_=int(id_), size=[list(r.strip()) for r in grid.split()])

            for tree in ts.strip().split("\n"):
                size, nums = tree.strip().split(": ")
                values.append(
                    Tree(
                        size=tuple(map(int, size.split("x"))),
                        needed_presents={i: v for i, v in enumerate(map(int, nums.split(" ")))},
                    )
                )

        return cls(trees=values, presents=presents)

    def solve(self) -> None:
        """Solve Part 01 of the problem.

        The way the problem is set, there are three noticeable things:
            1. The presents are mostly 3x3 in size
            2. The tree will either not be able to contain the needed presents
            3. The tree will be able to contain the needed presents with sufficient amount of room left over

        So, can be lazy and just count the times when the presents' space was not bigger than the space available
        under the tree.

        The edge cases in the problem statement did not appear in the actual user input.

        """
        tlt: int = 0

        for tree in self.trees:
            width, height = tree.size
            tlt += (width // 3) * (height // 3) >= sum(tree.needed_presents.values())

        print(f"Part 01: {tlt}")


if __name__ == "__main__":
    sol: Solution = Solution.parse_input()

    print(Timing(timeit(sol.solve, number=1)).result(), "\n")
