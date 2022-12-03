DATA = [[int(x) for x in line.strip()] for line in open("input.txt", "r")]
ANS = 0
COLUMNS = len(DATA[0])
ROWS = len(DATA)


def flash(row, column):
    global ANS
    ANS += 1
    DATA[row][column] = -1
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            rr = row + dr
            cc = column + dc
            if 0 <= rr < ROWS and 0 <= cc < COLUMNS and DATA[rr][cc] != -1:
                DATA[rr][cc] += 1
                if DATA[rr][cc] > 9:
                    flash(rr, cc)


def solve():
    steps = 0
    while True:
        steps += 1
        for row in range(ROWS):
            for column in range(COLUMNS):
                DATA[row][column] += 1

        for row in range(ROWS):
            for column in range(COLUMNS):
                if DATA[row][column] > 9:
                    flash(row, column)

        done = True
        for row in range(ROWS):
            for column in range(COLUMNS):
                if DATA[row][column] == -1:
                    DATA[row][column] = 0
                else:
                    done = False

        if steps == 100:
            print(f"Part 1: {ANS}")
        if done:
            print(f"Part 2: {steps}")
            break


solve()
