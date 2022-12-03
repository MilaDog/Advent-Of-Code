def get_input():
    with open("input.txt", "r") as f:
        return [int(line.strip()) for line in f]
    # return [199,200,208,210,200,207,240,269,260,263]


def part1(vals):
    return sum([vals[x] > vals[x - 1] for x in range(len(vals))])


def part2(vals):
    sw = [vals[x] + vals[x + 1] + vals[x + 2] for x in range(len(vals) - 2)]
    return part1(sw)


print(f"Part 1: {part1(get_input())}\nPart 2: {part2(get_input())}")
