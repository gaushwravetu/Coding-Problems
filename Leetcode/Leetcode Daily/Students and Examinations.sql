# Write your MySQL query statement below
-- SELECT S.student_id, S.student_name, E.subject_name
-- FROM Students S
-- RIGHT JOIN Examinations E ON S.student_id=E.student_id;

WITH all_combinations AS (
    SELECT S.student_id, S.student_name, Sub.subject_name
    FROM Students S
    CROSS JOIN Subjects Sub
),
exam_counts AS (
    SELECT student_id, subject_name, COUNT(*) AS attended_exams
    FROM Examinations
    GROUP BY student_id, subject_name
)
SELECT 
    all_combinations.student_id,
    all_combinations.student_name,
    all_combinations.subject_name,
    COALESCE(exam_counts.attended_exams, 0) AS attended_exams
FROM 
    all_combinations
LEFT JOIN 
    exam_counts ON all_combinations.student_id = exam_counts.student_id
                AND all_combinations.subject_name = exam_counts.subject_name
ORDER BY 
    all_combinations.student_id, all_combinations.subject_name;

