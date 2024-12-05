-- Create Table
CREATE TABLE IF NOT EXISTS day03(
    id SERIAL,
    bin VARCHAR(12),
    PRIMARY KEY (id)
);

-- Add day03/input -> add your path to file
\ copy day03(bin)
FROM
    'input.csv' CSV HEADER;

-- Needed function
CREATE FUNCTION get_bit(indx int)
returns char(1)
language plpgsql
as
$$
declare
bit char(1);
begin
SELECT CASE WHEN COUNT(*) > (SELECT COUNT(*) FROM day03 GROUP BY SUBSTRING(bin,indx,1) HAVING SUBSTRING(bin,indx,1) = '0') THEN '1' ELSE '0' END
INTO bit
FROM day03
GROUP BY SUBSTRING(bin,indx,1)
HAVING SUBSTRING(bin,indx,1) = '1';
return bit;
end;
$$;

CREATE FUNCTION get_gamma()
returns varchar(12)
language plpgsql
as
$$
declare
gamma varchar(12);
begin
for i in 1..12 loop
gamma := gamma || get_bit(i);
end loop;

return gamma;
end;
$$;

-- Part 1

-- Part 2
