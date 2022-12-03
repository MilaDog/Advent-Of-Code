f = open("input.txt")
contents = f.readline()

# Part 1
print("Floor:", contents.count("(") - contents.count(")"))

# Part 2
changes = {"(": 1, ")": -1}

pos = 1
floor = 0

for x in contents:
    if x in changes:
        floor += changes[x]

    if floor == -1:
        print("Basement entered:", pos)
        break

    pos += 1

f.close()
