import flet as ft
from db import main_db

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    filter_type = 'all'
    task_list = ft.Column()

    def load_tasks():
        task_list.controls.clear()
        for task_id, task_text, completed in main_db.get_tasks(filter_type):
            task_list.controls.append(view_tasks(
                task_id=task_id,
                task_text=task_text,
                completed=completed
            ))
        task_list.update()

    def view_tasks(task_id, task_text, completed=None):
        def toggle_task(task_id, is_completed):
            main_db.update_task(task_id=task_id, completed=int(is_completed))
            load_tasks()

        checkbox = ft.Checkbox(
            value=bool(completed),
            on_change=lambda e: toggle_task(task_id=task_id, is_completed=e.control.value)
        )

        def save_task(e):
            main_db.update_task(task_id=task_id, new_task=task_field.value)
            task_field.read_only = True
            task_field.update()

        def enable_edit(e):
            task_field.read_only = not task_field.read_only
            task_field.update()

        def delete_task(e):
            main_db.delete_task(task_id=task_id)
            task_list.controls.remove(row)
            task_list.update()

        task_field = ft.TextField(read_only=True, value=task_text, expand=True)
        edit_button = ft.IconButton(icon=ft.Icons.EDIT, on_click=enable_edit)
        save_button = ft.IconButton(icon=ft.Icons.SAVE, on_click=save_task)
        delete_button = ft.IconButton(icon=ft.Icons.DELETE, icon_color=ft.Colors.RED_400, on_click=delete_task)

        row = ft.Row([checkbox, task_field, edit_button, save_button, delete_button])
        return row

    def add_task_db(e):
        if task_input.value:
            task = task_input.value
            task_id = main_db.add_task(task=task)
            task_list.controls.append(view_tasks(task_id=task_id, task_text=task))
            task_list.update()
            task_input.value = None
            task_input.update()

    def clear_completed(e):
        main_db.delete_completed_tasks()
        load_tasks()

    clear_button = ft.ElevatedButton(
    'Очистить выполненные',
    icon_color=ft.Colors.RED_400,
    on_click=clear_completed
)

    task_input = ft.TextField(label="Введите задачу", expand=True, on_submit=add_task_db)
    task_button = ft.IconButton(icon=ft.Icons.ADD, on_click=add_task_db)
    send_task = ft.Row([task_input, task_button])

    def set_filter(filter_value):
        nonlocal filter_type
        filter_type = filter_value
        load_tasks()

    filter_buttons = ft.Row([
        ft.ElevatedButton(
            'All tasks', on_click=lambda e: set_filter('all'),
            icon=ft.Icons.ALL_INBOX, icon_color=ft.Colors.BLACK_87
        ),
        ft.ElevatedButton(
            'In a process', on_click=lambda e: set_filter('uncompleted'),
            icon=ft.Icons.WATCH, icon_color=ft.Colors.YELLOW_900, bgcolor=ft.Colors.YELLOW_100
        ),
        ft.ElevatedButton(
            'Done', on_click=lambda e: set_filter('completed'),
            icon=ft.Icons.CHECK_BOX, icon_color=ft.Colors.GREEN_900, bgcolor=ft.Colors.GREEN_100
        ),
    ], alignment=ft.MainAxisAlignment.SPACE_AROUND)

    page.add(send_task, filter_buttons, task_list, clear_button)
    load_tasks()

if __name__ == "__main__":
    main_db.init_db()
    ft.app(main, view=ft.AppView.WEB_BROWSER)
