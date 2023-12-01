from re import findall

DIGIT_WORDS = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]


def part1(lines: list[str]) -> int:
    """Solution to Part 1"""
    total: int = 0

    for line in lines:
        digits: list[str] = findall(r"\d", line)
        total += int(digits[0] + digits[-1])

    return total


def part2(lines: list[str]) -> int:
    """Solution to Part 2"""
    total: int = 0

    for line in lines:
        found = findall(r"(?=(" + "|".join(DIGIT_WORDS[1:]) + r"|\d))", line)
        first, last = found[0], found[-1]

        if not first.isdigit():
            first = str(DIGIT_WORDS.index(first))
        if not last.isdigit():
            last = str(DIGIT_WORDS.index(last))

        total += int(first + last)

    return total


def main() -> None:
    with open("input.txt") as file:
        lines: list = file.read().strip().split("\n")

    print(f"Part 1: {part1(lines)}")
    print(f"Part 2: {part2(lines)}")


if __name__ == "__main__":
    import timeit

    print(timeit.timeit(main, number=1))
