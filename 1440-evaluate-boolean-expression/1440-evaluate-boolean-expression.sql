# Write your MySQL query statement below

select

a.left_operand, a.operator, a.right_operand,
case 
    when operator='=' and b.value=c.value then 'true'
    when operator='=' and b.value<>c.value then 'false'
    when operator='<' and b.value<c.value then 'true'
    when operator='<' and b.value>=c.value then 'false'
    when operator='>' and b.value>c.value then 'true'
    when operator='>' and b.value<=c.value then 'false'
    else 'false' end as value
from
expressions a
left join variables b
on a.left_operand = b.name
left join variables c
on a.right_operand = c.name;