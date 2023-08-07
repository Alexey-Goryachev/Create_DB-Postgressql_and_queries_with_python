--query 1
SELECT s.first_name, s.last_name,  ROUND(AVG(sg.grade), 2) AS average_grade, sg.student_id 
FROM  students AS s
LEFT JOIN student_grades AS sg ON s.student_id = sg.student_id 
WHERE sg.student_id IS NOT NULL 
GROUP BY sg.student_id , s.first_name , s.last_name 
ORDER BY average_grade DESC 
LIMIT 5;