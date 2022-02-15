# Write your MySQL query statement below

select 
    a.name
    from employee a
    inner join employee b
    on a.id = b.managerid
    group by 1
    having count(*)>=5;