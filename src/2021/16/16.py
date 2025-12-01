inp = open("input.txt").read().strip()
b = bin(int(inp, 16))[2:]  # Get binary value from hex
b = b.zfill(len(inp) * 4)  # encoding some 0, so lengths are the same (bin len = hex len * 4)

TOTAL_V = 0


def update(data, n):
    ret = data[0][:n]
    data[0] = data[0][n:]
    return ret


def get_literal(data):
    t = []
    while True:
        i, *d = update(data, 5)
        t += d
        if i == "0":
            break
    return int("".join(t), 2)


def solve(b):
    global TOTAL_V

    version = update(b, 3)
    TOTAL_V += int(version, 2)

    # Getting literal value
    type_id = int(update(b, 3), 2)
    if type_id == 4:
        return get_literal(b)

    # Getting length type id
    len_type_id = update(b, 1)[0]
    spv = []
    if len_type_id == "0":  # Total length in bits of sub packets
        len_sub_packets = int(update(b, 15), 2)
        sub_packets = [update(b, len_sub_packets)]
        while sub_packets[0]:
            spv.append(solve(sub_packets))
    else:
        # Total number of sub packets following the LTID (length type id)
        spv = [solve(b) for _ in range(int(update(b, 11), 2))]

    # Matching other type ids - part 2
    match type_id:
        case 0:
            return sum(spv)
        case 1:
            p = 1
            for x in spv:
                p *= x
            return p
        case 2:
            return min(spv)
        case 3:
            return max(spv)
        case 5:
            return int(spv[0] > spv[1])
        case 6:
            return int(spv[0] < spv[1])
        case 7:
            return int(spv[0] == spv[1])


p2 = solve([b])
print(f"Part 1: {TOTAL_V}")
print(f"Part 2: {p2}")
