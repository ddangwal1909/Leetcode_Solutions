SELECT ROUND(SUM(dailyavg)/ COUNT(*) *100,2) AS average_daily_percent
FROM
    (
        SELECT a.action_date, COUNT(DISTINCT  r.post_id) / COUNT(DISTINCT a.post_id) AS dailyavg
        FROM Actions a
        LEFT JOIN Removals r
            ON a.post_id=r.post_id
        WHERE action='report'
        AND extra LIKE 'spam'
        GROUP BY a.action_date
    ) t