-- answers.sql
-- Assignment: SQL Basics

-- 1. Create a new database
CREATE DATABASE salesDB;

-- 2. Drop a demo database
DROP DATABASE demo;

-- Optional practice (You can run this after creating the database)
USE salesDB;

-- Create a sample table
CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(20)
);

-- Add some sample records
INSERT INTO customers (full_name, email, phone)
VALUES 
('Bradly kiptanui', 'bradlykiptanui@gmail.com', '0705510920'),
('Brian Otieno', 'brianotieno@gmail.com', '0723456789');

-- View all customer records
SELECT * FROM customers;
