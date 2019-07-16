-- Query  to do a list with left joins
-- This query lists movies with genre
SELECT tv_genres.name as genre, COUNT(tv_genres.name) as number_of_shows
       FROM tv_genres
       RIGHT JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id
       GROUP BY tv_genres.name
       ORDER BY number_of_shows DESC
;
