import psycopg2
from psycopg2 import Error

def sql_5(sql):
    try:
        with psycopg2.connect(user="postgres", password="qwerty", host="127.0.0.1", port="5432", database="postgres_db") as connection:
            cursor = connection.cursor()
            cursor.execute(sql)
            return cursor.fetchall()
    except Error as error:
        print(error)

sql = '''SELECT subject_name, t.first_name, t.last_name
FROM subjects AS sub
JOIN teachers AS t ON sub.teacher_id = t.teacher_id;'''        

print(sql_5(sql))