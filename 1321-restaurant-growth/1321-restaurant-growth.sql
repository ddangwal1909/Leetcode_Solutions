# Write your MySQL query statement below

select 
* from (
select 
    visited_on, 
    round(sum(amount) over (order by visited_on rows between 6 preceding and current row ),2) as amount,
    round(avg(amount) over (order by visited_on rows between 6 preceding and current row ),2) as average_amount
from (select visited_on, sum(amount) as amount from customer group by 1) a
order by visited_on asc
) c
where visited_on>= ( select distinct visited_on from customer order by 1 limit 1 offset 6)
;