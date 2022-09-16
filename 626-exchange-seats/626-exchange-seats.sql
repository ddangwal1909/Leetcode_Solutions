# Write your MySQL query statement below


select 
case 
when id%2=0 then id-1
when id%2!=0 and id=sum(1) over () then id 
else id+1 end as id,
student
from seat
order by id