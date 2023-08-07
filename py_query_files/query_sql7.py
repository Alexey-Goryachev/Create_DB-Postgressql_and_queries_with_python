import psycopg2
from psycopg2 import Error

def sql_7(sql):
    try:
        with psycopg2.connect(user="postgres", password="qwerty", host="127.0.0.1", port="5432", database="postgres_db") as connection:
            cursor = connection.cursor()
            cursor.execute(sql)
            return cursor.fetchall()
    except Error as error:
        print(error)

sql = '''SELECT s.first_name, s.last_name , g.group_name, sub.subject_name, sg.grade
FROM students AS  s 
JOIN "groups" AS g ON s.group_id = g.group_id
JOIN  student_grades AS sg ON s.student_id = sg.student_id 
JOIN  subjects AS sub ON sg.subject_id = sub.subject_id 
ORDER BY g.group_name, sub.subject_name;'''        

print(sql_7(sql))