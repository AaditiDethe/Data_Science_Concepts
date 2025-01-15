trSELECT customer_id, COUNT(*)
FROM payment
GROUP BY customer_id
HAVING COUNT(*)>=40;

SELECT customer_id,SUM(amount)
FROM payment
WHERE staff_id=2
GROUP BY customer_id
HAVING SUM(amount)>100;

SELECT amount as rental_price FROM payment;

SELECT SUM(amount) as net_revenue FROM payment;

SELECT COUNT(amount) AS num_of_transactions FROM payment;

SELECT COUNT(*) AS num_of_transactions FROM payment;

SELECT customer_id,SUM(amount)
FROM payment
GROUP BY customer_id;

SELECT customer_id,SUM(amount) AS total_spent
FROM payment
GROUP BY customer_id;

SELECT customer_id,SUM(amount) AS total_spent
FROM payment
GROUP BY customer_id
HAVING SUM(amount)>100

SELECT customer_id,SUM(amount)
FROM payment
GROUP BY customer_id
HAVING SUM(amount)>100

SELECT customer_id,SUM(amount) AS total_spent
FROM payment
GROUP BY customer_id
HAVING total_spent>100;

SELECT customer_id,amount
FROM payment
WHERE amount > 2;

SELECT customer_id,amount AS new_name
FROM payment
WHERE new_name> 2;

SELECT * FROM customer;

SELECT * FROM payment;

SELECT payment_id,payment.customer_id,first_name FROM payment
INNER JOIN customer
ON payment.customer_id=customer.customer_id;

SELECT payment_id,payment.customer_id,first_name FROM customer
INNER JOIN payment
ON payment.customer_id=customer.customer_id;

SELECT * FROM customer
FULL OUTER JOIN payment
ON customer.customer_id=payment.customer_id;

SELECT * FROM film;

SELECT * FROM inventory;

SELECT film.film_id,title,inventory_id
FROM film
LEFT JOIN inventory ON
inventory.film_id=film.film_id;

SELECT film.film_id,title,inventory_id,store_id
FROM film
LEFT JOIN inventory ON
inventory.film_id=film.film_id;

SELECT film.film_id,title,inventory_id,store_id
FROM film
LEFT JOIN inventory ON
inventory.film_id=film.film_id
WHERE inventory.film_id IS null;
--it will display null values

SELECT film.film_id,title,inventory_id,store_id
FROM film
RIGHT JOIN inventory ON
inventory.film_id=film.film_id;

SELECT film.film_id,title,inventory_id,store_id
FROM inventory
RIGHT JOIN film ON
inventory.film_id=film.film_id;

SELECT film.film_id,title,inventory_id,store_id
FROM inventory 
RIGHT JOIN film ON
inventory.film_id=film.film_id
WHERE inventory.film_id IS null;

