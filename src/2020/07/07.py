import re
from collections import defaultdict

lines = open("input.txt").read().split("\n")

bag_contains = defaultdict(list)
bag_contained_in = defaultdict(list)

for line in lines:
    main_bag = re.findall(r"^([a-z]+ [a-z]+)", line)[0]
    for cnt, colour in re.findall(r"(\d+) ([a-z]+ [a-z]+) bags?[,.]", line):
        cnt = int(cnt)
        bag_contains[main_bag].append((cnt, colour))
        bag_contained_in[colour].append(main_bag)

# Part 1 -> how many bags contain at least one 'shiny gold' (SG) bag
SG = set()


def check(c):
    for x in bag_contained_in[c]:
        SG.add(x)
        check(x)


check("shiny gold")
print(f"Part 1: {len(SG)}")


# Part 2 -> how many other bags must your 'shiny gold' bag contain
# I.E. -> 'shiny gold' contains x, x contains y, y contains ... and so on
def p2(c):
    tlt = 0
    for cnt, colour in bag_contains[c]:
        tlt += cnt
        tlt += cnt * p2(colour)
    return tlt


print("Part 2:", p2("shiny gold"))
