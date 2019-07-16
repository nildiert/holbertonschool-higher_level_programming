-- Query  to do a list
-- This query lists all the cities of California
SELECT *
       FROM cities
       WHERE state_id =
       (
       SELECT id
       FROM states
       WHERE name = 'California')
       ORDER BY id;
