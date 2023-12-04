# Advent of Code, 2015 Day 07
# MilaDog

from timeit import timeit
from re import findall
from itertools import permutations

TEST_DATA: str = """London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141"""

def parse_line(line: str) -> list:
    _from, _to, dist = findall(r"(\w+) to (\w+) = (\d+)", line)[0]
    return [tuple(sorted((_from, _to))), int(dist)]

def get_unique_locations(data: str) -> set:
    return set(findall(r"([a-zA-Z]+)\s+", data.replace("to", "")))


def solve() -> None:
    with open("input.txt", "r") as file:
        lines = file.readlines()

    # lines = TEST_DATA.splitlines()

    parsed_data = [parse_line(x) for x in lines]
    locations = {data[0]: data[1] for data in parsed_data}
    unique_loc = get_unique_locations("\n".join(lines))

    res = []
    for perm in permutations(unique_loc):
        d: int = 0

        for i, l in enumerate(perm):
            # Handle index out of bounds
            if i == len(perm) - 1:
                break

            x, y = l, perm[i+1]
            d += locations.get(tuple(sorted((x,y))), 0)

        res.append(d)

    print(f"Part 1: {min(res)}")
    print(f"Part 2: {max(res)}")
        

def main() -> None:
    solve()


if __name__ == "__main__":
    print(timeit(main, number=1))
