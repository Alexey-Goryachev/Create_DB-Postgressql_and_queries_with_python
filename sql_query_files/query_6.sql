--query 6
SELECT s.first_name, s.last_name , g.group_name
FROM students AS  s 
JOIN "groups" AS g ON s.group_id = g.group_id
ORDER BY g.group_name;
