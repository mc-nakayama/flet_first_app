import flet as ft

def main(page: ft.Page):
    page.title = "First App"
    page.window_width = 320
    page.windwow_height = 300
    page.window_top = 200
    page.window_left = 200

    def buttton_clicked(e):
        txt.value = "ボタンがクリックされました"
        txt.update()

    btn = ft.CupertinoFilledButton(
        text="クリックしてください",
        on_click=buttton_clicked,
    )

    txt =  ft.Text()

    page.add(btn, txt)

ft.app(target=main)
