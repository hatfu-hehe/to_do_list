# CRUD
task_table = """
    CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT NOT NULL,
    completed INTEGER DEFAULT 0
    )
"""
# Create
insert_task = 'INSERT INTO tasks (task) VALUES (?)'
# Read
select_tasks = 'SELECT * FROM tasks'
select_tasks_completed = "SELECT id, task, completed FROM tasks WHERE completed = 1"
select_tasks_uncompleted = "SELECT id, task, completed FROM tasks WHERE completed = 0"
# Update
update_tasks = 'UPDATE tasks SET task = ? WHERE id = ?'
update_completed = 'UPDATE tasks SET completed = ? WHERE id = ?'
# Delete
delete_tasks = 'DELETE FROM tasks WHERE id = ?'
delete_completed = 'DELETE FROM tasks WHERE completed = 1'