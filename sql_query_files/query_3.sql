--query 3
SELECT g.group_name, sub.subject_name, round(avg(sg.grade), 2) AS average_grade
FROM students AS s
JOIN "groups" AS g ON s.group_id = g.group_id 
JOIN  student_grades AS sg ON s.student_id = sg.student_id 
JOIN subjects AS sub ON sg.subject_id = sub.subject_id 
GROUP BY sub.subject_name, g.group_name
ORDER BY g.group_name;