DROP TABLE IF EXISTS Restaurant;

-- Create Restaurant table
CREATE TABLE IF NOT EXISTS Restaurant (
  name TEXT,
  neighborhood TEXT,
  cuisine TEXT, 
  review REAL,
  price TEXT,
  health TEXT
);

-- Insert data
INSERT INTO Restaurant (name, neighborhood, cuisine, review, price, health)
VALUES
  ('Candy Peter', 'Brooklyn', 'Steak', 4.4, '$$$$', 'A'),
  ('Jongro', 'Midtown', 'Korean', 3.5, '$$', 'A'),
  ('Pocha', 'Midtown', 'Pizza', 4.0, '$$$', 'B'),
  ('Lighthouse', 'Queens', 'Chinese', 3.9, '$', 'A'),
  ('Minca', 'Downtown', 'American', 4.6, '$$$', ''),
  ('Marea', 'Chinatown', 'Chinese', 3.0, '$$', ''),
  ('Dirty Candy', 'Uptown', 'Italian', 4.9, '$$$$', 'B'),
  ('Di Fara Pizza', 'Brooklyn', 'Pizza', 3.8, '$$', 'A'),
  ('Golden Unicorn', 'Uptown', 'Italian', 3.8, '$$', 'A');

-- BASED ON THE DATA ABOVE, LET'S ANSWER THE FOLLOWING QUESTIONS
SELECT * FROM Restaurant;
-- 1) What are the distinct (or unique) neighborhoods?
SELECT DISTINCT neighborhood
FROM Restaurant; 
-- 2) What are the distinct cuisine types?
SELECT DISTINCT cuisine
FROM Restaurant;
-- 3) What are the options for Chinese takeout?
SELECT * FROM Restaurant
WHERE LOWER (cuisine)= "chinese";
-- 4) Which restaurants have reviews 4 and above?
SELECT * FROM Restaurant
WHERE review>=4;
-- 5) Which Italian restaurants have a price category $$ or $$$
SELECT * FROM Restaurant
WHERE cuisine= "Italian" 
AND (price= "$$" OR price= "$$$");

SELECT * FROM Restaurant
WHERE cuisine= "Italian" 
AND price IN ("$$" , "$$$");

-- 6) Which restaurants with exactly $$$ price category?
SELECT * FROM Restaurant
WHERE price= "$$$";
-- 7) Which restaurants contain "Candy" in their names?
SELECT * FROM Restaurant
WHERE name LIKE "Candy%";
-- 8) Which restaurants in Midtown, Downtown, or Chinatown?

-- 9) Which restaurants have Health grade pending (empty value)?

-- 10) Find the top 4 restaurants based on reviews
