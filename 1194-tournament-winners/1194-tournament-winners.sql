# Write your MySQL query statement below

with scores as
( 
    select player, sum(score) as tot_points
    from
    (
    (
    select first_player as player, first_score as score
    from matches
    )
    
    union all
    
    (
    select second_player as player, second_score as score
    from matches
    )
    
    ) A
    group by 1
    
),

combined as 
(
    select a.*, b.group_id from scores a left join players b on a.player = b.player_id
),

best_players as
( 
    select group_id, player_id from
    (
    select group_id, player as player_id,row_number() over (partition by group_id order by tot_points desc, player) as rnk 
    from combined )
    A
    where A.rnk=1
)
select * from best_players;



