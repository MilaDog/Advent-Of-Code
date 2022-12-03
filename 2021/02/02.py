def get_input():
    with open("input.txt", "r") as f:
        values = []
        for line in f:
            value = line.strip().split(" ")
            values.append((value[0], int(value[1])))
        return values
    # return [("forward", 5),("down", 5),("forward", 8),("up", 3),("down", 8),("forward", 2)]


def part1(values):
    hor, vert = 0, 0
    for val in values:
        if val[0] == "forward":
            hor += val[1]
        elif val[0] == "up":
            vert += val[1]
        else:
            vert -= val[1]
    return abs(hor * vert)


def part2(values):
    hor, vert, aim = 0, 0, 0
    for val in values:
        if val[0] == "forward":
            hor += val[1]
            vert += aim * val[1]
        elif val[0] == "up":
            aim -= val[1]
        else:
            aim += val[1]
    return abs(hor * vert)


print(f"Part 1: {part1(get_input())}")
print(f"Part 2: {part2(get_input())}")
