-- SQL script to insert sample data
-- Customers
INSERT INTO customers (name, email) VALUES
('Alice', 'alice@example.com'),
('Bob', 'bob@example.com'),
('Charlie', 'charlie@example.com'),
('Daisy', 'daisy@example.com'),
('Eve', 'eve@example.com');

-- Products
INSERT INTO products (name, price, stock) VALUES
('Milk', 2.5, 100),
('Bread', 1.5, 50),
('Eggs', 0.2, 500),
('Soap', 1.0, 200),
('Juice', 3.0, 75);

-- Orders
INSERT INTO orders (customer_id, product_id, quantity, order_date) VALUES
(1, 1, 2, '2025-06-01'),
(2, 3, 12, '2025-06-02'),
(3, 2, 5, '2025-06-03'),
(1, 4, 3, '2025-06-04'),
(5, 5, 1, '2025-06-05');
