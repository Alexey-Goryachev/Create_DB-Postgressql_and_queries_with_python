import psycopg2
from psycopg2 import Error

def sql_1(sql):
    try:
        with psycopg2.connect(user="postgres", password="qwerty", host="127.0.0.1", port="5432", database="postgres_db") as connection:
            cursor = connection.cursor()
            cursor.execute(sql)
            return cursor.fetchall()
    except Error as error:
        print(error)

sql = '''SELECT s.first_name, s.last_name,  ROUND(AVG(sg.grade), 2) AS average_grade, sg.student_id 
FROM  students AS s
LEFT JOIN student_grades AS sg ON s.student_id = sg.student_id 
WHERE sg.student_id IS NOT NULL 
GROUP BY sg.student_id , s.first_name , s.last_name 
ORDER BY average_grade DESC 
LIMIT 5;'''        

print(sql_1(sql))
