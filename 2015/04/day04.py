from hashlib import md5
from itertools import count


def check(chck):
    init = "ckczppom"
    for x in count(1):
        c = md5((init + str(x)).encode()).hexdigest()
        if c[:5] == chck or c[:6] == chck:
            return x


print("Part 1: ", check("00000"))
print("Part 2: ", check("000000"))
