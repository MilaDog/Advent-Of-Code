import re

inp = re.findall(r"(\d+)\.\.(\d+), y=(-?\d+)\.\.(-?\d+)", open("input.txt").read().strip())
xa, xb, ya, yb = [int(x) for x in inp[0]]

print(f"Part 1: {ya * (ya + 1) // 2}")

TLT = 0
for DX in range(xb + 1):
    for DY in range(ya, -ya + 1):
        x = y = 0
        dx, dy = DX, DY
        while y >= ya:
            x, y = x + dx, y + dy

            if dx > 0:
                dx -= 1
            elif dx < 0:
                dx += 1
            dy -= 1

            # Is in final area
            if xa <= x <= xb and ya <= y <= yb:
                TLT += 1
                break

print(f"Part 2: {TLT}")
