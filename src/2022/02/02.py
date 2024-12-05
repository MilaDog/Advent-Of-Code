TURNS = [x.strip().split(" ") for x in open("input.txt").readlines()]


def solve_p1():
    tlt: int = 0

    d: dict = {
        "AY": 6,
        "BZ": 6,
        "CX": 6,
        "AX": 3,
        "BY": 3,
        "CZ": 3,
        "AZ": 0,
        "BX": 0,
        "CY": 0,
    }

    # Points for each choice made
    scores: dict = {"X": 1, "Y": 2, "Z": 3}

    for turn in TURNS:
        tlt += scores[turn[1]]  # points for choice
        tlt += d["".join(turn)]  # win or lose or die points
    print(f"Part 1: {tlt}")


def solve_p2():
    d: dict = {
        "AX": 3,
        "AY": 1,
        "AZ": 2,
        "BX": 1,
        "BY": 2,
        "BZ": 3,
        "CX": 2,
        "CY": 3,
        "CZ": 1,
    }

    # play a Z = win, play a Y = tie, play an X = lose
    scores: dict = {"X": 0, "Y": 3, "Z": 6}

    tlt: int = 0
    for turn in TURNS:
        tlt += scores[turn[1]]  # win or lose or tie points
        tlt += d["".join(turn)]  # choice points
    print(f"Part 2: {tlt}")


solve_p1()
solve_p2()
