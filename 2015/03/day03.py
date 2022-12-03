with open("input.txt") as f:
    ps = list(f.readline())

# Part 1
movements = {'^': 1, '>': 1, 'v': -1, '<': -1}


def get_coord(pos, dir):
    x, y = pos[0], pos[1]
    match dir:
        case '^':
            y += 1
        case 'v':
            y -= 1
        case '>':
            x += 1
        case '<':
            x -= 1
    return (x, y)


def part1():
    strt = (0, 0)
    coords = {strt: 1}

    for dir in ps:
        coord = get_coord(strt, dir)
        strt = coord

        if coord in coords.keys():
            coords[coord] += 1
        else:
            coords[coord] = 1

    return sum([1 for x in coords.values() if x > 0])


# Part 2
def part2():
    strt = (0, 0)
    strt2 = (0, 0)
    coords = {strt: 1}

    for i, dir in enumerate(ps):

        if i % 2 != 0:
            coord = get_coord(strt, dir)
            strt = coord

            if coord in coords.keys():
                coords[coord] += 1
            else:
                coords[coord] = 1

        else:
            coord = get_coord(strt2, dir)
            strt2 = coord

            if coord in coords.keys():
                coords[coord] += 1
            else:
                coords[coord] = 1

    return sum([1 for x in coords.values() if x > 0])


print("Part 1: ", part1())
print("Part 2: ", part2())
