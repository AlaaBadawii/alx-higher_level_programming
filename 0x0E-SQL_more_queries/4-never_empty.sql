-- script that creates the table id_not_null on your MySQL server
CREATE TABLE IF NOT EXISTS id_not_null(
	id INT 1 UNIQUE,
	name VARCHAR(256)
);
