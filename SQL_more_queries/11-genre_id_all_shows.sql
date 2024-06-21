-- Select the title of TV shows and the genre_id from tv_show_genres table
-- Use LEFT JOIN to include all shows even if they don't have a genre
-- Results are ordered by tv_shows.title and tv_show_genres.genre_id in ascending order
SELECT 
    tv_shows.title, 
    tv_show_genres.genre_id 
FROM 
    tv_shows 
LEFT JOIN 
    tv_show_genres ON tv_shows.id = tv_show_genres.show_id 
ORDER BY 
    tv_shows.title ASC, 
    tv_show_genres.genre_id ASC;
