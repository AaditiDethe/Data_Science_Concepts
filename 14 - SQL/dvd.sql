SELECT  * FROM customer
WHERE first_name LIKE 'J%'

SELECT  count(*)FROM customer
WHERE first_name LIKE 'J%'

SELECT  count(*)FROM customer
WHERE first_name LIKE 'J%' AND last_name LIKE 'S%'

SELECT  * FROM customer
WHERE first_name LIKE 'J%' AND last_name LIKE 'S%'

SELECT  * FROM customer
WHERE first_name ILIKE 'j%' AND last_name ILIKE 'j%'

SELECT  * FROM customer
WHERE first_name LIKE '%er%'

SELECT  count(*) FROM customer
WHERE first_name LIKE '%er%'

SELECT  * FROM customer
WHERE first_name LIKE '%her%'

SELECT  count(*) FROM customer
WHERE first_name LIKE '%her%'

SELECT  * FROM customer
WHERE first_name LIKE '%_her%'