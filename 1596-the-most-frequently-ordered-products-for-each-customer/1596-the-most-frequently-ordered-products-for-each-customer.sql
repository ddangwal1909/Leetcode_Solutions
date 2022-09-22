# Write your MySQL query statement below


select 
res.customer_id,
res.product_id,
b.product_name
from(
select a.*,
rank() over (partition by customer_id order by freq desc) as rnk
from (
select 
customer_id,
product_id,
count(*) as freq
from
orders group by 1,2
)a) res 
left join products b
on res.product_id = b.product_id
where res.rnk=1
;