import flet as ft


def main(page: ft.Page):
    page.title = "Todo Today"
    page.theme_mode = ft.TemeMode.LIGHT
    page.window.width = 400
    page.window.height = 400
    page.window.top = 200
    page.window.left = 200
    page.padding = 30

    new_task = ft.TextField(hint_text="今日しなくてはいけないことをメモ",
                            expanded=True)
    tasks_ft = ft.Column()

    def add_clicked(e):
        task = ft.Container(
            ft.Row(
                ft.Checkbox(label=new_task.value),
            )
        ),
    alignment= ft.alignment.center,
    width=400,
    height=50,
    bgcolor=ft.Colors.AMBER,
    border_radius=ft.border_radius.all(5),
    )
    tasks_view.controls.append(task)
    new_task.value = "",
    view.update()

    view = ft.Column(
    [
        ft.Row[
            new_task,
            ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=add_clicked),
        ],
    ),
    tasks_view,
    ],
    width=400,
)
    page
ft.app(target=main)
