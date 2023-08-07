--query 7
SELECT s.first_name, s.last_name , g.group_name, sub.subject_name, sg.grade
FROM students AS  s 
JOIN "groups" AS g ON s.group_id = g.group_id
JOIN  student_grades AS sg ON s.student_id = sg.student_id 
JOIN  subjects AS sub ON sg.subject_id = sub.subject_id 
ORDER BY g.group_name, sub.subject_name;