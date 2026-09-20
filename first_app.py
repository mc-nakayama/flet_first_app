import flet as ft #Fletライブラリをインポート

# Fletは必ずmain関数を定義する必要あり
def main(page: ft.Page):
    page.title = "First App"
    page.window_width = 160
    page.windwow_height = 200
    page.window_top = 100
    page.window_left = 100

    def buttton_clicked(e):
        txt.value = "ボタンがクリックされました"
        txt.update()

    # btn = ft.CupertinoFilledButton(
    #     text="クリックしてください",
    #     on_click=buttton_clicked,
    # )
    btn = ft.ElevatedButton(
        text="クリックしてください",
        on_click=buttton_clicked,
    )

    txt =  ft.Text()

    page.add(btn, txt)

ft.app(target=main)
