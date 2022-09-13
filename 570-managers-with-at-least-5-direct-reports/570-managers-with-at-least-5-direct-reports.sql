# Write your MySQL query statement below

select distinct name
from employee where 
id in (
select 
managerid
from
employee
group by 1
having count(*)>=5
);