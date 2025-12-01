def get_input():
    with open("input.txt", "r") as f:
        return [x.strip() for x in f]
    # return ["00100","11110","10110","10111","10101","01111","00111","11100","10000","11001","00010","01010"]


def bit_criteria(values, pos, get_min):
    bit0, bit1 = 0, 0
    for x in values:
        if x[pos] == "0":
            bit0 += 1
        else:
            bit1 += 1
    bitfnl = ("1", "0")[bit0 > bit1] if get_min else ("0", "1")[bit0 > bit1]
    values = [x for x in values if x[pos] == bitfnl]
    return int(values[0], 2) if len(values) == 1 else bit_criteria(values, pos + 1, get_min)


def part1(values):
    transposed = ["".join(val) for val in zip(*values)]
    gr = "".join(["1" if x.count("1") > x.count("0") else "0" for x in transposed])
    er = "".join(["0" if x == "1" else "1" for x in gr])
    return int(gr, 2) * int(er, 2)


def part2(values):
    return bit_criteria(values, 0, False) * bit_criteria(values, 0, True)


print(f"Part 1: {part1(get_input())}")
print(f"Part 2: {part2(get_input())}")
