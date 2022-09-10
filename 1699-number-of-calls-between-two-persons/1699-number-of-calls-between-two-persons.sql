# Write your MySQL query statement below

select 
person1,
person1+diff as person2,
call_count,
total_duration
from(
select 
case when from_id<to_id then from_id else to_id end as person1,
abs(from_id-to_id) as diff,
count(*) as call_count , 
sum(duration) as total_duration
from calls
group by 1,2
) a;