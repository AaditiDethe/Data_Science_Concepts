SELECT * FROM customer;

SELECT customer_id FROM customer;

SELECT customer_id,
CASE
	WHEN (customer_id<=100) THEN 'Premium'
	WHEN (customer_id BETWEEN 100 AND 200) THEN 'Plus'
	ELSE 'Normal'
END
FROM customer;

SELECT customer_id,
CASE
	WHEN (customer_id<=100) THEN 'Premium'
	WHEN (customer_id BETWEEN 100 AND 200) THEN 'Plus'
	ELSE 'Normal'
END AS customer_class
FROM customer;

SELECT customer_id,    --comma is important
CASE customer_id
	WHEN 2 THEN 'Winner'
	WHEN 5 THEN 'Second Place'
	ELSE 'Normal'
END AS raffle_results
FROM customer;

SELECT * FROM film;

SELECT rental_rate FROM film;


SELECT rental_rate,
CASE rental_rate
	WHEN (4.99) THEN '5'
	WHEN (2.99) THEN '3'
	ELSE '1'
END
FROM film;

SELECT 
SUM(CASE rental_rate
	WHEN 0.99 THEN 1
	ELSE 0
END) AS number_of_bargains
FROM film

