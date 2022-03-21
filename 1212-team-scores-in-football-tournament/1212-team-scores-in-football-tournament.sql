# Write your MySQL query statement below




select team_id,team_name,coalesce(b.points_guest,0)+coalesce(c.points_host,0) as num_points
from
teams a
left join 
(
select guest_team, sum(case when guest_goals>host_goals then 3 when guest_goals=host_goals then 1 else 0 end) as points_guest
from matches
group by 1
) b
on a.team_id = b.guest_team
left join
(
select host_team, sum(case when host_goals>guest_goals then 3 when host_goals=guest_goals then 1 else 0 end) as points_host
from matches
group by 1
) c
on a.team_id = c.host_team
order by num_points desc, team_id asc
;