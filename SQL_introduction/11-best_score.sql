-- This script selects all records from the second_table
-- where the score is greater than or equal to 10.
-- The results display both the score and the name,
-- and are ordered by score in descending order.

SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
