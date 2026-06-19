import sqlite3
from db import queries
from config import path_db


def init_db():
    conn = sqlite3.connect(path_db)       # Соединение к БД
    cursor = conn.cursor()                # Исполнитель который относит запросы к БД
    cursor.execute(queries.task_table)    # Принимает сам запрос в виде строки
    conn.commit()
    conn.close()


def add_task(task):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()   # () - это методы которые "живут" внутри обьекта
    cursor.execute(queries.insert_task, (task, ))
    conn.commit()
    task_id = cursor.lastrowid  # это атрибут или параметр который храниться внтури обьекта
    conn.close()
    return task_id


def update_task(task_id, new_task):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()  
    # тут строго последовательно
    cursor.execute(queries.update_task, (new_task, task_id))
    conn.commit()
    conn.close()


def get_tasks(filter_type):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    if filter_type == 'all':
        cursor.execute(queries.select_tasks)
    elif filter_type == 'completed':
        cursor.execute(queries.select_tasks_completed)
    elif filter_type == 'uncompleted':
        cursor.execute(queries.select_tasks_uncompleted)
    
    tasks = cursor.fetchall()   # all - все, many - несколько
    conn.close()
    return tasks
    
    