# Write your MySQL query statement below

with recursive cte as
(
select a.*, case when b.user_id then txns else 0 end as visited_and_transacted
from
visits a
left join ( select user_id, transaction_date,count(*) as txns from transactions group by 1,2) b
on a.user_id = b.user_id and a.visit_date=b.transaction_date
),
cte2 AS (
SELECT 0 AS transactions_count
UNION ALL
SELECT transactions_count+1 AS transactions_count FROM cte2
WHERE transactions_count+1<=(SELECT MAX(visited_and_transacted) FROM cte)
)
select A.transactions_count,coalesce(B.visits_count,0) as visits_count from cte2 A 
left join ( select visited_and_transacted , count(*) as visits_count from cte group by 1) B
on A.transactions_count = B.visited_and_transacted
order by 1;
