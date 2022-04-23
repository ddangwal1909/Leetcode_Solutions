# Write your MySQL query statement below

select * from (
select 
name, b.amount as BALANCE from 
users a
left join (select account, sum(amount) as amount from transactions group by 1) b
on a.account = b.account
) c where c.BALANCE>10000;