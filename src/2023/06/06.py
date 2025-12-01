from dataclasses import dataclass
from math import prod
from re import findall
from timeit import timeit

TEST_DATA: str = """Time:      7  15   30
Distance:  9  40  200"""


@dataclass
class Race:
    time: int
    distance: int

    @classmethod
    def parse(cls, data: str):
        """Parse Parse the race data. Return list of all Races

        Args:
            data (str): Race data to parse
        """
        times, distances = [list(map(int, findall(r"(\d+)", line))) for line in data.strip().splitlines()]

        res: list[Race] = [Race(x, y) for (x, y) in zip(times, distances)]

        return res


def binary_search(race: Race) -> int:
    """binary_search Use of a binary search to find the number of ways that the boat button can be held to win the race.

    Args:
        race (Race): Race to search

    Returns:
        int: Number of ways that the race can be won
    """
    # Want to know
    # 1) Lowest Value s.t. boat travel distance > current winning race distance
    # 2) Highest Value s.t. boat travel distance > current winning race distance
    # Since graph reflects about axis (time/2), highest can be calculated.

    lower, upper = 1, race.time // 2

    while lower + 1 < upper:
        mid: int = (upper + lower) // 2
        boat_travel_distance: int = mid * (race.time - mid)

        if boat_travel_distance > race.distance:
            upper = mid

        else:
            lower = mid

    lowest: int = upper
    highest: int = int((race.time / 2) + (race.time / 2 - lowest))

    return highest - lowest + 1


def solve(races: list[Race]) -> int:
    """Solve Solve Part 1 for the day.

    Args:
        data (list[list[int]]): Data to use

    Returns:
        int: Answer to Part 1
    """
    res: list[int] = [binary_search(race) for race in races]
    return prod(res)


def main() -> None:
    """Entry point to solving  the day's problems"""
    # data = TEST_DATA

    with open("input.txt", "r") as file:
        data: str = file.read().strip()

    races: list[Race] = Race.parse(data)
    print(f"Part 1: {solve(races)}")

    race_time: str = "".join(str(race.time) for race in races)
    race_distance: str = "".join(str(race.distance) for race in races)
    part_2_race: Race = Race(int(race_time), int(race_distance))
    print(f"Part 2: {solve([part_2_race])}")


if __name__ == "__main__":
    print(timeit(main, number=1))
