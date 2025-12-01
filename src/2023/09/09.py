from functools import reduce
from itertools import pairwise
from timeit import timeit

from timing import Timing


def get_histories() -> list[str]:
    """Read in history values and return"""
    with open("input.txt", "r") as file:
        data: str = file.read()

    return [line for line in data.splitlines()]


def parse_history_line(line: str) -> list[int]:
    """Parse history line, return list of values"""
    return list(map(int, line.strip().split()))


def get_history_report(history: list[int]) -> list[list[int]]:
    """Make history report"""
    res: list[list[int]] = [history.copy()]

    curr_history: list[int] = history.copy()
    while set(curr_history) != {0}:
        temp = [curr - prev for prev, curr in pairwise(curr_history)]
        res.append(temp)
        curr_history = temp

    return res


def get_history_reports(histories: list[list[int]]) -> list[list[list[int]]]:
    """Generate the full history report for each history"""
    return [get_history_report(history) for history in histories]


def get_part_1(reports) -> int:
    """Determine the next value in the sequence"""
    history_reports_next_sequence_value: list[int] = []

    for report in reports:
        vals: list[int] = [x[-1] for x in report]
        history_reports_next_sequence_value.append(sum(vals))

    return sum(history_reports_next_sequence_value)


def get_part_2(reports) -> int:
    """Determine the previous value in the sequence: i.e. before the start"""
    history_reports_next_sequence_value: list[int] = []

    for report in reports:
        history_reports_next_sequence_value.append(reduce(lambda a, b: b - a, [r[0] for r in reversed(report)]))

    return sum(history_reports_next_sequence_value)


def main() -> None:
    """Entry point to problem"""
    histories: list[list[int]] = [parse_history_line(line) for line in get_histories()]
    reports = get_history_reports(histories)

    print("Part 1:", get_part_1(reports))
    print("Part 2:", get_part_2(reports))


if __name__ == "__main__":
    t = Timing(timeit(main, number=1))
    print(t.microseconds, "ms")
