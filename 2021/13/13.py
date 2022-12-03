import re

def get_input():
    coords = [x for x in re.findall(r'(\d+),(\d+)',open("input.txt").read())]
    folds = [x for x in re.findall(r'fold along ([xy])=(\d+)', open("input.txt").read())]

    coords = [(int(x), int(y)) for x,y in coords]
    folds = [(a, int(n)) for a,n in folds]

    return coords, folds

def solve():
    coords, folds = get_input()
    
    G = set(coords)
    
    for i, (axis, n) in enumerate(folds):
        G2 = set()
        if axis == 'x':
            G2 = set((x,y) if x<n else (n*2-x,y) for (x,y) in G)
        else:
            G2 = set((x,y) if y<n else (x, n*2-y) for (x,y) in G)

        G = G2
        if i == 0:
            print(f"Part 1: {len(G2)}")
    
    Y = max([y for x,y in G]) + 1
    X = max([x for x,y in G]) + 1

    lines = []
    for y in range(Y):
        l = ""
        for x in range(X):
            l += "\u2588" if (x,y) in G else " "
        lines.append(l)
    print("Part 2:\n")
    print("\n".join(lines))

solve()