# Write your MySQL query statement below


select  
    name,
    sum(coalesce(distance,0)) as travelled_distance
from 
    users a
left join 
    rides b
    on a.id = b.user_id
group by name
order by travelled_distance desc, name






 