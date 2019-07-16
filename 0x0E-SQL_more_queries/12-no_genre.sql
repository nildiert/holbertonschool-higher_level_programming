-- Query  to do a list with left joins
-- This query lists movies with genre
SELECT tv_shows.title, tv_show_genres.genre_id
       FROM tv_show_genres
       RIGHT OUTER JOIN tv_shows
       	     ON tv_shows.id = tv_show_genres.show_id
	     WHERE show_id IS NULL
	     ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
