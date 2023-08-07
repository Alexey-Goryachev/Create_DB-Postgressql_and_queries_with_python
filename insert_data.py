from datetime import datetime
import faker
import psycopg2
from random import randint
from psycopg2 import Error

#переменные константы для создания БД
NUMBER_STUDENTS = 30
NUMBER_GROUPS = 3
NUMBER_TEACHERS = 5
NUMBER_SUBJECTS = 5
NAME_GROUPS = ['First', 'Second', 'Third']
FACULTY = 'Engeneering'
NAME_SUBJECTS = ['Математика', 'Фізика', 'Программування', 'Англійська мова', 'Українська мова']

#функция подготовки данных для вставки в БД
def prepare_data(students, groups, teachers, subjects):
    fake_data = faker.Faker('uk-UA')
    for_students = []
    for_groups = []
    for_teachers = []
    for_subjects = []
    for_student_grades = []

    for _ in range(students):
        for_students.append((fake_data.first_name(), fake_data.last_name(), fake_data.email(),randint(1, NUMBER_GROUPS)))
    
    for gr in groups:
        for_groups.append((gr, FACULTY))
    
    for _ in range(teachers):
        for_teachers.append((fake_data.first_name(), fake_data.last_name(), fake_data.email()))

    for sub in subjects:
        for_subjects.append((sub, subjects.index(sub) + 1))
        
    for _ in range(students):
        data_received = datetime(2023, randint(1, 6), randint(1, 27)).date()
        for_student_grades.append((randint(1, NUMBER_STUDENTS), randint(1, NUMBER_SUBJECTS), randint(1, 5), data_received))

    return for_students, for_groups, for_teachers, for_subjects, for_student_grades


#функция для вставки данных в таблицы БД
def insert_data_to_db(students, groups, teachers, subjects, student_grades):
    try:
        with psycopg2.connect(user="postgres", password="qwerty", host="127.0.0.1", port="5432", database="postgres_db") as connection:
            cursor = connection.cursor()
            sql_to_groups = '''INSERT INTO groups(group_name, faculty) VALUES (%s, %s)'''
            cursor.executemany(sql_to_groups, groups)

            sql_to_students = '''INSERT INTO students(first_name, last_name, email, group_id) VALUES (%s, %s, %s, %s)'''
            cursor.executemany(sql_to_students, students)

            sql_to_teachers = '''INSERT INTO teachers(first_name, last_name, email) VALUES (%s, %s, %s)'''
            cursor.executemany(sql_to_teachers, teachers)

            sql_to_subjects = '''INSERT INTO subjects(subject_name, teacher_id) VALUES (%s, %s)'''
            cursor.executemany(sql_to_subjects, subjects)

            sql_to_sudent_grades = '''INSERT INTO student_grades(student_id, subject_id, grade, date_received) VALUES (%s, %s, %s, %s)'''
            cursor.executemany(sql_to_sudent_grades, student_grades)        

            connection.commit()
    except Error as error:
        print(error)


if __name__ == '__main__':
    students, groups, teachers, subjects, student_grades = prepare_data(NUMBER_STUDENTS, NAME_GROUPS, NUMBER_TEACHERS, NAME_SUBJECTS)
    insert_data_to_db(students, groups, teachers, subjects, student_grades)
  