# Advent of Code, 2023 Day 04
# MilaDog

from timeit import timeit
from dataclasses import dataclass

TEST_DATA: str = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""


@dataclass
class SingleRange:
    start: int
    end: int

    @classmethod
    def parse(cls, data: tuple[int, int]):
        """
        parse Parse the given range. Result: [start, end)]

        Args:
            data (tuple):Range data to parse
        """
        start_, lngth = data
        return SingleRange(start_, start_ + lngth)


def parse_data_map(data: str) -> list[int]:
    """Parse the given mapping into its parts: (destination start, source start, range length)"""
    return list(map(int, data.strip().split()))


def parse_seed_ranges(seeds: list[int]) -> list[tuple[int, int]]:
    """Parse the given seeds into pairs of two: (i, i+1)
    This represents the range: [start, end)"""
    return [SingleRange.parse(x) for x in list(zip(seeds[::1], seeds[1::2]))]


def parse_input() -> list:
    """Parse given input. Return list of necessary data"""
    res: list[str] = []

    # with open("input.txt", "r") as file:
    #     sections: list[str] = file.read().strip().split("\n\n")

    sections = TEST_DATA.strip().split("\n\n")

    # Seeds section
    res.append(list(map(int, sections[0].split(" ")[1:])))

    # Parsing mapping section
    for section in sections[1:]:
        parts: list[str] = section.strip().split("\n")
        res.append([parse_data_map(x) for x in parts[1:]])

    return res


def part_1() -> int:
    """Solving Parts"""
    data: list[str] = parse_input()

    # Getting seeds
    seeds: list[int] = data[0]
    res: dict = {s: [] for s in seeds}

    # Going through each section
    for section in data[1:]:
        for seed, path in res.items():
            key: int = seed if len(path) == 0 else path[-1]

            for line in section:
                dest, src, lngth = line

                if src <= key < (src + lngth):
                    idx: int = key - src
                    key = dest + idx
                    break

            path.append(key)
            res[seed] = path

    # Getting lowest location number
    location_nums: list[int] = [x[-1] for x in res.values()]
    return min(location_nums)


def part_2() -> int:
    """Solving Part 2"""
    data: list[int] = parse_input()
    seeds: list[SingleRange] = parse_seed_ranges(data.pop(0))

    # Going through each section
    locations: list[SingleRange] = []
    for section in data:
        seed_ranges = seeds
        res = []

        # Splitting the ranges
        while seed_ranges:
            curr_seed = seed_ranges.pop()

            for dest, src, lngth in section:
                section_range = SingleRange(src, src + lngth)

                # Range is completely outside, continue
                if (
                    curr_seed.start >= section_range.end
                    or curr_seed.end <= section_range.start
                ):
                    continue

                # Range is to the left, get left side range and add back
                if curr_seed.start <= section_range.start:
                    # Getting range and adding back
                    left_range = SingleRange(curr_seed.start, section_range.start)
                    seed_ranges.append(left_range)

                    # Updating current curr_seed
                    curr_seed = SingleRange(section_range.start, curr_seed.end)

                # Range is to the right, get right side range and add back
                if curr_seed.end > section_range.end:
                    # Getting range and adding back
                    right_range = SingleRange(section_range.end, curr_seed.end)
                    seed_ranges.append(right_range)

                    # Updating current curr_seed
                    curr_seed = SingleRange(curr_seed.start, section_range.end)

                # Range is completely inside, completed
                if (
                    curr_seed.start >= section_range.start
                    and curr_seed.end <= section_range.end
                ):
                    # Updating seed_range
                    start: int = dest + (curr_seed.start - section_range.start)
                    end: int = dest + (curr_seed.end - section_range.end)
                    curr_seed = SingleRange(start, end)
                    break

            res.append(curr_seed)
        locations += res
        res = []

    # Getting smallest location number
    location_values: list[int] = [x.start for x in locations]
    print(locations)
    return min(location_values)


def main() -> None:
    """Solving problem"""
    print(f"Part 1: {part_1()}")
    print(f"Part 2: {part_2()}")


if __name__ == "__main__":
    print(timeit(main, number=1))
