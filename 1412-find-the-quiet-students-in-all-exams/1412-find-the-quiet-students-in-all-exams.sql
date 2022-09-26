# Write your MySQL query statement below

with cte as (
select 
student_id,
rank() over (partition by exam_id order by score) as rnk_asc,
rank() over (partition by exam_id order by score desc) as rnk_desc
from exam
),
cte1 as
(select 
student_id, 
min(rnk_asc) as rnk_asc,
min(rnk_desc) as rnk_desc
from
 cte
 group by 1
)
select 
a.student_id, 
a.student_name
from 
student a
inner join (select distinct student_id from cte1 where rnk_asc<>1 and rnk_desc<>1) b
on a.student_id=b.student_id
order by 1;
