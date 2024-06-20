-- This script lists all records from the second_table
-- Excludes rows without a name value
-- Displays the score and the name
-- Records are listed by descending score

SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
