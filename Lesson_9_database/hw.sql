CREATE DATABASE IF NOT EXISTS hw;
USE hw;

CREATE TABLE IF NOT EXISTS employees(
	id INT UNSIGNED NOT NULL AUTO_INCREMENT primary key,
	first_name VARCHAR(20) NOT NULL ,
	last_name VARCHAR(20) NOT NULL,
	position VARCHAR(100) NOT NULL,
	salary NUMERIC(19, 4) NOT NULL
);

INSERT INTO employees(first_name, last_name, position, salary) VALUES ('Baley', 'Elijah', 'Police officer', 100000);
INSERT INTO employees(first_name, last_name, position, salary) VALUES ('R. Daneel', 'Olivaw', 'Police officer', 0);
INSERT INTO employees(first_name, last_name, position, salary) VALUES ('Julius', 'Enderby', 'Commissioner of Police', 300000);
INSERT INTO employees(first_name, last_name, position, salary) VALUES ('R. Sammy', 'None', 'Robot assigned to the Police Department', 0);
INSERT INTO employees(first_name, last_name, position, salary) VALUES ('Han', 'Fastolfe', 'Roboticist', 700000);

SELECT * FROM hw.employees WHERE salary > 30000;
SELECT * FROM hw.employees WHERE salary > 30000 AND position = 'Police Officer';

CREATE TABLE IF NOT EXISTS subordination(
	superior_id INT UNSIGNED,
	worker_id INT UNSIGNED,
    FOREIGN KEY (superior_id) REFERENCES employees(id),
    FOREIGN KEY (worker_id) REFERENCES employees(id),
    PRIMARY KEY(superior_id, worker_id)
);

INSERT INTO subordination(superior_id, worker_id) VALUES (3, 1), (3, 2), (3, 4), (5, 2), (5, 3);

SELECT * FROM employees
INNER JOIN subordination ON subordination.worker_id = employees.id
WHERE subordination.superior_id = (
	SELECT id FROM employees WHERE first_name = 'Han'
);
