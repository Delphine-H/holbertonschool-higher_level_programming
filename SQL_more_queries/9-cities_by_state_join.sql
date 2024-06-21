-- Select the id, name of cities and the corresponding state name using a subquery
-- The subquery finds the state name based on the state_id in the cities table
-- Results are ordered by cities.id in ascending order
SELECT 
    cities.id, 
    cities.name, 
    (SELECT states.name FROM states WHERE states.id = cities.state_id) AS state_name 
FROM 
    cities
JOIN
	state ON cities.state_id = state.id
ORDER BY 
    cities.id ASC;
