CREATE TABLE IF NOT EXISTS temperature (
	created_on timestamp DEFAULT CURRENT_TIMESTAMP,
    value DOUBLE PRECISION
);

INSERT INTO temperature (value) VALUES (10.5);

