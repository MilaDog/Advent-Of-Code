from dis import Instruction
import re

with open("input.txt") as f:
    ps = f.readlines()


def part1():
    dn = dict()

    ins = [x.strip() for x in ps if re.findall(r"^(\d{1,}) -> (.*)$", x)]
    vals = [x.split(" -> ") for x in ins]
    dn[vals[1]] = int(vals[0])

    for line in ps:
        from1, from2, target, instru = "", "", "", ""

        if re.search(r"OR|NOT|AND|RSHIFT|LSHIFT", line):
            from1, instr, from2, target = re.findall(
                r"(.*)\s*(OR|AND|RSHIFT|LSHIFT|NOT) (.*) -> (.*)", line)

            # match instr:
            #     case "AND":

            #     case "NOT":

            #     case "OR":

            #     case "RSHIFT":

            #     case "LSHIFT:

            #     case _:


print(part1())
