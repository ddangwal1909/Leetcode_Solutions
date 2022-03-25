# Write your MySQL query statement below


select round(avg(num),1) as median from
(
select a.*, lag(end_range,1,0) over (order by num) as start_range from
(
select num, frequency,sum(frequency) over (order by num rows between unbounded preceding and current row) end_range
from Numbers
order by num
) A
) B where ((select sum(frequency) from numbers)/2) between start_range and end_range
;