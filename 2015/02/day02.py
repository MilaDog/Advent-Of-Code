f = open("input.txt")
contents = f.read().splitlines()

# Part 1
total_feet = 0
total_ribbon = 0

for content in contents:
    l, w, h = content.split("x")
    l, w, h = int(l), int(w), int(h)

    lw, wh, hl = l * w, w * h, h * l
    extra = min([lw, wh, hl])

    total_feet += 2 * (lw + wh + hl) + extra

    # Part 2
    bow = l * w * h
    ribbon = min([l + l + w + w, w + w + h + h, h + h + l + l])

    total_ribbon += (bow + ribbon)
f.close()

print("Total wrapping:", total_feet)
print("Total ribbon:", total_ribbon)
