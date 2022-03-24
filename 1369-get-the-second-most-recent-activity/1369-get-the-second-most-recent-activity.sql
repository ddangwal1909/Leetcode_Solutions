# Write your MySQL query statement below


with cte as (
select a.*,dense_rank() over (partition by username order by startDate desc) as rnk
from
UserActivity a
),
inclusions as
(select username, max(rnk) as rnk_mx from cte
group by username
having rnk_mx=1
)
, combined as (
    
(select b.* from inclusions a left join UserActivity b on a.username = b.username)
    
union
    
( select username, activity, startDate, endDate from cte where rnk=2)
)
select * from combined;
