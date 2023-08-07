import psycopg2
from psycopg2 import Error

def sql_4(sql):
    try:
        with psycopg2.connect(user="postgres", password="qwerty", host="127.0.0.1", port="5432", database="postgres_db") as connection:
            cursor = connection.cursor()
            cursor.execute(sql)
            return cursor.fetchall()
    except Error as error:
        print(error)

sql = '''SELECT avg(grade) AS average_grade
FROM student_grades;'''        

print(sql_4(sql))