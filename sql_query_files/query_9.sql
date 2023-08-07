--query 9
SELECT s.first_name, s.last_name, sub.subject_name
FROM students AS s 
JOIN student_grades AS sg ON s.student_id = sg.student_id 
JOIN subjects AS sub ON sg.subject_id = sub.subject_id
ORDER BY s.first_name;