# Write your MySQL query statement below
# Write your MySQL query statement below

WITH
  tmp AS (select a.*,b.name as country
from person a
left join country b
on substr(a.phone_number,1,3) = b.country_code)
,
tmp2  AS 
(
    (
select 
B.country, 
A.duration
from calls A
left join tmp B
on A.caller_id = B.id
    )
union all
    (
select 
B.country, 
A.duration
from calls A
left join tmp B
on A.callee_id = B.id
    )
),
tmp3 as 

(
    select 
    A.country, 
    A.avg_country,
    B.glbl_avg
    from
    (
    select 
        country, 
        sum(duration)/count(*) as avg_country
    from
        tmp2 
    group by 1
    ) A
    cross join (select sum(duration)/count(*) as glbl_avg from tmp2) B
)
select country from tmp3 where avg_country>glbl_avg;