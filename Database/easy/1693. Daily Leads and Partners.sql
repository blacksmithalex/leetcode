# Write your MySQL query statement below
SELECT 
    date_id,
    make_name, 
    COUNT(distinct lead_id) as unique_leads,
    COUNT(distinct partner_id) as unique_partners
FROM 
    DailySales
GROUP BY
    date_id,
    make_name;