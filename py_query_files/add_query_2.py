import psycopg2
from psycopg2 import Error

def add_sql_2(sql):
    try:
        with psycopg2.connect(user="postgres", password="qwerty", host="127.0.0.1", port="5432", database="postgres_db") as connection:
            cursor = connection.cursor()
            cursor.execute(sql)
            return cursor.fetchall()
    except Error as error:
        print(error)

sql = '''SELECT s.first_name, s.last_name, g.group_name, sub.subject_name, sg.grade, sg.date_received 
FROM students AS s 
JOIN "groups" AS g ON s.group_id = g.group_id
JOIN student_grades AS sg ON s.student_id = sg.student_id 
JOIN subjects AS sub ON sg.subject_id = sub.subject_id 
JOIN (
    SELECT subject_id, MAX(date_received) AS max_date
    FROM student_grades
    GROUP BY subject_id
) AS max_dates ON sg.subject_id = max_dates.subject_id AND sg.date_received = max_dates.max_date
ORDER BY sg.date_received DESC, sub.subject_name;'''        

print(add_sql_2(sql))