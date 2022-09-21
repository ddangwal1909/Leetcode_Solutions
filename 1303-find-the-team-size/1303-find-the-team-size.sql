# Write your MySQL query statement below
with cte as (
select team_id,count(*) as team_size 
from employee
group by 1
) 
select employee_id,b.team_size
from employee a
left join cte b
on a.team_id = b.team_id;