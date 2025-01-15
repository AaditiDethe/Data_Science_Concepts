SELECT * FROM customer 
WHERE first_name NOT LIKE '_her%'

SELECT count(*) FROM customer 
WHERE first_name NOT LIKE '_her%'

SELECT * FROM customer 
WHERE first_name LIKE 'A%'
ORDER BY last_name

SELECT * FROM customer 
WHERE first_name LIKE 'A%' AND last_name NOT LIKE 'B%'
ORDER BY last_name

SELECT count(*) FROM payment
WHERE amount>56uu

SELECT count(amount) FROM payment
WHERE amount>5

SELECT count(*) FROM actor
WHERE first_name LIKE 'P%'

SELECT count(DISTINCT(district)) FROM address;

SELECT count(distinct(address_id)) from address;

SELECT  DISTINCT(district) FROM address;

SELECT COUNT(*) FROM film
WHERE rating='R' AND replacement_cost BETWEEN 5 AND 15;

SELECT count(*) FROM film 
WHERE title LIKE '%Truman%'

SELECT count(title) FROM film 
WHERE title LIKE '%Truman%'

SELECT * FROM film 
WHERE title LIKE '%Truman%'

SELECT MIN(replacement_cost) FROM film;

SELECT MAX(replacement_cost) FROM film;

SELECT MAX(replacement_cost) , MIN(replacement_cost)  FROM film;