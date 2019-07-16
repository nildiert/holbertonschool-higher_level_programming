-- Query  to do a list with join
-- This query lists cities and states
SELECT cities.id, cities.name, states.name
	FROM cities
	LEFT JOIN states
	ON states.id = cities.state_id;
