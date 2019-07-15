-- Query to order by top
-- This query shows by temp and city
SELECT state, MAX(value) as max_temp
       FROM temperatures
       GROUP BY state
       ORDER BY state
       LIMIT 3;
