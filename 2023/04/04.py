# Advent of Code, 2023 Day 04
# MilaDog

from collections import defaultdict
from timeit import timeit
from re import findall

TEST_DATA: str = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""


def calculate_scratch_card_winning_numbers(
    drawn_numbers: set[int], scratch_card_numbers: set[int]
) -> list[int]:
    """Determine the winning numbers that the given srcatch card has based on the given drawn winning numbers"""
    return drawn_numbers & scratch_card_numbers


def parse_scratch_cards(lines: list[str]) -> dict:
    """Parse the input and return a dictionary of results: Card Number: [winning_numbers, scratch_card_numbers]"""
    res: dict[int, list[set[int]]] = {}

    for line in lines:
        card, data = line.strip().split(": ")
        card_number: int = int(card[5:])
        data_nums: list[str] = data.strip().split(" | ")

        winning_nums: set(int) = set(map(int, findall(r"(\d+)", data_nums[0])))
        scratch_nums: set(int) = set(map(int, findall(r"(\d+)", data_nums[1])))

        res[card_number] = [winning_nums, scratch_nums]

    return res


def part_1(data: dict) -> int:
    """Parse each line and calculate winning score. Return total for all lines"""

    res: list[int] = []

    for winning_nums, scratch_nums in data.values():
        win_cnt: int = len(
            calculate_scratch_card_winning_numbers(winning_nums, scratch_nums)
        )
        # Formula to calculate score: 2^(n-1)
        res.append(int(pow(2, win_cnt - 1)))

    return sum(res)


def part_2(data: dict) -> int:
    """Calculate the number of total scratch cards experienced"""

    res = defaultdict(int)

    for i, card_data in enumerate(data.values()):
        res[i] += 1

        wins: list[int] = calculate_scratch_card_winning_numbers(
            card_data[0], card_data[1]
        )

        if not wins:
            continue

        for j in range(1, len(wins) + 1):
            # Eg: Card 1 has 3 winning numbers, so card 2 through 4 gain a copy.
            # Since we have only 1 Card 1 (original), Cards 2-4 get an extra.
            # For Card 2, 2 winning numbers are found, so extra cards for Cards 3-4.
            # Since Card 2 now has 2 (1 original + copy from previous card winning), we add the current number of Card 2
            # to the following numbers. And so on...
            res[i + j] += res[i]

    return sum(res.values())


def main() -> None:
    # lines = TEST_DATA.splitlines()
    # data = parse_scratch_cards(lines)

    with open("input.txt", "r") as file:
        lines = file.readlines()
        data = parse_scratch_cards(lines)

    print(f"Part 1: {part_1(data)}")
    print(f"Part 2: {part_2(data)}")


if __name__ == "__main__":
    print(timeit(main, number=1))
