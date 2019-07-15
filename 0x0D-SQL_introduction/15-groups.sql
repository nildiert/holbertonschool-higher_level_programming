-- Query to show the cant of scores
-- This query, shows the count of scores
SELECT score, count(score) as number
       FROM second_table
       GROUP BY score
       ORDER BY score DESC;
