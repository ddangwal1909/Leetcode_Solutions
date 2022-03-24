# Write your MySQL query statement below


with tmp as 
(
(
select distinct student_id from(
select student_id,rank() over (partition by exam_id order by score desc) rnk
from
Exam
) A where rnk=1)
union
(
select distinct student_id from(
select student_id, rank() over (partition by exam_id order by score) as rnk
from Exam
) B where rnk=1
)
),
dst_student as 
(select distinct A.student_id,b.student_name from Exam A 
 left join Student b 
 on A.student_id = b.student_id 
)
select
student_id, student_name 
from dst_student 
where student_id not in (select * from tmp) 
order by student_id;