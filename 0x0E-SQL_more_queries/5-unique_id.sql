-- Query  to create table
-- This query creates a table in a database passes like arg
CREATE TABLE IF NOT EXISTS unique_id(
       id INT,
       name VARCHAR(256) NOT NULL,
       UNIQUE KEY(id)
);
