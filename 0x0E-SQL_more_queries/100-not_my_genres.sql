-- Write a script that uses the hbtn_0d_tvshows
--  database to list all genres not linked to the show Dexter
SELECT	name
FROM	tv_genres
WHERE	id NOT IN
	(
		SELECT	genre_id
		FROM	tv_show_genres
			INNER JOIN tv_shows
				ON id = show_id
		WHERE	title = 'Dexter'
	)
ORDER BY name;
