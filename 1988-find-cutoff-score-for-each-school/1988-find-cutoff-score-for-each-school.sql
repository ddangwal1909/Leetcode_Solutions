# Write your MySQL query statement below


select T.school_id ,
coalesce(U.score,-1) as score
from schools T
left join (
select * from (
select 
a.*,
row_number() over (partition by school_id order by score) as rnk
from
(
select school_id, capacity, score,student_count,
case when capacity>=student_count then 1 else 0 end as flag
from schools,exam
) a
where flag=1 
) b where rnk=1) U
on T.school_id = U.school_id;
