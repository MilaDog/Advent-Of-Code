-- Create table
CREATE TABLE day02(
    id SERIAL,
    RANGE TEXT,
    char TEXT,
    PASSWORD TEXT,
    PRIMARY KEY (id)
);

-- Populate table -> replace with path to file
\ copy day02(RANGE, char, PASSWORD)
FROM
    'input.csv' DELIMITER ';' CSV HEADER;

-- Part 1
WITH inputs AS(
    SELECT
        CAST(SPLIT_PART(d.range, '-', 1) AS INT) AS min,
        CAST(SPLIT_PART(d.range, '-', 2) AS INT) AS max,
        LEFT(d.char, 1) AS char,
        d.password
    FROM
        day02 AS d
),
p1 AS (
    SELECT
        *,
        LENGTH(inputs.password) - LENGTH(REPLACE(inputs.password, inputs.char, '')) AS ltrCount
    FROM
        inputs
)
SELECT
    COUNT(*) AS Part1
FROM
    p1
WHERE
    p1.ltrCount BETWEEN p1.min
    AND p1.max;

-- Part 2
WITH p2 AS (
    SELECT
        CAST(SPLIT_PART(d.range, '-', 1) AS INT) AS min,
        CAST(SPLIT_PART(d.range, '-', 2) AS INT) AS max,
        CAST(LEFT(d.char, 1) AS TEXT) AS char,
        d.password
    FROM
        day02 AS d
),
chck AS (
    SELECT
        SUBSTRING(p2.password FROM p2.min FOR 1) = p2.char AS found1,
        SUBSTRING(p2.password FROM p2.max FOR 1) = p2.char AS found2
    FROM
        p2
)
SELECT
    COUNT(*) AS Part2
FROM
    chck
WHERE
(
    (chck.found1 OR chck.found2) AND (NOT chck.found1 OR NOT chck.found2)
);
