import psycopg2
from psycopg2 import Error

def sql_2(sql):
    try:
        with psycopg2.connect(user="postgres", password="qwerty", host="127.0.0.1", port="5432", database="postgres_db") as connection:
            cursor = connection.cursor()
            cursor.execute(sql)
            return cursor.fetchall()
    except Error as error:
        print(error)

sql = '''SELECT sub.subject_name, s.first_name, s.last_name, round(avg(sg.grade), 2) AS average_grade  
FROM students AS s
JOIN student_grades AS sg ON s.student_id = sg.student_id
JOIN subjects AS sub ON sg.subject_id = sub.subject_id
GROUP BY sg.subject_id, s.first_name, s.last_name, sub.subject_name, sg.student_id, sg.grade_id 
ORDER BY average_grade DESC, s.first_name DESC, sub.subject_name DESC 
LIMIT 7;'''        

print(sql_2(sql))