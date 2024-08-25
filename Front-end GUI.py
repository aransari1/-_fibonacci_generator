import flet as ft
from flet import TextField, ElevatedButton, Text, Row, Column
from flet_core.control_event import ControlEvent

def Main_Function (page: ft.Page) -> None:
    page.title = "Fibonacci Generator"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window.width = 400
    page.window.height = 600
    #page.theme_mode = 'light'

    User_Range: TextField = TextField(value='1', text_align=ft.TextAlign.CENTER, width=70)
    
    def Decrement_Function(e: ControlEvent) -> None:
        User_Range.value = str(int(User_Range.value) - 1 )
        page.update()

    def Increment_Function(e: ControlEvent) -> None:
        User_Range.value = str(int(User_Range.value) + 1 )
        page.update()
    

    page.add(
        ft.Row(
                [
                    ft.IconButton(ft.icons.REMOVE, on_click=Decrement_Function),
                    User_Range,
                    ft.IconButton(ft.icons.ADD, on_click=Increment_Function)
                ],
                    alignment=ft.MainAxisAlignment.CENTER
              )
            )

if __name__ == '__main__':
    ft.app(target=Main_Function)
    #ft.app(target=Main_Function, view=ft.WEB_BROWSER)
    