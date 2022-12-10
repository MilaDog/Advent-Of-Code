def solve() -> None:
    actions: list = [x.strip() for x in open("input.txt").read().strip().splitlines()]

    cnt: int = 0
    tlt: int = 1
    recorded_actions: list[int] = list()
    display_code: list[str] = list()
    view: str = ""

    for action in actions:
        cycles = 2 if action[0] == 'a' else 1

        for _ in range(cycles):
            if tlt - 1 <= cnt % 40 <= tlt + 1:
                view += "#"
            else:
                view += " "

            if len(view) == 40:
                display_code.append(view)
                view = ""

            cnt += 1
            if cnt in range(20, 221, 40):
                recorded_actions.append(tlt * cnt)

        tlt += int(action.split()[1]) if action[0] == 'a' else 0

    print(f"Part 1: {sum(recorded_actions)}")
    print(f"Part 2: ")
    print("\n".join(display_code))


solve()
