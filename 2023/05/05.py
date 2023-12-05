# Advent of Code, 2023 Day 04
# MilaDog

from timeit import timeit

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

def parse_data_map(data: str) -> list[int]:
    """Parse the given mapping into its parts: (destination start, source start, range length)"""
    return list(map(int, data.strip().split()))

def parse_input() -> list:
    """Parse given input. Return list of necessary data"""
    res: list[str] = []

    with open("input.txt") as file:
        sections: list[str] = file.read().strip().split("\n\n") 

    # Seeds section
    res.append(list(map(int, sections[0].split(" ")[1:])))

    # Parsing mapping section
    for section in sections[1:]:
        parts: list[str] = section.strip().split("\n")
        res.append([parse_data_map(x) for x in parts[1:]])

    return res

def solve() -> None:
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
    print(f"Part 1: {min(location_nums)}")

def main() -> None:
    """Solving problem"""
    solve()

if __name__ == "__main__":
    print(timeit(main, number=1))