-- Query  to do a list with left joins
-- This query lists movies with genre
SELECT tv_shows.title, tv_show_genres.genre_id
    FROM tv_shows
    LEFT JOIN tv_show_genres
        ON tv_show_genres.show_id = tv_shows.id
    RIGHT JOIN tv_genres
        ON tv_genres.id = tv_show_genres.genre_id
	ORDER BY tv_shows.title;
