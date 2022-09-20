# Write your MySQL query statement below
Select request_at AS Day, ROUND(SUM(IF(status != 'completed', 1,0))/COUNT(*), 2) AS "Cancellation Rate"
From trips
Where
client_id in (Select users_id from Users Where banned = "No") and
driver_id in (Select users_id from Users Where banned = "No") and
request_at between "2013-10-01" and "2013-10-03"
Group By request_at;