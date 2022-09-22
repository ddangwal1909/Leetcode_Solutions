# Write your MySQL query statement below

select min(log_id) as  start_id , max(log_id) as end_id
from (
select log_id, log_id-rnk as diff
from
(select log_id,
dense_rank() over (order by log_id) as rnk
from 
logs
) res
) final group by diff;