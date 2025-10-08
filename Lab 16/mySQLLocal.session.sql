CREATE TABLE employees (
    emp_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    department VARCHAR(50),
    salary DECIMAL(10,2),
    hire_date DATE
);



-- 3. Insert sample data into employees
INSERT INTO employees (first_name, last_name, department, salary, hire_date) VALUES
('Amit', 'Sharma', 'HR', 45000, '2020-05-20'),
('Priya', 'Patel', 'Finance', 60000, '2021-02-10'),
('Ravi', 'Kumar', 'IT', 55000, '2019-08-14'),
('Neha', 'Reddy', 'Marketing', 48000, '2022-01-05'),
('Arjun', 'Singh', 'IT', 62000, '2020-09-12');

SELECT * FROM employees;
-- 2. Create the employees table
CREATE TABLE employees (
    emp_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    department VARCHAR(50),
    salary DECIMAL(10,2),
    hire_date DATE
);

-- 3. Insert sample data into employees
INSERT INTO employees (first_name, last_name, department, salary, hire_date) VALUES
('Amit', 'Sharma', 'HR', 45000, '2020-05-20'),
('Priya', 'Patel', 'Finance', 60000, '2021-02-10'),
('Ravi', 'Kumar', 'IT', 55000, '2019-08-14'),
('Neha', 'Reddy', 'Marketing', 48000, '2022-01-05'),
('Arjun', 'Singh', 'IT', 62000, '2020-09-12');

-- 4. Create the departments table
DROP TABLE IF EXISTS departments;
CREATE TABLE departments (
    dept_id INT AUTO_INCREMENT PRIMARY KEY,
    dept_name VARCHAR(50) NOT NULL,
    location VARCHAR(50)
);

-- 5. Insert sample data into departments
INSERT INTO departments (dept_name, location) VALUES
('HR', 'Hyderabad'),
('Finance', 'Mumbai'),
('IT', 'Banglore'),
('Marketing', 'Delhi');

-- 6. Select all records from departments
SELECT * FROM departments;

-- 7. Queries on employees table

-- 1. Display all records from the employees table.
SELECT * FROM employees;

-- 2. Display only employee names and their departments.
SELECT first_name, last_name, department FROM employees;

-- 3. Show unique department names.
SELECT DISTINCT department FROM employees;

-- 4. Find employees with salary greater than 50000.
SELECT * FROM employees WHERE salary > 50000;

-- 5. Find employees from the IT department.
SELECT * FROM employees WHERE department = 'IT';

-- 6. Display employees hired after 2020.
SELECT * FROM employees WHERE hire_date > '2020-12-31';

-- 7. Show employees in ascending order of salary.
SELECT * FROM employees ORDER BY salary ASC;

-- 8. Show top 3 highest-paid employees.
SELECT * FROM employees ORDER BY salary DESC LIMIT 3;

-- 9. Count total employees in the company.
SELECT COUNT(*) AS total_employees FROM employees;

-- 10. Find the average salary of employees.
SELECT AVG(salary) AS average_salary FROM employees;

-- 11. Find the highest and lowest salary.
SELECT MAX(salary) AS highest_salary, MIN(salary) AS lowest_salary FROM employees;

-- 12. Find total salary expenditure per department.
SELECT department, SUM(salary) AS total_salary FROM employees GROUP BY department;

-- 13. Display departments having more than one employee.
SELECT department, COUNT() AS emp_count FROM employees GROUP BY department HAVING COUNT() > 1;

-- 14. Show average salary by department.
SELECT department, AVG(salary) AS avg_salary FROM employees GROUP BY department;

-- 15. Count employees hired each year.
SELECT YEAR(hire_date) AS year, COUNT(*) AS emp_count FROM employees GROUP BY YEAR(hire_date);

-- 16. List employees with their department locations.
SELECT e.*, d.location
FROM employees e
JOIN departments d ON e.department = d.dept_name;

-- 17. Find employees working in Bangalore.
SELECT e.*
FROM employees e
JOIN departments d ON e.department = d.dept_name
WHERE d.location = 'Banglore';

-- 18. Display all employees even if they don’t belong to a department.
SELECT e.*, d.location
FROM employees e
LEFT JOIN departments d ON e.department = d.dept_name;

-- 19. Find departments with no employees.
SELECT d.*
FROM departments d
LEFT JOIN employees e ON d.dept_name = e.department
WHERE e.emp_id IS NULL;

-- 20. Count employees in each department.
SELECT department, COUNT(*) AS emp_count FROM employees GROUP BY department;

-- 21. Find employees earning above average salary.
SELECT * FROM employees WHERE salary > (SELECT AVG(salary) FROM employees);

-- 22. Find the department with the highest average salary.
SELECT department, AVG(salary) AS avg_salary
FROM employees
GROUP BY department
ORDER BY avg_salary DESC
LIMIT 1;

-- 23. Find employees hired most recently.
SELECT * FROM employees WHERE hire_date = (SELECT MAX(hire_date) FROM employees);

-- 24. Find employees earning the second highest salary.
SELECT *
FROM employees
WHERE salary = (
    SELECT DISTINCT salary
    FROM employees
    ORDER BY salary DESC
    LIMIT 1 OFFSET 1
);

-- 25. Find all employees in the same department as 'Amit Sharma'.
SELECT *
FROM employees
WHERE department = (
    SELECT department FROM employees WHERE first_name = 'Amit' AND last_name = 'Sharma'
);

-- 26. Increase salary by 10% for IT employees.
UPDATE employees SET salary = salary * 1.10 WHERE department = 'IT';

-- 27. Change department of employee 'Ravi' to Marketing.
UPDATE employees SET department = 'Marketing' WHERE first_name = 'Ravi';

-- 28. Delete employees with salary below 40000.
DELETE FROM employees WHERE salary < 40000;

-- 29. Add a new column 'email' to employees.
ALTER TABLE employees ADD COLUMN email VARCHAR(100);

-- 30. Update email IDs for all employees.
UPDATE employees SET email = CONCAT(LOWER(first_name), '.', LOWER(last_name), '@company.com');

-- 31. Find top 2 departments by average salary.
SELECT department, AVG(salary) AS avg_salary
FROM employees
GROUP BY department
ORDER BY avg_salary DESC
LIMIT 2;

-- 32. Find how many employees work in each city.
SELECT d.location, COUNT(e.emp_id) AS emp_count
FROM employees e
JOIN departments d ON e.department = d.dept_name
GROUP BY d.location;

-- 33. Show employee count and total salary together.
SELECT COUNT(*) AS emp_count, SUM(salary) AS total_salary FROM employees;

-- 34. Display employees with names starting with 'A'.
SELECT * FROM employees WHERE first_name LIKE 'A%';

-- 35. Display employees whose last name ends with 'a'.
SELECT * FROM employees WHERE last_name LIKE '%a';

-- 36. Find employees hired in 2020.
SELECT * FROM employees WHERE YEAR(hire_date) = 2020;

-- 37. Show number of days since each employee was hired.
SELECT *, DATEDIFF(CURDATE(), hire_date) AS days_since_hired FROM employees;

-- 38. Display employee names in uppercase.
SELECT UPPER(first_name) AS first_name, UPPER(last_name) AS last_name FROM employees;

-- 39. Concatenate first and last names.
SELECT CONCAT(first_name, ' ', last_name) AS full_name FROM employees;

-- 40. Find employees whose salary is between 45000 and 60000.
SELECT * FROM employees WHERE salary BETWEEN 45000 AND 60000;

-- 41. Create a view for high salary employees (>55000).
CREATE VIEW high_salary_employees AS
SELECT * FROM employees WHERE salary > 55000;

-- 42. Display all records from the view.
SELECT * FROM high_salary_employees;

-- 43. Add NOT NULL constraint to department name.
ALTER TABLE employees MODIFY department VARCHAR(50) NOT NULL;

-- 44. Drop the view.
DROP VIEW IF EXISTS high_salary_employees;

-- 45. Rename the employees table to staff.
RENAME TABLE employees TO staff;

-- 46. Create a backup copy of the employees table.
CREATE TABLE employees_backup AS SELECT * FROM staff;

-- 47. Delete all data but keep the structure.
TRUNCATE TABLE employees_backup;

-- 48. Drop the employees backup table.
DROP TABLE IF EXISTS employees_backup;

-- 49. Create an index on employee last name.
CREATE INDEX idx_lastname ON staff(last_name);

-- 50. Drop the index.
DROP INDEX idx_lastname ON staff;

-- 51. Show staff with department locations (after renaming)
SELECT e.*, d.location
FROM staff e
JOIN departments d ON e.department = d.dept_name;