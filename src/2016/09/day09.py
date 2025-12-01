from timeit import timeit

from timing import Timing


class Solution:
    def __init__(self, data: str) -> None:
        self.data: str = data

    @classmethod
    def parse_input(cls) -> "Solution":
        """Parse the problem data input to be used.

        Returns:
            Solution:
                Class instance with the parsed input data.
        """
        with open("input.txt", "r") as file:
            value: str = file.read().strip()

        return cls(data=value)

    def decompress(self, data: str) -> tuple[str, bool]:
        changed: bool = False
        cnt: int = 0
        length: int = len(data)

        res: str = ""
        while cnt < length:
            # Checking for start of repeat
            if data[cnt] == "(":
                i: int = cnt

                # Getting the end
                while data[i] != ")":
                    i += 1

                repeat: str = data[cnt + 1 : i]
                ln, amt = map(int, repeat.split("x"))

                # Getting section to repeat
                section: str = data[i + 1 : i + 1 + ln]
                res += section * amt

                # Update pointer
                cnt = i + 1 + ln

                changed = True
                continue

            res += data[cnt]
            cnt += 1

        return res, changed

    def part_01(self) -> None:
        """Solve Part 01 of the problem.

        Returns:
            None
        """
        res, _ = self.decompress(self.data)
        print(f"Part 01: {len(res)}")

    def part_02(self) -> None:
        """Solve Part 02 of the problem.

        Returns:
            None
        """
        res: str = self.data
        while True:
            res, has_changed = self.decompress(res)

            if not has_changed:
                break

        print(f"Part 02: {len(res)}")


if __name__ == "__main__":
    sol: Solution = Solution.parse_input()

    print(Timing(timeit(sol.part_01, number=1)).result(), "\n")
    print(Timing(timeit(sol.part_02, number=1)).result(), "\n")
