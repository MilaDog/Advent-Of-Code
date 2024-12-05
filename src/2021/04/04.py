def get_input():
    with open("input.txt", "r") as f:
        numbers = [int(num) for num in f.readline().split(",")]
        boards = [
            [[*map(int, r.split())] for r in b.split("\n")]
            for b in f.read().strip().split("\n\n")
        ]
        return numbers, boards


def check_board(win_index):
    numbers, boards = get_input()

    checked, bingo, scores = set(), [], []

    for num in numbers:
        checked.add(num)
        for board in boards:
            rows_and_cols = board + [col for col in zip(*board)]
            for line in rows_and_cols:
                if all(n in checked for n in line) and board not in bingo:
                    bingo.append(board)
                    scores.append(
                        sum(sum(n for n in line if n not in checked) for line in board)
                        * num
                    )
    return scores[win_index]


def part1():
    return check_board(0)


def part2():
    return check_board(-1)


print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
