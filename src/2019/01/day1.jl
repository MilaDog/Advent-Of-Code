using CSV

function readFile()
    return CSV.read("./day1/input.csv", header=false)
end

# Part 1
function getFuel(input)

    # Calculating fuel required from input
    fuelP1 = Int(floor(input/3))-2

    if fuelP1 < 0
        return 0
    else
        return fuelP1
    end

end

# Part 2
function getFuel_fuel(input)

    # Getting total fuel needed
    total_fuel = getFuel(input)
    extra_fuel = total_fuel

    while extra_fuel > 0
        # Calculating fuel needed extra
        extra_fuel = getFuel(extra_fuel)
        total_fuel += extra_fuel
    end

    return total_fuel

end

# Starting
function getVals()

    # Getting fuel from given input
    input = readFile()

    # Summing up all the fuel needed | going through each value in the column
    p1 = getFuel.(input[:,1]) |> sum
    p2 = getFuel_fuel.(input[:,1]) |> sum

    @time println(p1)
    @time println(p2)

end
getVals()
