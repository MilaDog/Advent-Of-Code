from timeit import timeit

from common.python.timing import Timing


def read_data() -> str:
    with open("input.txt", "r") as file:
        data: str = file.read().strip()

    return data


def parse_data(data: str) -> list[list[str]]:
    """Parse the input data into useable form"""
    return [list(row.strip()) for row in data.splitlines()]


def step(dirr: str) -> tuple[int, int]:
    """Make step into next cell"""
    return [(0, 1), (0, -1), (1, 0), (-1, 0)]["RLDU".index(dirr)]


def solve(grid: list[list[str]], start: tuple[int, int, str]) -> int:
    """Solve the problem, return the number of energised cells"""

    visited_cells: set = set()  # tuple[x, y, direction]
    unvisited_directions: list[tuple[int, int, str]] = [start]

    while unvisited_directions:
        curr = unvisited_directions.pop()

        if curr in visited_cells:
            continue

        # Cell has been visited
        visited_cells.add(curr)

        # breaking up tuple
        x, y, dirr = curr
        dx, dy = step(dirr)

        if 0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[0]):
            if grid[x + dx][y + dy] == ".":
                # Make step.
                unvisited_directions.append((x + dx, y + dy, dirr))

            elif grid[x + dx][y + dy] == "/":
                # Make step. Rotate 90
                # print(curr)
                # print(grid[curr[0]][curr[1]])
                if dirr == "R":
                    unvisited_directions.append((x + dx, y + dy, "U"))
                elif dirr == "L":
                    unvisited_directions.append((x + dx, y + dy, "D"))
                elif dirr == "U":
                    unvisited_directions.append((x + dx, y + dy, "R"))
                elif dirr == "D":
                    unvisited_directions.append((x + dx, y + dy, "L"))

            elif grid[x + dx][y + dy] == "\\":
                # Make step. Rotate 90
                if dirr == "R":
                    unvisited_directions.append((x + dx, y + dy, "D"))
                elif dirr == "L":
                    unvisited_directions.append((x + dx, y + dy, "U"))
                elif dirr == "U":
                    unvisited_directions.append((x + dx, y + dy, "L"))
                elif dirr == "D":
                    unvisited_directions.append((x + dx, y + dy, "R"))

            elif grid[x + dx][y + dy] == "|":
                # Make step. Rotate 90
                if dirr in ["R", "L"]:
                    unvisited_directions.append((x + dx, y + dy, "U"))
                    unvisited_directions.append((x + dx, y + dy, "D"))
                else:
                    unvisited_directions.append((x + dx, y + dy, dirr))

            elif grid[x + dx][y + dy] == "-":
                # Make step. Rotate 90
                if dirr in ["U", "D"]:
                    unvisited_directions.append((x + dx, y + dy, "R"))
                    unvisited_directions.append((x + dx, y + dy, "L"))
                else:
                    unvisited_directions.append((x + dx, y + dy, dirr))

    return len(set((x, y) for x, y, _ in visited_cells))


def main() -> None:
    """Entry point to solving the problem"""
    grid: list[list[str]] = parse_data(read_data())
    print(f"Part 1: {solve(grid, (0, -1, 'R')) - 1}")  # -1 due to starting outside the grid

    # Part 2
    ans: int = 0
    for i in range(len(grid)):
        ans = max(ans, solve(grid, (i, 0, "R")))
        ans = max(ans, solve(grid, (i, len(grid[0]) - 1, "L")))

    for i in range(len(grid[0])):
        ans = max(ans, solve(grid, (0, i, "D")))
        ans = max(ans, solve(grid, (len(grid) - 1, i, "U")))

    print(f"Part 2: {ans}")


if __name__ == "__main__":
    print(Timing(timeit(main, number=1)).milliseconds, "milliseconds")
