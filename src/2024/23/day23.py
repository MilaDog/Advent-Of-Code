from collections import Counter, defaultdict
from itertools import combinations
from timeit import timeit

from src.common.python.timing import Timing


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
                # values[to].add(to)
                # values[from_].add(from_)

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
                if a in self.links[b]:
                    if a[0] == "t" or b[0] == "t" or link[0] == "t":
                        if "".join(sorted({a, b, link})) not in seen:
                            seen.add("".join(sorted({a, b, link})))
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

        tlt = ",".join(sorted(longest))
        print(f"Part 02: {tlt}")


if __name__ == "__main__":
    sol: Solution = Solution.parse_input()

    print(Timing(timeit(sol.part_01, number=1)).result(), "\n")
    print(Timing(timeit(sol.part_02, number=1)).result(), "\n")
