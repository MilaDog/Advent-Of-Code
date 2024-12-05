def get_input():
    with open("input.txt", "r") as f:
        data = [line.strip().split(" | ") for line in f.readlines()]
        return data


def part1(data):
    tlt = 0
    for x, y in data:
        for y in map(set, y.split()):
            match len(y):
                case 2:
                    tlt += 1
                case 3:
                    tlt += 1
                case 4:
                    tlt += 1
                case 7:
                    tlt += 1
                case _:
                    pass
    return tlt


def part2(data):
    tlt = 0
    for x, y in data:
        t = ""
        l = {len(s): set(s) for s in x.split()}
        for n in map(set, y.split()):
            match (
                len(n),
                len(n & l[4]),
                len(n & l[3]),
            ):  # what segments are in each. Known numbers are 4 (beafb) and 7 (dab), and from that, 1 (ab) can also be used
                case 2, _, _:
                    t += "1"
                case 3, _, _:
                    t += "7"
                case 4, _, _:
                    t += "4"
                case 5, 2, 2:
                    t += "2"
                case 5, 3, 3:
                    t += "3"
                case 5, 3, 2:
                    t += "5"
                case 6, 3, 2:
                    t += "6"
                case 6, 3, 3:
                    t += "0"
                case 6, 4, 3:
                    t += "9"
                case 7, _, _:
                    t += "8"
        tlt += int(t)
    return tlt


print(f"Part 1: {part1(get_input())}")
print(f"Part 2: {part2(get_input())}")
