# # Advent of Code, Day 02 2023
# # MilaDog

# # Same problem, just in an OOP style

from dataclasses import dataclass
from math import prod
from timeit import timeit


@dataclass
class Round:
    red: int = 0
    green: int = 0
    blue: int = 0

    @classmethod
    def parse(cls, data: str):
        """Parse Parse the game round, returning Round for all coloured cubes drawn in that round

        Args:
            data (str): Round data
        """
        return Round(**{color: int(count) for count, color in (cube_data.split(" ") for cube_data in data.split(", "))})


@dataclass
class Game:
    id: int
    rounds: list[Round]

    @classmethod
    def parse(cls, data: str):
        """Parse Parse game data, returning object of given game

        Args:
            data (str): Game to parse
        """
        header, game_data = data.split(": ")
        id = int(header.split(" ")[1])

        return Game(
            id,
            [Round.parse(data.strip()) for data in game_data.strip().split("; ")],
        )

    @property
    def get_max_cubes(self):
        """get_max_cubes Returns the max amount of cubes drawn during one round for the game
        """
        return (
            max(r.red for r in self.rounds),
            max(r.green for r in self.rounds),
            max(r.blue for r in self.rounds),
        )

    def is_valid(self):
        """is_valid Determines if the given game is valid or not
        """
        reds, greens, blues = self.get_max_cubes
        return reds <= 12 and greens <= 13 and blues <= 14


def part_1(games: list[Game]) -> int:
    """part_1 Determine the amount of valid games from input and sum the respective Game Number

    Args:
        games (list[Game]): List of Games to check

    Returns:
        int: Sum of all valid Game Numbers
    """
    return sum(game.id for game in games if game.is_valid())


def part_2(games: list[Game]) -> int:
    """part_2 Determine the minimum amount of cubes to make a Game possible, and sum the product of each Game's minimum cube count

    Args:
        games (list[Game]): List of Games to check

    Returns:
        int: Sum of the product of all the minimun amount of cubes possible for the Game
    """
    return sum(prod(game.get_max_cubes) for game in games)


def main() -> None:
    """Entry point for program"""
    with open("input.txt", "r") as file:
        data: str = file.read().strip()

    games = [Game.parse(line) for line in data.splitlines()]
    print(f"Part 1: {part_1(games)}")
    print(f"Part 2: {part_2(games)}")


if __name__ == "__main__":
    print(timeit(main, number=1))
