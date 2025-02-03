-- Total Sales
SELECT SUM(amount) AS total_sales FROM sales;

-- Top 5 Customers
SELECT user_id, SUM(amount) AS total_spent
FROM sales
GROUP BY user_id
ORDER BY total_spent DESC
LIMIT 5;