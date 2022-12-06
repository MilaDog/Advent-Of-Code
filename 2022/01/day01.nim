import strutils, strformat, algorithm, math

proc solve(): void = 
    let file = readFile("input.txt").strip().splitLines()

    var 
        tlt: int = 0
        values: seq[int] = @[]

    for cal in file:
        if len(cal) == 0:
            values.add(tlt)
            tlt = 0
        else:
            tlt += parseInt(cal)

    echo fmt"Part 1: {max(values)}"
    echo fmt"Part 2: {values.sorted(Descending)[0..2].sum}"

solve()