seats = [x.strip() for x in open("input.txt")]
S = set()

# Using binary space partitioning
# can convert each seat to binary and get the value
for s in seats:
    trans = str.maketrans("FBLR", "0101")
    s = s.translate(trans)
    S.add(int(s, 2))

print(f"Part 1: {max(S)}")

for i in S:
    if i + 1 not in S and i + 2 in S:
        print(f"Part 2: {i + 1}")
