-- Select the title of TV shows and the genre_id from tv_show_genres table
-- Use LEFT JOIN to include only shows that do not have a genre linked (genre_id IS NULL)
-- Results are ordered by tv_shows.title and tv_show_genres.genre_id in ascending order
SELECT 
    tv_shows.title, 
    tv_show_genres.genre_id 
FROM 
    tv_shows 
LEFT JOIN 
    tv_show_genres ON tv_shows.id = tv_show_genres.show_id 
WHERE 
    tv_show_genres.genre_id IS NULL 
ORDER BY 
    tv_shows.title ASC, 
    tv_show_genres.genre_id ASC;
