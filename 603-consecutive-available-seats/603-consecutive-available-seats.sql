# Write your MySQL query statement below


select seat_id from (
select seat_id, 
case when next_free=1 and prev_free=1 and free=1 then 1
when next_free=1 and prev_free=0 and free=1 then 1
when prev_free=1 and next_free=0 and free=1 then 1
else 0 end as flag
from (
select seat_id, 
free,
case when lead(free,1,0) over (order by seat_id) = 1 then 1 else 0 end as next_free,
case when lag(free,1,0) over (order by seat_id) = 1 then 1 else 0 end as prev_free
from cinema
) a
) res where flag=1
order by seat_id
;