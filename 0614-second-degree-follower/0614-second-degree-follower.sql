# Write your MySQL query statement below

with cte as
(
select 
follower
from 
follow
group by 1
)
select
a.followee as follower,
count(*) as num
from
follow a
inner join cte b
on a.followee = b.follower
group by 1
order by 1;


