def get_input():
    return [x.strip() for x in open("input.txt").readlines()]


def solve():
    D = get_input()
    p1 = False

    x = [3, 1, 5, 7, 1]
    y = [1, 1, 1, 1, 2]

    totalTrees = 1

    for dx, dy in zip(x, y):
        trees = x = 0
        for pos in D[::dy]:
            trees += 1 if pos[x % len(pos)] == "#" else 0
            x += dx

        if not p1:
            print(trees)
            p1 = True

        totalTrees *= trees
    print(totalTrees)


solve()
