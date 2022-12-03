import re

with open("input.txt") as f:
    ps = f.readlines()


def solve():
    coords = {}
    brightness = {}

    for line in ps:
        pos = [int(x) for x in re.findall(r"\d{1,3}", line)]
        instruction = re.findall(r"turn on|turn off|toggle", line)[0]

        for x in range(pos[0], pos[2] + 1):
            for y in range(pos[1], pos[3] + 1):
                match instruction:
                    case "turn on":
                        coords[(x, y)] = True

                        if (x, y) in brightness.keys():
                            brightness[(x, y)] += 1
                        else:
                            brightness[(x, y)] = 1

                    case "turn off":
                        coords[(x, y)] = False

                        if (x, y) in brightness.keys():
                            brightness[(x, y)] -= 1 if brightness[(x, y)] > 0 else 0
                        else:
                            brightness[(x, y)] = 0

                    case "toggle":
                        if (x, y) not in coords.keys():
                            coords[(x, y)] = True
                        else:
                            coords[(x, y)] = not coords[(x, y)]

                        if (x, y) in brightness.keys():
                            brightness[(x, y)] += 2
                        else:
                            brightness[(x, y)] = 2

    print("Part 1: ", sum(coords.values()))
    print("Part 2: ", sum(brightness.values()))


solve()
