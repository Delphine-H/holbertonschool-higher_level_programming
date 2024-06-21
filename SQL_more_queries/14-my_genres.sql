-- Select the genre names from tv_genres based on the show Dexter from tv_shows and tv_show_genres
-- Use INNER JOIN to link tv_shows, tv_show_genres, and tv_genres based on their respective IDs
-- Results are ordered by genre name in ascending order
SELECT 
    tv_genres.name
FROM 
    tv_shows
JOIN 
    tv_show_genres ON tv_shows.id = tv_show_genres.show_id
JOIN 
    tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE 
    tv_shows.title = 'Dexter'
ORDER BY 
    tv_genres.name ASC;
