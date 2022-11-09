# Write your MySQL query statement below



select 
id,
case when Jan_revenue =0 then NULL else Jan_revenue end as Jan_Revenue,
case when Feb_revenue =0 then NULL else Feb_revenue end as Feb_Revenue,
case when Mar_revenue =0 then NULL else Mar_revenue end as Mar_Revenue,
case when Apr_revenue =0 then NULL else Apr_revenue end as Apr_Revenue,
case when May_revenue =0 then NULL else May_revenue end as May_Revenue,
case when Jun_revenue =0 then NULL else Jun_revenue end as Jun_Revenue,
case when Jul_revenue =0 then NULL else Jul_revenue end as Jul_Revenue,
case when Aug_revenue =0 then NULL else Aug_revenue end as Aug_Revenue,
case when Sep_revenue =0 then NULL else Sep_revenue end as Sep_Revenue,
case when Oct_revenue =0 then NULL else Oct_revenue end as Oct_Revenue,
case when Nov_revenue =0 then NULL else Nov_revenue end as Nov_Revenue,
case when Dec_revenue =0 then NULL else Dec_revenue end as Dec_Revenue
from
(
select 
id,
sum(case when month='Jan' then revenue else 0 end) as Jan_revenue,
sum(case when month='Feb' then revenue else 0 end) as Feb_revenue,
sum(case when month='Mar' then revenue else 0 end) as Mar_revenue,
sum(case when month='Apr' then revenue else 0 end) as Apr_revenue,
sum(case when month='May' then revenue else 0 end) as May_revenue,
sum(case when month='Jun' then revenue else 0 end) as Jun_revenue,
sum(case when month='Jul' then revenue else 0 end) as Jul_revenue,
sum(case when month='Aug' then revenue else 0 end) as Aug_revenue,
sum(case when month='Sep' then revenue else 0 end) as Sep_revenue,
sum(case when month='Oct' then revenue else 0 end) as Oct_revenue,
sum(case when month='Nov' then revenue else 0 end) as Nov_revenue,
sum(case when month='Dec' then revenue else 0 end) as Dec_revenue
from
Department
group by 1
) res
;