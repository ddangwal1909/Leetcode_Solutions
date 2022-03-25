# Write your MySQL query statement below

with cte as (
select 
    concat(substr(pay_date,1,4),'-',substr(pay_date,6,2)) as pay_month,
    a.*,
    b.department_id
    from salary a
    left join employee b
    on a.employee_id = b.employee_id
),
cte2 as(
select
    pay_month,
    department_id, 
    case 
        when avg(amount) over (partition by pay_month) > avg(amount) over (partition by pay_month, department_id) then 'lower'
        when avg(amount) over (partition by pay_month) <  avg(amount) over (partition by pay_month, department_id) then 'higher'
    else 'same' end as comparison
from cte
)
select distinct a.* from cte2 a