from collections import namedtuple


def tail_in_range(tail: list[int], head: list[int]) -> bool:
    return (tail[0] - head[0] in [-1, 1, 0]) and (tail[1] - head[1] in [-1, 1, 0])


def position_change(val_tail: int, val_head: int) -> int:
    if val_tail - val_head > 0:
        return -1
    elif val_tail - val_head < 0:
        return 1
    else:
        return 0


def solve(amt: int) -> int:
    Movement: namedtuple = namedtuple("Movement", "d n")
    movements = [Movement(d, int(n)) for d, n in [m.split() for m in open("input.txt").read().strip().splitlines()]]

    seen = list()
    knots: list[list[int]] = [[0, 0]] * amt
    seen.append(knots[0])
    changes: dict[str: list[int]] = {"U": [0, 1], "D": [0, -1], "L": [-1, 0], "R": [1, 0]}

    for move in movements:
        for _ in range(move.n):
            dx, dy = changes[move.d]
            knots[0] = [knots[0][0] + dx, knots[0][1] + dy]

            for i in range(1, amt):
                tail = knots[i]
                head = knots[i - 1]

                if not tail_in_range(tail, head):
                    match move.d:
                        case 'U' | 'D':
                            knots[i] = [tail[0] + position_change(tail[0], head[0]),
                                        tail[1] + position_change(tail[1], head[1])]

                        case 'L' | 'R':

                            knots[i] = [tail[0] + position_change(tail[0], head[0]),
                                        tail[1] + position_change(tail[1], head[1])]
            if knots[-1] not in seen:
                seen.append(knots[-1])

    return len(seen)


print(f"Part 1: {solve(2)}")
print(f"Part 2: {solve(10)}")
