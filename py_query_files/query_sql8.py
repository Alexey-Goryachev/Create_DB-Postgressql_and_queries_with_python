import psycopg2
from psycopg2 import Error

def sql_8(sql):
    try:
        with psycopg2.connect(user="postgres", password="qwerty", host="127.0.0.1", port="5432", database="postgres_db") as connection:
            cursor = connection.cursor()
            cursor.execute(sql)
            return cursor.fetchall()
    except Error as error:
        print(error)

sql = '''SELECT subject_name, t.first_name, t.last_name, round(avg(sg.grade), 2) AS average_grade 
FROM subjects AS sub
JOIN teachers AS t ON sub.teacher_id = t.teacher_id
JOIN student_grades AS sg ON sub.subject_id = sg.subject_id
GROUP BY sub.subject_name, t.first_name, t.last_name
ORDER BY sub.subject_name;'''        

print(sql_8(sql))