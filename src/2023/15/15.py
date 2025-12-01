from dataclasses import dataclass
from functools import reduce
from re import findall
from timeit import timeit

from timing import Timing

# class HolidayStringHelper:
#     def __init__(self, data: str):
#         self.steps = self._parse_data(data)

#     @classmethod
#     def read_data(cls):
#         """Read in the given input to solve the problem"""
#         with open("input.txt", "r") as file:
#             data: str = file.read().strip()

#         return cls(data)

#     def _parse_data(self, data: str):
#         """Parse the given data. Return list of Lens and its corresponding operator"""
#         lens = namedtuple("Lens", "label, focal_level, raw")
#         steps: list[str] = [x.strip() for x in data.strip().split(",")]

#         res = []
#         for step in steps:
#             found_values: list[str] = findall(r"^([a-z]+)([=-])(\d?)$", step)[0]
#             res.append((lens(found_values[0], found_values[-1], step), found_values[1]))

#         return res

#     @staticmethod
#     def hash_value(value: str) -> int:
#         """Hash the given value"""
#         return reduce(lambda res, c: ((res + ord(c)) * 17) % 256, value, 0)


# class LensBox:
#     def __init__(self):
#         """Initialise Lens Box"""
#         self.lenses = {}


# def part_1(helper: HolidayStringHelper) -> int:
#     """Solve Part 1 of the problem"""
#     return sum(HolidayStringHelper.hash_value(step[0].raw) for step in helper.steps)

# def part_2(helper: HolidayStringHelper) -> int:
#     """Solve Part 2 of the problem"""
#     lens_boxes: list[LensBox] = [LensBox() for _ in range(256)]

#     for lens, oper in helper.steps:
#         hashed_label: int = HolidayStringHelper.hash_value(lens.label)

#         if oper == "=":
#             pass

#         else:
#             if lens_boxes[hashed_label].lenses.

# def main() -> None:
#     """Main entry point for solving the problem"""
#     helper = HolidayStringHelper.read_data()

#     print(f"Part 1: {part_1(helper)}")


# if __name__ == "__main__":
#     print(Timing(timeit(main, number=1)).microseconds, "microseconds")


@dataclass(frozen=True)
class Lens:
    label: str
    focal_length: int
    operator: str


def parse_input() -> list[str]:
    """Parse the given input"""
    with open("input.txt", "r") as file:
        data: str = file.read().strip()

    return [x.strip() for x in data.split(",")]


def calculate_hash_of_step(step: str) -> int:
    """Calculate the HASH value for the given step"""
    return reduce(lambda res, c: ((res + ord(c)) * 17) % 256, step, 0)


def generate_label_for_step(step: str):
    """Create the necessary label for the step"""
    found_values: list[str] = findall(r"^([a-z]+)([=-])(\d?)$", step)[0]

    if len(found_values[-1]) == 0:
        focal: int = 0
    else:
        focal: int = int(found_values[-1])

    return Lens(label=found_values[0], focal_length=focal, operator=found_values[1])


def main() -> None:
    """Entry point to solving the problem"""
    data: list[str] = parse_input()

    part_1_values: list[int] = [calculate_hash_of_step(step) for step in data]
    print(f"Part 1: {sum(part_1_values)}")

    part_2_values: list[Lens] = [generate_label_for_step(step) for step in data]

    x = [{} for _ in range(256)]

    for s in part_2_values:
        hashed_label: int = calculate_hash_of_step(s.label)

        if s.operator == "=":
            x[hashed_label][s.label] = s.focal_length

        else:
            try:
                x[hashed_label].pop(s.label)
            except Exception:
                continue

    total = 0
    for i, l in enumerate(x, 1):
        for j, f in enumerate(l.values(), 1):
            total += i * f * j

    print(f"Part 2: {total}")


if __name__ == "__main__":
    print(Timing(timeit(main, number=1)).microseconds, "microseconds")
