-- Select the title of TV shows and their corresponding genres from tv_shows, tv_genres, and tv_show_genres
-- Use LEFT JOIN to include all shows from tv_shows and match genres from tv_show_genres and tv_genres
-- Results are ordered by show title and genre name in ascending order
SELECT 
    tv_shows.title,
    tv_genres.name
FROM 
    tv_shows
LEFT JOIN 
    tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN 
    tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY 
    tv_shows.title ASC, tv_genres.name ASC;
