-- Select the titles of TV shows from tv_shows based on the genre Comedy from tv_genres and tv_show_genres
-- Use INNER JOIN to link tv_genres, tv_show_genres, and tv_shows based on their respective IDs
-- Results are ordered by show title in ascending order
SELECT 
    tv_shows.title
FROM 
    tv_genres
JOIN 
    tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN 
    tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE 
    tv_genres.name = 'Comedy'
ORDER BY 
    tv_shows.title ASC;
