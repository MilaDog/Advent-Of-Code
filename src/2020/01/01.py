def get_input():
    return [int(x.strip()) for x in open("input.txt").readlines()]


def part1(nums):
    n = len(nums)

    for a in range(n):
        for b in range(a, n):
            if nums[a] + nums[b] == 2020:
                return nums[a] * nums[b]


def part2(nums):
    n = len(nums)

    for a in range(n):
        for b in range(a, n):
            for c in range(b, n):
                if nums[a] + nums[b] + nums[c] == 2020:
                    return nums[a] * nums[b] * nums[c]


print(f"Part 1: {part1(get_input())}")
print(f"Part 2: {part2(get_input())}")
