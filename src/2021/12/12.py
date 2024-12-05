from collections import defaultdict


def get_input():
    graph = defaultdict(list)
    for path in open("input.txt"):
        a, b = path.strip().split("-")
        graph[a].append(b)
        graph[b].append(a)

    return graph


GRAPH = get_input()


def dfs(start, visited, part2=False):
    if start == "end":
        return 1

    tlt = 0
    for neigh in GRAPH[start]:
        if neigh not in visited:
            new_visited = visited + [neigh] if neigh.islower() else visited
            tlt += dfs(neigh, new_visited, part2)
        elif part2 and neigh != "start":
            tlt += dfs(neigh, visited, False)
    return tlt


def part1():
    return dfs("start", ["start"], False)


def part2():
    return dfs("start", ["start"], True)


print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
