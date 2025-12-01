def get_input():
    return [x.strip() for x in open("input.txt").readlines()]


def valid_password(line):
    rng, char, pwd = line.split()
    char = char[0]
    begin, end = map(int, rng.split("-"))

    return begin <= pwd.count(char) <= end


def part1(pwds):
    return sum([valid_password(x) for x in pwds])


def part2(pwds):
    tlt = []

    for line in pwds:
        rng, char, pwd = line.split()
        char = char[0]
        ind1, ind2 = map(int, rng.split("-"))

        tlt.append(
            int(pwd[ind1 - 1] == char and pwd[ind2 - 1] != char) or int(pwd[ind1 - 1] != char and pwd[ind2 - 1] == char)
        )
    return sum(tlt)


print(f"Part 1: {part1(get_input())}")
print(f"Part 2: {part2(get_input())}")
