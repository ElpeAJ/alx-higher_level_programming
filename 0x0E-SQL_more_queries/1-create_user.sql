-- Create a user with all permissions on
-- local server
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost'
IDENTIFIED BY 'user_0d_1_pwd';

-- Set privileges for the new user
GRANT ALL
ON *.*
TO 'user_0d_1'@'localhost';
