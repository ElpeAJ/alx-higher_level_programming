-- Prints the number of occurence
-- of records for each score
SELECT	score,
	COUNT(*) AS number
FROM	second_table
GROUP BY score
ORDER BY number DESC;
