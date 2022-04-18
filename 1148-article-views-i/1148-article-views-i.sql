# Write your MySQL query statement below
select 
distinct
a.author_id as id
from 
views a
where a.viewer_id = a.author_id
order by 1
;