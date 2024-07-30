CREATE TABLE restaurants (
  name TEXT,
  cuisine TEXT,
  review INTEGER,
  health TEXT
);

INSERT INTO restaurants (name, cuisine, review, health) 
VALUES ('Steak Farm', 'Steak', 4,'A');

INSERT INTO restaurants (name, cuisine, review, health) 
VALUES ('Beetroot Cafe', 'Vegetarian', 5,'A');

INSERT INTO restaurants (name, cuisine, review, health) 
VALUES ('Foodcamp', 'Fast Food', 5,'B');

INSERT INTO restaurants (name, cuisine, review, health) 
VALUES ('Chippy Dale', 'Fast Food', 3,'C');

INSERT INTO restaurants (name, cuisine, review, health) 
VALUES ('Crazy Pickle', 'Eastern European', NULL, NULL);

SELECT *
FROM restaurants;

SELECT DISTINCT cuisine
FROM restaurants;

SELECT *
FROM restaurants
WHERE cuisine = 'Vegetarian';

SELECT *
FROM restaurants
WHERE review >= 4;

SELECT *
FROM restaurants
WHERE cuisine = 'Steak' 
  AND health = 'A';

SELECT *
FROM restaurants
WHERE name LIKE '%beetroot%';

SELECT *
FROM restaurants
WHERE health = 'A'
    OR health = 'B'

SELECT *
FROM restaurants
WHERE health IS NULL;

SELECT *
FROM restaurants
ORDER BY review DESC
LIMIT 3;

SELECT name,
 CASE
  WHEN review > 5 THEN 'Amazing'
  WHEN review > 4 THEN 'Great'
  WHEN review > 3 THEN 'Good'
  ELSE 'Fine'
 END AS 'Review'
FROM restaurants;