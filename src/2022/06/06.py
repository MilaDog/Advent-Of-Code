def solve(amt: int):
    chars = list(open("input.txt").read().strip())
    for i in range(amt, len(chars)):
        if len(set(chars[i - amt : i])) == amt:
            return i


print(f"Part 1: {solve(4)}")
print(f"Part 2: {solve(14)}")
