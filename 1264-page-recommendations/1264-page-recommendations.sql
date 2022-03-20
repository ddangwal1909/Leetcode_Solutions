# Write your MySQL query statement below

select recommended_page from 
(
(select
distinct
b.page_id as recommended_page
from
(select 
user1_id,
user2_id
from 
Friendship 
where user2_id=1
) a
left join 
(select 
* from 
likes where user_id<>1
) b
on a.user1_id = b.user_id
order by recommended_page
)

union
(
select
distinct
b.page_id as recommended_page
from
(select 
user1_id,
user2_id
from 
Friendship 
where user1_id=1
) a
left join 
(select 
* from 
likes where user_id<>1
) b
on a.user2_id = b.user_id
order by recommended_page
)
) res
where res.recommended_page is not NULL and res.recommended_page not in (
select distinct page_id from likes where user_id = 1)
;