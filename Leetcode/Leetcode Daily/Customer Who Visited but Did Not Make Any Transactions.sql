# Write your MySQL query statement below
WITH T AS (
    SELECT Visits.customer_id
    FROM Visits
    LEFT JOIN Transactions ON Visits.visit_id = Transactions.visit_id
    WHERE Transactions.transaction_id IS NULL
)
SELECT customer_id, COUNT(customer_id) AS count_no_trans
FROM T
GROUP BY customer_id