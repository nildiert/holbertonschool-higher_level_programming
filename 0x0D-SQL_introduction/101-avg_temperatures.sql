-- Query to order by temp
-- This query shows by temp and city
SELECT city, AVG(values) as avg_temp GROUP BY city ORDER BY DESC;
