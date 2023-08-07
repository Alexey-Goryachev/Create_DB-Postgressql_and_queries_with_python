import psycopg2
from psycopg2 import Error

def sql_6(sql):
    try:
        with psycopg2.connect(user="postgres", password="qwerty", host="127.0.0.1", port="5432", database="postgres_db") as connection:
            cursor = connection.cursor()
            cursor.execute(sql)
            return cursor.fetchall()
    except Error as error:
        print(error)

sql = '''SELECT s.first_name, s.last_name , g.group_name
FROM students AS  s 
JOIN "groups" AS g ON s.group_id = g.group_id
ORDER BY g.group_name;'''        

print(sql_6(sql))