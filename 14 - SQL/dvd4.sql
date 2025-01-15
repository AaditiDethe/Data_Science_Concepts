SELECT * FROM customer;

SELECT * FROM address;

SELECT *FROM address
INNER JOIN customer
ON address.address_id=customer.address_id;

SELECT *FROM address
INNER JOIN customer
ON address.address_id=customer.address_id
WHERE district='California';

SELECT district,email FROM address
INNER JOIN customer ON
address.address_id=customer.address_id
WHERE district='California';

SELECT * FROM  film;

SELECT * FROM actor;

SELECT * FROM film_actor;

SELECT * FROM actor
INNER JOIN film_actor
ON actor.actor_id=film_actor.actor_id;   --film_id is common

SELECT * FROM film
INNER JOIN film_actor
ON actor.actor_id=film_actor.actor_id
INNER JOIN film
ON film_actor.film_id=film.film_id;

SELECT title,first_name,last_name FROM actor
INNER JOIN film_actor
ON actor.actor_id=film_actor.actor_id
INNER JOIN film
ON film_actor.film_id=film.film_id;

SELECT title,first_name,last_name FROM actor
INNER JOIN film_actor
ON actor.actor_id=film_actor.actor_id
INNER JOIN film
ON film_actor.film_id=film.film_id
WHERE first_name='Nick' AND
last_name='Wahlberg';

SELECT * FROM payment;



