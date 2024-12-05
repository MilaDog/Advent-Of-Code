-- Create table
CREATE TABLE IF NOT EXISTS day01(id SERIAL, numbers INT, PRIMARY KEY (id));

-- Populate table -> add in path to file
\ copy day01(numbers)
FROM
    'input.csv' CSV HEADER;

-- Part 1
SELECT
    (a.numbers * b.numbers) AS Part1
FROM
    day01 AS a,
    day01 AS b
WHERE
    a.numbers + b.numbers = 2020
LIMIT
    1;

-- Part 2
SELECT
    (a.numbers * b.numbers * c.numbers) AS Part2
FROM
    day01 AS a,
    day01 AS b,
    day01 AS c
WHERE
    a.numbers + b.numbers + c.numbers = 2020
LIMIT
    1;
