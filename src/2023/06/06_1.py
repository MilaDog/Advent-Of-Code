from math import floor, ceil, sqrt, prod
from re import findall
from timeit import timeit


# Toy boat travels at x mm/ms. The travel mm/ms is equivalent to the duration the boat button is held.
# Eg: Button held for 1 ms results in boat movement speed of 1 mm/ms. If the total time for the race is 7ms
# and holding the boat button counts towards total race time, then the example boat will have travels (7-1) = 6 mm in total.

# Formula to represent this:
# t = T - B, where T is total race time, B is button hold time and t is the travel time
# D = t * B, where D is the total distance traveled, t is the travel time and B is the button hold time

# Then, D = (T - B) * B
#         = TB - B^2

# Thus, a quadratic equation is present, being:
#     B^2 - TB + D = 0

# Thus, solving for B, we have:
#     B1 = (T + sqrt(T^2 - 4D))/2
#     B2 = (T - sqrt(T^2 - 4D))/2

# Answer is: ceil(B2) - floor(B1) + 1


def calc(time, distance) -> int:
    x = sqrt(time**2 - 4 * distance)

    b1 = ceil((time - x) / 2)
    b2 = floor((time + x) / 2)

    return b2 - b1 + 1


def main() -> None:
    with open("input.txt", "r") as file:
        lines = file.read().splitlines()

    values = [list(map(int, findall(r"(\d+)", line))) for line in lines]

    p1 = [calc(t, d) for t, d in zip(values[0], values[1])]
    print(prod(p1))

    t, d = "".join(map(str, values[0])), "".join(map(str, values[1]))
    p2 = calc(int(t), int(d))
    print(p2)


if __name__ == "__main__":
    print(timeit(main, number=1))
