-- 1. สินค้าไหนขายดีสุด
SELECT
    product_name,
    SUM(quantity) AS total_quantity,
    SUM(total_amount) AS total_sales
FROM orders
WHERE is_successful = TRUE
GROUP BY product_name
ORDER BY total_sales DESC;

-- 2. what month has the highest sales
SELECT
    EXTRACT(MONTH FROM order_date) AS month,
    SUM(total_amount) AS total_sales
FROM orders
WHERE is_successful = TRUE
GROUP BY EXTRACT(MONTH FROM order_date)
ORDER BY month DESC;

-- 3. what category has the highest sales and in each category how many orders?
SELECT
    category,
    COUNT(*) AS total_orders,
    SUM(total_amount) AS total_sales
FROM orders
WHERE is_successful = TRUE
GROUP BY category
ORDER BY total_sales DESC;

-- 4. each od category rank by total sales
SELECT
    category,
    SUM(total_amount) AS total_sales,
    RANK() OVER (ORDER BY SUM(total_amount) DESC) AS sales_rank
FROM orders
WHERE is_successful = TRUE
GROUP BY category
ORDER BY total_sales DESC;