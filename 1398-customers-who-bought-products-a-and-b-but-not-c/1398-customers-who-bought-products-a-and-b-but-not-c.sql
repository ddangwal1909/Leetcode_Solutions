# Write your MySQL query statement below


select 
a.customer_id,a.customer_name
from customers a
inner join(
select customer_id
from orders 
where product_name in ('A','B') and customer_id not in (
select distinct customer_id from orders where product_name in ('C')
)
group by 1
having count(distinct product_name)=2
)b
on a.customer_id=b.customer_id
order by customer_id;