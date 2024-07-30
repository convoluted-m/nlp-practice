CREATE TABLE friends (
  id INTEGER,
  name TEXT,
  birthday DATE
);

INSERT INTO friends (id, name, birthday) 
VALUES (1, 'Ororo Munroe','1940-05-30');

INSERT INTO friends (id, name, birthday) 
VALUES (2, 'Mickey  Mouse','1990-05-30');

INSERT INTO friends (id, name, birthday) 
VALUES (3, 'Bugs Bunny','1998-01-02');

UPDATE friends
SET name = 'Storm'
WHERE id = 1;


ALTER TABLE friends
ADD COLUMN email TEXT;

UPDATE friends
SET email = 'storm@codecademy.com'
WHERE id = 1;

UPDATE friends
SET email = 'mickey@codecademy.com'
WHERE id = 2;

UPDATE friends
SET email = 'bugs@codecademy.com'
WHERE id = 3; 

DELETE FROM friends
WHERE id = 1;

UPDATE friends
SET id = '1'
WHERE id = 2;

UPDATE friends
SET id = '2'
WHERE id = 3;

SELECT *
FROM friends;