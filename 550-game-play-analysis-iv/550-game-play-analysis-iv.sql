with cte as (select player_id, min(event_date) over(partition by player_id) + 1= event_date as is_return from activity)
select round(sum(is_return)/count(distinct player_id), 2)  as fraction from cte