-- Query to show the cant of scores
-- This query, shows the count of scores
SELECT score, name
       FROM second_table
       WHERE name != NULL
       OR name != ''
       ORDER BY score DESC;
