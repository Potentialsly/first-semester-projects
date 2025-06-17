-- SQL queries for retrieving insights
SELECT o.order_id, c.name AS customer_name, p.name AS product_name, o.quantity, o.order_date
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN products p ON o.product_id = p.product_id
WHERE c.name = 'Alice';

--
SELECT COUNT(*) AS total_orders FROM orders;


--

SELECT SUM(p.price * o.quantity) AS total_revenue
FROM orders o
JOIN products p ON o.product_id = p.product_id;


--
SELECT o.order_id, c.name AS customer_name, p.name AS product_name, o.quantity
FROM orders o
INNER JOIN customers c ON o.customer_id = c.customer_id
INNER JOIN products p ON o.product_id = p.product_id;


--
SELECT p.name AS product_name, o.order_id
FROM products p
LEFT JOIN orders o ON p.product_id = o.product_id;



