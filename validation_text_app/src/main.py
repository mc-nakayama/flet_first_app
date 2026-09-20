import flet as ft


def main(page: ft.Page):
    page.window.width = 400
    page.window.height = 400

    def submit(e):
        page.add(ft.Text(f"電話番号は: {field1.value}"))
        page.add(ft.Text(f"住所は: {field2.value}"))

    field1 = ft.TextField(
        label= "電話番号を入力してください（13文字以内）：",
        suffix=ft.ElevatedButton("Submit", on_click=submit),
        keyboard_type=ft.KeyboardType.NUMBER,
        on_submit=submit,
        max_length=13,
        input_filter=ft.InputFilter(
            allow = True,
            regex_string= r"^[0-9-]*$",
            replacement_string=""
        ),
    )
    field2 = ft.TextField(
        label="住所を20文字以内で入力してください",
        suffix=ft.ElevatedButton("Submit", on_click=submit),
        keyboard_type=ft.KeyboardType.TEXT,
        on_submit=submit,
        max_length=20
    )

    page.add(field1)
    page.add(field2)

ft.app(target=main)
