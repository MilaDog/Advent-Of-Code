def count_smaller_trees(val: int, row: list[int]) -> int:
    for i, x in enumerate(row):
        if x >= val:
            return i + 1
    return len(row)


def solve() -> None:
    grid = [list(map(int, list(x.strip()))) for x in open("input.txt").read().splitlines()]
    grid_zipped = list(map(list, list(zip(*grid))))

    tlt1: int = (len(grid[0]) - 1) * 4  # Getting the edges of visible trees
    tlt2: int = 0

    # Part 1
    for row in range(1, len(grid) - 1):
        for col in range(1, len(grid[0]) - 1):
            val = grid[row][col]
            row_l = grid[row][:col]  # Left of val
            row_r = grid[row][col + 1:]  # Right of val

            val_zipped = grid_zipped[col][row]
            z_row_l = grid_zipped[col][:row]  # Left of val
            z_row_r = grid_zipped[col][row + 1:]  # Right of val

            # Part 2
            p2: int = 1

            p2 *= count_smaller_trees(val, row_l[::-1])
            p2 *= count_smaller_trees(val, row_r)
            p2 *= count_smaller_trees(val_zipped, z_row_l[::-1])
            p2 *= count_smaller_trees(val_zipped, z_row_r)

            if p2 > tlt2:
                tlt2 = p2

            # Part 1
            if val > max(row_l) or val > max(row_r):
                tlt1 += 1
                continue

            if val_zipped > max(z_row_l) or val > max(z_row_r):
                tlt1 += 1
                continue

    print(f"Part 1: {tlt1}")
    print(f"Part 2: {tlt2}")


solve()
