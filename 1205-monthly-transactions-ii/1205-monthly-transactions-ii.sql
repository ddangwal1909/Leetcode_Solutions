# Write your MySQL query statement below


select * from 
(
select 
A.month,
A.country,
coalesce(B.approved_count,0) as approved_count,
coalesce(B.approved_amount,0) as approved_amount,
coalesce(D.chargeback_count,0) as chargeback_count,
coalesce(D.chargeback_amount,0) as chargeback_amount
from
((select distinct substr(T.trans_date,1,7) as month, country
 from
transactions T
  )
 union
 
 (select distinct substr(c.trans_date,1,7) as month, b.country
    from chargebacks c
    left join transactions b    
    on c.trans_id = b.id
 )

) A
left join 
(
select 
substr(a.trans_date,1,7) as month, country, 
sum(case when state='approved' then 1 else 0 end ) as approved_count, 
sum(case when state='approved' then amount else 0.0 end) as approved_amount
from 
transactions a
group by 1,2
) B
ON A.month = B.month and A.country = B.country
left join
(
select 
substr(c.trans_date,1,7) as chrg_mnth, 
b.country,
sum(b.amount) as chargeback_amount,
count(*) as chargeback_count
from chargebacks c
left join transactions b
on c.trans_id = b.id
group by 1,2
) D
ON A.month = D.chrg_mnth and A.country = D.country
) res
where not (approved_count=0 and approved_amount=0 and chargeback_count=0 and chargeback_amount=0 )
    
;
