-- Query  to do a list with left joins
-- This query lists movies with genre
SELECT tv_genres.name
       FROM tv_show_genres
       LEFT JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
       LEFT JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
       WHERE tv_shows.title = 'Dexter' ORDER BY tv_genres.name ASC;
