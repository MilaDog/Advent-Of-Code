from heapq import heappop, heappush

grid = list(
    list(map(int, x)) for x in open("input.txt").read().strip().split("\n"))


def dijsktra(n):
    R = len(grid[0])
    C = len(grid)
    print(R, C)
    seen = set()
    queue = [(0, 0, 0)]

    while queue:
        d, x, y = heappop(queue)

        # checking if current pos is the distination
        # If so, return the amount of steps taken to get there
        if (x, y) == (n * R - 1, n * C - 1):
            return d

        # Change in pos -> hor and vert
        for nx, ny in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            dx, dy = x + nx, y + ny

            # Checking if the change is out of bounds fo the grid
            if dx < 0 or dy < 0 or dx >= n * C or dy >= n * R:
                continue

            # Getting new pos (new row, new column)
            # (grid_val + row + column -1) % 9 + 1  -> val at pos in original grid
            # Then calculating new distince
            a, nr = divmod(dx, R)
            b, nc = divmod(dy, C)
            nd = d + (grid[nc][nr] + a + b - 1) % 9 + 1

            if (dx, dy) not in seen:
                seen.add((dx, dy))
                heappush(queue, (nd, dx, dy))


print(dijsktra(1))
print(dijsktra(5))