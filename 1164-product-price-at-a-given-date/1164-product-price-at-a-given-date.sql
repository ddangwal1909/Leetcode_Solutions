# Write your MySQL query statement below



select a.product_id, coalesce(b.final_price,10) as price
from
(
select distinct product_id
from products
) a
left join (select * from (
select product_id, row_number() over (partition by product_id order by change_date desc) as rnk ,  new_price as final_price
from products
where change_date<='2019-08-16'
)c where c.rnk=1 )b
on a.product_id = b.product_id
;