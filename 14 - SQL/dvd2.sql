SELECT * FROM payment;

SELECT customer_id,staff_id,SUM(amount) FROM payment
GROUP BY staff_id,customer_id;

SELECT staff_id,customer_id,SUM(amount) FROM payment
GROUP BY staff_id,customer_id
ORDER BY staff_id;

SELECT staff_id,customer_id,SUM(amount) FROM payment
GROUP BY staff_id,customer_id
ORDER BY staff_id,customer_id;

SELECT staff_id,customer_id,SUM(amount) FROM payment
GROUP BY staff_id,customer_id
ORDER BY SUM(amount) ;

SELECT DATE(payment_date) FROM payment;

SELECT DATE(payment_date),SUM(amount) FROM payment
GROUP BY DATE(payment_date);

SELECT DATE(payment_date),SUM(amount) FROM payment
GROUP BY DATE(payment_date)
ORDER BY SUM(amount) DESC;

SELECT staff_id,COUNT(amount)
FROM payment
GROUP BY staff_id;

SELECT rating,AVG(replacement_cost)
FROM film
GROUP BY rating;

SELECT rating,
ROUND(AVG(replacement_cost),2)
FROM film
GROUP BY rating;

SELECT customer_id,SUM(amount)
FROM payment
GROUP BY customer_id
ORDER BY SUM(amount) DESC
LIMIT 5;

SELECT customer_id FROM payment;

SELECT customer_id FROM payment
GROUP BY customer_id;

SELECT customer_id,SUM(amount) FROM payment
GROUP BY customer_id
ORDER BY COUNT(amount) DESC;

SELECT customer_id,SUM(amount) FROM payment
GROUP BY customer_id
HAVING SUM(amount)>100;

SELECT customer_id,SUM(amount) FROM payment
WHERE customer_id NOT IN (184,87,477)
GROUP BY customer_id;


