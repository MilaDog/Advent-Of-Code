from dataclasses import dataclass
from re import findall
from math import lcm


@dataclass(kw_only=True)
class Monkey:
    id: int
    items: list[int]
    operation: list[str]
    test: int
    true_throw_to: int
    false_throw_to: int
    inspection_count: int = 0

    def perform_operation(self, part1: bool = True, lcm: int = 1) -> tuple([int, int]):
        self.inspection_count += 1

        val: int = self.items.pop(0)
        match self.operation:
            case ["+", v]:
                val += int(v) if v.isdigit() else val

            case ["-", v]:
                val -= int(v) if v.isdigit() else val

            case ["*", v]:
                val *= int(v) if v.isdigit() else val

            case ["/", v]:
                val //= int(v) if v.isdigit() else val

        if part1:
            val //= 3
        else:
            val %= lcm

        if val % self.test == 0:
            return (val, self.true_throw_to)
        else:
            return (val, self.false_throw_to)


def solve(part1: bool = True, amt: int = 20) -> int:
    actions: list[str] = [x.strip() for x in open("input.txt").read().split("\n\n")]

    monkeys: list[Monkey] = list()

    for i, action in enumerate(actions):
        lines = action.strip().split("\n")
        id = i
        items = list(map(int, [x for x in findall(r"(\d+)", lines[1])]))
        operation = lines[2].split()[-2:]
        test = list(map(int, findall(r"(\d+)", lines[3])))[0]
        true_throw_to = int(findall(r"(\d+)", lines[4])[0])
        false_throw_to = int(findall(r"(\d+)", lines[5])[0])
        mnk = Monkey(
            id=id,
            items=items,
            operation=operation,
            test=test,
            true_throw_to=true_throw_to,
            false_throw_to=false_throw_to,
        )
        monkeys.append(mnk)

    lcm_: int = lcm(*[m.test for m in monkeys])
    for _ in range(amt):
        for i in range(len(monkeys)):
            mnk = monkeys[i]
            for _ in range(len(mnk.items)):
                val, to_monkey = mnk.perform_operation(part1, lcm_)
                monkeys[to_monkey].items.append(val)

    total_monkey_inspections: list[int] = sorted(
        [x.inspection_count for x in monkeys], reverse=True
    )
    return total_monkey_inspections[0] * total_monkey_inspections[1]


print(f"Part 1: {solve(True, 20)}")
print(f"Part 2: {solve(False, 10000)}")
