from collections import defaultdict
from timeit import timeit

from timing import Timing


class Solution:
    def __init__(self, structure: dict[str, list[str]], weightings: dict[str, int]) -> None:
        self.structure: dict[str, list[str]] = structure
        self.weightings: dict[str, int] = weightings

    @classmethod
    def parse_input(cls) -> "Solution":
        """Parse the problem data input to be used.

        Returns:
            Solution:
                Class instance with the parsed input data.
        """
        weightings: dict[str, int] = defaultdict(int)
        structure: dict[str, list[str]] = defaultdict(list)

        with open("input.txt", "r") as file:
            for line in file.readlines():
                line = line.strip().replace("(", "").replace(")", "").replace(",", "")

                # Structure: (iD, weight, [children])
                iD: str
                weight: str
                children: list[str] = []

                if "->" in line:
                    iD, weight, *children = line.replace("-> ", "").split(" ")

                else:
                    iD, weight = line.strip().replace("(", "").replace(")", "").split(" ")

                weightings[iD] = int(weight)
                structure[iD] = children

        return cls(structure=structure, weightings=weightings)

    def part_01(self) -> None:
        """Solve Part 01 of the problem.

        Returns:
            None
        """
        # Get all iDs that have children
        have_children: list[str] = [k for k, v in self.structure.items() if v]

        # Get all keys
        programs: set[str] = set(self.structure.keys())

        # For each program that has children, remove from all programs.
        # Bottom program will be the remaining one
        children: list[str] = []
        for key in have_children:
            children += self.structure[key]

        res: str = list(programs - set(children)).pop(0)

        print(f"Part 01: {res}")

    def determine_subtree_weighting(self, child: str) -> int:
        tlt: int = 0
        to_process: list[str] = [child]

        while to_process:
            processing: str = to_process.pop()
            tlt += self.weightings[processing]
            to_process += self.structure[processing]

        return tlt

    def part_02(self) -> None:
        """Solve Part 02 of the problem.

        Returns:
            None
        """
        tlt: int = 0

        head: str = "mkxke"
        print(head, self.weightings[head], self.determine_subtree_weighting(head))

        d = defaultdict(list)
        for child in self.structure[head]:
            d[self.determine_subtree_weighting(child)] += [(child, self.weightings[child])]
        print(d)

        t = [k for k in d.items() if len(k[1]) == 1]
        head = t[0][1][0][0]
        d.clear()
        for child in self.structure[head]:
            d[self.determine_subtree_weighting(child)] += [(child, self.weightings[child])]
        print(d)

        t = [k for k in d.items() if len(k[1]) == 1]
        head = t[0][1][0][0]
        d.clear()
        for child in self.structure[head]:
            d[self.determine_subtree_weighting(child)] += [(child, self.weightings[child])]
        print(d)

        t = [k for k in d.items() if len(k[1]) == 1]
        head = t[0][1][0][0]
        d.clear()
        for child in self.structure[head]:
            d[self.determine_subtree_weighting(child)] += [(child, self.weightings[child])]
        print(d)

        print(f"Part 02: {tlt}")


if __name__ == "__main__":
    sol: Solution = Solution.parse_input()

    print(Timing(timeit(sol.part_01, number=1)).result(), "\n")
    print(Timing(timeit(sol.part_02, number=1)).result(), "\n")
