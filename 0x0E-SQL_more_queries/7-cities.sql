-- Create database hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Connect to the newly created database
CONNECT hbtn_0d_usa;

-- Create table cities in the current database
CREATE TABLE IF NOT EXISTS cities
(
	id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	FOREIGN KEY(state_id) REFERENCES states(id)
);
