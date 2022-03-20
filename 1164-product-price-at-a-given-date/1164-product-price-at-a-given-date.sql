# Write your MySQL query statement below


(
select product_id, new_price as price
from(
select 
* , row_number() over (partition by product_id order by change_date desc) as rnk
from 
(
select * from products 
where change_date<='2019-08-16'
) a
)b
where rnk=1
)
union
(
select distinct product_id,10 as price from products
where product_id not in ( select distinct product_id from products 
where change_date<='2019-08-16')
)