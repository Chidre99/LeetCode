# Write your MySQL query statement below

select p.product_id,
round(ifnull(sum(p.price * us.units)/sum(us.units),0),2) as average_price 
from prices as p
left join unitssold as us
on p.product_id  = us.product_id 
AND us.purchase_date BETWEEN p.start_date AND p.end_date
group by p.product_id 