
select
x.student_id,
x.student_name,
x.subject_name,
sum(case when c.student_id is NULL then 0 else 1 end) as attended_exams
from
(select 
    a.*, b.subject_name
from students a
cross join subjects b
) x
left join examinations c
on c.student_id = x.student_id and c.subject_name = x.subject_name
group by x.student_id,x.student_name,x.subject_name
order by student_id,subject_name;