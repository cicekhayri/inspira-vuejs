-- Up
CREATE TABLE users (
	id INTEGER NOT NULL,
	name VARCHAR(255) NOT NULL,
	email VARCHAR(255) NOT NULL,
	address VARCHAR(255) NULL,
	PRIMARY KEY (id),
	UNIQUE (email)
);
-- Down
