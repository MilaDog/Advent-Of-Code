using CSV

function readFile()
    x = CSV.read("./day2/input.csv", header=false, delim='|')
    return parse.(Int, split(x[1,1], ','))
end

# Going through array -> return final value at pos=1
function opCode(x)

    pos=1

    while pos < length(x)

        opcode = x[pos]

        # Values for calculations
        a = x[pos+1]
        b = x[pos+2]
        c = x[pos+3]

        # Checking opCodes from input
        if opcode == 99
            break
        elseif opcode == 1
            x[c+1] = x[a+1] + x[b+1]
        elseif opcode == 2
            x[c+1] = x[a+1] * x[b+1]
        end

        # Increasing pointer
        pos += 4

    end
    return x[1]
end


function getVals()

    input = readFile()

    # Part 1 - copy of info from input.csv
    vals_p1 = deepcopy(input)
    vals_p1[2] = 12
    vals_p1[3] = 2
    part1 = opCode(vals_p1)
    @time println(part1)


    # Part 2 - copy of info from input.csv
    for noun = 0:99
        for verb = 0:99

            # Reset - resetting memory
            vals_p2 = deepcopy(input)
            vals_p2[2] = noun
            vals_p2[3] = verb

            if opCode(vals_p2) == 19690720
                @time println(100 * noun + verb)
                @goto exit_loop
            end
        end
    end
    @label exit_loop
end
getVals()
