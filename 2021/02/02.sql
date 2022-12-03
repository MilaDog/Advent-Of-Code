-- Create Table
CREATE TABLE IF NOT EXISTS day02(
    id SERIAL,
    direction VARCHAR(20),
    steps INT,
    PRIMARY KEY (id)
);

-- Add day02/input -> add your path to file
\ copy day02(direction, steps)
FROM
    'input.csv' DELIMITER ';' CSV HEADER;

-- Part 1
WITH calc AS (
    SELECT
        id,
        direction,
        steps,
        SUM(
            CASE
                WHEN direction = 'forward' THEN steps
                ELSE 0
            END
        ) AS hor,
        SUM(
            CASE
                WHEN direction = 'up' THEN - steps
                WHEN direction = 'down' THEN steps
                ELSE 0
            END
        ) AS vert
    FROM
        day02
)
SELECT
    (hor * vert) AS Part1
FROM
    calc;

-- Part 2
WITH calc AS (
    SELECT
        id,
        direction,
        steps,
        SUM(
            CASE
                WHEN direction = 'forward' THEN steps
                ELSE 0
            END
        ) OVER w AS hor,
        SUM(
            CASE
                WHEN direction = 'up' THEN - steps
                WHEN direction = 'down' THEN steps
                ELSE 0
            END
        ) OVER w AS vert
    FROM
        day02 WINDOW w AS (
            ORDER BY
                id
        )
),
aim AS (
    SELECT
        id,
        vert * steps AS aim_increase
    FROM
        calc
    WHERE
        direction = 'forward'
),
sum_aim AS (
    SELECT
        SUM(aim_increase) AS aim_fnl
    FROM
        aim
)
SELECT
    ABS(
        aim_fnl * (
            SELECT
                max(hor)
            FROM
                calc
        )
    ) AS Part1
FROM
    sum_aim;