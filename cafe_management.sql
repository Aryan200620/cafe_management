CREATE DATABASE IF NOT EXISTS cafe_management;

USE cafe_management;

CREATE TABLE IF NOT EXISTS users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL
);

INSERT IGNORE INTO users(username, password)
VALUES ('admin', 'admin123');

CREATE TABLE IF NOT EXISTS menu (
    id INT PRIMARY KEY AUTO_INCREMENT,
    item_name VARCHAR(100) NOT NULL,
    category VARCHAR(50) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    quantity INT NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS customers (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS employees (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(20),
    role VARCHAR(50),
    salary DECIMAL(10,2)
);

CREATE TABLE IF NOT EXISTS orders (
    id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    total DECIMAL(10,2),
    FOREIGN KEY (customer_id)
        REFERENCES customers(id)
        ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS order_items (
    id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT,
    menu_id INT,
    quantity INT,
    price DECIMAL(10,2),
    FOREIGN KEY (order_id)
        REFERENCES orders(id)
        ON DELETE CASCADE,
    FOREIGN KEY (menu_id)
        REFERENCES menu(id)
        ON DELETE CASCADE
);

INSERT INTO menu(item_name, category, price, quantity)
SELECT 'Cappuccino', 'Coffee', 120, 50
WHERE NOT EXISTS (SELECT 1 FROM menu WHERE item_name = 'Cappuccino');

INSERT INTO menu(item_name, category, price, quantity)
SELECT 'Espresso', 'Coffee', 90, 50
WHERE NOT EXISTS (SELECT 1 FROM menu WHERE item_name = 'Espresso');

INSERT INTO menu(item_name, category, price, quantity)
SELECT 'Cold Coffee', 'Beverage', 150, 40
WHERE NOT EXISTS (SELECT 1 FROM menu WHERE item_name = 'Cold Coffee');

INSERT INTO menu(item_name, category, price, quantity)
SELECT 'Veg Burger', 'Fast Food', 180, 30
WHERE NOT EXISTS (SELECT 1 FROM menu WHERE item_name = 'Veg Burger');

INSERT INTO menu(item_name, category, price, quantity)
SELECT 'Cheese Pizza', 'Fast Food', 250, 25
WHERE NOT EXISTS (SELECT 1 FROM menu WHERE item_name = 'Cheese Pizza');

INSERT INTO menu(item_name, category, price, quantity)
SELECT 'French Fries', 'Snacks', 100, 40
WHERE NOT EXISTS (SELECT 1 FROM menu WHERE item_name = 'French Fries');

INSERT INTO menu(item_name, category, price, quantity)
SELECT 'Chocolate Cake', 'Dessert', 140, 20
WHERE NOT EXISTS (SELECT 1 FROM menu WHERE item_name = 'Chocolate Cake');

INSERT INTO menu(item_name, category, price, quantity)
SELECT 'Ice Cream', 'Dessert', 100, 30
WHERE NOT EXISTS (SELECT 1 FROM menu WHERE item_name = 'Ice Cream');

INSERT INTO customers(name, phone)
SELECT 'Rahul Sharma', '9876543210'
WHERE NOT EXISTS (SELECT 1 FROM customers WHERE phone = '9876543210');

INSERT INTO customers(name, phone)
SELECT 'Amit Kumar', '9876543211'
WHERE NOT EXISTS (SELECT 1 FROM customers WHERE phone = '9876543211');
