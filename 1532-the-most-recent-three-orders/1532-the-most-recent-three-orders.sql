# Write your MySQL query statement below

select name as customer_name, customer_id, order_id, order_date
from(
select 
a.*,b.name,row_number() over (partition by a.customer_id order by a.order_date desc) as rnk
from orders a
left join customers b
on a.customer_id = b.customer_id
) C where rnk<=3
order by 1,2,4 desc

;
