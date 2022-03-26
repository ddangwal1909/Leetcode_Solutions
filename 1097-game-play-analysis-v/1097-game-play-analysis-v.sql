# Write your MySQL query statement below


with install_dates as 
(   
    select * from (
    select player_id, event_date, row_number () over (partition by player_id order by event_date) as rnk
        from activity
                    ) A where rnk=1
),
retention as
(
    select a.*, case when b.player_id then 1 else 0 end as retention 
    from install_dates a
    left join activity b
    on a.player_id = b.player_id and datediff(b.event_date,a.event_date)=1
),
aggregate as
( select event_date as install_dt, count(distinct player_id) as installs, round(sum(retention)/count(distinct player_id),2) as Day1_retention 
    from retention 
    group by 1
)
select * from aggregate;

