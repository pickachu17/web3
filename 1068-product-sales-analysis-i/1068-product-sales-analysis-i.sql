# Write your MySQL query statement below
SELECT product_name, year,  price 
from SALES
INNER JOIN product ON sales.product_id=product.product_id;