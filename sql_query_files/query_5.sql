--query 5
SELECT subject_name, t.first_name, t.last_name
FROM subjects AS sub
JOIN teachers AS t ON sub.teacher_id = t.teacher_id;