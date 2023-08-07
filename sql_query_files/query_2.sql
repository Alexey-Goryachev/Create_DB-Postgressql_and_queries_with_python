--query 2
SELECT sub.subject_name, s.first_name, s.last_name, round(avg(sg.grade), 2) AS average_grade  
FROM students AS s
JOIN student_grades AS sg ON s.student_id = sg.student_id
JOIN subjects AS sub ON sg.subject_id = sub.subject_id
GROUP BY sg.subject_id, s.first_name, s.last_name, sub.subject_name, sg.student_id, sg.grade_id 
ORDER BY average_grade DESC, s.first_name DESC, sub.subject_name DESC 
LIMIT 7;


SELECT subject_name, average_grade, first_name, last_name
FROM (
    SELECT 
        sub.subject_name, 
        round(avg(sg.grade), 2) AS average_grade, 
        s.first_name, 
        s.last_name,
        ROW_NUMBER() OVER (PARTITION BY sub.subject_id ORDER BY avg(sg.grade) DESC) AS row_num
    FROM subjects AS sub
    JOIN student_grades AS sg ON sub.subject_id = sg.subject_id 
    JOIN students AS s ON sg.student_id = s.student_id 
    GROUP BY sg.subject_id, sub.subject_name, s.first_name, s.last_name, sub.subject_id
) AS ranked_data
WHERE row_num = 1
ORDER BY subject_name;
