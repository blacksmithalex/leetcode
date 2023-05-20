# Write your MySQL query statement below
WITH Extra AS(
SELECT 
    customer_number, 
    COUNT(*) as number_orders
FROM 
    Orders 
GROUP BY 
    customer_number
)

SELECT 
    customer_number
FROM
    Extra
WHERE number_orders = (SELECT MAX(number_orders) FROM Extra);