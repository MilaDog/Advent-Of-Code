import re


def get_input():
    return [
        n.replace("\n", " ")
        for n in [x.strip() for x in open("input.txt").read().split("\n\n")]
    ]


# Part 1 -> Get total amount fo valid passports
def part1():
    VALID_TERMS = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    tlt = 0
    for p in get_input():
        tlt += 1 if all(t in p for t in VALID_TERMS) else 0
    return tlt


# Part 2 -> Get actual valid passports from part 1's 'valid passports'
def part2():
    tlt = 0
    for p in get_input():
        if (
            (
                re.search(r"byr:19[2-9]\d|byr:200[0-2]", p)
                and re.search(r"iyr:201\d|iyr:2020", p)
                and re.search(r"eyr:202\d|eyr:2030", p)
                and re.search(
                    r"hgt:1[5-8]\dcm|hgt:19[0-3]cm|hgt:59in|hgt:6\din|hgt:7[0-6]in", p
                )
            )
            and re.search(r"hcl:#[0-9a-f]{6}", p)
            and re.search(r"ecl:(amb|blu|brn|gry|grn|hzl|oth)", p)
            and (re.search(r"pid:\d{9}\b", p))
        ):
            tlt += 1
    return tlt


print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
