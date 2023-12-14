-- Create hbtn_0d_2 database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create new user: user_0d_2
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost'
IDENTIFIED BY 'user_0d_2_pwd';

-- Grant user_0d_2 the select
-- privilege in the database hbtn_0d_2
GRANT SELECT
ON hbtn_0d_2.*
TO 'user_0d_2'@'localhost';
