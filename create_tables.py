import psycopg2
from psycopg2 import Error


#функиця для создания таблиц в БД
def create_tables():
    with open('tables.sql', 'r') as f:
        sql = f.read()

    try:
        connection = psycopg2.connect(user="postgres",
                                    password="qwerty",
                                    host="127.0.0.1",
                                    port="5432",
                                    database="postgres_db")

        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()
        print("Таблица успешно создана в PostgreSQL")

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с PostgreSQL закрыто")

if __name__=='__main__':
    create_tables()
