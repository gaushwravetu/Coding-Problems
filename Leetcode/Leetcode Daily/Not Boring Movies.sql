# Write your MySQL query statement below
SELECT *
FROM Cinema c
Where c.id % 2 = 1 AND c.description != 'boring'
ORDER BY c.rating DESC;