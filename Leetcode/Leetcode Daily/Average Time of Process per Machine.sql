# Write your MySQL query statement belew
SELECT 
    A.machine_id, A.process_id, A.activity_type, A.timestamp,
    B.machine_id, B.process_id, B.activity_type, B.timestamp
    -- ROUND(AVG(B.timestamp - A.timestamp),3) AS processing_time
FROM 
    Activity A
JOIN 
    Activity B 
    ON A.machine_id = B.machine_id 
    AND A.process_id = B.process_id
    AND A.activity_type = 'start'
    AND B.activity_type = 'end'
-- GROUP BY 
--     A.machine_id;