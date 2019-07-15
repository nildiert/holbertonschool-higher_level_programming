-- Query to order by temp
-- This query shows by temp and city
SELECT city, AVG(value) as avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
