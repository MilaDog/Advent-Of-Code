from collections import Counter, defaultdict
from itertools import combinations
from timeit import timeit

from timing import Timing


class Solution:
    """Solutions to the problems."""

    def __init__(self, data: dict[str, set[str]]) -> None:
        self.links: dict[str, set[str]] = data

    @classmethod
    def parse_input(cls) -> "Solution":
        """Parse the problem data input to be used.

        Returns:
            Solution:
                Class instance with the parsed input data.
        """
        with open("input.txt", "r") as file:
            values: dict[str, set[str]] = defaultdict(set)

            for line in file.readlines():
                from_, to = line.strip().split("-")
                values[from_].add(to)
                values[to].add(from_)

        return cls(data=values)

    def part_01(self) -> None:
        """Solve Part 01 of the problem.

        Returns:
            None
        """
        tlt: int = 0
        seen: set[str] = set()
        for link in self.links:
            for a, b in combinations(self.links[link], 2):
                if (
                    a in self.links[b]
                    and "t" in (a + b + link)[::2]
                    and (network := "".join(sorted({a, b, link}))) not in seen
                ):
                    seen.add(network)
                    tlt += 1

        print(f"Part 01: {tlt}")

    def part_02(self) -> None:
        """Solve Part 02 of the problem.

        Returns:
            None
        """
        longest: set[str] = set()

        for link in self.links:
            c: Counter[str] = Counter(self.links[link])

            for x in self.links[link]:
                c.update(self.links[x])

            if most_common := c.most_common(1):
                values: list[str] = [k for k, v in c.items() if v >= most_common[-1][1] - 1]
                if len(set(values)) > len(longest):
                    longest = set(values)

        print(f"Part 02: {",".join(sorted(longest))}")


if __name__ == "__main__":
    sol: Solution = Solution.parse_input()

    print(Timing(timeit(sol.part_01, number=1)).result(), "\n")
    print(Timing(timeit(sol.part_02, number=1)).result(), "\n")
