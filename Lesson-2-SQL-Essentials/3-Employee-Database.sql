CREATE DATABASE EmployeeDB;
USE EmployeeDB;

CREATE TABLE Departments (
      department_id INT PRIMARY KEY,
      department_name VARCHAR(100)
    );
    
    CREATE TABLE Employees (
      employee_id INT PRIMARY KEY,
      name VARCHAR(100),
      age INT,
      department_id INT,
      FOREIGN KEY (department_id) REFERENCES Departments(department_id)
    );
    
    -- Task 1
    -- SQL DISTINCT department that employee work
SELECT DISTINCT department_id
FROM Employees;

-- Task 2
-- SQL COUNT functionality
SELECT department_id, COUNT(*) AS employee_count
FROM Employees
GROUP BY department_id;

-- Task 3
-- SQL BETWEEN functionality
SELECT name, age, department_id
FROM Employees
WHERE age BETWEEN 25 AND 30;