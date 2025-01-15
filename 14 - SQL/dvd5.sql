SELECT * FROM job;

INSERT INTO job(job_name)
VALUES 
('Cowboy')

SELECT * FROM job;

DELETE FROM job
WHERE job_name='Cowboy'
RETURNING job_id,job_name;

SELECT * FROM job;

CREATE TABLE information(
	info_id SERIAL PRIMARY KEY,
	title VARCHAR(500) NOT NULL,
	person VARCHAR(50) NOT NULL UNIQUE
);

SELECT * FROM information;

ALTER TABLE information 
RENAME TO new_info;

SELECT * FROM new_info;   --information table is renamed to new_info

ALTER TABLE new_info 
RENAME COLUMN person TO people;

SELECT * FROM new_info;

INSERT INTO new_info(title) 
VALUES ('Some new title');   --ERROR 

--SO DO THIS:
ALTER TABLE new_info
ALTER COLUMN people DROP NOT NULL;

INSERT INTO new_info(title) 
VALUES ('Some new title');

SELECT * FROM new_info;   

SELECT * FROM new_info;

ALTER TABLE new_info
DROP COLUMN people;

SELECT * FROM new_info;

ALTER TABLE new_info 
DROP COLUMN people;
--ERROR : column 'people' do not exist

ALTER TABLE new_info
DROP COLUMN IF EXISTS people;

CREATE TABLE employees(
	emp_id SERIAL PRIMARY KEY,
	first_name VARCHAR(50) NOT NULL,
	last_name VARCHAR(50) NOT NULL,
	birthdate DATE CHECK (birthdate>'1900-01-01'),
	hire_date DATE CHECK (hire_date>birthdate),
	salary INTEGER CHECk (salary>0)
);

SELECT * FROM employees;

INSERT INTO employees(
	first_name,
	last_name,
	birthdate,
	hire_date,
	salary
)
VALUES('Jose','Portilla','1899-11-03','2010-01-01',100)
--ERROR: Values chech constraints

INSERT INTO employees(
	first_name,
	last_name,
	birthdate,
	hire_date,
	salary
)
VALUES('Jose','Portilla','1990-11-03','2010-01-01',100)
	
SELECT * FROM employees;

INSERT INTO employees(
	first_name,
	last_name,
	birthdate,
	hire_date,
	salary
)
VALUES('Samny','Smith','1990-11-03','2010-01-01',-100) 
--ERROR: salary is -ve and constraint is salary>0
	
SELECT * FROM employees;

INSERT INTO employees(
	first_name,
	last_name,
	birthdate,
	hire_date,
	salary
)
VALUES('Samny','Smith','1990-11-03','2010-01-01',100) 
SELECT * FROM employees;

