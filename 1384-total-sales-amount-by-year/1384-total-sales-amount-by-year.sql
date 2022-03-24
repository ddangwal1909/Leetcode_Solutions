# Write your MySQL query statement below

with cte as 
(select * from
  (select product_id, '2018' as report_year,
       average_daily_sales*(datediff(least('2018-12-31', period_end), greatest('2018-01-01', period_start))+1) as total_amount from sales
   union all
   select product_id, '2019' as report_year, 
       average_daily_sales*(datediff(least('2019-12-31', period_end), greatest('2019-01-01', period_start))+1) as total_amount from sales
   union all
   select product_id, '2020' as report_year, 
       average_daily_sales*(datediff(least('2020-12-31', period_end), greatest('2020-01-01', period_start))+1) as total_amount from sales) p
  where total_amount>0)

select a.product_id, b.product_name, a.report_year, a.total_amount
from cte a left join product b on 
a.product_id=b.product_id
order by 1,3