-- Create Table
CREATE TABLE IF NOT EXISTS day01(id SERIAL, depths INT, PRIMARY KEY (id));

-- Add day01/input -> add your path to file
\ copy day01(depths)
FROM
    'input.csv' CSV HEADER;

-- Part 1
WITH lagg AS (
    SELECT
        depths AS curr,
        LAG(depths, 1) OVER (
            ORDER BY
                id
        ) AS prev
    FROM
        day01
)
SELECT
    COUNT(*) AS Part1
FROM
    lagg
WHERE
    curr > prev;

-- Part 2
WITH wind AS (
    SELECT
        MIN(id) OVER w AS rowid,
        SUM(depths) OVER w AS depth
    FROM
        day01 WINDOW w AS (
            ORDER BY
                id ROWS BETWEEN CURRENT ROW
                AND 2 FOLLOWING
        )
),
lagg AS (
    SELECT
        depth AS curr,
        LAG(depth, 1) OVER (
            ORDER BY
                rowid
        ) AS prev
    FROM
        wind
)
SELECT
    COUNT(*) AS Part2
FROM
    lagg
WHERE
    curr > prev;
