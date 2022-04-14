# Write your MySQL query statement below


select name as customers from 
customers 
where id not in (
select 
a.id 
from customers a
inner join orders b
on a.id = b.customerid
);


