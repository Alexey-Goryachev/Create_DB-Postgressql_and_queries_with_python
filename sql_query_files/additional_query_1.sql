--additional_query_1.sql
SELECT s.first_name, s.last_name, sub.subject_name, round(avg(grade), 2) AS average_grade, t.first_name, t.last_name
FROM students AS s 
JOIN student_grades AS sg ON s.student_id = sg.student_id 
JOIN subjects AS sub ON sg.subject_id = sub.subject_id
JOIN teachers AS t ON sub.teacher_id = t.teacher_id 
GROUP BY sub.subject_name, s.first_name, s.last_name, t.first_name, t.last_name
ORDER BY s.first_name;