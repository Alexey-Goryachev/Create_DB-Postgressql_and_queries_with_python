--query 8
SELECT subject_name, t.first_name, t.last_name, round(avg(sg.grade), 2) AS average_grade 
FROM subjects AS sub
JOIN teachers AS t ON sub.teacher_id = t.teacher_id
JOIN student_grades AS sg ON sub.subject_id = sg.subject_id
GROUP BY sub.subject_name, t.first_name, t.last_name
ORDER BY sub.subject_name;