import re
from collections import defaultdict
from dataclasses import dataclass
from timeit import timeit

from common.python.timing import Timing


@dataclass
class BotAction:
    iD: int
    target_low_id: int
    target_low_type: str
    target_high_id: int
    target_high_type: str


class Solution:
    def __init__(self, data: tuple[list[str], list[str]]) -> None:
        self.data: tuple[list[str], list[str]] = data
        self.outputs: dict[int, list[int]] = defaultdict(list)

    @classmethod
    def parse_input(cls) -> "Solution":
        """
        Parse the problem data input to be used.

        Returns:
            Solution:
                Class instance with the parsed input data.
        """
        with open("input.txt", "r") as file:
            values: list[str] = []
            bots: list[str] = []

            for line in file.readlines():
                if line.startswith("value"):
                    values.append(line)
                else:
                    bots.append(line)

        return cls(data=(values, bots))

    def __parse_bot_action(self, action: str) -> BotAction:
        """
        Parse the given bot action.

        Args:
            action (str):
                Bot action to parse.

        Returns:
            BotAction:
                Class of the bot doing the action, and where the microchips should be sent.
        """
        giver, target_low, target_high = re.findall(r"(output|bot) (\d+)", action)
        return BotAction(
            iD=int(giver[1]),
            target_low_type=target_low[0],
            target_low_id=int(target_low[1]),
            target_high_type=target_high[0],
            target_high_id=int(target_high[1]),
        )

    def __get_next_bot(self, bots: dict[int, list[int]]) -> int:
        """
        Get the next bot to process if it has two available microchips in its inventory.

        Args:
            bots (dict[int, list[int]]):
                All the available bots to search through.

        Returns:
            int:
                ID of the next bot to process.
        """
        possible_bots: list[int] = [k for k, v in bots.items() if len(v) == 2]
        return possible_bots[0] if possible_bots else -1

    def part_01(self) -> None:
        """
        Solve Part 01 of the problem.

        Returns:
            None
        """

        bots: dict[int, list[int]] = defaultdict(list)
        actions: dict[int, list[BotAction]] = defaultdict(list)

        for line in self.data[0]:
            value, iD = map(int, re.findall(r"(\d+)", line))
            bots[iD].append(value)

        for line in self.data[1]:
            bot_action: BotAction = self.__parse_bot_action(line)
            actions[bot_action.iD].append(bot_action)

        # Getting starting bot
        while (curr_bot_id := self.__get_next_bot(bots)) != -1:
            if (sorted(bots[curr_bot_id])) == [17, 61]:
                print(f"Part 1: {curr_bot_id}")

            # Distribute microchips
            action: BotAction = actions[curr_bot_id][0]

            # LOW
            if action.target_low_type == "output":
                self.outputs[action.target_low_id].append(min(bots[curr_bot_id]))

            else:
                bots[action.target_low_id].append(min(bots[curr_bot_id]))

            # HIGH
            if action.target_high_type == "output":
                self.outputs[action.target_high_id].append(max(bots[curr_bot_id]))

            else:
                bots[action.target_high_id].append(max(bots[curr_bot_id]))

            # Clear current bot's chips
            bots[curr_bot_id].clear()

    def part_02(self) -> None:
        """
        Solve Part 02 of the problem.

        Returns:
            None
        """
        tlt: int = self.outputs[0][0] * self.outputs[1][0] * self.outputs[2][0]
        print(f"Part 02: {tlt}")


if __name__ == "__main__":
    sol: Solution = Solution.parse_input()

    print(Timing(timeit(sol.part_01, number=1)).result(), "\n")
    print(Timing(timeit(sol.part_02, number=1)).result(), "\n")
