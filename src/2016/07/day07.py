import re
from timeit import timeit

from timing import Timing


class Solution:
    def __init__(self, data: list[str]) -> None:
        self.data: list[str] = data

    @classmethod
    def parse_input(cls) -> "Solution":
        """Parse the problem data input to be used.

        Returns:
            Solution:
                Class instance with the parsed input data.
        """
        with open("input.txt", "r") as file:
            values: list[str] = [line.strip() for line in file.readlines()]

        return cls(data=values)

    def has_abba(self, section: str) -> bool:
        for i in range(0, len(section) - 3):
            window: str = section[i : i + 4]

            if window == window[::-1] and len(set(window)) == 2:
                return True

        return False

    def get_aba(self, section: str) -> list[str]:
        res: list[str] = []
        for i in range(0, len(section) - 2):
            window: str = section[i : i + 3]

            if window == window[::-1] and len(set(window)) == 2:
                res.append(window)

        return res

    def part_01(self) -> None:
        """Solve Part 01 of the problem.

        Returns:
            None
        """
        tlt: int = 0

        for ip in self.data:
            sections: list[str] = re.findall(r"]*(\w+)\[*", ip)
            hypernets: list[str] = re.findall(r"\[(\w+)]", ip)

            if any(self.has_abba(hn) for hn in hypernets):
                continue

            if any(self.has_abba(s) for s in set(sections) - set(hypernets)):
                tlt += 1

        print(f"Part 01: {tlt}")

    def part_02(self) -> None:
        """Solve Part 02 of the problem.

        Returns:
            None
        """
        tlt: int = 0

        for ip in self.data:
            sections: list[str] = re.findall(r"]*(\w+)\[*", ip)
            hypernets: list[str] = re.findall(r"\[(\w+)]", ip)

            for hn in hypernets:
                found: bool = False

                for aba in self.get_aba(hn):
                    target_aba: str = aba[1] + aba[0] + aba[1]
                    if any(target_aba in section for section in set(sections) - set(hypernets)):
                        found = True
                        break

                if found:
                    tlt += found
                    break

        print(f"Part 02: {tlt}")


if __name__ == "__main__":
    sol: Solution = Solution.parse_input()

    print(Timing(timeit(sol.part_01, number=1)).result(), "\n")
    print(Timing(timeit(sol.part_02, number=1)).result(), "\n")
