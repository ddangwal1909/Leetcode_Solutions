# Write your MySQL query statement below


select country_name,case when avg_weather<=15.0 then 'Cold' when avg_weather>=25.0 then 'Hot' else 'Warm' end as weather_type
from (
select country_name,round(avg(round(weather_state,2)),2) as avg_weather
from countries a
inner join ( select * from weather where day>='2019-11-01' and day<='2019-11-30') b
on a.country_id = b.country_id
group by 1
)
a;