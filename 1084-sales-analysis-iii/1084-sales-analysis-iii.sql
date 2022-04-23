# Write your MySQL query statement below

select
product_id,
product_name
from
(
select 
a.product_id,
b.product_name,
min(sale_date) as sale_date_min,
max(sale_date) as sale_date_max
from sales a
inner join product b
on a.product_id = b.product_id
group by 1,2
) b
where sale_date_min>='2019-01-01' and sale_date_max<='2019-03-31'
order by product_id;
