-- Select the id, name of cities and the corresponding state name using a subquery
-- The subquery finds the state name based on the state_id in the cities table
-- Results are ordered by cities.id in ascending order
SELECT 
    cities.id, 
    cities.name, 
	states.name
FROM 
    cities
JOIN
	states ON cities.state_id = states.id
ORDER BY 
    cities.id ASC;
