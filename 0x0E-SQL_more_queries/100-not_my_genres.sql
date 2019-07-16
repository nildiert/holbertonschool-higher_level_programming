-- Query  to do a list with left joins
-- This query lists movies with genre
SELECT tv_genres.name
    FROM tv_genres
    WHERE tv_genres.id NOT IN
    (SELECT tv_genres.id
    FROM tv_genres
    LEFT JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id
    LEFT JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
    WHERE tv_shows.title = 'Dexter'
    GROUP BY tv_genres.name)
    ORDER BY tv_genres.name ASC;
