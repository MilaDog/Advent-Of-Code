from timeit import timeit

from timing import Timing


def calculate_difference_level_for_mirrored_values(pair) -> int:
    """Calculate the difference level between two mirrored values. Difference level indicated by smudge level"""
    return sum(a != b for a, b in zip(pair[0], pair[1]))


def solve(grid, smudge_level) -> int:
    for i in range(1, len(grid)):
        right_side = grid[i:]
        left_side = grid[:i][::-1]
        search_length = min(len(right_side), len(left_side))

        difference_count: list[int] = []
        for mirrored_pair in zip(left_side[:search_length], right_side[:search_length]):
            difference_count.append(calculate_difference_level_for_mirrored_values(mirrored_pair))

        if sum(difference_count) == smudge_level:
            return i

    return 0


def main() -> None:
    """Entry point to solving the problem"""
    with open("input.txt", "r") as file:
        data = file.read()
    grids = data.strip().split("\n\n")

    for i in [False, True]:
        res = 0
        for grid in grids:
            rows = [list(line) for line in grid.strip().split("\n")]
            cols = list(zip(*rows))

            val = solve(rows, i)
            if val > 0:
                res += 100 * val
            else:
                res += solve(cols, i)

        print(f"Part {i+1}: {res}")


if __name__ == "__main__":
    print(Timing(timeit(main, number=1)).milliseconds, "milliseconds")
