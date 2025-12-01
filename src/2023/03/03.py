from dataclasses import dataclass
from math import prod
from re import finditer
from timeit import timeit


@dataclass
class Cell:
    value: int  # -1 is a . and -2 is any other symbol


class Grid:
    def __init__(self):
        # Parsing input
        self._grid: list[list[Cell]] = []
        with open("input.txt", "r") as file:
            for line in file.read().splitlines():
                found_numbers = [(int(x.group(0)), (x.start(), x.end())) for x in list(finditer(r"(\d+)", line))]

                row: list[Cell] = []
                num, coords = found_numbers.pop(0) if len(found_numbers) != 0 else (None, None)

                for i, val in enumerate(line.strip()):
                    if num is None and coords is None:
                        if val == "*":
                            row.append(Cell(-3))
                        elif val != ".":
                            row.append(Cell(-2))
                        else:
                            row.append(Cell(-1))
                        continue

                    if i in range(coords[0], coords[1]):
                        row.append(Cell(num))

                    elif val.isdigit() and i > coords[1]:
                        if len(found_numbers) != 0:
                            num, coords = found_numbers.pop(0)
                            row.append(Cell(num))

                    else:
                        if val == "*":
                            row.append(Cell(-3))
                        elif val != ".":
                            row.append(Cell(-2))
                        else:
                            row.append(Cell(-1))
                self.grid.append(row)

    @property
    def grid(self):
        """Get Grid"""
        return self._grid

    def check_has_symbol_in_surrounding_cell(self, row: int, col: int) -> tuple[bool, int]:
        """Checking surrounding cells of given cell for symbol. Ture if present, else False"""
        for x in [-1, 0, 1]:
            for y in [-1, 0, 1]:
                try:
                    if self.grid[row + x][col + y].value in [-2, -3]:
                        return True, self.grid[row + x][col + y].value

                except Exception:
                    continue
        return False, 0


def part_1(grid: Grid) -> int:
    """Solving Part 1"""
    # Going through grid and checking surrounding values.
    # If a symbol is present in the surrounding of that number, keep, else continue
    res: list[int] = []

    # print(grid.grid)
    for x in range(len(grid.grid)):
        valid_numbers: list[int] = []
        for y in range(len(grid.grid[0])):
            has, _ = grid.check_has_symbol_in_surrounding_cell(x, y)
            if grid.grid[x][y].value > 0 and has:
                valid_numbers.append(grid.grid[x][y].value)

        if valid_numbers:
            s: int = valid_numbers.pop(0)
            res.append(s)
            for n in valid_numbers:
                if n != s:
                    res.append(n)
                    s = n

    return sum(res)


def part_2(grid: Grid) -> int:
    """Solve Part 2"""
    res: list[int] = []

    # print(grid.grid)
    for x in range(len(grid.grid)):
        valid_numbers: list[int] = []
        for y in range(len(grid.grid[0])):
            has, sym = grid.check_has_symbol_in_surrounding_cell(x, y)
            if has and (sym == -3 or grid.grid[x][y].value > 0):
                valid_numbers.append((x, y, grid.grid[x][y].value, sym))

        if valid_numbers:
            s = valid_numbers.pop(0)
            curr_num = s[2]
            res.append((s[0], s[1], s[2]))
            for n in valid_numbers:
                if n[2] != curr_num:
                    res.append((s[0], s[1], s[2]))
                    curr_num = n[2]
    # print(res)
    v = [x for x in res if x[-1] > 0]
    y = [x for x in res if x[-1] < 0]

    t = []
    for r, c, _ in set(y):
        l = []
        # find nums in v that have corresponding row or col nums
        for r1, c1, k in v:
            if r == r1:
                l.append(k)
            elif c == c1:
                l.append(k)
        print(l, set(l))
        t.append(prod(set(l)))
    print(t)
    return sum(t)
    # return sum(res)


def main() -> None:
    """Entry point to solving problem"""
    grid: Grid = Grid()

    # print(f"Part 1: {part_1(grid)}")
    print(f"Part 2: {part_2(grid)}")


if __name__ == "__main__":
    print(timeit(main, number=1))
