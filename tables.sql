-- Таблица групп
CREATE TABLE IF NOT EXISTS groups (
    group_id SERIAL PRIMARY KEY ,
    group_name VARCHAR(50),
    faculty VARCHAR(50)    
);

-- Таблица студентов
CREATE TABLE IF NOT EXISTS students (
    student_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    group_id INTEGER,
    FOREIGN KEY (group_id) REFERENCES groups(group_id)
);

--Таблица преподавателей
CREATE TABLE IF NOT EXISTS teachers (
    teacher_id SERIAL PRIMARY KEY ,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100)
);

--Таблица предметов
CREATE TABLE IF NOT EXISTS subjects (
    subject_id SERIAL PRIMARY KEY ,
    subject_name VARCHAR(100),
    teacher_id INTEGER,
    FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id)
);

--Таблица оценок студентов
CREATE TABLE IF NOT EXISTS student_grades (
    grade_id SERIAL PRIMARY KEY ,
    student_id INTEGER,
    subject_id INTEGER,
    grade INTEGER,
    date_received DATE,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (subject_id) REFERENCES subjects(subject_id)
);
