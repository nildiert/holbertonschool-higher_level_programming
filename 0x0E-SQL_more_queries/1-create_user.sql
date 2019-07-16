-- Query  to list privileges
-- This query lists all privileges of two users
CREATE USER user_0d_1@localhost IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON * . * TO user_0d_1@localhost;
