-- Retrieves records without NULL name values
SELECT	score, name
FROM	second_table
WHERE NAME IS NOT NULL
ORDER BY score DESC;
