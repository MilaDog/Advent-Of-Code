# Chronospatial Computer

## Part 1

Fairly straight forward question. Iterate the given program and perform the operations. Fast enough to brute force
the solution.

## Part 2

On the other hand, Part 2 cannot easily be brute forced. The correct answer for me was 15 digits long, so if you
want, enjoy brute forcing the answer for the next couple of decades.

A different approach had to be taken. At first, I had no idea. Then decided to have a peek at what other people did.
No idea what was going on. Just that it had to be reversed engineered. So, after leaving it to process in my brain,
I finally started to understand what was actually going on.

So, taking the program I had, `2,4,1,1,7,5,4,6,0,3,1,4,5,5,3,0`, let's break it down into its groups, with their
literal or combo value:

Other needed info: `rA`, `rB`, `rC` being registers `A` to `C` respectively.

| Code | Operand | Is literal | Value |
|------|---------|------------|-------|
| 2    | 4       | No         | rA    |
| 1    | 1       | Yes        | 1     |
| 7    | 5       | No         | rB    |
| 4    | 6       | -          | -     |
| 0    | 3       | No         | 3     |
| 1    | 4       | Yes        | 4     |
| 5    | 5       | No         | rB    |
| 3    | 0       | No         | -     |

with the Combo Value as:

- value <= 3: v
- value == 4: rA
- value == 5: rB
- value == 6: rC

So, with that, below are the actions that take place:

| Code | Operand | Value | Operation         |
|------|---------|-------|-------------------|
| 2    | 4       | rA    | rA % 8 -> rB      |
| 1    | 1       | 1     | rB ^ 1 -> rB      |
| 7    | 5       | rB    | rA >> rB -> rC    |
| 4    | 6       | -     | rB ^ rC -> rB     |
| 0    | 3       | 3     | rA >> 3 -> rA     |
| 1    | 4       | 4     | rB ^ 4 -> rB      |
| 5    | 5       | rB    | rB % 8 -> display |
| 3    | 0       | -     | rA != 0: repeat   |

Simplified, we have the following:

```py
rB = (rA % 8) ^ 1
rC = (rA) >> rB
rB ^= (rC + 4)

print(rB % 8)
```

Now, having to determine the answer to the problem, we start by iterating the given program backwards. Then for each
possible `rA` value, we plug it into the above function, with a bit offset. If `rB % 8` equals the operation code in
the program, then
that is a potential valid `rA` value, so we need to process it further.
Then, once all the operation codes have been worked through, we have stored all the potential `rA` values that give
a copy of the original program. We select the minimum, and that is the answer.

```py
potential_rA_values: list[int] = [0]    # Start at 0
to_process: list[int] = []

for opcode in program[::-1]:
    for rA in potential_rA_values:
        for bit in range(8):
            rB = (bit % 8) ^ 1
            rC = (rA+bit) >> rB
            rB ^= (rC+4)

            if rB % 8 == opcode:
                to_process.append((rA+bit) << 3)

        to_process, potential_A = [], to_process

print(min([rA >> 3 for rA in potential_rA_values]))
```
