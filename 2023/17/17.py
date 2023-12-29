from enum import Enum
from timeit import timeit
from collections import namedtuple, defaultdict
from heapq import heappop, heappush

from common.python.timing import Timing

class Directions(Enum):
    NORTH: tuple[int, int] = (-1, 0)
    EAST: tuple[int, int] = (0, 1)
    SOUTH: tuple[int, int] = (1, 0)
    WEST: tuple[int, int] = (0, -1)

class Node:
    def __init__(self, weight: int, distance: int, coords: namedtuple):
        self.weight = weight
        self.distance = distance
        self.coords = coords

    def __lt__(self, other) -> bool:
        return self.distance < other.distance
    
    def __str__(self) -> str:
        """Stringed version of data"""
        return f"Node: weight={self.weight}; distance={self.distance}; coords={self.coords}"
    
    def __repr__(self) -> str:
        """Stringed version of data"""
        return f"Node: weight={self.weight}; distance={self.distance}; coords={self.coords}"

class Grid:
    def __init__(self, data: str) -> None:
        self.grid: list[list[Node]] = self._parse_data(data)
        self.height: int = len(self.grid)
        self.width: int = len(self.grid[0])

    @classmethod
    def read_file(cls):
        """Read in input"""
        with open("input.txt", "r") as file:
            data: str = file.read().strip()

        return cls(data)

    @staticmethod
    def _parse_data(data: str) -> list[list[Node]]:
        """Part the input data and return a matrix of Nodes"""
        coords_: namedtuple = namedtuple("Coords", "x, y")

        res: list[list[Node]] = []
        for x, line in enumerate(data.strip().splitlines()):
            row: list[Node] = []
            for y, weight in enumerate(list(line.strip())):
                row.append(Node(int(weight), 0, coords_(x, y)))
            
            res.append(row)

        return res
    
    def within_grid(self, x: int, y: int) -> bool:
        """Check if the current node is within the grid"""
        return 0 <= x < self.height - 1 and 0 <= y < self.width -1
    
    def get_adjacent_nodes(self, node: Node, cannot_go: Directions = None) -> list[Node] | None:
        """Get a list of all adjacent nodes and their direction"""
        if node is None:
            return None

        res = []
        adj_: namedtuple = namedtuple("ADJ", "x, y, dirr")

        valid_directions = (set(Directions) ^ set(cannot_go)) if cannot_go is not None else Directions

        for dirr in valid_directions:
            dx, dy = dirr.value

            # Calculate if new location is within the grid
            if self.within_grid(node.coords.x + dx, node.coords.y + dy):
                res.append(adj_(node.coords.x + dx, node.coords.y + dy, dirr))

        return res if res else None



def solve(grid: Grid, start: Node) -> int:
    """Solve the problem. Return the distance of shortest path"""
    pq: list = [(start, (None, 0))]   # tuple[Node, tuple[Direction, step_count]]
    visited = set()

    distances: defaultdict[Node, int] = {}

    while pq:
        curr, step = heappop(pq)
        distances[curr] = curr.distance

        # Checking if Node has been visited
        if curr in visited:
            continue
        visited.add(curr)

        # Looping through adjacent Nodes:
        for adj in grid.get_adjacent_nodes(curr, step[0] if step[1] == 3 else None):
            adjacent_node: Node = grid.grid[adj.x][adj.y]

            # Cannot travel backwards
            if adjacent_node in visited:
                continue

            # Checking if the next node to visit is the destination
            # if (adjacent_node.coords.x, adjacent_node.coords.y) == (len(grid.grid)-1, len(grid.grid[0])-1):
            #     return curr.distance + adjacent_node.weight

            # if adjacent_node not in distances:
            #     distances[adjacent_node] = adjacent_node.weight

            # else: 
            if curr.distance + adjacent_node.weight < adjacent_node.distance:
                adjacent_node.distance = curr.distance + adjacent_node.weight

                step_cnt: int = step[1]+ 1 if step[0] == adj.dirr else 0
                grid.grid[adj.x][adj.y] = adjacent_node
                heappush(pq, (adjacent_node, (adj.dirr, step_cnt)))
    
    return grid.grid[grid.height-1][grid.width-1].distance

def main() -> None:
    """Main entry point for problem"""
    grid: Grid = Grid.read_file()

    # Starting point
    start: Node = grid.grid[0][0]
    start.weight = 0

    print(f"Part 1: {solve(grid, start)}")


if __name__ == "__main__":
    print(Timing(timeit(main, number=1)).seconds, "seconds")
