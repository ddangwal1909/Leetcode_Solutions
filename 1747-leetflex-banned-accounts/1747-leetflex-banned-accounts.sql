# Write your MySQL query statement below

select 
distinct account_id
from
(select a.*, 
lead(ip_address,1,NULL) over (partition by account_id order by login) as nxt_ip,
lead(login,1,NULL) over (partition by account_id order by login) as nxt_login,
lead(logout,1,NULL) over (partition by account_id order by login) as nxt_logout
from
loginfo a
) b
where 
nxt_ip is not NULL and nxt_ip!=ip_address and nxt_login<=logout;