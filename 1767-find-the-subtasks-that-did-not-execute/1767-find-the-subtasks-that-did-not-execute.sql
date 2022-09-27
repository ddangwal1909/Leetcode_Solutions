# Write your MySQL query statement below

with recursive cte as (
select 1 as n
union
select n+1 from cte 
where n<=19
),
cte1 as (
select a.task_id,
b.n as taskno
from tasks a, cte b
where b.n<=a.subtasks_count
),
cte3 as (
select 
a.task_id,
a.taskno as subtask_id,
case when b.subtask_id is NULL then 1 else 0 end as flag
from cte1 a
left join executed b
on a.task_id=b.task_id and a.taskno=b.subtask_id
)
select 
task_id,
subtask_id
from 
cte3
where flag=1;

