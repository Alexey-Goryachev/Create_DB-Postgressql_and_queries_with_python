import psycopg2
from psycopg2 import Error

def add_sql_1(sql):
    try:
        with psycopg2.connect(user="postgres", password="qwerty", host="127.0.0.1", port="5432", database="postgres_db") as connection:
            cursor = connection.cursor()
            cursor.execute(sql)
            return cursor.fetchall()
    except Error as error:
        print(error)

sql = '''SELECT s.first_name, s.last_name, sub.subject_name, round(avg(grade), 2) AS average_grade, t.first_name, t.last_name
FROM students AS s 
JOIN student_grades AS sg ON s.student_id = sg.student_id 
JOIN subjects AS sub ON sg.subject_id = sub.subject_id
JOIN teachers AS t ON sub.teacher_id = t.teacher_id 
GROUP BY sub.subject_name, s.first_name, s.last_name, t.first_name, t.last_name
ORDER BY s.first_name;'''        

print(add_sql_1(sql))