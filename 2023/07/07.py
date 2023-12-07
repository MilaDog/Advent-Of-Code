from timeit import timeit
from dataclasses import dataclass
from collections import Counter


@dataclass(frozen=True)
class Hand:
    hand: str
    bid: int
    order: int = -1


class Hands:
    def __init__(self):
        with open("input.txt", "r") as file:
            data: str = file.read().strip()

        self.hands: list[Hand] = [Hands.parse_line(line) for line in data.splitlines()]

    @classmethod
    def parse_line(cls, line: str) -> Hand:
        """Parse input line and return Hand object of data"""
        hand_, bid = line.strip().split(" ")
        return Hand(hand_, int(bid))

    def calculate_hand_strength(
        self, hand: Hand, part_2: bool = False
    ) -> tuple[int, int]:
        """
        calculate_hand_strength Determine the strength of the given hand

        Args:
            hand (Hand): Hand to have its strength determined
            part_2 (bool, optional): Whether hand falls into Part 2of the problem. Defaults to False.

        Returns:
            tuple[int, int]: Returns the strength of the hand, as well as the modified hand. Allows for sorting.
        """
        curr_hand = hand.hand

        # Replacing some characters to make sorting and counting easier
        curr_hand = curr_hand.replace("T", chr(ord("9") + 1))
        curr_hand = curr_hand.replace("Q", chr(ord("9") + 3))
        curr_hand = curr_hand.replace("K", chr(ord("9") + 4))
        curr_hand = curr_hand.replace("A", chr(ord("9") + 5))
        curr_hand = (
            curr_hand.replace("J", chr(ord("9") + 2))
            if not part_2
            else curr_hand.replace("J", chr(ord("2") - 1))
        )

        if hand.order != -1:
            return hand.order, curr_hand

        hand_count: Counter = Counter(curr_hand)
        match sorted(hand_count.values(), reverse=True):
            case [5]:
                return 7, curr_hand
            case [4, 1]:
                return 6, curr_hand
            case [3, 2]:
                return 5, curr_hand
            case [3, 1, 1]:
                return 4, curr_hand
            case [2, 2, 1]:
                return 3, curr_hand
            case [2, 1, 1, 1]:
                return 2, curr_hand
            case [1, 1, 1, 1, 1]:
                return (1, curr_hand)
            case _:
                assert f"{False}, {hand}, {hand_count}, {curr_hand}"


def part_1(hands: Hands) -> int:
    """
    part_1 Determine the answer to Part 1

    Args:
        hands (Hands): All Hands that need to be processed

    Returns:
        int: Answer to problem
    """
    values: list[int] = sorted(
        hands.hands, key=lambda x: hands.calculate_hand_strength(x, False)
    )
    res: list[int] = [(x.bid * (i + 1)) for i, x in enumerate(values)]
    return sum(res)


def part_2(hands: Hands) -> int:
    """
    part_2 Determine the answer to Part 2

    Args:
        hands (Hands): All Hands that need to be processed

    Returns:
        int: Answer to problem
    """
    hands_res: list[Hand] = []
    for hand in hands.hands:
        t = []
        for l in "23456789TQKA":
            curr: Hand = Hand(hand.hand.replace("J", l), hand.bid)
            t.append((hands.calculate_hand_strength(curr), (hand.hand, curr.bid)))
        hands_res.append(max(t))

    hands_res = [Hand(y[0], y[1], x[0]) for x, y in hands_res]
    values: list[int] = sorted(
        hands_res, key=lambda x: hands.calculate_hand_strength(x, True)
    )
    res: list[int] = [(x.bid * (i + 1)) for i, x in enumerate(values)]
    return sum(res)


def main() -> None:
    """Entry point for problem"""
    hands: Hands = Hands()

    print(f"Part 1: {part_1(hands)}")
    print(f"Part 2: {part_2(hands)}")


if __name__ == "__main__":
    print(timeit(main, number=1))
