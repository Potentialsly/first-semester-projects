-- SQL script to create necessary tables

CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    name TEXT,
    email TEXT
);

CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    name TEXT,
    price NUMERIC
);

CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES customers(customer_id),
    product_id INT REFERENCES products(product_id),
    quantity INT,
    order_date DATE
);

ALTER TABLE products ADD COLUMN stock INT DEFAULT 0;
