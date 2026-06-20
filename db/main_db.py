import sqlite3
from db import queries
from config import path_db

def init_db():
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.task_table)
    conn.commit()
    conn.close()

def add_task(task):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.insert_task, (task, ))
    conn.commit()
    task_id = cursor.lastrowid
    conn.close()
    return task_id

def update_task(task_id, new_task=None, completed=None):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    if new_task is not None:
        cursor.execute(queries.update_tasks, (new_task, task_id))
    elif completed is not None:
        cursor.execute(queries.update_completed, (completed, task_id))
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
    tasks = cursor.fetchall()
    conn.close()
    return tasks

def delete_task(task_id):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.delete_tasks, (task_id, ))
    conn.commit()
    conn.close()

def delete_completed_tasks():
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.delete_completed)
    conn.commit()
    conn.close()


    
    