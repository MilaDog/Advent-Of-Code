import re
from collections import defaultdict
from functools import reduce
from operator import mul
from timeit import timeit

from src.common.python.timing import Timing


class Robot:
    """Robot in the problem."""

    def __init__(self, initial_position: tuple[int, int], velocity: tuple[int, int]) -> None:
        self.position: tuple[int, int] = initial_position
        self.velocity: tuple[int, int] = velocity

    def calculate_position_change(self, repeat: int, grid_bounds: tuple[int, int]) -> tuple[int, int]:
        """Calculate the new position of the Robot after `repeat` amount of times.

        Args:
            repeat (int):
                Number of times for the Robot to change its position.
            grid_bounds (tuple[int, int]):
                Bounds of the grid that the Robot can move in.

        Returns:
            tuple[int, int]
                New Robot position.
        """
        x: int = (self.position[0] + self.velocity[0] * repeat) % grid_bounds[0]
        y: int = (self.position[1] + self.velocity[1] * repeat) % grid_bounds[1]

        return x, y

    def __repr__(self) -> str:
        return f"Robot[position:{self.position}, velocity:{self.velocity}]"

    def __str__(self) -> str:
        return f"Robot[position:{self.position}, velocity:{self.velocity}]"


class Solution:
    """Solutions to the problems."""

    def __init__(self, data: list[Robot]) -> None:
        self.robots: list[Robot] = data
        self.grid_bounds: tuple[int, int] = (101, 103)

    @classmethod
    def parse_input(cls) -> "Solution":
        """Parse the problem data input to be used.

        Returns:
            Solution:
                Class instance with the parsed input data.
        """
        with open("input.txt", "r") as file:
            values: list[Robot] = []

            x: int
            y: int
            vx: int
            vy: int
            for line in file.readlines():
                x, y, vx, vy = map(int, re.findall(r"-*\d+", line.strip()))
                values.append(Robot(initial_position=(x, y), velocity=(vx, vy)))

        return cls(data=values)

    def display_robots(self, robots: list[tuple[int, int]]) -> bool:
        """Display the Robot positions.

        Args:
            robots (list[Robot]):
                Robots to display.

        Returns:
            bool:
                If a tree was displayed or not.
        """
        grid: list[list[str]] = [["-" for _ in range(self.grid_bounds[0])] for _ in range(self.grid_bounds[1])]

        for robot in robots:
            grid[robot[1]][robot[0]] = "1"

        lines = ["".join(line) for line in grid]

        if any("1111111111" in line for line in lines):
            for line in lines:
                print(line)
            print()
            return True
        return False

    def part_01(self) -> None:
        """Solve Part 01 of the problem.

        Returns:
            None
        """
        # Update Robot positions.
        updated_robot_positions: dict[tuple[int, int], int] = defaultdict(int)
        for robot in self.robots:
            new_position: tuple[int, int] = robot.calculate_position_change(repeat=100, grid_bounds=self.grid_bounds)
            updated_robot_positions[new_position] += 1

        # Calculate number of Robots in regions
        x_mid: int = self.grid_bounds[0] // 2
        y_mid: int = self.grid_bounds[1] // 2

        grid_sections: dict[int, int] = {1: 0, 2: 0, 3: 0, 4: 0}
        for x in range(self.grid_bounds[0]):
            for y in range(self.grid_bounds[1]):
                if x == x_mid or y == y_mid:
                    continue

                if x < x_mid and y < y_mid:
                    grid_sections[1] += updated_robot_positions.get((x, y), 0)

                elif x > x_mid and y < y_mid:
                    grid_sections[2] += updated_robot_positions.get((x, y), 0)

                elif x < x_mid and y > y_mid:
                    grid_sections[3] += updated_robot_positions.get((x, y), 0)

                elif x > x_mid and y > y_mid:
                    grid_sections[4] += updated_robot_positions.get((x, y), 0)

        tlt: int = reduce(mul, grid_sections.values())
        print(f"Part 01: {tlt}")

    def part_02(self) -> None:
        """Solve Part 02 of the problem.

        Returns:
            None
        """
        tlt: int = 0

        # Update Robot positions.
        for i in range(5000, 10_000):
            updated_robot_positions: dict[tuple[int, int], int] = defaultdict(int)
            for robot in self.robots:
                new_position: tuple[int, int] = robot.calculate_position_change(repeat=i, grid_bounds=self.grid_bounds)
                updated_robot_positions[new_position] += 1
            had_tree: bool = self.display_robots(list(updated_robot_positions.keys()))

            if had_tree:
                tlt = i
                break

        print(f"Part 02: {tlt}")


if __name__ == "__main__":
    sol: Solution = Solution.parse_input()

    print(Timing(timeit(sol.part_01, number=1)).result(), "\n")
    print(Timing(timeit(sol.part_02, number=1)).result(), "\n")
