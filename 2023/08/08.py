from timeit import timeit
from dataclasses import dataclass
from re import findall
from itertools import cycle
from math import lcm


@dataclass(frozen=True)
class NodeCoords:
    left: str
    right: str

    @classmethod
    def parse(cls, line: str):
        """Parse an input line into the required Node"""
        parts: list[str] = list(findall(r"(\w+)", line.split("=")[-1]))

        return NodeCoords(parts[0], parts[1])

    def get_coord_from_direction(self, direction: str) -> str:
        """Return the cordinate for the Node based on the given direction"""
        return self.left if direction == "L" else self.right


def camel_walk(instruct: str, nodes: dict[str, NodeCoords], start: str) -> int:
    """Camel walk till Node ends with 'Z'"""
    curr: str = start

    for cnt, dir in enumerate(cycle(instruct), 1):
        curr = nodes[curr].get_coord_from_direction(dir)

        if curr[-1] == "Z":
            return cnt
    return -1


def part_1(instruct: str, nodes: dict[str, NodeCoords]) -> int:
    """Calculate the number of steps taken to reach Node 'ZZZ'"""
    return camel_walk(instruct, nodes, "AAA")


def part_2(instruct: str, nodes: dict[str, NodeCoords]) -> int:
    """Calculate the number of steps taken for all nodes ending with A to reach node ending with Z"""
    nodes_ending_with_a: list[str] = [x for x in nodes.keys() if x[-1] == "A"]
    return lcm(*[camel_walk(instruct, nodes, start) for start in nodes_ending_with_a])


def main() -> None:
    """Main entry point for the problem"""
    with open("input.txt", "r") as file:
        data: str = file.read()

    instruct, elements = data.strip().split("\n\n")
    nodes: dict[str, NodeCoords] = {x.split("=")[0].strip(): NodeCoords.parse(x) for x in elements.split("\n")}

    print(f"Part 1: {part_1(instruct.strip(), nodes)}")
    print(f"Part 2: {part_2(instruct.strip(), nodes)}")


if __name__ == "__main__":
    print(timeit(main, number=1))
